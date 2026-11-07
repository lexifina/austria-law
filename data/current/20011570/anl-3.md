## Anlage 3

## zu § 10a

## Teil I

## Daten für den Datenverbund der Schulen im Zusammenhang mit der Anmeldung

1.1 Definition der Schnittstellen zwischen den lokalen Evidenzen und der BRZ: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchUG-BKV“ = Schulunterrichtsgesetz für Berufstätige, Kollegs und Vorbereitungslehrgänge, [BGBl. I Nr. 33/1997](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1997_33_1/1997_33_1.pdf>), SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

2\. Das Wurzel-Element datenverbund\_anmeldung (Webservice: addRequest) muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| xmlns | mit dem Wert „datenverbund\_schulen\_anmeldung“ |
| meldedatum | mit dem Datum dieser Meldung |
| absender | mit der (Schul- bzw. Cluster-)Kennzahl des Absenders |

3\. Das Element schule ist ein Kind-Element von „datenverbund\_anmeldung“, muss mindestens einmal pro Datenmeldung vorhanden sein (Schüler von Exposituren, dislozierten Klassen, Schulcluster uä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen zu melden) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt (gemäß der vom BMBWF zur Verfügung gestellten österreichischen Schulendatei) |

4\. Das Element schueler ist ein Kind-Element von „schule“, muss mindestens einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>vbPKBF</p></td>
    <td colspan="2"><p>mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Bildung und Forschung gemäß § 9 E-GovG (wenn verfügbar)</p></td>
  </tr>
  <tr>
    <td><p>vbPKAS</p></td>
    <td colspan="2"><p>mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik gemäß § 9 E-GovG (wenn verfügbar)</p></td>
  </tr>
  <tr>
    <td><p>svnr</p></td>
    <td colspan="2"><p>mit der Sozialversicherungsnummer der Schülerin oder des Schülers (wenn verfügbar) zum Zweck der Inanspruchnahme von Leistungen gemäß § 8 Abs. 1 Z 3 lit. h und i des Allgemeinen Sozialversicherungsgesetzes – ASVG, <a href="https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1955_189_0/1955_189_0.pdf">BGBl. 189/1955</a></p></td>
  </tr>
  <tr>
    <td><p>ersatz</p></td>
    <td colspan="2"><p>mit der Ersatzkennung für die Schülerin oder den Schüler, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind bzw. bis zur Ausstattung mit bPK, wenn die Sozialversicherungsnummer („svnr“) nicht verfügbar ist</p></td>
  </tr>
  <tr>
    <td><p>vorname</p></td>
    <td colspan="2"><p>mit dem ersten Vornamen laut den vorgelegten Personenstandsdokumenten</p></td>
  </tr>
  <tr>
    <td><p>weitere-vornamen</p></td>
    <td colspan="2"><p>mit eventuellen weiteren Vornamen laut den vorgelegten Personenstandsdokumenten, wobei bei der Angabe von mehr als einem weiteren Vornamen ein Abstand eingegeben werden muss</p></td>
  </tr>
  <tr>
    <td><p>zuname</p></td>
    <td colspan="2"><p>mit dem oder den Familiennamen laut den vorgelegten Personenstandsdokumenten</p></td>
  </tr>
  <tr>
    <td><p>akadGradVor</p></td>
    <td colspan="2"><p>mit einem allfälligen, dem Namen vorgestellten akademischen Grad laut Verleihungsurkunde</p></td>
  </tr>
  <tr>
    <td><p>akadGradNach</p></td>
    <td colspan="2"><p>mit einem allfälligen, dem Namen nachgestellten akademischen Grad laut Verleihungsurkunde</p></td>
  </tr>
  <tr>
    <td><p>geburtsDatum</p></td>
    <td colspan="2"><p>mit dem Geburtsdatum der Schülerin oder des Schülers</p></td>
  </tr>
  <tr>
    <td><p>geschlecht</p></td>
    <td colspan="2"><p>mit dem Geschlecht der Schülerin oder des Schülers in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„m“</p></td>
    <td><p>für männlich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„w“</p></td>
    <td><p>für weiblich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„x“</p></td>
    <td><p>für divers</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>für offen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„i“</p></td>
    <td><p>für inter</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>für den Fall, dass von jeglicher Geschlechtsangabe abgesehen wurde</p></td>
  </tr>
  <tr>
    <td><p>plz</p></td>
    <td colspan="2"><p>mit der Postleitzahl der Heimatadresse der Schülerin oder des Schülers, bei einer Auslandsadresse Eintrag des Postleitzahlen-Ersatzcodes nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes</p></td>
  </tr>
  <tr>
    <td><p>ort</p></td>
    <td colspan="2"><p>mit der Bezeichnung des Ortes der Heimatadresse der Schülerin oder des Schülers</p></td>
  </tr>
  <tr>
    <td><p>strasse</p></td>
    <td colspan="2"><p>mit der Straßenbezeichnung samt Hausnummer der Heimatadresse der Schülerin oder des Schülers</p></td>
  </tr>
