"""Functional smoke test of the built Austrian law repository: the things a reader does with it work. Standard library only.

    python -X utf8 scripts/austria-law/test_repo.py [--repo ../austria-law] [--record]

It asserts that:
1. `git blame` on a much-amended provision names amending laws as authors of its lines;
2. tools/stand_am.py gives the text before and after an amendment, and each equals the file at that commit and its parent;
3. `git log --follow` on a file lists its amending laws in the order they took effect;
4. every tag resolves to a commit, and every commit but the documentation commit has an `In-force:` trailer;
5. no commit is authored by Lexifina except the documentation commit (the last one);
6. every git or tool command in the README's table runs and prints something.
The provisions tested are picked from the history (the files with the most commits by laws), not hard-coded.
With --record the result is written to verification.json next to this script (for REPRODUCE.md).
"""
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

    def law_commits(self, path: str) -> list[tuple[str, str, str, str]]:
        """(hash, author name, author email, In-force) of the commits by laws that touched the file, newest first."""
        out = self.git('log', '--follow', '--format=%H%x09%an%x09%ae%x09%(trailers:key=In-force,valueonly,separator=)',
                       'main', '--', path)
        rows = [tuple(x.strip() for x in l.split('\t')) for l in out.splitlines() if l]
        return [r for r in rows if LAW_EMAIL.match(r[2]) and r[2] != 'ris@ris-bka.invalid']

    def busy(self) -> list[str]:
        """One file per act: the file most often changed by laws."""
        if self._busy is None:
            counts: dict[str, int] = {}
            out = self.git('log', '--format=%x00%ae', '--name-only', 'main')
            for block in out.split('\x00')[1:]:
                lines = [l for l in block.splitlines() if l]
                if not lines or not LAW_EMAIL.match(lines[0]) or lines[0] == 'ris@ris-bka.invalid':
                    continue
                for f in lines[1:]:
                    if f.endswith('.md') and '/' in f and not f.endswith('README.md'):
                        counts[f] = counts.get(f, 0) + 1
            present = set(self.git('ls-tree', '-r', '--name-only', 'main').split())
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

    # 1
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

    # 2
    def on_date(self):
        done = []
        for path in self.busy():
            act = path.split('/', 1)[0]
            rows = self.law_commits(path)
            # The newest change whose day before is a different text: compare the tool with the commit and its parent.
            for h, _, _, day in rows:
                before = self.git('log', '-1', '--format=%(trailers:key=In-force,valueonly,separator=)', f'{h}~1').strip()
                if not before or before >= day:
                    continue
                prev_day = (dt.date.fromisoformat(day) - dt.timedelta(days=1)).isoformat()
                spec = path.split('/', 1)[1]
                b = self.tool(day, act, spec)
                a = self.tool(prev_day, act, spec)
                want_b = self.git('show', f'{h}:{path}')
                assert b.strip() == want_b.strip(), f'{path} on {day} is not the file at {h[:10]}'
                assert a != b, f'{path}: no change between {prev_day} and {day}'
                done.append(f'{path} {prev_day} != {day}')
                break
            else:
                raise AssertionError(f'{path}: no amendment found to test')
        whole = self.tool('2020-01-01', 'dsg')
        assert whole.strip(), 'the whole DSG on 2020-01-01 is empty'
        return '; '.join(done)

    # 3
    def follow(self):
        checked = []
        for path in self.busy():
            rows = self.law_commits(path)
            assert len(rows) >= 2, f'{path}: {len(rows)} law commits'
            days = [r[3] for r in rows]
            assert days == sorted(days, reverse=True), f'{path}: not in date order {days}'
            checked.append(f'{path} {len(rows)} law commits')
        return '; '.join(checked)

    # 4
    def tags_and_trailers(self):
        tags = self.git('tag').split()
        assert tags, 'no tags'
        for t in tags:
            self.git('rev-parse', '--verify', '-q', f'{t}^{{commit}}')
        rows = self.git('log', '--format=%H%x09%an%x09%(trailers:key=In-force,valueonly,separator=)', 'main').splitlines()
        missing = [r for r in rows[1:] if not r.split('\t')[2].strip()]
        assert not missing, f'{len(missing)} commits without In-force, e.g. {missing[:2]}'
        bad = [r for r in rows[1:] if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r.split('\t')[2].strip())]
        assert not bad, f'malformed In-force {bad[:2]}'
        return f'{len(tags)} tags resolve; {len(rows) - 1} commits carry In-force'

    # 5
    def lexifina(self):
        rows = self.git('log', '--format=%H%x09%an%x09%ae%x09%cn', 'main').splitlines()
        by_lex = [r for r in rows if r.split('\t')[1] == 'Lexifina']
        assert len(by_lex) == 1 and by_lex[0] == rows[0], f'{len(by_lex)} commits by Lexifina'
        assert all(r.split('\t')[3] == 'Lexifina' for r in rows), 'a committer other than Lexifina'
        bad = {r.split('\t')[2] for r in rows[1:] if not LAW_EMAIL.match(r.split('\t')[2])}
        assert not bad, f'unexpected author emails {bad}'
        return f'only the documentation commit {rows[0][:10]} is by Lexifina'

    # 6
    def readme(self):
        text = (self.repo / 'README.md').read_text(encoding='utf-8')
        table = text[text.index('## The questions'):text.index('## The dates')]
        rows = '\n'.join(l for l in table.splitlines() if l.startswith('|'))
        cmds = [c for c in re.findall(r'`([^`]+)`', rows) if c.startswith(('git ', 'python '))]
        assert len(cmds) >= 6, f'only {len(cmds)} commands found'
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
    ap.add_argument('--repo', default=str(HERE.parents[2] / 'austria-law'))
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
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['smoke'] = {'passed': sum(r[1] for r in s.results), 'total': len(s.results),
                        'results': [{'test': n, 'ok': o, 'detail': d} for n, o, d in s.results]}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(0 if ok else 1)


if __name__ == '__main__':
    main()
