# How this history was made, and how to make it again

This file records how the `austria/bund/acts` repository was built from the official RIS Open Government Data API v2.6 (`https://data.bka.gv.at/ris/api/v2.6/Bundesrecht`).

## Short version

```sh
python3 -X utf8 tools/build.py --jurisdiction bund --repo . --today 2026-11-09 --offline
python3 -X utf8 tools/check_repo.py --jurisdiction bund --repo . --today 2026-11-09
python3 -X utf8 tools/test_repo.py --repo .
```

`data/fassungen.json` lists every RIS document (`NOR...` / `LBG...`) used, with the SHA-256 of its XML (sha256 of `data/fassungen.json`: `bf2cc88bda75b556dda9ea86c74eba2484eb95c38069a04965278a59ec67ac47`).

## Coverage (100 acts, 16703 provisions, 46113 versions in force)

| Act | Slug | Gesetzesnummer | RIS documents | Provisions | Versions in force | Data notes |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| B-VG | `b-vg/` | 10000138 | 1340 | 241 | 1262 | 2 |
| DSG | `dsg/` | 10001597 | 314 | 90 | 282 | 0 |
| AVG | `avg/` | 10005768 | 360 | 124 | 348 | 6 |
| VStG | `vstg/` | 10005770 | 327 | 106 | 323 | 0 |
| VwGVG | `vwgvg/` | 20008255 | 126 | 64 | 119 | 0 |
| VVG | `vvg/` | 10005772 | 54 | 19 | 51 | 0 |
| VStG-ÜR 1991 | `vstg-uer/` | 10005771 | 2 | 2 | 2 | 0 |
| ZustG | `zustg/` | 10005522 | 185 | 53 | 185 | 0 |
| ABGB | `abgb/` | 10001622 | 2566 | 1687 | 2558 | 9 |
| UGB | `ugb/` | 10001702 | 1681 | 972 | 1656 | 5 |
| KSchG | `kschg/` | 10002462 | 255 | 107 | 251 | 7 |
| MRG | `mrg/` | 10002531 | 220 | 94 | 214 | 2 |
| WEG 2002 | `weg-2002/` | 20001921 | 137 | 70 | 137 | 0 |
| GmbHG | `gmbhg/` | 10001720 | 328 | 175 | 325 | 2 |
| AktG | `aktg/` | 10002070 | 998 | 335 | 994 | 7 |
| URHG | `urhg/` | 10001848 | 373 | 191 | 373 | 9 |
| PATG-1970 | `patg-1970/` | 10002181 | 534 | 231 | 528 | 5 |
| MSCHG-1970 | `mschg-1970/` | 10002180 | 391 | 139 | 391 | 3 |
| StGB | `stgb/` | 10002296 | 1133 | 454 | 1104 | 20 |
| StPO | `stpo/` | 10002326 | 2191 | 662 | 2074 | 8 |
| ZPO | `zpo/` | 10001699 | 1105 | 705 | 1102 | 2 |
| JN | `jn/` | 10001697 | 290 | 169 | 280 | 5 |
| EO | `eo/` | 10001700 | 1766 | 684 | 1766 | 2 |
| VfGG | `vfgg/` | 10000245 | 558 | 145 | 538 | 0 |
| VwGG | `vwgg/` | 10000795 | 405 | 100 | 390 | 0 |
| GOG | `gog-nr/` | 10000576 | 485 | 167 | 483 | 4 |
| MedienG | `medieng/` | 10000719 | 266 | 130 | 260 | 5 |
| ASVG | `asvg/` | 10008147 | 5121 | 1235 | 4290 | 121 |
| ArbVG | `arbvg/` | 10008329 | 487 | 299 | 485 | 0 |
| AngG | `angg/` | 10008069 | 97 | 57 | 95 | 0 |
| URLG | `urlg/` | 10008376 | 56 | 26 | 56 | 0 |
| AZG | `azg/` | 10008238 | 334 | 80 | 331 | 0 |
| ARG | `arg/` | 10008541 | 186 | 52 | 184 | 0 |
| DHG | `dhg/` | 10008209 | 18 | 11 | 18 | 1 |
| EFZG | `efzg/` | 10008308 | 52 | 27 | 52 | 0 |
| AuslBG | `auslbeg/` | 10008365 | 480 | 82 | 466 | 1 |
| EStG 1988 | `estg-1988/` | 10004570 | 1989 | 181 | 1811 | 25 |
| UStG 1994 | `ustg-1994/` | 10004873 | 442 | 44 | 424 | 1 |
| KStG 1988 | `kstg-1988/` | 10004569 | 457 | 44 | 425 | 9 |
| BAO | `bao/` | 10003940 | 1399 | 428 | 1357 | 12 |
| FAG 2024 | `fag-2024/` | 20012472 | 53 | 37 | 52 | 0 |
| BHG 2013 | `bhg-2013/` | 20006632 | 257 | 134 | 230 | 0 |
| BVergG 2018 | `bvergg-2018/` | 20010295 | 563 | 404 | 561 | 0 |
| GewO 1994 | `gewo-1994/` | 10007517 | 1790 | 528 | 1772 | 5 |
| EG-K 2013 | `eg-k-2013/` | 20008506 | 112 | 59 | 112 | 0 |
| DRUCKGERAETEGESETZ | `druckgeraetegesetz/` | 20009418 | 124 | 81 | 124 | 0 |
| ASchG | `aschg/` | 10008910 | 448 | 144 | 445 | 0 |
| BauKG | `baukg/` | 10009146 | 38 | 24 | 34 | 0 |
| MinroG | `minrog/` | 10008040 | 437 | 255 | 434 | 0 |
| ROHRLEITUNGSGESETZ | `rohrleitungsgesetz/` | 10006405 | 114 | 54 | 114 | 0 |
| StrSchG 2020 | `strschg-2020/` | 20011197 | 161 | 159 | 161 | 0 |
| ElWOG 2010 | `elwog-2010/` | 20007045 | 277 | 146 | 275 | 0 |
| EAG | `eag/` | 20011619 | 263 | 117 | 242 | 0 |
| ÖSG 2012 | `oesg-2012/` | 20007386 | 190 | 76 | 190 | 0 |
| STWG | `stwg/` | 10006274 | 47 | 34 | 47 | 0 |
| EL-LEITUNGSANLAGEN-BG | `el-leitungsanlagen-bg/` | 10006275 | 37 | 28 | 37 | 0 |
| ETG 1992 | `etg-1992/` | 10012241 | 118 | 54 | 118 | 0 |
| E-ControlG | `e-controlg/` | 20007046 | 161 | 53 | 158 | 0 |
| EEffG | `eeffg/` | 20008914 | 111 | 89 | 111 | 1 |
| EnLG 2012 | `enlg-2012/` | 20008276 | 85 | 49 | 85 | 0 |
| GWG 2011 | `gwg-2011/` | 20007523 | 355 | 199 | 354 | 0 |
| UVP-G 2000 | `uvp-g/` | 10010767 | 373 | 76 | 370 | 0 |
| WRG 1959 | `wrg-1959/` | 10010290 | 716 | 233 | 707 | 0 |
| AWG 2002 | `awg-2002/` | 20002086 | 676 | 178 | 664 | 1 |
| ALSAG | `alsag/` | 10010583 | 228 | 49 | 219 | 0 |
| ForstG | `forstg/` | 10010371 | 414 | 211 | 414 | 0 |
| IG-L | `ig-l/` | 10011027 | 185 | 93 | 185 | 1 |
| BLRG | `blrg/` | 20002155 | 28 | 12 | 28 | 0 |
| Bundes-LärmG | `bundes-laermg/` | 20004158 | 15 | 15 | 15 | 0 |
| UIG | `uig/` | 10010766 | 65 | 22 | 65 | 0 |
| B-UHG | `b-uhg/` | 20006304 | 37 | 25 | 37 | 0 |
| ChemG 1996 | `chemg-1996/` | 10011071 | 425 | 87 | 425 | 0 |
| KFG 1967 | `kfg-1967/` | 10011384 | 1404 | 198 | 1370 | 22 |
| StVO 1960 | `stvo-1960/` | 10011336 | 620 | 150 | 613 | 5 |
| FSG | `fsg/` | 10012723 | 547 | 63 | 534 | 0 |
| BStG 1971 | `bstg-1971/` | 10011428 | 231 | 57 | 230 | 0 |
| BStMG | `bstmg/` | 20002090 | 255 | 49 | 254 | 0 |
| GGBG | `ggbg/` | 10012852 | 193 | 53 | 193 | 7 |
| KflG | `kflg/` | 20000098 | 233 | 75 | 231 | 0 |
| GelverkG | `gelverkg/` | 10007795 | 138 | 38 | 133 | 4 |
| GütbefG | `guetbefg/` | 10007643 | 178 | 46 | 174 | 0 |
| EisbG | `eisbg/` | 10011302 | 1240 | 457 | 1237 | 0 |
| LFG | `lfg/` | 10011306 | 1003 | 238 | 999 | 3 |
| SchFG | `schfg/` | 10012703 | 605 | 178 | 602 | 0 |
| DMSG | `dmsg/` | 10009184 | 142 | 54 | 142 | 0 |
| SPG | `spg/` | 10005792 | 700 | 153 | 670 | 0 |
| WaffG | `waffg/` | 10006016 | 344 | 96 | 333 | 5 |
| TSchG | `tschg/` | 20003541 | 275 | 67 | 273 | 0 |
| KDV 1967 | `kdv-1967/` | 10011385 | 662 | 255 | 653 | 23 |
| FSG-DV | `fsg-dv/` | 10012724 | 168 | 29 | 167 | 0 |
| PBStV | `pbstv/` | 10012794 | 137 | 30 | 137 | 0 |
| StVZVO 1998 | `stvzvo-1998/` | 10012793 | 31 | 20 | 31 | 0 |
| BMVO | `bmvo/` | 10012574 | 37 | 36 | 37 | 0 |
| OrgStVfgV | `orgstvfgv/` | 20000324 | 11 | 7 | 11 | 0 |
| KURZPARKZONEN-UEV | `kurzparkzonen-uev/` | 10012343 | 22 | 14 | 22 | 0 |
| ZustV | `zustv/` | 10012863 | 113 | 26 | 113 | 0 |
| VwFormV | `vwformv/` | 20008683 | 9 | 5 | 9 | 0 |
| ETV 2020 | `etv-2020/` | 20011222 | 17 | 13 | 17 | 0 |
| ABFALLVERZEICHNIS-V-2020 | `abfallverzeichnis-v-2020/` | 20011285 | 24 | 23 | 24 | 0 |
| DVO 2008 | `dvo-2008/` | 20005653 | 130 | 66 | 129 | 0 |