</table>

## Teil II

## Daten für den Datenverbund der Schulen im Zusammenhang mit der Aufnahme

1.1 Definition der Schnittstellen zwischen den lokalen Schulverwaltungsprogrammen und der BRZ: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

1.2. Falls die Datenübermittlung in technischer Hinsicht nicht nach Maßgabe dieser Anlage erfolgen kann, so sind für die Datenmeldung die von der Bundesministerin oder dem Bundesminister für Bildung vorgegebenen Formate zu verwenden.

1.3 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchUG-BKV“ = Schulunterrichtsgesetz für Berufstätige, Kollegs und Vorbereitungslehrgänge, [BGBl. I Nr. 33/1997](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1997_33_1/1997_33_1.pdf>), SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

2\. Das Wurzel-Element datenverbund muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| xmlns | mit dem Wert „datenverbund\_schulen“ |
| meldedatum | mit dem Datum dieser Meldung |
| absender | mit der (Schul- bzw. Cluster-)Kennzahl des Absenders |

3\. Das Element schule ist ein Kind-Element von „datenverbund“, muss mindestens einmal pro Datenmeldung vorhanden sein (Schüler von Exposituren, dislozierten Klassen, Schulcluster uä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen zu melden) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt (gemäß der vom BMBWF zur Verfügung gestellten österreichischen Schulendatei) |

