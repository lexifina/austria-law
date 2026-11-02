## Anhang 4

## Freiwilliger Teil: Anwendungsdaten

| Feldname | Pflicht | Format | Beschreibung |
| --- | --- | --- | --- |
| MelderID | Ja | Text | ID des Tierarztes bzw. LFBIS des Betriebes, falls nicht vorhanden VIS-Registriernummer oder ID des Bündlers |
| Meldejahr | Ja | Zahl | Kalenderjahr der Anwendung |
| Art der Meldung \* | Ja | Katalog | „Anwendung“ |
| Anwendung durch TA | Ja | Boolean | Anwendung durch Tierarzt ja/nein |
| Datum | Ja | Datum | Datum der Anwendung im Format TT.MM.JJJJ |
| ID des Tierarztes | Nein | Text | ID des anwendenden Tierarztes |
| LFBIS | Ja | Text | Betriebsnummer (LFBIS) – falls nicht vorhanden, VIS-Registrierungsnummer – des Betriebes, auf dem die Anwendung der Arzneispezialität erfolgt ist |
| Zulassungsnummer \* | Ja | Text | Zulassungsnummer der Arzneispezialität |
| Tierart \* | Ja | Katalog | auszuwählende Tierart: „Rind“, „Schwein“,… etc. |
| Nutzungsart \* | Ja | Katalog |  |
| Tierkennzeichen | Ja | Text | Rind: Ohrmarkennummer Schweine oder Hühner: Herden-, Stall- oder Buchtenbezeichnung |
| Tagessumme angewandte Menge | Ja | Zahl | angewandte Menge in der Anwendungsdauer |
| Anwendungseinheit \* | Ja | Katalog | Kleinste anzuwendende Einheit in „ml“, „l“, „g“, „kg“, „stk“ |
| Anzahl der behandelten Tiere | Ja | Text | Anzahl der behandelten Tiere |
| Diagnosecode \* | Ja | Katalog |  |
| Anwendungsdauer (in Tagen) | Ja | Text | auf dem Abgabebeleg angegebene Anwendungs- oder Einsatzdauer |
| Chargennummer | Nein | Text | Charge der Arzneispezialität |
| HAPO\_ID \*\* | Nein | Text | Identifikationsnummer der tierärztlichen Hausapotheke |

\* gemäß der veröffentlichten Liste(n) der durchführenden Stelle

\*\* Wartung der Liste durch ÖTK
