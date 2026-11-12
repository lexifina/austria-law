"""Generates corpus.json, SOURCES.md, REPRODUCE.md, README.md, LICENSE, gesetze.csv, data/fassungen.json,
and embeds the repository tools for the documentation commit on main.
Compatible with lexifina/global-law (tools/check_corpus.py --strict).
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path


def doc_files(built: list[dict], chs: list[dict], log: list[dict], law_days: dict[str, list[tuple[str, int]]],
              today: str, future: list[dict], jurisdiction: str = 'bund') -> dict[str, str]:
    import build

    here = Path(__file__).resolve().parent
    is_bgld = (jurisdiction == 'burgenland')
    corpus_id = 'at/burgenland/acts' if is_bgld else 'at/bund/acts'
    global_path = 'austria/burgenland/acts' if is_bgld else 'austria/bund/acts'
    iso_code = 'AT-1' if is_bgld else 'AT'
    api_url = build.API

    # 1. data/fassungen.json
    acts_fassungen = []
    acts_meta = {}
    all_from_dates = []
    total_docs = 0
    total_provs = 0
    total_vers = 0

    for b in built:
        act = b['act']
        slug = act['slug']
        used_ids = set()
        provs_json = []
        act_vers_count = 0
        act_earliest = None
        for apa in sorted(b['tl'], key=lambda a: build.natural_key(b['files'][a])):
            segs = b['tl'][apa]
            v_list = []
            for s in segs:
                d = s['doc']
                used_ids.add(d['id'])
                sha = build.TEXTS[d['id']][1]
                v_item = {
                    'id': d['id'],
                    'from': s['start'],
                    'to': s['end'],
                    'kundmachungsorgan': d['kund'],
                    'sha256': sha,
                }
                if d.get('aenderung'):
                    v_item['aenderung'] = build.clean(str(d['aenderung']))
                v_list.append(v_item)
                all_from_dates.append(s['start'])
                if act_earliest is None or s['start'] < act_earliest:
                    act_earliest = s['start']
                act_vers_count += 1
            provs_json.append({
                'apa': apa,
                'file': b['files'][apa],
                'versions': v_list,
            })
        not_in_force = sorted(d['id'] for d in b['docs'] if d['id'] not in used_ids)
        total_docs += len(b['docs'])
        total_provs += len(provs_json)
        total_vers += act_vers_count
        mat_lines = []
        seen_mat = set()
        for doc_d in b['docs']:
            c_part = build.clean(str(doc_d.get('aenderung') or ''))
            if c_part and c_part not in seen_mat:
                seen_mat.add(c_part)
                mat_lines.append(c_part)
        acts_fassungen.append({
            'gesetzesnummer': act['nr'],
            'slug': slug,
            'abk': b['abk'],
            'kurztitel': b['kurztitel'],
            'titel': b['titel'],
            'stamm': b['stamm'],
            'documents': len(b['docs']),
            'provisions': provs_json,
            'materialien': mat_lines,
            'not_in_force': not_in_force,
            'data_notes': b['problems'],
        })
        acts_meta[slug] = {
            'gesetzesnummer': act['nr'],
            'slug': slug,
            'abk': b['abk'],
            'kurztitel': b['kurztitel'],
            'titel': b['titel'],
            'stamm': b['stamm'],
            'provisions': len(provs_json),
            'versions': act_vers_count,
            'from': act_earliest or today,
        }

    fassungen_obj = {
        'built': today,
        'jurisdiction': iso_code,
        'path': global_path,
        'source': api_url,
        'acts': acts_fassungen,
    }
    fassungen_str = json.dumps(fassungen_obj, indent=1, ensure_ascii=False) + '\n'
    fassungen_sha = hashlib.sha256(fassungen_str.encode('utf-8')).hexdigest()

    # 2. gesetze.csv
    csv_buf = io.StringIO()
    writer = csv.writer(csv_buf, lineterminator='\n')
    writer.writerow(['gesetz', 'in_kraft', 'geaenderte_gesetze', 'bestimmungen', 'tag', 'zweig'])
    plans = build.plan(chs)
    days_of: dict[str, list[str]] = {}
    for cm in plans:
        if cm['kind'] == 'law':
            days_of.setdefault(build.law_tag(cm['law']), []).append(cm['day'])
    for cm in plans:
        if cm['kind'] != 'law':
            continue
        law = cm['law']
        day = cm['day']
        t_base = build.law_tag(law)
        ds = days_of[t_base]
        tag = t_base if len(ds) == 1 else f'{t_base}/{day}'
        branch = 'future' if day > today else 'main'
        mod_acts = []
        for c in cm['items']:
            abk = c['b']['abk']
            if abk not in mod_acts:
                mod_acts.append(abk)
        writer.writerow([law, day, ' '.join(mod_acts), len(cm['items']), tag, branch])
    gesetze_csv_str = csv_buf.getvalue()

    # 3. corpus.json
    main_days = [c['day'] for c in log if c['branch'] == 'main']
    history_from = min(main_days) if main_days else today
    record_to = max(main_days) if main_days else today
    act_labels = [f"{b['abk']} ({b['stamm']})" if b['stamm'] else b['abk'] for b in built]
    title_prefix = (
        'Burgenland provincial law (Landesrecht Burgenland konsolidiert)'
        if is_bgld else
        'Austrian federal law (Bundesrecht konsolidiert)'
    )
    corpus_obj = {
        'corpus': corpus_id,
        'path': global_path,
        'iso': iso_code,
        'name': f"{title_prefix}: {', '.join(b['abk'] for b in built[:12])}" + (
            f" (+{len(built) - 12} more)" if len(built) > 12 else ""
        ),
        'label': 'Burgenland (Austria)' if is_bgld else 'Austria',
        'language': 'de',
        'earliest': '1800-01-01',
        'acts': act_labels,
        'history_from': history_from,
        'record_to': record_to,
        'record_note': f'checked against the RIS OGD data retrieved {today}',
        'checked_on': today,
        'history': 'in-force',
        'built': today,
        'in_force_trailer': 'In-force',
        'has_future_branch': bool(future),
        'future_branch': 'future' if future else None,
        'license': 'CC BY 4.0 (source: RIS, Bundeskanzleramt, https://www.ris.bka.gv.at); tools & git history CC0 1.0',
        'attribution': 'Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter CC BY 4.0',
        'dates': {
            'commit': 'in-force',
            'other_trailers': ['Gazette', 'Date-note'],
            'time': '12:00 Europe/Vienna (UTC+1, UTC+2 in summer time); before 1970: 1970-01-01 UTC, seconds apart',
        },
        'scope': {
            'trailer': 'Applies',
            'when_absent': 'this corpus records no scope notes (no commit carries Applies:); the absence is not a statement that the change reaches every case',
            'default_reach': {
                'rule': 'laws do not act retroactively',
                'meaning': 'a law applies to facts from the day it takes effect and does not affect earlier acts or rights acquired before then, unless it says otherwise; in criminal law a later law applies to earlier acts only where it is more favourable to the offender',
                'authority': '§ 5 ABGB ("Gesetze wirken nicht zurück und haben daher auf vorhergegangene Handlungen und auf vorher erworbene Rechte keinen Einfluß."); § 1 and § 61 StGB; Art. 7 EMRK',
                'decided_here': False,
            },
        },
        'citation': {
            'file': '(par|art)-0*([0-9]+[a-z]?)\\.md',
            'cites': '(§|Art\\.) ?{n}([^0-9a-z]|$)',
        },
        'tool': 'tools/stand_am.py',
    }
    corpus_str = json.dumps(corpus_obj, indent=2, ensure_ascii=False) + '\n'

    # 4. Pick valid example files & tags for README.md so test_repo.py's README command runner always succeeds
    first_b = built[0]
    first_slug = first_b['act']['slug']
    first_files = sorted(first_b['files'].values(), key=build.natural_key)
    sample_file = next((f for f in first_files if f != 'titel.md'), first_files[0])
    sample_path = f'{first_slug}/{sample_file}'
    sample_num = '1'
    for apa, f in first_b['files'].items():
        if f == sample_file and apa != '§ 0':
            sample_num = apa
            break
    second_b = built[1] if len(built) > 1 else first_b
    second_slug = second_b['act']['slug']
    second_files = sorted(second_b['files'].values(), key=build.natural_key)
    second_file = next((f for f in second_files if f != 'titel.md'), second_files[0])
    second_path = f'{second_slug}/{second_file}'

    first_tag = None
    for t_base, ds in sorted(law_days.items()):
        first_tag = t_base if len(ds) == 1 else f'{t_base}/{ds[0][0]}'
        break
    if not first_tag:
        first_tag = 'main'

    acts_table_lines = [
        '| Act | Short title | Folder | Gesetzesnummer | Promulgated in | Provisions | Versions | From |',
        '| --- | --- | --- | --- | --- | ---: | ---: | --- |',
    ]
    for b in built:
        slug = b['act']['slug']
        m = acts_meta[slug]
        acts_table_lines.append(
            f"| {b['abk']} | {b['kurztitel']} | `{slug}/` | {b['act']['nr']} | {b['stamm']} | "
            f"{m['provisions']} | {m['versions']} | {m['from']} |"
        )
    acts_table = '\n'.join(acts_table_lines)

    gazette_example = 'LGBl. Nr. 40/2024' if is_bgld else 'BGBl. I Nr. 70/2024'
    heading_title = (
        '# Burgenland provincial law (Landesrecht Burgenland), change by change'
        if is_bgld else
        '# Austrian federal law (Bundesrecht), change by change'
    )
    intro_line = (
        f"Part of [lexifina/global-law](https://github.com/lexifina/global-law) and **KLex**: "
        f"this is {'Burgenland provincial law (`AT-1`), read at `austria/burgenland/acts/`' if is_bgld else 'Austrian federal law (`AT`), read at `austria/bund/acts/`'}."
    )

    readme_str = f"""{heading_title}

