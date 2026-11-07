## Anlage 1

## zu § 5 Abs. 1, § 7 Abs. 1 und § 25

## Teil I

## Daten der Schulen für die Gesamtevidenz

1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1 Definition der Schnittstellen zwischen den Evidenzen gemäß § 5 BilDokG 2020 (lokalen Schulverwaltungsprogrammen) und der Gesamtevidenz: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so ist eines der von der Bundesanstalt „Statistik Österreich“ vorgegebenen Formate zu verwenden.

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchUG-BKV“ = Schulunterrichtsgesetz für Berufstätige, Kollegs und Vorbereitungslehrgänge, [BGBl. I Nr. 33/1997](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1997_33_1/1997_33_1.pdf>), „SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

1.3 Die „semestrierte Oberstufe“ (bzw. auslaufend die „Neue Oberstufe“) umfasst die 10. und die folgenden Schulstufen an zumindest dreijährigen mittleren und höheren Schulen.

2\. Das Wurzel-Element bildungsdokumentation muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

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

3\. Das Element schule ist ein Kind-Element von „bildungsdokumentation“, muss mindestens einmal pro Datenmeldung vorhanden sein (Schülerinnen oder Schüler von Exposituren, dislozierten Klassen u. ä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen zu melden) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten österreichischen Schulendatei) |

4\. Das Element schueler ist ein Kind-Element von „schule“, muss mindestens einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| vbPKBF | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Bildung und Forschung gemäß § 9 E-GovG (wenn verfügbar) |
| vbPKAS | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik gemäß § 9 E-GovG (wenn verfügbar) |
| svnr | bis zur Ausstattung mit bPK mit der Sozialversicherungsnummer der Schülerin oder des Schülers (wenn verfügbar) |
| ersatz | mit der Ersatzkennung für die Schülerin oder den Schüler, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind bzw. bis zur Ausstattung mit bPK, wenn die Sozialversicherungsnummer („svnr“) nicht verfügbar ist |
| gebdat | mit dem Geburtsdatum der Schülerin oder des Schülers |
| geschlecht | mit dem Geschlecht der Schülerin oder des Schülers („m“ für männlich, „w“ für weiblich, „x“ für divers, „o“ für offen, „i“ für inter und „k“, wenn von jeglicher Geschlechtsangabe abgesehen wurde) |
| staat | mit der Staatsangehörigkeit der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes) |
| erstsprache1 | mit der (ersten) Angabe zu der Sprache bzw. den Sprachen der Schülerin oder des Schülers, in der bzw. denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprache(n)“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache2 | mit der (gegebenenfalls) zweiten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache3 | mit der (gegebenenfalls) dritten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache1 | mit der (ersten) Angabe über die im Alltag regelmäßig gebrauchte(n) Sprache(n) der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache2 | mit der (gegebenenfalls) zweiten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache3 | mit der (gegebenenfalls) dritten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| spf | mit der Angabe, ob ein sonderpädagogischer Förderbedarf bescheidmäßig festgestellt ist („f“) bzw. bei noch laufenden Verfahren („v“), sonst „n“ |
| integr-berufsausb | mit der Angabe, ob eine Inanspruchnahme einer Ausbildung gem. § 8b Abs. 1 oder 2 des Berufsausbildungsgesetzes, [BGBl. Nr. 142/1969](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1969_142_0/1969_142_0.pdf>), vorliegt, sonst „n“. Angabe „v“ für die „verlängerte Lehre“ und „t“ für die „Teilqualifikation“ |
| plz | mit der Postleitzahl der Heimatadresse der Schülerin oder des Schülers, bei einer Auslandsadresse Eintrag des Postleitzahlen-Ersatzcodes nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes |
| ort | mit der Bezeichnung des Ortes der Heimatadresse der Schülerin oder des Schülers |
| zusatzort | mit der Kennung „j“, wenn eine zusätzliche Wohnadresse am Bildungsort besteht, sonst „n“ |
| matrikel | für ein bildungseinrichtungsspezifisches Personenkennzeichen |
| eingeschult | mit der Angabe des Kalenderjahres, in dem die Schülerin oder der Schüler in die erste Schulstufe bzw. als Schulpflichtige oder Schulpflichtiger in die Vorschulstufe eintrat (gegebenenfalls gemäß Rückrechnung nach dem SchPflG, zB bei Zuzug aus dem Ausland) |

