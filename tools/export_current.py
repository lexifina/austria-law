"""Export an independently reviewed clean candidate into a checkout. No network or PR writes."""

import argparse
from pathlib import Path
import os
import shutil
import tempfile
import clean_current as clean


def export(candidate, checkout, review=None):
    manifest = clean.verify(candidate)
    review = review or candidate.with_name(candidate.name + "-review.json")
    receipt = clean.read(review)
    if (
        not receipt.get("reviewer")
        or not receipt.get("notes")
        or receipt.get("manifest_sha256") != clean.digest(candidate / "manifest.json")
    ):
        raise ValueError("review receipt does not match the exact validated candidate")
    data = checkout / "data"
    data.mkdir(parents=True, exist_ok=True)
    target = data / "current"
    if target.exists():
        if (target / "manifest.json").exists():
            clean.verify(target)
        else:
            # Recognise only the previous generated HTML export before replacing it.
            old = clean.read(data / "current-snapshot.json")
            files = {r["nr"] + ".html": r["sha256"] for r in old["records"]}
            if {p.name for p in target.iterdir()} != set(files):
                raise ValueError("unrecognised destination files")
            if any(clean.digest(target / name) != sha for name, sha in files.items()):
                raise ValueError("previous export hash mismatch")
    stage = Path(tempfile.mkdtemp(prefix=".current-", dir=data))
    backup = data / ".current-backup"
    if backup.exists():
        raise ValueError(
            "unfinished prior export; inspect .current-backup before retrying"
        )
    try:
        shutil.copytree(candidate, stage, dirs_exist_ok=True)
        clean.verify(stage)
        if target.exists():
            os.replace(target, backup)
        try:
            os.replace(stage, target)
        except BaseException:
            if backup.exists():
                os.replace(backup, target)
            raise
        if backup.exists():
            shutil.rmtree(backup)
        for name in ("current-catalog.json", "current-snapshot.json"):
            path = data / name
            if path.exists():
                path.unlink()
        clean.save(data / "current-review.json", receipt)
    finally:
        if stage.exists():
            shutil.rmtree(stage)
    return manifest["instrument_count"]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidate", type=Path, required=True)
    ap.add_argument("--checkout", type=Path, required=True)
    ap.add_argument("--review", type=Path)
    args = ap.parse_args()
    print(f"Exported {export(args.candidate, args.checkout, args.review)} instruments")
