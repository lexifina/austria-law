## Anlage 1

## Einzelheiten zu meldender Daten

## Tabelle 1

## Meldepflichtige Einzelheiten von Energiegroßhandelsprodukten im Zusammenhang mit der Nominierung und Allokation von Strom

<table>
  <tr>
    <td><p>Feld Nr.</p></td>
    <td><p>Feldinhalt</p></td>
    <td><p>Beschreibung</p></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><p>Belegkopf des Fahrplans</p></td>
  </tr>
  <tr>
    <td><ul>
<li>1.</li>
</ul></td>
    <td><p>Dokumentenkennung</p></td>
    <td><p>Eindeutige Kennung des Dokuments, für das die Zeitreihendaten übermittelt werden.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>2.</li>
</ul></td>
    <td><p>Version des Dokuments</p></td>
    <td><p>Version des übermittelten Dokuments. Ein Dokument kann mehrere Male übermittelt werden, wobei jede Übermittlung – beginnend mit 1 – schrittweise ansteigend als neue Version des Dokuments gekennzeichnet wird.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>3.</li>
</ul></td>
    <td><p>Art des Dokuments</p></td>
    <td><p>Code der übermittelten Dokumentenart.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>4.</li>
</ul></td>
    <td><p>Art des Prozesses</p></td>
    <td><p>Die Art des Prozesses auf welchen das Dokument verweist.</p>
<p>Mögliche Werte sind:</p>
<p>A01 – Day-Ahead Fahrplan</p>
<p>A02 – Intraday Fahrplan</p>
<p>etc.</p>
<p>anhängig davon, ob die Übermittlung in einer einzigen Übermittlung durchgeführt wird (Day-Ahead, Intraday am Ende des Tages) oder mittels mehrerer Übermittlungen die den Tag abdecken.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>5.</li>
</ul></td>
    <td><p>Art der Fahrplan-Klassifizierung</p></td>
    <td><p>Klassifizierung des Fahrplans nach Aggregation und Klassifizierungstyp.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>6.</li>
</ul></td>
    <td><p>Identität des Absenders</p></td>
    <td><p>Kennung der Partei, die das Dokument versandt hat und für dessen Inhalt verantwortlich ist (EIC-Code).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>7.</li>
</ul></td>
    <td><p>Rolle des Absenders</p></td>
    <td><p>Angabe der Rolle des Absenders (TSO, sonstige meldende Stelle).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>8.</li>
</ul></td>
    <td><p>Identität des Empfängers</p></td>
    <td><p>Kennung der Partei, die das Dokument erhält.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>9.</li>
</ul></td>
    <td><p>Rolle des Empfängers</p></td>
    <td><p>Angabe der Rolle des Empfängers.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>10.</li>
</ul></td>
    <td><p>Datum und Uhrzeit der Erstellung</p></td>
    <td><p>Datum und Uhrzeit der Übertragung der Fahrplandaten (ISO 8601).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>11.</li>
</ul></td>
    <td><p>Fahrplan-Zeitraum</p></td>
    <td><p>Anfangs- und Enddatum und –uhrzeit des Zeitintervalls welches vom Dokument, das den Fahrplan beinhaltet, umfasst wird.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>12.</li>
</ul></td>
    <td><p>Bereich</p></td>
    <td><p>Von dem Fahrplan-Dokument abgedeckter Bereich.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>13.</li>
</ul></td>
    <td><p>Subjektpartei (falls anwendbar)</p></td>
    <td><p>Die Partei die dem Fahrplan-Dokument unterliegt.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>14.</li>
</ul></td>
    <td><p>Subjektrolle (falls anwendbar)</p></td>
    <td><p>Angabe der Rolle des Subjekts.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>15.</li>
</ul></td>
    <td><p>Abstimmung-Zeitraum (falls anwendbar)</p></td>
    <td><p>Anfangs- und Enddatum und –zeit des Zeitraums welcher im Fahrplan abgestimmt wird.</p></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><p>Fahrplan-Zeitreihe</p></td>
  </tr>
  <tr>
    <td><ul>
<li>16.</li>
</ul></td>
    <td><p>Absender Zeitreihen-Identifikation</p></td>
    <td><p>Vom Absender zu vergebende Bezeichnung der Zeitreihe.</p>
