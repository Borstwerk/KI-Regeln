---
name: vermoegensprojektion
description: Modelliert mögliche Vermögensentwicklung über Zeit anhand expliziter Spar-/Entnahmeraten, Rendite-, Kosten- und Inflationsannahmen in mehreren Szenarien. Verwenden bei Fragen wie "Wie könnte sich mein Vermögen entwickeln?"; nicht als Renditeprognose, Garantie oder Ersatz aktueller Steuer-/Produktdaten.
---

# Vermögensprojektion

Dieser Skill nutzt `../../Finanzplanung-Grundsaetze.md` und `../../Vermoegensprojektion-und-Szenarien.md`.

## Workflow

1. Ziel, Zeitraum und Startzustand klären.
2. Spar-/Entnahmeraten und große geplante Cashflows erfassen.
3. Rendite, Inflation, Kosten und gegebenenfalls Steuern als getrennte Inputs behandeln.
4. Quelle beziehungsweise Annahmestatus jedes materiellen Inputs markieren.
5. Mehrere Szenarien modellieren statt einen sicheren Endwert zu behaupten.
6. Nominale und reale Ergebnisse unterscheiden.
7. Sensitivität gegenüber wichtigen Annahmen zeigen.
8. Nicht modellierte Risiken nennen.

## Abgrenzung

Nicht verwenden für:

- aktuelle Budgetbaseline → `finanzstatus-und-cashflow`;
- konkrete Produktwahl → `anlagevergleich`;
- vorhandene Portfolioexposures → `portfolioanalyse`.

## Regeln

- Projektion ≠ Prognose ≠ Garantie.
- Historische Rendite nicht als Zukunftswert ausgeben.
- Fehlende Kosten oder Steuern nicht automatisch mit Null modellieren.
- Keine erfundene Monte-Carlo-Erfolgswahrscheinlichkeit.
- Aktuelle Markt-/Steuerannahmen bei Materialität recherchieren.

## Ausgabe

Inputs, Quellen-/Annahmestatus, Szenarien, nominal/real, Sensitivitäten und Restunsicherheit.

## Leitfrage

> Was passiert mit dem Ergebnis, wenn sich die wichtigste Annahme als falsch erweist?