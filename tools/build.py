"""Builds a git repository of Austrian federal law from the RIS (Rechtsinformationssystem des Bundes), in which every
amending law is one commit, dated the day it took effect.

    python -X utf8 scripts/austria-law/build.py --today 2026-10-29 [--repo ../austria-law] [--offline]
                                                [--only 10001597,...] [--verify-rebuild] [--fetch-only]

The RIS publishes the consolidated federal law ("Bundesrecht konsolidiert", application BrKons) through its Open
Government Data API (data.bka.gv.at/ris/api/v2.6). Every historical version of every section (§), article (Art.) or
annex (Anl.) of an act is its own document (a NOR number) with the days it was in force (Inkrafttretensdatum,
Ausserkrafttretensdatum) and its promulgation organ, which names the law that last amended that version
("BGBl. I Nr. 165/1999 zuletzt geändert durch BGBl. I Nr. 70/2024"). We model each provision's history directly from
these in-force windows: no whole-act snapshots are compared. A version is credited to the law RIS names for it when
that law differs from the one RIS names for the provision's previous version; otherwise it is never credited to a law
and gets its own labelled commit by the RIS. A provision whose last window ends, or that has a gap between two
windows, leaves the text that day; that removal is credited by date only to the one law that took effect in the act
that day, or else to no law.

The RIS OGD terms (FAQ, 28 Nov 2025) are binding for the fetch: one connection, a pause of two seconds between
requests, and requests only between 20:00 and 05:00 Vienna time or at weekends and on Austrian public holidays. The
fetcher enforces all three; everything it reads is cached in .cache/ next to this file, so a rebuild needs no network.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CACHE = HERE / '.cache'
API = 'https://data.bka.gv.at/ris/api/v2.6/Bundesrecht'
UA = 'lexifina-watch/1.0 (+https://lexifina.com/watch; corpus@lexifina.com)'
PAUSE = 2.0          # seconds between the end of one request and the start of the next (RIS OGD terms)
COMMITTER = ('Lexifina', 'austria-law@lexifina.com')
PUBLISHER = ('RIS (Bundeskanzleramt)', 'ris@ris-bka.invalid')
NS = '{http://www.bka.gv.at}'

# The acts in the record, by RIS Gesetzesnummer, with the folder each one gets.
# The first record is the constitution and one much-amended act; more (ABGB 10001622, StGB 10002296, UGB 10001702,
# ZPO 10001699) go in acts_extra.json and are appended later.
ACTS = [
    {'nr': '10000138', 'slug': 'b-vg'},
    {'nr': '10001597', 'slug': 'dsg'},
]
EXTRA = HERE / 'acts_extra.json'   # further acts, added after the core two: [{"nr": ..., "slug": ...}]


def all_acts() -> list[dict]:
    acts = list(ACTS)
    if EXTRA.exists():
        acts += json.loads(EXTRA.read_text(encoding='utf-8'))
    return acts


# ---------------------------------------------------------------- time in Vienna (no tz database on this machine)

def last_sunday(year: int, month: int) -> dt.date:
    d = (dt.date(year, month + 1, 1) if month < 12 else dt.date(year + 1, 1, 1)) - dt.timedelta(days=1)
    return d - dt.timedelta(days=(d.weekday() + 1) % 7)


def vienna_offset(day: dt.date) -> int:
    """Hours ahead of UTC at noon on a day in Vienna. Austria kept no summer time from 1949 to 1979. From 1980 it is
    on from the first Sunday in April (1980) or the last Sunday in March (from 1981) to the last Sunday in September
    (until 1995) or October (from 1996); at noon the change days already have the new time."""
    y = day.year
    if y < 1980:
        return 1
    start = (dt.date(1980, 4, 1) + dt.timedelta(days=(6 - dt.date(1980, 4, 1).weekday()) % 7)) if y == 1980 else last_sunday(y, 3)
    end = last_sunday(y, 9 if y < 1996 else 10)
    return 2 if start <= day < end else 1


def easter(y: int) -> dt.date:
    a, b, c = y % 19, y // 100, y % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    return dt.date(y, month, (h + l - 7 * m + 114) % 31 + 1)


def holiday(d: dt.date) -> bool:
    """Austrian public holidays (Feiertagsruhegesetz 1957, § 1)."""
    e = easter(d.year)
    moving = {e + dt.timedelta(days=n) for n in (1, 39, 50, 60)}   # Easter Monday, Ascension, Whit Monday, Corpus Christi
    fixed = {(1, 1), (1, 6), (5, 1), (8, 15), (10, 26), (11, 1), (12, 8), (12, 25), (12, 26)}
    return d in moving or (d.month, d.day) in fixed


def vienna_now() -> dt.datetime:
    utc = dt.datetime.now(dt.timezone.utc)
    # The offset at the moment: summer time changes at 01:00 UTC on the change days.
    y = utc.year
    start = dt.datetime.combine(last_sunday(y, 3), dt.time(1), dt.timezone.utc)
    end = dt.datetime.combine(last_sunday(y, 10), dt.time(1), dt.timezone.utc)
    off = 2 if start <= utc < end else 1
    return (utc + dt.timedelta(hours=off)).replace(tzinfo=None)


def fetch_allowed(now: dt.datetime) -> bool:
    """RIS OGD terms: only 20:00-05:00 Vienna time, or at weekends and on public holidays."""
    return now.hour >= 20 or now.hour < 5 or now.weekday() >= 5 or holiday(now.date())


# ---------------------------------------------------------------- fetching

REQUESTS: list[dict] = []   # every URL the build read, for REPRODUCE.md
TEXTS: dict[str, tuple[str, str]] = {}   # NOR id -> (rendered text, sha256 of the XML)
TAGS: dict[str, int] = {}
_last = [0.0]
NET = {'count': 0}


def _get(url: str) -> bytes | None:
    while not fetch_allowed(vienna_now()):
        print(f'{vienna_now():%Y-%m-%d %H:%M} Vienna: outside the RIS OGD hours (20:00-05:00, weekends, holidays); waiting',
              flush=True)
        time.sleep(600)
    wait = _last[0] + PAUSE - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip'})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    body = gzip.decompress(body)
                return body
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            raise
        except urllib.error.URLError as exc:
            if 'CERTIFICATE' not in str(exc).upper():
                raise
            out = subprocess.run(['curl', '-sS', '-f', '--compressed', '-A', UA, url], capture_output=True)
            if out.returncode:
                raise RuntimeError(f'curl {url}: {out.stderr.decode(errors="replace")}')
            return out.stdout
    finally:
        _last[0] = time.monotonic()
        NET['count'] += 1


def cache_path(url: str) -> Path:
    return CACHE / hashlib.sha256(url.encode()).hexdigest()[:32]


def fetch(url: str, offline: bool = False, check=None) -> bytes | None:
    """GET with a file cache keyed by the URL, so a rebuild reads the same bytes. A 404 is cached too (as an empty
    file with the suffix .404)."""
    path = cache_path(url)
    REQUESTS.append({'url': url, 'file': path})
    if path.exists():
        return path.read_bytes()
    if path.with_suffix('.404').exists():
        return None
    if offline:
        raise SystemExit(f'not cached: {url}')
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / '.gitignore').write_text('*\n')
    for attempt in range(4):
        try:
            body = _get(url)
            if body is None:
                path.with_suffix('.404').write_bytes(b'')
                return None
            if check and not check(body):
                raise RuntimeError(f'unexpected answer for {url}: {body[:200]!r}')
            path.write_bytes(body)
            return body
        except Exception as exc:
            if attempt == 3:
                raise
            print(f'retry {attempt + 1} {url}: {exc}', flush=True)
            time.sleep(30 * (attempt + 1))
    raise AssertionError


# ---------------------------------------------------------------- the act's documents

def list_url(nr: str, page: int) -> str:
    return f'{API}?Applikation=BrKons&Gesetzesnummer={nr}&DokumenteProSeite=OneHundred&Seitennummer={page}'


def as_list(x) -> list:
    return x if isinstance(x, list) else ([] if x is None else [x])


def clean(s: str | None) -> str:
    """Runs of white space (spaces, line breaks, tabs, no-break spaces) become one space; soft hyphens go."""
    return re.sub(r'[\s ]+', ' ', (s or '').replace('­', '')).strip()


ONLY_APA: set[str] = set()


def list_docs(nr: str, offline: bool) -> list[dict]:
    """Every document (every version of every provision) RIS holds for one act, from its search pages."""
    docs, page, hits = [], 1, None
    while True:
        raw = fetch(list_url(nr, page), offline, check=lambda b: b'OgdSearchResult' in b)
        res = json.loads(raw.decode('utf-8'))['OgdSearchResult']
        if 'OgdDocumentResults' not in res:
            raise SystemExit(f'{nr} page {page}: {str(res)[:300]}')
        r = res['OgdDocumentResults']
        hits = int(r['Hits']['#text'])
        refs = as_list(r.get('OgdDocumentReference'))
        for ref in refs:
            docs.append(read_ref(ref))
        if not refs or len(docs) >= hits:
            break
        page += 1
    ids = [d['id'] for d in docs]
    if len(set(ids)) != len(ids) or len(ids) != hits:
        raise SystemExit(f'{nr}: {len(ids)} documents ({len(set(ids))} distinct) for {hits} hits')
    for d in docs:
        if d['gesnr'] != nr:
            raise SystemExit(f'{d["id"]} belongs to {d["gesnr"]}, not {nr}')
    if ONLY_APA:
        docs = [d for d in docs if d['apa'] in ONLY_APA]
    return sorted(docs, key=lambda d: d['id'])


# 'BGBl. I Nr. 165/1999 zuletzt geändert durch BGBl. I Nr. 70/2024', '... aufgehoben durch ...'
BY_RE = re.compile(r'^(.*?)\s+((?:zuletzt )?geändert|aufgehoben|eingefügt|idF|in der Fassung)\s+durch\s+(.*)$')


def read_ref(ref: dict) -> dict:
    md = ref['Data']['Metadaten']
    br = md['Bundesrecht']
    k = br['BrKons']
    urls = {u['DataType']: u['Url'] for u in as_list(ref['Data']['Dokumentliste']['ContentReference']['Urls']['ContentUrl'])}
    kund = clean(k.get('Kundmachungsorgan'))
    m = BY_RE.match(kund)
    stamm, rel, last = (clean(m.group(1)), m.group(2), clean(m.group(3))) if m else (kund, '', '')
    return {
        'id': md['Technisch']['ID'], 'apa': clean(k.get('ArtikelParagraphAnlage')), 'from': k.get('Inkrafttretensdatum'),
        'to': k.get('Ausserkrafttretensdatum'), 'kund': kund, 'stamm': stamm, 'law': last or stamm, 'rel': rel,
        'novelle': clean(' '.join(x for x in (k.get('NovellenPublikationsorgan'), k.get('NovellenBgblnummer')) if x)),
        'kurztitel': clean(br.get('Kurztitel')), 'titel': br.get('Titel') or '', 'abk': clean(k.get('Abkuerzung')),
        'typ': clean(k.get('Typ')), 'gesnr': k.get('Gesetzesnummer'), 'xml': urls.get('Xml'), 'html': urls.get('Html'),
        'eli': br.get('Eli') or md['Allgemein'].get('DokumentUrl'), 'beachte': clean(k.get('Beachte')),
        'anmerkung': clean(k.get('Anmerkung')), 'ur': clean(k.get('Uebergangsrecht')), 'aenderung': k.get('Aenderung') or '',
    }


# ---------------------------------------------------------------- one document's text

def local(e) -> str:
    t = e.tag
    return t[t.index('}') + 1:] if isinstance(t, str) and t[0] == '{' else (t if isinstance(t, str) else '')


BLOCK = {'ueberschrift', 'absatz', 'liste', 'aufzaehlung', 'listelem', 'table', 'tr', 'schlussteil', 'abschnitt',
         'gliederung', 'erlaeuterung', 'tbody', 'thead', 'tfoot', 'ziffernliste', 'kzinhalt', 'fzinhalt', 'binary',
         'quelle', 'p', 'div', 'pre', 'schluss', 'literaliste',
         'subliteraliste', 'subziffernliste', 'strichliste', 'substrichliste'}
GAP = {'tab', 'br', 'td', 'th'}   # inline elements that separate words


def text_section(raw: bytes) -> list:
    """The elements of the document's 'Text' part: after the heading 'Text' and before the next metadata heading
    (Zuletzt aktualisiert am, Gesetzesnummer, Beachte, Anmerkung, Schlagworte ...)."""
    root = etree.fromstring(raw)
    out, on = [], False
    for ab in root.iter(NS + 'abschnitt'):
        for c in ab:
            name = local(c)
            if name == 'ueberschrift' and c.get('typ') == 'titel':
                on = clean(''.join(c.itertext())) == 'Text'
                continue
            if on and name not in ('kzinhalt', 'fzinhalt'):
                out.append(c)
    return out


def inline_child(c) -> str:
    """The words of one inline child (without its tail)."""
    name = local(c)
    if not name:              # comment or processing instruction
        return ''
    if name in GAP:
        return ' ' + inline(c) + ' '
    if name == 'symbol':
        return inline(c) + ' '
    return inline(c)


def inline(e, skip_blocks: bool = True) -> str:
    """The words of an element and its inline children; a tab or line break is a space, a list symbol is followed by
    one."""
    parts = [e.text or '']
    for c in e:
        if not (skip_blocks and local(c) in BLOCK):
            parts.append(inline_child(c))
        parts.append(c.tail or '')
    return ''.join(parts)


def runs(e) -> list:
    """An element's content in document order: strings of inline text, and child block elements between them."""
    out, buf = [], [e.text or '']
    for c in e:
        if local(c) in BLOCK:
            out.append(''.join(buf))
            out.append(c)
            buf = []
        else:
            buf.append(inline_child(c))
        buf.append(c.tail or '')
    out.append(''.join(buf))
    return out


