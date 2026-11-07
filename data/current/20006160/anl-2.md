## Anhang 2

## Vorgaben für elektronische Aufzeichnungen und Meldungen

- 1 ALLGEMEINES

Der Abfallsammler oder -behandler hat seine Aufzeichnungen so zu führen, dass die Nachvollziehbarkeit der Abfälle einschließlich der Einhaltung von abfallbezogenen Rechtsvorschriften (zB Vermischungsverbot gemäß AWG 2002, getrennte Erfassung von biogenen Abfällen und von Klärschlämmen gemäß Kompostverordnung) und Bescheidinhalten (für eine Behandlungsanlage zur Behandlung zugelassene Abfallarten) gewährleistet ist. Jede physische Abfallbewegung darf (von jedem Aufzeichnungspflichtigen) immer nur einmal aufgezeichnet werden.

Für die Angabe von Personen, Standorten und Anlagen einschließlich untergeordneter Anlagen sind die im Register gemäß § 22 AWG 2002 enthaltenen Identifikationsnummern zu verwenden. Für die Angabe von Behandlungsverfahren, Anlagentypen, Pufferlagerarten, Abfallarten, Kontaminationsgruppen, Kompostarten und -bezeichnungen, Herkunftspersonenkreise und Quantifizierungsarten sind die am EDM-Portal, edm.gv.at, veröffentlichten Referenztabellen mit Identifikationsnummern und standardisierten Zuordnungen zu verwenden. Bei der Erstellung von Auszügen, Zusammenfassungen und Meldungen ist das am EDM-Portal, edm.gv.at, veröffentlichte Dokument „Dokumentation des XML-Datenformats für Aufzeichnungen, Zusammenfassungen und Jahresabfallbilanzen entsprechend Abfallbilanzverordnung“ anzuwenden.

Die Buchungsarten sind gemäß der am EDM-Portal, edm.gv.at, veröffentlichten Tabelle der Buchungsarten zu verwenden. Ein einfaches Streckengeschäft liegt vor, wenn ein Abfallsammler einen Abfall direkt von einem Übergeber zu einem Übernehmer transportiert, ohne dass hierbei ein Standort des Abfallsammlers angefahren wird. Das Streckengeschäft beginnt mit einer Übergabe in ein Streckengeschäft (durch einen Abfallersterzeuger, Abfallsammler oder Abfallbehandler); der Abfallsammler, der das Streckengeschäft durchführt, übernimmt den Abfall in ein Streckengeschäft und übergibt es aus dem Streckengeschäft an den Abfallbehandler (oder allenfalls an einen weiteren Abfallsammler); dieser übernimmt den Abfall aus einem Streckengeschäft<sup>1</sup>. Ein zusammengesetztes Streckengeschäft liegt vor, wenn das Streckengeschäft in einer Abfolge von mehreren Abfallsammlern abgewickelt wird, wobei im Regelfall nur ein einziger Abfallsammler den Abfall tatsächlich übernimmt und die anderen lediglich rechtlich über die Abholung oder Entgegennahme des Abfalls verfügen.

Lohnarbeit ist das Behandeln von Abfall im Auftrag eines Abfallbesitzers durch einen Abfallbehandler (Lohnbehandler), der keine eigenständige Verfügungsberechtigung in Bezug auf den zu behandelnden und den behandelten Abfall hat. Die Verfügungsberechtigung verbleibt beim Auftraggeber. Der Lohnbehandler<sup>2</sup> führt eine Abfallbehandlung durch und ist damit zur Aufzeichnung verpflichtet.

Bei einer Sammeltour holt ein Abfallsammler Abfälle nacheinander von mehreren Übergebern ab und bringt sie gemeinsam zu einem Empfangsort. Sofern dieser Empfangsort ein Standort des Abfallsammlers ist, handelt es sich um eine Sammeltour. Wenn der Empfangsort von einem anderen Sammler oder Behandler betrieben wird, liegt eine Kombination aus einer Sammeltour mit einem Streckengeschäft vor.

