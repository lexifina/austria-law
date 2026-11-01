"""Discover current RIS consolidated-law title records without rebuilding git history.

Standard library only. See CATALOG.md for scope, notice requirements and commands.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

API = 'https://data.bka.gv.at/ris/api/v2.6/'
FAQ = API
SOURCE = 'Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt'
CORE = {'10000138': 'b-vg', '10001597': 'dsg'}


def as_list(value):
    return value if isinstance(value, list) else ([] if value is None else [value])


def easter(year):
    a, b, c = year % 19, year // 100, year % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    n = h + l - 7 * m + 114
    return dt.date(year, n // 31, n % 31 + 1)


def allowed(now):
    """RIS bulk access hours, evaluated in Europe/Vienna."""
    day = now.date()
    fixed = {(1, 1), (1, 6), (5, 1), (8, 15), (10, 26), (11, 1), (12, 8), (12, 25), (12, 26)}
    moving = {easter(day.year) + dt.timedelta(days=n) for n in (1, 39, 50, 60)}
    return (now.hour >= 20 or now.hour < 5 or now.weekday() >= 5
            or (day.month, day.day) in fixed or day in moving)


def query_url(scope, date, page):
    query = {
        'Applikation': 'BrKons',
        'Fassung.FassungVom': date,
        'Abschnitt.Von': '0', 'Abschnitt.Bis': '0', 'Abschnitt.Typ': 'Paragraph',
        'DokumenteProSeite': 'OneHundred', 'Seitennummer': str(page),
    }
    return API + 'Bundesrecht?' + urllib.parse.urlencode(query)


def parse_page(raw, page, page_size=100):
    result = json.loads(raw)['OgdSearchResult']
    if 'Error' in result:
        raise ValueError(f'RIS error: {result["Error"]}')
    result = result['OgdDocumentResults']
    hits = result['Hits']
    total = int(hits['#text'])
    if total < 0 or int(hits['@pageNumber']) != page or int(hits['@pageSize']) != page_size:
        raise ValueError(f'unexpected pagination: {hits}')
    refs = as_list(result.get('OgdDocumentReference'))
    expected = min(page_size, max(0, total - (page - 1) * page_size))
    if len(refs) != expected:
        raise ValueError(f'page {page}: {len(refs)} records, expected {expected}')
    return total, refs


def record(ref, scope, date):
    md = ref['Data']['Metadaten']
    app = 'BrKons'
    if md['Technisch']['Applikation'] != app:
        raise ValueError('RIS returned the wrong application')
    law = md['Bundesrecht']
    norm = law[app]
    if norm.get('ArtikelParagraphAnlage') != '§ 0' or norm.get('Dokumenttyp') != 'Norm':
        raise ValueError('RIS ignored the title-record filter')
    nr = norm['Gesetzesnummer']
    if not re.fullmatch(r'\d{8}', nr):
        raise ValueError(f'invalid Gesetzesnummer: {nr!r}')
    start, end = norm.get('Inkrafttretensdatum'), norm.get('Ausserkrafttretensdatum')
    if not start or start > date or (end and end < date):
        raise ValueError(f'{nr}: title record is not in force on {date}')
    # Parse the dates too, rather than accepting malformed lexical comparisons.
    dt.date.fromisoformat(start)
    if end:
        dt.date.fromisoformat(end)
    urls = {}
    for content in as_list(ref['Data']['Dokumentliste']['ContentReference']):
        if content.get('ContentType') == 'MainDocument':
            urls.update({x['DataType']: x['Url'] for x in as_list(content['Urls']['ContentUrl'])})
    full_url = norm['GesamteRechtsvorschriftUrl']
    parts = urllib.parse.urlsplit(full_url)
    params = urllib.parse.parse_qs(parts.query)
    params['FassungVom'] = [date]
    full_url = urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(params, doseq=True)))
    return {
        'id': f'at/{scope}/{nr}', 'jurisdiction': scope, 'nr': nr,
        'slug': CORE.get(nr, f'ris-{nr}'),
        'kurztitel': law.get('Kurztitel', '').strip(),
        'titel_html': law.get('Titel', ''), 'abkuerzung': norm.get('Abkuerzung'),
        'typ': norm.get('Typ'), 'kundmachungsorgan': norm.get('Kundmachungsorgan'),
        'in_force_from': start, 'in_force_to': end, 'document_id': md['Technisch']['ID'],
        'document_url': md['Allgemein'].get('DokumentUrl'),
        'eli': norm.get('Eli') or law.get('Eli'),
        'full_text_url': full_url, 'title_document_urls': urls,
    }


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_bytes(data)
    os.replace(tmp, path)


class Client:
    """One sequential connection with a two-second pause after every response."""
    def __init__(self, cache, offline=False, user_agent=None):
        self.cache, self.offline, self.user_agent = cache, offline, user_agent
        self.last = 0.0

    def get(self, url):
        key = hashlib.sha256(url.encode()).hexdigest()
        body_path = self.cache / (key + '.json')
        meta_path = self.cache / (key + '.meta.json')
        if body_path.exists() and meta_path.exists():
            body = body_path.read_bytes()
            meta = json.loads(meta_path.read_text(encoding='utf-8'))
            if meta['url'] != url or meta['sha256'] != hashlib.sha256(body).hexdigest():
                raise ValueError(f'cache integrity failure: {body_path}')
            return body, meta
        if self.offline:
            raise ValueError(f'not cached: {url}')
        for attempt in range(4):
            time.sleep(max(0, self.last + 2 - time.monotonic()))
            while not allowed(dt.datetime.now(ZoneInfo('Europe/Vienna'))):
                print('Outside RIS bulk access hours; checking again in 30 seconds.', flush=True)
                time.sleep(30)
            try:
                request = urllib.request.Request(url, headers={
                    'User-Agent': self.user_agent, 'Accept-Encoding': 'gzip', 'Accept': 'application/json',
                })
                try:
                    with urllib.request.urlopen(request, timeout=120) as response:
                        body = response.read()
                        if response.headers.get('Content-Encoding') == 'gzip':
                            body = gzip.decompress(body)
                finally:
                    self.last = time.monotonic()
                # Do not persist an HTTP-200 error or HTML page as a successful result.
                result = json.loads(body)['OgdSearchResult']
                if 'OgdDocumentResults' not in result:
                    raise ValueError(f'RIS returned no results: {result}')
                meta = {'url': url, 'sha256': hashlib.sha256(body).hexdigest(),
                        'retrieved_at': dt.datetime.now(dt.timezone.utc).isoformat()}
                atomic_write(body_path, body)
                atomic_write(meta_path, (json.dumps(meta, indent=2) + '\n').encode())
                return body, meta
            except urllib.error.HTTPError as exc:
                if exc.code not in (429, 500, 502, 503, 504) or attempt == 3:
                    raise
                retry = exc.headers.get('Retry-After', '')
                try:
                    wait = float(retry)
                except ValueError:
                    try:
                        from email.utils import parsedate_to_datetime
                        wait = (parsedate_to_datetime(retry) - dt.datetime.now(dt.timezone.utc)).total_seconds()
                    except (ValueError, TypeError):
                        wait = 0
                time.sleep(max(30 * (attempt + 1), wait))
            except (urllib.error.URLError, TimeoutError):
                if attempt == 3:
                    raise
                time.sleep(30 * (attempt + 1))
        raise AssertionError('unreachable')


def discover(scopes, date, get):
    records, queries, totals = [], [], {}
    for scope in scopes:
        expected_total, seen, seen_laws = None, set(), set()
        page = 1
        while True:
            url = query_url(scope, date, page)
            raw, provenance = get(url)
            total, refs = parse_page(raw, page)
            if expected_total is None:
                expected_total = total
            if total != expected_total:
                raise ValueError(f'{scope}: hit count changed during download; use a fresh cache')
            for ref in refs:
                row = record(ref, scope, date)
                if row['document_id'] in seen or row['id'] in seen_laws:
                    raise ValueError(f'{scope}: duplicate title/document across pages; use a fresh cache')
                seen.add(row['document_id'])
                seen_laws.add(row['id'])
                records.append(row)
            queries.append({'scope': scope, 'page': page, 'hits': total, **provenance})
            print(f'{scope}: page {page}/{max(1, math.ceil(total / 100))}, {len(seen)}/{total} titles', flush=True)
            if len(seen) == total:
                break
            page += 1
        totals[scope] = expected_total
    return {
        'schema_version': 1, 'as_of': date, 'complete': True,
        'coverage': 'All RIS consolidated-law § 0 title records in force on as_of in the listed jurisdictions; '
                    'not a full-text or historical-version download, nor all Austrian sources of law.',
        'source': SOURCE, 'source_url': 'https://www.ris.bka.gv.at/',
        'license': 'CC-BY-4.0',
        'attribution': 'Quelle: ' + SOURCE + ', https://www.ris.bka.gv.at, CC BY 4.0. '
                       'Metadata reorganised; full legal text not included.',
        'jurisdictions': list(scopes), 'totals': totals, 'count': len(records),
        'records': sorted(records, key=lambda r: r['id']), 'queries': queries,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', required=True, type=dt.date.fromisoformat)
    parser.add_argument('--scope', choices=['federal'], default='federal')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cache', type=Path, default=Path('tools/.catalog-cache'))
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--notice-sent', action='store_true', help='affirm that the RIS bulk-download notice has been sent')
    parser.add_argument('--user-agent', help='application name/version and a contact URL or email')
    parser.add_argument('--acts-output', type=Path, help='optional federal acts_extra.json discovery list for the history builder')
    args = parser.parse_args()
    if not args.offline and (not args.notice_sent or not args.user_agent):
        parser.error('network access requires --notice-sent and --user-agent; see CATALOG.md and ' + FAQ)
    if args.date > dt.datetime.now(ZoneInfo('Europe/Vienna')).date():
        parser.error('--date must not be in the future')
    if args.acts_output and args.acts_output.resolve() == args.output.resolve():
        parser.error('--acts-output and --output must be different files')
    scopes = [args.scope]
    # Cache namespaces prevent a later snapshot from silently reusing an older query.
    cache = args.cache / args.date.isoformat()
    cache.mkdir(parents=True, exist_ok=True)
    lock = cache / '.running'
    try:
        lock.mkdir()
    except FileExistsError:
        parser.error(f'another catalog process may be running; inspect {lock} before removing a stale lock')
    try:
        client = Client(cache, args.offline, args.user_agent)
        catalog = discover(scopes, args.date.isoformat(), client.get)
        if args.acts_output:
            extras = [{'nr': r['nr'], 'slug': r['slug']} for r in catalog['records']
                      if r['jurisdiction'] == 'federal' and r['nr'] not in CORE]
            atomic_write(args.acts_output, (json.dumps(extras, indent=2) + '\n').encode())
        atomic_write(args.output, (json.dumps(catalog, ensure_ascii=False, indent=2) + '\n').encode())
        print(f'Wrote {catalog["count"]} title records to {args.output}')
    finally:
        lock.rmdir()


if __name__ == '__main__':
    main()
