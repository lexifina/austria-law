## Anlage 2

## Aufbau der Jahresmeldung

## 1\. Satzarten im Überblick

| Satzart X01 | Basisdaten zum stationären Aufenthalt/ambulanten Besuch |
| --- | --- |
| Satzart X02 | Daten nach Hauptkostenstellen/Fachgebieten |
| Satzart X03 | Diagnosen |
| Satzart X04 | Medizinische Leistungen |
| Satzart X05 | Scoringdaten |
| Satzart X06 | Akzeptierte Errors/Warnings |
| Satzart X07 | Kommentare |

| Satzart I11 | SAPS3-Daten |
| --- | --- |
| Satzart I12 | TISS-A-Daten |

| Satzart L01 | Spezielle Leistungsbereiche |
| --- | --- |
| Satzart L02 | Abrechnungsrelevante Kostenträger |
| Satzart L03 | Exklusionen medizinischer Leistungen |
| Satzart L04 | Exklusionen tagesklinischer medizinischer Leistungen |

| Satzart E01 | Stammdaten extramuraler Leistungserbringer/Leistungserbringerinnen |
| --- | --- |

| Satzart P01 | Pseudonyme Patienten/Patientinnen |
| --- | --- |

| Satzart K01 | Kostenstellenplan |
| --- | --- |
| Satzart K02 | KA-Stammdaten |
| Satzart K03 | KA-Statistik (Ressourcen und Inanspruchnahme) |
| Satzart K04 | KA-Statistik (Personal-Vollzeitäquivalente nach Funktionsgruppen und Dienstverhältnis) |
| Satzart K05 | KA-Statistik (Personal des ärztlichen Dienstes) |
| Satzart K06 | KA-Statistik (Konsiliarärztlicher Dienst) |
| Satzart K07 | KA-Statistik (Personal der nicht-ärztlichen Gesundheitsberufe) |
| Satzart K08 | Kostenstellen-Statistik und Kostennachweis (Bettenführende Hauptkostenstelle) |
| Satzart K09 | Kostenstellen-Statistik und Kostennachweis (Nicht-bettenführende Hauptkostenstelle) |
| Satzart K10 | Kostenstellen-Statistik und Kostennachweis (Neben- und Hilfskostenstellen) |
| Satzart K11 | Sammel-Kostennachweis Summenblatt |
| Satzart K12 | Sammel-Kostennachweis Detailblätter |
| Satzart K13 | Kalkulatorischer Anhang – Kostenminderungen |
| Satzart K14 | Kalkulatorischer Anhang – Kalkulatorischer Anlagenspiegel |
| Satzart K15 | Kalkulatorischer Anhang – Allgemeine Kostenbereiche |
| Satzart K16 | Kalkulatorischer Anhang – Ausgewählte Kosten |

| Satzart G01 | Großgerätebasisdaten |
| --- | --- |
| Satzart G02 | Großgeräteleistungsdaten |

| Satzart B01 | Basisinformationen |
| --- | --- |
| Satzart B02 | Vermögens- und Kapitalstruktur (VKS) |
| Satzart B03 | Eigenmittelverteilungsrechnung (EVR) |
| Satzart B04 | Quellen- und Verwendungsanalyse (QVA) |
| Satzart B05 | Erlösstruktur (ES) |
| Satzart B06 | Zuschussstruktur (ZS) |

| Satzart A01 | Antiinfektiva-Abrufe |
| --- | --- |
| Satzart S11 | Prüf- und Summensatz |

Die einzelnen Satzarten enthalten die folgenden Datenfelder. Schlüsselfelder, also Datenfelder, die in ihrer Kombination einen Datensatz eindeutig identifizieren, sind dabei grau hinterlegt dargestellt. Alle Satzarten bzw. Datenfelder sind verpflichtend zu befüllen, sofern über Fußnoten keine anderen Festlegungen getroffen werden.

## 2\. Satzarten im Detail

## Satzart X01 – Basisdaten zum stationären Aufenthalt/ambulanten Besuch

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer/Leistungserbringer-Stammdaten-ID | 20 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 1\) |
| Datensatz-ID | 64 | alphanumerisch | 1\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Aufnahme-/Kontaktuhrzeit | 4 | alphanumerisch | 2\) |
| Behandlungsart | 1 | alphanumerisch |  |
| Geburtsdatum | 8 | alphanumerisch | 1\) |
| Altersgruppe bei Entlassung/Kontakt | 2 | numerisch |  |
| Geschlecht | 1 | alphanumerisch |  |
| Staatsbürgerschaft | 2 | alphanumerisch |  |
| Wohnsitz – Staat | 2 | alphanumerisch |  |
| Wohnsitz – Postleitzahl | 4 | numerisch | 3\) |
| Wohnsitz – Gemeindecode | 5 | numerisch | 3\) |
| Aufnahme-/Zugangsart 1 | 1 | alphanumerisch | 4\) |
| Aufnahme-/Zugangsart 2 | 1 | alphanumerisch | 4\) |
| Transportart | 1 | alphanumerisch | 5\) |
| Zugewiesen von – Krankenanstaltennummer | 6 | alphanumerisch | 6\) |
| Zugewiesen an – Krankenanstaltennummer | 6 | alphanumerisch | 6\) |
| Entlassungs-/Abgangsart | 1 | alphanumerisch | 7\) |
| Entlassungsdatum | 8 | alphanumerisch | 8\) |
| Entlassungsuhrzeit | 4 | alphanumerisch | 8\) |
| Leistungszuständiger Kostenträger – Code | 2 | alphanumerisch | 9\) |
| Fondsrelevanz | 1 | alphanumerisch | 10\) |
| Plausibilitätskennzeichen | 1 | numerisch |  |
| Abrechnender Kostenträger – Code | 2 | alphanumerisch | 11\) |
| Abrechnungsquartal der Sozialversicherung | 5 | alphanumerisch | 11\) |

