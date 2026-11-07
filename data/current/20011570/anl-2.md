## Anlage 2

## zu § 8 und § 9

## Daten für die Feststellung der Erfüllung der allgemeinen Schulpflicht

Definition der Schnittstelle zwischen den Evidenzen der Schulen bzw. der Bildungsdirektionen gemäß § 5 BilDokG 2020 und der BRZ GmbH:

Als Schnittstelle für die Datenübermittlung fungiert eine CSV-Datei oder eine XLSX-Datei im Zeichensatzformat UTF-8. Für Schulen besteht außerdem die Möglichkeit via Webservice die Datenübermittlung vorzunehmen.

Die technische Spezifikation wird durch die BRZ GmbH vorgegeben.

| Feldname | Format | Pflichtfeld (Ja/Nein) | Anmerkung |
| --- | --- | --- | --- |
| meldedatum | JJJJ-MM-TT | Ja | Datum der Erstellung der Meldung (CSV-Datei) |
| absender | 6-stellige Schul- bzw. Clusterkennzahl oder Behördenkennzahl | Ja | Schulkennzahl, Clusterkennzahl oder Behördenkennzahl der oder des Absenders |
| schuljahr | JJJJ/JJ | Ja | Angabe des Schuljahres, zu dem diese Meldung erfolgt zB 2021/22 |
| skz | 6-stellige Schulkennzahl | Ja | Schulkennzahl der Schule, für die diese Meldung erfolgt |
| paragraph | String (max. 20 Zeichen) Erlaubte Werte: § 2 Abs. 2 § 11 § 12 § 13 § 15 | Ja | Angabe des angewendeten Paragraphen zur allgemeinen Schulpflicht des Schulpflichtgesetzes 1985, entfällt bei der Meldung der Schulen bzw. der Schulcluster |
| vbPKBF | String | ab Schuljahr 2023/24 verpflichtend | Verschlüsseltes bPK-BF (bereichsspezifisches Personenkennzeichen Bildung und Forschung) |
| zuname | String (max. 50 Zeichen) | Ja | der oder die Familienname(n) der Schülerin oder des Schülers |
| vorname | String (max. 100 Zeichen) | Ja | der oder die Vorname(n) der Schülerin oder des Schülers |
| gebdat | JJJJ-MM-TT | Ja | Geburtsdatum der Schülerin oder des Schülers |
| geschlecht | „m“ für männlich, „w“ für weiblich, „x“ für divers, „o“ für offen „i“ für inter „k“ für den Fall, dass von jeglicher Geschlechtsangabe abgesehen wurde | Ja | Geschlecht der Schülerin oder des Schülers |
| plz | 4-stellige österreichische PLZ | Ja, nur wenn Feld z-plz leer | Postleitzahl des Wohnsitzes der Schülerin oder des Schülers |
| ort | String (max. 50 Zeichen) | Ja, nur wenn Feld z-ort leer | Bezeichnung des Ortes des Wohnsitzes der Schülerin oder des Schülers |
| strasse | String (max. 130 Zeichen) | Ja, nur wenn Feld z-strasse leer | Adresse des Wohnsitzes der Schülerin oder des Schülers, inkl. Hausnummer, Stiege und Tür |
| z-plz | 4-stellige österreichische PLZ | Nein | Postleitzahl eines allfälligen zusätzlichen Wohnsitzes der Schülerin oder des Schülers am Bildungsort |
| z-ort | String (max. 50 Zeichen) | Nein | Bezeichnung des Ortes eines allfälligen zusätzlichen Wohnsitzes der Schülerin oder des Schülers am Bildungsort |
| z-strasse | String (max. 130 Zeichen) | Nein | Adresse eines allfälligen zusätzlichen Wohnsitzes der Schülerin oder des Schülers am Bildungsort, inklusive Hausnummer, Stiege und Tür |
| eingeschult | JJJJ | Ja | Erstes Jahr der allgemeinen Schulpflicht: Angabe des Kalenderjahres, in dem die Schülerin oder der Schüler in die erste Schulstufe bzw. als Schulpflichtige oder Schulpflichtiger in die Vorschulstufe eintrat (gegebenenfalls gemäß Rückrechnung nach dem Schulpflichtgesetz 1985, zB bei Zuzug aus dem Ausland) (Ausnahmen sind möglich; vorzeitige Einschulung, Frühchen), entfällt bei der Meldung der Bildungsdirektorin oder des Bildungsdirektors |
| beginn | JJJJ-MM-TT | Nein | Datum des Beginns der laufenden Ausbildung zB 2021-09-01, ), entfällt bei der Meldung der Bildungsdirektorin oder des Bildungsdirektors |
| bemerkung | String (max. 500 Zeichen) | Nein | Bemerkungsfeld, entfällt bei der Meldung der Schulen bzw. der Schulcluster |
