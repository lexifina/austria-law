### Anhang 7

## Vorgaben zum elektronischen Datenmanagement

- 1. STAMMDATEN FÜR DEPONIEN

Im Stammdatenregister gemäß § 22 AWG 2002 sind die im Folgenden genannten Daten anzugeben, wobei bei Anlagen gemäß den Z 7 bis 15 auch die Umrisspolygone anzugeben sind.

### Stammdaten

- 1. Name, Anschrift (Sitz) des Deponieinhabers und eine für die Zustellung maßgebliche inländische Geschäftsanschrift, einschließlich einer Telefaxnummer;

- 2. sofern vorhanden: Firmenbuchnummer, Vereinsregisternummer, Ergänzungsregisternummer;

- 3. Branchencode (vierstellig);

- 4. Adressen und Bezeichnungen der Standorte; im Falle des Betreibens einer mobilen Anlage, ist an der Sitzadresse ein Standort einzutragen;

- 5. Grundstücke (Katastralgemeinde und Grundstücksnummern), auf denen sich der jeweilige Standort befindet, ÖSTAT-Gemeindekennzahl (wird vom System aus der Angabe zur Standortadresse generiert);

- 6. die Behandlungsverfahren, die am jeweiligen Standort durchgeführt werden;

- 7. die gesamte Betriebsanlage für jeden Standort der registrierten Person;

- 8. jede Deponie mit dem genehmigten Deponiebereich (das Umrisspolygon muss für den Deponiebereich angegeben werden); in Abhängigkeit vom Genehmigungsbescheid können auch mehrere Deponien an einem Standort eingetragen werden;

- 9. jedes Kompartiment mit Angabe der zugehörigen Deponie(unter)klasse und dem jeweiligen Status durch Angabe der Phase (zB Ablagerungsphase); für jede Deponie muss zumindest ein Kompartiment eingetragen werden;

- 10. jeden Kompartimentsabschnitt und den verbleibenden Teil des Kompartiments;

- 11. jedes Zwischenlager gemäß § 33;

- 12. jede andere Anlage innerhalb des Deponiebereichs gemäß § 34; gegebenenfalls Zuordnung zu einem anderem Betreiber gemäß § 40 Abs. 2;

- 13. jede mobile Anlage, die im Deponiebereich als mobile Anlage betrieben wird; anstelle der Umrisspolygone kann die konkrete Anlage, in der die mobile Anlage aufgestellt wird, angegeben werden; mobile Anlagen sind als solche zu kennzeichnen;

- 14. Deponiesickerwasser- und Abwasserbehandlungsanlagen;

- 15. Deponiegasanlagen;

- 16. Anlagen gemäß den Z 7 bis 14 sind soweit zutreffend als Berichtseinheiten mit Angabe des Typs der Berichtseinheit, zB Berichtseinheit für Abfall-Input-Output-Meldungen oder Jahresabfallbilanzmeldungen – BE_ABIL, zu kennzeichnen. Für die Kennzeichnung von Anlagen als BE_ABIL ist das Dokument „Abgrenzung von relevanten Anlagen“, veröffentlicht am EDM-Portal, edm.gv.at, anzuwenden;

- 17. die Beziehungen der Anlagen gemäß den Z 8 bis 15 untereinander und zur gesamten Betriebsanlage gemäß Z 7 sind durch Verwendung der Attribute „gehört zu“ und „besteht aus“ anzugeben;

- 18. Für jede Anlage gemäß den Z 7 bis 15 sind alle zutreffenden Anlagentypen anzugeben. Bei der gesamten Betriebsanlage müssen abweichend dazu nur die wesentlichen Anlagentypen angegeben werden. Für jede Anlage, in der Abfälle behandelt werden, ist jedenfalls ein Anlagentyp (zutreffendenfalls mehrere Anlagentypen) aus der Liste von Anlagentypen für die Abfallbehandlung und -lagerung anzugeben. Sofern (auch) andere Anlagentypen zutreffen, sind diese aus der jeweils zutreffenden Liste von Anlagentypen auszuwählen;

