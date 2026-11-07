## Anlage 3

## Einmeldung Steuerdaten

## 1\. Dateiname

\_\_ .csv

Beispiel: xxxx\_2011-09-12\_001.csv ODER xxxx\_2011-09-12\_104600000.csv

Der Dateiname muss eindeutig sein.

## 2\. Fileformat

Comma Separated File, Trennzeichen ';'

Zahlenformat: Punkt oder Komma als Dezimaltrennzeichen, KEINE Tausendertrennzeichen

Beispiel: 123456.1234 ODER 123456,1234

Anzahl der Nachkommastellen: 4

Bei weniger als 4 gemeldeten Nachkommastellen werden die nicht gemeldeten Nachkommastellen mit 0 aufgefüllt; Daten mit mehr als 4 Nachkommastellen werden als Fehler zurückgewiesen.

## 3\. Ablauf der Steuerdatenmeldung bis zur Veröffentlichung

Die Steuerdatenmeldung an die Meldestelle erfolgt via MFT im definierten Fileformat. In einem Meldefile können mehrere Steuerdatenmeldungen enthalten sein.

Die Steuerdatenmeldung mit dem Status ‚NEW‘ oder ‚UPDATE‘ an die Meldestelle hat bis spätestens 15 Uhr zu erfolgen und muss immer die gesamten Meldedaten je Stichtag und ISIN umfassen; die korrespondierende Meldung mit dem Status ‚CONFIRMED‘ hat bis 15:25 Uhr zu erfolgen.

Die Steuerdatenmeldung wird bei der Meldestelle dahingehend geprüft, ob alle erforderlichen Felder gemäß dieser Verordnung befüllt sind, und verarbeitet. Treten bei der Prüfung Fehler auf, schickt die Meldestelle eine Fehlermeldung (Status ‚ERROR‘) an den Steuerlichen Vertreter zurück und die Steuerdatenmeldung muss zur Gänze neu übermittelt werden.

Ist die Steuerdatenmeldung formal in Ordnung, errechnet die Meldestelle die daraus abgeleiteten Daten und retourniert diese zur Bestätigung an den Steuerlichen Vertreter. Der Status dieser Meldung ist ‚OPEN‘.

Die Bestätigung der Steuerdatenmeldung und Freigabe zur Veröffentlichung durch den Steuerlichen Vertreter erfolgt durch Rückmeldung mit dem Status ‚CONFIRMED‘.

Nach Einlangen der Steuerdatenmeldung mit dem Status ‚CONFIRMED‘ bei der Meldestelle retourniert die Meldestelle die Steuerdatenmeldung mit dem Status ‚FINAL‘ als Bestätigung, die Freigabe der zu veröffentlichenden Steuerdatenmeldung des Steuerlichen Vertreters erhalten zu haben. Damit gilt die Meldung als eingebracht.

Datenmeldungen mit dem Status ‚OPEN‘ können, so der Steuerliche Vertreter einen Fehler erkennt, noch gelöscht werden. Dazu ist die Steuerdatenmeldung mit dem Status ‚DELETE‘ an die Meldestelle zu übermitteln. Die ursprüngliche Steuerdatenmeldung wird von der Meldestelle mit dem Status ‚DELETED‘ versehen und dem Steuerlichen Vertreter zurück bestätigt. Es erfolgt keine Veröffentlichung der Meldung.

Eine bereits veröffentlichte Steuerdatenmeldung kann nicht mehr gelöscht werden. Es besteht jedoch gemäß § 4 Abs. 1 die Möglichkeit, eine Korrektur der Steuerdatenmeldung zu übermitteln. Der Status für eine korrigierte Steuerdatenmeldung lautet ‚UPDATE‘.

## 4\. Fileaufbau

