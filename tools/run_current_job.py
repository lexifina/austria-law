"""Run a current-law sync, verify its export, and open a data-only pull request."""
import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys

import export_current
import sync_current


def command(*args, cwd=None):
    return subprocess.check_output(list(args), cwd=cwd, text=True, stderr=subprocess.STDOUT).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--date', required=True, type=dt.date.fromisoformat)
    parser.add_argument('--notice-file', type=Path, required=True)
    parser.add_argument('--wait-for-notice', action='store_true')
    args = parser.parse_args()
    root, repo = args.root.resolve(), args.repo.resolve()
    root.mkdir(parents=True, exist_ok=True)
    job = root / ('job-' + args.date.isoformat() + '.json')
    if job.exists() and sync_current.read(job).get('phase') in ('published', 'no_changes'):
        print(sync_current.read(job).get('pr_url', 'No changes to publish.'))
        return
    try:
        invocation = [sys.executable, '-u', str(Path(__file__).with_name('sync_current.py')),
                      '--root', str(root), '--date', str(args.date), '--notice-file', str(args.notice_file.resolve())]
        if args.wait_for_notice:
            invocation.append('--wait-for-notice')
        subprocess.run(invocation, check=True)
        manifest = sync_current.read(root / 'runs' / str(args.date) / 'manifest.json')
        if not manifest['complete'] or manifest['as_of'] != str(args.date):
            raise ValueError('sync did not produce the requested complete generation')
        if manifest.get('previous_as_of') and not manifest['changes']:
            sync_current.save(job, {'phase': 'no_changes', 'as_of': str(args.date), 'count': manifest['count']})
            print('No changes to publish.', flush=True)
            return
        branch = 'codex/current-federal-' + str(args.date)
        checkout = root / ('pr-' + str(args.date))
        if not checkout.exists():
            command('git', 'fetch', 'origin', 'main', cwd=repo)
            command('git', 'worktree', 'add', '-b', branch, str(checkout), 'origin/main', cwd=repo)
        elif command('git', 'branch', '--show-current', cwd=checkout) != branch:
            raise ValueError('unexpected branch in data PR checkout')
        count = export_current.export(root, checkout)
        command('git', 'add', 'data/current', 'data/current-catalog.json', 'data/current-snapshot.json', cwd=checkout)
        staged = subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=checkout)
        if staged.returncode == 1:
            command('git', 'commit', '-m', f'Import current federal-law text snapshot for {args.date}', cwd=checkout)
        elif staged.returncode != 0:
            raise ValueError('could not inspect staged data changes')
        command('git', 'push', '-u', 'fork', branch, cwd=checkout)
        owner = command('gh', 'api', 'user', '--jq', '.login')
        prs = json.loads(command('gh', 'pr', 'list', '--repo', 'lexifina/austria-law',
                                 '--head', owner + ':' + branch, '--state', 'open', '--json', 'url'))
        if prs:
            url = prs[0]['url']
        else:
            body = root / ('pr-body-' + str(args.date) + '.txt')
            body.write_text(f'Adds the current consolidated federal-law catalog and HTML text snapshots for '
                            f'{count:,} instruments as of {args.date}, fetched from RIS with one connection, '
                            'a two-second pause and the permitted access hours after the advance notice.\n\n'
                            'The data includes per-instrument source URLs, response and content hashes, provision '
                            'designations and a source-query manifest. Every exported file was checked against '
                            'its manifest hash, and catalog/snapshot counts and instrument IDs match.\n\n'
                            'This is a current-text snapshot in data/current, separate from the existing '
                            'historical law folders. It does not reconstruct amendment history. External '
                            'binary annexes and images remain source links. Consolidated text is informational; '
                            'RIS attribution is retained under CC BY 4.0.\n', encoding='utf-8')
            url = command('gh', 'pr', 'create', '--repo', 'lexifina/austria-law', '--base', 'main',
                          '--head', owner + ':' + branch, '--title', f'Import current federal law as of {args.date}',
                          '--body-file', str(body))
        sync_current.save(job, {'phase': 'published', 'as_of': str(args.date), 'count': count, 'pr_url': url})
        print(url, flush=True)
    except BaseException as exc:
        sync_current.save(job, {'phase': 'failed', 'as_of': str(args.date), 'error': str(exc)})
        raise


if __name__ == '__main__':
    main()
