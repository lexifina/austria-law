## Anlage 4

## zu § 12 Abs. 1 und 2, § 13 Abs. 1 und § 14 Abs. 1

## Teil I

## Daten hinsichtlich der Aufgabenebene für standardisierte Prüfungsgebiete der abschließenden Prüfungen, der Externistenprüfungen, die einer abschließenden Prüfung entsprechen, sowie der Berufsreifeprüfung

1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1 Definition der Schnittstellen zwischen den Evidenzen gemäß § 5 BilDokG 2020 (lokalen Schulverwaltungsprogrammen) und der Datenbasis der abschließenden Prüfungen der Bundesministerin oder des Bundesministers für Bildung: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so ist eines der von der Bundesministerin oder dem Bundesminister für Bildung vorgegebenen Formate zu verwenden.

1.2 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „BRPG“ = Berufsreifeprüfungsgesetz, [BGBl. I Nr. 68/1997](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1997_68_1/1997_68_1.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

2\. Das Wurzel-Element standardisiert\_srdp muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td colspan="2"><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>xmlns</p></td>
    <td colspan="2"><p>mit dem Wert „standardisiert_aufgabenebene“</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>meldedatum</p></td>
    <td colspan="2"><p>mit dem Datum dieser Meldung</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>absender</p></td>
    <td colspan="2"><p>mit der (Schul-, Cluster-)Kennzahl des Absenders</p></td>
  </tr>
  <tr>
    <td><p>termin</p></td>
    <td colspan="3"><p>mit der Angabe des Prüfungstermins zu dem die Meldung erfolgt</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ht-JJJJ“</p></td>
    <td><p>für die Meldung zum Haupttermin; so wäre zB für den Haupttermin im Schuljahr 2021/22 hier „ht-2022“ einzutragen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„he-JJJJ“</p></td>
    <td><p>für die Meldung zum Herbsttermin; so wäre zB für den Herbsttermin im Schuljahr 2022/23 hier „he-2022“ einzutragen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„wi-JJJJ“</p></td>
    <td><p>für die Meldung zum Wintertermin; so wäre zB für den Wintertermin im Schuljahr 2022/23 hier „wi-2023“ einzutragen</p></td>
  </tr>
  <tr>
    <td><p>erhebungsphase</p></td>
    <td colspan="3"><p>mit der Angabe des Meldedurchgangs, zu dem diese Meldung erfolgt</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„1“</p></td>
    <td><p>für die Meldung der Ergebnisse der Klausurarbeit bzw. der Klausurarbeiten (vor allfälligen Kompensationsprüfungen)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„2“</p></td>
    <td><p>für die Meldung inklusive der Ergebnisse der Kompensationsprüfung bzw. der Kompensationsprüfungen und der gesamthaften Beurteilung(en)</p></td>
  </tr>
</table>

3\. Das Element bildungseinrichtung ist ein Kind-Element von „standardisiert\_srdp“, muss mindestens einmal pro Datenmeldung vorhanden sein (Prüfungskandidatinnen oder Prüfungskandidaten von Exposituren, dislozierten Klassen u. ä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen zu melden) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt bzw. mit der Erwachsenenbildungsinstitutskennzahl des Erwachsenenbildungsinstituts, für das diese Meldung erfolgt (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten österreichischen Schulendatei und dem Verzeichnis der Erwachsenenbildungsinstitute) |

4\. Das Element leermeldung ist ein Kind-Element von „bildungseinrichtung“, muss im Falle einer Leermeldung gemäß § 12 Abs. 2 einmal pro Datenmeldung vorhanden sein und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| leer | mit der Angabe einer Leermeldung gemäß § 12 Abs. 2 mit dem Wert „l“ |

5\. Das Element kandidat ist ein Kind-Element von „bildungseinrichtung“, muss einmal pro Prüfungskandidatin oder pro Prüfungskandidaten und Datenmeldung vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>bPKBF</p></td>
    <td colspan="2"><p>mit dem bereichsspezifischen Personenkennzeichen Bildung und Forschung gemäß § 9 E-GovG (wenn verfügbar)</p></td>
  </tr>
  <tr>
    <td><p>vbPKAS</p></td>
    <td colspan="2"><p>mit dem verschlüsselten bereichsspezifischen Personenkennzeichen Amtliche Statistik gemäß § 9 E-GovG (wenn verfügbar)</p></td>
  </tr>
  <tr>
    <td><p>geschlecht</p></td>
    <td colspan="2"><p>mit dem Geschlecht der Prüfungskandidatin oder des Prüfungskandidaten, in folgenden Ausprägungen:</p></td>
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
    <td><p>matrikel</p></td>
    <td colspan="2"><p>für ein bildungseinrichtungsspezifisches Personenkennzeichen, hier zB die eindeutige SOKRATES-ID der Prüfungskandidatin oder des Prüfungskandidaten</p></td>
  </tr>
</table>

6\. Das Element ausbildung ist ein Kind-Element von „kandidat“, muss pro Prüfungskandidatin oder Prüfungskandidaten und Datenmeldung einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schulform</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl der Ausbildung, in der die abschließende Prüfung erfolgt (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>extern</p></td>
    <td colspan="2"><p>mit der Angabe, ob es sich bei der Prüfungskandidatin oder dem Prüfungskandidaten um eine Externistin oder einen Externisten „e“ oder keine Externistin oder keinen Externisten „s“ handelt.</p></td>
  </tr>
  <tr>
    <td><p>art</p></td>
    <td colspan="2"><p>mit der Angabe der Art der abschließenden Prüfung in folgenden Ausprägungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„rpr“</p></td>
    <td><p>Reifeprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„rud“</p></td>
    <td><p>Reife-und Diplomprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„brp“</p></td>
    <td><p>Berufsreifeprüfung (BRP)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„erp“</p></td>
    <td><p>Externistenreifeprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„erd“</p></td>
    <td><p>Externistenreife- und Diplomprüfung</p></td>
  </tr>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="2"><p>mit der Angabe des Schuljahres der Abschlussklasse bzw. des Abschlussjahrganges. Im Fall der Nichtverfügbarkeit bei einer Externistenreifeprüfung oder Externistenreife- und Diplomprüfung oder Berufsreifeprüfung ist hier 1000/01 als Proxy einzugeben</p></td>
  </tr>
  <tr>
    <td><p>klasse</p></td>
    <td colspan="2"><p>mit der (schulüblichen) Bezeichnung der besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe.</p>
<p>Im Fall der Nichtverfügbarkeit bei einer Externistenreifeprüfung oder Externistenreife- und Diplomprüfung oder Berufsreifeprüfung ist hier „1ext“ einzugeben.</p></td>
  </tr>
</table>

7\. Das Element klausur ist ein Kind-Element von „ausbildung“, muss für jedes Prüfungsgebiet bzw. jede Teilprüfung, in dem bzw. der die Prüfungskandidatin oder der Prüfungskandidat eine standardisierte Klausurarbeit abgelegt hat, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="3"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>pruefungstag</p></td>
    <td><p>„JJJJ-MM-TT“</p></td>
    <td colspan="2"><p>mit der Angabe des Datums der Prüfung des Prüfungsgebiets, für die Meldung in der Erhebungsphase 2 ist im Fall des Antritts zu einer Kompensationsprüfung der Tag der schriftlichen Klausur einzutragen.</p></td>
  </tr>
  <tr>
    <td><p>pruefungsgebiet</p></td>
    <td colspan="3"><p>mit der Angabe des Prüfungsgebiets gemäß der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Prüfungsgebietsliste</p></td>
  </tr>
  <tr>
    <td><p>antritt</p></td>
    <td colspan="3"><p>Mit der Angabe des Antritts im gegenständlichen Prüfungsgebiet</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>1. Antritt</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>1. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>2. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>3. Wiederholung</p></td>
  </tr>
  <tr>
    <td><p>kla_beurteilung</p></td>
    <td colspan="3"><p>mit der Angabe der Beurteilungsstufe der Klausurarbeit (vor einer allfälligen Kompensationsprüfung) oder der Angabe „nicht beurteilt“ (bei vorgetäuschten Leistungen)</p>
<p>in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td colspan="2"><p>nicht beurteilt</p></td>
  </tr>
  <tr>
    <td><p>schwellenwert</p></td>
    <td colspan="3"><p>mit der Angabe, ob bei einer Beurteilung mit „Nicht genügend“ der Schwellenwert erreicht wurde in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„0“</p></td>
    <td><p>keine Erreichung des Schwellenwerts</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„1“</p></td>
    <td><p>Erreichung des Schwellenwerts</p></td>
  </tr>
  <tr>
    <td><p>komp_beurteilung</p></td>
    <td colspan="3"><p>mit der Angabe der Beurteilungsstufe bzw. Information bezüglich Kompensationsprüfung, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td colspan="2"><p>keine Kompensationsprüfung vorgesehen, bei positiver Beurteilung oder Nichtbeurteilung des Prüfungsgebiets bzw. im Falle einer Berufsreifeprüfung für die Prüfungsgebiete Deutsch, lebende Fremdsprache und Fachbereich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td colspan="2"><p>für die Meldung vor dem Termin der Kompensationsprüfung (Erhebungsphase=„1“), wenn eine solche vorgesehen ist (nicht „c“)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td colspan="2"><p>nicht angetreten</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td colspan="2"><p>Nicht genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td colspan="2"><p>nicht beurteilt</p></td>
  </tr>
  <tr>
    <td><p>klp_beurteilung</p></td>
    <td colspan="3"><p>mit der Angabe der Beurteilungsstufe der Klausurprüfung (einschließlich einer allfälligen Kompensationsprüfung) oder der Angabe „nicht beurteilt“ (bei vorgetäuschten Leistungen) in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td colspan="2"><p>Nicht genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td colspan="2"><p>nicht beurteilt</p></td>
  </tr>
  <tr>
    <td><p>schulstufe_beurteilung</p></td>
    <td colspan="3"><p>mit der Angabe der Beurteilungsstufe der einzubeziehenden Leistungen der letzten Schulstufe, in welcher der das Prüfungsgebiet betreffende Unterrichtsgegenstand bzw. die das Prüfungsgebiet betreffenden Unterrichtsgegenstände unterrichtet wurde bzw. wurden oder der Angabe „keine Einbeziehung“, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td colspan="2"><p>keine Einbeziehung, da keine vorgesehen ist</p></td>
  </tr>
  <tr>
    <td><p>gesamth_kl_beurteilung</p></td>
    <td colspan="3"><p>mit der Angabe der gesamthaften Beurteilung des Prüfungsgebietes (Klausurarbeit, Kompensationsprüfung, einbezogene Leistung der letzten Schulstufe) in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td colspan="2"><p>für die Meldung vor dem Termin der Kompensationsprüfung (Erhebungsphase=„1“) wenn eine solche vorgesehen ist</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„5“</p></td>
    <td colspan="2"><p>Nicht genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„n“</p></td>
    <td colspan="2"><p>nicht beurteilt</p></td>
  </tr>
</table>

Zusätzlich sind die Ergebnisse auf Ebene der einzelnen Aufgaben gemäß der von der Bundesministerin oder dem Bundesminister zur Verfügung gestellten Formulare zu übermitteln. Diese haben Folgendes zu enthalten:

In den Prüfungsgebieten „Mathematik“, „Angewandte Mathematik“, „Lebende Fremdsprache“, „Latein“ und „Griechisch“: eine Aufzählung der Aufgaben, die maximal zu erreichende Punkteanzahl pro Aufgabe sowie die davon individuell erreichte Punkteanzahl pro Aufgabe.

In den Prüfungsgebieten „Deutsch“, „Slowenisch“, „Kroatisch“ und „Ungarisch“ (jeweils als Unterrichtssprache): die gewählte Aufgabe der Aufgabenstellung.

Zusätzlich ist pro Prüfungsgebiet der Technologieeinsatz anzugeben.

## Teil II

## Daten hinsichtlich des Gesamterfolgs der abschließenden Prüfungen, der Externistenprüfungen, die einer abschließenden Prüfung entsprechen, sowie der Berufsreifeprüfung

1\. Definitionen, Verweise, Begriffsbestimmungen:

1.1. Es ist für jede für jede Prüfungskandidatin und jeden Prüfungskandidaten sowie für jede Schülerin und jeden Schüler einer Abschlussklasse oder eines Abschlussjahrganges ohne Antrittsberechtigung eine Datenmeldung zu übermitteln.

Sollten bei Prüfungskandidatinnen oder Prüfungskandidaten Leistungen aus Vorterminen vorliegen, sind diese im Falle einer Reife- oder Reife- und Diplomprüfung, bei Externistinnen und Externisten falls vorhanden, mitzumelden.

Sollte eine Übermittlung mittels XML-Datei nicht möglich sein, so sind die von der Bundesanstalt „Statistik Österreich“ bereitgestellten Formate zu verwenden.

1.2 Definition der Schnittstellen zwischen den Evidenzen gemäß § 5 BilDokG 2020 (lokalen Schulverwaltungsprogrammen) und der Datenbasis der abschließenden Prüfungen bei der Bundesanstalt „Statistik Österreich“: Als Schnittstelle für die Datenübermittlung fungiert eine XML-Datei im Zeichensatzformat UTF-8, Datumsfelder sind im Format JJJJ-MM-TT abzuspeichern. Die Datei beginnt mit der Zeichenfolge .

1.3 Verweise auf bundesgesetzliche Rechtsvorschriften sind wie folgt zu verstehen: „SchOG“ = Schulorganisationsgesetz, [BGBl. Nr. 242/1962](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1962_242_0/1962_242_0.pdf>), „SchUG“ = Schulunterrichtsgesetz, [BGBl. Nr. 472/1986](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1986_472_0/1986_472_0.pdf>), „SchUG-BKV“ = Schulunterrichtsgesetz für Berufstätige, Kollegs und Vorbereitungslehrgänge, [BGBl. I Nr. 33/1997](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1997_33_1/1997_33_1.pdf>), „„BRPG“ = Berufsreifeprüfungsgesetz, [BGBl. I Nr. 68/1997](<https://ogd.ris.bka.gv.at/Dokumente/BgblPdf/1997_68_1/1997_68_1.pdf>), „E-GovG“ = E-Government-Gesetz, [BGBl. I Nr. 10/2004](<https://ogd.ris.bka.gv.at/eli/bgbl/I/2004/10>).

2\. Das Wurzel-Element erfolg\_srdp muss genau einmal pro Datenübermittlung vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td colspan="2"><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>xmlns</p></td>
    <td colspan="2"><p>mit dem Wert „erfolg_kandidat“</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>meldedatum</p></td>
    <td colspan="2"><p>mit dem Datum dieser Meldung</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>absender</p></td>
    <td colspan="2"><p>mit der (Schul-, Cluster- bzw. Erwachsenenbildungseinrichtungs-)Kennzahl des Absenders</p></td>
  </tr>
  <tr>
    <td><p>termin</p></td>
    <td colspan="3"><p>mit der Angabe des Prüfungstermins zu dem die Meldung erfolgt</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ht-JJJJ“</p></td>
    <td><p>für die Meldung zum Haupttermin; so wäre zB für den Haupttermin im Schuljahr 2021/22 hier „ht-2022“ einzutragen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„he-JJJJ“</p></td>
    <td><p>für die Meldung zum Herbsttermin; so wäre zB für den Herbsttermin im Schuljahr 2022/23 hier „he-2022“ einzutragen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„wi-JJJJ“</p></td>
    <td><p>für die Meldung zum Wintertermin; so wäre zB für den Wintertermin im Schuljahr 2022/23 hier „wi-2023“ einzutragen</p></td>
  </tr>
</table>

3\. Das Element bildungseinrichtung ist ein Kind-Element von „erfolg\_srdp“, muss mindestens einmal pro Datenmeldung vorhanden sein (Prüfungskandidatinnen oder Prüfungskandidaten sowie Schülerinnen oder Schüler in Abschlussklassen und Abschlussjahrgängen ohne Antrittsberechtigung von Exposituren, dislozierten Klassen u. ä. sind getrennt unter den Schulkennzahlen der dislozierten Stellen zu melden) und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| skz | mit der Schulkennzahl der Schule, für die diese Meldung erfolgt bzw. mit der Erwachsenenbildungsinstitutskennzahl des Erwachsenenbildungsinstituts, für das diese Meldung erfolgt (gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten österreichischen Schulendatei und dem Verzeichnis der Erwachsenenbildungsinstitute) |

4\. Das Element leermeldung ist ein Kind-Element von „bildungseinrichtung“, muss im Falle einer Leermeldung gemäß § 13 Abs. 2 einmal pro Datenmeldung vorhanden sein und weist folgendes Attribut auf:

| Attribut | Wert |
| --- | --- |
| leer | mit der Angabe einer Leermeldung gemäß § 13 Abs. 2 mit dem Wert „l“ |

5\. Das Element kandidat ist ein Kind-Element von „bildungseinrichtung“, muss mindestens einmal pro Prüfungskandidatin oder pro Prüfungskandidaten bzw. pro Schülerin oder pro Schüler einer Abschlussklasse oder eines Abschlussjahrganges ohne Antrittsberechtigung und Datenmeldung vorhanden sein und weist folgende Attribute auf:

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
    <td colspan="2"><p>bis zur Ausstattung mit bereichsspezifischen Personenkennzeichen mit der Sozialversicherungsnummer (wenn verfügbar)</p></td>
  </tr>
  <tr>
    <td><p>ersatz</p></td>
    <td colspan="2"><p>mit der Ersatzkennung, wenn die bereichsspezifischen Personenkennzeichen nicht verfügbar sind bzw. bis zur Ausstattung mit bereichsspezifischen Personenkennzeichen, wenn die Sozialversicherungsnummer („svnr“) nicht verfügbar ist</p></td>
  </tr>
  <tr>
    <td><p>gebdat</p></td>
    <td colspan="2"><p>mit dem Geburtsdatum</p></td>
  </tr>
  <tr>
    <td><p>geschlecht</p></td>
    <td colspan="2"><p>mit dem Geschlecht, in folgenden Ausprägungen:</p></td>
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
    <td><p>staat</p></td>
    <td colspan="2"><p>mit der Staatsangehörigkeit (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes)</p></td>
  </tr>
  <tr>
    <td><p>erstsprache1</p></td>
    <td colspan="2"><p>mit der (ersten) Angabe zu der Sprache bzw. den Sprachen, in der bzw. denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprache(n)“), (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes)</p></td>
  </tr>
  <tr>
    <td><p>erstsprache2</p></td>
    <td colspan="2"><p>mit der (gegebenenfalls) zweiten Angabe zu den Sprachen, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“), (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes)</p></td>
  </tr>
  <tr>
    <td><p>erstsprache3</p></td>
    <td colspan="2"><p>mit der (gegebenenfalls) dritten Angabe zu den Sprachen, in denen der Spracherwerb bis zur Vollendung des dritten Lebensjahrs erfolgte („Erstsprachen“), (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes)</p></td>
  </tr>
  <tr>
    <td><p>alltagsprache1</p></td>
    <td colspan="2"><p>mit der (ersten) Angabe über die im Alltag regelmäßig gebrauchte(n) Sprache(n), (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes)</p></td>
  </tr>
  <tr>
    <td><p>alltagsprache2</p></td>
    <td colspan="2"><p>mit der (gegebenenfalls) zweiten Angabe über die im Alltag regelmäßig gebrauchten Sprachen (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes)</p></td>
  </tr>
  <tr>
    <td><p>alltagsprache3</p></td>
    <td colspan="2"><p>mit der (gegebenenfalls) dritten Angabe über die im Alltag regelmäßig gebrauchten Sprachen (nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Sprachencodes)</p></td>
  </tr>
  <tr>
    <td><p>plz</p></td>
    <td colspan="2"><p>mit der Postleitzahl der Heimatadresse, bei einer Auslandsadresse Eintrag des Postleitzahlen-Ersatzcodes nach Maßgabe des von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Verzeichnisses der Staatencodes</p></td>
  </tr>
  <tr>
    <td><p>ort</p></td>
    <td colspan="2"><p>mit der Bezeichnung des Ortes der Heimatadresse</p></td>
  </tr>
  <tr>
    <td><p>zusatzort</p></td>
    <td colspan="2"><p>mit der Kennung „j“, wenn eine zusätzliche Wohnadresse am Bildungsort besteht, sonst „n“</p></td>
  </tr>
  <tr>
    <td><p>matrikel</p></td>
    <td colspan="2"><p>für ein bildungseinrichtungsspezifisches Personenkennzeichen – hier zB die eindeutige SOKRATES-ID</p></td>
  </tr>
</table>

6\. Das Element ausbildung ist ein Kind-Element von „kandidat“, muss pro Prüfungskandidatin oder pro Prüfungskandidaten bzw. pro Schülerin oder pro Schüler einer Abschlussklasse oder eines Abschlussjahrganges ohne Antrittsberechtigung und Datenmeldung einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>schulform</p></td>
    <td colspan="2"><p>mit der Schulformkennzahl der Ausbildung, in der die abschließende Prüfung erfolgt (nach Maßgabe der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei)</p></td>
  </tr>
  <tr>
    <td><p>extern</p></td>
    <td colspan="2"><p>mit der Angabe, ob es sich bei der Prüfungskandidatin oder dem Prüfungskandidaten um eine Externistin oder einen Externisten „e“ oder keine Externistin oder keinen Externisten „s“ handelt.</p></td>
  </tr>
  <tr>
    <td><p>art</p></td>
    <td colspan="2"><p>mit der Angabe der Art der abschließenden Prüfung in folgenden Ausprägungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„rpr“</p></td>
    <td><p>Reifeprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„rud“</p></td>
    <td><p>Reife-und Diplomprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„brp“</p></td>
    <td><p>Berufsreifeprüfung (BRP)</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„erp“</p></td>
    <td><p>Externistenreifeprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„erd“</p></td>
    <td><p>Externistenreife- und Diplomprüfung</p></td>
  </tr>
  <tr>
    <td><p>antrittsberechtigt</p></td>
    <td colspan="2"><p>mit der Angabe, ob eine Antrittsberechtigung gegeben ist, mit den Ausprägungen „1“ für antrittsberechtigt und „0“ für nicht antrittsberechtigt</p></td>
  </tr>
</table>

7\. Das Element ausbildung\_srdp ist ein Kind-Element von „ausbildung“, muss pro Prüfungskandidatin oder pro Prüfungskandidaten der Reifeprüfung oder Reife- und Diplomprüfung bzw. pro Schülerin oder pro Schüler einer Abschlussklasse oder eines Abschlussjahrganges ohne Antrittsberechtigung zur Reifeprüfung oder Reife- und Diplomprüfung (jeweils ohne Externistinnen und Externisten, ohne Kandidatinnen und Kandidaten, die bereits bei einem früheren Termin angetreten sind) und Datenmeldung einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>schuljahr</p></td>
    <td colspan="2"><p>mit der Angabe des Schuljahres der Abschlussklasse bzw. des Abschlussjahrganges</p></td>
  </tr>
  <tr>
    <td><p>klasse</p></td>
    <td colspan="2"><p>mit der (schulüblichen) Bezeichnung der besuchten (Stamm-)Klasse bzw. Jahrgang usw., wobei die erste Stelle numerisch ist und das Ausbildungsjahr bzw. -semester dieses Lehrplans wiedergibt (der Wertevorrat pro Lehrplan ist in der von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Schulformendatei definiert), die weiteren Stellen dienen zur Unterscheidung von Parallelklassen innerhalb der Schule; Klassenteile einer Stammklasse unterscheiden sich nicht in der Klassenbezeichnung, sondern durch die Schulformkennzahl bzw. Schulstufe.</p></td>
  </tr>
  <tr>
    <td><p>bilingual</p></td>
    <td colspan="2"><p>mit der Information, ob fremdsprachiger bzw. zweisprachiger Unterricht (Lebende Fremdsprache als Unterrichtssprache) besucht wurde (§ 16 Abs. 3 SchUG), in folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„d“</p></td>
    <td><p>für durchgehend fremd- bzw. zweisprachigen Unterricht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„k“</p></td>
    <td><p>für (praktisch) keinen fremd- bzw. zweisprachigen Unterricht</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„t“</p></td>
    <td><p>für teilweise fremd- bzw. zweisprachigen Unterricht</p></td>
  </tr>
  <tr>
    <td><p>bilingualsprache</p></td>
    <td colspan="2"><p>mit der Angabe der Unterrichtssprache, wenn der Wert des Attributs „bilingual“ gleich „d“ oder „t“ ist gemäß dem von der Bundesministerin oder vom Bundesminister für Bildung zur Verfügung gestellten Fremdsprachenverzeichnis; ansonsten bleibt dieses Attribut leer.</p></td>
  </tr>
</table>

8\. Das Element klausur ist ein Kind-Element von „ausbildung“, muss für jedes Prüfungsgebiet bzw. jede Teilprüfung, in dem bzw. der die Prüfungskandidatin oder der Prüfungskandidat eine Klausurarbeit im Rahmen einer abschließenden Prüfung, einer Externistenprüfung, die einer abschließenden Prüfung entspricht oder einer Berufsreifeprüfung abzulegen hat, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="4"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>pruefungstag</p></td>
    <td><p>„JJJJ-MM-TT“</p></td>
    <td colspan="3"><p>mit der Angabe des Datums der Prüfung des Prüfungsgebiets, ist im Fall des Antritts zu einer Kompensationsprüfung ist der Tag der schriftlichen Klausur einzutragen.</p></td>
  </tr>
  <tr>
    <td><p>pruefungsgebiet_e1</p></td>
    <td colspan="4"><p>mit der Ebene 1 der Klassifikation des Prüfungsgebiets, gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Liste der Prüfungsgebiete</p></td>
  </tr>
  <tr>
    <td><p>pruefungsgebiet_e2</p></td>
    <td colspan="4"><p>mit der Ebene 2 der Klassifikation des Prüfungsgebiets, gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Liste der Prüfungsgebiete</p></td>
  </tr>
  <tr>
    <td><p>pruefungsgebiet_e3</p></td>
    <td colspan="4"><p>mit der Ebene 3 der Klassifikation des Prüfungsgebiets, gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Liste der Prüfungsgebiete</p></td>
  </tr>
  <tr>
    <td><p>pruefungsgebiet_e4</p></td>
    <td colspan="4"><p>mit der Ebene 4 der Klassifikation des Prüfungsgebiets, gemäß der von der Bundesministerin oder dem Bundesminister für Bildung zur Verfügung gestellten Liste der Prüfungsgebiete</p></td>
  </tr>
  <tr>
    <td><p>langbezeichnung</p></td>
    <td colspan="4"><p>mit der Langbezeichnung, ggf. inkl. Angabe der betreffenden Fremdsprache bzw. des (schulautonomen) Prüfungsgebietes</p></td>
  </tr>
  <tr>
    <td><p>kurzbezeichnung</p></td>
    <td colspan="4"><p>mit der Kurzbezeichnung, ggf. inkl. Angabe der betreffenden Fremdsprache bzw. des (schulautonomen) Prüfungsgebietes</p></td>
  </tr>
  <tr>
    <td><p>standardisiert</p></td>
    <td colspan="4"><p>mit der Angabe, ob es sich um eine standardisierte Klausurarbeit handelt, mit den Ausprägungen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„1“</p></td>
    <td colspan="2"><p>standardisierte Klausurarbeit</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„0“</p></td>
    <td colspan="2"><p>nicht standardisierte Klausurarbeit</p></td>
  </tr>
  <tr>
    <td><p>vorgezogen</p></td>
    <td colspan="4"><p>mit der Angabe, ob es sich um eine vorgezogene Teilprüfung gemäß § 36 Abs. 3 SchUG bzw. § 35 Abs. 3 SchUG-BKV handelt</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„1“</p></td>
    <td><p>vorgezogene Teilprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„0“</p></td>
    <td><p>keine vorgezogene Teilprüfung</p></td>
  </tr>
  <tr>
    <td><p>termin_pruefungsgebiet</p></td>
    <td colspan="4"><p>mit der Angabe des Prüfungstermins, an dem das Ergebnis erzielt wurde</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„ht-JJJJ“</p></td>
    <td colspan="2"><p>für ein Ergebnis aus dem Haupttermin; so wäre zB für den Haupttermin des Schuljahres 2021/22 hier „ht-2022“ einzutragen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„he-JJJJ“</p></td>
    <td colspan="2"><p>für ein Ergebnis aus dem Herbsttermin</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„wi-JJJJ“</p></td>
    <td colspan="2"><p>für ein Ergebnis aus dem Wintertermin</p></td>
  </tr>
  <tr>
    <td><p>antritt</p></td>
    <td colspan="4"><p>mit der Angabe des Antritts im gegenständlichen Prüfungsgebiet</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„1“</p></td>
    <td colspan="2"><p>1. Antritt</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„2“</p></td>
    <td colspan="2"><p>1. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„3“</p></td>
    <td colspan="2"><p>2. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„4“</p></td>
    <td colspan="2"><p>3. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„v“</p></td>
    <td colspan="2"><p>Ergebnis aus einem Vortermin</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„g“</p></td>
    <td colspan="2"><p>gerechtfertigt verhindert</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„u“</p></td>
    <td colspan="2"><p>ungerechtfertigt ferngeblieben</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„a“</p></td>
    <td colspan="2"><p>Anerkennung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„b“</p></td>
    <td colspan="2"><p>entfällt oder befreit</p></td>
  </tr>
</table>

9\. Das Element klausur\_ergebnis ist ein Kind-Element von „klausur“, ist nur erforderlich, wenn das Attribut „antritt“ „1“, „2“, „3“, „4“ oder „v“ ist, muss für jedes Prüfungsgebiet bzw. jede Teilprüfung, in dem bzw. der die Prüfungskandidatin oder der Prüfungskandidat eine Klausurarbeit im Rahmen einer abschließenden Prüfung, einer Externistenprüfung, die einer abschließenden Prüfung entspricht oder einer Berufsreifeprüfung abgelegt hat, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>kla_beurteilung</p></td>
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufe der Klausurarbeit (vor einer allfälligen Kompensationsprüfung) oder der Angabe „nicht beurteilt“ (bei vorgetäuschten Leistungen)</p>
<p>in folgender Differenzierung:</p></td>
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
    <td><p>„n“</p></td>
    <td><p>nicht beurteilt</p></td>
  </tr>
  <tr>
    <td><p>schwellenwert</p></td>
    <td colspan="2"><p>mit der Angabe, ob bei einer Beurteilung mit „Nicht genügend“ der Schwellenwert erreicht wurde in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„0“</p></td>
    <td><p>keine Erreichung des Schwellenwerts</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td><p>Erreichung des Schwellenwerts</p></td>
  </tr>
  <tr>
    <td><p>komp_beurteilung</p></td>
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufe bzw. Information bezüglich Kompensationsprüfung, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„c“</p></td>
    <td><p>keine Kompensationsprüfung vorgesehen, bei positiver Beurteilung oder Nichtbeurteilung des Prüfungsgebiets bzw. im Falle einer Berufsreifeprüfung für die Prüfungsgebiete Deutsch, lebende Fremdsprache und Fachbereich</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„f“</p></td>
    <td><p>nicht angetreten</p></td>
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
    <td><p>nicht beurteilt</p></td>
  </tr>
  <tr>
    <td><p>klp_beurteilung</p></td>
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufe der Klausurprüfung (einschließlich einer allfälligen Kompensationsprüfung) oder der Angabe „nicht beurteilt“ (bei vorgetäuschten Leistungen) in folgender Differenzierung:</p></td>
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
    <td><p>nicht beurteilt,, da keine vorgesehen ist oder der Schwellenwert nicht erreicht und die Kompensationsprüfung negativ war</p></td>
  </tr>
  <tr>
    <td><p>schulstufe_beurteilung</p></td>
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufe der einzubeziehenden Leistungen der letzten Schulstufe, in welcher der das Prüfungsgebiet betreffende Unterrichtsgegenstand bzw. die das Prüfungsgebiet betreffenden Unterrichtsgegenstände unterrichtet wurde bzw. wurden oder der Angabe „keine Einbeziehung“, in folgender Differenzierung:</p></td>
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
    <td><p>„k“</p></td>
    <td><p>keine Einbeziehung</p></td>
  </tr>
  <tr>
    <td><p>gesamth_kl_beurteilung</p></td>
    <td colspan="2"><p>mit der Angabe der gesamthaften Beurteilung des Prüfungsgebietes (Klausurarbeit, Kompensationsprüfung, einbezogene Leistung der letzten Schulstufe) in folgender Differenzierung:</p></td>
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
    <td><p>nicht beurteilt</p></td>
  </tr>
</table>

10\. Das Element pruefung ist ein Kind-Element von „ausbildung“, muss für jedes Prüfungsgebiet bzw. jede abschließende Arbeit – mit Ausnahme der Klausurprüfung – in der die Prüfungskandidatin oder der Prüfungskandidat eine abschließende Prüfung, eine Externistenprüfung, die einer abschließenden Prüfung entspricht oder eine Berufsreifeprüfung abgelegt hat, mindestens einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="5"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>pruefungsgebiet</p></td>
    <td colspan="5"><p>mit der Klassifikation der Prüfungsgebiete, gemäß der von der Bundesministerin oder dem Bundesminister zur Verfügung gestellten Liste der Prüfungsgebiete</p></td>
  </tr>
  <tr>
    <td><p>langbezeichnung</p></td>
    <td colspan="5"><p>mit der Langbezeichnung und ggf. inkl. Angabe der betreffenden Fremdsprache bzw. des (schulautonomen) Prüfungsgebietes</p></td>
  </tr>
  <tr>
    <td><p>pruefungsart</p></td>
    <td colspan="5"><p>Mit der Angabe der Prüfungsart zu der die Meldung erfolgt</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„aba“</p></td>
    <td colspan="3"><p>abschließende Arbeit</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„dpa“</p></td>
    <td colspan="3"><p>Diplomarbeit</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„vwa“</p></td>
    <td colspan="3"><p>vorwissenschaftliche Arbeit (auslaufend)</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„mue“</p></td>
    <td colspan="3"><p>Mündliche Prüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„pra“</p></td>
    <td colspan="3"><p>Projektarbeit im Rahmen der BRP</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„vp“</p></td>
    <td colspan="3"><p>Vorprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„zp“</p></td>
    <td colspan="3"><p>Zusatzprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„vor“</p></td>
    <td colspan="3"><p>vorgezogene Teilprüfung</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2"><p>„tei“</p></td>
    <td colspan="3"><p>Teilprüfung (BRP)</p></td>
  </tr>
  <tr>
    <td><p>termin_pruefungsgebiet</p></td>
    <td colspan="5"><p>mit der Angabe des Prüfungstermins, an dem das Ergebnis erzielt wurde</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„ht-JJJJ“</p></td>
    <td colspan="2"><p>für ein Ergebnis aus dem Haupttermin; so wäre zB für den Haupttermin des Schuljahres 2021/22 hier „ht-2022“ einzutragen</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„he-JJJJ“</p></td>
    <td colspan="2"><p>für ein Ergebnis aus dem Herbsttermin</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„wi-JJJJ“</p></td>
    <td colspan="2"><p>für ein Ergebnis aus dem Wintertermin</p></td>
  </tr>
  <tr>
    <td><p>datum</p></td>
    <td colspan="4"><p>„JJJJ-MM-TT“</p></td>
    <td><p>mit der Angabe des Datums der Prüfung des Prüfungsgebiets, im Falle einer abschließenden Arbeit ist das Datum der Präsentation anzugeben.</p></td>
  </tr>
  <tr>
    <td><p>antritt</p></td>
    <td colspan="5"><p>mit der Angabe des Antritts in gegenständlichem Prüfungsgebiet</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„1“</p></td>
    <td colspan="4"><p>1. Antritt</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„2“</p></td>
    <td colspan="4"><p>1. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„3“</p></td>
    <td colspan="4"><p>2. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„4“</p></td>
    <td colspan="4"><p>3. Wiederholung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„v“</p></td>
    <td colspan="4"><p>Ergebnis aus einem Vortermin</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„g“</p></td>
    <td colspan="4"><p>gerechtfertigt verhindert</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„u“</p></td>
    <td colspan="4"><p>ungerechtfertigt ferngeblieben</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„a“</p></td>
    <td colspan="4"><p>Anerkennung</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„b“</p></td>
    <td colspan="4"><p>entfällt oder befreit</p></td>
  </tr>
</table>

11\. Das Element pruefung\_ergebnis ist ein Kind-Element von „pruefung“, ist nur erforderlich, wenn das Attribut „antritt“ „1“, „2“, „3“, „4“ oder „v“ ist; muss für jedes Prüfungsgebiet bzw. jede abschließende Arbeit – mit Ausnahme der Klausurprüfung – in der die Prüfungskandidatin oder der Prüfungskandidat eine abschließende Prüfung, eine Externistenprüfung, die einer abschließenden Prüfung entspricht oder eine Berufsreifeprüfung abgelegt hat, einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>pr_beurteilung</p></td>
    <td colspan="4"><p>mit der Angabe der Beurteilungsstufen der Prüfung in folgender Differenzierung (bei Anerkennung ist die Note der anerkannten Prüfung einzugeben):</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„1“</p></td>
    <td><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„2“</p></td>
    <td><p>Gut</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„3“</p></td>
    <td><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„4“</p></td>
    <td><p>Genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„5“</p></td>
    <td><p>Nicht genügend</p></td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3"><p>„n“</p></td>
    <td><p>nicht beurteilt</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>schulstufe_beurteilung</p></td>
    <td colspan="3"><p>mit der Angabe der Beurteilungsstufe der einzubeziehenden Leistungen der letzten Schulstufe, in welcher der das Prüfungsgebiet betreffende Unterrichtsgegenstand bzw. die das Prüfungsgebiet betreffenden Unterrichtsgegenstände unterrichtet wurde bzw. wurden oder der Angabe „keine Einbeziehung“, in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Gut</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Genügend</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„k“</p></td>
    <td colspan="2"><p>Einbeziehung nicht vorgesehen</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„v“</p></td>
    <td colspan="2"><p>Ausschluss der Einbeziehung durch die Prüfungskommission</p></td>
  </tr>
  <tr>
    <td colspan="2"><p>gesamth_pr_beurteilung</p></td>
    <td colspan="3"><p>mit der Angabe der gesamthaften Beurteilung des Prüfungsgebietes (Ergebnis der Prüfung mitsamt der gegebenenfalls einzubeziehenden Leistungen der letzten Schulstufe, in welcher der das Prüfungsgebiet betreffende Unterrichtsgegenstand bzw. die das Prüfungsgebiet betreffenden Unterrichtsgegenstände unterrichtet wurde bzw. wurden) in folgender Differenzierung:</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„1“</p></td>
    <td colspan="2"><p>Sehr gut</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„2“</p></td>
    <td colspan="2"><p>Gut</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„3“</p></td>
    <td colspan="2"><p>Befriedigend</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„4“</p></td>
    <td colspan="2"><p>Genügend</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„5“</p></td>
    <td colspan="2"><p>Nicht genügend</p></td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td><p>„n“</p></td>
    <td colspan="2"><p>nicht beurteilt</p></td>
  </tr>
</table>

12\. Das Element brp\_pruefung\_ergebnis ist ein Kind-Element von „pruefung\_ergebnis“, muss für Prüfungskandidatinnen und Prüfungskandidaten der Berufsreifeprüfung in den Prüfungsgebieten „Deutsch“ und „Fachbereich“ im Falle einer erfolgten Beurteilung je einmal vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>brp_pr_beurteilung</p></td>
    <td colspan="2"><p>mit der Angabe der Beurteilungsstufen der Prüfung in folgender Differenzierung (bei Anerkennung ist die Note der anerkannten Prüfung einzugeben):</p></td>
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
    <td><p>nicht beurteilt</p></td>
  </tr>
</table>

13\. Das Element abschlussdetails ist ein Kind-Element von „ausbildung“, muss genau einmal pro Prüfungskandidatin oder pro Prüfungskandidaten bzw. pro Schülerin oder pro Schüler einer Abschlussklasse oder eines Abschlussjahrganges ohne Antrittsberechtigung und Datenmeldung vorhanden sein und weist folgende Attribute auf:

<table>
  <tr>
    <td><p>Attribut</p></td>
    <td colspan="2"><p>Wert</p></td>
  </tr>
  <tr>
    <td><p>termin</p></td>
    <td colspan="2"><p>mit dem Datum des Prüfungszeugnisses (bzw. der letzten Prüfung, wenn kein Zeugnis ausgestellt wurde). Im Falle einer Nichtantrittsberechtigung oder einem Nichtantreten ist hier das Datum des letzten Zeugnisses der Abschlussklasse bzw. des Abschlussjahrgangs einzutragen.</p></td>
  </tr>
  <tr>
    <td><p>ergebnis</p></td>
    <td colspan="2"><p>mit der Angabe über die Gesamtbeurteilung dieser abschließenden Prüfung in den folgenden Ausprägungen:</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„na“</p></td>
    <td><p>zur abschließenden Prüfung nicht antrittsberechtigt</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ka“</p></td>
    <td><p>zu keinem Prüfungsgebiet der abschließenden Prüfung angetreten</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ae“</p></td>
    <td><p>mit ausgezeichnetem Erfolg bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„ge“</p></td>
    <td><p>mit gutem Erfolg bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„be“</p></td>
    <td><p>bestanden</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nw“</p></td>
    <td><p>nicht bestanden mit Wiederholungsmöglichkeit</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„nb“</p></td>
    <td><p>nicht bestanden ohne weitere Wiederholungsmöglichkeit</p></td>
  </tr>
  <tr>
    <td></td>
    <td><p>„vn“</p></td>
    <td><p>Vollständigkeit noch nicht gegeben, da (Teil)-Prüfungen noch offen sind bzw. bei der BRP ein Teil der Prüfungen in Deutsch oder Fachbereich noch offen ist.</p></td>
  </tr>
</table>