<p>Diese muss einmalig das gesamte Dokument sein und die Vermeidung einer Duplikation des Produkts, der Art des Geschäftes, der Aggregationsebene des angegebenen Objektes, des Liefergebiets, des Herkunftsgebiets, der Zählpunktbezeichnung, der importierenden Bilanzgruppe, der exportierenden Bilanzgruppe, der Art der Kapazitätsreservierung und der Identifikation der Kapazitätsreservierung garantieren.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>17.</li>
</ul></td>
    <td><p>Absender Zeitreihen-Version</p></td>
    <td><p>Die Zeitreihen-Version wird nur geändert, wenn sich eine Zeitreihe ändert.</p>
<p>Die Zeitreihen-Version muss die gleiche sein, wie die Version des Dokuments in welcher diese hinzugefügt oder geändert wurde. Wenn ein Dokument zurückgesandt wird, müssen alle Zeitreihen, unabhängig davon, ob diese geändert wurden oder nicht, noch einmal übermittelt werden. Im Falle der Löschung einer Zeitreihe, wird diese für alle Zeiträume mit Nullen ausgefüllt und zurückgesandt.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>18.</li>
</ul></td>
    <td><p>Art des Geschäfts</p></td>
    <td><p>Genauere Bezeichnung der Art des Geschäfts, für das ein Fahrplan abgegeben wird. z. B. Erzeugungsfahrplan, interner oder externer Handel</p></td>
  </tr>
  <tr>
    <td><ul>
<li>19.</li>
</ul></td>
    <td><p>Produkt</p></td>
    <td><p>Identifizierung eines Energieproduktes wie Leistung, Energie, Blindleistung, Übertragungskapazität, etc. Mögliches Codes beinhalten z. B. (nicht abschließend):</p>
<p>8716867000016 – Wirkleistung</p></td>
  </tr>
  <tr>
    <td><ul>
<li>20.</li>
</ul></td>
    <td><p>Aggregationsebene des angegebenen Objekts</p></td>
    <td><p>Identifikation der Aggregationsebene eines Fahrplans; z. B. Aggregation je Regelzone oder (virtueller) Zählpunkt (z. B. Übergabestelle).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>21.</li>
</ul></td>
    <td><p>Liefergebiet (falls anwendbar)</p></td>
    <td><p>Gebiet (Zone) in welches das Produkt geliefert wird. Kein Übertragungsnetzbetreiber.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>22.</li>
</ul></td>
    <td><p>Herkunftsgebiet (falls anwendbar)</p></td>
    <td><p>Gebiet (Zone) aus welchem das Produkt geliefert wird. Kein Übertragungsnetzbetreiber.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>23.</li>
</ul></td>
    <td><p>Zählpunktbezeichnung (falls anwendbar)</p></td>
    <td><p>Die Kennung des Ortes an dem ein oder mehrere Produkte gemessen werden.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>24.</li>
</ul></td>
    <td><p>Importierende Bilanzgruppe (falls anwendbar)</p></td>
    <td><p>Energie aufnehmende Bilanzgruppe.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>25.</li>
</ul></td>
    <td><p>Exportierende Bilanzgruppe (falls anwendbar)</p></td>
    <td><p>Energie abgebende Bilanzgruppe.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>26.</li>
</ul></td>
    <td><p>Art der Kapazitätsreservierung (falls anwendbar)</p></td>
    <td><p>Bezeichnet wie eine bestimmte Kapazitätsreservierung ausgehandelt wurde; z. B. tägliche Auktion, wöchentliche Auktion.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>27.</li>
</ul></td>
    <td><p>Identifikation der Kapazitätsreservierung (falls anwendbar)</p></td>
    <td><p>Verweis auf eine bestimmte Kapazitätsreservierung, die einem Fahrplan zugrunde liegt.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>28.</li>
</ul></td>
    <td><p>Maßeinheit</p></td>
    <td><p>Die Maßeinheit die zum Ausdruck der Menge in der Zeitreihe verwendet wird.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>29.</li>
</ul></td>
    <td><p>Kurvenart (falls anwendbar)</p></td>
    <td><p>Codierte Darstellung der beschriebenen Kurvenart.</p></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><p>Ursache (falls anwendbar)</p></td>
  </tr>
  <tr>
    <td><ul>