| 1\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium, zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen dem Dachverband und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
| --- | --- |
|  | Die Datenfelder „Aufnahmezahl“ und „Geburtsdatum“ sind ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ bzw. „Geburtsdatum“ nie gleichzeitig befüllt sein. |
| 2\) | Für den extramuralen ambulanten Bereich ist dieses Datenfeld ab dem Zeitpunkt verpflichtend zu befüllen, ab dem den Sozialversicherungsträgern entsprechende Informationen vorliegen. |
| 3\) | Diese Datenfelder sind bei Patienten/Patientinnen mit österreichischem Wohnsitz verpflichtend zu befüllen. Bei Patienten/Patientinnen mit ausländischem Wohnsitz sind diese Datenfelder nicht zu befüllen. |
| 4\) | Für den spitalsambulanten und extramuralen ambulanten Bereich sind diese Datenfelder zu befüllen, sofern diese Informationen systematisch erfasst werden. |
| 5\) | Dieses Datenfeld ist verpflichtend zu befüllen, sofern diese Informationen systematisch erfasst werden. |
| 6\) | Für den stationären Bereich sind diese Datenfelder bei transferierten Patienten/Patientinnen zu befüllen. Für den spitalsambulanten und extramuralen ambulanten Bereich sind diese Datenfelder nicht zu befüllen. |
| 7\) | Für den stationären Bereich ist dieses Datenfeld für am Jahresende verbleibende Patienten/Patientinnen mit dem Kennzeichen „V“ zu befüllen. Für den spitalsambulanten und extramuralen ambulanten Bereich sind diese Datenfelder zu befüllen, sofern diese Informationen systematisch erfasst werden. |
| 8\) | Für den stationären Bereich sind diese Datenfelder zu befüllen, sofern es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. Für den spitalsambulanten und extramuralen ambulanten Bereich sind diese Datenfelder nicht zu befüllen. |
| 9\) | Dieses Datenfeld ist nicht zu befüllen, sofern es sich um am Jahresende verbleibende Patienten/Patientinnen im stationären Bereich handelt. |
| 10\) | Für den extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |
| 11\) | Diese Datenfelder sind ausschließlich in den Datenübermittlungen zwischen dem Dachverband und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |

## Satzart X02 – Daten nach Hauptkostenstellen/Fachgebieten

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer/Leistungserbringer-Stammdaten-ID | 20 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 1\) |
| Datensatz-ID | 64 | alphanumerisch | 1\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Hauptkostenstelle/Fachgebiet – Positionsnummer | 3 | alphanumerisch |  |
| Hauptkostenstelle – Funktionscode/Fachgebiet | 8 | numerisch |  |
| Hauptkostenstelle/Fachgebiet – Zugangsdatum/Kontaktdatum | 8 | alphanumerisch |  |
| Hauptkostenstelle/Fachgebiet – Zugangsuhrzeit/Kontaktuhrzeit | 4 | alphanumerisch | 2\) |
| Physische Anwesenheit | 1 | alphanumerisch | 3\) |
| Hauptkostenstelle – Abgangsdatum | 8 | alphanumerisch | 4\) |
| Hauptkostenstelle – Abgangsuhrzeit | 4 | alphanumerisch | 4\) |
| Hauptkostenstelle – Abgangsart | 1 | numerisch | 4\) |
| Hauptkostenstelle – Fachlicher Funktionscode | 8 | numerisch | 5\) |
| Hauptkostenstelle – Pflegerischer Funktionscode | 8 | numerisch | 5\) |
| Neugeborenes | 1 | alphanumerisch | 6\) |
| Altersgruppe bei Zugang/Kontakt | 2 | numerisch |  |
| Aufnahmezahl – funktionscodebezogen | 12 | alphanumerisch | 7\) |

| 1\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium, zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen dem Dachverband und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
| --- | --- |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |
| 2\) | Für den stationären Bereich sind diese Datenfelder nur für Intensiveinheiten auszufüllen, für die eine Intensivdokumentation (TISS-A/ SAPS3) übermittelt wird. Bei Datensätzen für am Jahresende verbleibende Patienten/Patientinnen sind diese Datenfelder nicht zu befüllen. |
|  | Für den extramuralen ambulanten Bereich ist dieses Datenfeld ab dem Zeitpunkt verpflichtend zu befüllen, ab dem den Sozialversicherungsträgern entsprechende Informationen vorliegen. |
| 3\) | Für den stationären Bereich ist dieses Datenfeld nicht zu befüllen. |
| 4\) | Für den stationären Bereich sind diese Datenfelder nur für Intensiveinheiten auszufüllen, für die eine Intensivdokumentation (TISS-A/ SAPS3) übermittelt wird. Bei Datensätzen für am Jahresende verbleibende Patienten/Patientinnen sind diese Datenfelder nicht zu befüllen. |
|  | Für den spitalsambulanten und extramuralen ambulanten Bereich sind diese Datenfelder nicht zu befüllen. |
| 5\) | Für den stationären Bereich sind diese Datenfelder zu befüllen, sofern dies auf Ebene der Landesgesundheitsfonds festgelegt wird. |
|  | Für den spitalsambulanten und extramuralen ambulanten Bereich sind diese Datenfelder nicht zu befüllen. |
| 6\) | Für den spitalsambulanten und extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |
| 7\) | Für den spitalsambulanten Bereich ist dieses Datenfeld ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds zu befüllen. |
|  | Für den stationären und extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |

## Satzart X03 – Diagnosen 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer/Leistungserbringer-Stammdaten-ID | 20 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 2\) |
| Datensatz-ID | 64 | alphanumerisch | 2\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Diagnose – Code | 7 | alphanumerisch |  |
| Diagnose – Typ | 1 | alphanumerisch |  |
| Diagnose – Art | 1 | alphanumerisch | 3\) |
| Diagnose – im stationären Aufenthalt erworben | 1 | alphanumerisch | 4\) |
| Aufnahmezahl – funktionscodebezogen | 12 | alphanumerisch | 5\) |

| 1\) | Für den stationären Bereich ist diese Satzart nur zu melden, wenn es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. |
| --- | --- |
| 2\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium, zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen dem Dachverband und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |
| 3\) | Für den spitalsambulanten und extramuralen ambulanten Bereich ist dieses Datenfeld zu befüllen, sofern dies im Rahmen der jährlich zu wartenden Abrechnungsmodelle oder von Modellprojekten der Bundesgesundheitsagentur vorgesehen ist. |
|  | Für den stationären Bereich ist dieses Datenfeld nicht zu befüllen. |
| 4\) | Für den stationären Bereich ist dieses Datenfeld für im Rahmen der jährlichen Wartung ausgewählte Diagnosen zu befüllen. |
|  | Für den spitalsambulanten und extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |
| 5\) | Für den spitalsambulanten Bereich ist dieses Datenfeld ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds zu befüllen. |
|  | Für den stationären und extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |

