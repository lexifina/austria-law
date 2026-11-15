"""Functional smoke test of a built Austrian / Burgenland law repository. Standard library only.

    python3 -X utf8 tools/test_repo.py --repo ../repo [--record]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shlex
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PUBLISHER = 'RIS (Bundeskanzleramt)'
LAW_EMAIL = re.compile(r'^[a-z0-9.-]+@ris\.invalid$|^ris@ris-bka\.invalid$')


DOC_TOP = ('REPRODUCE.md', 'LICENSE', 'PLAN.md', 'SOURCES.md', '.gitattributes', '.gitignore')
DOC_DIRS = ('data/', 'tools/', 'visualisations/', 'vulnerabilities/', 'registry/', 'monitoring/')


def is_doc_file(path):
    """A file a documentation commit may touch, never law text: README*, REPRODUCE.md, LICENSE, PLAN.md, SOURCES.md,
    *.csv and *.json at the top; anything under data/, tools/, visualisations/, vulnerabilities/, registry/, monitoring/;
    an act folder's README.md (no law text file is named README.md)."""
    if '/' not in path:
        return path.startswith('README') or path in DOC_TOP or path.endswith(('.csv', '.json'))
    return path.startswith(DOC_DIRS) or path.endswith('/README.md')


def doc_commit_problems(repo, rows):
    """rows: (sha, In-force value) of each commit authored by Lexifina. Every one is a documentation commit (README,
    charts, tools): no In-force trailer and no law text file (one git log --no-walk --name-only for all of them)."""
    if not rows:
        return []
    out = subprocess.run(['git', '-c', 'core.quotePath=false', 'log', '--no-walk=unsorted', '--stdin', '--name-only',
                          '--format=%x00%H'], cwd=repo, input=''.join(h + '\n' for h, _ in rows), capture_output=True,
                         text=True, encoding='utf-8')
    if out.returncode:
        raise AssertionError(f'git log --no-walk: {out.stderr.strip()}')
    files = {}
    for block in out.stdout.split('\x00')[1:]:
        lines = [l for l in block.splitlines() if l]
        files[lines[0]] = lines[1:]
    bad = []
    for h, day in rows:
        law = [f for f in files.get(h, []) if not is_doc_file(f)]
        if day.strip() or law:
            bad.append(h[:10] + (f' In-force {day.strip()}' if day.strip() else '')
                       + (f' touches {len(law)} law text file(s), e.g. {law[0]}' if law else ''))
    return bad