<li>30.</li>
</ul></td>
    <td><p>Ursachencode (falls anwendbar)</p></td>
    <td><p>Code zur Angabe, dass die Begründung für eine Änderung im Ursachentext, wörtlich erfolgt.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>31.</li>
</ul></td>
    <td><p>Ursachentext (falls anwendbar)</p></td>
    <td><p>Wörtliche Begründung einer Änderung.</p></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><p>Zeitraum</p></td>
  </tr>
  <tr>
    <td><ul>
<li>32.</li>
</ul></td>
    <td><p>Zeitintervall</p></td>
    <td><p>Anfangs- und Enddatum und -uhrzeit des Zeitintervalls des betreffenden Zeitraums (ISO 8601).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>33.</li>
</ul></td>
    <td><p>Auflösung</p></td>
    <td><p>Auflösung, d. h. Anzahl der Zeiträume, in die sich das Zeitintervall gliedert (ISO 8601).</p></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><p>Intervall, Wiederholende Felder</p></td>
  </tr>
  <tr>
    <td><ul>
<li>34.</li>
</ul></td>
    <td><p>Position</p></td>
    <td><p>Relative Position eines Zeitraums innerhalb eines Zeitintervalls.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>35.</li>
</ul></td>
    <td><p>Menge</p></td>
    <td><p>Die geplante Menge des Produkts für die Position im Zeitintervall.</p></td>
  </tr>
</table>

## Tabelle 2

## Meldepflichtige Einzelheiten im Zusammenhang mit Regelreserveprodukte Strom

A. Ausschreibungen für die Vorhaltung von Regelleistung, alle Angebote

<table>
  <tr>
    <td><p>Feld Nr.</p></td>
    <td><p>Feld</p></td>
    <td><p>Beschreibung</p></td>
  </tr>
  <tr>
    <td><ul>
<li>1.</li>
</ul></td>
    <td><p>Ausschreibung</p></td>
    <td><p>Bezeichnung der Ausschreibung.</p>
<p>Format: _JJJJ_KWXX_(Zusatz)</p>
<p>Werte Regelreservetyp:</p>
<p>PRL ...... Primärregelleistung</p>
<p>SRL ...... Sekundärregelleistung</p>
<p>TRL ...... Ausfallsreserve- und Tertiärregelleistung</p>
<p>JJJJ ....... Jahr</p>
<p>KW ...... Kalenderwoche</p>
<p>XX ........ Nummer der Kalenderwoche</p>
<p>Zusatz: z. B. für Second Call, Last Call</p></td>
  </tr>
  <tr>
    <td><ul>
<li>2.</li>
</ul></td>
    <td><p>Zeitpunkt des Angebots</p></td>
    <td><p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>3.</li>
</ul></td>
    <td><p>Angebotsnummer</p></td>
    <td><p>Eindeutige, einmalige Nummer zur Identifikation des Angebots.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>4.</li>
</ul></td>
    <td><p>Regelreserveanbieter</p></td>
    <td><p>Eindeutige Bezeichnung des Anbieters.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>5.</li>
</ul></td>
    <td><p>Produkt Alias</p></td>
    <td><p>Bezeichnung des Regelreserveprodukts.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>6.</li>
</ul></td>
    <td><p>Lieferzeitraum von</p></td>
    <td><p>Beginn des Vorhaltezeitraums des Regelreserveprodukts.</p>
<p>Format: dd.mm.yyyy</p></td>
  </tr>
  <tr>
    <td><ul>
<li>7.</li>
</ul></td>
    <td><p>Lieferzeitraum bis</p></td>
    <td><p>Ende des Vorhaltezeitraums des Regelreserveprodukts.</p>
<p>Format: dd.mm.yyyy</p></td>
  </tr>
  <tr>
    <td><ul>
<li>8.</li>
</ul></td>
    <td><p>Stunden</p></td>
    <td><p>Zeitdauer, für die Regelreserveleistung vorgehalten wird (in Stunden).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>9.</li>
</ul></td>
    <td><p>Leistung angeboten</p></td>
    <td><p>Regelreserveleistung, die angeboten wird.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>10.</li>
</ul></td>
    <td><p>Einheit von 9</p></td>
    <td><p>Typischerweise MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>11.</li>
