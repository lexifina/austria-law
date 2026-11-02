## Anlage 6

## zu § 17 Abs. 1, § 18 Abs. 2, § 19 Abs. 1, § 19a Abs. 1 und § 20 Abs. 1

## Teil I

## Daten der Schulen und der Testadministration für die individuellen Kompetenzerhebungen

1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1 Definition der Schnittstellen zwischen den Evidenzen gemäß § 5 BilDokG 2020 (lokalen Schulverwaltungsprogrammen) und der Datenbasis der individuellen Kompetenzerhebungen: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so ist eines der vom IQS vorgegebenen Formate zu verwenden.

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

1.3 Verweise auf Verordnungen sind wie folgt zu verstehen: „BistV“ = Verordnung über Bildungsstandards im Schulwesen, [BGBl. II Nr. 1/2009](<https://ogd.ris.bka.gv.at/eli/bgbl/II/2009/1>).

1.4 Die Verarbeitung der Daten gemäß Z 2 bis 7 erfolgt nach Maßgabe der technischen Möglichkeiten.

2\. Das Wurzel-Element kompetenzerhebungen muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| xmlns | mit dem Wert „kompetenzerhebungen\_schueler“ |
| meldedatum | mit dem Datum dieser Meldung |
| meldeart | mit „n“ für eine Neumeldung zu diesem Meldedurchgang (standard, überschreibt alle allfälligen bisherigen Meldungen dieser Schule zu diesem Meldedurchgang) |
| absender | mit der (Schul-)Kennzahl des Absenders |

3\. Das Element schule ist ein Kind-Element von „kompetenzerhebungen“, muss mindestens einmal pro Datenmeldung vorhanden sein (Schülerin oder Schüler von Exposituren, dislozierten Klassen uä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen zu melden) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten österreichischen Schulendatei) |

4\. Das Element schueler ist ein Kind-Element von „schule“, muss für die 3. und 4. Schulstufe sowie für die 7. und 8. Schulstufe für alle Schülerinnen und Schüler genau einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
|  |  |
| bPKBF | mit dem bereichsspezifischen Personenkennzeichen Bildung und Forschung gemäß § 9 E-GovG (wenn verfügbar) |
| vbPKAS | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik gemäß § 9 E-GovG (wenn verfügbar) |
| ersatz | mit der Ersatzkennung für die Schülerin oder den Schüler, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind, bzw. erst nach der ersten Datenmeldung verfügbar wurden |
| gebj | mit dem Jahr der Geburt der Schülerin oder des Schülers (Format JJJJ) |
| gebm | mit dem Monat der Geburt der Schülerin oder des Schülers (Format MM) |
| geschlecht | mit dem Geschlecht der Schülerin oder des Schülers („m“ für männlich, „w“ für weiblich, „x“ für divers, „o“ für offen, „i“ für inter und „k“, wenn von jeglicher Geschlechtsangabe abgesehen wurde) |
| staat | mit der Staatsangehörigkeit der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes) |
| erstsprache1 | mit der (ersten) Angabe zu der Sprache bzw. den Sprachen der Schülerin oder des Schülers, in der bzw. denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprache(n)“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache2 | mit der (gegebenenfalls) zweiten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache3 | mit der (gegebenenfalls) dritten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache1 | mit der (ersten) Angabe über die im Alltag regelmäßig gebrauchte(n) Sprache(n) der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache2 | mit der (gegebenenfalls) zweiten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache3 | mit der (gegebenenfalls) dritten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| spf | mit der Angabe, ob ein sonderpädagogischer Förderbedarf bescheidmäßig festgestellt ist („f“) bzw. bei noch laufenden Verfahren („v“), sonst „n“ |
| matrikel | für ein bildungseinrichtungsspezifisches Personenkennzeichen, |

