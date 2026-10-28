"""Checks the git repository against the RIS: every version of every provision, read back from git on the day it took
effect, and the version before on the day before, must equal the RIS text.

    python -X utf8 scripts/austria-law/check_repo.py --today 2026-10-29 [--repo ../austria-law] [--no-record]

From the cached RIS data only (no network). The commit in force on a day is found as tools/stand_am.py finds it: the
last commit touching the act whose In-force trailer is on or before that day (on the branch `future` for days after
--today). For each version:
1. File: the provision's file in git on its first day is byte for byte the text parsed from its XML, and on the day
   before it is the previous version's text (or absent, if the provision was not in force that day). After the last
   version's end the file must be absent.
2. Words: the file on its first day has the same words in the same order as the XML's text part, read without the
   build's parser (every text node, with words separated at block boundaries).
The result is written to verification.json next to this script (unless --no-record), for REPRODUCE.md.
"""
import argparse
import bisect
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from lxml import etree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

TOKEN = re.compile(r'\w+|[^\w\s]')
SEPARATE = {'absatz', 'ueberschrift', 'listelem', 'liste', 'aufzaehlung', 'table', 'tr', 'td', 'th', 'tab', 'br',
            'symbol', 'p', 'div', 'schluss', 'schlussteil'}


def blob_hash(text: str) -> str:
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def official_words(raw: bytes) -> list[str]:
    """All words of the document's text part: everything after the heading 'Text' up to the next heading of the
    document's metadata, with a word break at every block, cell, tab, line break and list symbol."""
    root = etree.fromstring(raw)
    parts, on = [], False

    def text(e) -> str:
        if not isinstance(e.tag, str):
            return e.tail or ''
        name = etree.QName(e).localname
        gap = ' ' if name in SEPARATE else ''
        return gap + (e.text or '') + ''.join(text(c) for c in e) + gap + (e.tail or '')
    for ab in root.iter('{http://www.bka.gv.at}abschnitt'):
        for c in ab:
            name = etree.QName(c).localname
            if name == 'ueberschrift' and c.get('typ') == 'titel':
                on = ' '.join(''.join(c.itertext()).split()) == 'Text'
                continue
            if on and name not in ('kzinhalt', 'fzinhalt'):
                tail, c.tail = c.tail, None
                parts.append(text(c))
                c.tail = tail
    return TOKEN.findall(' '.join(parts).replace('­', ''))


def repo_words(text: str) -> list[str]:
    out = []
    for line in text.split('\n'):
        line = re.sub(r'^\s*(#{2,3} |- )', '', line)
        if line.startswith('| ') and line.endswith(' |'):
            line = line[2:-2].replace(' | ', ' ')
        out.append(line)
    return TOKEN.findall(' '.join(out))


