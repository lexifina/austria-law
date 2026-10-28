# Austrian federal law, change by change

Austrian federal acts as a git repository. Each amending law is one commit, credited to that law and dated the day it
took effect, at noon in Vienna. The text is the consolidated federal law ("Bundesrecht konsolidiert") that the
Federal Chancellery publishes in the [RIS](https://www.ris.bka.gv.at) (Rechtsinformationssystem des Bundes).

*Deutsch: [unten](#deutsch).*

| Act | Short title | Folder | Gesetzesnummer | Promulgated in | Provisions | Versions | From |
| --- | --- | --- | --- | --- | ---: | ---: | --- |
| B-VG | Bundes-Verfassungsgesetz | `b-vg/` | 10000138 | BGBl. Nr. 1/1930 | 241 | 1262 | 1930-01-03 |
| DSG | Datenschutzgesetz | `dsg/` | 10001597 | BGBl. I Nr. 165/1999 | 90 | 282 | 2000-01-01 |

## The questions, as git commands

| Question | Command |
| --- | --- |
| What did Art. 10 B-VG say on 1 January 2010? | `python tools/stand_am.py 2010-01-01 b-vg 10` |
| The whole DSG as it stood on 1 January 2020 | `python tools/stand_am.py 2020-01-01 dsg` |
| Which law wrote each paragraph of § 24 DSG? | `git blame dsg/art-002/par-0024.md` |
| Every change to § 24 DSG, with the law and the day | `git log --follow --format="%an %(trailers:key=In-force,valueonly,separator=)" dsg/art-002/par-0024.md` |
| Everything one law changed | `git show --stat bgbl-i/1934/255` |
| The laws, with the days they took effect | [`gesetze.csv`](gesetze.csv) |
| Changes RIS credits to no new law | `git log --oneline --author="RIS (Bundeskanzleramt)"` |
| Changes credited by date only | `git log --oneline --grep="Evidence: date only"` |
| Word by word, what a law changed in a file | `git log -p --word-diff dsg/art-002/par-0024.md` |

On PowerShell, `git show "$($c):path"` keeps the commit and the path together. To pick a commit by date with git alone,
use the trailer, not the commit date: `stand_am.py` reads `In-force:`, because git cannot store dates before 1970 and a
bare `--before=DATE` depends on your time of day and zone. After a rebuild, refresh tags with `git fetch --force --tags`.

## The dates, and which one we use

A federal law has the day the Nationalrat passed it, the day it was published in the Federal Law Gazette
(Bundesgesetzblatt, BGBl.), and the day each provision took effect. **Commits are dated the day the change took
effect** (`In-force:`), at noon in Vienna (CET, or CEST in summer time): that is the day that decides which text
applies. It is the first day of the version in RIS (Inkrafttretensdatum). A version ends on its Ausserkrafttretensdatum;
where the next version does not begin the day after, the provision was not in force in between and its file is removed.
Days before 1970 are kept in `In-force:`; git cannot store them, so those commits
are dated 1 January 1970, seconds apart, in order. Some laws took effect before they were published (a retroactive
in-force day); such commits say so in a `Date-note:` trailer. Changes not yet in force are on the branch `future`, never
on `main`.

## What "author" means

The author of a commit is the law that made the change, such as `BGBl. I Nr. 70/2024`, at an address ending
`@ris.invalid` (which cannot exist), so `git blame` names the law. RIS gives every version of a provision its own
document, and names in it the law that last amended it ("BGBl. I Nr. 165/1999 zuletzt geändert durch
BGBl. I Nr. 70/2024"). A version is credited to that law when it differs from the law RIS names for the version
before, or when it is the provision's first version in RIS. Two further rules, each labelled in an `Evidence:` trailer:

- RIS names a repealing law for a provision's last version ("aufgehoben durch …"): the removal is credited to it.
- Where RIS names no law (a removal without "aufgehoben durch", or a last version whose amending law RIS replaced with
  the repealing one), the change is credited **by date only** to the one law RIS names for versions of that act
  beginning that day.

Otherwise no law is credited: the commit is by `RIS (Bundeskanzleramt)`, says why, and names the possible laws in
`Candidate:` trailers. That includes a version for which RIS names the same law as for the version before (for
example a law that changed a provision in two steps, or a correction). The committer is always `Lexifina`.

Blame credits whole lines (one paragraph per line). Where two laws changed one paragraph, the later one is named:
use `git log -p --word-diff` for the words.

## How it is checked

`tools/check_repo.py` reads every version of every provision back from git on the day it took effect, and the version
before on the day before, and compares both with the text in RIS: file by file, and word for word with all the words
of the RIS document read without the build's parser. `tools/test_repo.py` checks that the commands above work. The
results are in [`REPRODUCE.md`](REPRODUCE.md).

## Files

Each act is a folder (`b-vg/`, `dsg/`). Each section, article or annex is one file named after its RIS
designation: `Art. 10` is `b-vg/art-010.md`, `Art. 2 § 24` is `dsg/art-002/par-0024.md`,
`Anl. 1` is `anl-1.md`, and `§ 0` (the title and promulgation clause) is `titel.md`. Each paragraph is one line; the
headings of the parts that begin with a provision are `##` lines, its own heading a `###` line, and list items are
`-` lines, indented by level. Tables are one line per row. Only white space is normalised.

## What it does not show

- **Text before RIS.** RIS keeps past versions only as far back as it records them. Before a provision's first
  version in RIS its file is absent: that is not a statement that the provision was not law.
- **The acts not listed above.** The builder works for any act in RIS: add its Gesetzesnummer.
- **Which of two laws of one day** made a change, where RIS does not say (above).
- **The authentic text.** The consolidated text in RIS is for information; only the Federal Law Gazette is authentic.

## How it is built

`tools/build.py` reads the RIS OGD API and writes this repository from scratch; the same data gives the same hashes.
Every step, the RIS access rules it keeps, the software, the decisions made by hand and what an AI model did are in
[`REPRODUCE.md`](REPRODUCE.md). [`corpus.json`](corpus.json) describes the corpus for tools that read several of
Lexifina's law repositories; `data/fassungen.json` lists every RIS document used, with its sha256.

## Licence

Laws and other official enactments are not protected by copyright in Austria (§ 7 Abs. 1 Urheberrechtsgesetz). The
consolidated text and its metadata come from the RIS Open Government Data interface, which the Federal Chancellery
licenses under Creative Commons Attribution 4.0 International (CC BY 4.0):

> Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter
> CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/deed.de). The text was rearranged into one file per provision,
> with white space normalised; no words were changed.

RIS gives no fixed wording for the attribution; this is ours. The RIS says that the consolidated text is not
authentic and that no legal claims can be derived from using it. The history, commit messages, tables and tools are
released under [CC0 1.0](LICENSE), as far as they are ours.

---

## Deutsch

Österreichisches Bundesrecht als git-Repository, aus dem Bundesrecht konsolidiert des RIS.

- **Jeder Commit ist ein Änderungsgesetz**, als Autor eingetragen (`BGBl. I Nr. 70/2024`), sodass `git blame` zeigt,
  welches Gesetz welchen Absatz geschrieben hat. Das Gesetz ist jenes, das das RIS für die Fassung nennt
  („zuletzt geändert durch“).
- **Jeder Commit trägt den Tag des Inkrafttretens** (`In-force:`), 12 Uhr in Wien.
- **Jeder Paragraph, Artikel und jede Anlage ist eine Datei**, jeder Absatz eine Zeile.
- **Änderungen, für die das RIS kein neues Gesetz nennt, werden keinem Gesetz zugeschrieben**; der Commit ist vom RIS
  und nennt die möglichen Gesetze.
- Noch nicht in Kraft getretene Änderungen stehen im Zweig `future`.

Quelle: Rechtsinformationssystem des Bundes (RIS), CC BY 4.0. Rechtlich verbindlich ist nur das Bundesgesetzblatt.