4\. Das Element schueler ist ein Kind-Element von „schule“, muss mindestens einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>vbPKBF</p></td>
    <td colspan="2"><p>mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Bildung und Forschung gemäß § 9 E-GovG (wenn verfügbar)</p></td>
  </tr>
  <tr>
    <td><p>vbPKAS</p></td>
    <td colspan="2"><p>mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik gemäß § 9 E-GovG (wenn verfügbar)</p></td>
  </tr>
  <tr>
    <td><p>svnr</p></td>
    <td colspan="2"><p>mit der Sozialversicherungsnummer der Schülerin oder des Schülers (wenn verfügbar) zum Zweck der Inanspruchnahme von Leistungen gemäß § 8 Abs. 1 Z 3 lit. h und i des Allgemeinen Sozialversicherungsgesetzes – ASVG, <a href="https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1955_189_0/1955_189_0.pdf">BGBl. 189/1955</a></p></td>
  </tr>
  <tr>
    <td><p>ersatz</p></td>
    <td colspan="2"><p>mit der Ersatzkennung für die Schülerin oder den Schüler, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind bzw. bis zur Ausstattung mit bPK, wenn die Sozialversicherungsnummer („svnr“) nicht verfügbar ist</p></td>
  </tr>
  <tr>
    <td><p>vorname1</p></td>
    <td colspan="2"><p>mit dem ersten Vornamen laut den vorgelegten Personenstandsdokumenten</p></td>
  </tr>
  <tr>
    <td><p>weitere-vornamen</p></td>
    <td colspan="2"><p>mit eventuellen weiteren Vornamen laut den vorgelegten Personenstandsdokumenten, wobei bei der Angabe von mehr als einem weiteren Vornamen ein Abstand eingegeben werden muss</p></td>
  </tr>
  <tr>
    <td><p>nachname</p></td>
    <td colspan="2"><p>mit dem oder den Familiennamen laut den vorgelegten Personenstandsdokumenten</p></td>
  </tr>
  <tr>
    <td><p>v-akadem-grad</p></td>
    <td colspan="2"><p>mit einem allfälligen, dem Namen vorgestellten akademischen Grad laut Verleihungsurkunde</p></td>
  </tr>
  <tr>
    <td><p>n-akadem-grad</p></td>
    <td colspan="2"><p>mit einem allfälligen, dem Namen nachgestellten akademischen Grad laut Verleihungsurkunde</p></td>
  </tr>
  <tr>
    <td><p>geburtsDatum</p></td>
    <td colspan="2"><p>mit dem Geburtsdatum der Schülerin oder des Schülers</p></td>
  </tr>
  <tr>
    <td><p>geschlecht</p></td>
    <td colspan="2"><p>mit dem Geschlecht der Schülerin oder des Schülers in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„m“</p></td>
    <td><p>für männlich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„w“</p></td>
    <td><p>für weiblich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„x“</p></td>
    <td><p>für divers</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>für offen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„i“</p></td>
    <td><p>für inter</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>für den Fall, dass von jeglicher Geschlechtsangabe abgesehen wurde</p></td>
  </tr>
  <tr>
    <td><p>plz</p></td>
    <td colspan="2"><p>mit der Postleitzahl der Heimatadresse der Schülerin oder des Schülers, bei einer Auslandsadresse Eintrag des Postleitzahlen-Ersatzcodes nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes.</p></td>
  </tr>
  <tr>
    <td><p>ort</p></td>
    <td colspan="2"><p>mit der Bezeichnung des Ortes der Heimatadresse der Schülerin oder des Schülers</p></td>
  </tr>
  <tr>
    <td><p>strasse</p></td>
    <td colspan="2"><p>mit der Straßenbezeichnung samt Hausnummer der Heimatadresse der Schülerin oder des Schülers</p></td>
  </tr>
  <tr>
    <td><p>eingeschult</p></td>
    <td colspan="2"><p>mit der Angabe des Kalenderjahres, in dem die Schülerin oder der Schüler in die erste Schulstufe bzw. als Schulpflichtige oder Schulpflichtiger in die Vorschulstufe eintrat (gegebenenfalls gemäß Rückrechnung nach dem SchPflG, zB bei Zuzug aus dem Ausland)</p></td>
  </tr>
  <tr>
    <td><p>besuchsjahr</p></td>
    <td colspan="2"><p>mit der Angabe des (Besuchs-)Jahres in der betreffenden Ausbildung, in dem sich die Schülerin oder der Schüler zum Zeitpunkt der aktuellen Beendigung des Schulbesuchs befunden hat („1“ für das Schuljahr in dem diese Ausbildung begonnen wurde, „2“ im darauf folgenden Schuljahr, „3“ im dritten Schuljahr, in dem diese Ausbildung besucht wurde, und so fort; zurückliegende Schuljahre, die für die zulässige Höchstdauer des Schulbesuchs (§ 32 SchUG bzw. § 31 SchUG-BKV) nicht relevant sind, sind nicht zu berücksichtigen)</p></td>
  </tr>
  <tr>
    <td><p>vorSchulpflicht</p></td>
    <td colspan="2"><p>mit der Angabe gemäß Anlage 1 Teil I Z 15</p></td>
  </tr>
  <tr>
    <td><p>vorschule</p></td>
    <td colspan="2"><p>mit der Angabe, ob nach Widerruf der vorzeitigen Aufnahme bzw. nach Abmeldung vom Besuch der 1. Schulstufe durch das ggf. nicht schulpflichtige Kind die Vorschulstufe besucht wurde (§ 7 Abs. 11SchPflG); sofern zutreffend, ist das Schuljahr (im Format jjjj/jj) des Besuchs der Vorschulstufe anzugeben</p></td>
  </tr>
  <tr>
    <td><p>fruehchen</p></td>
    <td colspan="2"><p>mit der Angabe des für die Bestimmung des Beginns der allgemeinen Schulpflicht relevanten Tages der Geburt des Schülers; zutreffendenfalls mit der Angabe des gemäß Mutter-Kind-Pass festgestellten Tages der Geburt (§ 2 Abs. 2 Schulpflichtgesetz 1985), sonst des Geburtsdatums des Schülers</p></td>
  </tr>