- 19. Kontaktadressen, einschließlich vorhandener e-Mail-Adressen, und Kontaktpersonen (Standort);

- 20. das Deponieaufsichtsorgan durch Name und GLN, wenn keine GLN vorhanden ist, durch Name und Adresse; den Angaben ist der Bestellungsbescheid zugrunde zu legen [insbesondere bezüglich der Angabe, ob eine juristische Person (zB ein technisches Büro) oder eine natürliche Person (zB ein Mitarbeiter eines technischen Büros) als Deponieaufsichtsorgan bestellt wurde];

- 21. Name und Adresse des Ausstufungsverantwortlichen;

und die zugehörigen Identifikationsnummern.

- 2. VORGABEN FÜR ELEKTRONISCHE AUFZEICHNUNGEN UND MELDUNGEN

- 2.1. Allgemeines

Die nachfolgenden Aufzeichnungen sind für jede Anlage gemäß § 40 Abs. 1 Z 2 bis 6 (relevante Anlagen) getrennt zu führen.

Die unten genannten Aufzeichnungen sind unmittelbar bei der Anlieferung von Abfällen an eine dieser Anlagen oder beim Abtransport von Abfällen von einer dieser Anlagen vorzunehmen. Die Aufzeichnungen sind so zu führen, dass die Nachvollziehbarkeit der Abfallströme innerhalb der Deponie gewährleistet ist. Die Aufzeichnungen müssen gegebenenfalls Abfallneuzuordnungen und für Input-Pufferlager, Output-Pufferlager oder eigenständige Lager auch den Lagerstand und etwaige Lagerstandskorrekturen enthalten.

Die Aufzeichnungen sind so zu führen, dass jederzeit ein Auszug oder eine Zusammenfassung aus den Aufzeichnungen entsprechend dem in der ON-Regel 192150 „Datenstrukturen für den elektronischen Datenaustausch in der Abfallwirtschaft“, ausgegeben am 1. November 2007, definierten Datenmodell möglich ist. Die sich daraus ergebenden XML-Datenformat-Strukturen der Aufzeichnungen, XML-Schnittstellen für Auszüge und Meldungen sowie Buchungsarten und Prüfregeln werden auf dem EDM-Portal, edm.gv.at, veröffentlicht. Die Prüfregeln sind für den Berichtszeitraum 2008 im Hinblick auf die Dateninhalte der Deponiemeldungen vor dem 1. März 2008 zu vereinfachen. Für die Berichtszeiträume 2008 bis 2010 sind mit den Prüfregeln alternative Dateninhalte im Bezug auf die XML-Schnittstellen zuzulassen (zB Abfallart gemäß Anhang 5 der Abfallverzeichnisverordnung, BGBl. II Nr. 570/2003, in der geltenden Fassung, statt der GTIN für die Abfallart). Die Prüfregeln für die Berichtszeiträume 2008, 2009 und 2010 werden jeweils im September des vorangehenden Kalenderjahres veröffentlicht.

Inhaber von Deponien oder Abfallsammler oder -behandler als Inhaber von Anlagen gemäß § 40 Abs. 1 Z 2 bis 6 müssen aus ihren Aufzeichnungen über diese Schnittstellen eine einzige XML-Datei (gemäß der Vorgabe „Dokumentation des XML-Datenformats für Abfall-Input-Output-Meldungen entsprechend Deponieverordnung“) mit der Abfall-Input-Output-Meldung aller dieser Anlagen erstellen und am EDM-Portal in das elektronische Register gemäß § 22 AWG 2002 hochladen. Bestehen für den Meldepflichtigen auch Verpflichtungen zur Übermittlung von Abfall-Input-Output-Meldungen nach anderen Rechtsvorschriften, zB gemäß der Abfallverbrennungsverordnung, so sind diese Abfall-Input-Output-Meldungen in einer einzigen Datei hochzuladen. Mit In-Kraft-Treten einer Abfallbilanzverordnung gemäß § 21 Abs. 3 AWG 2002 ist die Abfall-Input-Output-Meldung als Teil der Jahresabfallbilanz hochzuladen.