def render_blocks(els: list) -> list[str]:
    lines: list[str] = []

    def add(s: str):
        s = clean(s)
        if s:
            lines.append(s)

    def walk(e, level: int):
        name = local(e)
        if not name:
            return
        if name == 'ueberschrift':
            t = clean(inline(e))
            if t:
                lines.append(('## ' if (e.get('typ') or '').startswith('g') else '### ') + t)
        elif name == 'aufzaehlung':
            for c in e:
                walk(c, int(float(e.get('ebene') or 1)))
        elif name == 'listelem':
            # Text, nested lists, then the text that closes them, in that order.
            first = True
            for r in runs(e):
                if isinstance(r, str):
                    t = clean(r)
                    if t:
                        lines.append('  ' * max(level - 1, 0) + ('- ' if first else '  ') + t)
                        first = False
                else:
                    walk(r, level + 1)
        elif name == 'table':
            for tr in e.iter(NS + 'tr'):
                cells = [clean(inline(td, skip_blocks=False)) for td in tr if local(td) in ('td', 'th')]
                row = ' | '.join(x for x in cells if x)
                if row:
                    lines.append('| ' + row + ' |')
        elif name in BLOCK and any(local(c) in BLOCK for c in e):
            for r in runs(e):
                if isinstance(r, str):
                    add(r)
                else:
                    walk(r, int(float(r.get('ebene') or level)))
        else:
            add(inline(e, skip_blocks=False))

    for e in els:
        walk(e, 1)
    return lines