5\. Das Element ausbildung ist ein Kind-Element von „schueler“, muss pro Schülerin oder pro Schüler und Datenmeldung einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="2"><p>mit der Angabe des laufenden Schuljahres</p></td>
  </tr>
  <tr>
    <td><p>schulform</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl dieser Ausbildung (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>klasse</p></td>
    <td colspan="2"><p>mit der (schulüblichen) Bezeichnung der besuchten (Stamm-)Klasse, wobei die erste Stelle numerisch ist und das Ausbildungsjahr dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="2"><p>mit der von der Schülerin oder vom Schüler besuchten Schulstufe, die eine schulartenübergreifende Nummerierung der Ausbildungsjahre ist, mit den Werten „3“ und „4“ für das 3. und 4. Grundschuljahr sowie „7“ und „8“ für die jeweiligen Schulstufen der Sekundarstufe I. Der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert</p></td>
  </tr>
  <tr>
    <td><p>status</p></td>
    <td colspan="2"><p>mit der Angabe über den Schülerstatus in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>für ordentliche Schülerinnen und Schüler</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 4 Abs. 2 lit. a SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus dem Grund der Ablegung einer Einstufungsprüfung nicht zulässig ist (§ 4 Abs. 2 lit. b SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 3 Abs. 1 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus anderen Gründen nicht zulässig ist</p></td>
  </tr>
</table>

6\. Das Element domaenen ist ein Kind-Element von „ausbildung“, muss genau einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| gruppe\_deutsch | mit der schulinternen Bezeichnung der Gruppe, in der die Schülerin oder der Schüler im Unterrichtsgegenstand Deutsch unterrichtet wird. Gibt es keine Gruppenteilungen, so ist hier die Klassenbezeichnung analog Z 5 (Element „ausbildung“) einzugeben |
| gruppe\_mathematik | mit der schulinternen Bezeichnung der Gruppe, in der die Schülerin oder der Schüler im Unterrichtsgegenstand Mathematik unterrichtet wird. Gibt es keine Gruppenteilungen, so ist hier die Klassenbezeichnung analog Z 5 (Element „ausbildung“) einzugeben |
| gruppe\_englisch | mit der schulinternen Bezeichnung der Gruppe, in der die Schülerin oder der Schüler im Unterrichtsgegenstand Englisch unterrichtet wird. Gibt es keine Gruppenteilungen, so ist hier die Klassenbezeichnung analog Z 5 (Element „ausbildung“) einzugeben; trifft nur auf Schülerinnen und Schüler der Schulstufen 7 und 8 zu. |

7\. Daten aus der Testadministration, die im Laufe der Durchführung der Kompetenzerhebungen und der Reflexionsgespräche in der Datenbasis des IQS verarbeitet werden:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="3"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>erhebungs-ID</p></td>
    <td colspan="3"><p>dient der Zuordnung der Testmaterialien und wird in der Datenbasis pro Schülerin und Schüler generiert</p></td>
  </tr>
  <tr>
    <td><p>modul</p></td>
    <td colspan="3"><p>mit der Angabe über das Modul der jeweiligen Kompetenzerhebung on folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>bd</p></td>
    <td colspan="2"><p>Basismodul Deutsch (Lesen)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>bm</p></td>
    <td colspan="2"><p>Basismodul Mathematik</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>be</p></td>
    <td colspan="2"><p>Basismodul Englisch (Rezeptive Fertigkeiten)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>zdv</p></td>
    <td colspan="2"><p>Zyklusmodul Deutsch (Verfassen von Texten, Textproduktion)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>zdh</p></td>
    <td colspan="2"><p>Zyklusmodul Deutsch (Zuhören)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>zes</p></td>
    <td colspan="2"><p>Zyklusmodul Englisch (Schreiben)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>fdl</p></td>
    <td colspan="2"><p>Fokusmodul Deutsch (Lesen leicht)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>em</p></td>
    <td colspan="2"><p>Ergänzende Module lt. Bezeichnung auf der Website des IQS (www.iqs.gv.at)</p></td>
  </tr>
  <tr>
    <td><p>datum</p></td>
    <td colspan="3"><p>Datum der Durchführung des jeweiligen Moduls der Kompetenzerhebung</p></td>
  </tr>
  <tr>
    <td><p>teilnahme</p></td>
    <td colspan="3"><p>mit der Angabe der Teilnahme bzw. Nichtteilnahme im jeweiligen Modul der Kompetenzerhebung in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„t“</p></td>
    <td><p>verpflichtende Teilnahme</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„f“</p></td>
    <td><p>freiwillige Teilnahme</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„n_ga“</p></td>
    <td><p>Nichtteilnahme, gerechtfertigt abwesend gemäß § 9 Abs. 3 SchPflG</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„n_f“</p></td>
    <td><p>Nichtteilnahme, freigestellt gemäß § 9 Abs. 6 SchPflG</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„n_ua“</p></td>
    <td><p>Nichtteilnahme, unentschuldigt abwesend</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„n_nsch“</p></td>
    <td><p>Nichtteilnahme, nicht mehr Schülerin oder Schüler dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„n_bist“</p></td>
    <td><p>Nichtteilnahme, Anwendung des § 1 Abs. 3 und 5 BistV</p></td>
  </tr>
  <tr>
    <td><p>lehrperson</p></td>
    <td colspan="3"><p>mit der Zuordnung einer Lehrerin oder eines Lehrers zur jeweiligen Gruppe/Klasse des jeweiligen Moduls der Kompetenzerhebung</p></td>
  </tr>
  <tr>
    <td><p>leistung</p></td>
    <td colspan="3"><p>Leistungsdaten der Schüler/innen im jeweiligen Modul der Kompetenzerhebung (Schülerantworten und deren Bewertungen)</p></td>
  </tr>
  <tr>
    <td><p>gespraech</p></td>
    <td colspan="3"><p>mit der Angabe „j“, wenn bis zum Stichtag das Gespräch durchgeführt wurde, „ke“, wenn das Gespräch aufgrund Nichtzustandekommen von Seiten der Erziehungsberechtigten nicht durchgeführt werden konnte und „ks“, wenn aus sonstigen Gründen das Gespräch nicht durchgeführt werden konnte</p></td>
  </tr>
</table>

## Teil II

### Daten der Übermittlungen durch die Leiterin oder den Leiter des IQS

1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1 Definition der Schnittstellen zwischen der Datenbasis der individuellen Kompetenzerhebungen am IQS und dem Bildungsinformationssystem der Bundesministerin oder des Bundesministers für Bildung: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so ist das von der Bundesministerin oder dem Bundesminister für Bildung vorgegebene Format zu verwenden.

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

1.3 Verweise auf Verordnungen sind wie folgt zu verstehen: „BistV“ = Verordnung über Bildungsstandards im Schulwesen, [BGBl. II Nr. 1/2009](<https://ogd.ris.bka.gv.at/eli/bgbl/II/2009/1>).

1.4 Die Verarbeitung der Daten gemäß Z 2 bis 6 erfolgt nach Maßgabe der technischen Möglichkeiten.

2\. Das Wurzel-Element kompetenzerhebungen muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| xmlns | mit dem Wert „kompetenzerhebungen\_schueler“ |
| meldedatum | mit dem Datum dieser Meldung |
| meldeart | mit „n“ für eine Neumeldung zu diesem Meldedurchgang (standard, überschreibt alle allfälligen bisherigen Meldungen dieser Schule zu diesem Meldedurchgang) |

3\. Das Element schule ist ein Kind-Element von „kompetenzerhebungen“, muss mindestens einmal pro Datenmeldung vorhanden sein (Schülerinnen oder Schüler von Exposituren, dislozierten Klassen uä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen auszuweisen) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, der die folgenden Daten zuzuordnen sind (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten österreichischen Schulendatei) |

4\. Das Element schueler ist ein Kind-Element von „schule“, muss für die 3. und 4. Schulstufe sowie für die 7. und 8. Schulstufe für alle Schülerinnen und Schüler genau einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| bPKBF | mit dem bereichsspezifischen Personenkennzeichen Bildung und Forschung gemäß § 9 E-GovG (wenn verfügbar) |
| vbPKAS | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik gemäß § 9 E-GovG (wenn verfügbar) |
| ersatz | mit der Ersatzkennung für die Schülerin oder den Schüler, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind, bzw. erst nach der ersten Datenmeldung verfügbar wurden. |
| gebj | mit dem Jahr der Geburt der Schülerin oder des Schülers (Format JJJJ) |
| gebm | mit dem Monat der Geburt der Schülerin oder des Schülers (Format MM) |
| geschlecht | mit dem Geschlecht der Schülerin oder des Schülers („m“ für männlich, „w“ für weiblich, „x“ für divers, „o“ für offen, „i“ für inter und „k“, wenn von jeglicher Geschlechtsangabe abgesehen wurde) |
| staat | mit der Staatsangehörigkeit der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes) |
| erstsprache1 | mit der (ersten) Angabe zu der Sprache bzw. den Sprachen der Schülerin oder des Schülers, in der bzw. denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprache(n)“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache2 | mit der (gegebenenfalls) zweiten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache3 | mit der (gegebenenfalls) dritten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache1 | mit der (ersten) Angabe über die im Alltag regelmäßig gebrauchte(n) Sprache(n) der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache2 | mit der (gegebenenfalls) zweiten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache3 | mit der (gegebenenfalls) dritten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| spf | mit der Angabe, ob ein sonderpädagogischer Förderbedarf bescheidmäßig festgestellt ist („f“) bzw. bei noch laufenden Verfahren („v“), sonst „n“ |
| matrikel | für ein bildungseinrichtungsspezifisches Personenkennzeichen, |

5\. Das Element ausbildung ist ein Kind-Element von „schueler“, muss pro Schülerin oder pro Schüler und Datenmeldung einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="2"><p>mit der Angabe des laufenden Schuljahres</p></td>
  </tr>
  <tr>
    <td><p>schulform</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl dieser Ausbildung (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>klasse</p></td>
    <td colspan="2"><p>mit der (schulüblichen) Bezeichnung der besuchten (Stamm-)Klasse, wobei die erste Stelle numerisch ist und das Ausbildungsjahr dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="2"><p>mit der von der Schülerin oder vom Schüler besuchten Schulstufe, die eine schulartenübergreifende Nummerierung der Ausbildungsjahre ist, mit den Werten „3“ und „4“ für das 3. und 4. Grundschuljahr sowie „7“ und „8“ für die jeweiligen Schulstufen der Sekundarstufe I. Der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert</p></td>
  </tr>
  <tr>
    <td><p>status</p></td>
    <td colspan="2"><p>mit der Angabe über den Schülerstatus in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>für ordentliche Schülerinnen und Schüler</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 4 Abs. 2 lit. a SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus dem Grund der Ablegung einer Einstufungsprüfung nicht zulässig ist (§ 4 Abs. 2 lit. b SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 3 Abs. 1 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus anderen Gründen nicht zulässig ist</p></td>
  </tr>
</table>

6\. Das Element ergebnis ist ein Kind-Element von „schueler“, muss pro Schülerin oder pro Schüler und Datenmeldung einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>modul</p></td>
    <td colspan="2"><p>mit der Angabe über das Modul der jeweiligen Kompetenzerhebung</p>
<p>bd – Basismodul Deutsch (Lesen)</p>
<p>bm – Basismodul Mathematik</p>
<p>be – Basismodul Englisch (Rezeptive Fertigkeiten)</p>
<p>zdv – Zyklusmodul Deutsch (Verfassen von Texten, Textproduktion)</p>
<p>zdh – Zyklusmodul Deutsch (Zuhören)</p>
<p>zes – Zyklusmodul Englisch (Schreiben)</p></td>
  </tr>
  <tr>
    <td><p>datum</p></td>
    <td colspan="2"><p>Datum der Durchführung des jeweiligen Moduls der Kompetenzerhebung</p></td>
  </tr>
  <tr>
    <td><p>teilnahme</p></td>
    <td colspan="2"><p>mit der Angabe der Teilnahme bzw. Nichtteilnahme im jeweiligen Modul der Kompetenzerhebung in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„t“</p></td>
    <td><p>verpflichtende Teilnahme</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td><p>freiwillige Teilnahme</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n_ga“</p></td>
    <td><p>Nichtteilnahme, gerechtfertigt abwesend gemäß § 9 Abs. 3 SchPflG</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n_f“</p></td>
    <td><p>Nichtteilnahme, freigestellt gemäß § 9 Abs. 6 SchPflG</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n_ua“</p></td>
    <td><p>Nichtteilnahme, unentschuldigt abwesend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n_nsch“</p></td>
    <td><p>Nichtteilnahme, nicht mehr Schülerin oder Schüler dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n_bist“</p></td>
    <td><p>Nichtteilnahme, Anwendung des § 1 Abs. 3 und 5 BistV</p></td>
  </tr>
  <tr>
    <td><p>ergebnis</p></td>
    <td colspan="2"><p>Mit der Angabe der erreichten Skalenpunkte gemäß IQS-Zyklus-Berichterstattung im jeweiligen Modul der Kompetenzerhebung</p></td>
  </tr>
  <tr>
    <td><p>gespraech</p></td>
    <td colspan="2"><p>mit der Angabe „j“, wenn bis zum Stichtag das Gespräch durchgeführt wurde, „ke“, wenn das Gespräch aufgrund Nichtzustandekommen von Seiten der Erziehungsberechtigten nicht durchgeführt werden konnte und „ks“, wenn aus sonstigen Gründen das Gespräch nicht durchgeführt werden konnte</p></td>
  </tr>
</table>
