# How this history was made, and how to make it again

This file records how the repository was built: the sources and the rules for reading them, the commands, the
software, the decisions made by hand, and what an AI model did and did not do. The build writes it.

## Short version

```sh
git clone https://github.com/lexifina/austria-law && cd austria-law
pip install lxml
python -X utf8 tools/build.py --repo ../rebuilt --today 2026-10-28
git -C ../rebuilt rev-parse main        # the same hash as this repository's main
python -X utf8 tools/check_repo.py --repo ../rebuilt
python -X utf8 tools/test_repo.py --repo ../rebuilt
```

`tools/build.py` needs Python 3.12 or later with `lxml`, and git. It reads the RIS OGD API (or its own cache,
`tools/.cache/`) and writes this repository into `--repo`. With the same RIS data and the same `--today` it gives the
same commits with the same hashes. `data/fassungen.json` lists every RIS document used, with the sha256 of its XML
(sha256 of that file: `e45e436528f9f8683cdb01b165179e8fbdcc95adec06c611e6d594d863a130c3`). RIS updates its documents; then the hashes change too.

## Coverage

This repository holds 2 federal acts: B-VG (10000138), DSG (10001597). They are complete as RIS holds them: every document RIS
returns for each Gesetzesnummer was read. It is **not** the whole of Austrian federal law, and it holds no
Land law. Before a provision's first version in RIS its file is absent; RIS's history of the older acts is not
complete back to their enactment.

| Act | Gesetzesnummer | RIS documents | Provisions | Versions in force | Data notes |
| --- | --- | ---: | ---: | ---: | ---: |
| B-VG | 10000138 | 1340 | 241 | 1262 | 2 |
| DSG | 10001597 | 314 | 90 | 282 | 0 |

110 documents were never in force (RIS dates them to end the day before they begin: a version replaced before it
took effect) and are not in the history. 2 data notes (overlapping windows, two versions from one day) are listed
per act in `data/fassungen.json`; for an overlap the later version is used from its first day.

## Sources, and the rules for reading them

All legal text and all information about versions and amending laws come from the **RIS** (Rechtsinformationssystem
des Bundes), Bundesrecht konsolidiert, run by the Bundeskanzleramt, through its Open Government Data interface:

| What | Where |
| --- | --- |
| Every document (one version of one §, Art. or Anl.) of an act, 100 to a page, with Inkrafttretensdatum, Ausserkrafttretensdatum, ArtikelParagraphAnlage and Kundmachungsorgan | `https://data.bka.gv.at/ris/api/v2.6/Bundesrecht?Applikation=BrKons&Gesetzesnummer=<n>&DokumenteProSeite=OneHundred&Seitennummer=<p>` |
| The text of each version | `https://ogd.ris.bka.gv.at/Dokumente/Bundesnormen/<NOR>/<NOR>.xml`, listed with sha256 in `data/fassungen.json` |

The build read 18 search pages and 1544 XML documents. The data was retrieved on 2026-10-28
with the user agent `lexifina-watch/1.0 (+https://lexifina.com/watch; corpus@lexifina.com)`, one request at a time.

**The RIS terms were read before any bulk fetch.** robots.txt on data.bka.gv.at and ogd.ris.bka.gv.at has no Disallow
and no Crawl-delay, but the RIS OGD FAQ (data.bka.gv.at/ris/api/v2.6/, and OGD-FAQ.pdf of 28 November 2025) sets
binding technical rules: at most 0.5 requests per second (a pause of two seconds after each answer), no parallel connections, and requests only between 20:00 and 05:00 Vienna time or at weekends and on Austrian public holidays. Any use beyond single or manual-scale fetches must be announced beforehand to
ris.it@bka.gv.at ("Ankündigung eines geplanten Massendownloads (OGD)"), with the purpose, user agent, IP address and
time. `tools/build.py` enforces the three rules in code: one connection, a two-second pause after each answer, and a
wait outside the permitted hours (Austrian public holidays are computed). The bulk fetch was run only after Lexifina
had sent that notice. Licence: CC BY 4.0 (see LICENSE and README).

## The build, step by step

1. `python -X utf8 scripts/austria-law/build.py --today 2026-10-28 --fetch-only` in Lexifina's own repository filled the
   cache (resumable: it fetches only what is missing).