</ul></td>
    <td><p>Leistung akzeptiert</p></td>
    <td><p>Teilmenge von 9, die einen Zuschlag erhalten hat.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>12.</li>
</ul></td>
    <td><p>Einheit von 11</p></td>
    <td><p>Typischerweise MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>13.</li>
</ul></td>
    <td><p>Leistungspreis</p></td>
    <td><p>Preis für die Vorhaltung von Regelreserve.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>14.</li>
</ul></td>
    <td><p>Einheit von 13</p></td>
    <td><p>Euro/MW und Stunde der Vorhaltung oder Euro/MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>15.</li>
</ul></td>
    <td><p>Energiepreis</p></td>
    <td><p>Preis für aktivierte positive oder negative Regelreserve.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>16.</li>
</ul></td>
    <td><p>Einheit von 15</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>17.</li>
</ul></td>
    <td><p>Angebotswert</p></td>
    <td><p>Wert der Leistungsvorhaltung akzeptierter Angebote.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>18.</li>
</ul></td>
    <td><p>Einheit von 17</p></td>
    <td><p>Typischerweise Euro.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>19.</li>
</ul></td>
    <td><p>Rang</p></td>
    <td><p>Rang des Angebots innerhalb der Merit Order List für die Erteilung des Zuschlags.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>20.</li>
</ul></td>
    <td><p>Produkt ID</p></td>
    <td><p>Eindeutige, einmalige Nummer zur Kennzeichnung des Produkts (Feld 5).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>21.</li>
</ul></td>
    <td><p>Kennzeichnung Blockgebote</p></td>
    <td><p>Falls anwendbar.</p></td>
  </tr>
</table>

B. Ausschreibungen für Regelenergiegebote (Anpassung der Energiepreise von Sekundär- und Tertiärregelreservegeboten soweit vorgesehen, kurzfristige Ausschreibungen Tertiäregelenergiegebote), alle Angebote

<table>
  <tr>
    <td><p>Feld Nr.</p></td>
    <td><p>Feld</p></td>
    <td><p>Beschreibung</p></td>
  </tr>
  <tr>
    <td><ul>
<li>1.</li>
</ul></td>
    <td><p>Ausschreibung</p></td>
    <td><p>Bezeichnung der Ausschreibung.</p>
<p>Format: _JJJJ_MM_DD</p>
<p>Werte Regelreservetyp:</p>
<p>SRL_DA ...... Sekundärregelleistung</p>
<p>TRL_DA ...... Ausfallsreserve- und Tertiärregelleistung</p>
<p>JJJJ ....... Jahr</p>
<p>MM ...... Monat</p>
<p>XX ........ Tag</p></td>
  </tr>
  <tr>
    <td><ul>
<li>2.</li>
</ul></td>
    <td><p>Zeitpunkt des Angebots</p></td>
    <td><p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>3.</li>
</ul></td>
    <td><p>Angebotsnummer</p></td>
    <td><p>Eindeutige, einmalige Nummer zur Identifikation des Angebots.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>4.</li>
</ul></td>
    <td><p>Regelreserveanbieter</p></td>
    <td><p>Eindeutige Bezeichnung des Anbieters.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>5.</li>
</ul></td>
    <td><p>Produkt Alias</p></td>
    <td><p>Bezeichnung des Regelreserveprodukts.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>6.</li>
</ul></td>
    <td><p>Lieferzeitraum von</p></td>
    <td><p>Beginn des Vorhaltezeitraums des Regelreserveprodukts.</p>
<p>Format: dd.mm.yyyy</p></td>
  </tr>
  <tr>
    <td><ul>
<li>7.</li>
</ul></td>
    <td><p>Lieferzeitraum bis</p></td>
    <td><p>Ende des Vorhaltezeitraums des Regelreserveprodukts.</p>
<p>Format: dd.mm.yyyy</p></td>
  </tr>
  <tr>
    <td><ul>
<li>8.</li>
</ul></td>
    <td><p>Stunden</p></td>
    <td><p>Zeitdauer, für die Regelreserveleistung vorgehalten wird (in Stunden).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>9.</li>
</ul></td>
    <td><p>Leistung angeboten</p></td>
    <td><p>Regelreserveleistung, die angeboten wird.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>10.</li>
</ul></td>
    <td><p>Einheit von 9</p></td>
    <td><p>Typischerweise MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>11.</li>