Die Abfallmasse ist in Kilogramm (kg) mit der verwendeten Bestimmungsart (Quantifizierungsart: Messung, Berechnung, Schätzung) anzugeben. Für die Zusammenfassung von Abfallmassen, die mit unterschiedlichen Bestimmungsarten ermittelt wurden, ist diejenige mit der geringeren Genauigkeit anzugeben (wurde zB ein Teil gewogen und ein zweiter Teil geschätzt, so ist für die Bestimmungsart der gesamten Masse „Schätzung“ anzugeben).

Bei den Aufzeichnungen zu Abfallübernahmen, innerbetrieblichen Abfallbewegungen und Abfallübergaben ist für die Angabe der Anlage, aus welcher der Abfall stammt oder welcher der Abfall zugeführt wird, jeweils die konkretest mögliche Abfallbilanzberichtseinheit (BE\_ABIL) zu verwenden; dh. für einen Abfall, der einer bestimmten untergeordneten Anlage zugeführt wird, ist als Verbleibsanlage die untergeordnete Anlage anzugeben, sofern diese gemäß § 4 als für die Nachvollziehbarkeit der Abfälle relevante Anlage angelegt werden muss, und nicht die übergeordnete Anlage.

Ist für Herkunft oder Verbleib die Anlage anzugeben, ist hierfür die Anlagen-GLN zu verwenden. Sofern der Ort des Anfalls oder der Behandlung (der Verwertung) oder der Abfallbehandler nicht aus der Anlagen-GLN eindeutig zuordenbar ist, sind zusätzlich zur Anlagen-GLN der Aufstellungsstandort (bei mobilen Anlagen durch Angabe des Bezirks oder bei Betrieb innerhalb einer Abfallbehandlungsanlage durch Angabe der zugehörigen stationären Behandlungsanlage) und der Abfallbehandler anzugeben (vgl. mobile Anlagen und Lohnarbeit).

Wenn Abfälle außerhalb einer Anlage anfallen oder behandelt (verwertet) werden, ist statt der Anlage der Ort des Anfalls oder der Behandlung (der Verwertung) anzugeben.

Für die Angabe des Absende-, Empfangs-, Anfalls- oder Behandlungsortes ist die Standort-GLN zu verwenden. Wenn keine Standort-GLN vorhanden ist, sind die Adresse und der jeweilige Inhaber, falls keine Adresse vorhanden ist, die Katastralgemeinde und die Grundstücksnummern des Absende-, Empfangs-, Anfalls- oder Behandlungsortes und der jeweilige Inhaber anzugeben. Die Angabe der Straße, Haus-, Stiege-, Stock- und Türnummer einer Adresse kann bis zum 31. Dezember 2011 als unstrukturierte Angabe in der „Ersten Adresszeile“ der XML-Struktur der Adresse erfolgen, danach ist die strukturierte Angabe erforderlich.

Ist für Herkunft oder Verbleib der Inhaber eines Standortes oder einer Anlage, der Übergeber, der Übernehmer, der Lohnarbeiter oder die Gemeinde anzugeben, ist hierfür die Personen-GLN zu verwenden. Wenn dieser über keine Personen-GLN verfügt, sind Name, Sitz und Branche anzugeben.

- 2 ÜBERNAHME VON ABFALL VON EINER ANDEREN RECHTSPERSON

Für jede Abfallübernahme von einer anderen Rechtsperson ist getrennt aufzuzeichnen:

- – Buchungsart,

- – Datum der Übernahme,

- – als Herkunft – sofern in diesem Anhang nicht anderes geregelt ist – der Absendeort des Übergebers,

- – Abfallart,

- – Abfallmasse und

- – als Verbleib – sofern in diesem Anhang nicht anderes geregelt ist – die Anlage und das Behandlungsverfahren, der/dem der Abfall

  zugeführt wurde.