Auf Verlangen der Behörden müssen die Aufzeichnungen oder eine Zusammenfassung aus den Aufzeichnungen in Form einer XML-Datei (gemäß der Vorgabe „Dokumentation des XML-Datenformats für Abfall-Input-Output-Meldungen entsprechend Deponieverordnung“) über das EDM-Portal an die zuständige Behörde übermittelt werden.

Für die Angabe von Personen, Standorten und Anlagen einschließlich Anlagenteilen sind die im Stammdatenregister enthaltenen Identifikationsnummern zu verwenden. Für die Angabe von Behandlungsverfahren, Anlagentypen, Pufferlagerarten, Abfallarten, Kontaminationsgruppen, Herkunftspersonenkreise und Quantifizierungsarten sind die am EDM-Portal veröffentlichten Referenztabellen mit Identifikationsnummern und standardisierten Zuordnungen zu verwenden. Die Buchungsarten sind gemäß der am EDM-Portal veröffentlichten Tabelle der Buchungsarten zu verwenden.

Die Abfallmasse ist in Kilogramm (kg) mit der verwendeten Bestimmungsart (Quantifizierungsart: Messung, Berechnung, Schätzung) anzugeben. Für die Zusammenfassung von Abfallmassen, die mit unterschiedlichen Bestimmungsarten ermittelt wurden, ist diejenige mit der geringeren Genauigkeit anzugeben (wurde zB ein Teil gewogen und ein zweiter Teil geschätzt, so ist für die Bestimmungsart der gesamten Masse „Schätzung“ anzugeben).

Bei den Aufzeichnungen zu Abfallübernahmen, innerbetrieblichen Abfallbewegungen und Abfallübergaben ist für die Angabe der Anlage, aus der der Abfall stammt, oder der der Abfall zugeführt wird, jeweils die konkreteste Abfallbilanzberichtseinheit (BE_ABIL) zu verwenden, dh. für einen Abfall, der in einem bestimmten Kompartiment abgelagert wird, ist als Verbleibsanlage „Kompartiment“ und nicht „Deponie mit dem Deponiebereich“ anzugeben. Jede physische Abfallbewegung darf immer nur einmal aufgezeichnet werden.

Ist für Herkunft oder Verbleib die Anlage anzugeben, ist hierfür die Anlagen-GLN zu verwenden. Sofern der Ort des Anfalls oder der Behandlung oder der Abfallbehandler nicht aus der Anlagen-GLN eindeutig zuordenbar ist, sind zusätzlich zur Anlagen-GLN der Standort und der Abfallbehandler anzugeben (vgl. mobile Anlagen und Lohnarbeit). Wenn Abfälle außerhalb einer Anlage anfallen oder behandelt werden, ist bei den nachfolgend beschriebenen Buchungen statt der Anlage der Ort des Anfalls oder der Behandlung anzugeben.

Für die Angabe des Absende-, Empfangs-, Anfalls- oder Behandlungsortes ist die Standort-GLN zu verwenden. Wenn keine Standort-GLN vorhanden ist, sind die Adresse und der jeweilige Inhaber, falls keine Adresse vorhanden ist, die Katastralgemeinde und die Grundstücksnummern des Absende-, Empfangs-, Anfalls- oder Behandlungsortes und der jeweilige Inhaber anzugeben.

Die Angabe der Straße, Haus-, Stiege-, Stock- und Türnummer einer Adresse kann bis zum 31. Dezember 2011 als unstrukturierte Angabe in der „Ersten Adresszeile“ der XML-Struktur der Adresse erfolgen, danach ist die strukturierte Angabe erforderlich.

Ist für Herkunft oder Verbleib der Inhaber eines Standortes oder einer Anlage, der Übergeber, der Übernehmer oder der Lohnarbeiter anzugeben, ist hierfür die Personen-GLN zu verwenden. Wenn dieser über keine Personen-GLN verfügt, sind Name, Sitz und Branche anzugeben.

- 2.2. Übernahme von Abfällen von einer anderen Rechtsperson

