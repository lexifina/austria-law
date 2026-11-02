## Anlage 2

## zu § 7

## Daten der Schulen für die für Zwecke der Bundesstatistik zum Bildungswesen

- 1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1 Definition der Schnittstellen zwischen den Schulen und der Bundesanstalt „Statistik Österreich“: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so ist eines der von der Bundesanstalt „Statistik Österreich“ vorgegebenen Formate zu verwenden.

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

- 2\. Das Wurzel-Element bildungsdokumentation muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>xmlns</p></td>
    <td><p>mit dem Wert „bildungsdokumentation_schueler“</p></td>
  </tr>
  <tr>
    <td><p>meldedatum</p></td>
    <td><p>mit dem Datum dieser Meldung</p></td>
  </tr>
  <tr>
    <td rowspan="2"><p>meldeart</p></td>
    <td><p>mit „n“ für eine Neumeldung zu diesem Meldedurchgang (standard, überschreibt alle allfälligen bisherigen Meldungen dieser Schule zu diesem Meldedurchgang)</p></td>
  </tr>
  <tr>
    <td><p>mit „e“ für die Ergänzung zusätzlicher Informationen</p></td>
  </tr>
  <tr>
    <td><p>absender</p></td>
    <td><p>mit der (Schul-)Kennzahl des Absenders</p></td>
  </tr>
</table>

- 3\. Das Element schule ist ein Kind-Element von „bildungsdokumentation“, muss mindestens einmal pro Datenmeldung vorhanden sein (Schülerinnen oder Schüler von Exposituren, dislozierten Klassen u. ä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen zu melden) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten österreichischen Schulendatei) |

- 4\. Das Element schueler ist ein Kind-Element von „schule“, muss mindestens einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| vbPKBF | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Bildung und Forschung gemäß § 9 E-GovG (wenn verfügbar) |
| vbPKAS | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik gemäß § 9 E-GovG (wenn verfügbar) |
| svnr | bis zur Ausstattung mit bPK mit der Sozialversicherungsnummer der Schülerin oder des Schülers (wenn verfügbar) |
| ersatz | mit der Ersatzkennung für die Schülerin oder den Schüler, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind bzw. bis zur Ausstattung mit bPK, wenn die Sozialversicherungsnummer („svnr“) nicht verfügbar ist |
| gebdat | mit dem Geburtsdatum der Schülerin oder des Schülers |
| geschlecht | mit dem Geschlecht der Schülerin oder des Schülers („m“ für männlich, „w“ für weiblich, „x“ für divers, „o“ für offen, „i“ für inter und „k“, wenn von jeglicher Geschlechtsangabe abgesehen wurde) |
| staat | mit der Staatsangehörigkeit der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Staatencodes) |
| erstsprache1 | mit der (ersten) Angabe zu der Sprache bzw. den Sprachen der Schülerin oder des Schülers, in der bzw. denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprache(n)“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache2 | mit der (gegebenenfalls) zweiten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache3 | mit der (gegebenenfalls) dritten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache1 | mit der (ersten) Angabe über die im Alltag regelmäßig gebrauchte(n) Sprache(n) der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache2 | mit der (gegebenenfalls) zweiten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache3 | mit der (gegebenenfalls) dritten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| spf | mit der Angabe, ob ein sonderpädagogischer Förderbedarf bescheidmäßig festgestellt ist („f“) bzw. bei noch laufenden Verfahren („v“), sonst „n“ |
| integr-berufsausb | mit der Angabe, ob eine Inanspruchnahme einer Ausbildung gemäß § 11a Abs. 1 oder § 11b Abs. 1 des Land- und forstwirtschaftliches Berufsausbildungsgesetzes, [BGBl. Nr. 298/1990](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1990_298_0/1990_298_0.pdf>), in der Fassung [BGBl. I Nr. 157/2013](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2013/157>), vorliegt, sonst „n“. Angabe „v“ für die „verlängerte Lehre“ und „t“ für die „Teilqualifikation“ |
| plz | mit der Postleitzahl der Heimatadresse der Schülerin oder des Schülers, bei einer Auslandsadresse Eintrag des Postleitzahlen-Ersatzcodes nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Verzeichnisses der Staatencodes |
| ort | mit der Bezeichnung des Ortes der Heimatadresse der Schülerin oder des Schülers |
| zusatzort | mit der Kennung „j“, wenn eine zusätzliche Wohnadresse am Bildungsort besteht, sonst „n“ |
| matrikel | für ein bildungseinrichtungsspezifisches Personenkennzeichen |
| eingeschult | mit der Angabe des Kalenderjahres, in dem die Schülerin oder der Schüler in die erste Schulstufe bzw. als Schulpflichtige oder Schulpflichtiger in die Vorschulstufe eintrat (gegebenenfalls gemäß Rückrechnung nach dem SchPflG, zB bei Zuzug aus dem Ausland) |

