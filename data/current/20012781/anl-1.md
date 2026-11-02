## Anlage 1

## 1\. IT-spezifische Erläuterungen

## 1.1 Datenübermittlung

Bei der Datenübermittlung sind alle Datensätze, die in den einzelnen Satzarten die jeweilige Meldeperiode betreffen, zusammenzufassen und gesammelt zu übermitteln.

## 1.2. Spezielle Regelungen für den stationären und spitalsambulanten Bereich (exkl. Pseudonyme)

Wahlweise können alle Datensätze entweder in einer einzelnen Datei oder - getrennt nach Satzarten - in mehreren Dateien zusammengefasst werden. Für die Datei(en) gilt folgende Namenskonvention:

| Stelle | Länge | Typ | Beschreibung |
| --- | --- | --- | --- |
| 1 | 4 | alphanumerisch | Krankenanstalten-Nr. „Kxxx“ (ggf. Krankenanstaltenträger-Nr. „Txxx“) |
| 5 | 4 | alphanumerisch | Periode: T001–T365 (bzw. T366): Tag 1-365 (366), oder M001–M012: Monat Jänner bis Dezember, oder Q001–Q004: 1. bis 4.Quartal, oder H001–H002: 1./2. Halbjahr, oder J001: Gesamtjahr |
| 9 | 3 | alphanumerisch | ggf. Satzart (z. B. „X01“) |
| 9 bzw. 12 | 1 | . | Punkt als Trennzeichen |
| 10 bzw. 13 | 3 | alphanumerisch | Standard-Extension: z. B. „s24“ (für 2024), „s25“ (für 2025) etc. |

Jede Datei kann bei Bedarf auch ZIP-komprimiert übermittelt werden, wobei die beschriebenen Namenskonventionen auch für die Benennung der in der ZIP-Datei enthaltenen Datei(en) anzuwenden sind.

Innerhalb einer Datei sind die einzelnen Satzarten folgendermaßen sortiert zu übermitteln:

<table>
  <tr>
    <td><ul>
<li>1. Satzart K01 – Kostenstellenplan</li>
</ul></td>
  </tr>
  <tr>
    <td><ul>
<li>2. Satzarten X01–X07, I11–I12 (Blockung nach stationärem Aufenthalt/ambulantem Besuch oder Satzart)</li>
</ul></td>
  </tr>
  <tr>
    <td><ul>
<li>3. Satzarten L01–L04</li>
</ul></td>
  </tr>
  <tr>
    <td><ul>
<li>4. Satzarten K02–K16, G01–G02 (nur bei Jahresmeldung zu melden)</li>
</ul></td>
  </tr>
  <tr>
    <td><ul>
<li>5. Satzarten B01–B06</li>
</ul></td>
  </tr>
  <tr>
    <td><ul>
<li>6. Satzart A01</li>
</ul></td>
  </tr>
  <tr>
    <td><ul>
<li>7. Satzart S11</li>
</ul></td>
  </tr>
</table>

## 1.3. Spezielle Regelungen für den extramuralen Bereich sowie für die Pseudonyme des stationären und spitalsambulanten Bereichs

Die Daten werden unter Verwendung gängiger Verschlüsselungsmethoden und in mehrfach gepacktem Format übermittelt. Die Paketierung der Daten erfolgt dabei in mehreren Schichten, wobei in der obersten Schicht eines Pakets eine Steuerdatei im XML-Format („ddxx.paketinfo.xml“ – xx = Trägercode der anliefernden Stelle) enthalten ist, die den Dateninhalt beschreibt.

Innerhalb des Pakets befindet sich dann je Satzart und – für den extramuralen Bereich – Träger der Sozialversicherung ein eigenes ZIP-Archiv, das die eigentliche(n) Satzarten-Datei(en) enthält. Für eine Satzarten-Datei gilt dabei die Namenskonvention „{Trägercode}{Jahr}{Quartal}{Bezeichnung der Satzart}\_{LFNDNR}.txt“.

Bei Pseudonym-Satzarten enthält das ZIP-Archiv zusätzlich eine KEY-Datei.