Bei Übernahme von Abfällen im Rahmen eines Bau- und Abbruchvorhabens ist als Herkunft der Anfallsort anzugeben.

Bei Übernahme von Siedlungsabfällen oder Verpackungsabfällen direkt von Abfallersterzeugern im Rahmen der kommunalen Sammlung ist als Herkunft die Personen-GLN der Gemeinde und die Spezial-GTIN für „Abfallersterzeuger von Siedlungsabfällen“

oder „Abfallersterzeuger von Verpackungsabfällen“ anzugeben und jeweils eine Liste aller Übergeber gemäß § 3 Abs. 2 und 4 der Abfallnachweisverordnung 2003 zu führen. Die Abfallmasse der pro Gemeinde gesammelten Siedlungsabfälle und Verpackungsabfälle ist pro Tag und Abfallart aufzuzeichnen.

Bei Anlieferung von Sammelstellen im Rahmen der kommunalen Sammlung (zB Problemstoffsammelstellen, Mistplätze) ist statt dem Absendeort die Personen-GLN der Gemeinde anzugeben, sofern nicht eine Regelung zur getrennten Sammlung eine detailliertere Herkunftsangabe fordert. Bei Übernahme von Kleinmengen von privaten Haushalten oder ähnlichen Einrichtungen gemäß Anlage 6 Punkt 1.c der Kompostverordnung ist als Herkunft die Personen-GLN der Gemeinde und die Spezial-GTIN für „Kleinanlieferer“ anzugeben.

In allen anderen Fällen einer Übernahme von Abfällen direkt von Abfallersterzeugern ist zusätzlich zum Absendeort des Übergebers die Spezial-GTIN für „Abfallersterzeuger“ anzugeben.

Bei Übernahme aus einem Streckengeschäft ist als Herkunft der Übergeber (dh. derjenige, der über den Abfall rechtlich verfügt) anzugeben.

Bei Übernahme in ein Streckengeschäft hat der Aufzeichnungspflichtige als Verbleib seine Personen-GLN anzugeben. Bei Rück-Übernahme aus Lohnarbeit ist als Herkunft der Lohnarbeiter, der Behandlungsort, an dem die Lohnarbeit erfolgte, die Abfallbehandlungsanlage, aus welcher der Abfall stammt, und das Behandlungsverfahren, dem der Abfall unterzogen wurde, anzugeben.

- 3 INNERBETRIEBLICHE ABFALLBEWEGUNG

Für jede innerbetriebliche Abfallbewegung ist getrennt aufzuzeichnen:

- – Buchungsart,

- – Datum oder Zeitraum der innerbetrieblichen Abfallbewegung,

- – als Herkunft – sofern in diesem Anhang nicht anderes geregelt ist – die Anlage, aus welcher der Abfall stammt, und das Behandlungsverfahren, bei dem der Abfall angefallen ist (dies schließt auch „lagern“ für den Output aus einem Lager ein),

- – Abfallart,

- – Abfallmasse,

- – als Verbleib – sofern in diesem Anhang nicht anderes geregelt ist – die Anlage und das Behandlungsverfahren (dies schließt auch „lagern“ für den Input in ein Lager ein), der/dem der Abfall zugeführt wurde.

Bei innerbetrieblichen Abfällen, die nicht bei einer Abfallbehandlung anfallen oder aus einer Abfalllagerung kommen, ist als Herkunft entsprechend den Vorgaben des Punktes 1 („Allgemeines“) die Anlage, der Aufstellungsort oder der Anfallsort und die GTIN für das Behandlungsverfahren P1 „Abfall aus dem Produktions- oder Dienstleistungsbereich“ gemäß Abfallnachweisverordnung 2003 anzugeben.

