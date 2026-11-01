# Current text downloads and weekly updates

`tools/sync_current.py` downloads one RIS whole-law HTML response for each current federal instrument. It first
completes the catalog described in CATALOG.md, then acquires the texts sequentially. It retains every
`documentContent` block in RIS order, including repeated article designations originating in different amending
acts. It checks the returned instrument, date, application, title block and complete HTML response. Scripts,
event handlers, UI tokens and transient IDs are excluded; legal wording and block order are preserved, and
source links become absolute. External binary annexes/images remain links and are not mirrored.

This is a current-text snapshot, separate from the repository's existing amendment histories. It does not need
the missing `reproduce.py` history-builder dependency. No historical enactment dates or amendment authors are
invented for the snapshot.

## Initial run and advance notice

Send the RIS notice with the real downloader IP, user agent, period, and recurring weekly access if desired.
Record a notice **actually sent**, outside the repository, as JSON with `sent_at` (ISO timestamp), `user_agent`,
`source_ip`, and `weekly` (boolean). This file is an operational record, not an email sender or an approval
response. Never create a sent-notice record merely to bypass the gate. Do not commit the notice or source IP.

```sh
python tools/sync_current.py --root ../ris-sync --date 2026-11-01 \
  --notice-file ../ris-sync/notice-sent.json --wait-for-notice
```

The optional wait flag arms the run but performs no RIS requests until the sent-notice record exists.
`status.json` distinguishes `waiting_for_notice`, `catalog`, `texts`, `failed`, and `complete`. The raw-response
cache makes interrupted downloads resumable. A lock permits one sync at a time. On macOS, `caffeinate` inhibits
idle system sleep during an authorised network run, not while awaiting the notice; lid closure, shutdown and
manual sleep can still interrupt it. Resume the same command afterward. Use only one RIS process per source IP.

A completed generation lives in `runs/<date>/`, with a catalog, `current/<Gesetzesnummer>.html` files and a
manifest containing hashes, sources and provision designations. Only after all acquisitions succeed does
`latest.json` point to the new generation. Failures leave the previous published generation intact. Raw-response
caches are immutable acquisitions for that date; use a fresh root/cache to deliberately reacquire the same date.

`--offline` permits a full replay from cached source responses without sending requests.

## Weekly refresh

Run the same command with the next snapshot date and the same root. The updater:

1. Refreshes the small current title catalog to identify new, removed or retitled instruments.
2. Queries `History?Anwendung=Bundesnormen&IncludeDeletedDocuments=True` from two days before the last completed
   snapshot through the new date, paging through all results.
3. Also queries versions whose Inkrafttretensdatum or Ausserkrafttretensdatum falls in that window. This catches
   provisions taking effect or expiring even if they were published before the previous scan.
4. Downloads whole-law texts only for affected instruments and reuses verified local files for the others.
5. Records added, changed and removed instruments, comparing extracted legal-content blocks to suppress changes
   caused only by the page wrapper. It advances the checkpoint only after the entire new generation succeeds.

Unknown deletion records without a law number conservatively trigger reconciliation of all current texts.
Unrecognised response/pagination schemas fail instead of silently advancing the checkpoint. The history feed
may include historical corrections that do not change today's text; those can cause harmless extra fetches.
Source coverage still depends on what RIS exposes and there is no transactional source snapshot token.

The baseline includes 107 catalog requests at the observed 10,679-title count. Each weekly scan similarly needs
a few minutes for catalog metadata, plus change-feed pages and the affected full texts. The actual duration
depends on the number of changed instruments. A complete re-download should ordinarily be unnecessary.

## Data pull requests

`tools/run_current_job.py` runs a sync, verifies and exports the completed generation into an isolated checkout,
pushes a dated branch to the configured `fork` remote, and opens a data-only PR against `lexifina/austria-law`.
It requires authenticated `gh`, Git, a read-only `origin` pointing at the upstream repo, and a writable `fork`
remote. It never merges a PR or rewrites existing branches. The notice gate applies before the download starts.

```sh
python tools/run_current_job.py --root ../ris-sync --repo . --date 2026-11-01 \
  --notice-file ../ris-sync/notice-sent.json --wait-for-notice
```

For an export without publication, use `tools/export_current.py --root ../ris-sync --checkout <checkout>`.
It verifies every content hash and the catalog/manifest IDs before copying any files. Exported files are
`data/current/*.html`, `data/current-catalog.json` and `data/current-snapshot.json`.

## Validation and provenance

```sh
python -m unittest discover -s tools -p test_catalog.py -v
python -m unittest discover -s tools -p 'test_*current.py' -v
```

A manual ABGB full-law probe on 2026-11-01 returned 1,380 provision blocks, including repeated article
labels. The extractor retained all blocks in order and removed active page code. Offline tests cover partial
failure, prior-generation preservation, incremental downloads, effective-date changes, deletions, wrong-page
identity and truncated HTML. A live weekly bulk refresh has not yet been run.

Source: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, CC BY 4.0.
Access rules and the recommendation to use History are in https://data.bka.gv.at/ris/api/v2.6/.