def render(raw: bytes) -> str:
    lines = render_blocks(text_section(raw))
    return '\n\n'.join(lines) + '\n' if lines else ''


# ---------------------------------------------------------------- names: laws and files

LAW_RE = re.compile(r'^(?P<org>[A-Za-zÄÖÜäöü]+\.?)(?:\s+(?P<part>I{1,3}))?\s+(?P<kind>Nr\.|S\.?)\s*(?P<n>\d+[a-z]?)'
                    r'\s*/\s*(?P<y>\d{4})(?P<rest>.*)$')


def law_parts(label: str) -> dict | None:
    m = LAW_RE.match(label)
    if not m:
        return None
    org = m.group('org').rstrip('.')
    return {'org': org, 'part': m.group('part') or '', 'kind': 'S' if m.group('kind').startswith('S') else 'Nr',
            'n': m.group('n'), 'y': int(m.group('y')), 'rest': clean(m.group('rest'))}


def ascii_slug(s: str) -> str:
    s = s.replace('Ä', 'Ae').replace('Ö', 'Oe').replace('Ü', 'Ue').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    s = s.replace('ß', 'ss').replace('§', 'par')
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def law_author(label: str) -> tuple[str, str]:
    p = law_parts(label)
    if not p:
        return label, f'{ascii_slug(label)}@ris.invalid'
    slug = '-'.join(x for x in (ascii_slug(p['org']), p['part'].lower(), str(p['y']),
                                ('s' if p['kind'] == 'S' else '') + p['n']) if x)
    return label, f'{slug}@ris.invalid'