Wer Abfälle in eine Anlage gemäß § 40 Abs. 1 Z 2 bis 6 übernimmt, muss für jede Abfallübernahme von einer anderen Rechtsperson Folgendes aufzeichnen:

- – Buchungsart,

- – Datum der Übernahme,

- – als Herkunft – sofern in diesem Anhang nichts anderes geregelt ist – den Absendeort,

- – Abfallart,

- – Abfallmasse,

- – Behandlungsverfahren, dem der Abfall zugeführt wird, und

- – GLN der Anlage, der der Abfall zugeführt wird.

Bei Übernahme von Siedlungsabfällen direkt von Abfallerzeugern im Rahmen der kommunalen Sammlung gemäß § 3 Abs. 1 der Abfallnachweisverordnung 2003 ist statt dem Absendeort der Übergeber durch die Spezial-GTIN für „Abfallersterzeuger von Siedlungsabfällen“ anzugeben und eine Liste aller Übergeber zu führen. Die Abfallmasse der gemeinsam gesammelten Siedlungsabfälle ist pro Tag und Abfallart aufzuzeichnen.

Bei Übernahme von Verpackungsabfällen direkt von Abfallerzeugern im Rahmen eines Sammel- und Verwertungssystems gemäß § 3 Abs. 3 der Abfallnachweisverordnung 2003 ist statt dem Absendeort der Übergeber durch die Spezial-GTIN für „Abfallersterzeuger von Verpackungsabfällen“ anzugeben und eine Liste aller Übergeber zu führen. Die Abfallmasse der gemeinsam gesammelten Verpackungsabfälle ist pro Tag und Abfallart aufzuzeichnen.

In allen anderen Fällen einer Übernahme von Abfällen von Abfallersterzeugern ist zusätzlich zum Absendeort die Spezial-GTIN für „Abfallersterzeuger“ anzugeben.

Bei Anlieferung von Sammelstellen im Rahmen der kommunalen Sammlung (zB Problemstoffsammelstellen, Mistplätze) ist statt dem Absendeort die Personen-GLN der Gemeinde anzugeben, sofern nicht eine Regelung zur getrennten Sammlung eine detailliertere Herkunftsangabe fordert.

Bei Übernahme aus einem Streckengeschäft ist statt dem Absendeort der Übergeber (dh. derjenige, der über den Abfall rechtlich verfügt) anzugeben.

Bei Rück-Übernahme aus Lohnarbeit ist zusätzlich zum Standort, an dem die Abfallbehandlung (die Lohnarbeit) erfolgte, die Abfallbehandlungsanlage und das Behandlungsverfahren, dem der Abfall unterzogen wurde, und der Lohnarbeiter anzugeben.

Die Übernahme einer Kleinmenge zur Deponierung gemäß § 13 Abs. 1 und 2 ist durch die Angabe der entsprechenden Buchungsart zu kennzeichnen.

Für einen Abfall, der zur Deponierung übernommen wird, sind weiters die Daten gemäß § 16 Abs. 3 aufzuzeichnen: die Identifikationsnummer des aktuellen Beurteilungsnachweises, sofern kein Beurteilungsnachweis erforderlich ist, die Identifikationsnummer der Abfallinformation, die Angabe zur Abfallerzeugung und Abfallbeschreibung (Abfallerzeuger, Abfallerzeugungsdetails, Abfallerzeugungsprozess und Beschreibung zum Abfall gemäß XML-Datenstruktur).

Bei Aufnahme eines Abfalls in ein Zwischenlager gemäß § 33 Abs. 1 ist der Grund für die Aufnahme in das Zwischenlager aufzuzeichnen.