## Satzart X04 – Medizinische Leistungen 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer/Leistungserbringer-Stammdaten-ID | 20 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 2\) |
| Datensatz-ID | 64 | alphanumerisch | 2\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Medizinische Leistung – Code | 10 | alphanumerisch |  |
| Medizinische Leistung – Seitenlokalisation | 1 | alphanumerisch | 3\) |
| Medizinische Leistung – Abrechnungsrelevanz | 1 | alphanumerisch | 3\) |
| Medizinische Leistung – Anzahl | 7 | numerisch | 4\) |
| Medizinische Leistung – Datum der Erbringung | 8 | alphanumerisch |  |
| Medizinische Leistung – Uhrzeit der Erbringung | 4 | alphanumerisch | 5\) |
| Funktionscode/Fachgebiet leistungserbringend | 8 | numerisch | 6\) |
| Krankenanstaltennummer leistungserbringend | 6 | alphanumerisch | 6\) |
| Aufnahmezahl – funktionscodebezogen | 12 | alphanumerisch | 7\) |

| 1\) | Für den stationären Bereich ist diese Satzart nur zu melden, wenn es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. |
| --- | --- |
| 2\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium, zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen dem Dachverband und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |
| 3\) | Für den extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |
| 4\) | Für den spitalsambulanten und stationären Bereich sind hier ausschließlich ganze Zahlen im Zahlenformat 9999 anzugeben. |
|  | Für den extramuralen ambulanten Bereich ist das Zahlenformat 9999,99 zu verwenden. |
| 5\) | Für den stationären, spitalsambulanten und extramuralen ambulanten Bereich ist dieses Datenfeld verpflichtend zu befüllen, sofern diese Informationen systematisch erfasst werden. |
| 6\) | Für den extramuralen ambulanten Bereich ist das Datenfeld „Krankenanstaltennummer leistungserbringend“ nicht zu befüllen. |
|  | Bei extern erbrachten Leistungen im stationären und spitalsambulanten Bereich ist das Datenfeld „Krankenanstaltennummer leistungserbringend“ anstelle des Felds „Funktionscode/Fachgebiet leistungserbringend“ zu befüllen. |
| 7\) | Für den spitalsambulanten Bereich ist dieses Datenfeld ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds zu befüllen. |
|  | Für den stationären und extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |

## Satzart X05 – Scoringdaten 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 2\) |
| Datensatz-ID | 64 | alphanumerisch | 2\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Abrechnung – Gruppe | 8 | alphanumerisch |  |
| Abrechnung – Knoten | 3 | alphanumerisch |  |
| Leistungskomponente/Leistungspunkte | 8 | numerisch |  |
| Tageskomponente/Kontaktpunkte | 8 | numerisch |  |
| Punkte Belagsdauerausreißer nach unten – Leistungskomponente | 8 | numerisch | 3\) |
| Punkte Belagsdauerausreißer nach unten – Tageskomponente | 8 | numerisch | 3\) |
| Zusatzpunkte Belagsdauerausreißer nach oben | 8 | numerisch | 3\) |
| Zusatzpunkte Intensiv | 8 | numerisch | 3\) |
| Zusatzpunkte Mehrfachleistungen | 8 | numerisch |  |
| Punkte spezieller Bereiche (tageweise) | 8 | numerisch | 3\) |
| Punkte total | 8 | numerisch |  |

| 1\) | Für den stationären Bereich ist diese Satzart nur zu melden, wenn es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. |
| --- | --- |
|  | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| 2\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |
| 3\) | Für den spitalsambulanten Bereich sind diese Datenfelder nicht zu befüllen. |

## Satzart X06 – Akzeptierte Errors/Warnings 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 2\) |
| Datensatz-ID | 64 | alphanumerisch | 2\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Error/Warning – Wert | 20 | alphanumerisch |  |
| Error/Warning – Code | 4 | alphanumerisch |  |
| Error/Warning – Kommentar | 200 | alphanumerisch |  |

| 1\) | Für den stationären Bereich ist diese Satzart nur zu melden, wenn es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. |
| --- | --- |
|  | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| 2\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |

## Satzart X07 – Kommentare 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 2\) |
| Datensatz-ID | 64 | alphanumerisch | 2\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Kommentar 1 | 200 | alphanumerisch |  |
| Kommentar 2 | 200 | alphanumerisch |  |
| Kommentar 3 | 200 | alphanumerisch |  |
| Kommentar 4 | 200 | alphanumerisch |  |
| Kommentar 5 | 200 | alphanumerisch |  |
| Kommentar 6 | 200 | alphanumerisch |  |

| 1\) | Für den stationären Bereich ist diese Satzart nur zu melden, wenn es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. |
| --- | --- |
|  | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| 2\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |

## Satzart I11 – SAPS3-Daten 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 2\) |
| Datensatz-ID | 64 | alphanumerisch | 2\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Bettenführende Hauptkostenstelle – Positionsnummer | 3 | alphanumerisch |  |
| Erhebungsdatum | 8 | alphanumerisch |  |
| Akute Infektion bei Aufnahme | 2 | numerisch |  |
| Aufnahmegrund: Anderer, nicht klassifiziert | 1 | numerisch |  |
| Aufnahmegrund: Basispflege und Observanz | 1 | numerisch |  |
| Aufnahmegrund: Gastrointestinal | 1 | numerisch |  |
| Aufnahmegrund: Hämatologisch | 1 | numerisch |  |
| Aufnahmegrund: Kardiovaskulär | 2 | numerisch |  |
| Aufnahmegrund: Leber | 1 | numerisch |  |
| Aufnahmegrund: Metabolisch | 1 | numerisch |  |
| Aufnahmegrund: Neurologisch | 1 | numerisch |  |
| Aufnahmegrund: Renal | 1 | numerisch |  |
| Aufnahmegrund: Respiratorisch | 1 | numerisch |  |
| Aufnahmegrund: Schweres Trauma | 1 | numerisch |  |
| Aufnahmetyp | 1 | numerisch |  |
| Blutbild: Leukozyten (Minimum) | 5 | numerisch |  |
| Blutbild: pH-Wert | 4 | numerisch |  |
| Blutbild: Thrombozyten (Minimum) | 4 | numerisch |  |
| Chirurgie – Eingriff | 2 | numerisch |  |
| Chirurgischer Status | 1 | numerisch |  |
| Glasgow Coma Scale: motorische Reaktion | 1 | numerisch |  |
| Glasgow Coma Scale: verbale Reaktion | 1 | numerisch |  |
| Glasgow Coma Scale: visuelle Reaktion | 1 | numerisch |  |
| Herzfrequenz (Maximum) | 3 | numerisch |  |
| Koexistierende Erkrankungen | 21 | numerisch |  |
| Körpertemperatur (Maximum) | 4 | numerisch |  |
| Mechanische Beatmung | 1 | numerisch |  |
| Sauerstoff-Partialdruck arteriell (PaO2) | 5 | numerisch |  |
| Sauerstoffkonzentration inspiratorisch (FiO2) | 3 | numerisch |  |
| Serum: Bilirubin (Maximum) | 5 | numerisch |  |
| Serum: Kreatinin (Maximum) | 4 | numerisch |  |
| Systolischer Blutdruck (Minimum) | 3 | numerisch |  |
| Therapeutische Maßnahmen (vor IBS) | 3 | numerisch |  |
| Zutransferierung | 1 | numerisch |  |

