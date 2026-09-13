# Quellen und Inspirationen – Finanzen

## Zweck

Diese Datei dokumentiert methodische Referenzen. Sie macht externe Quellen nicht zu automatisch gültiger Projektwahrheit und ersetzt keine aktuelle Prüfung konkreter Produkte, Märkte, Unternehmen, Steuern oder Regulierung.

## Öffentliche Primär-/Behördenquellen

### SEC / Investor.gov

Verwendete Themenräume:

- Asset Allocation und Diversifikation;
- Risiko/Rendite;
- Kosten und Gebühren;
- Liquidität und Eigenschaften von Anlageprodukten.

Referenzen:

- https://www.investor.gov/introduction-investing/getting-started/asset-allocation
- https://www.investor.gov/introduction-investing/getting-started/understanding-fees
- https://www.investor.gov/introduction-investing/investing-basics/investment-products

Übernommen wird die methodische Trennung von Ziel/Zeithorizont/Risiko, Diversifikation, Kosten und Liquidität. US-spezifische Konten-, Steuer- oder Produktlogik ist keine zentrale KI-Regeln-Wahrheit.

### Consumer Financial Protection Bureau (CFPB)

Verwendete Themenräume:

- Cashflow/Budget als reale Ein-/Auszahlungsstruktur;
- Notfall-/Liquiditätsreserven;
- situationsabhängige Höhe von Rücklagen statt eines universellen Fixwerts.

Referenzen:

- https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/
- https://www.consumerfinance.gov/archive/blog/budgeting-how-to-create-a-budget-and-stick-with-it/

## Methodische Agent-Skill-Referenz

### Anthropic `financial-services`

Repository:

- https://github.com/anthropics/financial-services
- Lizenz: Apache-2.0.
- vertieft geprüfter Repository-Stand am 2026-09-06: Commit `69cbc81467a5dced793eee03dec4658aa24ef856`.

Der Repository-Stand wurde als methodischer Referenzraum betrachtet, nicht als automatisch synchronisierte Abhängigkeit. Es wurden keine fremden Skilltexte kopiert und keine Claude-/MCP-/Office-Runtime vorausgesetzt.

### Vertieft betrachtete Bereiche

#### Wealth Management

Insbesondere:

- `financial-plan`;
- `portfolio-rebalance`;
- `investment-proposal`;
- `tax-loss-harvesting` als bewusst stark jurisdiktionsabhängiger Gegenfall.

Nützliche Methoden:

- belastbare Ausgangslage vor Szenariomodellierung;
- Stress-/What-if-Szenarien statt nur eines Base Case;
- aktuellen Portfoliozustand vor Rebalancing bestimmen;
- Rebalancing gegen ein Ziel statt gegen ein abstraktes „besser“;
- Kosten, Liquidität, Cashflows und Steuerfolgen als getrennte Analyseachsen.

#### Financial Analysis

Insbesondere:

- `dcf-model`;
- `comps-analysis`.

Nützliche Methoden:

- Bewertungsinputs, Formeln und Annahmen nachvollziehbar trennen;
- DCF über operative Treiber, Diskontierung, Terminalannahmen und Sensitivitäten analysieren;
- Peer-Gruppen nach wirtschaftlicher Vergleichbarkeit begründen;
- Bewertungsmethoden nicht mit Unternehmensqualität oder Investmentempfehlung gleichsetzen;
- aktuelle Marktdaten und Kapitalstruktur mit Stichtag behandeln.

#### Equity Research

Insbesondere:

- `earnings-analysis`;
- `thesis-tracker`.

Nützliche Methoden:

- aktuelle Ergebnisberichte vor Analyse wirklich verifizieren;
- Beat/Miss nur gegen belegte Guidance beziehungsweise Erwartungsdaten behaupten;
- Investmentthesen falsifizierbar formulieren;
- disconfirming Evidence genauso systematisch verfolgen wie bestätigende Evidence;
- These, aktuelle Datenpunkte und Bewertung als getrennte Ebenen behandeln.

## Bewusst nicht übernommen

Nicht zur allgemeinen KI-Regeln-Wahrheit werden insbesondere:

- 401(k), IRA, Roth, 529, Social Security, RMD, Wash-Sale- oder andere US-spezifische Steuer-/Kontoregeln;
- feste Inflationsannahmen, Rebalancing-Bänder oder Erfolgswahrscheinlichkeits-Zielwerte;
- feste WACC-, Terminal-Growth-, Peer-Multiple- oder andere Bewertungsranges als universelle Defaults;
- automatische Trade-Listen oder Buy/Hold/Sell-Automatismen;
- Annahme, dass eine hohe Modell-Upside eine Order autorisiert;
- institutionelle Advisor-/Client-Reporting-, Pitchbook-, KYC-, Fund-Admin-, Month-End- oder Investment-Banking-Workflows als allgemeiner Finance-Core;
- Anthropic-spezifische Tool-, Connector-, MCP-, Subagent-, Excel-, Office-JS- oder Python-Struktur;
- fremde Skilltexte, Templates oder Formatvorgaben.

## Lokale Ableitung

Der vertiefte Audit führte zu:

- Härtung von `vermoegensprojektion`, `portfolioanalyse` und `anlagevergleich`;
- eigenständigem `portfolio-rebalancing`, weil Zielzustand, Inputs, Output und Failure Modes von reiner Portfolioanalyse abweichen;
- eigenständiger `unternehmensanalyse` für Geschäftsmodell, Economics, aktuelle Ergebnisse, Wettbewerb, Risiken und falsifizierbare These;
- eigenständiger `bewertungsanalyse` für DCF, Comparable Companies, Bewertungsannahmen und Sensitivität;
- keiner separaten `investmentthese`-Capability zum jetzigen Stand: These/Falsifikation bleibt zunächst Modus der Unternehmensanalyse, bis persistentes Thesis-Tracking als eigener wiederkehrender Job belegt ist.

## Grundregel

> Externe Finance-Methodik ist Review-Signal und Inspiration. Konkrete finanzielle Wahrheit bleibt daten-, zeit- und jurisdiktionsabhängig.