## Commits

- **4441** law-day commits on `main` (from `1812-01-01` to `2026-11-02`) + 1 documentation commit.
- **0** future law-day commits on `future` (for amendments promulgated in the Gazette with an `In-force` date after `2026-11-09`).

## Attribution & Licence

Quelle: Rechtsinformationssystem des Bundes (RIS), Bundeskanzleramt, https://www.ris.bka.gv.at, lizenziert unter CC BY 4.0.
Repository structure, commit history, tables and tools: CC0 1.0 Universal (see [`LICENSE`](LICENSE)).

## How the 98 further acts joined this repository

This repository first held B-VG and DSG (up to `1fbe3caae796`). The other 98 acts were built by MrKrojer with the
tools here, from the same RIS OGD API, as `KLex-Austria` (main `1c30fce07b85c48c3e7b374dde00ca47c8cc1eca`,
lexifina/global-law#21). Its B-VG and DSG history is the same as this repository's, commit for commit and byte for
byte: 300 commits, the same in-force dates and laws, and the same files on every one of those days.

Published commits are never rewritten, so its law commits were appended after `1fbe3caae796` instead of being merged
by date. Each keeps its author, its dates and its trailers; only the parent changed. A commit that changed only B-VG
or DSG was left out, because it is already here. A commit that also changed B-VG or DSG keeps only its other files,
and its message names the commit here that holds the B-VG and DSG changes. Readers take a provision's version from
its `In-force` trailer, not from the order of commits, so the appended history reads the same as KLex-Austria's.

`build.py --offline` rebuilds KLex-Austria's own history, in date order; to compare it with this repository, compare
the files on each `In-force` date, not the commit hashes.

The fetcher keeps to the RIS OGD terms by default: one connection, two seconds between requests, and requests only
from 20:00 to 05:00 Vienna time, at weekends or on public holidays (`--no-strict-hours` turns that off).