| Reihenfolge | Datensatz Typ | Code für Datensatz | Anzahl |
| --- | --- | --- | --- |
| 1 | Start | “START” | 1 (Pflichtfeld) |
| 2 | Status | “STATUS” | 1 (Pflichtfeld) |
| 3 | Ergänzende Angaben | „EA“ | 0..1 (optional) (Pflichtfeld, wenn Ausschüttungs-meldung) |
| 4 | Erträge (nicht länderspezifische Daten) | “E” | 0..n (optional) |
| 5 | Dividenden | “D” | 0..n (optional) |
| 6 | Zinsen | “Z” | 0..n (optional) |
| 7 | Zinsen Altemissionen | “ZA” | 0..n (optional) |
| 8 | Ausschüttungen ausländischer Subfonds | “AS” | 0..n (optional) |
| 9 | Steuerliche Behandlung | “STB” | 0..n (optional) nur von Meldestelle |
| 10 | Ende Datensatz | “END” | 1 (Pflichtfeld) |

Der gesamte Block kann sich innerhalb eines Files für mehrere ISINs wiederholen.

## Beschreibung Datensatz Start

| Spalte | Datenfeld | Format\* | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | “START” | Pflichtfeld |
| 2 | ISIN | X(12) | Pflichtfeld |
| 3 | Art | X(8) InvF – Investmentfonds gemäß InvFG, der nach dem InvFG aufgelegt ist oder vertrieben wird oder zu vertreiben wäre ImmoInvF – Immobilienfonds gemäß ImmoInvFG, der nach dem ImmoInvFG aufgelegt ist oder vertrieben wird oder zu vertreiben wäre AIF – Alternativer Investment Fund gemäß AIFMG, der nicht nach dem InvFG aufgelegt ist oder vertrieben wird oder zu vertreiben wäre ImmoAIF – AIF in Immobilien gemäß AIFMG, der nicht nach dem ImmoInvFG aufgelegt ist oder vertrieben wird oder zu vertreiben wäre | Pflichtfeld |
| 4 | Ertragstyp | X(1) A – Ausschütter T – Thesaurierer V – Vollthesaurierer | Pflichtfeld |
| 5 | Fondswährung Währungscode (ISO-4217) | X(3) | Pflichtfeld |
| 6 | Geschäftsjahr-Beginn | X(10) YYYYMMDD oder YYYY.MM.DD | Pflichtfeld |
| 7 | Geschäftsjahr-Ende | X(10) YYYYMMDD oder YYYY.MM.DD | Pflichtfeld |
| 8 | Meldung Jahresdaten | X(4) JA (Default) / NEIN |  |
| 9 | Meldezeitraum Beginn | X(10) YYYYMMDD oder YYYY.MM.DD | Pflichtfeld, wenn Zwischenausschüttung |
| 10 | Meldezeitraum Ende | X(10) YYYYMMDD oder YYYY.MM.DD | Pflichtfeld, wenn Zwischenausschüttung |
| 11 | Anzahl Anteile zum Ende des Meldezeitraums | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 12 | Meldedatum | X(10) YYYYMMDD oder YYYY.MM.DD | Optional (nur von Meldestelle) |
| 13 | Sitzland Fonds | X(2) ISO Ländercode | Pflichtfeld |
| 14 | Selbstnachweis \*\* | X(4) JA / NEIN (Default) | Optional |
| 15 | Öffentliches Angebot | X(4) JA (Default) / NEIN | Pflichtfeld |
| 16 | Mehr als 50 Anteilsinhaber | X(4) JA / NEIN (Default) | Pflichtfeld |
| 17 | Name der Anteilsgattung des Fonds | X(45) | Optional |
| 18 | Fonds unterliegt der KESt auf Zinsen gem. § 98 EStG 1988 | X(4) JA / NEIN | Pflichtfeld |
| 19 | Quellensteuer wurde ausschließlich als Aufwand abgezogen – eine Anrechnung ist nicht zulässig. | X(4) Ja / Nein | Pflichtfeld |
| 20 | Anzahl Anteile zum Zuflusszeitpunkt (§ 186 Abs. 2 Z 1 lit. b InvFG 2011 od. § 40 Abs. 1 Z 2 ImmoInvFG); es ist zulässig die Anzahl der Anteile zu einem Zeitpunkt, der bis zu 10 Bankarbeitstage vor dem Zuflusszeitpunkt liegt, anzugeben. | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 21 | LEI (Legal Entity Identifier) des Fonds | X(20) | Optional |