</ul></td>
    <td><p>Leistung akzeptiert</p></td>
    <td><p>Teilmenge von 9, die einen Zuschlag erhalten hat (Feld kann leer sein bei Tertiärregelenergiegeboten, die nicht von Market Makern kommen).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>12.</li>
</ul></td>
    <td><p>Einheit von 11</p></td>
    <td><p>Typischerweise MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>13.</li>
</ul></td>
    <td><p>Leistungspreis</p></td>
    <td><p>Preis für die Vorhaltung von Regelreserve (Feld kann leer sein bei Tertiärregelenergiegeboten, die nicht von Market Makern kommen).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>14.</li>
</ul></td>
    <td><p>Einheit von 13</p></td>
    <td><p>Euro/MW und Stunde der Vorhaltung.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>15.</li>
</ul></td>
    <td><p>Energiepreis</p></td>
    <td><p>Preis für aktivierte positive oder negative Regelreserve.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>16.</li>
</ul></td>
    <td><p>Einheit von 15</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>17.</li>
</ul></td>
    <td><p>Angebotswert</p></td>
    <td><p>Wert der Leistungsvorhaltung akzeptierter Angebote.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>18.</li>
</ul></td>
    <td><p>Einheit von 17</p></td>
    <td><p>Typischerweise Euro.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>19.</li>
</ul></td>
    <td><p>Angebotsnummer Leistungsangebot</p></td>
    <td><p>Nur bei Anpassungen der Energiepreise. Verweis auf die Angebotsnummer des ursprünglichen Gebots. (Feld kann leer sein bei Tertiärregelenergiegeboten, die nicht von Marktet Makern kommen).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>20.</li>
</ul></td>
    <td><p>Aktivierte Energie</p></td>
    <td><p>Volumen tatsächlich aktivierter Regelreserve, das einem bestimmten Angebot zugeordnet ist.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>21.</li>
</ul></td>
    <td><p>Einheit von 20</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>22.</li>
</ul></td>
    <td><p>Rang</p></td>
    <td><p>Rang des Angebots innerhalb der Merit Order List für Energieabrufe.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>23.</li>
</ul></td>
    <td><p>Produkt ID</p></td>
    <td><p>Eindeutige, einmalige Nummer zur Kennzeichnung des Produkts (Feld 5).</p></td>
  </tr>
</table>

C. Aktivierte Regelreserve (Zeitreihen im Viertelstundenraster)

<table>
  <tr>
    <td><p>Feld Nr.</p></td>
    <td><p>Feld</p></td>
    <td><p>Beschreibung</p></td>
  </tr>
  <tr>
    <td><ul>
<li>1.</li>
</ul></td>
    <td><p>Zeitstempel</p></td>
    <td><p>Beginn der Viertelstunde.</p>
<p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>2.</li>
</ul></td>
    <td><p>SRL+ Menge</p></td>
    <td><p>Volumen aktivierter Sekundärregelenergie (ohne Ausfallsreserve 24).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>3.</li>
</ul></td>
    <td><p>Einheit von 2</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>4.</li>
</ul></td>
    <td><p>SRL- Menge</p></td>
    <td><p>Volumen aktivierter negativer Sekundärregelenergie.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>5.</li>
</ul></td>
    <td><p>Einheit von 5</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>6.</li>
</ul></td>
    <td><p>INC+ Menge</p></td>
    <td><p>Austausch von Sekundärregelenergie mit benachbarten Regelzonen im Rahmen der Imbalance Netting Cooperation.</p>
<p>Richtung: Import</p></td>
  </tr>
  <tr>
    <td><ul>
<li>7.</li>
</ul></td>
    <td><p>Einheit von 6</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>8.</li>
</ul></td>
    <td><p>INC- Menge</p></td>
    <td><p>Austausch von Sekundärregelenergie mit benachbarten Regelzonen im Rahmen der Imbalance Netting Cooperation.</p>
<p>Richtung: Export</p></td>
  </tr>
  <tr>
    <td><ul>
<li>9.</li>
</ul></td>
    <td><p>Einheit von 8</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>10.</li>
</ul></td>
    <td><p>Settlementpreis INC</p></td>
    <td><p>Verrechnungspreis für 6 und 8.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>11.</li>
</ul></td>
    <td><p>Einheit von 10</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>12.</li>