- 5\. Das Element ausbildung ist ein Kind-Element von „schueler“, muss pro Schülerin oder pro Schüler und Datenmeldung einmal bzw. bei Wechsel der Ausbildung innerhalb der Schule zweimal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>beginn</p></td>
    <td colspan="2"><p>mit dem Datum des Beginns der laufenden bzw. – wenn beendet – letzten Ausbildung</p></td>
  </tr>
  <tr>
    <td><p>schulform</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl dieser Ausbildung (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei)</p></td>
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
    <td><p>„al“</p></td>
    <td><p>erfolgreich abgeschlossener Berufsschulbesuch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„as“</p></td>
    <td><p>erfolgreich abgeschlossen mit einer sonstigen abschließenden Prüfung</p></td>
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
    <td><p>„bl“</p></td>
    <td><p>vorzeitige Beendigung der Berufsschule infolge Beendigung des Lehrverhältnisses</p></td>
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
    <td><p>„bu“</p></td>
    <td><p>vorzeitige Beendigung der Ausbildung wegen ansonstiger Überschreitung der Höchstdauer</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bw“</p></td>
    <td><p>vorzeitige Beendigung der Ausbildung wegen nicht mehr zulässiger Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bz“</p></td>
    <td><p>sonstige nicht erfolgreiche Beendigung der Ausbildung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„eb“</p></td>
    <td><p>nicht abschließende Externistenprüfung bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„en“</p></td>
    <td><p>Externistenprüfung nicht bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ff“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung durch freiwillige Wiederholung der Schulstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fm“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden modularen Ausbildung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fn“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung in der nächsten Stufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fp“</p></td>
    <td><p>Fortsetzung der Ausbildung nach einem reinen Praxisjahr bzw. Praxissemester ohne Schulbesuch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fu“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung durch Überspringen einer Schulstufe bzw. eines Semesters</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fv“</p></td>
    <td><p>Fortsetzung des an der meldenden Schule bereits im vorangegangenen Schuljahr begonnenen Lehrganges, Kurses oder Ausbildungsjahres bzw. -semesters (bei schuljahresüberschneidender Ausbildungsorganisation)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fw“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung durch Wiederholung der Schulstufe bzw. des Semesters</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„kl“</p></td>
    <td><p>letztmalige Wiederholung einer Teilprüfung einer abschließenden Prüfung wurde nicht bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„kw“</p></td>
    <td><p>erste oder zweite Wiederholung einer Teilprüfung einer abschließenden Prüfung wurde nicht bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ne“</p></td>
    <td><p>Neueinstieg in die erste lehrplanmäßig vorgesehene Stufe bzw. das erste lehrplanmäßig vorgesehene Semester dieser Ausbildung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nf“</p></td>
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung durch freiwillige Wiederholung der Schulstufe bzw. des Semesters an dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ni“</p></td>
    <td><p>Neueinstieg in eine höhere Stufe bzw. ein höheres Semester dieser Ausbildung aus einer Schule im Ausland (Zuwanderung)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nm“</p></td>
    <td><p>Neueinstieg in die modulare Ausbildung an der meldenden Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nn“</p></td>
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung in der nächsten vorgesehenen Stufe an dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nq“</p></td>
    <td><p>Neueinstieg in eine höhere Stufe bzw. ein höheres Semester dieser Ausbildung infolge Übertritt aus einer anderen Ausbildung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nr“</p></td>
    <td><p>Anmeldung zum Schulbesuch während des Schuljahres</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nu“</p></td>
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung durch Überspringen einer Schulstufe bzw. eines Semesters an dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nw“</p></td>
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung durch Wiederholung der Schulstufe bzw. des Semesters an dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„up“</p></td>
    <td><p>Unterbrechung des Schulbesuchs für ein reines Praxisjahr bzw. Praxissemester ohne Schulbesuch</p></td>
  </tr>
  <tr>
    <td><p>ende</p></td>
    <td colspan="2"><p>mit dem Datum der Beendigung dieser Ausbildung (wenn zutreffend, dh. das Merkmal in „stand“ beginnt mit „a“ oder „b“ bzw. lautet „kl“)</p></td>
  </tr>