Eine Zusammenfassung der Aufzeichnungen (§ 41 Abs. 5) auf Verlangen der Behörden oder für zur Deponierung übernommene Abfälle des vorangegangenen Kalenderjahres gemäß § 17 Abs. 3 AWG 2002 hat gegliedert nach Zeitraum, Buchungsart, Herkunft (entsprechend den für die Aufzeichnungen festgelegten Anforderungen), Abfallart, Abfallmasse, Abfallerzeuger, Behandlungsverfahren, dem der Abfall zugeführt wurde, und Anlage, der der Abfall zugeführt wurde, zu erfolgen. In allen anderen Fällen einer Zusammenfassung der Aufzeichnungen für das vorangegangene Kalenderjahr können die Abfallersterzeuger nicht gefährlicher Abfälle pro Bundesland (aus dem der Abfall stammt) und Branche zusammengefasst werden. Für die Untergliederung sind die Bundesland-GLNs für Abfallersterzeuger zu verwenden.

- 2.3. Innerbetriebliche Abfallbewegungen

Für jede innerbetriebliche Abfallbewegung in eine oder aus einer Anlage gemäß § 40 Abs. 1 Z 2 bis 6 ist aufzuzeichnen:

- – Buchungsart,

- – Datum der innerbetrieblichen Abfallbewegung,

- – Anlage, aus der der Abfall stammt,

- – Behandlungsverfahren, bei dem der Abfall angefallen ist (dies schließt auch „Lagerung“ für den Output aus einem Zwischenlager ein),

- – Abfallart,

- – Abfallmasse,

- – Behandlungsverfahren, dem der Abfall zugeführt wird,

- – GLN der Anlage, der der Abfall zugeführt wird.

Bei Primärabfällen, die nicht in einer Anlage angefallen sind, die bereits im Stammdatenregister erfasst ist, ist die Standort-GLN anzugeben. Als Behandlungsverfahren, bei dem der Abfall angefallen ist, ist für Primärabfälle die GTIN für das Behandlungsverfahren P1 „Abfall aus dem Produktions- oder Dienstleistungsbereich“ gemäß Abfallnachweisverordnung 2003 anzugeben.

Für einen Abfall zur Deponierung sind weiters die Identifikationsnummer des aktuellen Beurteilungsnachweises, sofern kein Beurteilungsnachweis erforderlich ist, die Identifikationsnummer der Abfallinformation, Angaben zur Abfallerzeugung und Abfallbeschreibung (Abfallerzeuger, Abfallerzeugungsdetails, Abfallerzeugungsprozess und Beschreibung zum Abfall gemäß XML-Datenstruktur) aufzuzeichnen.

Bei der Deponierung eines Abfalls, der gemäß § 33 Abs. 1 in einem Zwischenlager für eine Identitätskontrolle oder für eine Untersuchung des Deponieaufsichtsorgans gelagert wurde, ist weiters das Ergebnis der Überprüfung und ein eindeutiger Bezug auf die Aufzeichnung der Übernahme gemäß Kapitel 2.1. aufzuzeichnen.

Im Falle der Zurückweisung eines Abfalls und des unmittelbar nachfolgenden Inputs in eine andere Anlage des Deponieinhabers (innerbetriebliche Abfallbewegung) ist die Angabe, dass eine Zurückweisung vorliegt, der Grund für die Zurückweisung und der Bezug zur Aufzeichnung der Übernahme gemäß Kapitel 2.1. anzugeben.

Eine Zusammenfassung der Aufzeichnungen hat gegliedert nach Zeitraum, Buchungsart, Anlage, aus der der Abfall stammt, Verfahren, bei dem der Abfall angefallen ist, Abfallart, Abfallmasse, zutreffendenfalls Zurückweisung, Behandlungsverfahren, dem der Abfall unterzogen wurde, und Anlage, der der Abfall zugeführt wurde, zu erfolgen.

- 2.4. Übergabe von Abfällen an eine andere Rechtsperson

Für jede Abfallübergabe an eine andere Rechtsperson ist aufzuzeichnen:

- – Buchungsart,

- – Datum der Übergabe,

- – Anlage, aus der der Abfall stammt,

- – Behandlungsverfahren, bei dem der Abfall angefallen ist,

- – Abfallart,

- – Abfallmasse und

- – als Verbleib – sofern in diesem Anhang nichts anderes geregelt ist – der Empfangsort.

Bei Übergabe in ein Streckengeschäft ist statt dem Empfangsort der Übernehmer (dh. derjenige, der über den Abfall rechtlich verfügt) anzugeben.

