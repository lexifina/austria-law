## Anlage 7

## zu § 22

## Daten hinsichtlich sozioökonomischer Faktoren

1\. Definition der Schnittstellen zwischen der Bundesanstalt „Statistik Österreich“ und der Datenbasis der Bundesministerin oder des Bundesministers für Bildung sowie jener der Leiterin oder des Leiters des IQS:

Als Schnittstelle für die Datenübermittlung fungiert eine CSV-Datei im Zeichensatzformat UTF-8.

2\. Die Attribute gemäß Z 3 bis 5 sind in folgenden Kategorien zu melden, sofern eine Re-Identifikation von Einzelpersonen ausgeschlossen ist:

2.1 Österreich gesamt, Bundesländer und Bildungsregionen

2.1.1 Schule gesamt

2.1.2 Schulart

2.1.3 Schulstufe

2.1.4 Schulstufe nach Schulart

2.2 Schule und gegebenenfalls Schulcluster

2.2.1 Schule und gegebenenfalls Schulcluster gesamt

2.2.2. Schulart

2.2.3 Schulstufe pro Schule, bei mehr als einer Schulart ist sowohl der Gesamtwert pro Schulstufe als auch der Wert pro Schulart anzugeben.

2.2.4 Klasse bzw. Schulstufe pro Schule bzw. nächsthöhere Ebene

3\. Sollte in den Kategorien gemäß Z 2 eine Re-Identifikation von Einzelpersonen nicht ausgeschlossen sein, so ist auf die nächsthöhere Aggregationsebene zu gehen.

4\. Für die Kategorien gemäß 2.1 sind folgende Attribute und Werte zu verwenden:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="3"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>bl</p></td>
    <td colspan="3"><p>mit der Bezeichnung für das Bundesland, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td colspan="2"><p>Österreich gesamt</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Burgenland</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Kärnten</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Niederösterreich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Oberösterreich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td colspan="2"><p>Salzburg</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„6“</p></td>
    <td colspan="2"><p>Steiermark</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„7“</p></td>
    <td colspan="2"><p>Tirol</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„8“</p></td>
    <td colspan="2"><p>Vorarlberg</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„9“</p></td>
    <td colspan="2"><p>Wien</p></td>
  </tr>
  <tr>
    <td><p>b_reg</p></td>
    <td colspan="3"><p>mit der Bezeichnung für die Bildungsregion (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Liste der Bildungsregionen)</p></td>
  </tr>
  <tr>
    <td><p>sart</p></td>
    <td colspan="3"><p>mit der Bezeichnung für die Schulart, in folgenden Ausprägungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„vs_p“</p></td>
    <td><p>Volksschule nur Primarstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„vs_s“</p></td>
    <td><p>Volksschule nur Sekundarstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„vs“</p></td>
    <td><p>Volksschule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ms“</p></td>
    <td><p>Mittelschule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„so_p“</p></td>
    <td><p>Sonderschule nur Primarstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„so_si“</p></td>
    <td><p>Sonderschule nur Sekundarstufe I</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„so“</p></td>
    <td><p>Sonderschule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„pts“</p></td>
    <td><p>Polytechnische Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ahs“</p></td>
    <td><p>Allgemeinbildende höhere Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ahs_u“</p></td>
    <td><p>Allgemeinbildende höhere Schule nur Unterstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ahs_o“</p></td>
    <td><p>Allgemeinbildende höhere Schule nur Oberstufe inkl. Oberstufenrealgymnasium</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ahs_lf“</p></td>
    <td><p>Allgemeinbildende höhere Schule nur Oberstufe ohne Oberstufenrealgymnasium (Langform)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ahs_org“</p></td>
    <td><p>Allgemeinbildende höhere Schule nur Oberstufenrealgymnasium</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„bs“</p></td>
    <td><p>Berufsschule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„bms“</p></td>
    <td><p>Berufsbildende mittlere Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„bhs“</p></td>
    <td><p>Berufsbildende höhere Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„bmhs“</p></td>
    <td><p>Berufsbildende mittlere und höhere Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„statut“</p></td>
    <td><p>Schule mit eigenem Organisationsstatut</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="3"><p>mit der Schulstufe, die eine schulartenübergreifende Nummerierung der Ausbildungsjahre ist, beginnend mit „1“ für das 1. Grundschuljahr und „0“ für die Vorschulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