def law_tag(label: str) -> str:
    p = law_parts(label)
    if not p:
        return 'law/' + ascii_slug(label)
    org = ascii_slug(p['org']) + (f'-{p["part"].lower()}' if p['part'] else '')
    return f'{org}/{p["y"]}/{("s" if p["kind"] == "S" else "") + p["n"]}'


def law_order(label: str) -> tuple:
    p = law_parts(label)
    if not p:
        return (9999, label, '', 0, '')
    n = re.match(r'\d+', p['n']).group(0)
    return (p['y'], p['org'], p['part'], int(n), p['n'])


def law_year(label: str) -> int | None:
    p = law_parts(label)
    return p['y'] if p else None


def num_part(prefix: str, x: str, width: int) -> str:
    m = re.fullmatch(r'(\d+)(.*)', x)
    if m:
        return f'{prefix}-{int(m.group(1)):0{width}d}{ascii_slug(m.group(2))}'
    return f'{prefix}-{ascii_slug(x)}'


def file_of(apa: str) -> str:
    """'§ 24a' -> par-0024a.md, 'Art. 10' -> art-010.md, 'Art. 2 § 24' -> art-002/par-0024.md, 'Anl. 1' -> anl-1.md,
    '§ 0' (the title and promulgation clause) -> titel.md."""
    if apa in ('§ 0', ''):
        return 'titel.md'
    toks = re.findall(r'(§§?|Art\.|Artikel|Anl\.|Anlage)\s*([^\s§]+)|(\S+)', apa)
    parts = []
    for kind, val, other in toks:
        if kind.startswith('§'):
            parts.append(num_part('par', val, 4))
        elif kind.startswith('Art'):
            parts.append(num_part('art', val, 3))
        elif kind.startswith('Anl'):
            parts.append(f'anl-{ascii_slug(val)}')
        elif other:
            parts.append(ascii_slug(other))
    parts = [p for p in parts if p]
    return '/'.join(parts) + '.md'


def natural_key(path: str) -> tuple:
    """Files in the order of the act: the title first, then by number, annexes last."""
    out = []
    for seg in path[:-3].split('/'):
        if seg == 'titel':
            out.append((0, 0, ''))
            continue
        m = re.fullmatch(r'(par|art|anl)-0*(\d*)(.*)', seg)
        if m:
            out.append(({'art': 1, 'par': 1, 'anl': 3}[m.group(1)], int(m.group(2) or 0), m.group(3)))
        else:
            out.append((2, 0, seg))
    return tuple(out)


# ---------------------------------------------------------------- one act: timelines and changes

def day_add(d: str, n: int) -> str:
    return (dt.date.fromisoformat(d) + dt.timedelta(days=n)).isoformat()


def timelines(docs: list[dict]) -> tuple[dict, list[str]]:
    """Per provision, its versions that were in force for at least one day, in order, each with the first and last
    day it held (end None: still in force), and the problems found: overlapping windows, two versions from one day."""
    by: dict[str, list[dict]] = {}
    problems = []
    for d in docs:
        if not d['from']:
            problems.append(f'{d["id"]} {d["apa"]}: no Inkrafttretensdatum')
            continue
        if d['to'] and d['to'] < d['from']:
            continue      # never in force: replaced before it took effect
        by.setdefault(d['apa'], []).append(d)
    out = {}
    for apa, vs in by.items():
        vs.sort(key=lambda d: (d['from'], d['to'] or '9999-99-99', d['id']))
        keep = []
        for v in vs:
            if keep and keep[-1]['from'] == v['from']:
                problems.append(f'{apa}: two versions from {v["from"]} ({keep[-1]["id"]}, {v["id"]}); the one in force '
                                f'longer is used')
                keep[-1] = v      # sorted by end: v ends later
                continue
            keep.append(v)
        segs = []
        for i, v in enumerate(keep):
            end = v['to']
            nxt = keep[i + 1] if i + 1 < len(keep) else None
            if nxt and (end is None or end >= nxt['from']):
                problems.append(f'{apa}: {v["id"]} ({v["from"]}..{v["to"]}) overlaps {nxt["id"]} from {nxt["from"]}; '
                                f'the later version is used from its first day')
                end = day_add(nxt['from'], -1)
            segs.append({'doc': v, 'start': v['from'], 'end': end})
        out[apa] = segs
    return out, problems