</table>

5\. Das Element ausbildung ist ein Kind-Element von „schueler“, muss pro Schülerin oder Schüler und Datenmeldung einmal bzw. bei Wechsel der Ausbildung innerhalb der Schule, zweimal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="2"><p>mit der Angabe des Schuljahres, zu dem diese Meldung erfolgt (das Schuljahr in dem die betreffende Schülerin oder der betreffende Schüler die meldende Schule zuletzt besucht hat)</p></td>
  </tr>
  <tr>
    <td><p>beginn</p></td>
    <td colspan="2"><p>mit dem Datum des Beginns der laufenden bzw. – wenn beendet – letzten Ausbildung</p></td>
  </tr>
  <tr>
    <td><p>ende</p></td>
    <td colspan="2"><p>mit dem Datum der Beendigung des Schulbesuchs an dieser Schule</p></td>
  </tr>
  <tr>
    <td><p>schulpflichtjahr</p></td>
    <td colspan="2"><p>mit der Angabe des Jahres der (neunjährigen) allgemeinen Schulpflicht in dem sich der Schüler im genannten Schuljahr befunden hat („0“ für einen Schulbesuch vor der Schulpflicht, „1“ bis „9“ für das jeweilige Jahr innerhalb der allgemeinen Schulpflicht und „10“ ff. für Ausbildungsjahre nach der allgemeinen Schulpflicht)</p></td>
  </tr>
  <tr>
    <td><p>schulform</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl dieser Ausbildung (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>stand</p></td>
    <td colspan="2"><p>mit der Information über den gegenwärtigen Stand dieser Ausbildung mit folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„aa“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer Abschlussprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ab“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer Berufsreifeprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ac“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer Reife- und Diplomprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ad“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer Diplomprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ae“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer Studienberechtigungsprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ag“</p></td>
    <td><p>erfolgreich abgeschlossene Volksschule mit Erfüllung der Voraussetzung zur Aufnahme in die 1. Klasse einer allgemein bildenden höheren Schule ohne Aufnahmsprüfung (§ 40 Abs. 1 SchOG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ah“</p></td>
    <td><p>erfolgreich abgeschlossene Mittelschule mit Erfüllung der Voraussetzung zur Aufnahme in die 5. Klasse einer allgemeinbildenden höheren Schule (§ 40 Abs. 3 Z 1 SchOG) bzw. in den 1. Jahrgang einer berufsbildenden höheren Schule (§ 68 Abs. 1 Z 4 SchOG), jeweils in Verbindung mit § 5 Abs. 2 der Verordnung über Aufnahms- und Eignungsprüfungen, <a href="https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1975_291_0/1975_291_0.pdf">BGBl. Nr. 291/1975</a>, ohne Aufnahmsprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„al“</p></td>
    <td><p>erfolgreich abgeschlossener Berufsschulbesuch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„am“</p></td>
    <td><p>erfolgreich abgeschlossene Mittelschule mit Erfüllung der Voraussetzung zur Aufnahme in die 1. Klasse einer mindestens dreijährigen berufsbildenden mittleren Schule (§ 55 Abs. 1a SchOG) ohne Aufnahmsprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„an“</p></td>
    <td><p>erfolgreich abgeschlossene Mittelschule, jedoch ohne Erfüllung der Voraussetzung zur Aufnahme in die 1. Klasse einer mindestens dreijährigen berufsbildenden mittleren Schule (§ 55 Abs. 1a SchOG) ohne Aufnahmsprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ao“</p></td>
    <td><p>erfolgreich abgeschlossene Sonderschule oder sonstige allgemein bildende Pflichtschule (Berufsvorbereitungsjahr, Oberstufe der Volksschule, zur Erfüllung der allgemeinen Schulpflicht geeignete Statutschule, usw.)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ar“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer Reifeprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„as“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer sonstigen abschließenden Prüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„at“</p></td>
    <td><p>erfolgreich abgeschlossene Polytechnische Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„av“</p></td>
    <td><p>erfolgreich abgeschlossene Volksschule, jedoch ohne Erfüllung der Voraussetzung zur Aufnahme in die 1. Klasse einer allgemeinbildenden höheren Schule ohne Aufnahmsprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ay“</p></td>
    <td><p>erfolgreich abgeschlossener Vorbereitungslehrgang bzw. Übergangsstufe zum Oberstufenrealgymnasium oder Aufbaugymnasium und -realgymnasium</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„az“</p></td>
    <td><p>erfolgreich abgeschlossene weiterführende Ausbildung ohne abschließende Prüfung (dh. mit positivem Abschlusszeugnis)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ba“</p></td>
    <td><p>Beendigung des Schulbesuchs mit noch nicht erfolgreich bestandener abschließender Prüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bb“</p></td>
    <td><p>nicht erfolgreicher Abschluss der Berufsschule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„be“</p></td>
    <td><p>vorzeitige Beendigung der Ausbildung infolge vier oder mehr negativer Beurteilungen in Pflichtgegenständen in der ersten Stufe einer berufsbildenden mittleren oder höheren Schule (§ 33 Abs. 2 lit. f iVm § 82a SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bh“</p></td>
    <td><p>nicht erfolgreiche Beendigung der Mittelschule (dh. ohne Abschluss der Mittelschule)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bl“</p></td>
    <td><p>vorzeitige Beendigung der Berufsschule infolge Beendigung des Lehrverhältnisses (§ 33 Abs. 2 lit. b SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bo“</p></td>
    <td><p>nicht erfolgreiche Beendigung einer Sonderschule oder anderen allgemeinbildenden Pflichtschule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„br“</p></td>
    <td><p>Abmeldung vom Schulbesuch während des Schuljahres</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bs“</p></td>
    <td><p>vorzeitige Beendigung dieser Ausbildung durch schulinternen Wechsel in eine andere Ausbildung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bt“</p></td>
    <td><p>nicht erfolgreiche Beendigung der Polytechnischen Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bu“</p></td>
    <td><p>vorzeitige Beendigung der Ausbildung wegen sonstiger Überschreitung der Höchstdauer gemäß § 32 SchUG bzw. § 31 SchUG-BKV</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bv“</p></td>
    <td><p>Beendigung des Schulbesuchs infolge Widerrufs der vorzeitigen Aufnahme in die erste Klasse der Volksschule (§ 33 Abs. 2 lit. e SchUG iVm § 7 Abs. 8 SchPflG) oder Abmeldung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bw“</p></td>
    <td><p>vorzeitige Beendigung der Ausbildung wegen einer nicht mehr zulässigen Wiederholung gemäß § 23a iVm § 33 Abs. 2 lit. g SchUG, jeweils idF <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a></p>
<p>oder § 32 Abs. 1 Z 5 SchUG-BKV“ oder wegen einer nicht mehr vorhandenen Antrittsmöglichkeit gemäß § 30 Abs. 6 iVm § 33 Abs. 2 lit. g SchUG oder § 82e Abs. 7 Z 1 iVm § 30 Abs. 6 und § 33 Abs. 2 lit. g SchUG oder § 32 Abs. 1 Z 5 SchUG-BKV</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bz“</p></td>
    <td><p>sonstige nicht erfolgreiche Beendigung der Ausbildung</p></td>
  </tr>
</table>

6\. Das Element verlaufsdetails ist ein Kind-Element von „ausbildung“, muss pro Ausbildung einmal vorhanden sein, sofern die Ausbildung noch nicht erfolgreich abgeschlossen wurde (dh. der Wert des Attributes „stand“ in Z 5 beginnt mit „b“) und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="4"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="4"><p>mit der Angabe der von der Schülerin oder dem Schüler zuletzt besuchten Schulstufe, die eine schulartenübergreifende Nummerierung der Ausbildungsjahre ist, beginnend mit „1“ für das 1. Grundschuljahr und „0“ für die Vorschulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>status</p></td>
    <td colspan="4"><p>mit der Angabe über den Schülerstatus in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„o“</p></td>
    <td colspan="2"><p>für ordentliche Schülerinnen und Schüler</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„a“</p></td>
    <td colspan="2"><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 4 Abs. 2 lit. a SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„b“</p></td>
    <td colspan="2"><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus dem Grund der Ablegung einer Einstufungsprüfung nicht zulässig ist (§ 4 Abs. 2 lit. b SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„c“</p></td>
    <td colspan="2"><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 3 Abs. 1 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„d“</p></td>
    <td colspan="2"><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus anderen Gründen nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td><p>ao-von</p></td>
    <td colspan="4"><p>Mit dem Datum des Beginns im Falle eines außerordentlichen Status (status ≠ „o“)</p></td>
  </tr>
  <tr>
    <td><p>ao-bis</p></td>
    <td colspan="4"><p>Mit dem Datum der Beendigung im Falle eines außerordentlichen Status (status ≠ „o“), wenn zutreffend</p></td>
  </tr>
  <tr>
    <td><p>fortsetzung</p></td>
    <td colspan="4"><p>mit der Information über die Berechtigung hinsichtlich des Fortsetzens der Ausbildung mit folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„bf“</p></td>
    <td colspan="2"><p>bei unterjährigem Fortsetzen der Schulstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ba“</p></td>
    <td colspan="2"><p>berechtigt zum Aufsteigen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„bw“</p></td>
    <td colspan="2"><p>berechtigt zum Wiederholen der Schulstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„nf“</p></td>
    <td colspan="2"><p>nicht berechtigt zum Fortsetzen der Ausbildung</p></td>
  </tr>
  <tr>
    <td><p>besuchsjahr</p></td>
    <td colspan="4"><p>mit der Angabe des (Besuchs-)Jahres in der betreffenden Ausbildung, in dem sich die Schülerin oder der Schüler zum Zeitpunkt der aktuellen Beendigung des Schulbesuchs befunden hat („1“ für das Schuljahr in dem diese Ausbildung begonnen wurde, „2“ im darauf folgenden Schuljahr, „3“ im dritten Schuljahr, in dem diese Ausbildung besucht wurde, und so fort; zurückliegende Schuljahre, die für die zulässige Höchstdauer des Schulbesuchs (§ 32 SchUG bzw. § 31 SchUG-BKV) nicht relevant sind, sind nicht zu berücksichtigen)</p></td>
  </tr>
  <tr>
    <td><p>uebersprung</p></td>
    <td colspan="4"><p>mit der Information, ob innerhalb der Ausbildung(sstufe) bereits eine Schulstufe übersprungen wurde (§ 26 SchUG); sofern zutreffend, Angabe der übersprungenen Schulstufe</p></td>
  </tr>
  <tr>
    <td><p>nost3ng</p></td>
    <td colspan="4"><p>mit der Information, ob die Berechtigung zum Aufsteigen mit drei „Nicht genügend“ oder Nichtbeurteilungen in der „Neuen Oberstufe“ (§ 25 Abs. 10 dritter Satz SchUG) in dieser Ausbildung bereits genutzt wurde; sofern zutreffend, ist das betreffende Schuljahr (im Format jjjj/jj) anzugeben</p></td>
  </tr>
  <tr>
    <td><p>sost2ng</p></td>
    <td colspan="4"><p>mit der Information, ob die Berechtigung zum Aufsteigen mit zwei „Nicht genügend“ oder Nichtbeurteilungen in der „semestrierten Oberstufe“ (§ 25 Abs. 10 Z 2 SchUG) in dieser Ausbildung bereits genutzt wurde; sofern zutreffend, ist das betreffende Schuljahr (im Format jjjj/jj) anzugeben</p></td>
  </tr>
  <tr>
    <td><p>7. Das Element zeugnis ist ein Kind-Element von „verlaufsdetails“, beinhaltet die Beurteilungen aus dem bzw. aus den an der meldenden Schule letztverfügbaren Jahreszeugnis (§ 22 SchUG), Semesterzeugnissen des jeweiligen Schuljahres (§ 22a SchUG, § 22a SchUG idF des Bundesgesetzes <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a>), letztere in Verbindung mit einem allfälligen Semesterprüfungszeugnis gemäß § 23b Abs. 6 bzw. § 23b Abs. 6 SchUG idF des Bundesgesetzes <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a> oder einem Zeugnis gemäß § 26b Abs. 4 bzw. § 26b Abs. 4 SchUG idF des Bundesgesetzes <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a>, Gesamtzeugnis (Zeugnis über sämtliche erfolgreich oder nicht erfolgreich abgeschlossenen Module gem. § 24 SchUG-BKV) bzw. aus der letzten Schulbesuchsbestätigung (§ 22 Abs. 11 SchUG; § 22a Abs. 7 SchUG, § 22a Abs. 7 SchUG idF des Bundesgesetzes <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a> bzw. § 24 Abs. 2 SchUG, soweit es sich um Beurteilungen über ein gesamtes Schuljahr bzw. Semester handelt) und weist folgende Attribute auf:Attribut</p></td>
    <td colspan="4"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="4"><p>mit der Angabe des Schuljahres auf das sich die folgende Beurteilung bezieht</p></td>
  </tr>
  <tr>
    <td><p>schulform</p></td>
    <td colspan="4"><p>mit der Schulformkennzahl dieser Ausbildung (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>gegenstandsart</p></td>
    <td colspan="4"><p>mit der Angabe zur Art des Gegenstandes, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td colspan="3"><p>für alternativen Pflichtgegenstand bzw. Wahlpflichtgegenstand</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td colspan="3"><p>für Freigegenstand</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„p“</p></td>
    <td colspan="3"><p>für (in der Stundentafel fix vorgegebenen) Pflichtgegenstand</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td colspan="3"><p>für Seminar</p></td>
  </tr>
  <tr>
    <td><p>gegenstand</p></td>
    <td colspan="4"><p>mit der Langbezeichnung des Gegenstandes aus der Stundentafel</p></td>
  </tr>
  <tr>
    <td><p>upis</p></td>
    <td colspan="4"><p>mit dem UPIS-Kürzel des Gegenstandes, soweit ein solches vergeben ist</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="4"><p>mit der betreffenden Schulstufe bzw. bei in Semestern gegliederten Ausbildungen das Semester und in Schulformen der „Neuen Oberstufe“ bzw. der semestrierten Oberstufe ab der 10. Schulstufe die Schulstufe samt Semester</p></td>
  </tr>
  <tr>
    <td><p>leistungsniveau</p></td>
    <td colspan="4"><p>mit Angabe des Leistungsniveaus der Beurteilung, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„k“</p></td>
    <td><p>keine Differenzierung nach Leistungsniveaus vorgesehen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„h“</p></td>
    <td><p>höheres Leistungsniveau (zB „Standard AHS“)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„n“</p></td>
    <td><p>niedrigeres Leistungsniveau (zB „Standard“)</p></td>
  </tr>
  <tr>
    <td><p>beurteilung</p></td>
    <td colspan="4"><p>mit der im Zeugnis ausgewiesenen Beurteilung dieses Gegenstandes, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="3"><p>für „Sehr gut“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="3"><p>für „Gut“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="3"><p>für „Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="3"><p>für „Genügend“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td colspan="3"><p>für „Nicht genügend“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„V“</p></td>
    <td colspan="3"><p>für eine verbale Beurteilung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„N“</p></td>
    <td colspan="3"><p>für „nicht beurteilt“</p></td>
  </tr>
</table>

8\. Das Element pruefung ist ein Kind-Element von „verlaufsdetails“, beinhaltet alle offenen Semesterprüfungen bzw. Kolloquien dieser Ausbildung sowie Wiederholungsprüfungen und Modulprüfungen, zu denen die Schülerin oder der Schüler noch antrittsberechtigt ist, und weist folgende Attribute auf:

<table>
  <tr>
    <td colspan="2"><p>Attribut</p></td>
    <td colspan="4"><p>Wert</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>gegenstandsart</p></td>
    <td colspan="4"><p>mit der Angabe zur Art des Gegenstandes, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td colspan="2"><p>„a“</p></td>
    <td colspan="2"><p>für alternativen Pflichtgegenstand bzw. Wahlpflichtgegenstand</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td colspan="2"><p>„f“</p></td>
    <td colspan="2"><p>für Freigegenstand</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td colspan="2"><p>„p“</p></td>
    <td colspan="2"><p>für (in der Stundentafel fix vorgegebenen) Pflichtgegenstand</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td colspan="2"><p>„s“</p></td>
    <td colspan="2"><p>für Seminar</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>gegenstand</p></td>
    <td colspan="4"><p>mit der Langbezeichnung des Gegenstandes aus der Stundentafel</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>upis</p></td>
    <td colspan="4"><p>mit dem UPIS-Kürzel des Gegenstandes, soweit ein solches vergeben ist</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>schulstufe</p></td>
    <td colspan="4"><p>mit der betreffenden Schulstufe bzw. bei in Semestern gegliederten Ausbildungen das Semester und in Schulformen der „Neuen Oberstufe“ bzw. der semestrierten Oberstufe ab der 10. Schulstufe die Schulstufe inkl. Semester</p></td>
  </tr>
  <tr>
    <td><p>pruefungsart</p></td>
    <td colspan="4"><p>mit der Angabe zur Art der Prüfung, in folgender Differenzierung:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„k“</p></td>
    <td colspan="2"><p>für Kolloqium (§ 23 SchUG-BKV)</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„m“</p></td>
    <td colspan="2"><p>für Modulprüfung (§ 23a SchUG-BKV)</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„s“</p></td>
    <td colspan="2"><p>für Semesterprüfung in der „Neuen Oberstufe“ (§ 23a SchUG idF <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a>), sofern „p“ nicht zutrifft, oder der semestrierten Oberstufe (§ 23a SchUG)</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„p“</p></td>
    <td colspan="2"><p>für Semesterprüfung in der „Neuen Oberstufe“ gemäß § 23a Abs. 3 3. Satz SchUG idF <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a></p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u“</p></td>
    <td colspan="3"><p>für Semesterprüfung über noch nicht besuchte Unterrichtsgegenstände in der „Neuen Oberstufe“ (§ 23b SchUG idF <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a>) oder der semestrierten Oberstufe (§ 23b SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„w“</p></td>
    <td colspan="2"><p>für Wiederholungsprüfung (§ 23 SchUG)</p></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="2"><p>antritt</p></td>
    <td colspan="4"><p>Anzahl der nicht erfolgreichen Prüfungsantritte (ggf. inkl. allfälliger Terminverluste infolge ungerechtfertigter Verhinderung)</p></td>
  </tr>
</table>

9\. Das Element schulpflichtverletzung ist ein Kind-Element von „schueler“, muss für jede Schülerin oder jeden Schüler, der die allgemeine Schulpflicht noch nicht erfüllt bzw. für die oder den Berufsschulpflicht besteht, einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| unentschTage | mit der Anzahl der unentschuldigten Fehltage im abgelaufenen Schuljahr (bei keinem unentschuldigten Fehltag ist hier „0“ anzugeben) |
| Verwarnungen | mit der Anzahl der Verwarnungen für unentschuldigte Fehltage im abgelaufenen Schuljahr (bei keiner Verwarnung ist hier „0“ anzugeben) |
| strafanz | mit der Anzahl der bisher von den besuchten Schulen erstatteten Strafanzeigen wegen Schulpflichtverletzung (bei keiner Erstattung ist hier „0“ anzugeben) |