5\. Das Element ausbildung ist ein Kind-Element von „schueler“, muss pro Schülerin oder pro Schüler und Datenmeldung einmal bzw. bei Wechsel der Ausbildung innerhalb der Schule zweimal vorhanden sein und weist folgende Attribute auf:

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
    <td><p>erfolgreich abgeschlossene Mittelschule mit Erfüllung der Voraussetzung zur Aufnahme in die 5. Klasse einer allgemeinbildenden höheren Schule (§ 40 Abs. 3 Z 1 SchOG) bzw. in den I. Jahrgang einer berufsbildenden höheren Schule (§ 68 Abs. 1 Z 1 SchOG) ohne Aufnahmsprüfung</p></td>
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
    <td><p>erfolgreich abgeschlossene Sonderschule oder sonstige allgemein bildende Pflichtschule (Berufsvorbereitungsjahr, Oberstufe der Volksschule, zur Erfüllung der allgemeinen Schulpflicht geeignete Statutschule usw.)</p></td>
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
    <td><p>erfolgreich abgeschlossene Volksschule, jedoch ohne Erfüllung der Voraussetzung zur Aufnahme in die 1. Klasse einer allgemein bildenden höheren Schule ohne Aufnahmsprüfung</p></td>
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
    <td><p>vorzeitige Beendigung der Ausbildung infolge vier oder mehr negativer Beurteilungen in Pflichtgegenständen in der ersten Stufe einer berufsbildenden mittleren oder höheren Schule (§ 33 Abs. 2 lit. f SchUG in Verbindung mit § 82a SchUG)</p></td>
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
    <td><p>nicht erfolgreiche Beendigung einer Sonderschule oder anderen allgemein bildenden Pflichtschule</p></td>
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
    <td><p>vorzeitige Beendigung der Ausbildung wegen ansonstiger Überschreitung der Höchstdauer gemäß § 32 SchUG bzw. § 31 SchUG-BKV</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bv“</p></td>
    <td><p>Beendigung des Schulbesuchs infolge Widerrufs der vorzeitigen Aufnahme in die erste Klasse der Volksschule (§ 33 Abs. 2 lit. e SchUG in Verbindung mit § 7 Abs. 8 SchPflG) oder Abmeldung</p></td>
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
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung durch freiwillige Wiederholung der Schulstufe (§ 27 Abs. 2 oder 2a SchUG) bzw. des Semesters</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fm“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden modularen Ausbildung gemäß SchUG-BKV</p></td>
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
    <td><p>„fs“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung in der Schuleingangsphase auf der gleichen Schulstufe wie im vorangegangenen Schuljahr (§ 17 Abs. 5 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fu“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung durch Überspringen einer Schulstufe (§ 26 SchUG) bzw. eines Semesters</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fv“</p></td>
    <td><p>Fortsetzung des an der meldenden Schule bereits im vorangegangenen Schuljahr begonnenen Lehrganges, Kurses oder Ausbildungsjahres bzw. -semesters (bei schuljahresüberschneidender Ausbildungsorganisation)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fw“</p></td>
    <td><p>Fortsetzung der an der meldenden Schule bereits laufenden Ausbildung durch Wiederholung der Schulstufe (§ 27 Abs. 1 SchUG) bzw. des Semesters</p></td>
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
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung durch freiwillige Wiederholung der Schulstufe (§ 27 Abs. 2 oder 2a SchUG) bzw. des Semesters an dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ni“</p></td>
    <td><p>Neueinstieg in eine höhere Stufe bzw. ein höheres Semester dieser Ausbildung aus einer Schule im Ausland (Zuwanderung)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nm“</p></td>
    <td><p>Neueinstieg in die modulare Ausbildung gemäß SchUG-BKV an der meldenden Schule</p></td>
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
    <td><p>„ns“</p></td>
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung in der Schuleingangsphase auf der gleichen Schulstufe wie im vorangegangenen Schuljahr (§ 17 Abs. 5 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nu“</p></td>
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung durch Überspringen einer Schulstufe (§ 26 SchUG) bzw. eines Semesters an dieser Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nw“</p></td>
    <td><p>Fortsetzung der zuletzt an einer anderen Schule besuchten Ausbildung durch Wiederholung der Schulstufe (§ 27 Abs. 1 SchUG) bzw. des Semesters an dieser Schule</p></td>
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

6\. Das Element ausbildungsdetails ist ein Kind-Element von „ausbildung“, muss genau einmal pro laufender Ausbildung (dh. der Wert des Attributes „stand“ in Z 5 beginnt mit „f“ oder „n“) vorhanden sein und weist folgende Attribute auf:

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
    <td colspan="3"><p>mit der (schulüblichen) Bezeichnung der besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe</p></td>
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
    <td colspan="2"><p>für modular (SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td colspan="2"><p>für „Neue Oberstufe“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„p“</p></td>
    <td colspan="2"><p>für „semestrierte Oberstufe“</p></td>
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
    <td colspan="3"><p>mit der von der Schülerin oder vom Schüler besuchten Schulstufe, die eine schulartenübergreifende Nummerierung der Ausbildungsjahre ist, beginnend mit „1“ für das 1. Grundschuljahr und „0“ für die Vorschulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="3"><p>mit der Schulformkennzahl für die besuchte Ausbildung (Lehrplan) gemäß der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei</p></td>
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
    <td colspan="2"><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 4 Abs. 2 lit. a SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td colspan="2"><p>für der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus dem Grund der Ablegung einer Einstufungsprüfung nicht zulässig ist (§ 4 Abs. 2 lit. b SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td colspan="2"><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler wegen mangelnder Kenntnis der Unterrichtssprache nicht zulässig ist (§ 3 Abs. 1 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td colspan="2"><p>für nicht der allgemeinen Schulpflicht unterliegende außerordentliche Schülerinnen und Schüler, deren Aufnahme als ordentliche Schülerinnen und Schüler aus anderen Gründen nicht zulässig ist</p></td>
  </tr>
  <tr>
    <td><p>bilingual</p></td>
    <td colspan="3"><p>mit der Information, ob fremdsprachiger bzw. zweisprachiger Unterricht (Lebende Fremdsprache als Unterrichtssprache) besucht wird (§ 16 Abs. 3 SchUG), in folgenden Ausprägungen:</p></td>
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
    <td colspan="3"><p>mit der Angabe der Sprache gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Fremdsprachenverzeichnis</p></td>
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
    <td colspan="2"><p>„kla“</p></td>
    <td><p>für Unterricht von Schülerinnen und Schülern der Deutschförderklasse in einer schulautonomen Deutschförderung</p></td>
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
    <td></td>
    <td colspan="2"><p>„kua“</p></td>
    <td><p>für Unterricht von Schülerinnen und Schülern des Deutschförderkurses in einer schulautonomen Deutschförderung</p></td>
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

7\. Das Element erstsprachenunterricht ist ein Kind-Element von „ausbildungsdetails“, muss für jede Erstsprache, in der die Schülerin oder der Schüler im laufenden Schuljahr bzw. Semester in Form des „Erstsprachenunterrichts“ unterrichtet wird, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>fach</p></td>
    <td colspan="2"><p>mit der Angabe des Faches (Gegenstands) gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Sprachenverzeichnis</p></td>
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

8\. Das Element schulerfolg ist ein Kind-Element von „ausbildung“, muss genau einmal pro Ausbildung einer Schülerin oder eines Schülers vorhanden sein, wenn diese Ausbildung nicht erst im aktuellen Jahrgang begonnen wurde (dh. der Wert des Attributes „stand“ in Z 5 beginnt nicht mit „n“) und weist folgende Attribute auf:

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
    <td colspan="2"><p>mit der (schulüblichen) Bezeichnung der zuletzt besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe</p></td>
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
    <td><p>für modular (SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>für „Neue Oberstufe“</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„p“</p></td>
    <td><p>für „semestrierte Oberstufe“</p></td>
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
    <td colspan="2"><p>Mit der von der Schülerin oder vom Schüler in diesem Ausbildungsdurchgang besuchten Schulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl für diese Ausbildung (Lehrplan) gemäß der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei</p></td>
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
    <td><p>„kla“</p></td>
    <td><p>für Unterricht von Schülerinnen und Schülern der Deutschförderklasse in einer schulautonomen Deutschförderung</p></td>
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
    <td></td>
    <td><p>„kua“</p></td>
    <td><p>für Unterricht von Schülerinnen und Schülern des Deutschförderkurses in einer schulautonomen Deutschförderung</p></td>
  </tr>
  <tr>
    <td><p>jahreserfolg</p></td>
    <td colspan="2"><p>mit der Gesamtbeurteilung im letzten Jahreszeugnis (bzw. Semester- oder Lehrgangszeugnis) in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>für Beurteilung mit ausgezeichnetem Erfolg (§ 22 Abs. 2 lit. g bzw. § 22a Abs. 2 Z 8 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>für berechtigt zum Aufsteigen trotz negativer oder keiner Beurteilung an Schulen für Berufstätige (§ 26 Abs. 1 erster Satz SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit negativer Beurteilung in der ersten oder zweiten Schulstufe (§ 25 Abs. 3 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td><p>für berechtigt zum Aufsteigen infolge eines fremdsprachigen Schulbesuchs im Ausland (§ 25 Abs. 9 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>für Beurteilung mit gutem Erfolg (§ 22 Abs. 2 lit. h bzw. § 22a Abs. 2 Z 9 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„h“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit „Nicht genügend“ nach Unterricht gemäß dem höheren Leistungsniveau (§ 25 Abs. 5 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit einem „Nicht genügend“ (§ 25 Abs. 2 SchUG – „Konferenzbeschluss“) bzw. mit einem „Nicht genügend“ oder einer Nichtbeurteilung in der „Neuen Oberstufe“ (§ 25 Abs. 10 SchUG idF <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a>) oder in der „semestrierten Oberstufe“ (§ 25 Abs. 10 Z 1 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td><p>für nicht berechtigt zum Aufsteigen in der 4. oder 5. Klasse einer allgemein bildenden höheren Schule oder nicht erfolgreicher Abschluss der 4. Klasse der Mittelschule oder 8. Klasse der Volksschule auf Grund einer negativen Beurteilung in Latein, Geometrisch Zeichnen oder einem besonderen Pflichtgegenstand gemäß § 28 Abs. 3 Z 1 SchUG</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„m“</p></td>
    <td><p>für berechtigt zum Aufsteigen in Sonderschulen für Kinder mit erhöhtem Förderbedarf bzw. mehrfach behinderte Kinder (§ 25 Abs. 6 SchUG)</p></td>
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
    <td><p>für berechtigt zum Aufsteigen oder erfolgreichen Abschluss der letzten Schulstufe mit positiver Beurteilung in allen Pflichtgegenständen (§ 25 Abs. 1 erster Satz SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„r“</p></td>
    <td><p>für nicht berechtigt zum Aufsteigen oder nicht erfolgreichen Abschluss der letzten Schulstufe wegen nicht zurückgelegter Pflichtpraktika (§ 25 Abs. 8 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„s“</p></td>
    <td><p>für berechtigt zum Aufsteigen bei Kindern mit sonderpädagogischem Förderbedarf an allgemeinen Schulen (§ 25 Abs. 5a SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„v“</p></td>
    <td><p>für berechtigt zum Aufsteigen in die 5. Stufe der Sonderschule trotz negativer Beurteilung in bestimmten Pflichtgegenständen (wie Musikerziehung, Bildnerische Erziehung, Schreiben, usw.) in Sonderschulen (§ 25 Abs. 4 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„w“</p></td>
    <td><p>für berechtigt zum Aufsteigen trotz negativer Beurteilung bei Wiederholung nach einem „Befriedigend“ in diesem Gegenstand (§ 25 Abs. 1 letzter Satz SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„x“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit zwei „Nicht genügend“ oder Nichtbeurteilungen in der „Neuen Oberstufe“ (§ 25 Abs. 10 erster und zweiter Satz SchUG idF <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a>) oder in der „semestrierten Oberstufe“ (§ 25 Abs. 10 Z 2 SchUG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„y“</p></td>
    <td><p>für berechtigt zum Aufsteigen mit drei „Nicht genügend“ oder Nichtbeurteilungen in der „Neuen Oberstufe“ (§ 25 Abs. 10 dritter Satz SchUG idF <a href="https://ogd.ris.bka.gv.at/eli/bgbl/I/2020/159">BGBl. I Nr. 159/2020</a>)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„z“</p></td>
    <td><p>für keine Jahres- bzw. Semesterbeurteilung bei modularen Ausbildungen gemäß SchUG-BKV</p></td>
  </tr>
  <tr>
    <td><p>nichtgen</p></td>
    <td colspan="2"><p>mit der Anzahl der „Nicht genügend“ in Pflichtgegenständen (nach allfälligen Wiederholungs-, Nachtrags- oder Semesterprüfungen)</p></td>
  </tr>
  <tr>
    <td><p>wdhp-angetr</p></td>
    <td colspan="2"><p>mit der Zahl der Wiederholungs-, Nachtrags- oder Semesterprüfungen usw. gemäß § 23 SchUG, zu denen die Schülerin oder der Schüler angetreten ist</p></td>
  </tr>
  <tr>
    <td><p>wdhp-bestand</p></td>
    <td colspan="2"><p>mit der Zahl der davon bestandenen Wiederholungs-, Nachtrags- oder Semesterprüfungen usw.</p></td>
  </tr>
  <tr>
    <td><p>wiederholung</p></td>
    <td colspan="2"><p>mit der Angabe bezüglich der Wiederholungsberechtigung (gemäß § 27 SchUG bzw. § 28 SchUG-BKV), in folgenden Ausprägungen:</p></td>
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

9\. Das Element gegenstand ist ein Kind-Element von „schulerfolg“, muss für jede Fremdsprache, in der die Schülerin oder der Schüler im abgelaufenen Schuljahr bzw. Semester unterrichtet wurde, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>fach</p></td>
    <td colspan="2"><p>mit der Angabe des Faches (Gegenstands) gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Fremdsprachenverzeichnis</p></td>
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

10\. Das Element erstsprachenunterricht\_erfolg ist ein Kind-Element von „schulerfolg“, muss für jede Erstsprache, in der die Schülerin oder der Schüler im abgelaufenen Schuljahr bzw. Semester in Form des „Erstsprachenunterrichts“ unterrichtet wurde, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>fach</p></td>
    <td colspan="2"><p>mit der Angabe des Faches (Gegenstands) gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Sprachenverzeichnis</p></td>
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

11\. Das Element leistungsbeurteilung ist ein Kind-Element von „schulerfolg“, muss für die Pflichtgegenstände Deutsch, (Angewandte) Mathematik, Englisch, Französisch, Italienisch, Spanisch, in der die Schülerin oder der Schüler im abgelaufenen Schuljahr bzw. Semester unterrichtet wurde, einmal vorhanden sein und weist folgende Attribute auf:

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
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufen gem. § 14 Leistungsbeurteilungsverordnung, <a href="https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1974_371_0/1974_371_0.pdf">BGBl. Nr. 371/1974</a> (nach allfälligen Nachtrags-, Wiederholungs- und Semesterprüfungen), mit der Angabe „nicht beurteilt“ bei vorgetäuschten Leistungen gem. § 18 Abs. 4 SchUG, mit der Angabe, ob die Feststellungsprüfung gem. § 20 Abs. 3 SchUG gestundet wurde, bzw. mit der Angabe „ohne Beurteilung“, wenn eine alternative Leistungsbeurteilung gem. § 18a SchUG, keine Beurteilung bei außerordentlichen Schülerinnen und Schülern gem. § 22 Abs. 11 letzter Satz SchUG oder keine Beurteilung bei Sonderschülerinnen und –schülern gem. § 20 Abs. 8 SchUG erfolgte, in folgender Differenzierung:</p></td>
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

12\. Das Element schulpflichtverletzung ist ein Kind-Element von „schulerfolg“, muss für jede Schülerin oder für jeden Schüler, die oder der im abgelaufenen Schuljahr die allgemeine Schulpflicht noch nicht erfüllt bzw. für die oder den Berufsschulpflicht bestanden hatte, einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| unentsch-tage-vorjahr | mit der Anzahl der unentschuldigten Fehltage im abgelaufenen Schuljahr (bei keinem unentschuldigten Fehltag ist hier „0“ anzugeben) |
| verwarnungen-vorjahr | mit der Anzahl der Verwarnungen für unentschuldigte Fehltage im abgelaufenen Schuljahr (bei keiner Verwarnung ist hier „0“ anzugeben) |
| strafanz-vorjahr | mit der Anzahl der seitens der Schule erstatteten Strafanzeigen wegen Schulpflichtverletzung im abgelaufenen Schuljahr (bei keiner Erstattung ist hier „0“ anzugeben) |

13\. Das Element abschlussdetails ist ein Kind-Element von „ausbildung“, muss dann genau einmal vorhanden sein, wenn diese Ausbildung mit einer abschließenden Prüfung beendet wurde bzw. werden sollte (dh. der Wert des Attributes „stand“ in Z 5 lautet „aa“, „ab“, „ac“, „ad“, „ae“, „ar“ oder „as“ bzw. „ba“, „kl“ oder „kw“) – bei Teilprüfungen nur dann, wenn es sich um die letzte(n) Teilprüfung(en) handelt – und weist folgende Attribute auf:

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
    <td><p>mit ausgezeichnetem Erfolg bestanden (§ 38 Abs. 6 Z 1 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>bestanden (§ 38 Abs. 6 Z 3 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in drei Prüfungsgebieten (§ 38 Abs. 6 Z 4 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in einem Prüfungsgebiet (§ 38 Abs. 6 Z 4 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td><p>mit gutem Erfolg bestanden (§ 38 Abs. 6 Z 2 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td><p>letztmalige Wiederholung von Teilprüfungen nicht bestanden, dh. ohne Berechtigung zu weiteren Wiederholungen (§ 40 Abs. 1 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>Nichtbeurteilung der Prüfungsgebiete wegen Verhinderung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„t“</p></td>
    <td><p>Terminverlust (nicht gerechtfertigtes Fernbleiben von der Wiederholung einer Teilprüfung, § 36a Abs. 3 letzter Satz SchUG bzw. § 36 Abs. 2 SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„v“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in vier oder mehr Prüfungsgebieten (§ 38 Abs. 6 Z 4 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„z“</p></td>
    <td><p>nicht bestanden mit negativer Beurteilung bzw. Nichtbeurteilung in zwei Prüfungsgebieten (§ 38 Abs. 6 Z 4 SchUG bzw. SchUG-BKV)</p></td>
  </tr>
</table>

14\. Das Element externist ist ein Kind-Element von „ausbildung“, muss genau einmal vorhanden sein, wenn es sich beim „schueler“ um einen Kandidaten für eine Externistenprüfung handelt, der mit dieser Prüfung die Ausbildung noch nicht mit einer abschließenden Prüfung erfolgreich abgeschlossen hat (dh. der Wert des Attributes „stand“ in Z 5 beginnt mit „e“) und weist folgende Attribute auf:

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
    <td colspan="2"><p>mit der Angabe der Schulstufe, über die die Externistenprüfung abgelegt wurde (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl für die Ausbildung (Lehrplan), über die die Externistenprüfung abgelegt wurde (gemäß der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
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
    <td><p>„m“</p></td>
    <td><p>Studienberechtigungsprüfung</p></td>
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

15\. Das Element bildungsverlauf-vor-schulpflicht ist ein Kind-Element von „schueler“, muss mindestens einmal pro Schülerin oder Schüler der Primarstufe vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>kindergartenjahre</p></td>
    <td colspan="2"><p>mit der Angabe, wie viele Kindergartenjahre eine elementarpädagogische Bildungseinrichtung vor Beginn der allgemeinen Schulpflicht besucht wurde, in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td><p>Kein Besuch einer elementarpädagogischen Bildungseinrichtung vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während eines Kindergartenjahrs unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während zweier Kindergartenjahre unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während drei Kindergartenjahren unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während vier Kindergartenjahren unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während fünf Kindergartenjahren unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„9“</p></td>
    <td><p>Keine Information über den Besuch einer elementarpädagogischen Bildungseinrichtung vorhanden</p></td>
  </tr>
</table>

16\. Das Element elementarbildungsdetails ist ein Kind-Element von „bildungsverlauf-vor-schulpflicht“, muss einmal pro besuchtem Kindergartenjahr in einer elementarpädagogischen Einrichtung (Eingabe „1“ bis “5 im Feld „kindergartenjahre“) vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>kindergartenjahr</p></td>
    <td colspan="2"><p>mit der Angabe des betreffenden Kindergartenjahres in einer elementarpädagogischen Einrichtung</p></td>
  </tr>
  <tr>
    <td><p>monate</p></td>
    <td colspan="2"><p>mit der Angabe, wie viele Monate im betreffenden Kindergartenjahr ein Besuch der elementarpädagogischen Einrichtung erfolgte (liegen keine Informationen über die Dauer in Monaten vor, so ist hier „-“ anzugeben)</p></td>
  </tr>
  <tr>
    <td><p>ausmass</p></td>
    <td colspan="2"><p>Mit der Angabe des durchschnittlichen Stundenausmaßes pro Woche des Besuchs der elementarpädagogischen Einrichtung im betreffenden Kindergartenjahr (liegen keine Informationen über das Ausmaß vor, so ist hier „-“ anzugeben)</p></td>
  </tr>
  <tr>
    <td><p>sprachfoerderung</p></td>
    <td colspan="2"><p>mit der Angabe, in welchem Ausmaß im genannten Kindergartenjahr eine besondere Sprachförderung in Deutsch erfolgte, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>durchschnittlich einmal pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„z“</p></td>
    <td><p>durchschnittlich zweimal pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>durchschnittlich dreimal oder öfter pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>keine besondere Sprachförderung in Deutsch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„-“</p></td>
    <td><p>Es liegen keine Informationen über den Besuch einer besonderen Sprachförderung vor</p></td>
  </tr>
</table>

## Teil II

## Daten der Bildungsdirektorinnen oder der Bildungsdirektoren für die Gesamtevidenz

1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1 Definition der Schnittstellen zwischen den Datenbasen der Bildungsdirektorinnen und Bildungsdirektoren gemäß § 5 Abs. 3 und 4 BilDokG 2020 und der Gesamtevidenz: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so ist eines der von der Bundesanstalt „Statistik Österreich“ vorgegebenen Formate zu verwenden.

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

2\. Das Wurzel-Element bildungsdokumentation muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>xmlns</p></td>
    <td><p>mit dem Wert „bildungsdokumentation_schulpflichtige“</p></td>
  </tr>
  <tr>
    <td><p>meldedatum</p></td>
    <td><p>mit dem Datum dieser Meldung</p></td>
  </tr>
  <tr>
    <td rowspan="2"><p>meldeart</p></td>
    <td><p>mit „n“ für eine Neumeldung zu diesem Meldedurchgang (standard, überschreibt alle allfälligen bisherigen Meldungen dieser Schulbehörde zu diesem Meldedurchgang)</p></td>
  </tr>
  <tr>
    <td><p>mit „e“ für die Ergänzung zusätzlicher Informationen dieser Schulbehörde</p></td>
  </tr>
  <tr>
    <td><p>absender</p></td>
    <td><p>mit der (Behörden-)Kennzahl des Absenders</p></td>
  </tr>
</table>

3\. Das Element schulbehoerde ist ein Kind-Element von „bildungsdokumentation“, muss einmal pro Datenmeldung vorhanden sein und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Kennzahl der Schulbehörde, für die diese Meldung erfolgt (gemäß dem von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Verzeichnis der Schulbehörden) |

4\. Das Element schulpflichtige ist ein Kind-Element von „schulbehoerde“, muss für jede Schulpflichtige oder jeden Schulpflichtigen, die bzw. der die Schulpflicht gemäß § 11, § 13, § 15 oder § 23 SchPflG erfüllt, einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| vbPKBF | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Bildung und Forschung der oder des Schulpflichtigen gemäß § 9 E-GovG (wenn verfügbar) |
| vbPKAS | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik der oder des Schulpflichtigen gemäß § 9 E-GovG (wenn verfügbar) |
| svnr | bis zur Ausstattung mit bPK mit der Sozialversicherungsnummer der oder des Schulpflichtigen (wenn verfügbar) |
| ersatz | mit der Ersatzkennung für die oder den Schulpflichtigen, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind bzw. bis zur Ausstattung mit bPK, wenn die Sozialversicherungsnummer („svnr“) nicht verfügbar ist |
| gebdat | mit dem Geburtsdatum der oder des Schulpflichtigen |
| geschlecht | mit dem Geschlecht der oder des Schulpflichtigen („m“ für männlich, „w“ für weiblich, „x“ für divers, „o“ für offen, „i“ für inter und „k“, wenn von jeglicher Geschlechtsangabe abgesehen wurde) |
| staat | mit der Staatsangehörigkeit der oder des Schulpflichtigen (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes) |
| erstsprache1 | mit der (ersten) Angabe zu der Sprache bzw. den Sprachen der Schülerin oder des Schülers, in der bzw. denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprache(n)“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache2 | mit der (gegebenenfalls) zweiten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| erstsprache3 | mit der (gegebenenfalls) dritten Angabe zu den Sprachen der Schülerin oder des Schülers, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“) (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache1 | mit der (ersten) Angabe über die im Alltag regelmäßig gebrauchte(n) Sprache(n) der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache2 | mit der (gegebenenfalls) zweiten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| alltagsprache3 | mit der (gegebenenfalls) dritten Angabe über die im Alltag regelmäßig gebrauchten Sprachen der Schülerin oder des Schülers (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes) |
| spf | mit der Angabe, ob ein sonderpädagogischer Förderbedarf bescheidmäßig festgestellt ist („f“) bzw. bei noch laufenden Verfahren („v“), sonst „n“ |
| integr-berufsausb | mit der Angabe, ob eine Inanspruchnahme einer Ausbildung gem. § 8b Abs. 1 oder 2 des Berufsausbildungsgesetzes, [BGBl. Nr. 142/1969](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1969_142_0/1969_142_0.pdf>), vorliegt, sonst „n“. Angabe „v“ für die „verlängerte Lehre“ und „t“ für die „Teilqualifikation“ |
| plz | mit der Postleitzahl der Heimatadresse der oder des Schulpflichtigen, bei einer Auslandsadresse Eintrag des Postleitzahlen-Ersatzcodes nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes |
| ort | mit der Bezeichnung des Ortes der Heimatadresse der oder des Schulpflichtigen |
| zusatzort | mit der Kennung „j“, wenn eine zusätzliche Wohnadresse am Bildungsort besteht, sonst „n“ |
| matrikel | für ein von der Bildungsdirektion zu vergebendes bildungseinrichtungsspezifisches Personenkennzeichen |
| eingeschult | mit der Angabe des Kalenderjahres, in dem die oder der Schulpflichtige in die erste Schulstufe bzw. als Schulpflichtige oder Schulpflichtiger in die Vorschulstufe eintrat (gegebenenfalls gemäß Rückrechnung nach dem SchPflG, zB bei Zuzug aus dem Ausland) |

5\. Das Element ausbildung ist ein Kind-Element von „schulpflichtige“, muss pro Schulpflichtiger oder Schulpflichtigen und Datenmeldung einmal bzw. bei Wechsel der Ausbildung, in welcher die Schulpflicht ersatzweise erfüllt wird, zweimal vorhanden sein und weist folgende Attribute auf:

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
    <td colspan="2"><p>mit der Schulformkennzahl dieser Ausbildung (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>stand</p></td>
    <td colspan="2"><p>mit der Information über den gegenwärtigen Stand dieser Ausbildung mit folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ag“</p></td>
    <td><p>erfolgreich abgeschlossene Volksschule mit Erfüllung der Voraussetzung zur Aufnahme in die 1. Klasse einer allgemein bildenden höheren Schule ohne Aufnahmsprüfung (§ 40 Abs. 1 SchOG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ah“</p></td>
    <td><p>erfolgreich abgeschlossene Mittelschule mit Erfüllung der Voraussetzung zur Aufnahme in die 5. Klasse einer allgemeinbildenden höheren Schule (§ 40 Abs. 3 Z 1 SchOG) bzw. in den I. Jahrgang einer berufsbildenden höheren Schule (§ 68 Abs. 1 Z 1 SchOG) ohne Aufnahmsprüfung</p></td>
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
    <td><p>erfolgreich abgeschlossene Sonderschule oder sonstige allgemein bildende Pflichtschule (Berufsvorbereitungsjahr, Oberstufe der Volksschule, zur Erfüllung der allgemeinen Schulpflicht geeignete Statutschule usw.)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„at“</p></td>
    <td><p>erfolgreich abgeschlossene Polytechnische Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„av“</p></td>
    <td><p>erfolgreich abgeschlossene Volksschule, jedoch ohne Erfüllung der Voraussetzung zur Aufnahme in die 1. Klasse einer allgemein bildenden höheren Schule ohne Aufnahmsprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ay“</p></td>
    <td><p>erfolgreich abgeschlossener Vorbereitungslehrgang bzw. erfolgreich abgeschlossene Übergangsstufe zum Oberstufenrealgymnasium oder Aufbaugymnasium und -realgymnasium</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„az“</p></td>
    <td><p>erfolgreich abgeschlossene weiterführende Ausbildung ohne abschließende Prüfung (dh. mit positivem Abschlusszeugnis)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bh“</p></td>
    <td><p>nicht erfolgreiche Beendigung der Mittelschule (dh. ohne Abschluss der Mittelschule)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bo“</p></td>
    <td><p>nicht erfolgreiche Beendigung einer Sonderschule oder anderen allgemein bildenden Pflichtschule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bt“</p></td>
    <td><p>nicht erfolgreiche Beendigung der Polytechnischen Schule</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„bz“</p></td>
    <td><p>sonstige nicht erfolgreiche Beendigung der Ausbildung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„es“</p></td>
    <td><p>Beendigung der ersatzweisen Erfüllung der Schulpflicht per Ende des Schuljahres durch Wechsel in eine zur Erfüllung der Schulpflicht geeignete öffentliche Schule oder Privatschule mit Öffentlichkeitsrecht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„eu“</p></td>
    <td><p>Beendigung der ersatzweisen Erfüllung der Schulpflicht während des Unterrichtsjahres durch Wechsel in eine zur Erfüllung der Schulpflicht geeignete öffentliche Schule oder Privatschule mit Öffentlichkeitsrecht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ex“</p></td>
    <td><p>Beendigung der ersatzweisen Erfüllung der Schulpflicht infolge des Erreichens des Endes der Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„fx“</p></td>
    <td><p>Fortsetzung der Erfüllung der Schulpflicht ohne Besuch einer zur Erfüllung der Schulpflicht geeigneten inländischen öffentlichen Schule bzw. Privatschule mit Öffentlichkeitsrecht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nx“</p></td>
    <td><p>Neueinstieg in die ersatzweise Erfüllung der Schulpflicht bzw. Wechsel in diese Ausbildung ohne Besuch einer zur Erfüllung der Schulpflicht geeigneten inländischen öffentlichen Schule bzw. Privatschule mit Öffentlichkeitsrecht</p></td>
  </tr>
  <tr>
    <td><p>ende</p></td>
    <td colspan="2"><p>mit dem Datum der Beendigung dieser Ausbildung bzw. der ersatzweisen Erfüllung der Schulpflicht (wenn zutreffend, dh. das Merkmal in „stand“ beginnt mit „a“, „b“ oder „e“)</p></td>
  </tr>
</table>

6\. Das Element schulpflichtersatz ist ein Kind-Element von „ausbildung“, muss genau einmal pro laufender Ausbildung (dh. der Wert des Attributes „stand“ in Z 5 beginnt mit „f“ oder „n“) vorhanden sein und weist folgende Attribute auf:

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
    <td><p>klasse</p></td>
    <td colspan="2"><p>wenn vorhanden, mit der (schulüblichen) Bezeichnung der besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe. Im Fall der Nichtverfügbarkeit ist hier „1ext“ einzugeben.</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="2"><p>mit der von der oder dem Schulpflichtigen besuchten Schulstufe, die eine schulartenübergreifende Nummerierung der Ausbildungsjahre ist, beginnend mit „1“ für das 1. Grundschuljahr und „0“ für die Vorschulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl für die besuchte Ausbildung (Lehrplan) gemäß der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei</p></td>
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
  <tr>
    <td><p>ersatzart</p></td>
    <td colspan="2"><p>mit der Angabe, auf welche Art die Schulpflicht ersatzweise erfüllt wird:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td><p>Besuch einer öffentlichen oder dieser gleichzuhaltenden Schule im Ausland (§ 13 Schulpflichtgesetz 1985)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td><p>Befreiung vom Schulbesuch (§ 15 Schulpflichtgesetz 1985)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„h“</p></td>
    <td><p>Teilnahme an einem gleichwertigen häuslichen Unterricht (§ 11 Abs. 2 Schulpflichtgesetz 1985)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„l“</p></td>
    <td><p>Befreiung vom Besuch der Berufsschule, wenn dies alle Unterrichtsfächer des aktuellen Lehrjahres betrifft (§ 23 Schulpflichtgesetz 1985)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„o“</p></td>
    <td><p>Teilnahme an einem gleichwertigen Unterricht an einer Privatschule ohne Öffentlichkeitsrecht (§ 11 Abs. 1 Schulpflichtgesetz 1985)</p></td>
  </tr>
  <tr>
    <td><p>seit</p></td>
    <td colspan="2"><p>mit dem Datum, seit wann die oder der Schulpflichtige vom regulären Schulbesuch befreit ist</p></td>
  </tr>
</table>

7\. Das Element schulerfolg ist ein Kind-Element von „ausbildung“, muss genau einmal pro Ausbildung einer oder eines Schulpflichtigen vorhanden sein, wenn diese Ausbildung nicht erst im aktuellen Schuljahr begonnen wurde (dh. der Wert des Attributes „stand“ in Z 5 beginnt nicht mit „n“) und weist folgende Attribute auf:

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
    <td><p>klasse</p></td>
    <td colspan="2"><p>wenn vorhanden, mit der (schulüblichen) Bezeichnung der zuletzt besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe. Im Fall der Nichtverfügbarkeit ist hier „1ext“ einzugeben.</p></td>
  </tr>
  <tr>
    <td><p>schulstufe</p></td>
    <td colspan="2"><p>Mit der von der oder dem Schulpflichtigen in diesem Ausbildungsdurchgang besuchten Schulstufe (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert)</p></td>
  </tr>
  <tr>
    <td><p>sfkz</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl für diese Ausbildung (Lehrplan) gemäß der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei</p></td>
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
  <tr>
    <td><p>jahreserfolg</p></td>
    <td colspan="2"><p>mit dem Ergebnis der Prüfung über den zureichenden Erfolg der Teilnahme an einem gleichwertigen Unterricht im abgelaufenen Schuljahr in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td><p>für den Fall, dass von einer Prüfung gemäß § 11 Abs. 4 SchPflG abzusehen war, da auch Schülerinnen und Schüler öffentlicher oder diesen gleichzuhaltenden Schulen in der entsprechenden Ausbildung am Ende des Schuljahres nicht beurteilt werden (§ 11 Abs. 4 zweiter Halbsatz SchPflG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>für den Fall, dass von einer Prüfung gemäß § 11 Abs. 4 SchPflG abzusehen war, da der zureichende Erfolg durch die Vorlage von Zeugnissen öffentlicher oder diesen gleichzuhaltenden Schulen glaubhaft gemacht wurde (§ 13 Abs. 3 zweiter Satz SchPflG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„i“</p></td>
    <td><p>für den Fall, dass von einer Prüfung gemäß § 11 Abs. 4 SchPflG abzusehen war, da die oder der Schulpflichtige bereits während des Unterrichtsjahres in eine zur Erfüllung der Schulpflicht geeignete öffentliche Schule oder Privatschule mit Öffentlichkeitsrecht übergetreten ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„j“</p></td>
    <td><p>für den Fall, dass das schulpflichtige Kind vom Schulbesuch befreit war (§ 15 SchPflG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>für den Fall, dass der vorgesehene Nachweis des zureichenden Erfolgs der Teilnahme an einem gleichwertigen Unterricht nicht erbracht wurde (§ 11 Abs. 4 zweiter Satz SchPflG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„p“</p></td>
    <td><p>für den Fall, dass der Nachweis des zureichenden Erfolgs der Teilnahme an einem gleichwertigen Unterricht erbracht wurde (§ 11 Abs. 4 erster Halbsatz SchPflG)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„q“</p></td>
    <td><p>für den Fall, dass die Befreiung vom Besuch der Berufsschule ohne Verpflichtung zur Ablegung von Prüfungen erfolgte (§ 23 SchPflG)</p></td>
  </tr>
</table>

8\. Das Element leistungsbeurteilung ist ein Kind-Element von „schulerfolg“, muss pro Person für die Pflichtgegenstände Deutsch, (Angewandte) Mathematik, Englisch, Französisch, Italienisch, Spanisch im abgelaufenen Schuljahr einmal vorhanden sein und weist folgende Attribute auf:

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
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufen gemäß § 14 Leistungsbeurteilungsverordnung, <a href="https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1974_371_0/1974_371_0.pdf">BGBl. Nr. 371/1974</a> (nach allfälligen Wiederholungsprüfungen), mit der Angabe „nicht beurteilt“ bei vorgetäuschten Leistungen gemäß § 18 Abs. 4 SchUG, mit der Angabe „keine Beurteilung“, wenn ein verpflichtender Antritt nicht erfolgt bzw. ein Antritt nicht vorgesehen ist, in folgender Differenzierung:</p></td>
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
    <td><p>„k“</p></td>
    <td><p>Keine Beurteilung, wenn ein verpflichtender Antritt nicht erfolgt ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nv“</p></td>
    <td><p>Keine Beurteilung, wenn ein Antritt nicht vorgesehen ist</p></td>
  </tr>
</table>

9\. Das Element schulpflichtverletzung ist ein Kind-Element von „schulerfolg“, muss für jede Schülerin oder für jeden Schüler, die oder der im abgelaufenen Schuljahr die allgemeine Schulpflicht noch nicht erfüllt bzw. für die oder den Berufsschulpflicht bestanden hatte, einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| unentsch-tage-vorjahr | mit der Anzahl der unentschuldigten Fehltage im abgelaufenen Schuljahr (bei keinem unentschuldigten Fehltag ist hier „0“ anzugeben) |
| verwarnungen-vorjahr | mit der Anzahl der Verwarnungen für unentschuldigte Fehltage im abgelaufenen Schuljahr (bei keiner Verwarnung ist hier „0“ anzugeben) |
| strafanz-vorjahr | mit der Anzahl der seitens der Schule erstatteten Strafanzeigen wegen Schulpflichtverletzung im abgelaufenen Schuljahr (bei keiner Erstattung ist hier „0“ anzugeben) |

10\. Das Element bildungsverlauf-vor-schulpflicht ist ein Kind-Element von „schulpflichtige“, muss mindestens einmal pro Schülerin oder Schüler der Primarstufe vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>kindergartenjahre</p></td>
    <td colspan="2"><p>mit der Angabe, wie viele Kindergartenjahre eine elementarpädagogische Bildungseinrichtung vor Beginn der allgemeinen Schulpflicht besucht wurde, in folgender Ausprägung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td><p>Kein Besuch einer elementarpädagogischen Bildungseinrichtung vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während eines Kindergartenjahrs unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während zweier Kindergartenjahre unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während drei Kindergartenjahren unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während vier Kindergartenjahren unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td><p>Besuch einer elementarpädagogischen Bildungseinrichtung während fünf Kindergartenjahren unmittelbar vor Beginn der allgemeinen Schulpflicht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„9“</p></td>
    <td><p>Keine Information über den Besuch einer elementarpädagogischen Bildungseinrichtung vorhanden</p></td>
  </tr>
</table>

11\. Das Element elementarbildungsdetails ist ein Kind-Element von „bildungsverlauf-vor-schulpflicht“, muss einmal pro besuchtem Kindergartenjahr in einer elementarpädagogischen Einrichtung (Eingabe „1“ bis “5 im Feld „kindergartenjahre“) vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>kindergartenjahr</p></td>
    <td colspan="2"><p>mit der Angabe des betreffenden Kindergartenjahres in einer elementarpädagogischen Einrichtung</p></td>
  </tr>
  <tr>
    <td><p>monate</p></td>
    <td colspan="2"><p>mit der Angabe, wie viele Monate im betreffenden Kindergartenjahr ein Besuch der elementarpädagogischen Einrichtung erfolgte (liegen keine Informationen über die Dauer in Monaten vor, so ist hier „-“ anzugeben)</p></td>
  </tr>
  <tr>
    <td><p>ausmass</p></td>
    <td colspan="2"><p>Mit der Angabe des durchschnittlichen Stundenausmaßes pro Woche des Besuchs der elementarpädagogischen Einrichtung im betreffenden Kindergartenjahr (liegen keine Informationen über das Ausmaß vor, so ist hier „-“ anzugeben)</p></td>
  </tr>
  <tr>
    <td><p>sprachfoerderung</p></td>
    <td colspan="2"><p>mit der Angabe, in welchem Ausmaß im genannten Kindergartenjahr eine besondere Sprachförderung in Deutsch erfolgte, in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„e“</p></td>
    <td><p>durchschnittlich einmal pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„z“</p></td>
    <td><p>durchschnittlich zweimal pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td><p>durchschnittlich dreimal oder öfter pro Woche</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>keine besondere Sprachförderung in Deutsch</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„-“</p></td>
    <td><p>Es liegen keine Informationen über den Besuch einer besonderen Sprachförderung vor</p></td>
  </tr>
</table>

## Teil III

## Daten zur Sommerschule für die Gesamtevidenz

1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1 Definition der Schnittstellen zwischen den Datenbasen der Sommerschulen gemäß § 5 Abs. 1 Z 19 BilDokG 2020 und der Gesamtevidenz: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so ist eines der von der Bundesanstalt „Statistik Österreich“ vorgegebenen Formate zu verwenden.

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchPflG“ = Schulpflichtgesetz 1985, [BGBl. Nr. 76/1985](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1985_76_0/1985_76_0.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

2\. Das Wurzel-Element bildungsdokumentation muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>xmlns</p></td>
    <td><p>mit dem Wert „bildungsdokumentation_sommerschule“</p></td>
  </tr>
  <tr>
    <td><p>meldedatum</p></td>
    <td><p>mit dem Datum dieser Meldung</p></td>
  </tr>
  <tr>
    <td rowspan="2"><p>meldeart</p></td>
    <td><p>mit „n“ für eine Neumeldung zu diesem Meldedurchgang (standard, überschreibt alle allfälligen bisherigen Meldungen dieser Schulkennzahl zu diesem Meldedurchgang)</p></td>
  </tr>
  <tr>
    <td><p>mit „e“ für die Ergänzung zusätzlicher Informationen dieser Schulkennzahl</p></td>
  </tr>
  <tr>
    <td><p>absender</p></td>
    <td><p>mit der Schulkennzahl des Absenders</p></td>
  </tr>
</table>

3\. Das Element sommerschule ist ein Kind-Element von „bildungsdokumentation“, muss einmal pro Datenmeldung vorhanden sein und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Kennzahl der Sommerschule, für die diese Meldung erfolgt (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten österreichischen Schulendatei) |

4\. Das Element schueler ist ein Kind-Element von „sommerschule“, muss für jede Schülerin oder jeden Schüler an der Sommerschule einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| vbPKBF | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Bildung und Forschung der oder des Schulpflichtigen gemäß § 9 E-GovG (wenn verfügbar) |
| vbPKAS | mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik der Schülerin oder des Schülers gemäß § 9 E-GovG (wenn verfügbar) |
| ersatz | mit der Ersatzkennung für die Schülerin oder den Schüler, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind |

5\. Das Element teilnahme ist ein Kind-Element von „schueler“, muss pro Schülerin oder Schüler und Datenmeldung einmal vorhanden sein und weist folgende Attribute auf:

| Attribut | Wert |
| --- | --- |
| teilnahmeart | Art der Teilnahme an der Sommerschule mit folgenden Ausprägungen: „t“ für die Teilnahme, „b“ für Buddy-Schülerin oder -Schüler |