def build_act(act: dict, offline: bool, texts: dict) -> dict:
    docs = list_docs(act['nr'], offline)
    tl, problems = timelines(docs)
    files: dict[str, str] = {}
    for apa in tl:
        f = file_of(apa)
        if f in files.values():
            raise SystemExit(f'{act["nr"]}: two provisions map to {f}')
        files[apa] = f
    for segs in tl.values():
        for s in segs:
            d = s['doc']
            if d['id'] not in texts:
                raw = fetch(d['xml'], offline, check=lambda b: b'<risdok' in b)
                texts[d['id']] = (render(raw), hashlib.sha256(raw).hexdigest())
    # the act's name: from its newest document
    newest = max(docs, key=lambda d: (d['from'] or '', d['id']))
    events = []    # (day, apa, kind, seg or None, prev seg or None)
    for apa, segs in tl.items():
        prev = None
        for s in segs:
            if prev is None or prev['end'] is not None and day_add(prev['end'], 1) < s['start']:
                if prev is not None:
                    events.append((day_add(prev['end'], 1), apa, 'remove', None, prev))
                    events.append((s['start'], apa, 'set', s, None))
                else:
                    events.append((s['start'], apa, 'set', s, None))
            else:
                events.append((s['start'], apa, 'set', s, prev))
            prev = s
        if prev['end'] is not None:
            events.append((day_add(prev['end'], 1), apa, 'remove', None, prev))
    return {'act': act, 'docs': docs, 'tl': tl, 'files': files, 'events': events, 'problems': problems,
            'abk': newest['abk'] or act['slug'].upper(), 'kurztitel': newest['kurztitel'],
            'titel': clean(re.sub(r'<br\s*/?>.*$', '', newest['titel'], flags=re.S)), 'stamm': newest['stamm']}


def changes(built: list[dict], texts: dict) -> list[dict]:
    """Every change of a file, with its cause: {'day', 'b', 'apa', 'kind' (new, amended, removed), 'text', 'doc',
    'cause' (a law, or 'candidates' or 'unexplained'), 'why', 'cands'}.

    RIS names for each version the law that last amended it ('zuletzt geändert durch'). For the last version of a
    provision that was later repealed it names the repealing law instead ('aufgehoben durch'), and the law that wrote
    that version's text is no longer named; such a version, and a removal RIS names no law for, is credited by date
    to the one law RIS names for versions beginning in the act that day, or else to none."""
    out = []
    for b in built:
        day_laws: dict[str, set[str]] = {}
        for day, apa, kind, s, prev in b['events']:
            if kind == 'set' and s['doc']['rel'] != 'aufgehoben':
                day_laws.setdefault(day, set()).add(s['doc']['law'])
            if kind == 'remove' and prev['doc']['rel'] == 'aufgehoben':
                day_laws.setdefault(day, set()).add(prev['doc']['law'])

        def by_date(day: str) -> tuple[str, list[str]]:
            cands = sorted(day_laws.get(day, set()), key=law_order)
            return (cands[0] if len(cands) == 1 else 'candidates' if cands else 'unexplained'), cands

        current: dict[str, dict | None] = {}    # the version in force now, None when the provision is out
        last_doc: dict[str, dict] = {}            # the provision's latest version so far, even across a gap
        for day, apa, kind, s, prev in sorted(b['events'], key=lambda e: (e[0], e[1], e[2] == 'set')):
            cur = current.get(apa)
            old = texts[cur['doc']['id']][0] if cur else None
            if kind == 'remove':
                current[apa] = None
                if old is None:
                    continue
                if prev['doc']['rel'] == 'aufgehoben':
                    cause, why, cands = prev['doc']['law'], 'named repealing law', []
                else:
                    cause, cands = by_date(day)
                    why = {'candidates': 'removal: several laws that day', 'unexplained': 'removal: no law that day'}.get(
                        cause, 'date-only removal')
                out.append({'day': day, 'b': b, 'apa': apa, 'kind': 'removed', 'text': None, 'doc': prev['doc'],
                            'cause': cause, 'why': why, 'cands': cands})
                continue
            new = texts[s['doc']['id']][0]
            prev_doc = last_doc.get(apa)
            current[apa] = s
            last_doc[apa] = s['doc']
            if new == old:
                continue
            law = s['doc']['law']
            if s['doc']['rel'] == 'aufgehoben':
                cause, cands = by_date(day)
                why = {'candidates': 'only the repealing law named: several laws that day',
                       'unexplained': 'only the repealing law named: no law that day'}.get(cause, 'date-only version')
            elif prev_doc is None:
                cause, why, cands = law, 'first version in RIS', []
            elif prev_doc['law'] != law or prev_doc['rel'] == 'aufgehoben':
                cause, why, cands = law, 'named law', []
            else:
                cause, why, cands = 'unexplained', 'same law as the version before', [law]
            out.append({'day': day, 'b': b, 'apa': apa, 'kind': 'new' if old is None else 'amended', 'text': new,
                        'doc': s['doc'], 'cause': cause, 'why': why, 'cands': cands})
    return out


# ---------------------------------------------------------------- commits

def commit_date(day: str, seq: list[int]) -> str:
    """Noon in Vienna on the day. Git cannot record a time before 1970, so changes in force before then are dated
    1 January 1970 (UTC), one second apart in the order they took effect; the real day is in the In-force trailer."""
    d = dt.date.fromisoformat(day)
    if d.year < 1970:
        seq[0] += 1
        return f'{seq[0]} +0000'
    off = vienna_offset(d)
    stamp = int(dt.datetime(d.year, d.month, d.day, 12, tzinfo=dt.timezone(dt.timedelta(hours=off))).timestamp())
    return f'{stamp} +0{off}00'


KIND_DE = {'new': 'Neu', 'amended': 'Geändert', 'removed': 'Außer Kraft'}