2. `python -X utf8 scripts/austria-law/build.py --today 2026-10-28 --offline` wrote this repository with one streamed
   `git fast-import`. `tools/build.py` here is that file (git blob `d8c1cadd2ace6528dd71f8ef01a46034ea267be4`), with `tools/reproduce.py`, which writes
   this file, `tools/check_repo.py`, `tools/test_repo.py` and the reader `tools/stand_am.py`.
3. `python -X utf8 scripts/austria-law/check_repo.py` read every provision version back from git with the
   `In-force:` trailer, on its first day and the version before on the day before, and compared them byte for byte
   with the text parsed afresh from the cached XML, and word for word with all words of the XML's text part, read
   without the build's parser. Result: 1544 provision versions checked on their first day and 1544 on the day before, 0 mismatches; 1544 versions word for word (741926 words), 0 mismatches.
4. `python -X utf8 scripts/austria-law/test_repo.py --record` ran the functional test
   (6 of 6 passed):
   - pass: blame names a law: b-vg/art-151.md lines by 51 author(s); dsg/art-002/par-0016.md lines by 3 author(s)
   - pass: text before and after an amendment: b-vg/art-151.md 2026-06-11 != 2026-06-12; dsg/art-002/par-0016.md 2024-06-28 != 2024-06-29
   - pass: log --follow in date order: b-vg/art-151.md 58 law commits; dsg/art-002/par-0016.md 6 law commits
   - pass: tags resolve, In-force on every commit: 246 tags resolve; 300 commits carry In-force
   - pass: only the documentation commit is by Lexifina: only the documentation commit d09b3b9845 is by Lexifina
   - pass: README commands run: 8 README commands ran and printed output
5. `python -X utf8 scripts/austria-law/build.py --offline --today 2026-10-28 --verify-rebuild` built the repository again
   from the cache into a temporary folder and compared the hashes. A second build from the same cache into an empty folder gave the same history: every one of the 247 refs (branches and tags) had the same hash, and the last law commit on main was `5f357f9bd1c0d09508b2ca81c03f29cdfed9c393` in both.
6. The build ran once more to write these results into this file, then was rebuilt and compared again before
   `git push -f origin main future --tags` to the private repository `lexifina/austria-law`.

It ran with Python 3.12.10, lxml 6.1.3 and git version 2.46.0.windows.1 on Windows 11. No network service other than the RIS is involved.

## How the text and the commits are derived

Everything below is done by `tools/build.py`, deterministically.

- **Provisions.** RIS keeps each version of each §, Art. or Anl. as a document with its in-force window. A
  provision is the act plus its `ArtikelParagraphAnlage` ("§ 24", "Art. 10", "Art. 2 § 24", "Anl. 1", "§ 0" for the
  title and promulgation clause). Its versions are its documents ordered by Inkrafttretensdatum; a document that
  ends before it begins was never in force and is left out; where two begin on one day, the one in force longer is
  used; where one overlaps the next, the next is used from its first day (each case is a data note).
- **Text.** The XML's part after the heading "Text" and before the next metadata heading. Each block (`absatz`,
  `ueberschrift`, `listelem`, table row) is one line, blank lines between: structure headings (typ g1, g2, …) are
  `##` lines, the provision's own heading `###`, list items `-` lines indented by level, table cells ` | `. Only white
  space is normalised (runs of spaces, tabs, line breaks and no-break spaces become one space) and soft hyphens are
  removed. Metadata (Beachte, Anmerkung, Schlagworte) stays in the commit message, not the file.
- **Days.** A version holds from its Inkrafttretensdatum to its Ausserkrafttretensdatum. If the next version does not
  begin the next day, the file is removed for the gap; after the last version's end it is removed.
- **Cause.** 1722 file changes, attributed as follows:

