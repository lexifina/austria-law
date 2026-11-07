"""Build and verify clean current-law data offline. Never fetch or publish."""

from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

import catalog
import normalize_current as normal

FORMAT_VERSION = 1
DEFAULT_RESOLUTIONS = Path(__file__).with_name("current-identities.json")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path, value):
    catalog.atomic_write(
        path, (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()
    )


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def safe_file(name):
    path = Path(name)
    if (
        path.is_absolute()
        or ".." in path.parts
        or not path.parts
        or path.suffix != ".md"
    ):
        raise ValueError("unsafe provision path")
    return path


def content_identity(metadata):
    """Separate substantive law/metadata changes from observation dates and hashes."""
    result = {
        k: v for k, v in metadata.items() if k not in {"snapshot_as_of", "source"}
    }
    result["provisions"] = [
        {
            k: v
            for k, v in p.items()
            if k not in {"source_locator", "source_fingerprint"}
        }
        for p in metadata["provisions"]
    ]
    return hashlib.sha256(
        json.dumps(result, ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()


def verify(directory, require_ready=True):
    manifest = read(directory / "manifest.json")
    index = read(directory / "catalog.json")
    if manifest.get("schema_version") != FORMAT_VERSION or not manifest.get("complete"):
        raise ValueError("clean collection is incomplete or has an unsupported schema")
    if require_ready and manifest.get("blocking_issues"):
        raise ValueError("clean collection has unresolved validation issues")
    if digest(directory / "catalog.json") != manifest["catalog_sha256"]:
        raise ValueError("clean catalog hash mismatch")
    ids = [r["gesetzesnummer"] for r in manifest["instruments"]]
    if (
        len(ids) != len(set(ids))
        or len(ids) != manifest["instrument_count"]
        or ids != [r["gesetzesnummer"] for r in index["instruments"]]
    ):
        raise ValueError("clean collection/catalog count mismatch")
    expected = {"catalog.json", "manifest.json", "quality-report.json"}
    entries = 0
    if digest(directory / "quality-report.json") != manifest["quality_report_sha256"]:
        raise ValueError("quality report hash mismatch")
    report = read(directory / "quality-report.json")
    if report["blocking_issues"] != manifest["blocking_issues"]:
        raise ValueError("inconsistent validation report")
    for row in manifest["instruments"]:
        nr = row["gesetzesnummer"]
        if not re.fullmatch(r"\d{8}", nr):
            raise ValueError("invalid instrument key")
        name = f"{nr}/act.json"
        expected.add(name)
        if digest(directory / name) != row["metadata_sha256"]:
            raise ValueError(f"{nr}: metadata hash mismatch")
        md = read(directory / name)
        if (
            md["gesetzesnummer"] != nr
            or md["sample_only"]
            or md["included_provisions"] != md["source_provision_count"]
        ):
            raise ValueError(f"{nr}: instrument identity or source accounting mismatch")
        if len(md["provisions"]) != md["included_provisions"]:
            raise ValueError("entry count mismatch")
        for provision in md["provisions"]:
            name = f"{nr}/{safe_file(provision['file']).as_posix()}"
            if name in expected:
                raise ValueError("duplicate provision path")
            expected.add(name)
            entries += 1
            if digest(directory / name) != provision["sha256"]:
                raise ValueError(f"{name}: provision hash mismatch")
            if require_ready and provision["identity_review_required"]:
                raise ValueError("unresolved provision identity")
    if entries != manifest["provision_count"]:
        raise ValueError("collection entry count mismatch")
    actual = {
        p.relative_to(directory).as_posix() for p in directory.rglob("*") if p.is_file()
    }
    if actual != expected:
        raise ValueError("unexpected or missing generated files")
    return manifest


def build(run, output, resolutions=DEFAULT_RESOLUTIONS, previous=None):
    if output.exists():
        raise ValueError("output already exists; choose a new candidate directory")
    source = read(run / "manifest.json")
    index = read(run / "catalog.json")
    if not source["complete"] or not index["complete"]:
        raise ValueError("incomplete source snapshot")
    records = source["records"]
    ids = [r["nr"] for r in records]
    if (
        len(ids) != len(set(ids))
        or len(ids) != source["count"]
        or set(ids) != {r["nr"] for r in index["records"]}
    ):
        raise ValueError("source catalog/snapshot count mismatch")
    mapping = (
        read(resolutions)["records"] if resolutions and resolutions.exists() else {}
    )
    issues = []
    rows = []
    catalog_rows = []
    statistics = Counter()
    prior = {}
    if previous:
        prior = {r["gesetzesnummer"]: r for r in verify(previous)["instruments"]}
    output.mkdir(parents=True)
    for i, row in enumerate(sorted(records, key=lambda r: r["nr"]), 1):
        nr = row["nr"]
        if not re.fullmatch(r"\d{8}", nr) or row["file"] != f"current/{nr}.html":
            raise ValueError("unsafe source path")
        metadata, checks, warnings = normal.convert(
            row, run, output, date=source["as_of"], resolutions=mapping
        )
        for c in checks:
            statistics["provisions"] += 1
            for k, v in c.items():
                if k.endswith("_preserved"):
                    statistics[k] += bool(v)
                    if not v:
                        issues.append(
                            {
                                "nr": nr,
                                "designation": c["designation"],
                                "check": k,
                                "detail": c.get("issue"),
                            }
                        )
        for p in metadata["provisions"]:
            safe_file(p["file"])
            if p["identity_review_required"]:
                issues.append(
                    {
                        "nr": nr,
                        "designation": p["designation"],
                        "check": "unresolved_identity",
                        "source_fingerprint": p["source_fingerprint"],
                    }
                )
        for w in warnings:
            issues.append({"nr": nr, "check": w})
        identity = content_identity(metadata)
        before = prior.get(nr)
        changes = []
        if previous:
            if before is None:
                changes = [{"change": "instrument_added"}]
            elif before["content_identity"] != identity:
                old = read(previous / nr / "act.json")
                oldp = {p["file"]: p for p in old["provisions"]}
                newp = {p["file"]: p for p in metadata["provisions"]}
                ambiguous_labels = {
                    p["designation"]
                    for p in oldp.values()
                    if p["identity_basis"] == "reviewed_local_key"
                }
                for p in newp.values():
                    if (
                        p["designation"] in ambiguous_labels
                        and p["identity_basis"] != "reviewed_local_key"
                        and p["file"] not in oldp
                    ):
                        issues.append(
                            {
                                "nr": nr,
                                "designation": p["designation"],
                                "check": "changed_ambiguous_identity_requires_review",
                                "source_fingerprint": p["source_fingerprint"],
                            }
                        )
                for path in sorted(oldp.keys() | newp.keys()):
                    if path not in oldp:
                        changes.append({"file": path, "change": "added"})
                    elif path not in newp:
                        changes.append({"file": path, "change": "removed"})
                    elif oldp[path]["sha256"] != newp[path]["sha256"]:
                        changes.append({"file": path, "change": "text_changed"})
                    elif {
                        k: v
                        for k, v in oldp[path].items()
                        if k not in {"source_locator", "source_fingerprint"}
                    } != {
                        k: v
                        for k, v in newp[path].items()
                        if k not in {"source_locator", "source_fingerprint"}
                    }:
                        changes.append({"file": path, "change": "metadata_changed"})
                if not changes:
                    changes = [{"change": "instrument_metadata_changed"}]
        rows.append(
            {
                "gesetzesnummer": nr,
                "metadata_sha256": digest(output / nr / "act.json"),
                "content_identity": identity,
                "changes": changes,
            }
        )
        catalog_rows.append(
            {
                "gesetzesnummer": nr,
                "title": metadata["short_title"],
                "abbreviation": metadata["abbreviation"],
                "type": metadata["instrument_type"],
                "file": nr + "/act.json",
            }
        )
        statistics["instruments"] += 1
        if i % 1000 == 0:
            print(
                f"Normalized {i}/{len(records)} instruments; {len(issues)} review issues",
                flush=True,
            )
    removed = sorted(prior.keys() - set(ids))
    report = {
        "format_version": FORMAT_VERSION,
        "statistics": dict(statistics),
        "blocking_issues": issues,
        "removed_instruments": removed,
        "changed_instruments": [r["gesetzesnummer"] for r in rows if r["changes"]],
        "manual_review": None,
        "limitations": [
            "Source images and binary annexes are linked, not mirrored or OCR-transcribed.",
            "Whole-law responses omit provision NOR identifiers and per-provision validity dates; unknown values are explicit.",
        ],
    }
    save(output / "quality-report.json", report)
    save(
        output / "catalog.json",
        {"schema_version": FORMAT_VERSION, "instruments": catalog_rows},
    )
    manifest = {
        "schema_version": FORMAT_VERSION,
        "complete": True,
        "snapshot_as_of": source["as_of"],
        "instrument_count": len(rows),
        "provision_count": statistics["provisions"],
        "blocking_issues": issues,
        "quality_report_sha256": digest(output / "quality-report.json"),
        "catalog_sha256": digest(output / "catalog.json"),
        "source_manifest_sha256": digest(run / "manifest.json"),
        "previous_as_of": read(previous / "manifest.json")["snapshot_as_of"]
        if previous
        else None,
        "removed_instruments": removed,
        "has_changes": not previous or bool(removed or any(r["changes"] for r in rows)),
        "instruments": rows,
    }
    save(output / "manifest.json", manifest)
    verify(output, require_ready=False)
    return manifest


def approve(directory, reviewer, notes):
    """Record a concrete human/agent review bound to this exact candidate manifest."""
    m = verify(directory)
    receipt = {
        "manifest_sha256": digest(directory / "manifest.json"),
        "reviewer": reviewer,
        "notes": notes,
        "instrument_count": m["instrument_count"],
        "provision_count": m["provision_count"],
    }
    # Kept beside the generated collection, not among legal data.
    save(directory.with_name(directory.name + "-review.json"), receipt)
    return receipt


def reproduce(run, directory, resolutions=DEFAULT_RESOLUTIONS):
    """Recompute every provision hash/metadata from captured sources without writing."""
    manifest = verify(directory)
    if manifest["source_manifest_sha256"] != digest(run / "manifest.json"):
        raise ValueError("candidate belongs to another source manifest")
    mapping = (
        read(resolutions)["records"] if resolutions and resolutions.exists() else {}
    )
    source = read(run / "manifest.json")
    count = 0
    for i, row in enumerate(source["records"], 1):
        metadata, checks, warnings = normal.convert(
            row, run, date=source["as_of"], resolutions=mapping
        )
        if warnings or any(
            p["identity_review_required"] for p in metadata["provisions"]
        ):
            raise ValueError(f"{row['nr']}: unresolved reproduction issue")
        if any(not v for c in checks for k, v in c.items() if k.endswith("_preserved")):
            raise ValueError(f"{row['nr']}: preservation check failed")
        encoded = (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode()
        if encoded != (directory / row["nr"] / "act.json").read_bytes():
            raise ValueError(f"{row['nr']}: reproduction differs")
        count += len(checks)
        if i % 2000 == 0:
            print(
                f"Reproduced {i}/{manifest['instrument_count']} instruments", flush=True
            )
    if count != manifest["provision_count"]:
        raise ValueError("reproduction entry count mismatch")
    return {
        "instruments": manifest["instrument_count"],
        "provisions": count,
        "deterministic": True,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="operation", required=True)
    b = sub.add_parser("build")
    b.add_argument("--run", type=Path, required=True)
    b.add_argument("--output", type=Path, required=True)
    b.add_argument("--previous", type=Path)
    b.add_argument("--resolutions", type=Path, default=DEFAULT_RESOLUTIONS)
    v = sub.add_parser("verify")
    v.add_argument("directory", type=Path)
    d = sub.add_parser("reproduce")
    d.add_argument("directory", type=Path)
    d.add_argument("--run", type=Path, required=True)
    d.add_argument("--resolutions", type=Path, default=DEFAULT_RESOLUTIONS)
    r = sub.add_parser("review")
    r.add_argument("directory", type=Path)
    r.add_argument("--reviewer", required=True)
    r.add_argument("--notes", required=True)
    args = ap.parse_args()
    if args.operation == "build":
        m = build(args.run, args.output, args.resolutions, args.previous)
        print(
            json.dumps(
                {
                    "instruments": m["instrument_count"],
                    "provisions": m["provision_count"],
                    "blocking_issues": len(m["blocking_issues"]),
                }
            )
        )
        sys.exit(2 if m["blocking_issues"] else 0)
    elif args.operation == "verify":
        print(json.dumps(verify(args.directory), ensure_ascii=False)[:200])
    elif args.operation == "reproduce":
        print(json.dumps(reproduce(args.run, args.directory, args.resolutions)))
    else:
        print(json.dumps(approve(args.directory, args.reviewer, args.notes)))


if __name__ == "__main__":
    main()