</table>

- 6\. Das Element ausbildungsdetails ist ein Kind-Element von „ausbildung“, muss genau einmal pro laufender Ausbildung (dh. der Wert des Attributes „stand“ in Z 5 beginnt mit „f“ oder „n“) vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="3"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="3"><p>mit der Angabe des laufenden Schuljahres</p></td>
  </tr>
  <tr>
    <td><p>semester</p></td>
    <td colspan="3"><p>bei nicht ganzjähriger Ausbildungsorganisation mit den Ausprägungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„w“</p></td>
    <td colspan="2"><p>für die Meldung zum Wintersemester</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td colspan="2"><p>für die Meldung zum Sommersemester</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td colspan="2"><p>für die Meldung zu einem unterjährigen Lehrgang</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>sonst „g“ für ganzjährige Ausbildungsorganisation</p></td>
  </tr>
  <tr>
    <td><p>klasse</p></td>
    <td colspan="3"><p>mit der (schulüblichen) Bezeichnung der besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe</p></td>
  </tr>
  <tr>
    <td><p>organisation</p></td>
    <td colspan="3"><p>mit der Information über die Art der Unterrichtsorganisation in dieser Klasse, in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td colspan="2"><p>für ganzjährig</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„h“</p></td>
    <td colspan="2"><p>für halbjährig (semesterweise)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td colspan="2"><p>für lehrgangsmäßig</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„m“</p></td>
    <td colspan="2"><p>für modular</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td colspan="2"><p>für saisonmäßig und</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„v“</p></td>
    <td colspan="2"><p>für verkürztes Unterrichtsjahr mit späterem Beginn</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="3"><p>mit der von der Schülerin oder vom Schüler besuchten Schulstufe, die eine schulartenübergreifende Nummerierung der Ausbildungsjahre ist, beginnend mit „1“ für das 1. Grundschuljahr und „0“ für die Vorschulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="3"><p>mit der Schulformkennzahl für die besuchte Ausbildung (Lehrplan) gemäß der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei</p></td>
  </tr>
  <tr>
    <td><p>status</p></td>
    <td colspan="3"><p>mit der Angabe über den Schülerstatus in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td colspan="2"><p>für ordentliche Schülerinnen und Schüler</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td colspan="2"><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td colspan="2"><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus dem Grund der Ablegung einer Einstufungsprüfung nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td colspan="2"><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td colspan="2"><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus anderen Gründen nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td><p>bilingual</p></td>
    <td colspan="3"><p>mit der Information, ob fremdsprachiger bzw. zweisprachiger Unterricht (Lebende Fremdsprache als Unterrichtssprache) besucht wird, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td colspan="2"><p>für durchgehend fremd- bzw. zweisprachigen Unterricht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td colspan="2"><p>für (praktisch) keinen fremd- bzw. zweisprachigen Unterricht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„t“</p></td>
    <td colspan="2"><p>für teilweise fremd- bzw. zweisprachigen Unterricht</p></td>
  </tr>
  <tr>
    <td><p>bilingualsprache</p></td>
    <td colspan="3"><p>mit der Angabe der Sprache gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Fremdsprachenverzeichnis</p></td>
  </tr>
  <tr>
    <td><p>deutschfoerderung</p></td>
    <td colspan="3"><p>mit der Information, ob und in welcher Form die Schülerin oder der Schüler Deutschförderung erhält, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„kdf“</p></td>
    <td><p>für keine Deutschfördermaßnahme</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„daz“</p></td>
    <td><p>für den Unterricht ordentlicher Schülerinnen und Schüler nach dem Lehrplan Deutsch sowie allfälligen Lehrplanzusätzen und didaktischen Grundsätzen für Deutsch als Zweitsprache</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„kl“</p></td>
    <td><p>für Unterricht in einer parallel zur Stammklasse geführten Deutschförderklasse</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„kli“</p></td>
    <td><p>für Unterricht in einer integrativen Deutschförderklasse</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ku“</p></td>
    <td><p>für Unterricht in einem parallel zur Stammklasse geführten Deutschförderkurs</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„kui“</p></td>
    <td><p>für Unterricht in einem integrativen Deutschförderkurs</p></td>
  </tr>
  <tr>
    <td><p>betreuung</p></td>
    <td colspan="3"><p>mit der Angabe, ob zum Stichtag ein Angebot einer schulischen Nachmittagsbetreuung bzw. der Betreuungsteil ganztägiger Schulformen von der Schülerin oder vom Schüler genutzt wird, samt Angabe der angemeldeten Tage, in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td colspan="2"><p>für keine Nutzung (bzw. kein Angebot)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>für Anmeldung/Nutzung für einen Tag pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>für Anmeldung/Nutzung für zwei Tage pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>für Anmeldung/Nutzung für drei Tage pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>für Anmeldung/Nutzung für vier Tage pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td colspan="2"><p>für Anmeldung/Nutzung für fünf Tage pro Woche</p></td>
  </tr>
  <tr>
    <td><p>betreuungsform</p></td>
    <td colspan="3"><p>mit der Angabe, ob bzw. welche Art der Betreuungsform besucht wird:</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„g“</p></td>
    <td><p>„getrennte“ Form</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„v“</p></td>
    <td><p>„verschränkte“ Form, nur möglich, wenn „betreuung“ = „5“</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„k“</p></td>
    <td><p>keine Betreuung, nur möglich, wenn „betreuung“ = „0“</p></td>
  </tr>