| Rule | File changes |
| --- | ---: |
| named law | 1111 |
| first version in RIS | 320 |
| removal: no law that day | 160 |
| same law as the version before | 65 |
| named repealing law | 31 |
| only the repealing law named: several laws that day | 16 |
| date-only version | 14 |
| only the repealing law named: no law that day | 2 |
| date-only removal | 2 |
| removal: several laws that day | 1 |

  "named law": RIS names a law in the version's Kundmachungsorgan ("zuletzt geändert durch") that differs from the
  version before. "first version in RIS": the first version RIS holds, credited to the law it names. "named repealing
  law": the last version's Kundmachungsorgan says "aufgehoben durch". "date-only": RIS names no law for the change,
  and exactly one law is named for versions of that act beginning that day (labelled `Evidence: date only`). The other
  rules credit no law: the commit is by `RIS (Bundeskanzleramt)` with `Candidate:` trailers.
- **Commits.** One commit per law per day across all acts (246 on main), one per day and set of candidate
  laws (7), one per day for changes nothing explains (47), in the order they
  took effect, then one documentation commit; 0 commits for days after 2026-10-28 are on `future`, which
  starts from main's documentation commit. 300 law-day commits on main in all.
  - The author is the law, `BGBl. I Nr. 70/2024`, at `bgbl-i-2024-70@ris.invalid` (`JGS Nr. 946/1811` at
    `jgs-1811-946@ris.invalid`, `dRGBl. S 219/1897` at `drgbl-1897-s219@ris.invalid`).
  - Author and committer dates are noon in Vienna on the in-force day: UTC+1, or UTC+2 in summer time (none 1949 to
    1979; from the last Sunday in March, the first Sunday in April in 1980, to the last Sunday in September until
    1995 and in October since 1996), written into the code because the build machine has no time-zone database. The
    committer is `Lexifina <austria-law@lexifina.com>`. 35 commits are before 1970 and are dated 1970-01-01,
    seconds apart, with the real day in `In-force:`.
  - Trailers: `Gazette:`, `Evidence:`, `Candidate:`, `In-force:`, `Date-note:`, `Affecting:`. The body lists, per
    act, the provisions new, amended or out of force, and each RIS document (NOR number) with its Kundmachungsorgan.
  - Tags: one per law (`bgbl-i/2024/70`; a law that took effect on several days has one per day,
    `bgbl-i/2018/24/2018-05-25`); 246 in all.
- **Documentation commit.** Dated 2026-10-28, the day the data was retrieved, not the day of the run.

## Decisions made by hand

1. **The acts.** The Federal Constitutional Act (B-VG) and the Data Protection Act (DSG): the constitution and one
   much-amended act, a small corpus checked in full. The RIS OGD hours (one connection, a two-second pause, nights and
   weekends only) make every act a night's fetch; the ABGB, StGB, UGB and ZPO are next, appended in later commits. The
   Gesetzesnummern were confirmed in the API (the Kurztitel of the documents returned).
2. **The per-version Kundmachungsorgan is the evidence, not the Aenderung list.** The brief suggested reading the
   amending law as the one that newly appears in a version's `Aenderung` list. In Bundesrecht konsolidiert that list
   is filled only on § 0, for the whole act; on each § it is empty. The Kundmachungsorgan of each version names the
   law that last amended it, which is the per-provision evidence used here.
3. **A repealed provision's last version.** RIS replaces its "zuletzt geändert durch" with "aufgehoben durch"; the
   law that wrote that version is then credited by date only, or not at all.
4. **German only**, the language of the source.

## What an AI model did

This repository was built in **Claude Code**, Anthropic's coding tool, by the model **Claude Opus 5.5** (model id
`claude-opus-5-5`), working from a brief by the user at Lexifina: a private "git for law" repository for Austria to
the same standard as Lexifina's other corpora.

The model:

- **Researched the source**: the RIS OGD API and its documents, its terms (the FAQ), robots.txt and the licence.
- **Wrote all the code and text in this repository**: the tools, the README, this file and the licence, and chose the
  design described in them.
- **Ran the commands above** and checked the results.

The model did **not**:

- **Write or edit any legal text.** Every word of every provision, every date and every law's designation is copied by
  the script from the RIS.
- **Take part in building the history.** No AI model runs when the history is built or checked.

The user decided the scope, sent the notice to the RIS before the bulk fetch, and decides whether the repository is
ever made public. The work was not reviewed line by line by a lawyer.

## Prior art

- Lexifina's other corpora, whose rules this one follows (the Swiss federal law and Liechtenstein builds, in German,
  and Slovakia, Estonia, Luxembourg, the Grundgesetz, UK legislation and the US Code).
