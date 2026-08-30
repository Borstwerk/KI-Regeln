---
name: portfolioanalyse
description: Prüft ein bestehendes Anlageportfolio read-only auf Allokation, Konzentration, Diversifikation, Overlap, Kosten, Liquidität und relevante Risikoexposures. Verwenden bei Depot-/Portfolio-Checks; nicht für automatische Rebalancing-Trades oder wenn aktuelle Holdings-/Produktdaten für exakte Aussagen fehlen.
---

# Portfolioanalyse

Dieser Skill nutzt `../../Finanzplanung-Grundsaetze.md` und `../../Portfolio-Risiko-Kosten-und-Diversifikation.md`.

## Workflow

1. Stichtag und verfügbare Portfolio-/Produktdaten bestimmen.
2. Anlageklassen und Positionen erfassen.
3. Konzentrationen und mögliche Overlaps prüfen.
4. Regionen, Branchen, Währungen und weitere relevante Exposures nur soweit belastbar analysieren.
5. Kosten und Liquidität separat bewerten.
6. Ziel, Zeithorizont und Risikotragfähigkeit nur aus bestätigten Angaben verwenden.
7. Findings von Tradevorschlägen trennen.
8. Fehlende aktuelle Daten als UNVERIFIED markieren.

## Abgrenzung

Nicht verwenden für:

- zukünftige Vermögensszenarien → `vermoegensprojektion`;
- Vergleich einzelner neuer Anlagen → `anlagevergleich`;
- Schulden-/Cashflowfragen → zuständige Finanzskills.

## Regeln

- Anzahl der Positionen ≠ Diversifikation.
- Diversifikation ≠ Verlustschutz.
- Vergangene Performance ≠ Qualitätsbeweis.
- Exakte aktuelle Gewichte/Fees/Holdings brauchen aktuelle Evidence.
- Analyse standardmäßig read-only; Review ≠ Trade-Autorisierung.

## Ausgabe

Stichtag, Struktur, Konzentrationen/Overlap, Kosten, Liquidität, Risiken, Zielabweichungen, Missing Evidence und mögliche nächste Analysefragen.

## Leitfrage

> Welche gemeinsamen Risiken verstecken sich hinter scheinbar unterschiedlichen Positionen?