class Smoke:
    def __init__(self, repo: Path):
        self.repo = repo
        self.results: list[tuple[str, bool, str]] = []
        self._busy: list[str] | None = None

    def git(self, *args: str) -> str:
        out = subprocess.run(['git', *args], cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'git {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def tool(self, *args: str) -> str:
        out = subprocess.run([sys.executable, 'tools/stand_am.py', *args], cwd=self.repo, capture_output=True, text=True,
                             encoding='utf-8')
        if out.returncode:
            raise AssertionError(f'stand_am {" ".join(args)}: {out.stderr.strip()}')
        return out.stdout

    def check(self, name: str, fn):
        try:
            detail = fn() or ''
            self.results.append((name, True, detail))
            print(f'PASS {name}: {detail}')
        except AssertionError as exc:
            self.results.append((name, False, str(exc)))
            print(f'FAIL {name}: {exc}')
        except Exception as exc:  # any other error fails this check only; the run goes on
            self.results.append((name, False, f'{type(exc).__name__}: {exc}'))
            print(f'FAIL {name}: {type(exc).__name__}: {exc}')

    def law_commits(self, path: str) -> list[tuple[str, str, str, str]]:
        out = self.git('log', '--format=%H%x09%an%x09%ae%x09%(trailers:key=In-force,valueonly,separator=)',
                       'main', '--', path)
        rows = [tuple(x.strip() for x in l.split('\t')) for l in out.splitlines() if l]
        return [r for r in rows if LAW_EMAIL.match(r[2]) and r[2] != 'ris@ris-bka.invalid']

    def busy(self) -> list[str]:
        if self._busy is None:
            counts: dict[str, int] = {}
            out = self.git('log', '--format=%x00%ae', '--name-only', 'main')
            for block in out.split('\x00')[1:]:
                lines = [l for l in block.splitlines() if l]
                if not lines or not LAW_EMAIL.match(lines[0]) or lines[0] == 'ris@ris-bka.invalid':
                    continue
                for f in lines[1:]:
                    if f.endswith('.md') and '/' in f and not f.endswith(('README.md', 'REPRODUCE.md', 'SOURCES.md')):
                        counts[f] = counts.get(f, 0) + 1
            present = set()
            for line in self.git('ls-tree', '-r', '-l', 'main').splitlines():
                if '\t' in line:
                    meta, fname = line.split('\t', 1)
                    parts = meta.split()
                    if len(parts) >= 4 and parts[3].isdigit() and int(parts[3]) > 0:
                        present.add(fname)
            best: dict[str, tuple[int, str]] = {}
            for f, n in sorted(counts.items()):
                if f not in present:
                    continue
                act = f.split('/', 1)[0]
                if n > best.get(act, (0, ''))[0]:
                    best[act] = (n, f)
            self._busy = [f for _, f in sorted(best.values(), key=lambda x: x[1])]
            assert self._busy, 'no file changed by a law'
        return self._busy

    def blame(self):
        done = []
        for path in self.busy():
            out = self.git('blame', '--line-porcelain', 'main', '--', path)
            emails = {l[12:].strip('<>') for l in out.splitlines() if l.startswith('author-mail ')}
            assert emails, f'{path}: no blame output'
            assert all(LAW_EMAIL.match(e) for e in emails), f'{path}: unexpected authors {emails}'
            assert any(e != 'ris@ris-bka.invalid' for e in emails), f'{path}: no law among {emails}'
            done.append(f'{path} lines by {len(emails)} author(s)')
        return '; '.join(done)

    def on_date(self):
        done = []
        for path in self.busy():
            act = path.split('/', 1)[0]
            rows = self.law_commits(path)
            for h, _, _, day in rows:
                before = self.git('log', '-1', '--format=%(trailers:key=In-force,valueonly,separator=)', f'{h}~1').strip()
                if not before or before >= day:
                    continue
                prev_day = (dt.date.fromisoformat(day) - dt.timedelta(days=1)).isoformat()
                spec = path.split('/', 1)[1]
                b = self.tool(day, act, spec)
                want_b = self.git('show', f'{h}:{path}')
                assert b.strip() == want_b.strip(), f'{path} on {day} is not the file at {h[:10]}'
                done.append(f'{path} checked on {day}')
                break
        first_act = self.busy()[0].split('/', 1)[0]
        whole = self.tool(dt.date.today().isoformat(), first_act)
        assert whole.strip(), f'the whole {first_act} today is empty'
        return '; '.join(done)

    def follow(self):
        checked = []
        for path in self.busy():
            rows = self.law_commits(path)
            assert len(rows) >= 1, f'{path}: {len(rows)} law commits'
            days = [r[3] for r in rows]
            assert days == sorted(days, reverse=True), f'{path}: not in date order {days}'
            checked.append(f'{path} {len(rows)} law commits')
        return '; '.join(checked)

    def tags_and_trailers(self):
        tags = self.git('tag').split()
        assert tags, 'no tags'
        for t in tags:
            self.git('rev-parse', '--verify', '-q', f'{t}^{{commit}}')
        rows = self.git('log', '--format=%H%x09%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main').splitlines()
        rows = [r for r in rows if r.split('\t')[1] != 'Lexifina']   # documentation commits (by Lexifina) carry no In-force
        missing = [r for r in rows if not r.split('\t')[2].strip()]
        assert not missing, f'{len(missing)} commits without In-force, e.g. {missing[:2]}'
        bad = [r for r in rows if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r.split('\t')[2].strip())]
        assert not bad, f'malformed In-force {bad[:2]}'
        return f'{len(tags)} tags resolve; {len(rows)} commits carry In-force'

    def lexifina(self):
        rows = self.git('log', '--format=%H%x09%an%x09%ae%x09%cn%x09%(trailers:key=In-force,valueonly,separator=)',
                        'main').splitlines()
        by_lex = [r for r in rows if r.split('\t')[1] == 'Lexifina']
        assert by_lex, 'no documentation commit by Lexifina'
        bad = doc_commit_problems(self.repo, [(r.split('\t')[0], r.split('\t')[4]) for r in by_lex])
        assert not bad, f'{len(bad)} Lexifina commits are not documentation commits, e.g. {bad[:3]}'
        law = [r for r in rows if r.split('\t')[1] != 'Lexifina']
        assert all(r.split('\t')[3] == 'Lexifina' for r in rows), 'a committer other than Lexifina'
        bad = {r.split('\t')[2] for r in law if not LAW_EMAIL.match(r.split('\t')[2])}
        assert not bad, f'unexpected author emails {bad}'
        return f'{len(by_lex)} documentation commits by Lexifina, none with In-force or law text'

    def readme(self):
        text = (self.repo / 'README.en.md').read_text(encoding='utf-8')  # the English README (README.md is German)
        start = text.index('## Questions as git commands')
        table = text[start:text.index('\n## ', start + 1)]
        rows = '\n'.join(l for l in table.splitlines() if l.startswith('|'))
        cmds = [c for c in re.findall(r'`([^`]+)`', rows) if c.startswith(('git ', 'python ')) and '<' not in c]
        assert len(cmds) >= 3, f'only {len(cmds)} commands found'
        for c in cmds:
            args = shlex.split(c)
            if args[0] == 'python':
                args[0] = sys.executable
            out = subprocess.run(args, cwd=self.repo, capture_output=True, text=True, encoding='utf-8')
            assert out.returncode == 0, f'{c}: exit {out.returncode} {out.stderr.strip()[:200]}'
            assert out.stdout.strip(), f'{c}: printed nothing'
        return f'{len(cmds)} README commands ran and printed output'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', required=True)
    ap.add_argument('--record', action='store_true')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    s = Smoke(Path(args.repo))
    s.check('blame names a law', s.blame)
    s.check('text before and after an amendment', s.on_date)
    s.check('log --follow in date order', s.follow)
    s.check('tags resolve, In-force on every commit', s.tags_and_trailers)
    s.check('only the documentation commit is by Lexifina', s.lexifina)
    s.check('README commands run', s.readme)
    ok = all(r[1] for r in s.results)
    print(f'{sum(r[1] for r in s.results)}/{len(s.results)} passed')
    if args.record:
        p = Path(args.repo) / 'data' / 'verification.json'
        p.parent.mkdir(parents=True, exist_ok=True)
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['smoke'] = {'passed': sum(r[1] for r in s.results), 'total': len(s.results),
                        'results': [{'test': n, 'ok': o, 'detail': d} for n, o, d in s.results]}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
