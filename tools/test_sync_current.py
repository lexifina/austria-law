"""Offline checks for law snapshots, incremental refresh and atomic publication."""

import contextlib
import copy
import io
from pathlib import Path
import tempfile
import unittest
from urllib.parse import parse_qs, urlsplit

import sync_current as sync
from test_catalog import FIXTURE, page


def law_html(
    nr="20000001", date="2026-11-01", text="Original wording &amp; punctuation."
):
    display = ".".join(reversed(date.split("-")))
    return (
        f"<html><head><title>RIS - Test - Bundesrecht konsolidiert, Fassung vom {display}</title></head>"
        f'<body><form action="/GeltendeFassung.wxe?Gesetzesnummer={nr}&amp;FassungVom={date}">'
        '<input value="transient token">'
        '<div class="documentContent"><h2 class="onlyScreenreader">§ 0</h2><div><h3>Langtitel</h3><p>Title</p></div></div>'
        '<div class="documentContent"><h2 class="onlyScreenreader">§ 1</h2>'
        f'<div id="transient-id"><h3>Text</h3><p>{text}</p><a onclick="dynamic()" href="/source">Source</a></div></div>'
        "</form></body></html>"
    ).encode()


def ref(nr):
    result = copy.deepcopy(FIXTURE)
    md = result["Data"]["Metadaten"]
    md["Technisch"]["ID"] = "NOR" + nr
    md["Bundesrecht"]["BrKons"]["Gesetzesnummer"] = nr
    return result


class FakeClient:
    def __init__(self, laws, changed=(), starts=(), ends=(), fail=None, deleted=False):
        self.laws, self.changed, self.starts, self.ends = laws, changed, starts, ends
        self.fail, self.deleted, self.downloads = fail, deleted, []

    def get(self, url, **kwargs):
        q = parse_qs(urlsplit(url).query)
        meta = {"url": url, "sha256": "test", "retrieved_at": "test"}
        if "GeltendeFassung" in url:
            nr, date = q["Gesetzesnummer"][0], q["FassungVom"][0]
            self.downloads.append(nr)
            if nr == self.fail:
                raise ValueError("simulated interruption")
            return law_html(
                nr,
                date,
                "Updated wording." if nr in self.changed else "Original wording.",
            ), meta
        if "/History?" in url:
            rows = (
                [{"DeletedDocument": "unknown"}]
                if self.deleted
                else [ref(nr) for nr in self.changed]
            )
        elif "Fassung.VonInkrafttretensdatum" in q:
            rows = [ref(nr) for nr in self.starts]
            for row in rows:
                row["Data"]["Metadaten"]["Bundesrecht"]["BrKons"][
                    "Inkrafttretensdatum"
                ] = q["Fassung.BisInkrafttretensdatum"][0]
        elif "Fassung.VonAusserkrafttretensdatum" in q:
            rows = [ref(nr) for nr in self.ends]
            for row in rows:
                row["Data"]["Metadaten"]["Bundesrecht"]["BrKons"][
                    "Ausserkrafttretensdatum"
                ] = q["Fassung.BisAusserkrafttretensdatum"][0]
        else:
            rows = [ref(nr) for nr in self.laws]
        return page(rows), meta


