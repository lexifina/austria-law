"""Prints an act, or one provision of it, as it stood on a given day, from this repository's history.

    python tools/stand_am.py 2010-01-01 b-vg 10           # Art. 10 B-VG on 1 January 2010
    python tools/stand_am.py 2020-01-01 dsg               # the whole DSG on 1 January 2020
    python tools/stand_am.py 2018-01-01 dsg art-002/par-0024.md

Each commit carries the day its change took effect in an `In-force:` trailer (git cannot store dates before 1970, so
the trailer, not the commit date, is the source of truth). The text in force on a day is the last commit on or before
it. Changes published but not yet in force are on the branch `future`; a date after today reads from there.
Standard library only.
"""
import datetime as dt
import re
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def natural_key(path: str) -> tuple:
    """Files in the order of the act: the title first, then by number, annexes last."""
    out = []
    for seg in path.split('/', 1)[1][:-3].split('/'):
        if seg == 'titel':
            out.append((0, 0, ''))
            continue
        m = re.fullmatch(r'(par|art|anl)-0*(\d*)(.*)', seg)
        if m:
            out.append(({'art': 1, 'par': 1, 'anl': 3}[m.group(1)], int(m.group(2) or 0), m.group(3)))
        else:
            out.append((2, 0, seg))
    return tuple(out)


def commit_on(day: str, act: str) -> str:
    """The last commit touching the act whose In-force day is on or before the day."""
    future = day > dt.date.today().isoformat() and git('branch', '--list', 'future').strip()
    out = git('log', '--format=%H%x09%(trailers:key=In-force,valueonly,separator=)', 'future' if future else 'main',
              '--', f'{act}/')
    for line in out.splitlines():
        h, _, d = line.partition('\t')
        if d.strip() and d.strip() <= day:
            return h
    return ''


def candidates(key: str) -> list[str]:
    """'10' or '§ 10' or 'Art. 10' -> the files that could hold it."""
    if key.endswith('.md'):
        return [key]
    k = re.sub(r'^(§|Art\.?|Artikel|Anl\.?|Anlage)\s*', '', key.strip())
    m = re.fullmatch(r'(\d+)\s*([a-z]*)', k)
    if not m:
        return [key + '.md']
    n, suf = int(m.group(1)), m.group(2)
    if key.startswith(('Anl', 'anl')):
        return [f'anl-{n}{suf}.md']
    par, art = f'par-{n:04d}{suf}.md', f'art-{n:03d}{suf}.md'
    return [art, par] if key.startswith('Art') else [par, art]


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    day, act = sys.argv[1], sys.argv[2].strip('/')
    dt.date.fromisoformat(day)
    commit = commit_on(day, act)
    if not commit:
        sys.exit(f'{act} is not in the record on {day}.')
    files = [f for f in git('ls-tree', '-r', '--name-only', commit, f'{act}/').split('\n') if f.endswith('.md')]
    if len(sys.argv) > 3:
        key = ' '.join(sys.argv[3:])
        names = candidates(key)
        hits = [f for f in files if f[len(act) + 1:] in names or f.endswith('/' + names[0])]
        if not hits:
            sys.exit(f'{act} {key} was not in the text on {day}.')
        sys.stdout.write(git('show', f'{commit}:{sorted(hits, key=natural_key)[0]}'))
        return
    files = sorted(files, key=natural_key)
    data = subprocess.run(['git', 'cat-file', '--batch'], input=''.join(f'{commit}:{f}\n' for f in files).encode(),
                          capture_output=True, check=True).stdout
    pos = 0
    for _ in files:
        nl = data.index(b'\n', pos)
        size = int(data[pos:nl].split()[2])
        sys.stdout.write(data[nl + 1:nl + 1 + size].decode('utf-8') + '\n')
        pos = nl + 1 + size + 1


if __name__ == '__main__':
    main()