| 1\) | Für den stationären Bereich ist diese Satzart nur zu melden, wenn es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. |
| --- | --- |
|  | Für den spitalsambulanten und extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| 2\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |

## Satzart I12 – TISS-A-Daten 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Aufnahmezahl | 12 | alphanumerisch | 2\) |
| Datensatz-ID | 64 | alphanumerisch | 2\) |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Bettenführende Hauptkostenstelle – Positionsnummer | 3 | alphanumerisch |  |
| Erhebungsdatum | 8 | alphanumerisch |  |
| Standard-Monitoring | 1 | numerisch |  |
| Labor | 1 | numerisch |  |
| Medikamente | 1 | numerisch |  |
| Verbandswechsel | 1 | numerisch |  |
| Drainagenpflege | 1 | numerisch |  |
| Atmungsmodus | 1 | numerisch |  |
| Atemwegszugang | 1 | numerisch |  |
| Tubus-/Stomapflege | 1 | numerisch |  |
| Atemtherapie | 1 | numerisch |  |
| Medikamente vasoaktiv | 1 | numerisch |  |
| Flüssigkeitsersatz massiv | 1 | numerisch |  |
| Katheter arteriell | 1 | numerisch |  |
| Monitoring hämodynamisch | 1 | numerisch |  |
| Katheter zentralvenös | 1 | numerisch |  |
| Reanimation kardiopulmonal | 1 | numerisch |  |
| Nierenersatztherapie | 1 | numerisch |  |
| Harnbilanzierung | 1 | numerisch |  |
| Diurese aktiv | 1 | numerisch |  |
| Hirndruckmessung | 1 | numerisch |  |
| Behandlung metabolischer Entgleisungen | 1 | numerisch |  |
| Ernährung enteral | 1 | numerisch |  |
| Ernährung parenteral | 1 | numerisch |  |
| Interventionen | 1 | numerisch |  |
| Diagnostik und Therapie außerhalb der IBS | 1 | numerisch |  |
| Agitation und Delirium | 1 | numerisch |  |
| Assist kardial | 1 | numerisch |  |
| Assist pulmonal | 1 | numerisch |  |
| Hypothermie therapeutisch | 1 | numerisch |  |
| Lebersupport extrakorporal | 1 | numerisch |  |
| Kontinuierliche intravenöse antikonvulsive Therapie | 1 | numerisch |  |

| 1\) | Für den stationären Bereich ist diese Satzart nur zu melden, wenn es sich nicht um am Jahresende verbleibende Patienten/Patientinnen handelt. |
| --- | --- |
|  | Für den spitalsambulanten und extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| 2\) | Das Datenfeld „Datensatz-ID“ ist ausschließlich in den Datenübermittlungen zwischen den Landesgesundheitsfonds bzw. den Landeshauptleuten und dem für das Gesundheitswesen zuständigen Bundesministerium sowie zwischen den Trägern von nicht-landesgesundheitsfondsfinanzierten Krankenanstalten und dem für das Gesundheitswesen zuständigen Bundesministerium zu befüllen. |
|  | Das Datenfeld „Aufnahmezahl“ ist ausschließlich in den Datenübermittlungen zwischen den Trägern von landesgesundheitsfondsfinanzierten Krankenanstalten und den Landesgesundheitsfonds bzw. den Landeshauptleuten zu befüllen. |
|  | Um die Wiederherstellung eines Personenbezuges vollständig auszuschließen, dürfen die Datenfelder „Datensatz-ID“ und „Aufnahmezahl“ nie gleichzeitig befüllt sein. |

## Satzart L01 – Spezielle Leistungsbereiche 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Hauptkostenstelle – Funktionscode | 8 | numerisch |  |
| Leistungsbereich | 1 | alphanumerisch |  |
| Gruppe/Stufe | 2 | alphanumerisch |  |
| Punkte | 6 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart L02 – Abrechnungsrelevante Kostenträger 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Kostenträger – Code | 2 | alphanumerisch |  |
| LGF – Relevanz | 1 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart L03 – Exklusionen medizinischer Leistungen 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Medizinische Leistung – Code | 10 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart L04 – Exklusionen tagesklinischer medizinischer Leistungen 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Medizinische Leistung – Code | 10 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart E01 – Stammdaten extramuraler Leistungserbringer/Leistungserbringerinnen 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Leistungserbringer-Stammdaten-ID | 20 | alphanumerisch |  |
| Berufssitz/Dienstort – Postleitzahl | 4 | numerisch |  |
| Berufssitz/Dienstort – Gemeindecode | 5 | numerisch |  |
| Organisationsform | 1 | alphanumerisch |  |
| Pseudonym Leistungserbringer/Leistungserbringerin | 88 | Alphanumerisch |  |
| Leistungserbringer-ID | 64 | alphanumerisch |  |
| Krankenanstaltennummer/Nummer des selbständigen Ambulatoriums | 6 | alphanumerisch | 2\) |

| 1\) | Für den spitalsambulanten und stationären Bereich ist diese Satzart nicht zu melden. |
| --- | --- |
| 2\) | Das Datenfeld ist nur zu befüllen, wenn es sich bei dem/der Leistungserbringer/in um eine Krankenanstalt handelt. Dabei ist im Falle einer bettenführenden Krankenanstalt die Krankenanstaltennummer und im Falle einer nicht-bettenführenden Krankenanstalt die Nummer des selbständigen Ambulatoriums einzutragen. |

