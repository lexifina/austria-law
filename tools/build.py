"""Builds a git repository of Austrian federal law (BrKons) or Burgenland provincial law (LrKons) from the RIS
(Rechtsinformationssystem des Bundes), in which every amending law (BGBl. / LGBl.) is one commit, dated the day it
took effect. 100% compatible with lexifina/global-law and lexifina/austria-law.

    python3 -X utf8 tools/build.py --jurisdiction bund|burgenland --today 2026-11-08 --repo ../repo [--offline]
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CACHE = Path(os.environ.get('KLEX_RIS_CACHE', str(HERE / '.cache')))
JURISDICTION = 'bund'
API = 'https://data.bka.gv.at/ris/api/v2.6/Bundesrecht'
UA = 'lexifina-watch/1.0 (+https://lexifina.com/watch; corpus@lexifina.com)'
PAUSE = 2.0          # seconds between requests (RIS OGD terms, FAQ of 28 Nov 2025: one connection, 2 s apart)
STRICT_HOURS = True   # RIS OGD terms: only 20:00-05:00 Vienna time, at weekends or on holidays
COMMITTER = ('Lexifina', 'austria-law@lexifina.com')
PUBLISHER = ('RIS (Bundeskanzleramt)', 'ris@ris-bka.invalid')
NS = '{http://www.bka.gv.at}'

ACTS_BUND = [
    # 1. Verfassung, Verwaltungsverfahren & Zustellung
    {'nr': '10000138', 'slug': 'b-vg'},                  # Bundes-Verfassungsgesetz (B-VG)
    {'nr': '10001597', 'slug': 'dsg'},                   # Datenschutzgesetz (DSG)
    {'nr': '10005768', 'slug': 'avg'},                   # Allgemeines Verwaltungsverfahrensgesetz 1991 (AVG)
    {'nr': '10005770', 'slug': 'vstg'},                  # Verwaltungsstrafgesetz 1991 (VStG)
    {'nr': '20008255', 'slug': 'vwgvg'},                 # Verwaltungsgerichtsverfahrensgesetz (VwGVG)
    {'nr': '10005772', 'slug': 'vvg'},                   # Verwaltungsvollstreckungsgesetz 1991 (VVG)
    {'nr': '10005771', 'slug': 'vstg-uer'},              # VStG-Übergangsrecht 1991
    {'nr': '10005522', 'slug': 'zustg'},                 # Zustellgesetz (ZustG)

    # 2. Zivil-, Unternehmens-, Wohn- & Konsumentenrecht
    {'nr': '10001622', 'slug': 'abgb'},                  # Allgemeines bürgerliches Gesetzbuch (ABGB)
    {'nr': '10001702', 'slug': 'ugb'},                   # Unternehmensgesetzbuch (UGB)
    {'nr': '10002462', 'slug': 'kschg'},                 # Konsumentenschutzgesetz (KSchG)
    {'nr': '10002531', 'slug': 'mrg'},                   # Mietrechtsgesetz (MRG)
    {'nr': '20001921', 'slug': 'weg-2002'},              # Wohnungseigentumsgesetz 2002 (WEG 2002)
    {'nr': '10001720', 'slug': 'gmbhg'},                 # Gesetz über Gesellschaften mit beschränkter Haftung (GmbHG)
    {'nr': '10002070', 'slug': 'aktg'},                  # Aktiengesetz (AktG)
    {'nr': '10001848', 'slug': 'urhg'},                  # Urheberrechtsgesetz (UrhG)
    {'nr': '10002181', 'slug': 'patg-1970'},             # Patentgesetz 1970 (PatG 1970)
    {'nr': '10002180', 'slug': 'mschg-1970'},            # Markenschutzgesetz 1970 (MSchG 1970)

    # 3. Justiz, Strafrecht, Zivilprozess & Höchstgerichte
    {'nr': '10002296', 'slug': 'stgb'},                  # Strafgesetzbuch (StGB)
    {'nr': '10002326', 'slug': 'stpo'},                  # Strafprozessordnung 1975 (StPO)
    {'nr': '10001699', 'slug': 'zpo'},                   # Zivilprozessordnung (ZPO)
    {'nr': '10001697', 'slug': 'jn'},                    # Jurisdiktionsnorm (JN)
    {'nr': '10001700', 'slug': 'eo'},                    # Exekutionsordnung (EO)
    {'nr': '10000245', 'slug': 'vfgg'},                  # Verfassungsgerichtshofgesetz 1953 (VfGG 1953)
    {'nr': '10000795', 'slug': 'vwgg'},                  # Verwaltungsgerichtshofgesetz 1985 (VwGG 1985)
    {'nr': '10000576', 'slug': 'gog-nr'},                # Geschäftsordnungsgesetz des Nationalrates (GOG-NR 1975)
    {'nr': '10000719', 'slug': 'medieng'},               # Mediengesetz (MedienG)

    # 4. Arbeit & Soziales
    {'nr': '10008147', 'slug': 'asvg'},                  # Allgemeines Sozialversicherungsgesetz (ASVG)
    {'nr': '10008329', 'slug': 'arbvg'},                 # Arbeitsverfassungsgesetz (ArbVG)
    {'nr': '10008069', 'slug': 'angg'},                  # Angestelltengesetz (AngG)
    {'nr': '10008376', 'slug': 'urlg'},                  # Urlaubsgesetz (UrlG)
    {'nr': '10008238', 'slug': 'azg'},                   # Arbeitszeitgesetz (AZG)
    {'nr': '10008541', 'slug': 'arg'},                   # Arbeitsruhegesetz (ARG)
    {'nr': '10008209', 'slug': 'dhg'},                   # Dienstnehmerhaftpflichtgesetz (DHG)
    {'nr': '10008308', 'slug': 'efzg'},                  # Entgeltfortzahlungsgesetz (EFZG)
    {'nr': '10008365', 'slug': 'auslbeg'},               # Ausländerbeschäftigungsgesetz (AuslBG)

    # 5. Steuern, Haushalt, Finanzen & Vergabe
    {'nr': '10004570', 'slug': 'estg-1988'},             # Einkommensteuergesetz 1988 (EStG 1988)
    {'nr': '10004873', 'slug': 'ustg-1994'},             # Umsatzsteuergesetz 1994 (UStG 1994)
    {'nr': '10004569', 'slug': 'kstg-1988'},             # Körperschaftsteuergesetz 1988 (KStG 1988)
    {'nr': '10003940', 'slug': 'bao'},                   # Bundesabgabenordnung (BAO)
    {'nr': '20012472', 'slug': 'fag-2024'},              # Finanzausgleichsgesetz 2024 (FAG 2024)
    {'nr': '20006632', 'slug': 'bhg-2013'},              # Bundeshaushaltsgesetz 2013 (BHG 2013)
    {'nr': '20010295', 'slug': 'bvergg-2018'},           # Bundesvergabegesetz 2018 (BVergG 2018)

    # 6. Gewerbe-, Betriebsanlagen-, Technik- & Arbeitnehmerschutzrecht
    {'nr': '10007517', 'slug': 'gewo-1994'},             # Gewerbeordnung 1994 (GewO 1994)
    {'nr': '20008506', 'slug': 'eg-k-2013'},             # Emissionsschutzgesetz für Kesselanlagen (EG-K 2013)
    {'nr': '20009418', 'slug': 'druckgeraetegesetz'},    # Druckgerätegesetz
    {'nr': '10008910', 'slug': 'aschg'},                 # ArbeitnehmerInnenschutzgesetz (ASchG)
    {'nr': '10009146', 'slug': 'baukg'},                 # Bauarbeitenkoordinationsgesetz (BauKG)
    {'nr': '10008040', 'slug': 'minrog'},                # Mineralrohstoffgesetz (MinroG)
    {'nr': '10006405', 'slug': 'rohrleitungsgesetz'},    # Rohrleitungsgesetz
    {'nr': '20011197', 'slug': 'strschg-2020'},          # Strahlenschutzgesetz 2020 (StrSchG 2020)

    # 7. Elektrizitäts- & Energierecht
    {'nr': '20007045', 'slug': 'elwog-2010'},            # Elektrizitätswirtschafts- und -organisationsgesetz 2010 (ElWOG 2010)
    {'nr': '20011619', 'slug': 'eag'},                   # Erneuerbaren-Ausbau-Gesetz (EAG)
    {'nr': '20007386', 'slug': 'oesg-2012'},             # Ökostromgesetz 2012 (ÖSG 2012)
    {'nr': '10006274', 'slug': 'stwg'},                  # Starkstromwegegesetz 1968 (StWG)
    {'nr': '10006275', 'slug': 'el-leitungsanlagen-bg'}, # BG über elektrische Leitungsanlagen (Grundsatzgesetz)
    {'nr': '10012241', 'slug': 'etg-1992'},              # Elektrotechnikgesetz 1992 (ETG 1992)
    {'nr': '20007046', 'slug': 'e-controlg'},            # Energie-Control-Gesetz (E-ControlG)
    {'nr': '20008914', 'slug': 'eeffg'},                 # Bundes-Energieeffizienzgesetz (EEffG)
    {'nr': '20008276', 'slug': 'enlg-2012'},             # Energielenkungsgesetz 2012 (EnLG 2012)
    {'nr': '20007523', 'slug': 'gwg-2011'},              # Gaswirtschaftsgesetz 2011 (GWG 2011)

    # 8. Wasser-, Abfall-, Forst- & Umweltrecht (UVP / Immissionsschutz)
    {'nr': '10010767', 'slug': 'uvp-g'},                 # Umweltverträglichkeitsprüfungsgesetz 2000 (UVP-G 2000)
    {'nr': '10010290', 'slug': 'wrg-1959'},              # Wasserrechtsgesetz 1959 (WRG 1959)
    {'nr': '20002086', 'slug': 'awg-2002'},              # Abfallwirtschaftsgesetz 2002 (AWG 2002)
    {'nr': '10010583', 'slug': 'alsag'},                 # Altlastensanierungsgesetz (ALSAG)
    {'nr': '10010371', 'slug': 'forstg'},                # Forstgesetz 1975 (ForstG 1975)
    {'nr': '10011027', 'slug': 'ig-l'},                  # Immissionsschutzgesetz – Luft (IG-L)
    {'nr': '20002155', 'slug': 'blrg'},                  # Bundesluftreinhaltegesetz (BLRG)
    {'nr': '20004158', 'slug': 'bundes-laermg'},         # Bundes-Umgebungslärmschutzgesetz (Bundes-LärmG)
    {'nr': '10010766', 'slug': 'uig'},                   # Umweltinformationsgesetz (UIG)
    {'nr': '20006304', 'slug': 'b-uhg'},                 # Bundes-Umwelthaftungsgesetz (B-UHG)
    {'nr': '10011071', 'slug': 'chemg-1996'},            # Chemikaliengesetz 1996 (ChemG 1996)

    # 9. Verkehrs-, Kraftfahr-, Infrastruktur- & Sonderanlagenrecht
    {'nr': '10011384', 'slug': 'kfg-1967'},              # Kraftfahrgesetz 1967 (KFG 1967)
    {'nr': '10011336', 'slug': 'stvo-1960'},             # Straßenverkehrsordnung 1960 (StVO 1960)
    {'nr': '10012723', 'slug': 'fsg'},                   # Führerscheingesetz (FSG)
    {'nr': '10011428', 'slug': 'bstg-1971'},             # Bundesstraßengesetz 1971 (BStG 1971)
    {'nr': '20002090', 'slug': 'bstmg'},                 # Bundesstraßen-Mautgesetz 2002 (BStMG)
    {'nr': '10012852', 'slug': 'ggbg'},                  # Gefahrgutbeförderungsgesetz (GGBG)
    {'nr': '20000098', 'slug': 'kflg'},                  # Kraftfahrliniengesetz (KflG)
    {'nr': '10007795', 'slug': 'gelverkg'},              # Gelegenheitsverkehrs-Gesetz 1996 (GelverkG)
    {'nr': '10007643', 'slug': 'guetbefg'},              # Güterbeförderungsgesetz 1995 (GütbefG)
    {'nr': '10011302', 'slug': 'eisbg'},                 # Eisenbahngesetz 1957 (EisbG)
    {'nr': '10011306', 'slug': 'lfg'},                   # Luftfahrtgesetz (LFG)
    {'nr': '10012703', 'slug': 'schfg'},                 # Schifffahrtsgesetz (SchFG)
    {'nr': '10009184', 'slug': 'dmsg'},                  # Denkmalschutzgesetz (DMSG)

    # 10. Sicherheit, Gesundheit & Tierschutz
    {'nr': '10005792', 'slug': 'spg'},                   # Sicherheitspolizeigesetz (SPG)
    {'nr': '10006016', 'slug': 'waffg'},                 # Waffengesetz 1996 (WaffG)
    {'nr': '20003541', 'slug': 'tschg'},                 # Tierschutzgesetz (TSchG)

    # 11. Zentrale Durchführungsverordnungen (Verkehr, Technik, Umwelt, Justiz)
    {'nr': '10011385', 'slug': 'kdv-1967'},              # Kraftfahrgesetz-Durchführungsverordnung 1967 (KDV 1967)
    {'nr': '10012724', 'slug': 'fsg-dv'},                # Führerscheingesetz-Durchführungsverordnung (FSG-DV)
    {'nr': '10012794', 'slug': 'pbstv'},                 # Prüf- und Begutachtungsstellenverordnung (PBStV)
    {'nr': '10012793', 'slug': 'stvzvo-1998'},           # Straßenverkehrszeichenverordnung 1998 (StVZVO 1998)
    {'nr': '10012574', 'slug': 'bmvo'},                  # Bodenmarkierungsverordnung (BMVO)
    {'nr': '20000324', 'slug': 'orgstvfgv'},             # Organstrafverfügungenverordnung (OrgStVfgV)
    {'nr': '10012343', 'slug': 'kurzparkzonen-uev'},     # Kurzparkzonen-Überwachungsverordnung
    {'nr': '10012863', 'slug': 'zustv'},                 # Zulassungsstellenverordnung (ZustV)
    {'nr': '20008683', 'slug': 'vwformv'},               # Verwaltungsformularverordnung (VwFormV - inkl. Anonymverfügung)
    {'nr': '20011222', 'slug': 'etv-2020'},              # Elektrotechnikverordnung 2020 (ETV 2020)
    {'nr': '20011285', 'slug': 'abfallverzeichnis-v-2020'}, # Abfallverzeichnisverordnung 2020
    {'nr': '20005653', 'slug': 'dvo-2008'},              # Deponieverordnung 2008 (DVO 2008)
]

ACTS_BURGENLAND = [
    # 1. Landesverfassung, Organisation & Gerichte
    {'nr': '10000141', 'slug': 'l-vg'},                  # Landes-Verfassungsgesetz (L-VG)
    {'nr': '20000221', 'slug': 'gemo'},                  # Burgenländische Gemeindeordnung 2003 (Bgld. GemO 2003)
    {'nr': '20000946', 'slug': 'lvwgg'},                 # Burgenländisches Landesverwaltungsgerichtsgesetz (Bgld. LVwGG)
    {'nr': '20001247', 'slug': 'lbedg'},                 # Burgenländisches Landesbedienstetengesetz 2020 (Bgld. LBedG 2020)
    {'nr': '20001481', 'slug': 'geol'},                  # Geschäftsordnung der Landesregierung (GeOL)
    {'nr': '20001472', 'slug': 'bh-geo'},                # Geschäftsordnung für die Bezirkshauptmannschaften im Burgenland

    # 2. Bauen, Raumordnung, Wohnen & Infrastruktur
    {'nr': '10000504', 'slug': 'baug'},                  # Burgenländisches Baugesetz 1997 (Bgld. BauG)
    {'nr': '20000684', 'slug': 'bgld-bauvo-2008'},       # Burgenländische Bauverordnung 2008 (Bgld. BauVO 2008)
    {'nr': '20001224', 'slug': 'rpg'},                   # Burgenländisches Raumplanungsgesetz 2019 (Bgld. RPG 2019)
    {'nr': '20000863', 'slug': 'lep-2011'},              # Landesentwicklungsprogramm 2011 (LEP 2011)
    {'nr': '20001187', 'slug': 'wfg-2018'},              # Burgenländisches Wohnbauförderungsgesetz 2018 (WFG 2018)
    {'nr': '20000352', 'slug': 'strassengesetz-2005'},   # Burgenländisches Straßengesetz 2005
    {'nr': '20000615', 'slug': 'gvg-2007'},              # Burgenländisches Grundverkehrsgesetz 2007 (Bgld. GVG 2007)

    # 3. Energie, Umwelt, Abfall & Naturschutz
    {'nr': '20000597', 'slug': 'elwg-2006'},             # Burgenländisches Elektrizitätswesengesetz 2006 (Bgld. ElWG 2006)
    {'nr': '20001332', 'slug': 'ezvo-pv-solar'},         # Bgld. Eignungszonenverordnung für Photovoltaik- und Solar-Freiflächenanlagen
    {'nr': '10000091', 'slug': 'starkstromwegegesetz'},  # Bgld. Starkstromwegegesetz
    {'nr': '10000365', 'slug': 'abfallwirtschaftsgesetz-1993'}, # Bgld. Abfallwirtschaftsgesetz 1993
    {'nr': '10000254', 'slug': 'ng'},                    # Burgenländisches Naturschutz- und Landschaftspflegegesetz (NG 1990)
    {'nr': '20000761', 'slug': 'uhg'},                   # Burgenländisches Umwelthaftungsgesetz (UHG)

    # 4. Landwirtschaft, Jagd, Fischerei & Weinbau
    {'nr': '20001124', 'slug': 'jagdg'},                 # Burgenländisches Jagdgesetz 2017 (Bgld. JagdG 2017)
    {'nr': '10000019', 'slug': 'fischereigesetz-1949'},  # Fischereigesetz 1949
    {'nr': '20001242', 'slug': 'weinbaug-2019'},         # Burgenländisches Weinbaugesetz 2019
    {'nr': '20000343', 'slug': 'landwirtschaftskammergesetz'}, # Burgenländisches Landwirtschaftskammergesetz

    # 5. Soziales, Bildung, Kinder & Kultur
    {'nr': '20001460', 'slug': 'shg'},                   # Burgenländisches Sozialhilfegesetz 2024 (Bgld. SHG 2024)
    {'nr': '20000713', 'slug': 'kbbg'},                  # Burgenländisches Kinderbildungs- und -betreuungsgesetz 2009 (Bgld. KBBG 2009)
    {'nr': '10000143', 'slug': 'kulturfoerderungsgesetz'}, # Burgenländisches Kulturförderungsgesetz
    {'nr': '20000258', 'slug': 'sportfoerderungsgesetz-2004'}, # Bgld. Sportförderungsgesetz 2004

    # 6. Tourismus, Freizeit, Veranstaltungen & Sicherheit
    {'nr': '20001302', 'slug': 'tg-2021'},               # Burgenländisches Tourismusgesetz 2021 (TG 2021)
    {'nr': '10000156', 'slug': 'camping-und-mobilheimplatzgesetz'}, # Bgld. Camping- und Mobilheimplatzgesetz
    {'nr': '10000372', 'slug': 'veranstaltungsgesetz'},  # Bgld. Veranstaltungsgesetz
    {'nr': '10000189', 'slug': 'katastrophenhilfegesetz'}, # Katastrophenhilfegesetz
]


def set_jurisdiction(jur: str):
    global JURISDICTION, API
    JURISDICTION = jur
    if jur == 'burgenland':
        API = 'https://data.bka.gv.at/ris/api/v2.6/Landesrecht'
    else:
        API = 'https://data.bka.gv.at/ris/api/v2.6/Bundesrecht'


def all_acts(jur: str | None = None, acts_file: str | None = None) -> list[dict]:
    j = jur or JURISDICTION
    if acts_file and Path(acts_file).exists():
        return json.loads(Path(acts_file).read_text(encoding='utf-8'))
    base = list(ACTS_BURGENLAND if j == 'burgenland' else ACTS_BUND)
    extra = HERE / (f'acts_{j}_extra.json' if j == 'burgenland' else 'acts_extra.json')
    if extra.exists():
        seen = {a['nr'] for a in base}
        for item in json.loads(extra.read_text(encoding='utf-8')):
            if item['nr'] not in seen:
                base.append(item)
                seen.add(item['nr'])
    return base


# ---------------------------------------------------------------- time in Vienna

def last_sunday(year: int, month: int) -> dt.date:
    d = (dt.date(year, month + 1, 1) if month < 12 else dt.date(year + 1, 1, 1)) - dt.timedelta(days=1)
    return d - dt.timedelta(days=(d.weekday() + 1) % 7)


def vienna_offset(day: dt.date) -> int:
    y = day.year
    if y < 1980:
        return 1
    start = (dt.date(1980, 4, 1) + dt.timedelta(days=(6 - dt.date(1980, 4, 1).weekday()) % 7)) if y == 1980 else last_sunday(y, 3)
    end = last_sunday(y, 9 if y < 1996 else 10)
    return 2 if start <= day < end else 1


def easter(y: int) -> dt.date:
    a, b, c = y % 19, y // 100, y % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    return dt.date(y, month, (h + l - 7 * m + 114) % 31 + 1)


def holiday(d: dt.date) -> bool:
    e = easter(d.year)
    moving = {e + dt.timedelta(days=n) for n in (1, 39, 50, 60)}
    fixed = {(1, 1), (1, 6), (5, 1), (8, 15), (10, 26), (11, 1), (12, 8), (12, 25), (12, 26)}
    return d in moving or (d.month, d.day) in fixed


def vienna_now() -> dt.datetime:
    utc = dt.datetime.now(dt.timezone.utc)
    y = utc.year
    start = dt.datetime.combine(last_sunday(y, 3), dt.time(1), dt.timezone.utc)
    end = dt.datetime.combine(last_sunday(y, 10), dt.time(1), dt.timezone.utc)
    off = 2 if start <= utc < end else 1
    return (utc + dt.timedelta(hours=off)).replace(tzinfo=None)


def fetch_allowed(now: dt.datetime) -> bool:
    if not STRICT_HOURS:
        return True
    return now.hour >= 20 or now.hour < 5 or now.weekday() >= 5 or holiday(now.date())


# ---------------------------------------------------------------- fetching

REQUESTS: list[dict] = []
TEXTS: dict[str, tuple[str, str]] = {}
TAGS: dict[str, int] = {}
_last = [0.0]
NET = {'count': 0}


def _get(url: str) -> bytes | None:
    while not fetch_allowed(vienna_now()):
        print(f'{vienna_now():%Y-%m-%d %H:%M} Vienna: outside the RIS OGD hours; waiting', flush=True)
        time.sleep(600)
    wait = _last[0] + PAUSE - time.monotonic()
    if wait > 0:
        time.sleep(wait)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip'})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read()
                if r.headers.get('Content-Encoding') == 'gzip':
                    body = gzip.decompress(body)
                return body
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            raise
        except urllib.error.URLError as exc:
            if 'CERTIFICATE' not in str(exc).upper():
                raise
            out = subprocess.run(['curl', '-sS', '-f', '--compressed', '-A', UA, url], capture_output=True)
            if out.returncode:
                raise RuntimeError(f'curl {url}: {out.stderr.decode(errors="replace")}')
            return out.stdout
    finally:
        _last[0] = time.monotonic()
        NET['count'] += 1


def cache_path(url: str) -> Path:
    return CACHE / hashlib.sha256(url.encode()).hexdigest()[:32]


def fetch(url: str, offline: bool = False, check=None) -> bytes | None:
    path = cache_path(url)
    REQUESTS.append({'url': url, 'file': path})
    if path.exists():
        return path.read_bytes()
    if path.with_suffix('.404').exists():
        return None
    if offline:
        raise SystemExit(f'not cached: {url}')
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / '.gitignore').write_text('*\n')
    for attempt in range(4):
        try:
            body = _get(url)
            if body is None:
                path.with_suffix('.404').write_bytes(b'')
                return None
            if check and not check(body):
                raise RuntimeError(f'unexpected answer for {url}: {body[:200]!r}')
            path.write_bytes(body)
            return body
        except Exception as exc:
            if attempt == 3:
                raise
            print(f'retry {attempt + 1} {url}: {exc}', flush=True)
            time.sleep(5 * (attempt + 1))
    raise AssertionError


# ---------------------------------------------------------------- the act's documents

def list_url(nr: str, page: int) -> str:
    if JURISDICTION == 'burgenland':
        return (f'{API}?Applikation=LrKons&Bundesland.SucheInBurgenland=true'
                f'&Gesetzesnummer={nr}&DokumenteProSeite=OneHundred&Seitennummer={page}')
    return f'{API}?Applikation=BrKons&Gesetzesnummer={nr}&DokumenteProSeite=OneHundred&Seitennummer={page}'


def as_list(x) -> list:
    return x if isinstance(x, list) else ([] if x is None else [x])


def clean(s: str | None) -> str:
    return re.sub(r'[\s\xa0]+', ' ', (s or '').replace('\xad', '')).strip()


def normalize_gazette(s: str) -> str:
    """Normalizes 'LGBl.Nr. 40/2024' -> 'LGBl. Nr. 40/2024' so LAW_RE parses both Bund and Land citations."""
    s = clean(s)
    s = re.sub(r'\b(LGBl|BGBl|StGBl|GBlÖ|dRGBl|ABl)\.\s*Nr\.', r'\1. Nr.', s)
    s = re.sub(r'\b(LGBl|BGBl|StGBl|GBlÖ|dRGBl)\s+Nr\.', r'\1. Nr.', s)
    return s


def normalize_apa(s: str | None) -> str:
    """Normalizes '§ 24 a' -> '§ 24a' and 'Art. 10 a' -> 'Art. 10a' so versions of the same provision share one timeline."""
    c = clean(s)
    c = re.sub(r'^((?:§§?|Art\.|Artikel|Anl\.|Anlage)\s*\d+)\s+([a-zA-Z])\b', r'\1\2', c)
    return c


ONLY_APA: set[str] = set()


def list_docs(nr: str, offline: bool) -> list[dict]:
    docs, page, hits = [], 1, None
    while True:
        raw = fetch(list_url(nr, page), offline, check=lambda b: b'OgdSearchResult' in b)
        res = json.loads(raw.decode('utf-8'))['OgdSearchResult']
        if 'OgdDocumentResults' not in res:
            raise SystemExit(f'{nr} page {page}: {str(res)[:300]}')
        r = res['OgdDocumentResults']
        hits = int(r['Hits']['#text'])
        refs = as_list(r.get('OgdDocumentReference'))
        for ref in refs:
            d = read_ref(ref)
            if d['xml']:
                docs.append(d)
        if not refs or len(docs) >= hits or len(refs) < 100:
            break
        page += 1
    # Deduplicate by document ID if RIS returns duplicates across pages
    by_id = {d['id']: d for d in docs}
    docs = [by_id[k] for k in sorted(by_id)]
    for d in docs:
        if d['gesnr'] != nr:
            raise SystemExit(f'{d["id"]} belongs to {d["gesnr"]}, not {nr}')
    if ONLY_APA:
        docs = [d for d in docs if d['apa'] in ONLY_APA]
    return sorted(docs, key=lambda d: d['id'])


BY_RE = re.compile(r'^(.*?)\s+((?:zuletzt )?geändert|aufgehoben|eingefügt|idF|in der Fassung)\s+durch\s+(.*)$')


def _extract_urls(docliste: dict) -> dict[str, str]:
    cref = docliste.get('ContentReference')
    refs = as_list(cref)
    urls: dict[str, str] = {}
    for item in refs:
        u_container = item.get('Urls') or {}
        for u in as_list(u_container.get('ContentUrl')):
            dt_type = u.get('DataType')
            url = u.get('Url')
            if dt_type and url and dt_type not in urls:
                urls[dt_type] = url
    return urls


def read_ref(ref: dict) -> dict:
    md = ref['Data']['Metadaten']
    if 'Landesrecht' in md:
        outer = md['Landesrecht']
        k = outer['LrKons']
    else:
        outer = md['Bundesrecht']
        k = outer['BrKons']
    urls = _extract_urls(ref['Data'].get('Dokumentliste') or {})
    kund = normalize_gazette(k.get('Kundmachungsorgan') or '')
    m = BY_RE.match(kund)
    stamm, rel, last = (normalize_gazette(m.group(1)), m.group(2), normalize_gazette(m.group(3))) if m else (kund, '', '')
    return {
        'id': md['Technisch']['ID'],
        'apa': normalize_apa(k.get('ArtikelParagraphAnlage')),
        'from': k.get('Inkrafttretensdatum'),
        'to': k.get('Ausserkrafttretensdatum'),
        'kund': kund,
        'stamm': stamm,
        'law': last or stamm,
        'rel': rel,
        'novelle': normalize_gazette(' '.join(x for x in (k.get('NovellenPublikationsorgan'), k.get('NovellenBgblnummer')) if x)),
        'kurztitel': clean(outer.get('Kurztitel')),
        'titel': outer.get('Titel') or '',
        'abk': clean(k.get('Abkuerzung')),
        'typ': clean(k.get('Typ')),
        'gesnr': str(k.get('Gesetzesnummer') or ''),
        'xml': urls.get('Xml'),
        'html': urls.get('Html'),
        'eli': outer.get('Eli') or k.get('Eli') or md.get('Allgemein', {}).get('DokumentUrl'),
        'beachte': clean(k.get('Beachte')),
        'anmerkung': clean(k.get('Anmerkung')),
        'ur': clean(k.get('Uebergangsrecht')),
        'aenderung': k.get('Aenderung') or '',
    }


# ---------------------------------------------------------------- one document's text

def local(e) -> str:
    t = e.tag
    return t[t.index('}') + 1:] if isinstance(t, str) and t[0] == '{' else (t if isinstance(t, str) else '')


BLOCK = {'ueberschrift', 'absatz', 'liste', 'aufzaehlung', 'listelem', 'table', 'tr', 'schlussteil', 'abschnitt',
         'gliederung', 'erlaeuterung', 'tbody', 'thead', 'tfoot', 'ziffernliste', 'kzinhalt', 'fzinhalt', 'binary',
         'quelle', 'p', 'div', 'pre', 'schluss', 'literaliste',
         'subliteraliste', 'subziffernliste', 'strichliste', 'substrichliste',
         'betragliste', 'subbetragliste', 'erlliste', 'suberlliste'}
GAP = {'tab', 'br', 'td', 'th'}


def text_section(raw: bytes) -> list:
    root = etree.fromstring(raw)
    out, on = [], False
    for ab in root.iter(NS + 'abschnitt'):
        for c in ab:
            name = local(c)
            if name == 'ueberschrift' and c.get('typ') == 'titel':
                on = clean(''.join(c.itertext())) == 'Text'
                continue
            if on and name not in ('kzinhalt', 'fzinhalt'):
                out.append(c)
    return out


def inline_child(c, skip_blocks: bool = True) -> str:
    name = local(c)
    if not name:
        return ''
    if name in GAP or name in BLOCK:
        return ' ' + inline(c, skip_blocks=skip_blocks) + ' '
    if name == 'symbol':
        return inline(c, skip_blocks=skip_blocks) + ' '
    return inline(c, skip_blocks=skip_blocks)


def inline(e, skip_blocks: bool = True) -> str:
    parts = [e.text or '']
    for c in e:
        if not (skip_blocks and local(c) in BLOCK):
            parts.append(inline_child(c, skip_blocks=skip_blocks))
        parts.append(c.tail or '')
    return ''.join(parts)


def runs(e) -> list:
    out, buf = [], [e.text or '']
    for c in e:
        if local(c) in BLOCK:
            out.append(''.join(buf))
            out.append(c)
            buf = []
        else:
            buf.append(inline_child(c))
        buf.append(c.tail or '')
    out.append(''.join(buf))
    return out


def render_blocks(els: list) -> list[str]:
    lines: list[str] = []

    def add(s: str):
        s = clean(s)
        if s:
            lines.append(s)

    def walk(e, level: int):
        name = local(e)
        if not name:
            return
        if name == 'ueberschrift':
            t = clean(inline(e))
            if t:
                lines.append(('## ' if (e.get('typ') or '').startswith('g') else '### ') + t)
        elif name == 'aufzaehlung':
            for c in e:
                walk(c, int(float(e.get('ebene') or 1)))
        elif name == 'listelem':
            first = True
            for r in runs(e):
                if isinstance(r, str):
                    t = clean(r)
                    if t:
                        lines.append('  ' * max(level - 1, 0) + ('- ' if first else '  ') + t)
                        first = False
                else:
                    walk(r, level + 1)
        elif name == 'table':
            def table_trs(node):
                for c in node:
                    cn = local(c)
                    if cn == 'tr':
                        yield c
                    elif cn != 'table':
                        yield from table_trs(c)
            for tr in table_trs(e):
                cells = [clean(inline(td, skip_blocks=False)) for td in tr if local(td) in ('td', 'th')]
                row = ' | '.join(x for x in cells if x)
                if row:
                    lines.append('| ' + row + ' |')
        elif name in BLOCK and any(local(c) in BLOCK for c in e):
            for r in runs(e):
                if isinstance(r, str):
                    add(r)
                else:
                    walk(r, int(float(r.get('ebene') or level)))
        else:
            add(inline(e, skip_blocks=False))

    for e in els:
        walk(e, 1)
    return lines


def render(raw: bytes) -> str:
    lines = render_blocks(text_section(raw))
    return '\n\n'.join(lines) + '\n' if lines else ''


# ---------------------------------------------------------------- names: laws and files

LAW_RE = re.compile(r'^(?P<org>[A-Za-zÄÖÜäöü]+\.?)(?:\s+(?P<part>I{1,3}))?\s*(?P<kind>Nr\.|S\.?)\s*(?P<n>\d+[a-z]?)'
                    r'\s*/\s*(?P<y>\d{4})(?P<rest>.*)$')


def law_parts(label: str) -> dict | None:
    m = LAW_RE.match(label)
    if not m:
        return None
    org = m.group('org').rstrip('.')
    return {'org': org, 'part': m.group('part') or '', 'kind': 'S' if m.group('kind').startswith('S') else 'Nr',
            'n': m.group('n'), 'y': int(m.group('y')), 'rest': clean(m.group('rest'))}


def ascii_slug(s: str) -> str:
    s = s.replace('Ä', 'Ae').replace('Ö', 'Oe').replace('Ü', 'Ue').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    s = s.replace('ß', 'ss').replace('§', 'par')
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def law_author(label: str) -> tuple[str, str]:
    p = law_parts(label)
    if not p:
        return label, f'{ascii_slug(label) or "law"}@ris.invalid'
    slug = '-'.join(x for x in (ascii_slug(p['org']), p['part'].lower(), str(p['y']),
                                ('s' if p['kind'] == 'S' else '') + p['n']) if x)
    return label, f'{slug}@ris.invalid'


def law_tag(label: str) -> str:
    p = law_parts(label)
    if not p:
        return 'law/' + (ascii_slug(label) or 'unknown')
    org = ascii_slug(p['org']) + (f'-{p["part"].lower()}' if p['part'] else '')
    return f'{org}/{p["y"]}/{("s" if p["kind"] == "S" else "") + p["n"]}'


def law_order(label: str) -> tuple:
    p = law_parts(label)
    if not p:
        return (9999, label, '', 0, '')
    n = re.match(r'\d+', p['n']).group(0)
    return (p['y'], p['org'], p['part'], int(n), p['n'])


def law_year(label: str) -> int | None:
    p = law_parts(label)
    return p['y'] if p else None


def num_part(prefix: str, x: str, width: int) -> str:
    m = re.fullmatch(r'(\d+)(.*)', x)
    if m:
        return f'{prefix}-{int(m.group(1)):0{width}d}{ascii_slug(m.group(2))}'
    return f'{prefix}-{ascii_slug(x)}'


def file_of(apa: str) -> str:
    if apa in ('§ 0', ''):
        return 'titel.md'
    toks = re.findall(r'(§§?|Art\.|Artikel|Anl\.|Anlage)\s*([^\s§]+)|(\S+)', apa)
    parts = []
    for kind, val, other in toks:
        if kind.startswith('§'):
            parts.append(num_part('par', val, 4))
        elif kind.startswith('Art'):
            parts.append(num_part('art', val, 3))
        elif kind.startswith('Anl'):
            parts.append(f'anl-{ascii_slug(val)}')
        elif other:
            parts.append(ascii_slug(other))
    parts = [p for p in parts if p]
    return ('/'.join(parts) if parts else 'titel') + '.md'


def natural_key(path: str) -> tuple:
    out = []
    for seg in path[:-3].split('/'):
        if seg == 'titel':
            out.append((0, 0, ''))
            continue
        m = re.fullmatch(r'(par|art|anl)-0*(\d*)(.*)', seg)
        if m:
            out.append(({'art': 1, 'par': 1, 'anl': 3}[m.group(1)], int(m.group(2) or 0), m.group(3)))
        else:
            out.append((2, 0, seg))
    return tuple(out)


# ---------------------------------------------------------------- one act: timelines and changes

def day_add(d: str, n: int) -> str:
    return (dt.date.fromisoformat(d) + dt.timedelta(days=n)).isoformat()


def timelines(docs: list[dict]) -> tuple[dict, list[str]]:
    by: dict[str, list[dict]] = {}
    problems = []
    for d in docs:
        if not d['from']:
            problems.append(f'{d["id"]} {d["apa"]}: no Inkrafttretensdatum')
            continue
        if d['to'] and d['to'] < d['from']:
            continue
        by.setdefault(d['apa'], []).append(d)
    out = {}
    for apa, vs in by.items():
        vs.sort(key=lambda d: (d['from'], d['to'] or '9999-99-99', d['id']))
        keep = []
        for v in vs:
            if keep and keep[-1]['from'] == v['from']:
                problems.append(f'{apa}: two versions from {v["from"]} ({keep[-1]["id"]}, {v["id"]}); the one in force '
                                f'longer is used')
                keep[-1] = v
                continue
            keep.append(v)
        segs = []
        for i, v in enumerate(keep):
            end = v['to']
            nxt = keep[i + 1] if i + 1 < len(keep) else None
            if nxt and (end is None or end >= nxt['from']):
                problems.append(f'{apa}: {v["id"]} ({v["from"]}..{v["to"]}) overlaps {nxt["id"]} from {nxt["from"]}; '
                                f'the later version is used from its first day')
                end = day_add(nxt['from'], -1)
            segs.append({'doc': v, 'start': v['from'], 'end': end})
        out[apa] = segs
    return out, problems


def build_act(act: dict, offline: bool, texts: dict) -> dict:
    docs = list_docs(act['nr'], offline)
    tl, problems = timelines(docs)
    files: dict[str, str] = {}
    used_files: set[str] = set()
    for apa in sorted(tl):
        f = file_of(apa)
        if f in used_files:
            base = f[:-3]
            idx = 2
            while f'{base}-{idx}.md' in used_files:
                idx += 1
            f = f'{base}-{idx}.md'
        files[apa] = f
        used_files.add(f)
    for segs in tl.values():
        for s in segs:
            d = s['doc']
            if d['id'] not in texts:
                raw = fetch(d['xml'], offline, check=lambda b: b'<risdok' in b)
                texts[d['id']] = (render(raw), hashlib.sha256(raw).hexdigest())
    if not docs:
        raise ValueError(f"No documents found in RIS for act {act['slug']} (nr={act['nr']})")
    newest = max(docs, key=lambda d: (d['from'] or '', d['id']))
    events = []
    for apa, segs in tl.items():
        prev = None
        for s in segs:
            if prev is None or prev['end'] is not None and day_add(prev['end'], 1) < s['start']:
                if prev is not None:
                    events.append((day_add(prev['end'], 1), apa, 'remove', None, prev))
                    events.append((s['start'], apa, 'set', s, None))
                else:
                    events.append((s['start'], apa, 'set', s, None))
            else:
                events.append((s['start'], apa, 'set', s, prev))
            prev = s
        if prev['end'] is not None:
            events.append((day_add(prev['end'], 1), apa, 'remove', None, prev))
    return {'act': act, 'docs': docs, 'tl': tl, 'files': files, 'events': events, 'problems': problems,
            'abk': newest['abk'] or act['slug'].upper(), 'kurztitel': newest['kurztitel'],
            'titel': clean(re.sub(r'<br\s*/?>.*$', '', newest['titel'], flags=re.S)), 'stamm': newest['stamm']}


def changes(built: list[dict], texts: dict) -> list[dict]:
    out = []
    for b in built:
        day_laws: dict[str, set[str]] = {}
        for day, apa, kind, s, prev in b['events']:
            if kind == 'set' and s['doc']['rel'] != 'aufgehoben' and s['doc']['law']:
                day_laws.setdefault(day, set()).add(s['doc']['law'])
            if kind == 'remove' and prev['doc']['rel'] == 'aufgehoben' and prev['doc']['law']:
                day_laws.setdefault(day, set()).add(prev['doc']['law'])

        def by_date(day: str) -> tuple[str, list[str]]:
            cands = sorted(day_laws.get(day, set()), key=law_order)
            return (cands[0] if len(cands) == 1 else 'candidates' if cands else 'unexplained'), cands

        current: dict[str, dict | None] = {}
        last_doc: dict[str, dict] = {}
        for day, apa, kind, s, prev in sorted(b['events'], key=lambda e: (e[0], e[1], e[2] == 'set')):
            cur = current.get(apa)
            old = texts[cur['doc']['id']][0] if cur else None
            if kind == 'remove':
                current[apa] = None
                if old is None:
                    continue
                if prev['doc']['rel'] == 'aufgehoben' and prev['doc']['law']:
                    cause, why, cands = prev['doc']['law'], 'named repealing law', []
                else:
                    cause, cands = by_date(day)
                    why = {'candidates': 'removal: several laws that day', 'unexplained': 'removal: no law that day'}.get(
                        cause, 'date-only removal')
                out.append({'day': day, 'b': b, 'apa': apa, 'kind': 'removed', 'text': None, 'doc': prev['doc'],
                            'cause': cause, 'why': why, 'cands': cands})
                continue
            new = texts[s['doc']['id']][0]
            prev_doc = last_doc.get(apa)
            current[apa] = s
            last_doc[apa] = s['doc']
            if new == old:
                continue
            law = s['doc']['law']
            if s['doc']['rel'] == 'aufgehoben' or not law:
                cause, cands = by_date(day)
                why = {'candidates': 'only the repealing law named: several laws that day',
                       'unexplained': 'only the repealing law named: no law that day'}.get(cause, 'date-only version')
            elif prev_doc is None:
                cause, why, cands = law, 'first version in RIS', []
            elif prev_doc['law'] != law or prev_doc['rel'] == 'aufgehoben':
                cause, why, cands = law, 'named law', []
            else:
                cause, why, cands = 'unexplained', 'same law as the version before', [law]
            out.append({'day': day, 'b': b, 'apa': apa, 'kind': 'new' if old is None else 'amended', 'text': new,
                        'doc': s['doc'], 'cause': cause, 'why': why, 'cands': cands})
    return out


# ---------------------------------------------------------------- commits

def commit_date(day: str, seq: list[int]) -> str:
    d = dt.date.fromisoformat(day)
    if d.year < 1970:
        seq[0] += 1
        return f'{seq[0]} +0000'
    off = vienna_offset(d)
    stamp = int(dt.datetime(d.year, d.month, d.day, 12, tzinfo=dt.timezone(dt.timedelta(hours=off))).timestamp())
    return f'{stamp} +0{off}00'


KIND_DE = {'new': 'Neu', 'amended': 'Geändert', 'removed': 'Außer Kraft'}


def plan(chs: list[dict]) -> list[dict]:
    groups: dict[tuple, list[dict]] = {}
    for c in chs:
        if c['cause'] == 'candidates':
            key = (c['day'], 1, tuple(law_order(x) for x in c['cands']), 'candidates', tuple(c['cands']))
        elif c['cause'] == 'unexplained':
            key = (c['day'], 2, (), 'unexplained', ())
        else:
            key = (c['day'], 0, law_order(c['cause']), c['cause'], ())
        groups.setdefault(key, []).append(c)
    out = []
    for key in sorted(groups):
        items = sorted(groups[key], key=lambda c: (c['b']['act']['slug'], natural_key(c['b']['files'][c['apa']])))
        out.append({'day': key[0], 'kind': ['law', 'candidates', 'unexplained'][key[1]], 'law': key[3],
                    'cands': list(key[4]), 'items': items})
    return out


def label_of(c: dict) -> str:
    return f'{c["b"]["abk"]} {c["apa"] if c["apa"] != "§ 0" else "Titel"}'


def message(cm: dict) -> tuple[tuple[str, str], str]:
    day, items = cm['day'], cm['items']
    labels = [label_of(c) for c in items]
    acts = []
    for c in items:
        if c['b']['abk'] not in acts:
            acts.append(c['b']['abk'])
    if cm['kind'] == 'law':
        head = cm['law']
        author = law_author(cm['law'])
    elif cm['kind'] == 'candidates':
        head = 'mehrere Gesetze'
        author = PUBLISHER
    else:
        head = 'ohne neues Gesetz'
        author = PUBLISHER
    subject = f'{", ".join(labels)} ({head})'
    if len(subject) > 72:
        subject = f'{"; ".join(acts)}: {len(items)} Bestimmungen ({head})'
    if len(subject) > 72:
        subject = f'{len(items)} Bestimmungen in {len(acts)} Gesetzen ({head})'
    body = []
    whys: dict[str, list[str]] = {}
    for c in items:
        whys.setdefault(c['why'], []).append(label_of(c))
    if cm['kind'] == 'law':
        body += [f'{cm["law"]}, in Kraft am {day}.', '', f'{cm["law"]}, in force on {day}.', '']
    elif cm['kind'] == 'candidates':
        names = ', '.join(cm['cands'])
        body += [f'An diesem Tag traten im Gesetz mehrere Gesetze in Kraft ({names}). Das RIS sagt nicht, welches die',
                 'folgenden Änderungen bewirkt hat; der Commit wird keinem von ihnen zugeschrieben.', '',
                 f'Several laws took effect in the act on this day ({names}). RIS does not say which of them made the',
                 'changes below, so they are credited to none of them.', '']
    else:
        body += ['Das RIS nennt für diese Änderungen kein Gesetz, das sie bewirkt hätte; der Commit wird keinem Gesetz',
                 'zugeschrieben.', '',
                 'RIS names no law that made these changes, so they are credited to no law.', '']
    by_act: dict[str, list[dict]] = {}
    for c in items:
        by_act.setdefault(c['b']['abk'], []).append(c)
    for abk, cs in by_act.items():
        b = cs[0]['b']
        body.append(f'{abk} ({b["kurztitel"]}):')
        for kind in ('new', 'amended', 'removed'):
            ks = [c for c in cs if c['kind'] == kind]
            if ks:
                body.append(f'  {KIND_DE[kind]}: ' + ', '.join(c['apa'] if c['apa'] != '§ 0' else 'Titel' for c in ks))
        body.append('')
    body.append('Fassungen im RIS (versions in RIS):')
    for c in items:
        d = c['doc']
        if c['kind'] == 'removed':
            body.append(f'- {label_of(c)}: {d["id"]}, in Kraft bis {d["to"]} ({d["kund"]})')
        else:
            body.append(f'- {label_of(c)}: {d["id"]} ({d["kund"]})')
    body.append('')
    trailers = []
    law = cm['law']
    ev = {
        'named law': f'RIS names {law} as the law that last amended the new version (zuletzt geaendert durch), and '
                     f'another law for the version before',
        'first version in RIS': f'the first version of the provision in RIS, for which RIS names {law}',
        'named repealing law': f'RIS names {law} as the repealing law of the last version (aufgehoben durch)',
        'date-only removal': 'date only (removal): RIS names no law for it, and this is the only law RIS names for '
                             'versions of the act beginning that day',
        'date-only version': 'date only: RIS names only the later repealing law for this version, and this is the only '
                             'law RIS names for versions of the act beginning that day',
        'removal: several laws that day': 'removal for which RIS names no law, on a day several laws took effect in the act',
        'only the repealing law named: several laws that day': 'RIS names only the later repealing law for this version, '
                                                              'on a day several laws took effect in the act',
        'same law as the version before': 'RIS names the same law for this version as for the one before',
        'removal: no law that day': 'removal for which RIS names no law, on a day no law took effect in the act',
        'only the repealing law named: no law that day': 'RIS names only the later repealing law for this version, and '
                                                        'no law took effect in the act that day',
    }
    if cm['kind'] == 'law':
        trailers.append(f'Gazette: {law}')
    for why in sorted(whys):
        n = len(whys[why])
        trailers.append(f'Evidence: {ev[why]} ({n} provision{"s" if n > 1 else ""})')
    cands = cm['cands'] if cm['kind'] == 'candidates' else sorted(
        {x for c in items for x in c['cands']}, key=law_order)
    trailers += [f'Candidate: {x}' for x in cands]
    trailers.append(f'In-force: {day}')
    y = law_year(cm['law']) if cm['kind'] == 'law' else None
    if y and int(day[:4]) < y:
        trailers.append(f'Date-note: in force before the year of its Gazette number ({y}), as RIS gives it')
    aff = ', '.join(labels)
    trailers.append(f'Affecting: {aff}')
    if day < '1970-01-01':
        body += ['Git kann kein Datum vor 1970 speichern: der Commit ist auf den 1. Januar 1970 datiert, der Tag des',
                 'Inkrafttretens steht in In-force. (Git cannot record dates before 1970: the real day is In-force.)', '']
    return author, f'{subject}\n\n' + '\n'.join(body).rstrip('\n') + '\n\n' + '\n'.join(trailers) + '\n'


class FastImport:
    def __init__(self, repo: Path):
        self.p = subprocess.Popen(['git', 'fast-import', '--quiet', '--done', '--date-format=raw'], cwd=repo,
                                  stdin=subprocess.PIPE)
        self.mark = 0

    def w(self, b: bytes):
        self.p.stdin.write(b)

    def data(self, s: str):
        b = s.encode('utf-8')
        self.w(f'data {len(b)}\n'.encode() + b + b'\n')

    def commit(self, ref: str, author: tuple[str, str], when: str, msg: str, parent: int | None, ops: list[tuple]) -> int:
        self.mark += 1
        self.w(f'commit {ref}\nmark :{self.mark}\n'.encode())
        self.w(f'author {author[0]} <{author[1]}> {when}\ncommitter {COMMITTER[0]} <{COMMITTER[1]}> {when}\n'.encode('utf-8'))
        self.data(msg)
        if parent:
            self.w(f'from :{parent}\n'.encode())
        for op in ops:
            if op[1] is None:
                self.w(f'D {op[0]}\n'.encode())
            else:
                self.w(f'M 100644 inline {op[0]}\n'.encode())
                self.data(op[1])
        self.w(b'\n')
        return self.mark

    def tag(self, name: str, mark: int):
        self.w(f'reset refs/tags/{name}\nfrom :{mark}\n\n'.encode())

    def finish(self):
        self.w(b'done\n')
        self.p.stdin.close()
        if self.p.wait():
            raise SystemExit('git fast-import failed')


def git(repo: Path, *args: str) -> str:
    out = subprocess.run(['git', *args], cwd=repo, capture_output=True, text=True, encoding='utf-8')
    if out.returncode:
        raise SystemExit(f'git {" ".join(args)} failed: {out.stderr}')
    return out.stdout


def prepare_repo(repo: Path) -> str | None:
    remote = None
    if repo.exists() and any(repo.iterdir()):
        if not (repo / '.git').exists():
            raise SystemExit(f'{repo} is not empty and not a git repository; refusing to overwrite it')
        out = subprocess.run(['git', 'remote', 'get-url', 'origin'], cwd=repo, capture_output=True, text=True)
        remote = out.stdout.strip() or None

        def force(fn, path, _exc):
            os.chmod(path, 0o700)
            fn(path)
        for p in repo.iterdir():
            shutil.rmtree(p, onexc=force) if p.is_dir() else p.unlink()
    repo.mkdir(parents=True, exist_ok=True)
    git(repo, 'init', '-q', '-b', 'main')
    git(repo, 'config', 'core.autocrlf', 'false')
    git(repo, 'config', 'core.quotepath', 'false')
    if remote:
        git(repo, 'remote', 'add', 'origin', remote)
    return remote


def write_repo(repo: Path, built: list[dict], chs: list[dict], today: str) -> tuple[list[dict], dict, dict]:
    prepare_repo(repo)
    fi = FastImport(repo)
    seq = [0]
    log = []
    law_days: dict[str, list[tuple[str, int]]] = {}
    parent = None
    main_tip = None
    future: list[dict] = []
    plans = plan(chs)
    days_of: dict[str, list[str]] = {}
    for cm in plans:
        if cm['kind'] == 'law':
            days_of.setdefault(law_tag(cm['law']), []).append(cm['day'])
    TAGS.clear()
    for t_base, ds in days_of.items():
        for d in ds:
            TAGS[t_base if len(ds) == 1 else f'{t_base}/{d}'] = 0
    for cm in plans:
        if cm['day'] > today:
            future.append(cm)
            continue
        author, msg = message(cm)
        ops = [(f'{c["b"]["act"]["slug"]}/{c["b"]["files"][c["apa"]]}', c['text']) for c in cm['items']]
        parent = fi.commit('refs/heads/main', author, commit_date(cm['day'], seq), msg, parent, ops)
        if cm['kind'] == 'law':
            law_days.setdefault(law_tag(cm['law']), []).append((cm['day'], parent))
        log.append({'day': cm['day'], 'kind': cm['kind'], 'law': cm['law'], 'items': len(cm['items']), 'mark': parent,
                    'clamped': cm['day'] < '1970-01-01', 'branch': 'main'})
    sys.path.insert(0, str(HERE))
    from reproduce import doc_files
    files = doc_files(built, chs, log, law_days, today, future, jurisdiction=JURISDICTION)
    when = commit_date(today, seq)
    parent = fi.commit('refs/heads/main', COMMITTER, when,
                       'Dokumentation, Tabellen, Werkzeuge und REPRODUCE.md\n\nDocumentation, tables, tools and REPRODUCE.md\n',
                       parent, sorted(files.items()))
    main_tip = parent
    fut_parent = parent
    for cm in future:
        author, msg = message(cm)
        ops = [(f'{c["b"]["act"]["slug"]}/{c["b"]["files"][c["apa"]]}', c['text']) for c in cm['items']]
        fut_parent = fi.commit('refs/heads/future', author, commit_date(cm['day'], seq), msg, fut_parent, ops)
        if cm['kind'] == 'law':
            law_days.setdefault(law_tag(cm['law']), []).append((cm['day'], fut_parent))
        log.append({'day': cm['day'], 'kind': cm['kind'], 'law': cm['law'], 'items': len(cm['items']),
                    'mark': fut_parent, 'clamped': False, 'branch': 'future'})
    tags = {}
    for t_base, days in sorted(law_days.items()):
        if len(days) == 1:
            tags[t_base] = days[0][1]
        else:
            for day, mark in days:
                tags[f'{t_base}/{day}'] = mark
    for name, mark in sorted(tags.items()):
        fi.tag(name, mark)
    fi.finish()
    git(repo, 'checkout', '-q', '-f', 'main')
    return log, tags, {'main_tip': main_tip}


def build_all(acts: list[dict], offline: bool) -> tuple[list[dict], dict, list[dict]]:
    texts = TEXTS
    built = []
    for a in acts:
        b = build_act(a, offline, texts)
        built.append(b)
        print(f'{a["slug"]}: {len(b["docs"])} documents, {len(b["tl"])} provisions, '
              f'{sum(len(s) for s in b["tl"].values())} versions in force; {len(b["problems"])} data notes; '
              f'{NET["count"]} requests so far', flush=True)
    chs = changes(built, texts)
    return built, texts, chs


def main():
    global PAUSE, STRICT_HOURS
    sys.modules['build'] = sys.modules[__name__]
    ap = argparse.ArgumentParser()
    ap.add_argument('--jurisdiction', choices=('bund', 'burgenland'), default='bund')
    ap.add_argument('--repo', required=True)
    ap.add_argument('--acts-file', default=None, help='optional JSON list of [{"nr": ..., "slug": ...}]')
    ap.add_argument('--offline', action='store_true', help='read only the cache; fail on anything not cached')
    ap.add_argument('--today', required=True, help='the build day: the day the data was retrieved')
    ap.add_argument('--only', default=None, help='comma-separated Gesetzesnummern (default: all acts)')
    ap.add_argument('--provisions', default=None, help='for tests only: keep just these APA values, separated by ";"')
    ap.add_argument('--fetch-only', action='store_true', help='fill the cache and stop')
    ap.add_argument('--rate', type=float, default=0.5, help='requests per second (default: 0.5, the RIS OGD terms)')
    ap.add_argument('--strict-hours', action=argparse.BooleanOptionalAction, default=True,
                    help='keep to the RIS OGD hours, 20:00-05:00 Vienna time or weekends and holidays (default: on)')
    ap.add_argument('--verify-rebuild', action='store_true')
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    set_jurisdiction(args.jurisdiction)
    PAUSE = 1.0 / max(args.rate, 0.1)
    STRICT_HOURS = args.strict_hours
    acts = all_acts(args.jurisdiction, args.acts_file)
    if args.provisions:
        ONLY_APA.update(x.strip() for x in args.provisions.split(';'))
    if args.only:
        want = set(args.only.split(','))
        acts = [a for a in acts if a['nr'] in want]
    if args.verify_rebuild:
        verify_rebuild(args)
        return
    if args.fetch_only:
        texts: dict = {}
        for a in acts:
            build_act(a, args.offline, texts)
            print(f'{a["slug"]}: cached; {NET["count"]} requests so far', flush=True)
        return
    t0 = time.time()
    built, texts, chs = build_all(acts, args.offline)
    for b in built:
        for p in b['problems']:
            print(f'   {b["act"]["slug"]}: {p}')
    log, tags, info = write_repo(Path(args.repo), built, chs, args.today)
    n_fut = sum(1 for c in log if c['branch'] == 'future')
    print(f'repo ({args.jurisdiction}): {len(log) - n_fut} commits on main + 1 documentation commit, {n_fut} on future, '
          f'{len(tags)} tags, {len(chs)} file changes -> {args.repo} ({time.time() - t0:.1f} s)', flush=True)


def verify_rebuild(args):
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [sys.executable, '-X', 'utf8', str(HERE / 'build.py'), '--jurisdiction', args.jurisdiction,
               '--offline', '--repo', tmp, '--today', args.today]
        if args.acts_file:
            cmd += ['--acts-file', args.acts_file]
        if args.only:
            cmd += ['--only', args.only]
        if args.provisions:
            cmd += ['--provisions', args.provisions]
        out = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        if out.returncode:
            raise SystemExit(out.stderr)

        def refs(r):
            return dict(l.split(' ', 1)[::-1] for l in git(Path(r), 'show-ref').split('\n') if l)
        a, b = refs(args.repo), refs(tmp)
        main_a = git(Path(args.repo), 'log', '--format=%H', 'main').split()
        main_b = git(Path(tmp), 'log', '--format=%H', 'main').split()
        rec = {'identical': a == b, 'refs': len(a), 'main': a.get('refs/heads/main'),
               'rebuilt_main': b.get('refs/heads/main'), 'commits_main': len(main_a),
               'history_tip': main_a[1] if len(main_a) > 1 else None,
               'history_identical': main_a[1:] == main_b[1:], 'future': a.get('refs/heads/future')}
        print(json.dumps(rec, indent=1))
        raise SystemExit(0 if rec['identical'] else 1)


if __name__ == '__main__':
    main()