## 1.4. Dateiformat

Jede Datei ist im UTF8-Format zu kodieren. In der Datei ist für jeden Datensatz eine neue Zeile zu beginnen, Spaltenüberschriften sind generell nicht zu übermitteln. Alle Datenfelder sind zeichensepariert zu übermitteln, wobei als Trennzeichen dafür in allen Satzarten ein Pipe-Symbol („\|“) zu verwenden ist. Innerhalb numerischer Datenfelder sind keine führenden Nullen und innerhalb alphanumerischer Datenfelder keine führenden oder abschließenden Leerzeichen zu übermitteln. Die jeweils angeführte Anzahl der Zeichen ist als maximal erlaubte Anzahl an Zeichen in diesem Feld zu verstehen.

## 2\. Hinweise zur Datenmeldung zu stationären Aufenthalten/ambulanten Besuchen

## 2.1. Satzarten-(Verarbeitungs-)Reihenfolge

Generell gilt, dass bei stationären Aufenthalten/ambulanten Besuchen die Reihenfolge durch die Satzart-Ziffer vorgegeben ist. Das heißt, dass Einträge der Satzart X02 erst nach einem Eintrag für die Satzart X01 erfolgen dürfen (analog für alle weiteren Satzarten). Für die Satzart S11 (Prüf- und Summensatz) existiert nur eine einzige Zeile am Ende der Datei.

Die Blockung nach stationären Aufenthalten/ambulanten Besuchen ist erlaubt. Das heißt, dass sämtliche Datensätze (aufsteigend nach Satzart) in Folge eingegeben werden dürfen. Der nächste stationäre Aufenthalt/ambulante Besuch beginnt wieder mit Satzart X01. Die Blockung nach Satzarten (aufsteigend nach Satzart) ist erlaubt. Das heißt, dass zuerst sämtliche Datensätze der Satzart X01 (für alle stationären Aufenthalte/ambulanten Besuche) und anschließend alle Datensätze der Satzart X02 (für alle durch Satzart X01 bereits bekannten stationären Aufenthalte/ambulanten Besuche) eingegeben werden dürfen (analog für alle weiteren Satzarten).

## 2.2. Ambulante Besuche mit Leistungen am Folgetag

Ambulante Besuche (Satzart X01), bei denen ein Kontakt auf einer Hauptkostenstelle bzw. einem Fachgebiet (Satzart X02) vor Mitternacht beginnt, dazugehörige Leistungen aber erst nach Mitternacht erbracht werden, sind sowohl in der Satzart X01 als auch in der Satzart X02 dem Kalendertag vor Mitternacht zuzuordnen. Bei den dazugehörigen Leistungen (Satzart X04) ist jedoch der Kalendertag nach Mitternacht im Datenfeld „Medizinische Leistung – Datum der Erbringung“ anzugeben.

## 2.3. Funktionscodes

Bei allen mit einem Funktionscode zu befüllenden Datenfeldern ist, sofern nichts anderes festgelegt ist, grundsätzlich der fachliche Funktionscode zu melden.

## 2.4. Intensivdokumentation

## 2.4.1. Erfassungszeitpunkte

| Erfassungszeitpunkt | Satzarten |
| --- | --- |
| Aufnahme | Satzart X02 – Patientenadministration (Aufnahmedaten) |
| Tag 0 (=erste Stunde) | Satzart I11 – SAPS3-Daten |
| Täglich (pro Pflegetag) | Satzart I12 – TISS-A-Daten |
| Entlassung | Satzart X02 – Patientenadministration (Entlassungsdaten) |

## 2.4.2. Dateneingabe

Im Rahmen der Intensivdokumentation gilt generell für alle Datenfelder, dass ein nicht befülltes Datenfeld „nicht erhoben“ bzw. „nicht pathologisch“ bedeutet. Bei Dezimalzahlen ist das Dezimaltrennzeichen in Abhängigkeit vom jeweiligen Datenformat explizit anzugeben, wobei ausschließlich das Komma gültig ist (z. B. 6,78).
