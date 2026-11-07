"""Capture, normalize and validate a current-law candidate. Never push or open a PR."""

import argparse
import datetime as dt
from pathlib import Path
import json
import subprocess
import sys
import clean_current as clean
import sync_current as sync


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--date", type=dt.date.fromisoformat, required=True)
    ap.add_argument("--notice-file", type=Path, required=True)
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--wait-for-notice", action="store_true")
    ap.add_argument("--previous", type=Path)
    ap.add_argument("--candidate", type=Path)
    ap.add_argument("--repo", type=Path, help="deprecated; no publishing occurs")
    args = ap.parse_args()
    root = args.root.resolve()
    date = str(args.date)
    root.mkdir(parents=True, exist_ok=True)
    if args.previous is None and (root / "clean-latest.json").exists():
        last = clean.read(root / "clean-latest.json")
        if last["as_of"] < date:
            args.previous = Path(last["candidate"])
    run = root / "runs" / date
    candidate = args.candidate or root / "clean" / date
    job = root / f"job-{date}.json"
    try:
        if not (run / "manifest.json").exists():
            invocation = [
                sys.executable,
                "-u",
                str(Path(__file__).with_name("sync_current.py")),
                "--root",
                str(root),
                "--date",
                date,
                "--notice-file",
                str(args.notice_file.resolve()),
            ]
            if args.offline:
                invocation.append("--offline")
            if args.wait_for_notice:
                invocation.append("--wait-for-notice")
            subprocess.run(invocation, check=True)
        source = clean.read(run / "manifest.json")
        if not source["complete"] or source["as_of"] != date:
            raise ValueError("wrong or incomplete capture generation")
        if candidate.exists():
            manifest = clean.verify(candidate, require_ready=False)
            if manifest["snapshot_as_of"] != date or manifest[
                "source_manifest_sha256"
            ] != clean.digest(run / "manifest.json"):
                raise ValueError(
                    "existing candidate belongs to a different source generation"
                )
        else:
            manifest = clean.build(run, candidate, previous=args.previous)
        if manifest["blocking_issues"]:
            phase = "needs_attention"
        elif args.previous and not manifest["has_changes"]:
            phase = "no_changes"
        else:
            phase = "ready_for_review"
        sync.save(
            job,
            {
                "phase": phase,
                "as_of": date,
                "candidate": str(candidate.resolve()),
                "count": manifest["instrument_count"],
                "provisions": manifest["provision_count"],
                "blocking_issues": len(manifest["blocking_issues"]),
            },
        )
        if not manifest["blocking_issues"]:
            sync.save(
                root / "clean-latest.json",
                {"candidate": str(candidate.resolve()), "as_of": date},
            )
        print(json.dumps(clean.read(job), indent=2))
        return 2 if manifest["blocking_issues"] else 0
    except BaseException as exc:
        sync.save(job, {"phase": "failed", "as_of": date, "error": str(exc)})
        raise


if __name__ == "__main__":
    sys.exit(main())