class Repo:
    def __init__(self, path: str, today: str):
        self.path, self.today = path, today
        self.trees: dict[tuple[str, str], dict[str, str]] = {}
        self.history: dict[tuple[str, str], tuple[list[str], list[str]]] = {}
        branches = subprocess.run(['git', 'branch', '--list', 'future'], cwd=path, capture_output=True, text=True).stdout
        self.has_future = bool(branches.strip())

    def git(self, *args) -> str:
        out = subprocess.run(['git', *args], cwd=self.path, capture_output=True, text=True, encoding='utf-8')
        if out.returncode:
            raise SystemExit(f'git {" ".join(args)}: {out.stderr}')
        return out.stdout

    def commit_on(self, day: str, slug: str) -> str:
        branch = 'future' if day > self.today and self.has_future else 'main'
        key = (branch, slug)
        if key not in self.history:
            rows = []
            for line in self.git('log', '--format=%H%x09%(trailers:key=In-force,valueonly,separator=)', branch, '--',
                                 f'{slug}/').splitlines():
                h, _, d = line.partition('\t')
                if d.strip():
                    rows.append((d.strip(), h))
            rows.reverse()      # oldest first; In-force days never decrease along the history
            self.history[key] = ([d for d, _ in rows], [h for _, h in rows])
        days, commits = self.history[key]
        i = bisect.bisect_right(days, day)
        return commits[i - 1] if i else ''

    def tree(self, commit: str, slug: str) -> dict[str, str]:
        if not commit:
            return {}
        key = (commit, slug)
        if key not in self.trees:
            t = {}
            for line in self.git('ls-tree', '-r', commit, f'{slug}/').splitlines():
                info, f = line.split('\t', 1)
                t[f[len(slug) + 1:]] = info.split()[2]
            self.trees[key] = t
        return self.trees[key]

    def blob(self, day: str, slug: str, file: str) -> str | None:
        return self.tree(self.commit_on(day, slug), slug).get(file)

    def read_blobs(self, shas: list[str]) -> dict[str, str]:
        shas = sorted(set(shas))
        data = subprocess.run(['git', 'cat-file', '--batch'], cwd=self.path, capture_output=True,
                              input=''.join(f'{s}\n' for s in shas).encode()).stdout
        out, pos = {}, 0
        for s in shas:
            nl = data.index(b'\n', pos)
            size = int(data[pos:nl].split()[2])
            out[s] = data[nl + 1:nl + 1 + size].decode('utf-8')
            pos = nl + 1 + size + 1
        return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(build.ROOT.parent / 'austria-law'))
    ap.add_argument('--today', required=True)
    ap.add_argument('--only', default=None)
    ap.add_argument('--provisions', default=None)
    ap.add_argument('--no-record', action='store_true')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    if args.provisions:
        build.ONLY_APA.update(x.strip() for x in args.provisions.split(';'))
    acts = build.all_acts()
    if args.only:
        acts = [a for a in acts if a['nr'] in set(args.only.split(','))]
    repo = Repo(args.repo, args.today)
    n = before = after = bad = 0
    words_n = words_bad = nwords = 0
    per_act = {}
    word_jobs = []
    for act in acts:
        slug = act['slug']
        docs = build.list_docs(act['nr'], offline=True)
        tl, _ = build.timelines(docs)
        cnt = 0
        for apa, segs in tl.items():
            f = build.file_of(apa)
            prev = None
            for s in segs:
                raw = build.fetch(s['doc']['xml'], offline=True)
                text = build.render(raw)
                got = repo.blob(s['start'], slug, f)
                n += 1
                cnt += 1
                if got != blob_hash(text):
                    bad += 1
                    print(f'MISMATCH {slug} {apa} on {s["start"]} ({s["doc"]["id"]})')
                # the day before: the previous version if it held that day, else no file
                d0 = build.day_add(s['start'], -1)
                want = blob_hash(prev[1]) if prev and prev[0]['end'] == d0 else None
                got0 = repo.blob(d0, slug, f)
                before += 1
                if got0 != want:
                    bad += 1
                    print(f'MISMATCH {slug} {apa} on {d0}, the day before {s["doc"]["id"]}')
                if got:
                    word_jobs.append((slug, apa, s['doc']['id'], got, raw))
                prev = (s, text)
            if prev and prev[0]['end']:
                d1 = build.day_add(prev[0]['end'], 1)
                after += 1
                if repo.blob(d1, slug, f) is not None:
                    bad += 1
                    print(f'MISMATCH {slug} {apa}: still present on {d1}, after its last version ended')
        per_act[slug] = cnt
    blobs = repo.read_blobs([j[3] for j in word_jobs])
    for slug, apa, nor, sha, raw in word_jobs:
        ow, rw = official_words(raw), repo_words(blobs[sha])
        words_n += 1
        nwords += len(ow)
        if ow != rw:
            words_bad += 1
            i = next((i for i, (a, b) in enumerate(zip(ow, rw)) if a != b), min(len(ow), len(rw)))
            print(f'WORDS {slug} {apa} {nor}: official {len(ow)} vs repo {len(rw)}; first difference at {i}: '
                  f'{" ".join(ow[max(0, i - 5):i + 5])!r} / {" ".join(rw[max(0, i - 5):i + 5])!r}')
    print(f'{n} versions checked on their first day, {before} on the day before, {after} removals after the last '
          f'version: {bad} mismatches; {words_n} versions word for word ({nwords} words), {words_bad} mismatches')
    print('per act:', per_act)
    if not args.no_record:
        p = HERE / 'verification.json'
        rec = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        rec['check'] = {'versions': n, 'before': before, 'after': after, 'mismatches': bad, 'wordcheck': words_n,
                        'words': nwords, 'word_mismatches': words_bad, 'per_act': per_act}
        p.write_text(json.dumps(rec, indent=1, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    raise SystemExit(1 if bad or words_bad else 0)


if __name__ == '__main__':
    main()
