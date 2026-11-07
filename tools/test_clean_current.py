"""Regression checks for legal text preservation, identity, review gates and update diffs."""

import datetime as dt
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import clean_current as clean
import normalize_current as n
import sync_current as sync
import catalog
from test_catalog import FIXTURE
import copy


def source_run(root, date="2026-11-01", entries=None):
    entries = entries or [("§ 1", "<p>Original wording.</p>")]
    blocks = '<div class="documentContent"><h2>§ 0</h2><div><h3>Langtitel</h3><p>Test act</p></div></div>'
    for label, body in entries:
        blocks += f'<div class="documentContent"><h2>{label}</h2><div><h3>Text</h3>{body}</div></div>'
    content = ("<html><body>" + blocks + "</body></html>").encode()
    path = root / "current/20000001.html"
    path.parent.mkdir(parents=True)
    path.write_bytes(content)
    ref = copy.deepcopy(FIXTURE)
    ref["Data"]["Metadaten"]["Bundesrecht"]["BrKons"]["Gesetzesnummer"] = "20000001"
    row = catalog.record(ref, "federal", date)
    manifest = {
        "complete": True,
        "as_of": date,
        "count": 1,
        "records": [
            {
                "nr": "20000001",
                "catalog": row,
                "file": "current/20000001.html",
                "sha256": n.checksum(content),
                "source": {
                    "url": "https://example.org/source",
                    "sha256": n.checksum(content),
                    "retrieved_at": date + "T00:00:00Z",
                },
                "provisions": ["§ 0"] + [x[0] for x in entries],
            }
        ],
    }
    clean.save(root / "manifest.json", manifest)
    clean.save(root / "catalog.json", {"complete": True, "records": [row]})
    return manifest["records"][0]


