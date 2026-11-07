# Current federal law: clean import and update checks

The current snapshot is separate from the existing `b-vg/` and `dsg/` amendment histories.
The importer does not reconstruct history or infer enactment dates. See [CURRENT_FORMAT.md](CURRENT_FORMAT.md)
for the finalized data contract.

## Setup

```sh
python3 -m venv .venv
.venv/bin/pip install -r tools/requirements-current.txt
```

## Capture, build, validate, review, export

These stages are separate. Neither downloading nor checking for updates pushes commits, opens a PR or merges.

For the completed initial download, reuse the cache without contacting RIS:

```sh
.venv/bin/python tools/run_current_job.py --root ../ris-sync --date 2026-11-01 \
  --notice-file ../ris-sync/notice-sent.json --offline
```

For a new capture, omit `--offline`, with a valid notice covering that period. The job creates a candidate under
`<root>/clean/<date>/`. `--candidate` selects another output location. Candidates are immutable: a retry verifies
an existing generation; use a new candidate directory when changing conversion code or identity resolutions.
`--previous` selects a verified clean baseline; otherwise the last successful clean candidate is used for a newer date.

`job-<date>.json` reports `ready_for_review`, `no_changes`, `needs_attention` or `failed`. Exit status 2 means
validation requires attention. `quality-report.json` lists every blocking issue and changed instrument.
The clean baseline advances only after all clean-data checks succeed. The separate raw `latest.json` means
capture completed, and does not imply that its data is reviewed or publishable.

Inspect changed Markdown, metadata and rendered examples, including tables, notes and source attachments.
Then record the actual review, bound to the exact candidate manifest:

```sh
.venv/bin/python tools/clean_current.py review ../ris-sync/clean/2026-11-01 \
  --reviewer 'Reviewer name' --notes 'Describe the inspected cases and remaining limitations.'
.venv/bin/python tools/export_current.py --candidate ../ris-sync/clean/2026-11-01 --checkout <data-checkout>
```

The export verifies all hashes and the review receipt before replacing generated data. It refuses unrelated
files in the destination and can migrate the previous HTML export after verifying its manifest. Publishing
is a separate Git/PR action after inspecting the staged diff. Keep the resulting PR in draft during review.
An unchanged scan requires no PR. Refresh an existing pending data PR rather than opening duplicates.

## Incremental checks and automation

Run `run_current_job.py` with a newer date and the same root. It refreshes the title catalog, queries RIS History
with deleted documents and a two-day overlap, and checks provisions entering into force or expiring in the
window. Only affected whole-law texts are fetched; other verified captures are reused. Unmapped deletion
records trigger full reconciliation. Pagination, application and effective-date filters are checked.

Normalization still checks the entire candidate offline. The clean diff compares provisions and metadata;
observation dates, retrieval hashes and source-block positions do not create substantive changes. The report
lists added/removed instruments and provisions, changed text, and changed metadata. Missing or unexpected
structures stop automatic export. An unknown ambiguous identity requires a reviewed source-to-key mapping.

This command can be invoked by a scheduler. It has no GitHub side effects and no interactive prompts. No weekly
schedule is installed by these tools. A live incremental RIS run has not yet been exercised; regression tests
simulate added/removed laws, amendments, effective dates, deletion fallback and interrupted acquisition.
RIS has no transactional snapshot token, so completeness remains bounded by its catalog and change feed.

## RIS access and notice

Record a notice actually sent in a local file outside Git: `sent_at` (ISO timestamp), `user_agent`, `source_ip`,
`period_start`, `period_end` (inclusive Vienna dates), and `weekly` (boolean). Do not put the IP or receipt in Git.
A recurring check needs a notice covering recurring use and its dates. The initial notice does not authorize
later access automatically. The downloader checks the period before starting and before every network request.

Only one sequential connection is used, with a two-second pause after a response. Access waits for 20:00–05:00
Vienna time, weekends or Austrian public holidays. A lock prevents simultaneous syncs within one job root;
use only one downloader per source IP. The response cache is verified and resumable. An incomplete capture
never replaces the prior complete capture. `--offline` sends no RIS requests. There is no email sender.

`status.json` describes capture progress. `--wait-for-notice` waits for a notice file without fetching.
On macOS, `caffeinate` inhibits idle sleep during authorized capture; lid closure and shutdown still interrupt it.

## Checks

```sh
.venv/bin/python -m unittest discover -s tools -p 'test_catalog.py' -v
.venv/bin/python -m unittest discover -s tools -p 'test_*current.py' -v
.venv/bin/python tools/clean_current.py verify ../ris-sync/clean/2026-11-01
.venv/bin/python tools/clean_current.py reproduce ../ris-sync/clean/2026-11-01 --run ../ris-sync/runs/2026-11-01
```

Source: [RIS, Bundeskanzleramt](https://www.ris.bka.gv.at), CC BY 4.0.
[Official API and access information](https://data.bka.gv.at/ris/api/v2.6/).