def plan(chs: list[dict]) -> list[dict]:
    """One commit per law per day (across all acts), then per day the changes with candidate laws (one commit per set
    of candidates), then the changes nothing explains."""
    groups: dict[tuple, list[dict]] = {}
    for c in chs:
        if c['cause'] == 'candidates':
            key = (c['day'], 1, tuple(law_order(x) for x in c['cands']), 'candidates', tuple(c['cands']))
        elif c['cause'] == 'unexplained':
            key = (c['day'], 2, (), 'unexplained', ())
        else:
            key = (c['day'], 0, law_order(c['cause']), c['cause'], ())
        groups.setdefault(key, []).append(c)
    out = []
    for key in sorted(groups):
        items = sorted(groups[key], key=lambda c: (c['b']['act']['slug'], natural_key(c['b']['files'][c['apa']])))
        out.append({'day': key[0], 'kind': ['law', 'candidates', 'unexplained'][key[1]], 'law': key[3],
                    'cands': list(key[4]), 'items': items})
    return out


def label_of(c: dict) -> str:
    return f'{c["b"]["abk"]} {c["apa"] if c["apa"] != "§ 0" else "Titel"}'


def message(cm: dict) -> tuple[tuple[str, str], str]:
    day, items = cm['day'], cm['items']
    labels = [label_of(c) for c in items]
    acts = []
    for c in items:
        if c['b']['abk'] not in acts:
            acts.append(c['b']['abk'])
    if cm['kind'] == 'law':
        head = cm['law']
        author = law_author(cm['law'])
    elif cm['kind'] == 'candidates':
        head = 'mehrere Gesetze'
        author = PUBLISHER
    else:
        head = 'ohne neues Gesetz'
        author = PUBLISHER
    subject = f'{", ".join(labels)} ({head})'
    if len(subject) > 72:
        subject = f'{"; ".join(acts)}: {len(items)} Bestimmungen ({head})'
    if len(subject) > 72:
        subject = f'{len(items)} Bestimmungen in {len(acts)} Gesetzen ({head})'
    body = []
    whys: dict[str, list[str]] = {}
    for c in items:
        whys.setdefault(c['why'], []).append(label_of(c))
    if cm['kind'] == 'law':
        body += [f'{cm["law"]}, in Kraft am {day}.', '', f'{cm["law"]}, in force on {day}.', '']
    elif cm['kind'] == 'candidates':
        names = ', '.join(cm['cands'])
        body += [f'An diesem Tag traten im Gesetz mehrere Gesetze in Kraft ({names}). Das RIS sagt nicht, welches die',
                 'folgenden Änderungen bewirkt hat; der Commit wird keinem von ihnen zugeschrieben.', '',
                 f'Several laws took effect in the act on this day ({names}). RIS does not say which of them made the',
                 'changes below, so they are credited to none of them.', '']
    else:
        body += ['Das RIS nennt für diese Änderungen kein Gesetz, das sie bewirkt hätte; der Commit wird keinem Gesetz',
                 'zugeschrieben.', '',
                 'RIS names no law that made these changes, so they are credited to no law.', '']
    by_act: dict[str, list[dict]] = {}
    for c in items:
        by_act.setdefault(c['b']['abk'], []).append(c)
    for abk, cs in by_act.items():
        b = cs[0]['b']
        body.append(f'{abk} ({b["kurztitel"]}):')
        for kind in ('new', 'amended', 'removed'):
            ks = [c for c in cs if c['kind'] == kind]
            if ks:
                body.append(f'  {KIND_DE[kind]}: ' + ', '.join(c['apa'] if c['apa'] != '§ 0' else 'Titel' for c in ks))
        body.append('')
    body.append('Fassungen im RIS (versions in RIS):')
    for c in items:
        d = c['doc']
        if c['kind'] == 'removed':
            body.append(f'- {label_of(c)}: {d["id"]}, in Kraft bis {d["to"]} ({d["kund"]})')
        else:
            body.append(f'- {label_of(c)}: {d["id"]} ({d["kund"]})')
    body.append('')
    trailers = []
    law = cm['law']
    ev = {
        'named law': f'RIS names {law} as the law that last amended the new version (zuletzt geaendert durch), and '
                     f'another law for the version before',
        'first version in RIS': f'the first version of the provision in RIS, for which RIS names {law}',
        'named repealing law': f'RIS names {law} as the repealing law of the last version (aufgehoben durch)',
        'date-only removal': 'date only (removal): RIS names no law for it, and this is the only law RIS names for '
                             'versions of the act beginning that day',
        'date-only version': 'date only: RIS names only the later repealing law for this version, and this is the only '
                             'law RIS names for versions of the act beginning that day',
        'removal: several laws that day': 'removal for which RIS names no law, on a day several laws took effect in the act',
        'only the repealing law named: several laws that day': 'RIS names only the later repealing law for this version, '
                                                              'on a day several laws took effect in the act',
        'same law as the version before': 'RIS names the same law for this version as for the one before',
        'removal: no law that day': 'removal for which RIS names no law, on a day no law took effect in the act',
        'only the repealing law named: no law that day': 'RIS names only the later repealing law for this version, and '
                                                        'no law took effect in the act that day',
    }
    if cm['kind'] == 'law':
        trailers.append(f'Gazette: {law}')
    for why in sorted(whys):
        n = len(whys[why])
        trailers.append(f'Evidence: {ev[why]} ({n} provision{"s" if n > 1 else ""})')
    cands = cm['cands'] if cm['kind'] == 'candidates' else sorted(
        {x for c in items for x in c['cands']}, key=law_order)
    trailers += [f'Candidate: {x}' for x in cands]
    trailers.append(f'In-force: {day}')
    y = law_year(cm['law']) if cm['kind'] == 'law' else None
    if y and int(day[:4]) < y:
        trailers.append(f'Date-note: in force before the year of its Gazette number ({y}), as RIS gives it')
    aff = ', '.join(labels)
    trailers.append(f'Affecting: {aff}')
    if day < '1970-01-01':
        body += ['Git kann kein Datum vor 1970 speichern: der Commit ist auf den 1. Januar 1970 datiert, der Tag des',
                 'Inkrafttretens steht in In-force. (Git cannot record dates before 1970: the real day is In-force.)', '']
    return author, f'{subject}\n\n' + '\n'.join(body).rstrip('\n') + '\n\n' + '\n'.join(trailers) + '\n'