</table>

5\. Für die Kategorien gemäß 2.2 sind zusätzlich folgende Attribute und Werte zu verwenden:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten österreichischen Schulendatei) |
| oe-pr | mit der Angabe der Information, ob es sich um eine öffentliche „oe“ oder private „pr“ Schule handelt |
| klasse | mit der (schulüblichen) Bezeichnung der (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe |
| schulart\_modus | mit der Angabe der überwiegenden Schulart |

6\. Folgende Attribute und Werte sind insofern zutreffend für jede Kategorie zu melden.

6.1 Es sind jeweils die Anzahlen und Anteile pro Kategorie anzugeben, Ausnahmen sind gesondert angeführt, fehlende Werte sind gesondert anzugeben.

6.2 Unter Bezugspersonen werden jene Personen verstanden, die aufgrund statistischer Verfahren einer Schülerin oder einem Schüler als „mit einer hohen Wahrscheinlichkeit ermittelte“ Erziehungsberechtigte zugeordnet werden können. Direkte Ableitungen von leiblichen Eltern bzw. Erziehungsberechtigten sind in der Datenbasis der Bundesanstalt „Statistik Österreich“ nicht möglich. Als erste Bezugsperson (b1) wird, falls vorhanden, bevorzugt die weibliche Bezugsperson bezeichnet, als zweite Bezugsperson (b2), falls vorhanden, bevorzugt die männliche Bezugsperson. Sollten zwei gleichgeschlechtliche Bezugspersonen ermittelt werden, sind diese ebenfalls abgebildet. Kann eine Bezugsperson (b1 oder b2) oder können beide Bezugspersonen (b1 und b2) nicht ermittelt werden, sind diese unter den fehlenden Werten anzugeben. Werden bei Attributen Angaben zu beiden Bezugspersonen gefordert, hat bei Vorhandensein nur einer Bezugsperson die Angabe nur zu dieser zu erfolgen.

6.3 Es sind ausschließlich Daten von Schulformen gemäß SchUG (nicht gemäß SchUG-BKV) zu melden.

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="5"><p>Wert</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>schueler</p></td>
    <td colspan="5"><p>mit der Angabe der Anzahl an Schülerinnen und Schüler gesamt, hier ist kein Anteil zu melden</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>sprache</p></td>
    <td colspan="5"><p>mit der oder den im Alltag gebrauchten Sprache(n) der Schülerinnen und Schüler in folgenden Ausprägungen gemäß Anlage 1 Z 4 Merkmale alltagssprache1 bis alltagssprache3</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„1“</p></td>
    <td colspan="3"><p>Angabe ausschließlich Deutsch</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„2“</p></td>
    <td colspan="3"><p>Angabe Deutsch sowie eine oder mehrere andere Sprache(n)</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„3“</p></td>
    <td colspan="3"><p>Angabe kein Deutsch</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>migrationshintergrund</p></td>
    <td colspan="5"><p>mit der Angabe der Schülerinnen und Schüler, deren beide Bezugspersonen nicht in Österreich geboren wurden.</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>zuzug</p></td>
    <td colspan="5"><p>mit der Angabe der Schülerinnen und Schüler, die im letzten Jahr „1“, in den letzten beiden Jahren „2“ oder in den letzten 5 Jahren „5“ aus dem Ausland zugezogen sind</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>gebland</p></td>
    <td colspan="5"><p>mit der Angabe des Geburtslands der Schülerinnen und Schüler, in folgender Ausprägung:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„oe“</p></td>
    <td colspan="3"><p>Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„eu“</p></td>
    <td colspan="3"><p>Land der Europäischen Union, ohne „oe“</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„int“</p></td>
    <td colspan="3"><p>Land außerhalb der Europäischen Union</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>haushalt</p></td>
    <td colspan="5"><p>mit der Angabe der durchschnittlichen Haushaltsgröße (arithmetisches Mittel und Median), hier sind keine Anzahlen und Anteile anzugeben</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>bezugsperson0</p></td>
    <td colspan="5"><p>Schülerinnen und Schüler, für die keine Bezugsperson ermittelt werden konnte</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>bezugsperson_1</p></td>
    <td colspan="5"><p>Schülerinnen und Schüler, für die die erste Bezugsperson ermittelt werden konnte</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="5"></td>
    <td></td>
  </tr>
  <tr>
    <td><p>bezugsperson_2</p></td>
    <td colspan="5"><p>Schülerinnen und Schüler, für die die zweite Bezugsperson ermittelt werden konnte</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="5"></td>
    <td></td>
  </tr>
  <tr>
    <td><p>bezugsperson_1_2</p></td>
    <td colspan="5"><p>Schülerinnen und Schüler, für die zwei Bezugspersonen ermittelt werden konnten</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="5"></td>
    <td></td>
  </tr>
  <tr>
    <td><p>bildung_b1</p></td>
    <td colspan="5"><p>höchste abgeschlossene Ausbildung der ersten Bezugsperson, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="4"><p>„ps“</p></td>
    <td><p>maximal Pflichtschule</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="4"><p>„le“</p></td>
    <td><p>Lehre, berufsbildende mittlere Schule</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="4"><p>„ma“</p></td>
    <td><p>Höhere Schule, Berufsreifeprüfung, Kolleg</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="4"><p>„hs“</p></td>
    <td><p>Hochschule, Akademie</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>bildung_b2</p></td>
    <td colspan="5"><p>höchste abgeschlossene Ausbildung der zweiten Bezugsperson, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„ps“</p></td>
    <td colspan="2"><p>maximal Pflichtschule</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„le“</p></td>
    <td colspan="2"><p>Lehre, berufsbildende mittlere Schule</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„ma“</p></td>
    <td colspan="2"><p>Höhere Schule, Berufsreifeprüfung, Kolleg</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„hs“</p></td>
    <td colspan="2"><p>Hochschule, Akademie</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>bildung_b1_b2</p></td>
    <td colspan="5"><p>höchste abgeschlossene Ausbildung der ersten und zweiten Bezugsperson</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„ngp“</p></td>
    <td colspan="2"><p>Bezugspersonen haben unterschiedlichen Abschluss, eine Bezugsperson hat maximal Pflichtschule</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„ng“</p></td>
    <td colspan="2"><p>Bezugspersonen haben unterschiedlichen Abschluss, aber nicht „ngp“</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„ps“</p></td>
    <td colspan="2"><p>maximal Pflichtschule</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„le“</p></td>
    <td colspan="2"><p>Lehre, berufsbildende mittlere Schule</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„ma“</p></td>
    <td colspan="2"><p>Höhere Schule, Berufsreifeprüfung, Kolleg</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„hs“</p></td>
    <td colspan="2"><p>Hochschule, Akademie</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>urbanisierungsgrad</p></td>
    <td colspan="5"><p>mit der Angabe des Grads der Urbanisierung des Schulstandorts nach der Klassifikation der Europäischen Kommission</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>urb_rur_typ</p></td>
    <td colspan="5"><p>mit der Angabe der Urban-Rural-Typologie der Statistik Austria des Schulstandorts mit den Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td><p>101</p></td>
    <td colspan="5"><p>Urbane Großzentren</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>102</p></td>
    <td colspan="5"><p>Urbane Mittelzentren</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>103</p></td>
    <td colspan="5"><p>Urbane Kleinzentren</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>210</p></td>
    <td colspan="5"><p>Regionale Zentren, zentral</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>220</p></td>
    <td colspan="5"><p>Regionale Zentren, intermediär</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>310</p></td>
    <td colspan="5"><p>Ländlicher Raum im Umland von Zentren, zentral</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>320</p></td>
    <td colspan="5"><p>Ländlicher Raum im Umland von Zentren, intermediär</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>330</p></td>
    <td colspan="5"><p>Ländlicher Raum im Umland von Zentren, peripher</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>410</p></td>
    <td colspan="5"><p>Ländlicher Raum, zentral</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>420</p></td>
    <td colspan="5"><p>Ländlicher Raum, intermediär</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>430</p></td>
    <td colspan="5"><p>Ländlicher Raum, peripher</p></td>
  </tr>
  <tr>
    <td><p>schueler_bpk_ermittelt</p></td>
    <td colspan="5"><p>Schülerinnen und Schüler, für die ein bPK-AS ermittelt werden konnte</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>einkommen_b1</p></td>
    <td colspan="5"><p>mit der Angabe der Einkommensklassifikation der ersten Bezugsperson relativ zu allen Einkommen der ermittelten Bezugspersonen österreichweit; in folgenden Ausprägungen</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q20“</p></td>
    <td colspan="3"><p>20 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q25“</p></td>
    <td colspan="3"><p>25 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q50“</p></td>
    <td colspan="3"><p>Median</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q75“</p></td>
    <td colspan="3"><p>75 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>einkommen_b2</p></td>
    <td colspan="5"><p>mit der Angabe der Einkommensklassifikation der zweiten Bezugsperson relativ zu allen Einkommen der ermittelten Bezugspersonen österreichweit; in folgenden Ausprägungen</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q20“</p></td>
    <td colspan="3"><p>20 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q25“</p></td>
    <td colspan="3"><p>25 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q50“</p></td>
    <td colspan="3"><p>Median</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q75“</p></td>
    <td colspan="3"><p>75 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>einkommen_b1_b2</p></td>
    <td colspan="5"><p>mit der Angabe der Einkommensklassifikation beider Bezugspersonen relativ zu allen Einkommen der ermittelten Bezugspersonen österreichweit; in folgenden Ausprägungen</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q20“</p></td>
    <td colspan="3"><p>20 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q25“</p></td>
    <td colspan="3"><p>25 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q50“</p></td>
    <td colspan="3"><p>Median</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„q75“</p></td>
    <td colspan="3"><p>75 %-Quantil</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>erw_status_b1</p></td>
    <td colspan="5"><p>Angaben zur Erwerbstätigkeit der ersten Bezugsperson, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u_v“</p></td>
    <td colspan="3"><p>unselbständige Erwerbsperson, beschäftigt in Vollzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„s_v“</p></td>
    <td colspan="3"><p>selbständige Erwerbsperson, beschäftigt in Vollzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u_t“</p></td>
    <td colspan="3"><p>unselbständige Erwerbsperson, beschäftigt in Teilzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„e_a“</p></td>
    <td colspan="3"><p>Erwerbsperson, arbeitslos</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„r“</p></td>
    <td colspan="3"><p>Nicht-Erwerbsperson, im Ruhestand/Pension</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„s“</p></td>
    <td colspan="3"><p>Nicht-Erwerbsperson, Studierende, Schülerin oder Schüler</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„so“</p></td>
    <td colspan="3"><p>sonstige Nicht-Erwerbsperson und sonstige arbeitslose Person</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>erw_status_b2</p></td>
    <td colspan="5"><p>Angaben zur Erwerbstätigkeit der zweiten Bezugsperson, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u_v“</p></td>
    <td colspan="3"><p>unselbständige Erwerbsperson, beschäftigt in Vollzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„s_v“</p></td>
    <td colspan="3"><p>selbständige Erwerbsperson, beschäftigt in Vollzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u_t“</p></td>
    <td colspan="3"><p>unselbständige Erwerbsperson, beschäftigt in Teilzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„a“</p></td>
    <td colspan="3"><p>Erwerbsperson, arbeitslos</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„r“</p></td>
    <td colspan="3"><p>Nicht-Erwerbsperson, im Ruhestand/Pension</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„s“</p></td>
    <td colspan="3"><p>Nicht-Erwerbsperson, Studierende, Schülerin oder Schüler</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„so“</p></td>
    <td colspan="3"><p>sonstige Nicht-Erwerbsperson und sonstige arbeitslose Person</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>erw_status_b1_b2</p></td>
    <td colspan="5"><p>Angaben zur Erwerbstätigkeit beider Bezugspersonen, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u“</p></td>
    <td colspan="3"><p>Unterschiedlich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u_v“</p></td>
    <td colspan="3"><p>unselbständige Erwerbsperson, beschäftigt in Vollzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„s_v“</p></td>
    <td colspan="3"><p>selbständige Erwerbsperson, beschäftigt in Vollzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u_t“</p></td>
    <td colspan="3"><p>unselbständige Erwerbsperson, beschäftigt in Teilzeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„a“</p></td>
    <td colspan="3"><p>Erwerbspersonen, alle arbeitslos</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„r“</p></td>
    <td colspan="3"><p>Nicht-Erwerbsperson, alle im Ruhestand/Pension</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„s“</p></td>
    <td colspan="3"><p>Nicht-Erwerbsperson, alle Studierende, Schülerin oder Schüler</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„so“</p></td>
    <td colspan="3"><p>alle sonstigen Nicht-Erwerbspersonen und sonstigen arbeitslosen Personen</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>erw_tage_b1</p></td>
    <td colspan="5"><p>mit der Angabe der Anzahl der Tage in Erwerbstätigkeit im Zeitraum eines Jahres der ersten Bezugsperson in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>0</p></td>
    <td colspan="3"><p>Null Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>1_bis_364</p></td>
    <td colspan="3"><p>1 bis 364 Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>365</p></td>
    <td colspan="3"><p>365 Tage (auch in Schaltjahren) in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>erw_tage_b2</p></td>
    <td colspan="5"><p>mit der Angabe der Anzahl der Tage in Erwerbstätigkeit im Zeitraum eines Jahres der zweiten Bezugsperson in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>0</p></td>
    <td colspan="3"><p>Null Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>1_bis_364</p></td>
    <td colspan="3"><p>1 bis 364 Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>365</p></td>
    <td colspan="3"><p>365 Tage (auch in Schaltjahren) in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>erw_tage_b1_b2</p></td>
    <td colspan="5"><p>mit der Angabe der Anzahl der Tage in Erwerbstätigkeit im Zeitraum eines Jahres beider Bezugspersonen; in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>0</p></td>
    <td colspan="3"><p>Null Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>1_bis_364</p></td>
    <td colspan="3"><p>1 bis 364 Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>365</p></td>
    <td colspan="3"><p>365 Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>366 bis 729</p></td>
    <td colspan="3"><p>366 bis 729 Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>730</p></td>
    <td colspan="3"><p>730 Tage in Erwerbstätigkeit</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>epinc20</p></td>
    <td colspan="5"><p>mit der Angabe des Anteils des Äquivalenzeinkommens, die unter dem unteren Quintil liegen</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>epinc20_KI_u</p></td>
    <td colspan="5"><p>mit der Angabe des unteren Werts des epinc20 zugehörigen Konfidenzinterwalls</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>epinc20_KI_o</p></td>
    <td colspan="5"><p>mit der Angabe des oberen Werts des epinc20 zugehörigen Konfidenzinterwalls</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>epinc_na</p></td>
    <td colspan="5"><p>mit der Angabe der fehlenden Werte für das Äquivalenzeinkommen</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>gebland_b1</p></td>
    <td colspan="5"><p>mit der Angabe des Geburtslands der ersten Bezugsperson, in folgender Ausprägung:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe“</p></td>
    <td colspan="2"><p>Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„eu“</p></td>
    <td colspan="2"><p>Land der Europäischen Union, ohne „oe“</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„int“</p></td>
    <td colspan="2"><p>Land außerhalb der Europäischen Union</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>gebland_b2</p></td>
    <td colspan="5"><p>mit der Angabe des Geburtslands der zweiten Bezugsperson, in folgender Ausprägung:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe“</p></td>
    <td colspan="2"><p>Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„eu“</p></td>
    <td colspan="2"><p>Land der Europäischen Union, ohne „oe“</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„int“</p></td>
    <td colspan="2"><p>Land außerhalb der Europäischen Union</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>gebland_b1_b2</p></td>
    <td colspan="5"><p>mit der Angabe der Geburtsländer beider Bezugspersonen, in folgender Ausprägung:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe“</p></td>
    <td colspan="2"><p>beide Bezugspersonen haben Österreich als Geburtsland</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„uoe“</p></td>
    <td colspan="2"><p>unterschiedliche Geburtsländer, eines davon Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„noe“</p></td>
    <td colspan="2"><p>keine Bezugsperson hat als Geburtsland Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>gebland_s_b1_b2</p></td>
    <td colspan="5"><p>mit der Angabe der Geburtsländer der Schülerin oder des Schülers sowie der Bezugspersonen, in folgender Ausprägung:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe“</p></td>
    <td colspan="2"><p>Die Schülerin und beide Bezugspersonen haben Österreich als Geburtsland</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe1“</p></td>
    <td colspan="2"><p>Die Schülerin und eine Bezugsperson haben Österreich als Geburtsland</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„mig1“</p></td>
    <td colspan="2"><p>Die Schülerin oder der Schüler und keine Bezugsperson hat als Geburtsland Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„mig2“</p></td>
    <td colspan="2"><p>Die Schülerin oder der Schüler hat als Geburtsland Österreich und keine Bezugsperson hat als Geburtsland Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>migx</p></td>
    <td colspan="2"><p>Das Geburtsland der Schülerin bzw. des Schülers ist unbekannt und keine Bezugsperson hat als Geburtsland Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>mig</p></td>
    <td colspan="2"><p>Das Geburtsland der Schülerin bzw. des Schülers ist unbekannt und zumindest eine Bezugsperson hat als Geburtsland Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>staat_b1</p></td>
    <td colspan="5"><p>mit der Angabe der Staatsbürgerschaft der ersten Bezugsperson, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe“</p></td>
    <td colspan="2"><p>Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„eu“</p></td>
    <td colspan="2"><p>Land der Europäischen Union, ohne „oe“</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„int“</p></td>
    <td colspan="2"><p>Land außerhalb der Europäischen Union</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>staat_b2</p></td>
    <td colspan="5"><p>mit der Angabe der Staatsbürgerschaft der zweiten Bezugsperson, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe“</p></td>
    <td colspan="2"><p>Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„eu“</p></td>
    <td colspan="2"><p>Land der Europäischen Union, ohne „oe“</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„int“</p></td>
    <td colspan="2"><p>Land außerhalb der Europäischen Union</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>oe_b1_b2</p></td>
    <td colspan="5"><p>mit der Angabe, ob eine oder beide Bezugspersonen die österreichische Staatsbürgerschaft besitzt bzw. besitzen, in folgenden Ausprägungen:</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„oe“</p></td>
    <td colspan="2"><p>beide Bezugspersonen: Österreichische Staatsbürgerschaft</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„uoe“</p></td>
    <td colspan="2"><p>unterschiedliche Staatsbürgerschaften, eine davon Österreich</p></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„noe“</p></td>
    <td colspan="2"><p>keine Bezugsperson hat die österreichische Staatsbürgerschaft</p></td>
    <td></td>
  </tr>
  <tr>
    <td><p>vollst_vorh</p></td>
    <td colspan="5"><p>mit der Angabe der Schülerinnen und Schüler für die alle Teilkomponenten der Ermittlung der sozioökonomischen Ausgangslage vorhanden sind.</p></td>
    <td></td>
  </tr>
</table>
