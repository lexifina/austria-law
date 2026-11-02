## Anhang 1

## 1\. Daten der tierärztlichen Hausapotheken

Datenübertragung: Datenbank der Kammer

| Feldname | Format | Pflicht | Beschreibung |
| --- | --- | --- | --- |
| Datum | Datum | ja | Datum der Anmeldung der HAPO im Format TT.MM.JJJJ |
| Hapo\_Id\* | Text | ja | Identifikationsnummer der tierärztlichen Hausapotheke |
| tierarzt\_id | Text | nein | Tierarztnummer |
| name | Text | ja | Name des Inhabers |
| strasse | Text | ja | Straße (Berufssitz) |
| hNr | Text | ja | Hausnummer (Berufssitz) |
| plz | Text | ja | Postleitzahl (Berufssitz) |
| ort | Text | ja | Ort (Berufssitz) |
| telefon | Text | nein | Telefonnummer |
| fax | Text | nein | Faxnummer |
| email | Text | nein | E-Mail Adresse |
| datumEnde | Datum | ja | Datum der Auflösung im Format TT.MM.JJJJ, leer falls TÄHAPO noch zugelassen |

\*Wartung der Liste durch Kammer

## 2\. Identifikationsnummer der tierärztlichen Hausapotheke

## 2.1. Standortnummer

Die Standortnummer hat folgendes Format zu enthalten:

1\. Die Buchstaben „HA“

2\. eine Ziffer, anhand der das Bundesland des Standortes abgeleitet werden kann:

- 1 – Burgenland

- 2 – Kärnten

- 3 – Niederösterreich

- 4 – Oberösterreich

- 5 – Salzburg

- 6 – Steiermark

- 7 – Tirol

- 8 – Vorarlberg

- 9 – Wien

3\. eine fortlaufende vierstellige Nummer, die mit Hilfe des elektronischen Veterinärregisters (VIS) generiert wird.

Beispieldatensatz:

HA10123

## 2.2. Identifikationsnummer

Die Identifikationsnummer der tierärztlichen Hausapotheke setzt sich aus deren Standortnummer (nach 2.1.) sowie aus der fünfstelligen Tierarztnummer der verantwortlichen Tierärztin oder des verantwortlichen Tierarztes zusammen. Einer vierstelligen Tierarztnummer ist dabei eine „0“ voran zu stellen.

Beispieldatensatz:

HA1012309876