</ul></td>
    <td><p>SRL+ Durchschnittspreis</p></td>
    <td><p>Mengengewichteter Durchschnittspreis aller Abrufe von 2 in einer Viertelstunde.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>13.</li>
</ul></td>
    <td><p>Einheit von 12</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>14.</li>
</ul></td>
    <td><p>SRL- Durchschnittspreis</p></td>
    <td><p>Mengengewichteter Durchschnittspreis aller Abrufe von 4 in einer Viertelstunde.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>15.</li>
</ul></td>
    <td><p>Einheit von 14</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>16.</li>
</ul></td>
    <td><p>TRL+ Menge</p></td>
    <td><p>Volumen aktivierter positiver Tertiäregelenergie (beinhalte auch Mengen, die als Ausfallsreserve 26 zu verrechnen sind).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>17.</li>
</ul></td>
    <td><p>Einheit von 16</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>18.</li>
</ul></td>
    <td><p>TRL- Menge</p></td>
    <td><p>Volumen aktivierter negativer Tertiärregelenergie.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>19.</li>
</ul></td>
    <td><p>Einheit von 18</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>20.</li>
</ul></td>
    <td><p>TRL+ Durchschnittspreis</p></td>
    <td><p>Mengengewichteter Durchschnittspreis aller Abrufe von 16 in einer Viertelstunde.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>21.</li>
</ul></td>
    <td><p>Einheit von 20</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>22.</li>
</ul></td>
    <td><p>TRL- Durchschnittspreis</p></td>
    <td><p>Mengengewichteter Durchschnittspreis aller Abrufe von 18 in einer Viertelstunde.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>23.</li>
</ul></td>
    <td><p>Einheit von 22</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>24.</li>
</ul></td>
    <td><p>ARE Menge</p></td>
    <td><p>Volumen aktivierter Ausfallsreserve, die von 20 abzuziehen und 2 zuzuschlagen ist.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>25.</li>
</ul></td>
    <td><p>Einheit von 24</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>26.</li>
</ul></td>
    <td><p>ARE Durchschnittspreis</p></td>
    <td><p>Mengengewichteter Durchschnittspreis aller Abrufe von 24 in einer Viertelstunde.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>27.</li>
</ul></td>
    <td><p>Einheit von 26</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>28.</li>
</ul></td>
    <td><p>UA Menge</p></td>
    <td><p>Volumen Rücklieferung für ungewollten Austausch.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>29.</li>
</ul></td>
    <td><p>Einheit von 28</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>30.</li>
</ul></td>
    <td><p>UA Durchschnittspreis</p></td>
    <td><p>Preis Rücklieferung für ungewollten Austausch (EXAA Börsenpreis).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>31.</li>
</ul></td>
    <td><p>Einheit von 30</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>32.</li>
</ul></td>
    <td><p>IGCC+ Menge</p></td>
    <td><p>Austausch von Sekundärregelenergie mit benachbarten Regelzonen im Rahmen der International Grid Control Cooperation.</p>
<p>Richtung: Import</p></td>
  </tr>
  <tr>
    <td><ul>
<li>33.</li>
</ul></td>
    <td><p>Einheit von 32</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>34.</li>
</ul></td>
    <td><p>IGCC- Menge</p></td>
    <td><p>Austausch von Sekundärregelenergie mit benachbarten Regelzonen im Rahmen der International Grid Control Cooperation.</p>
<p>Richtung: Export</p></td>
  </tr>
  <tr>
    <td><ul>
<li>35.</li>
</ul></td>
    <td><p>Einheit von 34</p></td>
    <td><p>Typischerweise MWh.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>36.</li>
</ul></td>
    <td><p>Settlementpreis IGCC</p></td>
    <td><p>Verrechnungspreis für 32 und 34.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>37.</li>
</ul></td>
    <td><p>Einheit von 36</p></td>
    <td><p>Typischerweise Euro/MWh.</p></td>
  </tr>
</table>

D. Informationen über die Ausschreibungen und deren Ergebnisse

<table>
  <tr>
    <td><p>Feld Nr.</p></td>
    <td><p>Feld</p></td>
    <td><p>Beschreibung</p></td>
  </tr>
  <tr>
    <td><ul>