</table>

- 7\. Das Element erstsprachenunterricht ist ein Kind-Element von „ausbildungsdetails“, muss für jede Erstsprache, in der die Schülerin oder der Schüler im laufenden Schuljahr bzw. Semester in Form des „muttersprachlichen Unterrichts“ unterrichtet wird, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>fach</p></td>
    <td colspan="2"><p>mit der Angabe des Faches (Gegenstands) gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Sprachenverzeichnis</p></td>
  </tr>
  <tr>
    <td><p>gegenstandsart</p></td>
    <td colspan="2"><p>mit der Angabe der Art des Gegenstands, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fk“</p></td>
    <td><p>für Freigegenstand in Kursform; Eingabe nur ab 5. Schulstufe möglich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fi“</p></td>
    <td><p>für Freigegenstand in integrativer Form; Eingabe nur ab 5. Schulstufe möglich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„uk“</p></td>
    <td><p>für unverbindliche Übung in Kursform</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ui“</p></td>
    <td><p>für unverbindliche Übung in integrativer Form</p></td>
  </tr>
  <tr>
    <td><p>wochenstunden</p></td>
    <td colspan="2"><p>mit der Angabe der Wochenstunden dieses Gegenstands laut Stundentafel</p></td>
  </tr>
</table>

- 8\. Das Element schulerfolg ist ein Kind-Element von „ausbildung“, muss genau einmal pro Ausbildung einer Schülerin oder eines Schülers vorhanden sein, wenn diese Ausbildung nicht erst im aktuellen Jahrgang begonnen wurde (dh. der Wert des Attributes „stand“ in Z 5 beginnt nicht mit „n“) und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="2"><p>mit der Angabe des abgelaufenen Schuljahres, auf das sich diese Schulerfolgsmeldung bezieht</p></td>
  </tr>
  <tr>
    <td><p>semester</p></td>
    <td colspan="2"><p>bei nicht ganzjähriger Ausbildungsorganisation mit den Ausprägungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„w“</p></td>
    <td><p>für die Meldung zum Wintersemester</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td><p>für die Meldung zum Sommersemester</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td><p>für die Meldung zu einem unterjährigen Lehrgang,</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>sonst „g“ für ganzjährige Ausbildungsorganisation</p></td>
  </tr>
  <tr>
    <td><p>klasse</p></td>
    <td colspan="2"><p>mit der (schulüblichen) Bezeichnung der zuletzt besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe</p></td>
  </tr>
  <tr>
    <td><p>organisation</p></td>
    <td colspan="2"><p>mit der Information über die Art der Unterrichtsorganisation in dieser Klasse, in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>für ganzjährig</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„h“</p></td>
    <td><p>für halbjährig (semesterweise)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td><p>für lehrgangsmäßig</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„m“</p></td>
    <td><p>für modular</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td><p>für saisonmäßig und</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„v“</p></td>
    <td><p>für verkürztes Unterrichtsjahr mit späterem Beginn</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="2"><p>Mit der von der Schülerin oder vom Schüler in diesem Ausbildungsdurchgang besuchten Schulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl für diese Ausbildung (Lehrplan) gemäß der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei</p></td>
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
    <td><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus dem Grund der Ablegung einer Einstufungsprüfung nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus anderen Gründen nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td><p>deutschfoerderung</p></td>
    <td colspan="2"><p>mit der Information, ob und in welcher Form die Schülerin oder der Schüler Deutschförderung am Ende des abgelaufenen Schuljahres (bzw. Semesters oder Lehrganges) erhalten hat, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„kdf“</p></td>
    <td><p>für keine Deutschfördermaßnahme</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„daz“</p></td>
    <td><p>für den Unterricht ordentlicher Schülerinnen und Schüler nach dem Lehrplan Deutsch sowie allfälligen Lehrplanzusätzen und didaktischen Grundsätzen für Deutsch als Zweitsprache</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„kl“</p></td>
    <td><p>für Unterricht in einer parallel zur Stammklasse geführten Deutschförderklasse</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„kli“</p></td>
    <td><p>für Unterricht in einer integrativen Deutschförderklasse</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ku“</p></td>
    <td><p>für Unterricht in einem parallel zur Stammklasse geführten Deutschförderkurs</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„kui“</p></td>
    <td><p>für Unterricht in einem integrativen Deutschförderkurs</p></td>
  </tr>
  <tr>
    <td><p>jahreserfolg</p></td>
    <td colspan="2"><p>mit der Gesamtbeurteilung im letzten Jahreszeugnis (bzw. Semester- oder Lehrgangszeugnis) in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>für Beurteilung mit ausgezeichnetem Erfolg</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>für berechtigt zum Aufsteigen trotz negativer oder keiner Beurteilung an Schulen für Berufstätige</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit negativer Beurteilung in der ersten oder zweiten Schulstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td><p>für berechtigt zum Aufsteigen infolge eines fremdsprachigen Schulbesuchs im Ausland</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>für Beurteilung mit gutem Erfolg</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„h“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit „Nicht genügend“ nach Unterricht gemäß dem höheren Leistungsniveau</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit einem „Nicht genügend“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>für nicht berechtigt zum Aufsteigen oder nicht erfolgreichen Abschluss der letzten Schulstufe infolge negativer oder fehlender Beurteilung(en) – soweit nicht eine andere Merkmalsausprägung zutrifft</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>Für Schülerinnen und Schüler ohne Beurteilung des Schulerfolgs (außerordentliche Schülerinnen und Schüler, vorzeitige Abmeldung usw.)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„p“</p></td>
    <td><p>für berechtigt zum Aufsteigen oder erfolgreichen Abschluss der letzten Schulstufe mit positiver Beurteilung in allen Pflichtgegenständen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„r“</p></td>
    <td><p>für nicht berechtigt zum Aufsteigen oder nicht erfolgreichen Abschluss der letzten Schulstufe wegen nicht zurückgelegter Pflichtpraktika</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„w“</p></td>
    <td><p>für berechtigt zum Aufsteigen trotz negativer Beurteilung bei Wiederholung nach einem „Befriedigend“ in diesem Gegenstand</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„x“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit zwei „Nicht genügend“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„z“</p></td>
    <td><p>für keine Jahres- bzw. Semesterbeurteilung bei modularen Ausbildungen</p></td>
  </tr>
  <tr>
    <td><p>nichtgen</p></td>
    <td colspan="2"><p>mit der Anzahl der „Nicht genügend“ in Pflichtgegenständen (nach allfälligen Wiederholungs-, Nachtrags- oder Semesterprüfungen)</p></td>
  </tr>
  <tr>
    <td><p>wdhp-angetr</p></td>
    <td colspan="2"><p>mit der Zahl der Wiederholungs-, Nachtrags- oder Semesterprüfungen usw., zu denen die Schülerin oder der Schüler angetreten ist</p></td>
  </tr>
  <tr>
    <td><p>wdhp-bestand</p></td>
    <td colspan="2"><p>mit der Zahl der davon bestandenen Wiederholungs-, Nachtrags- oder Semesterprüfungen usw.</p></td>
  </tr>
  <tr>
    <td><p>wiederholung</p></td>
    <td colspan="2"><p>mit der Angabe bezüglich der Wiederholungsberechtigung, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>für aufstiegsberechtigt bzw. letzte Stufe erfolgreich abgeschlossen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>für berechtigt zum Wiederholen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>für nicht berechtigt zum Wiederholen</p></td>
  </tr>
