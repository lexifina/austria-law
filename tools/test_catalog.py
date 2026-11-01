"""Offline regression checks for catalog completeness and RIS query semantics."""
import contextlib
import copy
import datetime as dt
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

import catalog

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/federal-title.json').read_text(encoding='utf-8'))
DATE = '2026-11-01'


def ref(n):
    value = copy.deepcopy(FIXTURE)
    md = value['Data']['Metadaten']
    md['Technisch']['ID'] = f'NOR{n:08}'
    md['Bundesrecht']['BrKons']['Gesetzesnummer'] = f'{20000000 + n:08}'
    return value


def page(refs, total=None, number=1, size=100):
    return json.dumps({'OgdSearchResult': {'OgdDocumentResults': {
        'Hits': {'#text': str(len(refs) if total is None else total),
                 '@pageNumber': str(number), '@pageSize': str(size)},
        'OgdDocumentReference': refs,
    }}}).encode()


class CatalogTests(unittest.TestCase):
    def collect(self, pages):
        def get(url):
            number = int(parse_qs(urlsplit(url).query)['Seitennummer'][0])
            return pages[number - 1], {'url': url, 'sha256': 'fixture', 'retrieved_at': 'fixture'}
        with contextlib.redirect_stdout(io.StringIO()):
            return catalog.discover(['federal'], DATE, get)

    def test_query_uses_nested_ris_parameters(self):
        q = parse_qs(urlsplit(catalog.query_url('federal', DATE, 2)).query)
        self.assertEqual(q['Fassung.FassungVom'], [DATE])
        self.assertEqual(q['Abschnitt.Typ'], ['Paragraph'])
        self.assertEqual(q['Abschnitt.Von'], ['0'])
        self.assertEqual(q['Abschnitt.Bis'], ['0'])
        self.assertEqual(q['Seitennummer'], ['2'])
        self.assertNotIn('FassungVom', q)
        self.assertNotIn('Paragraphnummer', q)

    def test_live_fixture_preserves_source_and_dated_full_text_link(self):
        result = catalog.record(FIXTURE, 'federal', DATE)
        self.assertEqual(result['document_id'], FIXTURE['Data']['Metadaten']['Technisch']['ID'])
        self.assertEqual(parse_qs(urlsplit(result['full_text_url']).query)['FassungVom'], [DATE])
        self.assertIn('Xml', result['title_document_urls'])

    def test_singleton_and_zero_hits(self):
        self.assertEqual(len(catalog.parse_page(page(ref(1)), 1)[1]), 1)
        self.assertEqual(self.collect([page([])])['count'], 0)

    def test_complete_multiple_pages(self):
        result = self.collect([page([ref(i) for i in range(100)], 101), page([ref(100)], 101, 2)])
        self.assertTrue(result['complete'])
        self.assertEqual(result['count'], 101)
        self.assertEqual(result['totals'], {'federal': 101})
        self.assertEqual(len(result['queries']), 2)

    def test_truncated_page_rejected(self):
        with self.assertRaisesRegex(ValueError, 'expected 100'):
            self.collect([page([ref(1)], 101)])

    def test_changed_hit_count_rejected(self):
        with self.assertRaisesRegex(ValueError, 'hit count changed'):
            self.collect([page([ref(i) for i in range(100)], 101), page([ref(100), ref(101)], 102, 2)])

    def test_repeated_document_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            self.collect([page([ref(i) for i in range(100)], 101), page([ref(0)], 101, 2)])

    def test_repeated_law_rejected(self):
        other = ref(2)
        other['Data']['Metadaten']['Bundesrecht']['BrKons']['Gesetzesnummer'] = '20000001'
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            self.collect([page([ref(1), other])])

    def test_silently_ignored_filter_rejected(self):
        value = ref(1)
        value['Data']['Metadaten']['Bundesrecht']['BrKons']['ArtikelParagraphAnlage'] = '§ 1'
        with self.assertRaisesRegex(ValueError, 'ignored'):
            self.collect([page([value])])

    def test_future_and_expired_title_rejected(self):
        for start, end in [('2027-01-01', None), ('2000-01-01', '2026-10-31')]:
            value = ref(1)
            norm = value['Data']['Metadaten']['Bundesrecht']['BrKons']
            norm['Inkrafttretensdatum'], norm['Ausserkrafttretensdatum'] = start, end
            with self.assertRaisesRegex(ValueError, 'not in force'):
                self.collect([page([value])])

    def test_source_title_without_start_date_is_retained_as_unknown(self):
        value = json.loads((Path(__file__).parent / 'fixtures/undated-title.json').read_text())
        result = catalog.record(value, 'federal', DATE)
        self.assertEqual(result['nr'], '10001518')
        self.assertIsNone(result['in_force_from'])
        self.assertEqual(result['validity_status'], 'unknown_missing_start_date')
        self.assertIn('späteren Zeitpunkt', result['ris_notes'])

    def test_end_date_is_inclusive(self):
        value = ref(1)
        value['Data']['Metadaten']['Bundesrecht']['BrKons']['Ausserkrafttretensdatum'] = DATE
        self.assertEqual(self.collect([page([value])])['count'], 1)

    def test_wrong_application_and_page_rejected(self):
        value = ref(1)
        value['Data']['Metadaten']['Technisch']['Applikation'] = 'LrKons'
        with self.assertRaisesRegex(ValueError, 'wrong application'):
            self.collect([page([value])])
        with self.assertRaisesRegex(ValueError, 'pagination'):
            catalog.parse_page(page([ref(1)], number=2), 1)

    def test_api_error_rejected(self):
        with self.assertRaisesRegex(ValueError, 'RIS error'):
            catalog.parse_page(b'{"OgdSearchResult":{"Error":{"Message":"bad query"}}}', 1)

    def test_offline_missing_cache_does_not_use_network(self):
        with tempfile.TemporaryDirectory() as tmp, patch('urllib.request.urlopen') as request:
            with self.assertRaisesRegex(ValueError, 'not cached'):
                catalog.Client(Path(tmp), offline=True).get('https://example.invalid/')
            request.assert_not_called()

    def test_cache_integrity_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            import hashlib
            url = 'https://example.invalid/'
            key = hashlib.sha256(url.encode()).hexdigest()
            root = Path(tmp)
            (root / (key + '.json')).write_text('{}')
            (root / (key + '.meta.json')).write_text(json.dumps({'url': url, 'sha256': 'wrong'}))
            with self.assertRaisesRegex(ValueError, 'integrity'):
                catalog.Client(root, offline=True).get(url)

    def test_access_hours_and_holidays(self):
        self.assertFalse(catalog.allowed(dt.datetime(2026, 11, 2, 12)))
        self.assertTrue(catalog.allowed(dt.datetime(2026, 11, 2, 20)))
        self.assertTrue(catalog.allowed(dt.datetime(2026, 11, 2, 4, 59)))
        self.assertFalse(catalog.allowed(dt.datetime(2026, 11, 2, 5)))
        self.assertTrue(catalog.allowed(dt.datetime(2026, 11, 1, 12)))
        self.assertTrue(catalog.allowed(dt.datetime(2026, 12, 8, 12)))
        self.assertTrue(catalog.allowed(dt.datetime(2026, 4, 6, 12)))

    def test_network_requires_notice_and_user_agent(self):
        with patch('sys.argv', ['catalog.py', '--date', DATE, '--output', 'unused.json']):
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                catalog.main()
        self.assertEqual(error.exception.code, 2)


if __name__ == '__main__':
    unittest.main()