## Satzart P01 – Pseudonyme Patienten/Patientinnen

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch | 1\) |
| Datensatz-ID | 64 | alphanumerisch |  |
| Aufnahme-/Kontaktdatum | 8 | alphanumerisch |  |
| Pseudonym Patient/Patientin | 88 | alphanumerisch |  |
| bPK GH Patient/Patientin | 300 | alphanumerisch |  |
| bPK SV Patient/Patientin | 300 | alphanumerisch |  |
| bPK AS Patient/Patientin | 300 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist dieses Datenfeld nicht zu befüllen. |
| --- | --- |

## Satzart K01 – Kostenstellenplan 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Funktionscode | 8 | numerisch |  |
| Interne Kostenstellennummer | 8 | alphanumerisch |  |
| Interne Kostenstellenbezeichnung | 50 | alphanumerisch |  |
| Spezielle Organisationsform | 1 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K02 – KA-Stammdaten 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Krankenanstalt – Bezeichnung | 150 | alphanumerisch |  |
| Krankenanstalt – Straße | 50 | alphanumerisch |  |
| Krankenanstalt – Postleitzahl | 6 | alphanumerisch |  |
| Krankenanstalt – Ort | 50 | alphanumerisch |  |
| Krankenanstalt – Telefon | 20 | alphanumerisch |  |
| Krankenanstalt – Fax | 20 | alphanumerisch |  |
| Krankenanstalt – Homepage | 100 | alphanumerisch |  |
| Rechtsträger – Bezeichnung | 150 | alphanumerisch |  |
| Rechtsträger – Straße | 50 | alphanumerisch |  |
| Rechtsträger – Postleitzahl | 6 | alphanumerisch |  |
| Rechtsträger – Ort | 50 | alphanumerisch |  |
| Rechtsträger – Telefon | 20 | alphanumerisch |  |
| Rechtsträger – Fax | 20 | alphanumerisch |  |
| Rechtsträger – Homepage | 100 | alphanumerisch |  |
| Ärztliche Leitung | 100 | alphanumerisch |  |
| Verwaltungsleitung | 100 | alphanumerisch |  |
| Pflegedienstleitung | 100 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K03 – KA-Statistik (Ressourcen und Inanspruchnahme) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Systemisierte Betten insgesamt | 6 | numerisch |  |
| Systemisierte Betten – Sonderklasse | 6 | numerisch |  |
| Tatsächlich aufgestellte Betten insgesamt | 6 | numerisch |  |
| Tatsächlich aufgestellte Betten – Sonderklasse | 6 | numerisch |  |
| Belagstage – Sonderklasse | 6 | numerisch |  |
| Aufnahmen – Sonderklasse | 6 | numerisch |  |
| Vom Vorjahr Verbliebene – Sonderklasse | 6 | numerisch |  |
| Entlassungen – Sonderklasse | 6 | numerisch |  |
| Verstorbene – Sonderklasse | 6 | numerisch |  |
| Aufnahmen von Begleitpersonen | 6 | numerisch |  |
| Belagstage von Begleitpersonen | 6 | numerisch |  |
| Ambulante Patienten/Patientinnen | 6 | numerisch |  |
| Ambulante Betreuungsplätze | 6 | numerisch |  |
| OP-Tische | 6 | numerisch |  |
| Entbindungsplätze | 6 | numerisch |  |
| Postoperative Überwachungsplätze | 6 | numerisch |  |
| Dialyseplätze | 6 | numerisch |  |
| Obduktionen durch Anstaltspersonal | 6 | numerisch |  |
| Obduktionen durch Fremdpersonal | 6 | numerisch |  |
| Entbindungen – Lebendgeborene | 6 | numerisch |  |
| Entbindungen – Totgeborene | 6 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K04 – KA-Statistik (Personal-Vollzeitäquivalente nach Funktionsgruppen und Dienstverhältnis) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Personalgruppenindex | 3 | alphanumerisch |  |
| Personal – Vollzeitäquivalente | 9 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K05 – KA-Statistik (Personal des ärztlichen Dienstes) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Fachhauptbereichsindex | 2 | alphanumerisch |  |
| Fachärzte/-ärztinnen – Kopfzahl | 6 | numerisch |  |
| Ärzte/Ärztinnen für Allgemeinmedizin – Kopfzahl | 6 | numerisch |  |
| Fachärzte/-ärztinnen in Ausbildung – Kopfzahl | 6 | numerisch |  |
| Ärzte/Ärztinnen für Allgemeinmedizin in Ausbildung – Kopfzahl | 6 | numerisch |  |
| Fachärzte/-ärztinnen – Vollzeitäquivalente | 9 | numerisch |  |
| Ärzte/Ärztinnen für Allgemeinmedizin – Vollzeitäquivalente | 9 | numerisch |  |
| Fachärzte/-ärztinnen in Ausbildung – Vollzeitäquivalente | 9 | numerisch |  |
| Ärzte/Ärztinnen für Allgemeinmedizin in Ausbildung – Vollzeitäquivalente | 9 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K06 – KA-Statistik (Konsiliarärztlicher Dienst) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Fachrichtungsindex | 2 | alphanumerisch |  |
| Konsiliarärzte/-ärztinnen – Kopfzahl | 6 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K07 – KA-Statistik (Personal der nicht-ärztlichen Gesundheitsberufe) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Index nicht-ärztliche Gesundheitsberufe | 2 | alphanumerisch |  |
| Personal männlich – Kopfzahl | 6 | numerisch |  |
| Personal weiblich – Kopfzahl | 6 | numerisch |  |
| Darunter EU-Ausländer/innen insgesamt – Kopfzahl | 6 | numerisch |  |
| Darunter Nicht-EU-Ausländer/innen insgesamt – Kopfzahl | 6 | numerisch |  |
| Personal männlich – Vollzeitäquivalente | 9 | numerisch |  |
| Personal weiblich – Vollzeitäquivalente | 9 | numerisch |  |
| Darunter EU-Ausländer/innen insgesamt – Vollzeitäquivalente | 9 | numerisch |  |
| Darunter Nicht-EU-Ausländer/innen insgesamt – Vollzeitäquivalente | 9 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K08 – Kostenstellen-Statistik und Kostennachweis (Bettenführende Hauptkostenstelle) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Bettenführende Hauptkostenstelle – Funktionscode | 8 | numerisch |  |
| Systemisierte Betten | 6 | numerisch |  |
| Tatsächlich aufgestellte Betten | 6 | numerisch |  |
| Nettogrundrissfläche | 6 | numerisch | 2\) |
| Ärzte/Ärztinnen – Vollzeitäquivalente (MLV 1-1) | 9 | Numerisch | 2\) |
| Apotheker/innen, Chemiker/innen, Physiker/innen u.ä. – Vollzeitäquivalente (MLV 1-2) | 9 | numerisch | 2\) |
| Hebammen – Vollzeitäquivalente (MLV 1-3) | 9 | numerisch | 2\) |
| Gehobener Dienst für Gesundheits- und Krankenpflege und weitere Gesundheitsberufe – Vollzeitäquivalente (MLV 1-4) | 9 | numerisch | 2\) |
| Gehobene med.-techn. Dienste, med.-techn. Fachdienst und Masseure/Masseurinnen – Vollzeitäquivalente (MLV 1-5) | 9 | numerisch | 2\) |
| Sanitäter, Pflegeassistenz, Pflegefachassistenz und MA – Vollzeitäquivalente (MLV 1-6) | 9 | numerisch | 2\) |
| Verwaltungs- und Kanzleipersonal – Vollzeitäquivalente (MLV 1-7) | 9 | numerisch | 2\) |
| Betriebspersonal – Vollzeitäquivalente (MLV 1-8) | 9 | numerisch | 2\) |
| Sonstiges Personal – Vollzeitäquivalente (MLV 1-9) | 9 | numerisch | 2\) |
| Personalkosten (KOAGR01) | 10 | numerisch | 2\) |
| Kosten für medizinische Gebrauchs- und Verbrauchsgüter (KOAGR02) | 10 | numerisch | 2\) |
| Kosten für nicht-medizinische Gebrauchs- und Verbrauchsgüter (KOAGR03) | 10 | numerisch | 2\) |
| Kosten für medizinische Fremdleistungen (KOAGR04) | 10 | numerisch | 2\) |
| Kosten für nicht-medizinische Fremdleistungen (KOAGR05) | 10 | numerisch | 2\) |
| Energiekosten (KOAGR06) | 10 | numerisch | 2\) |
| Abgaben, Beiträge, Gebühren und sonstige Kosten (KOAGR07) | 10 | numerisch | 2\) |
| Kalkulatorische Anlagekapitalkosten (KOAGR08) | 10 | numerisch | 2\) |
| Kosten der vorwiegend medizinisch bedingten Ver- und Entsorgung (KOAGR11) | 10 | numerisch | 2\) |
| Kosten der vorwiegend nicht-medizinisch bedingten Ver- und Entsorgung (KOAGR12) | 10 | numerisch | 2\) |
| Kosten der Verwaltung (KOAGR13) | 10 | numerisch | 2\) |
| Andere Sekundärkosten (KOAGR14) | 10 | numerisch | 2\) |
| Kostenminderungen | 10 | numerisch | 2\) |
| Summe abgegebener innerbetr. Leistungen | 10 | numerisch | 2\) |
| Unter- oder Überdeckung | 10 | numerisch | 2\) |
| Endkosten der Kostenstelle | 10 | numerisch | 2\) |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |
| 2\) | Für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten sind diese Datenfelder nicht zu befüllen. |