</table>

- 9\. Das Element gegenstand ist ein Kind-Element von „schulerfolg“, muss für jede Fremdsprache, in der die Schülerin oder der Schüler im abgelaufenen Schuljahr bzw. Semester unterrichtet wurde, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>fach</p></td>
    <td colspan="2"><p>mit der Angabe des Faches (Gegenstands) gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Fremdsprachenverzeichnis</p></td>
  </tr>
  <tr>
    <td><p>sprachennr</p></td>
    <td colspan="2"><p>für die Angabe bei lebenden Fremdsprachen, ob es sich dabei um die 1., 2., 3., 4. (oder weitere) lebende Fremdsprache handelt („1“, „2“, „3“, „4“)</p></td>
  </tr>
  <tr>
    <td><p>pflichtig</p></td>
    <td colspan="2"><p>mit der Angabe zur Pflichtigkeit dieses Faches, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>für alternativen Pflichtgegenstand bzw. Wahlpflichtgegenstand</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td><p>für Freigegenstand</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„p“</p></td>
    <td><p>für (in der Stundentafel fix vorgegebenen) Pflichtgegenstand</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td><p>für Seminar</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„u“</p></td>
    <td><p>für unverbindliche Übung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„v“</p></td>
    <td><p>für verbindliche Übung</p></td>
  </tr>
