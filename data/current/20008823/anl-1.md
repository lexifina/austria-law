## Anhang 1

## 1.1. Tierarzneimitteldatensatz

Anmerkung: Die detaillierte technische Spezifikation ist auf der Homepage der durchführenden Stelle veröffentlicht.

### 1.1.1. Bereitgestellte Datenfelder von Veterinärantibiotika

| Feldname | Pflicht | Format | Beschreibung |
| --- | --- | --- | --- |
| Zulassungsnummer | Ja | Text | Zulassungsnummer der Arzneispezialität |
| Bezeichnung | Ja | Text | Bezeichnung der Arzneispezialität |
| Darreichungsform | Ja | Text | Darreichungsform der Arzneispezialität |
| Zulassungsinhaber | Ja | Text | Organisationsname des Zulassungsinhabers der Arzneispezialität |
| Vertriebsfirma | Nein | Text | Organisationsname der Vertriebsfirma der Arzneispezialität |
| Status | Ja | Text | Status der Arzneispezialität |
| Datum des Status | Ja | Datum | Datum des Status der Arzneispezialität Anmerkung: Wenn die Arzneispezialität zugelassen ist, wird das Erstzulassungsdatum angezeigt. Ist die Arzneispezialität aufgehoben, wird das Aufhebungsdatum angezeigt |
| ATCvet Code | Ja | Text | ATCvet Code der Arzneispezialität |
| Abgabestatus | Ja | Text | Abgabestatus der Arzneispezialität |
| Anwendungseinheit | Ja | Katalog | Kleinste anzuwendende Einheit der Arzneispezialität in „ml“, „l“, „g“, „kg“, „stk“ |
| Packungsgröße | Ja | Zahl | Packungsgröße der Arzneispezialität (bezogen auf die Packungseinheit) |
| Einheit der Packung | Ja | Katalog | Einheit der Packungsgröße der Arzneispezialität (z. B. „ml“, „l“, „g“, „kg“, „stk“) |
| Tierart | Ja | Katalog | Bsp.: „Rind“, „Schwein“, etc. |
| Anwendungsart | Ja | Text |  |
| Indikation | Nein | Text | Einsatzindikation |
| Wirkstoff | Ja | Text | Wirkstoff der Arzneispezialität |
| add | Ja | Zahl | Animal Daily Dose in mg/GVE |
| Minimale Dosierung | Nein | Zahl | Minimale Dosierung |
| Maximale Dosierung | Nein | Zahl | Maximale Dosierung |
| Einheit der Dosierung | Nein | Katalog | Einheit der Dosierung |
| Minimale Anwendungsdauer | Nein | Zahl | Minimale Anwendungsdauer |
| Maximale Anwendungsdauer | Nein | Zahl | Maximale Anwendungsdauer |
| Einheit der Anwendungsdauer | Nein | Katalog | Einheit der Anwendungsdauer |
| pdd | Nein | Zahl | Prescribed Daily Dose in mg/GVE |
| Zielgewebe | Nein | Text | Bsp.: „Essbares Gewebe“, „Milch“ |
| Dosierung | Nein | Text |  |
| Wartezeit | Nein | Zahl |  |
| Einheit der Wartezeit | Nein | Katalog | Einheit der Wartezeit |
| Besonderheit (Wartezeit) | Nein | Text | Beschreibung von Besonderheiten bei Wartezeiten |
| Wirkstoff | Nein | Text | Bezeichnung des Wirkstoffs der Arzneispezialität |
| Wirkstoffgehalt von | Nein | Zahl | Wirkstoffgehalt des Wirkstoffes pro Anwendungseinheit |
| Wirkstoffgehalt bis | Nein | Zahl | Wirkstoffgehalt des Wirkstoffes pro Anwendungseinheit |
| Einheit des Wirkstoffgehalts | Nein | Katalog | Einheit des Wirkstoffgehalts |
| Fachinformation | Nein | Text | Link auf die gültige Fachinformation |
| Gebrauchsinformation | Nein | Text | Link auf die gültige Gebrauchsinformation |
| Antibiotika Mengenstromverordnung | Nein | Boolean |  |

## 1.1.2. Bereitgestellte Datenfelder von Veterinär-Arzneispezialitäten (ausgenommen Veterinärantibiotika)

| Feldname | Pflicht | Format | Beschreibung |
| --- | --- | --- | --- |
| Zulassungsnummer | Ja | Text | Zulassungsnummer der Arzneispezialität |
| Bezeichnung | Ja | Text | Bezeichnung der Arzneispezialität |
| Darreichungsform | Ja | Text | Darreichungsform der Arzneispezialität |
| Zulassungsinhaber | Ja | Text | Organisationsname des Zulassungsinhabers der Arzneispezialität |
| Vertriebsfirma | Nein | Text | Organisationsname der Vertriebsfirma der Arzneispezialität |
| Status | Ja | Text | Status der Arzneispezialität |
| Datum des Status | Ja | Datum | Datum des Status der Arzneispezialität Anmerkung: Wenn die Arzneispezialität zugelassen ist, wird das Erstzulassungsdatum angezeigt. Ist die Arzneispezialität aufgehoben, wird das Aufhebungsdatum angezeigt |
| ATCvet Code | Ja | Text | ATCvet Code der Arzneispezialität |
| Abgabestatus | Ja | Text | Abgabestatus der Arzneispezialität |
| Anwendungseinheit | Ja | Katalog | Kleinste anzuwendende Einheit der Arzneispezialität in „ml“, „l“, „g“, „kg“, „stk“ |
| Packungsgröße | Ja | Text | Packungsgröße der Arzneispezialität (bezogen auf die Packungseinheit) |
| Einheit der Packung | Ja | Text | Einheit der Packungsgröße der Arzneispezialität (z. B. „ml“, „l“, „g“, „kg“, „stk“) |
| Tierart | Ja | Katalog | Bsp.: „Rind“, „Schwein“, etc. |
| Anwendungsart | Ja | Text |  |
| Zielgewebe | Nein | Text | Bsp.: „Essbares Gewebe“, „Milch“ |
| Dosierung | Nein | Text |  |
| Wartezeit | Nein | Zahl |  |
| Einheit der Wartezeit | Nein | Katalog | Einheit der Wartezeit |
| Besonderheit (Wartezeit) | Nein | Text | Beschreibung von Besonderheiten bei Wartezeiten |
| Fachinformation | Nein | Text | Link auf die gültige Fachinformation |
| Gebrauchsinformation | Nein | Text | Link auf die gültige Gebrauchsinformation |
| Antibiotika Mengenstromverordnung | Nein | Boolean |  |