## Satzart K09 – Kostenstellen-Statistik und Kostennachweis (nicht-bettenführende Hauptkostenstelle) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Nicht-bettenführende Hauptkostenstelle – Funktionscode | 8 | numerisch |  |
| Ambulante Betreuungsplätze | 6 | numerisch |  |
| Ambulante Patienten/Patientinnen | 6 | numerisch |  |
| Frequenzen an ambulanten Patienten/Patientinnen | 8 | numerisch |  |
| Frequenzen an stationären Patienten/Patientinnen | 8 | numerisch |  |
| Frequenzen an stationären Patienten/Patientinnen anderer Krankenhäuser | 8 | numerisch |  |
| Nettogrundrissfläche | 6 | numerisch |  |
| Ärzte/Ärztinnen – Vollzeitäquivalente (MLV 1-1) | 9 | numerisch |  |
| Apotheker/innen, Chemiker/innen, Physiker/innen u.ä. – Vollzeitäquivalente (MLV 1-2) | 9 | numerisch |  |
| Hebammen – Vollzeitäquivalente (MLV 1-3) | 9 | numerisch |  |
| Gehobener Dienst für Gesundheits- und Krankenpflege und weitere Gesundheitsberufe – Vollzeitäquivalente (MLV 1-4) | 9 | numerisch |  |
| Gehobene med.-techn. Dienste, med.-techn. Fachdienst und Masseure/Masseurinnen – Vollzeitäquivalente (MLV 1-5) | 9 | numerisch |  |
| Sanitäter, Pflegeassistenz, Pflegefachassistenz und MA – Vollzeitäquivalente (MLV 1-6) | 9 | numerisch |  |
| Verwaltungs- und Kanzleipersonal – Vollzeitäquivalente (MLV 1-7) | 9 | numerisch |  |
| Betriebspersonal – Vollzeitäquiv. (MLV 1-8) | 9 | numerisch |  |
| Sonstiges Personal – Vollzeitäquiv. (MLV 1-9) | 9 | numerisch |  |
| Personalkosten (KOAGR01) | 10 | numerisch |  |
| Kosten für medizinische Gebrauchs- und Verbrauchsgüter (KOAGR02) | 10 | numerisch |  |
| Kosten für nicht-medizinische Gebrauchs- und Verbrauchsgüter (KOAGR03) | 10 | numerisch |  |
| Kosten für med. Fremdleistungen (KOAGR04) | 10 | numerisch |  |
| Kosten für nicht-medizinische Fremdleistungen (KOAGR05) | 10 | numerisch |  |
| Energiekosten (KOAGR06) | 10 | numerisch |  |
| Abgaben, Beiträge, Gebühren und sonstige Kosten (KOAGR07) | 10 | numerisch |  |
| Kalkulat. Anlagekapitalkosten (KOAGR08) | 10 | numerisch |  |
| Kosten der vorwiegend medizinisch bedingten Ver- und Entsorgung (KOAGR11) | 10 | numerisch |  |
| Kosten der vorwiegend nicht-medizinisch bedingten Ver- und Entsorgung (KOAGR12) | 10 | numerisch |  |
| Kosten der Verwaltung (KOAGR13) | 10 | numerisch |  |
| Andere Sekundärkosten (KOAGR14) | 10 | numerisch |  |
| Kostenminderungen | 10 | numerisch |  |
| Summe abgegebener innerbetr. Leistungen | 10 | numerisch |  |
| Unter- oder Überdeckung | 10 | numerisch |  |
| Endkosten der Kostenstelle | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K10 – Kostenstellen-Statistik und Kostennachweis (Neben- und Hilfskostenstellen) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Neben-/Hilfskostenstelle – Funktionscode | 8 | numerisch |  |
| Nettogrundrissfläche | 6 | numerisch |  |
| Personal insgesamt – Vollzeitäquivalente | 9 | numerisch |  |
| Personalkosten (KOAGR01) | 10 | numerisch |  |
| Kosten für medizinische Gebrauchs- und Verbrauchsgüter (KOAGR02) | 10 | numerisch |  |
| Kosten für nicht-medizinische Gebrauchs- und Verbrauchsgüter (KOAGR03) | 10 | numerisch |  |
| Kosten für medizinische Fremdleistungen (KOAGR04) | 10 | numerisch |  |
| Kosten für nicht-medizinische Fremdleistungen (KOAGR05) | 10 | numerisch |  |
| Energiekosten (KOAGR06) | 10 | numerisch |  |
| Abgaben, Beiträge, Gebühren und sonstige Kosten (KOAGR07) | 10 | numerisch |  |
| Kalkulatorische Anlagekapitalkosten (KOAGR08) | 10 | numerisch |  |
| Kosten der vorwiegend medizinisch bedingten Ver- und Entsorgung (KOAGR11) | 10 | numerisch |  |
| Kosten der vorwiegend nicht-medizinisch bedingten Ver- und Entsorgung (KOAGR12) | 10 | numerisch |  |
| Kosten der Verwaltung (KOAGR13) | 10 | numerisch |  |
| Andere Sekundärkosten (KOAGR14) | 10 | numerisch |  |
| Kostenminderungen | 10 | numerisch |  |
| Summe abgegebener innerbetrieblicher Leistungen | 10 | numerisch |  |
| Unter- oder Überdeckung | 10 | numerisch |  |
| Endkosten der Kostenstelle | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K11 – Sammel-Kostennachweis Summenblatt 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Personalkosten (KOAGR01) | 10 | numerisch |  |
| Kosten für medizinische Gebrauchs- und Verbrauchsgüter (KOAGR02) | 10 | numerisch |  |
| Kosten für nicht-medizinische Gebrauchs- und Verbrauchsgüter (KOAGR03) | 10 | numerisch |  |
| Kosten für medizinische Fremdleistungen (KOAGR04) | 10 | numerisch |  |
| Kosten für nicht-medizinische Fremdleistungen (KOAGR05) | 10 | numerisch |  |
| Energiekosten (KOAGR06) | 10 | numerisch |  |
| Abgaben, Beiträge, Gebühren und sonstige Kosten (KOAGR07) | 10 | numerisch |  |
| Kalkulatorische Anlagekapitalkosten (KOAGR08) | 10 | numerisch |  |
| Summe Primärkosten | 10 | numerisch |  |
| Kostenminderungen | 10 | numerisch |  |
| Endkosten der Krankenanstalt | 10 | numerisch |  |
| Summe der kalkulatorischen Abschreibungen | 10 | numerisch |  |
| Davon kalkulatorische Abschreibungen für Anlagegüter mit Restwert 0 | 10 | numerisch |  |
| Davon kalkulatorische Abschreibungen von Restwerten ausgeschiedener oder stillgelegter Anlagen | 10 | numerisch |  |
| Summe der kalkulatorischen Zinsen | 10 | numerisch |  |
| Summe der kalkulatorischen Mieten | 10 | numerisch |  |
| Endkosten der stationären Patientenversorgung | 10 | numerisch | 2\) |
| Endkosten der ambulanten Patientenversorgung | 10 | numerisch | 2\) |
| Endkosten der Nebenkostenstellen | 10 | numerisch | 2\) |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |
| 2\) | Diese Datenfelder sind nur zu befüllen, wenn im Kostennachweis einer oder mehrerer Kostenstellen (Satzarten K08 bis K10) Unter- oder Überdeckungsbeträge ausgewiesen werden. |