class CleanTests(unittest.TestCase):
    def test_visible_text_punctuation_and_hidden_alternatives(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            r = source_run(
                root,
                entries=[
                    (
                        "§ 1",
                        '<p><span aria-hidden="true">§ 1. (1) Wording.</span><span class="sr-only">Paragraph one duplicated.</span></p><p>548)</p><p>-- -- --</p><p>###</p>',
                    )
                ],
            )
            md, checks, w = n.convert(r, root, Path(t) / "out", date="2026-11-01")
            self.assertTrue(all(c["characters_preserved"] for c in checks))
            self.assertFalse(w)
            text = (Path(t) / "out/20000001/par-0001.md").read_text()
            self.assertNotIn("duplicated", text)
            self.assertIn("548\\)", text)

    def test_merged_nested_tables_images_and_inline_units(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            r = source_run(
                root,
                entries=[
                    (
                        "§ 1",
                        '<table><tr><td rowspan="2">A</td><td><span class="Hoch">2</span></td></tr><tr><td><table><tr><td><img src="https://example.org/figure.png"></td></tr></table></td></tr></table><p>CO<span class="Tief">2</span></p>',
                    )
                ],
            )
            md, c, w = n.convert(r, root, Path(t) / "out", date="2026-11-01")
            self.assertTrue(
                all(v for x in c for k, v in x.items() if k.endswith("_preserved"))
            )
            text = (Path(t) / "out/20000001/par-0001.md").read_text()
            self.assertIn('rowspan="2"', text)
            self.assertIn("<sub>2</sub>", text)
            self.assertIn("Source image", text)

    def test_nested_and_double_escaped_links_are_accounted_for(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            r = source_run(
                root,
                entries=[
                    (
                        "§ 1",
                        '<p><a href="https://example.org/outer"><span><a href="https://example.org/?x=1&amp;amp;y=2">citation</a></span></a></p>',
                    )
                ],
            )
            md, c, w = n.convert(r, root, Path(t) / "out", date="2026-11-01")
            self.assertTrue(
                all(x["characters_preserved"] and x["links_preserved"] for x in c)
            )
            self.assertEqual(len(md["provisions"][1]["links"]), 2)

    def test_treaty_suffix_is_retained_beside_ris_designation(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            r = source_run(
                root,
                entries=[
                    ("Art. 5", "<p>Artikel 5. A.</p>"),
                    ("Art. 5", "<p>Artikel 5bis. B.</p>"),
                ],
            )
            md, c, w = n.convert(r, root, date="2026-11-01")
            self.assertEqual(
                [p["file"] for p in md["provisions"][1:]],
                ["art-005.md", "art-005bis.md"],
            )
            self.assertTrue(
                all(p["designation"] == "Art. 5" for p in md["provisions"][1:])
            )
            self.assertFalse(w)

    def test_unresolved_identity_blocks_review_and_retains_all_entries(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            source_run(root, entries=[("§ 1", "<p>A.</p>"), ("§ 1", "<p>B.</p>")])
            out = Path(t) / "out"
            m = clean.build(root, out)
            self.assertEqual(m["provision_count"], 3)
            self.assertTrue(m["blocking_issues"])
            self.assertEqual(len(list((out / "20000001").glob("par-*.md"))), 2)
            with self.assertRaisesRegex(ValueError, "unresolved"):
                clean.approve(out, "reviewer", "reviewed")

    def test_duplicate_occurrence_mapping_invalidated_when_count_changes(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            r = source_run(
                root,
                entries=[("§ 1", "<p>Identical.</p>"), ("§ 1", "<p>Identical.</p>")],
            )
            md, _, _ = n.convert(r, root, date="2026-11-01")
            fingerprint = md["provisions"][1]["source_fingerprint"]
            mapping = {
                f"20000001:{fingerprint}:{i}": {
                    "file": f"par-0001--record-{i}.md",
                    "expected_occurrences": 2,
                }
                for i in (1, 2)
            }
            md, _, _ = n.convert(r, root, date="2026-11-01", resolutions=mapping)
            self.assertFalse(
                any(p["identity_review_required"] for p in md["provisions"])
            )
            other = Path(t) / "other"
            r2 = source_run(other, entries=[("§ 1", "<p>Identical.</p>")])
            md, _, _ = n.convert(r2, other, date="2026-11-01", resolutions=mapping)
            self.assertTrue(md["provisions"][1]["identity_review_required"])

    def test_changed_ambiguous_record_requires_review_and_unchanged_key_survives(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            r = source_run(
                root / "old-run", entries=[("§ 1", "<p>A.</p>"), ("§ 1", "<p>B.</p>")]
            )
            md, _, _ = n.convert(r, root / "old-run", date="2026-11-01")
            mapping = {
                f"20000001:{p['source_fingerprint']}:1": {
                    "file": f"par-0001--record-{i}.md",
                    "expected_occurrences": 1,
                }
                for i, p in enumerate(md["provisions"][1:])
            }
            resolutions = root / "resolutions.json"
            clean.save(resolutions, {"records": mapping})
            clean.build(root / "old-run", root / "old", resolutions=resolutions)
            source_run(root / "same-run", "2026-11-08", [("§ 1", "<p>A.</p>")])
            same = clean.build(
                root / "same-run",
                root / "same",
                resolutions=resolutions,
                previous=root / "old",
            )
            self.assertFalse(same["blocking_issues"])
            self.assertTrue((root / "same/20000001/par-0001--record-0.md").exists())
            source_run(
                root / "changed-run",
                "2026-11-08",
                [("§ 1", "<p>Changed ambiguous wording.</p>")],
            )
            changed = clean.build(
                root / "changed-run",
                root / "changed",
                resolutions=resolutions,
                previous=root / "old",
            )
            self.assertTrue(
                any(
                    i["check"] == "changed_ambiguous_identity_requires_review"
                    for i in changed["blocking_issues"]
                )
            )

    def test_unknown_structure_requires_attention(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            source_run(
                root,
                entries=[
                    ("§ 1", "<novel-legal-table>Visible text</novel-legal-table>")
                ],
            )
            m = clean.build(root, Path(t) / "out")
            self.assertTrue(
                any("unreviewed_source_tag" in i["check"] for i in m["blocking_issues"])
            )

    def test_identical_input_is_byte_deterministic(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            source_run(root)
            one, two = Path(t) / "one", Path(t) / "two"
            clean.build(root, one)
            clean.build(root, two)
            a = {
                p.relative_to(one): p.read_bytes()
                for p in one.rglob("*")
                if p.is_file()
            }
            b = {
                p.relative_to(two): p.read_bytes()
                for p in two.rglob("*")
                if p.is_file()
            }
            self.assertEqual(a, b)

    def test_observation_dates_do_not_create_substantive_changes(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            source_run(root / "a")
            clean.build(root / "a", root / "old")
            source_run(root / "b", "2026-11-08")
            m = clean.build(root / "b", root / "new", previous=root / "old")
            self.assertFalse(m["has_changes"])

    def test_changed_provision_has_specific_diff(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            source_run(root / "a")
            clean.build(root / "a", root / "old")
            source_run(root / "b", "2026-11-08", [("§ 1", "<p>Changed wording.</p>")])
            m = clean.build(root / "b", root / "new", previous=root / "old")
            self.assertEqual(
                m["instruments"][0]["changes"],
                [{"file": "par-0001.md", "change": "text_changed"}],
            )

    def test_review_receipt_is_bound_to_exact_manifest(self):
        import export_current

        with tempfile.TemporaryDirectory() as t:
            root = Path(t)
            source_run(root / "run")
            clean.build(root / "run", root / "out")
            clean.approve(root / "out", "reviewer", "Inspected rendered wording.")
            m = clean.read(root / "out/manifest.json")
            m["snapshot_as_of"] = "2026-11-02"
            clean.save(root / "out/manifest.json", m)
            with self.assertRaisesRegex(ValueError, "review receipt"):
                export_current.export(root / "out", root / "checkout")

    def test_corrupted_source_is_rejected(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t) / "run"
            r = source_run(root)
            (root / r["file"]).write_text("changed after download")
            with self.assertRaisesRegex(ValueError, "hash mismatch"):
                clean.build(root, Path(t) / "out")

    def test_notice_period_is_checked_before_each_network_request(self):
        notice = {"period_start": "2026-11-01", "period_end": "2026-11-08"}
        sync.check_notice_period(notice, dt.datetime(2026, 11, 8, 23, 59))
        with self.assertRaisesRegex(ValueError, "outside"):
            sync.check_notice_period(notice, dt.datetime(2026, 11, 9))
        with (
            tempfile.TemporaryDirectory() as t,
            patch("catalog.allowed", return_value=True),
            patch("catalog.time.sleep"),
            patch("catalog.urllib.request.urlopen") as request,
        ):
            client = catalog.Client(
                Path(t),
                user_agent="test",
                before_request=lambda: sync.check_notice_period(
                    notice, dt.datetime(2026, 11, 9)
                ),
            )
            with self.assertRaisesRegex(ValueError, "outside"):
                client.get("https://example.org/not-fetched")
            request.assert_not_called()


if __name__ == "__main__":
    unittest.main()