Für Stoffe, die im Falle eines Endens der Abfalleigenschaft auf Basis einer Verordnung wie zB der Kompostverordnung oder im Einzelfall auf Basis eines Feststellungsbescheides in den Wirtschaftskreislauf zurückgeführt werden, ist als Verbleib ein (Verwertungs-)Verfahren zur Produktherstellung gemäß Anhang 1 der Abfallnachweisverordnung 2003 (zB R3g) und ein entsprechendes Lager gemäß Anhang 1 Z 9 anzugeben. Die Aufzeichnungen der Stoffe, die in den Wirtschaftskreislauf zurückgeführt werden, können über einen Zeitraum von maximal zwei Wochen zusammengefasst werden, sofern hiermit die Nachvollziehbarkeit der Abfälle, einschließlich der Einhaltung der rechtlichen Anforderungen, noch gewährleistet ist. In bestehenden Verordnungen zum AWG 2002 enthaltene zusätzliche Aufzeichnungsinhalte und abweichende Regelungen zu Aufzeichnungsfristen bleiben unberührt. In besonderen Fällen, in denen die Nachvollziehbarkeit der Abfälle bei einer Zusammenfassung über einen Zeitraum von mehr als zwei Wochen gesichert gewährleistet ist, ist eine Zusammenfassung über einen Zeitraum von maximal einem Monat zulässig.

- 4 ÜBERGABE VON ABFALL AN EINE ANDERE RECHTSPERSON

Für jede Abfallübergabe an eine andere Rechtsperson ist getrennt aufzuzeichnen:

- – Buchungsart,

- – Datum der Übergabe,

- – als Herkunft – sofern in diesem Anhang nicht anderes geregelt ist – die Anlage, aus welcher der Abfall stammt, und das Behandlungsverfahren, bei dem der Abfall angefallen ist,

- – Abfallart,

- – Abfallmasse und

- – als Verbleib – sofern in diesem Anhang nicht anderes geregelt ist – der Empfangsort des Übernehmers.

Bei Übergabe in ein Streckengeschäft ist als Verbleib der Übernehmer (dh. derjenige, der über den Abfall rechtlich verfügt) anzugeben. Bei Übergabe aus einem Streckengeschäft hat der Aufzeichnungspflichtige als Herkunft seine Personen-GLN anzugeben. Bei Übergabe in Lohnarbeit ist als Verbleib der Lohnarbeiter, der Behandlungsort, an dem die Lohnarbeit erfolgt, die Abfallbehandlungsanlage, welcher der Abfall zugeführt wird, und das Behandlungsverfahren, dem der Abfall unterzogen wird, anzugeben.

- 5 LAGERSTAND

Zu Beginn jedes Monats, gegebenenfalls nur zum Ende jedes Kalenderjahres (vgl. § 5 Abs. 2), ist für jedes Lager und für jede Anlage, die über ein zugehöriges Input- oder Outputpufferlager verfügt, nach Pufferlagerart (sofern vorhanden) und für jede Abfallart, die der Aufzeichnungspflichtige extra erfassen möchte, die Lagermenge getrennt aufzuzeichnen; eine Schätzung ist zulässig. Eine Mischung verschiedener Abfälle aus den Übernahmen von Abfällen von anderen Rechtspersonen und innerbetrieblichen Abfallbewegungen im Input-Pufferlager kann ohne Angabe einer Abfallart aufgezeichnet werden. Im Bedarfsfall ist einmal monatlich eine Lagerstandskorrektur aufzuzeichnen. An einem Kalendertag darf für jede Abfallart nur eine Lagerstandsbuchung durchgeführt werden.

- 6 ABFALLARTENNEUZUORDNUNG