## Satzart K12 – Sammel-Kostennachweis Detailblätter 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Blattnummer | 5 | alphanumerisch |  |
| MLV-Nummer | 3 | numerisch |  |
| Aufwand gemäß Finanzbuchführung | 10 | numerisch |  |
| Neutraler Aufwand | 10 | numerisch |  |
| Kalkulatorische Kosten | 10 | numerisch |  |
| Kosten | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K13 – Kalkulatorischer Anhang – Kostenminderungen 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Index Kostenminderungsart | 2 | alphanumerisch |  |
| Kostenminderungen | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K14 – Kalkulatorischer Anhang – Kalkulatorischer Anlagenspiegel 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Anlagenindex | 2 | alphanumerisch |  |
| Anschaffungs- und Herstellungskosten | 10 | numerisch |  |
| Zugänge | 10 | numerisch |  |
| Abgänge | 10 | numerisch |  |
| Umbuchungen | 10 | numerisch |  |
| Kumulierte Abschreibungen | 10 | numerisch |  |
| Buchwerte am Ende des Berichtsjahres | 10 | numerisch |  |
| Buchwerte Vorjahr | 10 | numerisch |  |
| Abschreibungen laufendes Berichtsjahr | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K15 – Kalkulatorischer Anhang – Allgemeine Kostenbereiche 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Kostenbereichs-Kennzahlenindex | 2 | alphanumerisch |  |
| Kosten | 10 | numerisch |  |
| Bezugsgröße | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart K16 – Kalkulatorischer Anhang – Ausgewählte Kosten 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Kostenindex | 2 | alphanumerisch |  |
| Kosten | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart G01 – Großgerätebasisdaten 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Funktionscode | 8 | numerisch |  |
| Großgerät – Positionsnummer | 4 | alphanumerisch |  |
| Großgerät – Art (Geräteindex) | 3 | alphanumerisch |  |
| Großgerät – Type | 100 | alphanumerisch |  |
| Hersteller | 100 | alphanumerisch |  |
| Baujahr | 4 | numerisch |  |
| Anschaffungskosten | 10 | numerisch |  |
| Betriebszeiten | 200 | alphanumerisch |  |
| Kommentar | 200 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart G02 – Großgeräteleistungsdaten 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Großgerät – Positionsnummer | 4 | alphanumerisch |  |
| Großgerät – Leistungsindex | 3 | alphanumerisch |  |
| Ambulante Frequenzen/Patienten/Felder | 10 | numerisch |  |
| Stationäre Frequenzen/Patienten/Felder | 10 | numerisch |  |
| Durchschnittliche Dauer je Frequenz in Minuten | 4 | numerisch | 2\) |