\*\*) Formatbeschreibung:

- a) Format X(y) – alphanumerisches Feld mit y Stellen.

- b) X(10) YYYYMMDD oder YYYY.MM.DD – Datumsformat.

- c) Defaultwert – falls das Feld nicht befüllt wird, gilt der als Defaultwert bezeichnete Wert als gemeldet.

\*\*) Bei der Übermittlung der Steuerdatenmeldung (Status ‚NEW‘ oder ‚UPDATE‘ oder ‚CONFIRMED‘) kann der steuerliche Vertreter den Parameter Selbstnachweis ‚JA‘ angeben. Damit wird die Steuerdatenmeldung, so sie nach Ende der Melde- bzw. bei bereits erfolgter regulärer Meldung nach Ende der Korrekturfrist den Status ‚FINAL‘ erhält, als Selbstnachweis veröffentlicht.

Erhält die Steuerdatenmeldung vor dem Ende der Lieferfrist den Status ‚FINAL‘, so wird sie nicht als Selbstnachweis verarbeitet und regulär veröffentlicht.

## Beschreibung Datensatz Status

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | “STATUS” | Pflichtfeld |
| 2 | Status | X(30) – Status siehe Status-Tabelle | Pflichtfeld |
| 3 | ID | Numerisch, ganzzahlig Eindeutige ID (wird von Meldestelle bei Berechnung vergeben) | Optional bei ‚NEW‘ und bei ‚ERROR‘ nicht befüllt, sonst Pflichtfeld |
| 4 | ID – ursprünglich | Numerisch, ganzzahlig Ursprüngliche ID (Verweis der Meldestelle im Falle einer UPDATE-Meldung) | Optional Befüllung nur durch Meldestelle |
| 5 | Anmerkung | X(255) | Optional |

## Status-Tabelle

| Status | Beschreibung | Quelle |
| --- | --- | --- |
| NEW | Neue Meldung (Einmeldung) | Lieferant |
| ERROR | Fehlerhafte Meldung (mit Error.log an Lieferanten) -\> Neumeldung erforderlich | Meldestelle |
| NEW\_DECLINED | Ablehnung einer Meldung, die nicht als Selbstnachweis gekennzeichnet ist und die nach Ablauf der maximalen Meldefrist einlangt | Meldestelle |
| UPDATE | Änderung einer vorherigen Meldung | Lieferant |
| UPDATE\_ DECLINED | Ablehnung einer Korrektur-Meldung, die nicht als Selbstnachweis gekennzeichnet ist und die nach Ablauf der maximalen Meldefrist einlangt | Meldestelle |
| OPEN | Rückmeldung der Meldestelle auf eingelangte Daten samt Ergebnis der Berechnung – muss mit dem Status 'CONFIRMED' an die Meldestelle bestätigt werden | Meldestelle |
| CONFIRMED | Bestätigung der Meldung mit dem vorherigen Status 'OPEN' | Lieferant |
| CONFIRM\_ DECLINED | Ablehnung einer Bestätigungs-Meldung, die nicht als Selbstnachweis gekennzeichnet ist und die nach Ablauf der maximalen Meldefrist einlangt | Meldestelle |
| FINAL | Die Bestätigung der Meldung wurde verarbeitet, die Daten werden veröffentlicht | Meldestelle |
| DELETE | Löschen einer vorherigen Meldung (nur möglich vor Status 'CONFIRMED') | Lieferant |
| DELETED | Diese Meldung wurde gelöscht | Meldestelle |
| DELETE\_ DECLINED | Löschung wurde abgelehnt, da die Meldefrist bereits verstrichen ist oder die Meldung bereits mit Status 'CONFIRMED' bestätigt wurde | Meldestelle |

