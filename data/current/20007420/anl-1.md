## Anlage 1

### Einfache Derivate

- A.1. Futures

  - A.1.1. Anleihenfuture:

  Anzahl der Verträge \* Kontraktgröße (notional contract size) \* Marktwert der cheapest-to-deliver (CTD)- Referenz-Anleihe

  - A.1.2. Zinsenfuture (Interest Rate Future):

  Anzahl der Verträge \* Kontraktgröße (notional contract size)

  - A.1.3. Währungsfuture (Currency Future):

  Anzahl der Verträge \* Kontraktgröße (notional contract size)

  - A.1.4. Aktienfuture:

  Anzahl der Verträge \* Kontraktgröße (notional contract size) \* Marktwert der zugrundeliegenden Aktie

  - A.1.5. Indexfuture:

  Anzahl der Verträge \* Kontraktgröße (notional contract size) \* Index Level

- A.2. Plain Vanilla Optionen (gekaufte/verkaufte Puts und Calls)

  - A.2.1. Plain Vanilla Anleihenoption:

  Vertragswert (notional contract value) \* Marktwert der zugrundeliegenden Referenz-Anleihe \* Delta

  - A.2.2. Plain Vanilla Aktienoption:

  Anzahl der Verträge \* Kontraktgröße (notional contract size) \* Marktwert der zugrundeliegenden Aktie \* Delta

  - A.2.3. Plain Vanilla Zinsoption:

  Vertragswert (notional contract value) \* Delta

  - A.2.4. Plain Vanilla Währungsoption:

  Vertragswert der Währungspaare \* Delta

  - A.2.5. Plain Vanilla Indexoption:

  Anzahl der Verträge \* Kontraktgröße (notional contract size) \* Index Level \* Delta

  - A.2.6. Plain Vanilla Optionen auf Futures:

  Anzahl der Verträge \* Kontraktgröße (notional contract size) \* Marktwert der zugrundeliegenden Basiswerte \* Delta

  - A.2.7. Plain Vanilla Swaption:

  Referenz Swap Commitment Umrechnungswert (gemäß A.3.) \* Delta

  - A.2.8. Optionsscheine und vergleichbare Rechte:

  Anzahl der Aktien oder Anleihen \* Marktwert der zugrundeliegenden Basiswerte \* Delta

- A.3. Swaps

  - A.3.1. Plain Vanilla Fixed/Floating Rate Zinsen und Inflation Swaps:

  Marktwert des Basiswerts

  - A.3.2. Währungs-Swap:

  Nominalwert der Währungskomponente(n)

  - A.3.3. Zins/WährungsSwaps:

  Nominalwert der Währungskomponente(n) oder Währungspaare

  - A.3.4. Total Return Swap:

  Marktwert des zugrundeliegenden Basiswerts

  - A.3.5. Non-Basic Total Return Swap (TRS):

  Marktwert der beiden zugrundeliegenden Komponenten des TRS

  - A.3.6. Single Name Credit Default Swap:

  Protection Seller: Den höheren Wert des Marktwerts des zugrundeliegenden Basiswerts oder des Nominalwerts des Credit Defaults Swap

  Protection Buyer: Marktwert des zugrundeliegenden Basiswerts

  - A.3.7. Contract for Differences:

  Anzahl der Aktien oder Anleihen \* Marktwert des zugrundeliegenden Basiswerts

- A.4. Forwards

  - A.4.1. FX Forwards:

  Nominalwert der Währungskomponente(n)

  - A.4.2. Forward Rate Agreement:

  Nominalwert

- A.5. Leveraged Exposure betreffend Indizes oder Indizes mit eingebettetem Leverage:

  Ein Derivat, das ein gehebeltes Exposure zu einem Index besitzt und ein Index mit eingebautem Hebel müssen die jeweils zutreffenden Commitment-Umrechnungsformeln für die zugrundeliegenden Basiswerte verwenden.

### Eingebettete Derivate

- B.1. Wandelanleihe:

  Anzahl der betreffenden Aktien \* Marktwert der zugrundeliegenden bezugnehmenden Aktien \* Delta

- B.2. Credit Linked Notes:

  Marktwert der zugrundeliegenden Basiswerte

- B.3. Teilweise eingezahlte Wertpapiere

  Anzahl der Aktien oder Anleihen \* Marktwert der zugrundliegenden Vermögensgegenstände

### Exotische Derivate

- C.1. Variance Swaps:

  Variance Notional \* (current) Variancet

  Variance Notional \* min \[(current) Variancet; volatility cap2\]

  bei

[Source image](<https://ogd.ris.bka.gv.at/~/Dokumente/Bundesnormen/NOR40131315/image001.png>)

- C.2. Volatility Swaps:

  Vega Notional \* Volatilityt

  Vega Notional \* min \[(current) Volatilityt oder volatility cap\]

- C.3. Barrier Option:

  Anzahl der Verträge \* fiktive Kontraktgröße (notional contract size) \* Marktwert der zugrundeliegenden Aktie \* max Delta
