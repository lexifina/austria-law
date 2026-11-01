"""Export a verified completed snapshot into a checkout for a separate data PR."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil


def export(root, checkout):
    latest = json.loads((root / 'latest.json').read_text())
    run = root / Path(latest['manifest']).parent
    manifest = json.loads((run / 'manifest.json').read_text())
    catalog = json.loads((run / 'catalog.json').read_text())
    if not manifest.get('complete') or not catalog.get('complete'):
        raise ValueError('only complete snapshots can be exported')
    records = manifest['records']
    ids = {r['nr'] for r in records}
    if (len(records) != manifest['count'] or len(ids) != len(records)
            or ids != {r['nr'] for r in catalog['records']}):
        raise ValueError('snapshot/catalog counts or instruments differ')
    # Verify everything before modifying the destination checkout.
    for row in records:
        if not re.fullmatch(r'\d{8}', row['nr']) or row['file'] != f'current/{row["nr"]}.html':
            raise ValueError('unexpected snapshot path')
        raw = (run / row['file']).read_bytes()
        if hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise ValueError(f'{row["nr"]}: snapshot hash mismatch')
    target = checkout / 'data' / 'current'
    target.mkdir(parents=True, exist_ok=True)
    for row in records:
        shutil.copyfile(run / row['file'], target / (row['nr'] + '.html'))
    for path in target.iterdir():
        if re.fullmatch(r'\d{8}\.html', path.name) and path.stem not in ids:
            path.unlink()
    (checkout / 'data/current-snapshot.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    (checkout / 'data/current-catalog.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + '\n')
    return manifest['count']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--checkout', type=Path, required=True)
    args = parser.parse_args()
    print(f'Exported {export(args.root, args.checkout)} instruments')