| 1\) | Für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden. |
| --- | --- |
| 2\) | Dieses Datenfeld ist nur bei Erhebung von Frequenzen zu befüllen. |

## Satzart B01 – Basisinformation 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstalten-/Trägernummer | 6 | alphanumerisch |  |
| Berichtstyp | 1 | alphanumerisch |  |
| Berechnungstyp | 1 | alphanumerisch |  |
| Zuordnungsart | 1 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart B02 – Vermögens- und Kapitalstruktur (VKS) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstalten-/Trägernummer | 6 | alphanumerisch |  |
| Berichtstyp | 1 | alphanumerisch |  |
| VKSIndex | 3 | alphanumerisch |  |
| Wert Berichtsjahr | 10 | numerisch |  |
| Wert Vorjahr | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart B03 – Eigenmittelverteilungsrechnung (EVR) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstalten-/Trägernummer | 6 | alphanumerisch |  |
| Berichtstyp | 1 | alphanumerisch |  |
| EVRIndex | 3 | alphanumerisch |  |
| Wert Berichtsjahr | 10 | numerisch |  |
| Wert Vorjahr | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart B04 – Quellen- und Verwendungsanalyse (QVA) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstalten-/Trägernummer | 6 | alphanumerisch |  |
| Berichtstyp | 1 | alphanumerisch |  |
| QVAIndex | 3 | alphanumerisch |  |
| Wert Berichtsjahr | 10 | numerisch |  |
| Wert Vorjahr | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart B05 – Erlösstruktur (ES) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstalten-/Trägernummer | 6 | alphanumerisch |  |
| Berichtstyp | 1 | alphanumerisch |  |
| ErlösIndex | 3 | alphanumerisch |  |
| Wert Gesamt | 10 | numerisch |  |
| Wert LGF | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart B06 – Zuschussstruktur (ZS) 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstalten-/Trägernummer | 6 | alphanumerisch |  |
| Berichtstyp | 1 | alphanumerisch |  |
| FinanzierungsträgerIndex | 2 | alphanumerisch |  |
| ZuschussartIndex | 3 | alphanumerisch |  |
| Zuschuss | 10 | numerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten ist diese Satzart nicht zu melden. |
| --- | --- |

## Satzart A01 – Antiinfektiva-Abrufe 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Monat | 2 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Bettenführende bzw. nicht-bettenführende Hauptkostenstelle – Funktionscode | 8 | numerisch | 2\) |
| Bezugsland | 2 | alphanumerisch |  |
| Pharmazentralnummer | 15 | alphanumerisch |  |
| Handelsname | 100 | alphanumerisch |  |
| Abgerufene Packungen | 10 | numerisch |  |
| Menge je Packungseinheit | 10 | numerisch |  |
| Packungseinheit | 10 | alphanumerisch |  |
| ATC-Code | 10 | alphanumerisch |  |

- 1\) Diese Satzart ist ab dem Berichtsjahr 2025 zu melden. Für nicht-landesgesundheitsfondsfinanzierte Krankenanstalten sowie für den extramuralen ambulanten Bereich ist diese Satzart nicht zu melden.

- 2\) Informationen zu nicht-bettenführenden Hauptkostenstellen sind nur zu melden, sofern diese Informationen systematisch erfasst werden.

## Satzart S11 – Prüf- und Summensatz 1)

| Feld | Maximale Länge | Datenformat |  |
| --- | --- | --- | --- |
| Satzartenkennzeichen | 3 | alphanumerisch |  |
| Jahr | 4 | numerisch |  |
| Krankenanstaltennummer | 6 | alphanumerisch |  |
| Anzahl übermittelte Sätze Satzart X01 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart X02 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart X03 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart X04 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart X05 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart X06 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart X07 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart I11 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart I12 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart L01 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart L02 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart L03 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart L04 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K01 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K02 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K03 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K04 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K05 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K06 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K07 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K08 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K09 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K10 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K11 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K12 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K13 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K14 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K15 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart K16 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart G01 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart G02 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart B01 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart B02 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart B03 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart B04 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart B05 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart B06 | 10 | numerisch |  |
| Anzahl übermittelte Sätze Satzart A01 | 10 | Numerisch |  |
| Leerfeld | 10 | numerisch |  |
| Anzahl der Fehlersätze | 10 | numerisch |  |
| Anzahl der Warningssätze | 10 | numerisch |  |
| Leistungskomponente/Leistungspunkte | 10 | numerisch |  |
| Tageskomponente/Kontaktpunkte | 10 | numerisch |  |
| Punkte Belagsdauerausreißer nach unten – Leistungskomponente | 10 | numerisch |  |
| Punkte Belagsdauerausreißer nach unten – Tageskomponente | 10 | numerisch |  |
| Zusatzpunkte Belagsdauerausreißer nach oben | 10 | numerisch |  |
| Zusatzpunkte Intensiv | 10 | numerisch |  |
| Zusatzpunkte Mehrfachleistungen | 10 | numerisch |  |
| Punkte spezieller Bereiche (tageweise) | 10 | numerisch |  |
| Summe Punkte total innerhalb LGF/PRIKRAF | 10 | numerisch |  |
| Summe Punkte total außerhalb LGF/PRIKRAF | 10 | numerisch |  |
| Kommentar | 200 | alphanumerisch |  |

| 1\) | Für den extramuralen ambulanten Bereich sowie von der beim Dachverband eingerichteten Pseudonymisierungsstelle ist diese Satzart nicht zu melden. |
| --- | --- |