</table>

- 10\. Das Element erstsprachenunterricht\_erfolg ist ein Kind-Element von „schulerfolg“, muss für jede Erstsprache, in der die Schülerin oder der Schüler im abgelaufenen Schuljahr bzw. Semester in Form des „muttersprachlichen Unterrichts“ unterrichtet wurde, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>fach</p></td>
    <td colspan="2"><p>mit der Angabe des Faches (Gegenstands) gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Sprachenverzeichnis</p></td>
  </tr>
  <tr>
    <td><p>gegenstandsart</p></td>
    <td colspan="2"><p>mit der Angabe der Art des Gegenstands, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fk“</p></td>
    <td><p>für Freigegenstand in Kursform; Eingabe nur ab 5. Schulstufe möglich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fi“</p></td>
    <td><p>für Freigegenstand in integrativer Form; Eingabe nur ab 5. Schulstufe möglich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„uk“</p></td>
    <td><p>für unverbindliche Übung in Kursform</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ui“</p></td>
    <td><p>für unverbindliche Übung in integrativer Form</p></td>
  </tr>
  <tr>
    <td><p>wochenstunden</p></td>
    <td colspan="2"><p>mit der Angabe der Wochenstunden dieses Gegenstands laut Stundentafel</p></td>
  </tr>
</table>

