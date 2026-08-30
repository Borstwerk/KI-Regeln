# Quellen und Inspirationen – Finanzen

## Zweck

Diese Datei dokumentiert methodische Referenzen. Sie macht externe Quellen nicht zu automatisch gültiger Projektwahrheit und ersetzt keine aktuelle Prüfung konkreter Produkte, Märkte, Steuern oder Regulierung.

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
- Lizenz: Apache-2.0 zum geprüften Stand 2026-08-30.

Selektiv betrachtet wurden insbesondere `financial-plan` und `portfolio-rebalance` im Wealth-Management-Bereich.

Nützlich als Inspiration:

- vollständige Baseline vor Szenariomodellierung;
- Stress-/What-if-Szenarien statt nur Base Case;
- Kosten und Steuerwirkung als separate Analyseachsen;
- aktuelle Portfolioallokation vor Rebalancing-/Trade-Fragen erfassen.

Nicht übernommen:

- 401(k), IRA, Roth, 529, Social Security, RMD und andere US-spezifische Regeln als Default;
- feste Inflations-, Rebalancing-Band- oder Erfolgswahrscheinlichkeitswerte;
- automatische Trade-Listen als Folge einer Portfolioanalyse;
- Tool-/Plugin-Struktur oder Skilltexte.

## Grundregel

> Externe Finance-Methodik ist Review-Signal und Inspiration. Konkrete finanzielle Wahrheit bleibt daten-, zeit- und jurisdiktionsabhängig.