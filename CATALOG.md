# Current federal-law catalog

`tools/catalog.py` discovers the **§ 0 title records in Bundesrecht konsolidiert (BrKons)** that RIS reports as in
force on an explicit date. This includes regulations, treaties and other federal instruments, not just statutes.
It is a metadata catalog with dated links to the full consolidated text. It does not import that text or amendment
histories, does not cover Land law, and does not claim to enumerate every source of Austrian law.

## Access rules and notice

Before a bulk run, send the notice required by the [RIS OGD FAQ](https://data.bka.gv.at/ris/api/v2.6/) to
`ris.it@bka.gv.at`, subject `Ankündigung eines geplanten Massendownloads (OGD): austria-law`.
Include purpose/applications, the exact user agent, the downloader's public IP address/range, planned dates/hours,
and estimated end. This is advance notification to help RIS distinguish the traffic from an attack; the FAQ does
not specify an approval response to wait for. The original repository's notice for two acts must not be assumed
to cover another downloader or a full-catalog run.

The importer requires an explicit `--notice-sent` acknowledgement and a user agent before network access. It
uses one connection, pauses at least two seconds after each response, honours Retry-After on transient HTTP
errors, and waits outside 20:00–05:00 Europe/Vienna, weekends and Austrian public holidays. Run only one RIS
fetcher at a time, including `build.py` and any jobs on the same IP. The cache lock prevents concurrent catalog
runs in the same dated cache; it does not coordinate other fetchers or different cache roots.

## Run

Python 3.12+ with the standard library and a Europe/Vienna timezone database is sufficient. No `lxml` or GitHub
credentials are needed by the catalog importer. Once the notice has actually been sent:

```sh
python tools/catalog.py --date 2026-11-01 --scope federal \
  --output data/catalog-2026-11-01.json \
  --notice-sent \
  --user-agent 'austria-law-catalog/1.0 (+https://github.com/axhoff/austria-law)'
```

Interrupted runs resume from `tools/.catalog-cache/<date>/`. A successful run writes the output only after
validating every page. Replay the exact same data without network access:

```sh
python tools/catalog.py --date 2026-11-01 --scope federal \
  --output data/catalog-2026-11-01.json --offline
python -m unittest discover -s tools -p test_catalog.py -v
```

The dated cache is an immutable acquisition: resuming or replaying does not refresh its responses. To acquire
updated source data even for the same as-of date, use a new `--cache` directory. A failed/incomplete run leaves
an existing catalog file untouched. Remove a stale `.running` directory only after confirming its process is
no longer running. Raw API responses and acquisition metadata are cached; the published catalog records each
query URL, page, hit count, retrieval time and response SHA-256.

## Completeness checks

The query uses `Fassung.FassungVom`, `Abschnitt.Von=0`, `Abschnitt.Bis=0`, and `Abschnitt.Typ=Paragraph`.
Top-level parameters such as `FassungVom` and `Paragraphnummer` can be silently ignored by this endpoint.
These names follow the [official API manual](https://www.data.gv.at/katalog/dataset/0fb9ae1a-92cb-4ab8-a589-470c16d4fe21/resource/42070d46-01fe-4b36-803f-4af925290f59/download/dokumentation_ogd-ris_api.pdf),
sections for BrKons and complex parameters.

The importer rejects API errors, incorrect page number/size, truncated pages, changing hit counts, repeated
document IDs, multiple title records for a law, wrong applications, records other than `§ 0`/`Norm`, and title
versions outside the requested inclusive validity window. It checks cached bytes against their recorded hash.
Only a fully enumerated result gets `complete: true`, scoped explicitly to this query. RIS has no transactional
snapshot token: these checks cannot detect every concurrent edit, or prove RIS itself is complete. If checks
fail because the source changed during acquisition, repeat with a fresh cache.

A small manual probe on 2026-11-01 returned **10,679 title hits** and 100 title records on the first page.
This is a source-reported count, not a completed catalog or a count of statutes alone. At that count a complete
catalog takes 107 API requests, at least 212 seconds of inter-request pauses plus response times. No bulk run
or full-text acquisition was performed while preparing this change. `tools/fixtures/federal-title.json` is one
unaltered document reference from that first page; pagination tests use synthetic envelopes. Its source is the
same query produced by `query_url('federal', '2026-11-01', 1)`, retrieved on 2026-11-01. It is covered by the RIS
CC BY 4.0 attribution below.

## Relationship to the historical corpus

Keep `corpus.json`, `data/fassungen.json`, the law folders and existing history unchanged until legal text and
versions have been fetched and verified. A metadata catalog is not evidence that a provision's full text was
imported or checked. Full historical ingestion is much larger than title discovery.

An optional `--acts-output <path>` writes a **discovery list** in the existing `acts_extra.json` format, excluding
B-VG and DSG and assigning stable `ris-<Gesetzesnummer>` folders to other instruments. Review the list before
using it as `tools/acts_extra.json`; it does not preserve custom extra-act slugs from another list. This selects
currently listed instruments for the history builder; it is not a catalog of every instrument ever repealed.
It must not be mistaken for a completed history import.

The supplied `tools/build.py` imports `reproduce.doc_files`, but `tools/reproduce.py` is absent from this checkout.
That dependency needs restoring before a full rebuild can succeed. The catalog tool is independent of it.
Do not point the builder at this checkout: its `--repo` output preparation deletes existing contents.

## Source and licence

Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Metadata is reorganised; legal text is not included in
the catalog. The existing repository licence applies to the new tooling. Consolidated RIS texts are for
information; the authentic promulgations remain the authoritative source.