Wird, zB Rahmen der Eingangskontrolle, festgestellt, dass die ursprünglich zugeordnete Abfallart nicht korrekt ist, so hat eine Abfallartenneuzuordnung zu erfolgen, die mit der Buchungsart „Abfallartenneuzuordnung“ unter Angabe des Datums, der ursprünglichen Abfallart, der neu zugeordneten Abfallart (bei Abfall mit der Spezifizierung 77 einschließlich allfälliger Kontaminationsgruppen gemäß Zuordnungstabelle am EDM-Portal), der betroffenen Abfallmasse und des Ortes (der Anlage oder, sofern der Abfall noch nicht in eine Anlage eingebracht wurde, des Standortes) zu dokumentieren ist.

- 7 ZUSAMMENFASSUNG

Eine Zusammenfassung der Aufzeichnungen auf Verlangen der Behörde (§ 7) oder für die Jahresabfallbilanz (§ 8) hat

- – für Übernahmen von Abfällen von anderen Rechtspersonen, für innerbetriebliche Abfallbewegungen und für Übergaben von Abfällen an andere Rechtspersonen (gegebenenfalls unter Angabe der Daten gemäß § 8 Abs. 5) gegliedert nach Zeitraum, Buchungsart, Herkunft

- – entsprechend den für die Aufzeichnung festgelegten Anforderungen –, Abfallart, Abfallmasse und Verbleib – entsprechend den für die Aufzeichnung festgelegten Anforderungen – zu erfolgen;

  Für eine Zusammenfassung der Aufzeichnungen können Übernahmen von Abfallersterzeugern gefährlicher oder nicht gefährlicher Abfälle – mit Ausnahme von Übernahmen von Siedlungsabfällen oder Verpackungsabfällen direkt von Abfallersterzeugern im Rahmen der kommunalen Sammlung und von Übernahmen von Kleinmengen von privaten Haushalten oder ähnlichen Einrichtungen gemäß Anlage 6 der Kompostverordnung – pro Bundesland (aus dem der Abfall stammt) und Branche zusammengefasst werden. Die Branche ist gemäß § 5 Abs. 4 entsprechend der Einteilung gemäß Abschnitt 8 Nummer 1.1 der EG-AbfallstatistikV anzugeben.

- – für jede Abfallbilanzberichtseinheit den Lagerstand des Lagers oder des Input- und Output-Pufferlagers (sofern vorhanden) am Beginn und Ende des Berichtszeitraums gegliedert nach jeder extra erfassten Abfallart, für Mischungen verschiedener Abfälle im Input-Pufferlager auch ohne Angabe einer Abfallart, Abfallmasse und Pufferlagerart unter Verwendung der Struktur „Lagerstandsbuchung“ zu enthalten. Zu jeder Lagerstandsangabe am Beginn eines Berichtszeitraums muss auch eine korrespondierende Lagerstandsangabe am Ende des Berichtszeitraums angegeben werden (und umgekehrt);

  Die Lagerstandskorrekturen sind unter Verwendung der Struktur „Lagerstandskorrekturbuchung“ gegliedert nach Pufferlagerart für jede extra erfasste Abfallart, für Mischungen verschiedener Abfälle im Input-Pufferlager auch ohne Angabe einer Abfallart, über den Berichtszeitraum zusammenzufassen.

- – für Abfallartenneuzuordnungen gegliedert nach Zeitraum, ursprünglicher Abfallart, neu zugeordneter Abfallart (bei Abfall mit der Spezifizierung 77 einschließlich allfälliger Kontaminationsgruppen gemäß Zuordnungstabelle am EDM-Portal) und Abfallmasse zu erfolgen. Die Ortsangabe kann entfallen.

\_\_\_\_\_\_\_\_\_\_\_\_\_

1 Wesentlich ist hierbei, dass in den Aufzeichnungen der Übergaben und Übernahmen für die Identifikation des Abfallsammlers, der das Streckengeschäft durchführt, in der Regel eine Personen-GLN aufzuzeichnen ist.

2 Als Abfallbehandler benötigt der Lohnarbeiter eine Berechtigung für seine Tätigkeit gemäß § 24 oder § 25 AWG 2002.
