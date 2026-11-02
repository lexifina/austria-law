"""Resumable initial federal-law text snapshots and incremental current-law refreshes.

Does not rebuild amendment history. Network access requires a record of a sent RIS notice.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
from html import escape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
from zoneinfo import ZoneInfo

import catalog

UA = 'austria-law-catalog/1.0 (+https://github.com/axhoff/austria-law)'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


def save(path, data):
    catalog.atomic_write(path, (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode())


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


class LawHTML(HTMLParser):
    """Extract RIS documentContent blocks, preserving text and presentation structure.

    Remove active content and transient element IDs; resolve source links without fetching assets.
    """
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source, self.depth = source, 0
        self.blocks, self.parts, self.labels = [], [], []
        self.label, self.in_label, self.title, self.in_title = '', False, '', False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'title':
            self.in_title = True
        if tag == 'div' and self.depth == 0 and 'documentContent' in values.get('class', '').split():
            self.depth, self.parts, self.label = 1, [], ''
        elif self.depth and tag == 'div':
            self.depth += 1
        if not self.depth:
            return
        if tag in ('script', 'iframe', 'object', 'embed', 'form', 'input'):
            raise ValueError(f'unexpected active element in RIS law content: {tag}')
        if tag == 'h2' and 'onlyScreenreader' in values.get('class', '').split():
            self.in_label = True
        kept = []
        for key, value in attrs:
            if key == 'id' or key.lower().startswith('on'):
                continue
            if key in ('href', 'src') and value:
                value = urllib.parse.urljoin(self.source, value)
                if urllib.parse.urlsplit(value).scheme not in ('http', 'https', 'mailto'):
                    raise ValueError('unexpected non-web link in legal content')
            if value is not None:
                kept.append(f' {key}="{escape(value, quote=True)}"')
        self.parts.append('<' + tag + ''.join(kept) + '>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if not self.depth:
            return
        if tag not in VOID:
            self.parts.append('</' + tag + '>')
        if tag == 'h2':
            self.in_label = False
        if tag == 'div':
            self.depth -= 1
            if self.depth == 0:
                self.blocks.append(''.join(self.parts))
                self.labels.append(' '.join(self.label.split()))

    def handle_data(self, value):
        if self.in_title:
            self.title += value
        if self.depth:
            self.parts.append(escape(value))
        if self.depth and self.in_label:
            self.label += value


def full_url(nr, date):
    return 'https://ogd.ris.bka.gv.at/GeltendeFassung.wxe?' + urllib.parse.urlencode({
        'Abfrage': 'Bundesnormen', 'Gesetzesnummer': nr, 'FassungVom': date,
    })


def extract(raw, nr, date):
    source = full_url(nr, date)
    parser = LawHTML(source)
    parser.feed(raw.decode('utf-8-sig'))
    parser.close()
    wanted = dt.date.fromisoformat(date).strftime('%d.%m.%Y')
    if wanted not in parser.title or 'Bundesrecht konsolidiert' not in parser.title:
        raise ValueError(f'{nr}: RIS did not return the requested date/application')
    # Identity must be present in the page's form action, not merely in a navigation link.
    match = re.search(rb'<form\b[^>]*\baction="([^"]+)"', raw, re.I)
    from html import unescape
    action = urllib.parse.parse_qs(urllib.parse.urlsplit(unescape(match.group(1).decode()) if match else '').query)
    if action.get('Gesetzesnummer') != [nr] or action.get('FassungVom') != [date]:
        raise ValueError(f'{nr}: RIS returned a different instrument/date')
    if parser.depth or not parser.blocks or parser.labels[0] != '§ 0':
        raise ValueError(f'{nr}: missing or incomplete RIS document blocks')
    if any(not label for label in parser.labels) or not raw.rstrip().lower().endswith(b'</html>'):
        raise ValueError(f'{nr}: missing designations or truncated HTML')
    # RIS can repeat an article designation from separate amending acts; retain every block in source order.
    # A successful HTTP response with an RIS error page must never become a law file.
    body = '\n'.join(parser.blocks)
    title = escape(parser.title.strip())
    html = (f'<!doctype html>\n<html lang="de"><head><meta charset="utf-8"><title>{title}</title></head>\n'
            f'<body>\n{body}\n</body></html>\n').encode()
    return html, parser.labels


def changes_url(kind, start, end, page):
    if kind == 'history':
        query = {'Anwendung': 'Bundesnormen', 'AenderungenVon': start, 'AenderungenBis': end,
                 'IncludeDeletedDocuments': 'True'}
        endpoint = 'History'
    else:
        field = 'Inkrafttretensdatum' if kind == 'starts' else 'Ausserkrafttretensdatum'
        query = {'Applikation': 'BrKons', f'Fassung.Von{field}': start, f'Fassung.Bis{field}': end}
        endpoint = 'Bundesrecht'
    query.update({'DokumenteProSeite': 'OneHundred', 'Seitennummer': str(page)})
    return catalog.API + endpoint + '?' + urllib.parse.urlencode(query)


def changed_laws(client, start, end):
    laws, queries, uncertain = set(), [], False
    for kind in ('history', 'starts', 'ends'):
        seen, expected, page = set(), None, 1
        while True:
            url = changes_url(kind, start, end, page)
            raw, provenance = client.get(url)
            total, refs = catalog.parse_page(raw, page)
            if expected is None:
                expected = total
            if total != expected:
                raise ValueError(f'{kind}: changed pagination count; repeat with a fresh cache')
            for ref in refs:
                # Deleted documents may no longer carry a Gesetzesnummer. Conservatively reconcile all texts.
                md = ref.get('Data', {}).get('Metadaten', {})
                doc_id = md.get('Technisch', {}).get('ID')
                nr = md.get('Bundesrecht', {}).get('BrKons', {}).get('Gesetzesnummer')
                if not doc_id or not nr:
                    uncertain = True
                if doc_id:
                    if doc_id in seen:
                        raise ValueError(f'{kind}: repeated document across pages')
                    seen.add(doc_id)
                if nr:
                    if not re.fullmatch(r'\d{8}', nr):
                        raise ValueError('invalid change-feed Gesetzesnummer')
                    if md.get('Technisch', {}).get('Applikation') != 'BrKons':
                        raise ValueError('wrong application in change feed')
                    if kind != 'history':
                        field = 'Inkrafttretensdatum' if kind == 'starts' else 'Ausserkrafttretensdatum'
                        value = md['Bundesrecht']['BrKons'].get(field)
                        if not value or not start <= value <= end:
                            raise ValueError('RIS ignored an effective-date range filter')
                    laws.add(nr)
            queries.append({'kind': kind, 'hits': total, 'page': page, **provenance})
            if page * 100 >= total:
                break
            page += 1
    return laws, queries, uncertain


def catalog_fingerprint(row):
    return {key: row.get(key) for key in ('nr', 'kurztitel', 'titel_html', 'abkuerzung', 'typ',
            'kundmachungsorgan', 'in_force_from', 'in_force_to', 'validity_status', 'ris_notes', 'document_id')}


def link_or_copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        target.unlink()
    try:
        os.link(source, target)
    except OSError:
        shutil.copyfile(source, target)


def check_notice_period(notice, now=None):
    """Check at request time too: waiting for an access window cannot extend a notice."""
    now=now or dt.datetime.now(ZoneInfo('Europe/Vienna'))
    start=notice.get('period_start');end=notice.get('period_end')
    if not start or not end:
        raise ValueError('sent notice needs explicit period_start and period_end before network access')
    first,last=dt.date.fromisoformat(start),dt.date.fromisoformat(end)
    if not first<=now.date()<=last:
        raise ValueError('current date is outside the announced RIS access period')


def sync(root, date, client, progress):
    run = root / 'runs' / date
    run.mkdir(parents=True, exist_ok=True)
    latest = read(root / 'latest.json') if (root / 'latest.json').exists() else None
    previous = read(root / latest['manifest']) if latest else None
    if previous and previous['as_of'] >= date:
        if previous['as_of'] == date:
            return previous
        raise ValueError('cannot replace a newer snapshot with an older one')
    progress('catalog', 0, None)
    index = catalog.discover(['federal'], date, client.get,
                             progress=lambda done, total: progress('catalog', done, total))
    save(run / 'catalog.json', index)
    old = {row['nr']: row for row in previous['records']} if previous else {}
    new = {row['nr']: row for row in index['records']}
    if previous:
        # Inclusive overlap covers delayed imports and boundary dates; queries are idempotent.
        start = (dt.date.fromisoformat(previous['as_of']) - dt.timedelta(days=2)).isoformat()
        affected, queries, reconcile_all = changed_laws(client, start, date)
        affected.update(nr for nr, row in new.items()
                        if nr not in old or catalog_fingerprint(row) != catalog_fingerprint(old[nr]['catalog']))
        if reconcile_all:
            affected.update(new)
    else:
        affected, queries, reconcile_all = set(new), [], False
    records, changes = [], []
    previous_run = root / Path(latest['manifest']).parent if latest else None
    for i, (nr, row) in enumerate(sorted(new.items()), 1):
        target = run / 'current' / (nr + '.html')
        if nr not in affected and nr in old:
            before = old[nr]
            source = previous_run / before['file']
            if digest(source.read_bytes()) != before['sha256']:
                raise ValueError(f'{nr}: previous snapshot hash mismatch')
            link_or_copy(source, target)
            entry = {**before, 'catalog': row}
        else:
            url = full_url(nr, date)
            raw, provenance = client.get(url, kind='html', validate=lambda b: extract(b, nr, date))
            html, labels = extract(raw, nr, date)
            catalog.atomic_write(target, html)
            entry = {'nr': nr, 'catalog': row, 'file': 'current/' + nr + '.html', 'sha256': digest(html),
                     'source_as_of': date, 'source': provenance, 'provisions': labels}
            before = old.get(nr)
            # The rendered wrapper's date/title may differ; the actual document blocks decide text changes.
            def block_hash(data):
                return digest(data.split(b'<body>\n', 1)[1].rsplit(b'\n</body>', 1)[0])
            unchanged = before and block_hash((previous_run / before['file']).read_bytes()) == block_hash(html)
            if not unchanged:
                changes.append({'nr': nr, 'change': 'added' if before is None else 'changed'})
            elif catalog_fingerprint(row) != catalog_fingerprint(before['catalog']):
                changes.append({'nr': nr, 'change': 'metadata'})
        records.append(entry)
        # Persist each response in the cache; retain the prior published manifest until all succeed.
        progress('texts', i, len(new))
    changes += [{'nr': nr, 'change': 'removed'} for nr in sorted(old.keys() - new.keys())]
    manifest = {'schema_version': 1, 'complete': True, 'as_of': date, 'count': len(records),
                'coverage': 'Current consolidated federal-law HTML text snapshots. External binary annexes/images '
                            'remain source links; amendment history is not reconstructed.',
                'source': catalog.SOURCE, 'license': 'CC-BY-4.0',
                'attribution': index['attribution'].replace('Metadata reorganised; full legal text not included.',
                    'Legal content extracted from RIS HTML; scripts, event handlers and transient element IDs '
                    'removed, and links resolved to absolute URLs. Legal wording unchanged.'),
                'previous_as_of': previous['as_of'] if previous else None,
                'changes': changes, 'change_queries': queries, 'full_reconciliation': reconcile_all,
                'records': records}
    save(run / 'manifest.json', manifest)
    save(root / 'latest.json', {'manifest': f'runs/{date}/manifest.json', 'as_of': date})
    return manifest


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, required=True)
    ap.add_argument('--date', type=dt.date.fromisoformat, required=True)
    ap.add_argument('--notice-file', type=Path, required=True,
                    help='JSON record of a notice actually sent: sent_at, user_agent, source_ip, weekly')
    ap.add_argument('--wait-for-notice', action='store_true')
    ap.add_argument('--offline', action='store_true')
    args = ap.parse_args()
    args.root.mkdir(parents=True, exist_ok=True)
    status = args.root / 'status.json'

    def progress(phase, done, total, **extra):
        save(status, {'phase': phase, 'completed': done, 'total': total,
                      'as_of': args.date.isoformat(), 'updated_at': dt.datetime.now(dt.timezone.utc).isoformat(), **extra})
        print(f'{phase}: {done}/{total}', flush=True)

    lock = args.root / '.running'
    try:
        lock.mkdir()
    except FileExistsError:
        ap.error(f'another sync may be running: {lock}')
    awake = None
    try:
        while not args.offline and not args.notice_file.exists():
            progress('waiting_for_notice', 0, None)
            if not args.wait_for_notice:
                raise ValueError('bulk download notice has not been recorded as sent')
            time.sleep(30)
        notice = read(args.notice_file) if args.notice_file.exists() else {}
        if not args.offline:
            for key in ('sent_at', 'user_agent', 'source_ip'):
                if not notice.get(key):
                    raise ValueError(f'notice receipt is missing {key}')
            dt.datetime.fromisoformat(notice['sent_at'])
            check_notice_period(notice)
            latest=read(args.root/'latest.json') if (args.root/'latest.json').exists() else None
            if latest and latest['as_of']<args.date.isoformat() and not notice.get('weekly'):
                raise ValueError('recurring downloads were not included in the sent notice')
        if args.date > dt.datetime.now(ZoneInfo('Europe/Vienna')).date():
            raise ValueError('snapshot date is in the future')
        if not args.offline and shutil.which('caffeinate'):
            awake = subprocess.Popen(['caffeinate', '-i', '-w', str(os.getpid())])
        cache = args.root / 'cache' / args.date.isoformat()
        cache.mkdir(parents=True, exist_ok=True)
        client = catalog.Client(cache, args.offline, notice.get('user_agent', UA),
                                before_request=lambda: check_notice_period(notice))
        manifest = sync(args.root, args.date.isoformat(), client, progress)
        progress('complete', manifest['count'], manifest['count'], manifest=f'runs/{args.date}/manifest.json')
    except BaseException as exc:
        last = read(status) if status.exists() else {}
        progress('failed', last.get('completed', 0), last.get('total'),
                 failed_phase=last.get('phase'), error=str(exc))
        raise
    finally:
        if awake is not None:
            awake.terminate()
        lock.rmdir()


if __name__ == '__main__':
    main()