- 11\. Das Element leistungsbeurteilung ist ein Kind-Element von „schulerfolg“, muss für die Pflichtgegenstände Deutsch, (Angewandte) Mathematik, Englisch, Französisch, Italienisch, Spanisch, in der die Schülerin oder der Schüler im abgelaufenen Schuljahr bzw. Semester unterrichtet wurde, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>fach</p></td>
    <td colspan="2"><p>mit der Angabe des Faches (Gegenstands), in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>für den Pflichtgegenstand Deutsch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>für den Pflichtgegenstand Englisch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td><p>für den Pflichtgegenstand Französisch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td><p>für den Pflichtgegenstand Spanisch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„i“</p></td>
    <td><p>für den Pflichtgegenstand Italienisch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„m“</p></td>
    <td><p>für den Pflichtgegenstand (Angewandte) Mathematik</p></td>
  </tr>
  <tr>
    <td><p>beurteilung</p></td>
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufen (nach allfälligen Nachtrags-, Wiederholungs- und Semesterprüfungen), mit der Angabe „nicht beurteilt“ bei vorgetäuschten Leistungen, mit der Angabe, ob die Feststellungsprüfung gestundet wurde, bzw. mit der Angabe „ohne Beurteilung“, wenn eine alternative Leistungsbeurteilung, keine Beurteilung bei außerordentlichen Schülerinnen und Schülern oder keine Beurteilung bei Sonderschülerinnen und –schülern erfolgte, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td><p>Gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td><p>Genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td><p>Nicht genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>Nicht beurteilt</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>Gestundet</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>Ohne Beurteilung</p></td>
  </tr>
</table>