class FastImport:
    """One streamed `git fast-import`: each commit is written as it is made and its texts dropped."""

    def __init__(self, repo: Path):
        self.p = subprocess.Popen(['git', 'fast-import', '--quiet', '--done', '--date-format=raw'], cwd=repo,
                                  stdin=subprocess.PIPE)
        self.mark = 0

    def w(self, b: bytes):
        self.p.stdin.write(b)

    def data(self, s: str):
        b = s.encode('utf-8')
        self.w(f'data {len(b)}\n'.encode() + b + b'\n')

    def commit(self, ref: str, author: tuple[str, str], when: str, msg: str, parent: int | None, ops: list[tuple]) -> int:
        self.mark += 1
        self.w(f'commit {ref}\nmark :{self.mark}\n'.encode())
        self.w(f'author {author[0]} <{author[1]}> {when}\ncommitter {COMMITTER[0]} <{COMMITTER[1]}> {when}\n'.encode('utf-8'))
        self.data(msg)
        if parent:
            self.w(f'from :{parent}\n'.encode())
        for op in ops:
            if op[1] is None:
                self.w(f'D {op[0]}\n'.encode())
            else:
                self.w(f'M 100644 inline {op[0]}\n'.encode())
                self.data(op[1])
        self.w(b'\n')
        return self.mark

    def tag(self, name: str, mark: int):
        self.w(f'reset refs/tags/{name}\nfrom :{mark}\n\n'.encode())

    def finish(self):
        self.w(b'done\n')
        self.p.stdin.close()
        if self.p.wait():
            raise SystemExit('git fast-import failed')


def git(repo: Path, *args: str) -> str:
    out = subprocess.run(['git', *args], cwd=repo, capture_output=True, text=True, encoding='utf-8')
    if out.returncode:
        raise SystemExit(f'git {" ".join(args)} failed: {out.stderr}')
    return out.stdout


def prepare_repo(repo: Path) -> str | None:
    """Empties the target (an earlier build, or the placeholder clone) keeping its remote; refuses anything else."""
    remote = None
    if repo.exists() and any(repo.iterdir()):
        if not (repo / '.git').exists():
            raise SystemExit(f'{repo} is not empty and not a git repository; refusing to overwrite it')
        out = subprocess.run(['git', 'remote', 'get-url', 'origin'], cwd=repo, capture_output=True, text=True)
        remote = out.stdout.strip() or None
        if remote and 'austria-law' not in remote:
            raise SystemExit(f'{repo} has the remote {remote}; refusing to overwrite it')

        def force(fn, path, _exc):
            os.chmod(path, 0o700)
            fn(path)
        for p in repo.iterdir():
            shutil.rmtree(p, onexc=force) if p.is_dir() else p.unlink()
    repo.mkdir(parents=True, exist_ok=True)
    git(repo, 'init', '-q', '-b', 'main')
    git(repo, 'config', 'core.autocrlf', 'false')
    git(repo, 'config', 'core.quotepath', 'false')
    if remote:
        git(repo, 'remote', 'add', 'origin', remote)
    return remote


def write_repo(repo: Path, built: list[dict], chs: list[dict], today: str) -> tuple[list[dict], dict, dict]:
    prepare_repo(repo)
    fi = FastImport(repo)
    seq = [0]
    log = []
    law_days: dict[str, list[tuple[str, int]]] = {}
    parent = None
    main_tip = None
    future: list[dict] = []
    plans = plan(chs)
    days_of: dict[str, list[str]] = {}
    for cm in plans:
        if cm['kind'] == 'law':
            days_of.setdefault(cm['law'], []).append(cm['day'])
    TAGS.clear()
    for law, ds in days_of.items():
        for d in ds:
            TAGS[law_tag(law) if len(ds) == 1 else f'{law_tag(law)}/{d}'] = 0
    for cm in plans:
        if cm['day'] > today:
            future.append(cm)
            continue
        author, msg = message(cm)
        ops = [(f'{c["b"]["act"]["slug"]}/{c["b"]["files"][c["apa"]]}', c['text']) for c in cm['items']]
        parent = fi.commit('refs/heads/main', author, commit_date(cm['day'], seq), msg, parent, ops)
        if cm['kind'] == 'law':
            law_days.setdefault(cm['law'], []).append((cm['day'], parent))
        log.append({'day': cm['day'], 'kind': cm['kind'], 'law': cm['law'], 'items': len(cm['items']), 'mark': parent,
                    'clamped': cm['day'] < '1970-01-01', 'branch': 'main'})
    # Documentation, tables, tools and the record of how it was made come last on main, by Lexifina, dated the
    # build day (the day the data was retrieved), so the same data gives the same hashes on any later day.
    from reproduce import doc_files
    files = doc_files(built, chs, log, law_days, today, future)
    when = commit_date(today, seq)
    parent = fi.commit('refs/heads/main', COMMITTER, when,
                       'Dokumentation, Tabellen, Werkzeuge und REPRODUCE.md\n\nDocumentation, tables, tools and REPRODUCE.md\n',
                       parent, sorted(files.items()))
    main_tip = parent
    fut_parent = parent
    for cm in future:
        author, msg = message(cm)
        ops = [(f'{c["b"]["act"]["slug"]}/{c["b"]["files"][c["apa"]]}', c['text']) for c in cm['items']]
        fut_parent = fi.commit('refs/heads/future', author, commit_date(cm['day'], seq), msg, fut_parent, ops)
        if cm['kind'] == 'law':
            law_days.setdefault(cm['law'], []).append((cm['day'], fut_parent))
        log.append({'day': cm['day'], 'kind': cm['kind'], 'law': cm['law'], 'items': len(cm['items']),
                    'mark': fut_parent, 'clamped': False, 'branch': 'future'})
    tags = {}
    for law, days in sorted(law_days.items()):
        if len(days) == 1:
            tags[law_tag(law)] = days[0][1]
        else:
            for day, mark in days:
                tags[f'{law_tag(law)}/{day}'] = mark
    for name, mark in sorted(tags.items()):
        fi.tag(name, mark)
    fi.finish()
    git(repo, 'checkout', '-q', '-f', 'main')
    return log, tags, {'main_tip': main_tip}