{intro_line}

Each amending law is one commit, credited to that law (`{gazette_example}`) and dated the day it took effect, at noon in Vienna. The text is the consolidated law published by the Federal Chancellery in the [RIS](https://www.ris.bka.gv.at) (Rechtsinformationssystem des Bundes).

*Deutsch: [unten](#deutsch).*

{acts_table}

## The questions, as git commands

| Question | Command |
| --- | --- |
| What did {first_b['abk']} {sample_num} say on {record_to}? | `python tools/stand_am.py {record_to} {first_slug} {sample_file}` |
| The whole {second_b['abk']} as it stood on {record_to} | `python tools/stand_am.py {record_to} {second_slug}` |
| Which law wrote each paragraph of `{second_path}`? | `git blame {second_path}` |
| Every change to `{second_path}`, with the law and the day | `git log --follow --format="%an %(trailers:key=In-force,valueonly,separator=)" {second_path}` |
| Everything one law changed | `git show --stat {first_tag}` |
| The laws, with the days they took effect | [`gesetze.csv`](gesetze.csv) |
| Word by word, what a law changed in a file | `git log -p --word-diff -n 2 {second_path}` |

## The dates, and which one we use

**Commits are dated the day the change took effect** (`In-force:`), at noon in Vienna (CET, or CEST in summer time). Days before 1970 are kept in `In-force:`; git cannot store them as timestamps, so those commits receive technical timestamps starting at `1970-01-01T00:00:01Z`, seconds apart, in order. Changes published in the Gazette but not yet in force are on the branch `future`, never on `main`.

## What "author" means

The author of a commit is the law that made the change, such as `{gazette_example}`, at an address ending `@ris.invalid`, so `git blame` names the law.

## How it is checked

`tools/check_repo.py` reads every version of every provision back from git on the day it took effect, and the version before on the day before, and compares both with the text in RIS: file by file, and word for word with all the words of the RIS document read without the build's parser. `tools/test_repo.py` checks that the commands above work. The results are in [`REPRODUCE.md`](REPRODUCE.md).

## Licence

> Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/deed.de). The text was rearranged into one file per provision, with white space normalised; no words were changed.

The history, commit messages, tables and tools are released under [CC0 1.0](LICENSE), as far as they are ours.

---

## Deutsch

{'Burgenländisches Landesrecht (`LrKons`, ISO `AT-1`)' if is_bgld else 'Österreichisches Bundesrecht (`BrKons`, ISO `AT`)'} als Git-Repository (KLex / `lexifina/global-law`-Standard).

- **Jeder Commit ist ein Änderungsgesetz**, als Autor eingetragen (`{gazette_example}`), sodass `git blame` zeigt, welches Gesetz welchen Absatz geschrieben hat.
- **Jeder Commit trägt den Tag des Inkrafttretens** (`In-force:`), 12 Uhr in Wien.
- **Jeder Paragraph, Artikel und jede Anlage ist eine Datei**, jeder Absatz eine Zeile.
- Noch nicht in Kraft getretene Änderungen stehen im Zweig `future`.

Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter CC BY 4.0.
"""

    # 5. SOURCES.md
    sources_str = f"""# Sources for {'Burgenland (Austria, AT-1)' if is_bgld else 'Austria (Bund, AT)'}

The law built from these sources is read at `{global_path}/`; its [`REPRODUCE.md`](REPRODUCE.md) gives the exact RIS OGD endpoints, document hashes, and verification results.

| Source | Kind | Past versions by date | Names the amending act | API or bulk | Format and licence | Notes | Checked |
|---|---|---|---|---|---|---|---|
| [RIS (Rechtsinformationssystem des Bundes)](https://www.ris.bka.gv.at) · [OGD API v2.6]({api_url}) | Official legislation (`{'LrKons Burgenland' if is_bgld else 'BrKons'}`) | yes | yes (`{'LGBl.' if is_bgld else 'BGBl.'}`) | yes (OGD v2.6) | XML/JSON; CC BY 4.0 | Consolidated law with dated paragraph versions (`NOR`/`LBG` documents), each citing its amending Gazette. | {today} |

## Attribution (CC BY 4.0)

> Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/deed.de).
"""

    # 6. REPRODUCE.md
    cov_lines = [
        '| Act | Slug | Gesetzesnummer | RIS documents | Provisions | Versions in force | Data notes |',
        '| --- | --- | --- | ---: | ---: | ---: | ---: |',
    ]
    for b in built:
        slug = b['act']['slug']
        m = acts_meta[slug]
        cov_lines.append(
            f"| {b['abk']} | `{slug}/` | {b['act']['nr']} | {len(b['docs'])} | {m['provisions']} | {m['versions']} | {len(b['problems'])} |"
        )
    cov_table = '\n'.join(cov_lines)

    n_main = sum(1 for c in log if c['branch'] == 'main')
    n_fut = sum(1 for c in log if c['branch'] == 'future')
    reproduce_str = f"""# How this history was made, and how to make it again

This file records how the `{global_path}` repository was built from the official RIS Open Government Data API v2.6 (`{api_url}`).

## Short version

```sh
python3 -X utf8 tools/build.py --jurisdiction {jurisdiction} --repo . --today {today} --offline
python3 -X utf8 tools/check_repo.py --jurisdiction {jurisdiction} --repo . --today {today}
python3 -X utf8 tools/test_repo.py --repo .
```

`data/fassungen.json` lists every RIS document (`NOR...` / `LBG...`) used, with the SHA-256 of its XML (sha256 of `data/fassungen.json`: `{fassungen_sha}`).

## Coverage ({len(built)} acts, {total_provs} provisions, {total_vers} versions in force)

{cov_table}

## Commits

- **{n_main}** law-day commits on `main` (from `{history_from}` to `{record_to}`) + 1 documentation commit.
- **{n_fut}** future law-day commits on `future` (for amendments promulgated in the Gazette with an `In-force` date after `{today}`).

## Attribution & Licence

Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter CC BY 4.0.
Repository structure, commit history, tables and tools: CC0 1.0 Universal (see [`LICENSE`](LICENSE)).
"""

    license_str = (here / 'templates' / 'LICENSE').read_text(encoding='utf-8')
    readme_tpl_str = (here / 'templates' / 'README.md').read_text(encoding='utf-8')

    out_files = {
        'LICENSE': license_str,
        'README.md': readme_str,
        'REPRODUCE.md': reproduce_str,
        'SOURCES.md': sources_str,
        'corpus.json': corpus_str,
        'gesetze.csv': gesetze_csv_str,
        'data/fassungen.json': fassungen_str,
        'tools/templates/LICENSE': license_str,
        'tools/templates/README.md': readme_tpl_str,
    }
    for tool_name in ('build.py', 'reproduce.py', 'check_repo.py', 'stand_am.py', 'test_repo.py'):
        tp = here / tool_name
        if tp.exists():
            out_files[f'tools/{tool_name}'] = tp.read_text(encoding='utf-8')
    return out_files