<li>1.</li>
</ul></td>
    <td><p>Ausschreibung</p></td>
    <td><p>Siehe oben Tabellen A und B, Feld 1.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>2.</li>
</ul></td>
    <td><p>Regelreservetyp</p></td>
    <td><p>Werte Regelreservetyp:</p>
<p>PCR ...... Primärregelleistung</p>
<p>SCR ...... Sekundärregelleistung</p>
<p>TCR ...... Ausfallsreserve- und Tertiärregelleistung</p>
<p>SCE…….Sekundärregelenergie</p>
<p>TCE……Ausfallsreserve- und Tertiärregelenergie</p></td>
  </tr>
  <tr>
    <td><ul>
<li>3.</li>
</ul></td>
    <td><p>Subtyp</p></td>
    <td><p>Werte:</p>
<p>First Call</p>
<p>Second Call</p>
<p>Last Call</p>
<p>Emergency Call</p>
<p>Intraday Emergency Call</p></td>
  </tr>
  <tr>
    <td><ul>
<li>4.</li>
</ul></td>
    <td><p>Geplante Öffnung</p></td>
    <td><p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>5.</li>
</ul></td>
    <td><p>Geplante Schließung</p></td>
    <td><p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>6.</li>
</ul></td>
    <td><p>Lieferung von</p></td>
    <td><p>Beginn des Vorhaltezeitraums des Regelreserveprodukts.</p>
<p>Format: dd.mm.yyyy</p></td>
  </tr>
  <tr>
    <td><ul>
<li>7.</li>
</ul></td>
    <td><p>Lieferung bis</p></td>
    <td><p>Ende des Vorhaltezeitraums des Regelreserveprodukts.</p>
<p>Format: dd.mm.yyyy</p></td>
  </tr>
  <tr>
    <td><ul>
<li>8.</li>
</ul></td>
    <td><p>Veröffentlichungsdatum</p></td>
    <td><p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>9.</li>
</ul></td>
    <td><p>Ausschreibungseröffnung</p></td>
    <td><p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>10.</li>
</ul></td>
    <td><p>Ausschreibungsschließung</p></td>
    <td><p>Format: dd.mm.yyyy hh:mm</p></td>
  </tr>
  <tr>
    <td><ul>
<li>11.</li>
</ul></td>
    <td><p>Produkt Alias</p></td>
    <td><p>Bezeichnung des Regelreserveprodukts.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>12.</li>
</ul></td>
    <td><p>Stunden</p></td>
    <td><p>Zeitdauer, für die Regelreserveleistung vorgehalten wird (in Stunden).</p></td>
  </tr>
  <tr>
    <td><ul>
<li>13.</li>
</ul></td>
    <td><p>Ausgeschriebene Menge</p></td>
    <td><p>Regelreserveleistung, die in der Ausschreibung beschafft werden soll.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>14.</li>
</ul></td>
    <td><p>Einheit von 13</p></td>
    <td><p>Typischerweise MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>15.</li>
</ul></td>
    <td><p>Angebotene Menge</p></td>
    <td><p>Summe der angebotenen Regelreserveleistungen.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>16.</li>
</ul></td>
    <td><p>Einheit von 15</p></td>
    <td><p>Typischerweise MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>17.</li>
</ul></td>
    <td><p>Akzeptierte Menge</p></td>
    <td><p>Summe der angebotenen Regelreserveleistungen, die einen Zuschlag erhalten haben.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>18.</li>
</ul></td>
    <td><p>Einheit von 17</p></td>
    <td><p>Typischerweise MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>19.</li>
</ul></td>
    <td><p>Durchschnittspreis</p></td>
    <td><p>Mengengewichteter Durchschnittspreis für ein Regelreserveprodukt.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>20.</li>
</ul></td>
    <td><p>Einheit von 19</p></td>
    <td><p>Euro/MW und Stunde der Vorhaltung oder Euro/MW.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>21.</li>
</ul></td>
    <td><p>Teilnehmer</p></td>
    <td><p>Anzahl der Anbieter, die an der Ausschreibung teilnehmen.</p></td>
  </tr>
  <tr>
    <td><ul>
<li>22.</li>
</ul></td>
    <td><p>Teilnehmer mit Zuschlag</p></td>
    <td><p>Anzahl der Anbieter mit bezuschlagten Angeboten.</p></td>
  </tr>
</table>