# ---------------------------------------------------------------- main

def data_day() -> str:
    files = [p for p in CACHE.iterdir() if p.name != '.gitignore'] if CACHE.exists() else []
    if not files:
        raise SystemExit('the cache is empty: give --today')
    return dt.date.fromtimestamp(max(p.stat().st_mtime for p in files)).isoformat()


def build_all(acts: list[dict], offline: bool) -> tuple[list[dict], dict, list[dict]]:
    texts = TEXTS
    built = []
    for a in acts:
        b = build_act(a, offline, texts)
        built.append(b)
        print(f'{a["slug"]}: {len(b["docs"])} documents, {len(b["tl"])} provisions, '
              f'{sum(len(s) for s in b["tl"].values())} versions in force; {len(b["problems"])} data notes; '
              f'{NET["count"]} requests so far', flush=True)
    chs = changes(built, texts)
    return built, texts, chs


def main():
    sys.modules['build'] = sys.modules[__name__]   # reproduce.py imports this module by name
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', default=str(ROOT.parent / 'austria-law'))
    ap.add_argument('--offline', action='store_true', help='read only the cache; fail on anything not cached')
    ap.add_argument('--today', required=True, help='the build day: the day the data was retrieved')
    ap.add_argument('--only', default=None, help='comma-separated Gesetzesnummern (default: all acts)')
    ap.add_argument('--provisions', default=None,
                    help='for tests only: keep just these ArtikelParagraphAnlage values, separated by ";"')
    ap.add_argument('--fetch-only', action='store_true', help='fill the cache and stop')
    ap.add_argument('--verify-rebuild', action='store_true',
                    help='build again into a temporary folder from the cache and compare every hash with --repo')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    acts = all_acts()
    if args.provisions:
        ONLY_APA.update(x.strip() for x in args.provisions.split(';'))
    if args.only:
        want = set(args.only.split(','))
        acts = [a for a in acts if a['nr'] in want]
    if args.verify_rebuild:
        verify_rebuild(args)
        return
    if args.fetch_only:
        texts: dict = {}
        for a in acts:
            build_act(a, args.offline, texts)
            print(f'{a["slug"]}: cached; {NET["count"]} requests so far', flush=True)
        return
    t0 = time.time()
    built, texts, chs = build_all(acts, args.offline)
    for b in built:
        for p in b['problems']:
            print(f'   {b["act"]["slug"]}: {p}')
    log, tags, info = write_repo(Path(args.repo), built, chs, args.today)
    n_fut = sum(1 for c in log if c['branch'] == 'future')
    print(f'repo: {len(log) - n_fut} commits on main + 1 documentation commit, {n_fut} on future, {len(tags)} tags, '
          f'{len(chs)} file changes -> {args.repo} ({time.time() - t0:.0f} s)')


def verify_rebuild(args):
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [sys.executable, '-X', 'utf8', str(HERE / 'build.py'), '--offline', '--repo', tmp, '--today', args.today]
        if args.only:
            cmd += ['--only', args.only]
        if args.provisions:
            cmd += ['--provisions', args.provisions]
        out = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        if out.returncode:
            raise SystemExit(out.stderr)

        def refs(r):
            return dict(l.split(' ', 1)[::-1] for l in git(Path(r), 'show-ref').split('\n') if l)
        a, b = refs(args.repo), refs(tmp)
        main_a = git(Path(args.repo), 'log', '--format=%H', 'main').split()
        main_b = git(Path(tmp), 'log', '--format=%H', 'main').split()
        rec = {'identical': a == b, 'refs': len(a), 'main': a.get('refs/heads/main'),
               'rebuilt_main': b.get('refs/heads/main'), 'commits_main': len(main_a),
               'history_tip': main_a[1] if len(main_a) > 1 else None,
               'history_identical': main_a[1:] == main_b[1:], 'future': a.get('refs/heads/future')}
        print(json.dumps(rec, indent=1))
        p = HERE / 'verification.json'
        ver = json.loads(p.read_text(encoding='utf-8')) if p.exists() else {}
        ver['rebuild'] = {k: rec[k] for k in ('identical', 'history_identical', 'history_tip', 'commits_main', 'refs')}
        p.write_text(json.dumps(ver, indent=1, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
        for f in Path(tmp).rglob('*'):
            os.chmod(f, 0o700)
        raise SystemExit(0 if rec['identical'] else 1)


if __name__ == '__main__':
    main()