class SyncTests(unittest.TestCase):
    def run_sync(self, root, date, client):
        with contextlib.redirect_stdout(io.StringIO()):
            return sync.sync(root, date, client, lambda *args: None)

    def test_extract_keeps_words_and_resolves_links(self):
        raw, labels = sync.extract(law_html(), "20000001", "2026-11-01")
        self.assertEqual(labels, ["§ 0", "§ 1"])
        self.assertIn(b"Original wording &amp; punctuation.", raw)
        self.assertIn(b'href="https://ogd.ris.bka.gv.at/source"', raw)
        self.assertNotIn(b"onclick", raw)
        self.assertNotIn(b"transient", raw)

    def test_wrong_law_or_date_rejected(self):
        for nr, date in [("20000002", "2026-11-01"), ("20000001", "2026-11-08")]:
            with self.assertRaises(ValueError):
                sync.extract(law_html(), nr, date)

    def test_truncation_and_error_pages_rejected(self):
        for raw in [
            law_html()[:-10],
            b"<html><title>Error</title><body>Service unavailable</body></html>",
        ]:
            with self.assertRaises(ValueError):
                sync.extract(raw, "20000001", "2026-11-01")

    def test_repeated_source_designations_preserved(self):
        raw = law_html().replace(
            b"</form>",
            b'<div class="documentContent"><h2 class="onlyScreenreader">'
            + "§ 1".encode()
            + b"</h2><p>Another article of an amending act.</p></div></form>",
        )
        html, labels = sync.extract(raw, "20000001", "2026-11-01")
        self.assertEqual(labels.count("§ 1"), 2)
        self.assertIn(b"Another article of an amending act.", html)

    def test_active_content_inside_law_rejected(self):
        raw = law_html(text="<script>bad()</script>")
        with self.assertRaisesRegex(ValueError, "active element"):
            sync.extract(raw, "20000001", "2026-11-01")

    def test_initial_download_and_incremental_update(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = FakeClient(["20000001", "20000002", "20000003"])
            old = self.run_sync(root, "2026-11-01", first)
            self.assertEqual(len(first.downloads), 3)
            self.assertEqual(old["count"], 3)
            old_bytes = (root / "runs/2026-11-01/current/20000002.html").read_bytes()
            second = FakeClient(
                ["20000001", "20000002", "20000003"], changed=["20000002"]
            )
            new = self.run_sync(root, "2026-11-08", second)
            self.assertEqual(second.downloads, ["20000002"])
            self.assertEqual(new["changes"], [{"nr": "20000002", "change": "changed"}])
            self.assertEqual(
                (root / "runs/2026-11-01/current/20000002.html").read_bytes(), old_bytes
            )
            self.assertEqual(sync.read(root / "latest.json")["as_of"], "2026-11-08")

    def test_effective_and_expiring_provisions_trigger_refresh(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_sync(root, "2026-11-01", FakeClient(["20000001", "20000002"]))
            second = FakeClient(
                ["20000001", "20000002"], starts=["20000001"], ends=["20000002"]
            )
            result = self.run_sync(root, "2026-11-08", second)
            self.assertEqual(second.downloads, ["20000001", "20000002"])
            self.assertEqual(result["changes"], [])

    def test_added_and_removed_instruments(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_sync(root, "2026-11-01", FakeClient(["20000001"]))
            result = self.run_sync(root, "2026-11-08", FakeClient(["20000002"]))
            self.assertEqual(
                result["changes"],
                [
                    {"nr": "20000002", "change": "added"},
                    {"nr": "20000001", "change": "removed"},
                ],
            )

    def test_failed_update_preserves_published_generation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_sync(root, "2026-11-01", FakeClient(["20000001"]))
            latest = (root / "latest.json").read_bytes()
            with self.assertRaisesRegex(ValueError, "interruption"):
                self.run_sync(
                    root,
                    "2026-11-08",
                    FakeClient(["20000001", "20000002"], fail="20000002"),
                )
            self.assertEqual((root / "latest.json").read_bytes(), latest)
            self.assertFalse((root / "runs/2026-11-08/manifest.json").exists())

    def test_unmapped_deletion_forces_full_reconciliation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_sync(root, "2026-11-01", FakeClient(["20000001", "20000002"]))
            client = FakeClient(["20000001", "20000002"], deleted=True)
            result = self.run_sync(root, "2026-11-08", client)
            self.assertTrue(result["full_reconciliation"])
            self.assertEqual(len(client.downloads), 2)

    def test_verified_export_and_hash_failure(self):
        import export_current, clean_current

        with tempfile.TemporaryDirectory() as tmp:
            root, checkout, candidate = (
                Path(tmp) / "sync",
                Path(tmp) / "checkout",
                Path(tmp) / "clean",
            )
            root.mkdir()
            self.run_sync(root, "2026-11-01", FakeClient(["20000001"]))
            clean_current.build(root / "runs/2026-11-01", candidate)
            with self.assertRaises(FileNotFoundError):
                export_current.export(candidate, checkout)
            clean_current.approve(
                candidate,
                "test reviewer",
                "Inspected fixture wording, source links and metadata.",
            )
            self.assertEqual(export_current.export(candidate, checkout), 1)
            before = (checkout / "data/current/20000001/par-0001.md").read_bytes()
            (candidate / "20000001/par-0001.md").write_bytes(b"corrupted")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                export_current.export(candidate, checkout)
            self.assertEqual(
                (checkout / "data/current/20000001/par-0001.md").read_bytes(), before
            )

    def test_completed_date_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_sync(root, "2026-11-01", FakeClient(["20000001"]))
            client = FakeClient([], fail="20000001")
            self.assertEqual(self.run_sync(root, "2026-11-01", client)["count"], 1)
            self.assertEqual(client.downloads, [])

    def test_missing_notice_stops_before_network(self):
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            argv = [
                "sync_current.py",
                "--root",
                str(root),
                "--date",
                "2026-11-01",
                "--notice-file",
                str(root / "not-sent.json"),
            ]
            with patch("sys.argv", argv), patch("urllib.request.urlopen") as request:
                with (
                    contextlib.redirect_stdout(io.StringIO()),
                    self.assertRaisesRegex(ValueError, "not been recorded"),
                ):
                    sync.main()
                request.assert_not_called()
            self.assertFalse((root / ".running").exists())
            self.assertEqual(sync.read(root / "status.json")["phase"], "failed")

    def test_job_does_not_open_pr_for_unchanged_snapshot(self):
        import run_current_job, clean_current
        from unittest.mock import patch

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.run_sync(root, "2026-11-01", FakeClient(["20000001"]))
            clean_current.build(root / "runs/2026-11-01", root / "first")
            self.run_sync(root, "2026-11-08", FakeClient(["20000001"]))
            argv = [
                "run_current_job.py",
                "--root",
                str(root),
                "--date",
                "2026-11-08",
                "--notice-file",
                str(root / "notice.json"),
                "--previous",
                str(root / "first"),
            ]
            with patch("sys.argv", argv), patch("subprocess.run") as network:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(run_current_job.main(), 0)
                network.assert_not_called()
            self.assertEqual(
                sync.read(root / "job-2026-11-08.json")["phase"], "no_changes"
            )

    def test_boundary_query_names(self):
        url = sync.changes_url("starts", "2026-11-01", "2026-11-08", 1)
        q = parse_qs(urlsplit(url).query)
        self.assertEqual(q["Fassung.VonInkrafttretensdatum"], ["2026-11-01"])
        self.assertEqual(q["Fassung.BisInkrafttretensdatum"], ["2026-11-08"])
        q = parse_qs(
            urlsplit(sync.changes_url("history", "2026-11-01", "2026-11-08", 1)).query
        )
        self.assertEqual(q["IncludeDeletedDocuments"], ["True"])


if __name__ == "__main__":
    unittest.main()