## Beschreibung Datensatz Ergänzende Angaben

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | „EA“ | Pflichtfeld |
| 2 | Ausschüttungstag | X(10) YYYYMMDD oder YYYY.MM.DD | Optional Pflichtfeld, wenn Ausschüttung |
| 3 | Ex-Tag | X(10) YYYYMMDD oder YYYY.MM.DD | Optional |
| 4 | Record Date | X(10) YYYYMMDD oder YYYY.MM.DD | Optional |
| 5 | Kapitalrückzahlung | X(3) N – Nein KR – Kapitalrückzahlung ohne Ausbuchung KRA – Kapitalrückzahlung mit Ausbuchung | Optional |
| 6 | Wiederanlagerabatt | Numerisch, 4 Nachkommastellen | Optional |
| 7 | Wiederanlagerabatt Art | X(1) P – Prozent S – Stück | Optional |
| 8 | Wiederanlagerabatt Zeitraum bis | X(10) YYYYMMDD oder YYYY.MM.DD | Optional |
| 9 | Kuponnummer | Numerisch, ganzzahlig | Optional |
| 10 | Verwaltungsgesellschaft | X(60) | nur von Meldestelle zu befüllen |
| 11 | Steuerlicher Vertreter | X(75) | nur von Meldestelle zu befüllen |

## Beschreibung Datensatz Ertrag

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | “E” – Ertrag | Pflichtfeld |
| 2 | Code oder Referenz des Feldes laut Code-Verzeichnis | X(150) | Pflichtfeld |
| 3 | Wert des Feldes | Numerisch, 4 Nachkommastellen | Pflichtfeld |

## Beschreibung Datensatz Dividende

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | “D” – Dividende | Pflichtfeld |
| 2 | Code oder Referenz des Feldes laut Code-Verzeichnis | X(150) | Pflichtfeld |
| 3 | Wert des Feldes | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 4 | Code für Land / Besonderheit laut Codeverzeichnis | X(5) | Pflichtfeld |

## Beschreibung Datensatz Zinsen

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | “Z” – Zinsen | Pflichtfeld |
| 2 | Code oder Referenz des Feldes laut Code-Verzeichnis | X(150) | Pflichtfeld |
| 3 | Wert des Feldes | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 4 | Code für Land / Besonderheit laut Codeverzeichnis | X(5) | Pflichtfeld |

## Beschreibung Datensatz Zinsen Altemissionen

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | “ZA” – Zinsen Alt-emissionen | Pflichtfeld |
| 2 | Code oder Referenz des Feldes laut Code-Verzeichnis | X(150) | Pflichtfeld |
| 3 | Wert des Feldes | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 4 | Code für Land / Besonderheit laut Codeverzeichnis | X(5) | Pflichtfeld |

## Beschreibung Datensatz Ausschüttung ausländischer Subfonds

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz | “AS” – Ausschüttungen ausländischer Subfonds | Pflichtfeld |
| 2 | Code oder Referenz des Feldes laut Code-Verzeichnis | X(150) | Pflichtfeld |
| 3 | Wert des Feldes | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 4 | Code für Land / Besonderheit laut Codeverzeichnis | X(5) | Pflichtfeld |

## Beschreibung Datensatz Steuerliche Behandlung

## (wird nur bei Rückmeldungen mit Status 'OPEN' verwendet)

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Code für Datensatz (zur Identifizierung des Feldes) | “STB” – Steuerliche Behandlung | Pflichtfeld |
| 2 | Code oder Referenz des Feldes laut Code-Verzeichnis | X(150) | Pflichtfeld |
| 3 | Betrag für Privatanleger mit Option | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 4 | Betrag für Privatanleger ohne Option | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 5 | Betrag für Betriebsvermögen mit Option | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 6 | Betrag für Betriebsvermögen ohne Option | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 7 | Betrag für Betriebsvermögen einer juristischen Person | Numerisch, 4 Nachkommastellen | Pflichtfeld |
| 8 | Betrag für Stiftung | Numerisch, 4 Nachkommastellen | Pflichtfeld |

## Beschreibung Datensatz Ende

| Spalte | Datenfeld | Format | Beschreibung |
| --- | --- | --- | --- |
| 1 | Datensatz Code | “END” Ende Datensatz | Pflichtfeld |
| 2 | ISIN | X(12) | Pflichtfeld |
| 3 | Timestamp | X(19) YYYY.MM.DD HH:MM:SS / YYYYMMDD HH:MM:SS | Optional |