- 12\. Das Element abschlussdetails ist ein Kind-Element von „ausbildung“, muss dann genau einmal vorhanden sein, wenn diese Ausbildung mit einer abschließenden Prüfung beendet wurde bzw. werden sollte (dh. der Wert des Attributes „stand“ in Z 5 lautet „aa“, „ab“, „ac“, „ad“, „ae“, „ar“ oder „as“ bzw. „ba“, „kl“ oder „kw“) – bei Teilprüfungen nur dann, wenn es sich um die letzte(n) Teilprüfung(en) handelt – und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="2"><p>mit der Angabe des Schuljahres der Abschlussklasse</p></td>
  </tr>
  <tr>
    <td><p>semester</p></td>
    <td colspan="2"><p>bei nicht ganzjähriger Ausbildungsorganisation mit den Ausprägungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„w“</p></td>
    <td><p>für die Meldung zum Wintersemester</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td><p>für die Meldung zum Sommersemester</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td><p>für die Meldung zu einem unterjährigen Lehrgang,</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>sonst „g“ für ganzjährige Ausbildungsorganisation</p></td>
  </tr>
  <tr>
    <td><p>termin</p></td>
    <td colspan="2"><p>mit dem Datum des Prüfungszeugnisses (bzw. der letzten Prüfung, wenn kein Zeugnis ausgestellt wurde)</p></td>
  </tr>
  <tr>
    <td><p>extern</p></td>
    <td colspan="2"><p>mit der Angabe, ob es sich bei der Prüfungskandidatin oder beim Prüfungskandidaten um eine Externistin bzw. einen Externisten „e“ oder eine (ehemalige) Schülerin oder einen (ehemaligen) Schüler der eigenen Schule „s“ handelt</p></td>
  </tr>
  <tr>
    <td><p>zulassung</p></td>
    <td colspan="2"><p>mit der Angabe über die Art der Zulassung zu diesem Prüfungstermin in den folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td><p>für erstmalige Zulassung zur Hauptprüfung (bzw. Fortsetzung dieser Prüfung nach gerechtfertigter Verhinderung)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td><p>für 1. Wiederholung von (nicht bestandenen) Teilprüfungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td><p>für 2. Wiederholung von (nicht bestandenen) Teilprüfungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td><p>für 3. Wiederholung von (nicht bestandenen) Teilprüfungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>Im Falle der Wiederholung von Teilprüfungen ist für dieses Merkmal jene Prüfung relevant, die am häufigsten wiederholt werden musste</p></td>
  </tr>
  <tr>
    <td><p>ergebnis</p></td>
    <td colspan="2"><p>mit der Angabe über die Gesamtbeurteilung dieser abschließenden Prüfung in den folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>mit ausgezeichnetem Erfolg bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in drei Prüfungsgebieten</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in einem Prüfungsgebiet</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>mit gutem Erfolg bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td><p>letztmalige Wiederholung von Teilprüfungen nicht bestanden, dh. ohne Berechtigung zu weiteren Wiederholungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>Nichtbeurteilung der Prüfungsgebiete wegen Verhinderung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„t“</p></td>
    <td><p>Terminverlust (nicht gerechtfertigtes Fernbleiben von der Wiederholung einer Teilprüfung)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„v“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in vier oder mehr Prüfungsgebieten</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„z“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in zwei Prüfungsgebieten</p></td>
  </tr>
</table>

- 13\. Das Element externist ist ein Kind-Element von „ausbildung“, muss genau einmal vorhanden sein, wenn es sich beim „schueler“ um einen Kandidaten für eine Externistenprüfung handelt, der mit dieser Prüfung die Ausbildung noch nicht mit einer abschließenden Prüfung erfolgreich abgeschlossen hat (dh. der Wert des Attributes „stand“ in Z 5 beginnt mit „e“) und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>termin</p></td>
    <td colspan="2"><p>mit dem Datum des Prüfungszeugnisses</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="2"><p>mit der Angabe der Schulstufe, über die die Externistenprüfung abgelegt wurde (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl für die Ausbildung (Lehrplan), über die die Externistenprüfung abgelegt wurde (gemäß der von der Bundesministerin oder vom Bundesminister für Bildung, Wissenschaft und Forschung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>art</p></td>
    <td colspan="2"><p>mit der Angabe zur Art der Externistenprüfung, die abgelegt wurde, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>Prüfung gemäß § 13 Abs. 3 SchPflG (zureichender Erfolg eines Unterrichts an einer Schule im Ausland)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>Prüfung gemäß § 22 Abs. 4 SchPflG (zureichender Erfolg eines Unterrichts an einer Berufsschule ohne Öffentlichkeitsrecht)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>Prüfung gemäß § 11 Abs. 4 SchPflG (zureichender Erfolg eines gleichwertigen Unterrichts)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>über eine Schulstufe</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td><p>Prüfung über eine Schulart (ohne abschließende Prüfung)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„u“</p></td>
    <td><p>über den Lehrstoff einzelner Unterrichtsgegenstände</p></td>
  </tr>
  <tr>
    <td><p>erfolg</p></td>
    <td colspan="2"><p>mit der Angabe über das Ergebnis dieser Prüfung in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>für Beurteilung mit ausgezeichnetem Erfolg</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>für Beurteilung mit gutem Erfolg</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>für erfolgreich bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>für nicht bestanden (negative Beurteilung)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>ohne Beurteilung (zB wenn die Prüfung noch nicht abgeschlossen wurde uä.)</p></td>
  </tr>
</table>