Bei Übergabe in Lohnarbeit ist zusätzlich zum Standort, an dem die Abfallbehandlung (die Lohnarbeit) erfolgt, die Abfallbehandlungsanlage und das Behandlungsverfahren, dem der Abfall unterzogen wird, und der Lohnarbeiter anzugeben.

Im Fall der Zurückweisung eines Abfalls ist der Bezug zur Aufzeichnung der Übernahme gemäß Kapitel 2.1. und der Grund für die Zurückweisung anzugeben.

Eine Zusammenfassung der Aufzeichnungen hat gegliedert nach Zeitraum, Buchungsart, Anlage, aus der der Abfall stammt, Verfahren, bei dem der Abfall angefallen ist, Abfallart, Abfallmasse, zutreffendenfalls Zurückweisung und Verbleib (entsprechend den für die Aufzeichnungen festgelegten Anforderungen) zu erfolgen.

- 2.5. Lagerstand

Zu Beginn und am Ende jedes Meldezeitraums und zu Beginn jedes Monats ist für jede Anlage gemäß § 40 Abs. 1 Z 2 bis 6 die Lagermenge des Lagers oder des Input- und Output-Pufferlagers (sofern vorhanden) nach Pufferlagerart und für jede Abfallart, die der Aufzeichnungspflichtige extra erfassen möchte, getrennt aufzuzeichnen; eine Schätzung ist zulässig. Eine Mischung verschiedener Abfälle aus den Abfallübernahmen und innerbetrieblichen Abfallbewegungen in den Pufferlagern kann ohne Angabe einer Abfallart aufgezeichnet werden. Im Bedarfsfall ist einmal monatlich eine Lagerstandskorrektur aufzuzeichnen.

In einer Zusammenfassung der Aufzeichnungen ist für jede Abfallbilanzberichtseinheit der Lagerstand des Lagers oder des Input- und Output-Pufferlagers (sofern vorhanden) am Beginn und Ende des Berichtszeitraums gegliedert nach jeder extra erfassten Abfallart, für Mischungen verschiedener Abfälle im Input-Pufferlager ohne Angabe einer Abfallart, Abfallmasse und Pufferlagerart unter Verwendung der Struktur „Lagerstandsbuchung“ anzugeben. An einem Kalendertag kann für jede Abfallart nur eine Lagerstandsbuchung durchgeführt werden. Zu jeder Lagerstandsangabe am Beginn eines Berichtszeitraums muss auch eine korrespondierende Lagerstandsangabe am Ende des Berichtszeitraums angegeben werden (und umgekehrt). Die Lagerstandskorrekturen sind unter Verwendung der Struktur „Lagerstandskorrekturbuchung“ gegliedert nach Pufferlagerart für jede extra erfasste Abfallart, für Mischungen verschiedener Abfälle im Input-Pufferlager ohne Angabe einer Abfallart, über den Berichtszeitraum zusammenzufassen.

- 2.6. Abfallartenneuzuordnung

Wird, zB im Rahmen der Eingangskontrolle, festgestellt, dass die ursprünglich zugeordnete Abfallart nicht korrekt ist, so hat eine Abfallartenneuzuordnung zu erfolgen, die mit der Buchungsart „Abfallartenneuzuordnung“ unter Angabe des Datums, der ursprünglichen Abfallart, der neu zugeordneten Abfallart (bei Abfall mit der Spezifizierung 77 einschließlich allfälliger Kontaminationsgruppen gemäß Zuordnungstabelle am EDM-Portal), der betroffenen Abfallmasse und des Ortes (der Anlage oder, sofern der Abfall noch nicht in eine Anlage eingebracht wurde, des Standortes) zu dokumentieren ist. Für die Abfall-Input-Output-Meldung sind die Abfallartenneuzuordnungen im Berichtszeitraum, die dieselbe Kombination aus ursprünglicher Abfallart und neu zugeordneter Abfallart betreffen, aufzusummieren und die Ortsangabe kann entfallen.
