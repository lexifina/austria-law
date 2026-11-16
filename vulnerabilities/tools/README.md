# Tools

The scripts behind this Austria-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/austria-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only austria-law, its commit and its
language (`de`). `build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py`, `patch_de.py` and
`config.json` sit three folders up, next to the copy of global-law (`gl/vulnerabilities/scripts/`).

| Script | What it does |
| --- | --- |
| `run.sh` | Applies `patch_de.py`, indexes the history and texts, adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category: the 11 whose old and new date open the same sentence, and the 29 shortest of the rest |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in German and English, light and dark |
| `config.json` | The repository, the German category names, the files and folders that are not law, and the chart's labels |
| `patch_de.py` | The Austrian German fixes below, in the copy of global-law's scripts (`python -X utf8 patch_de.py <scripts dir>`; a fix already in place is skipped) |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_detectors_vi.py` | The same for Vietnamese dates, references and amounts (found by the Vietnam run); it changes nothing here, but `redo.py` runs it on every repository |
| `patch_es.py` | The same for Spanish dates and for "marco" and "escudo" read as currencies; it changes nothing here either |
| `patch_ca.py` | The same for Catalan dates and time limits, the Catalan peseta, and "sucre" (sugar) read as a currency; it changes nothing here either |
| `map_moved.py` | For a repository that moved its act folders (`data/paths.json`), rewrites the paths in the history table to each act's folder since the move; this repository has not moved its folders, so it does nothing here |
| `redo.py` | Runs the patches, `patch_de.py` last, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--keep-reviews` keeps every review already made and reviews only new strong flags; `--full` runs every step again through `run.sh`, sends every category to the model and keeps every review already made; `EMBED_FONTS` names the script that embeds the chart's fonts) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
`run_triage.sh` was given `data/` and `tools/` as the folders that are not law; no flag is in them, so the 40 strongest
lapsed time limits in law texts are the 40 strongest of all.

The detectors carried the fixes in `patch_detectors.py`, `patch_detectors_vi.py` and `patch_es.py` when they were run.
`patch_ca.py` and the twelfth round of `patch_detectors.py` ("brisan" as a whole word) came later; the scans and detectors
they touch were run again and gave the same flags, so `redo.py` was not needed. `add_root.py` is unchanged: it counts all
4,513 commits of this repository as changes to the law. Changes made for this repository, all in `patch_de.py` (the
reference, currency and note fixes apply only where `pins.json` gives the language as `de`; the month names and fill words
apply to every language, in this copy only):

- Dates: the time-limit search reads the Austrian month names "Jänner" and "Feber", and the words "bis zum Ablauf des" and
  "bis einschließlich" between "bis" and the date ("bis zum Ablauf des 31. Dezember 2020"). Lapsed time limits went from
  541 to 701 and empty periods, which read the same dates, from 88 to 102.
- References: a section followed by another act's abbreviation or name is a reference to that act, not to a section of
  the citing act: a mixed-case or hyphenated abbreviation ("§ 221 Abs. 1 Z 2 UGB", "§ 70 ZaDiG 2018", "Art. 10 B-VG"),
  with "Abs.", "Z" and "lit." in between, an act's name ending in -gesetz, -ordnung, -vertrag and the like
  ("§ 26 Verwaltungsstrafgesetz 1991", "Artikel 73 der Wechselordnung"), but not "dieses Bundesgesetzes", and an act named
  after a list or range ("§§ 10, 17 und 18 VStG"). "§§ 70 bis 75" is a range, not a § 70bis; "S. 28" after an Official
  Journal citation is a page; and the RIS's notes ("(Anm.: aus BGBl. Nr. 475/1990, zu den §§ 96, ...)"), which name the
  provisions an amending act changed, are skipped like other amendment notes. References to deleted provisions went from
  495 to 323.
- Currencies: the Austrian schilling, as "Schilling" or as "S" after an amount ("5 000 S jährlich"), but not the page in
  "ABl. Nr. L 66 S 7". Dead currencies went from 1 to 105.
- Publisher notes: the RIS's own corrections, "(Anm.: richtig ...)", count like "[sic]". Publisher notes went from 37 to 74.

The scans and detectors these fixes touch, and the model review of references to deleted provisions, were run again after
them; two reviews made before the last reference fix are of flags it removed ("S. 31" in § 12c AuslBG and "S. 28" in
§ 137c GewO 1994, pages of the Official Journal), so 200 of the 202 reviews match a flag. A first version of
`patch_de.py` edited a line that `patch_detectors_vi.py` checks to know it is in place, so a second run of the patches
stopped there, and its schilling fix did not recognise itself once `patch_ca.py` had edited the line after it; both now
leave those lines as the other patches expect, with the same result.
`run.sh` takes `LE_WORKERS`, `LE_GREP_THREADS` and `LE_PRIORITY` from the environment when they are set, as `redo.py`
passes them.
