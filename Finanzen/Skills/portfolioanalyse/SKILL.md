---
name: portfolioanalyse
description: Prüft ein bestehendes Anlageportfolio read-only auf Allokation, Konzentration, Diversifikation, Overlap, Kosten, Liquidität, Zielabweichungen und relevante Risikoexposures. Verwenden bei Depot-/Portfolio-Checks; nicht für Rebalancing-Pläne, automatische Trades oder exakte Aussagen aus veralteten Holdings-/Produktdaten.
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
7. Falls eine bestätigte Zielallokation vorliegt, Abweichungen read-only sichtbar machen.
8. Findings von Änderungs- oder Tradevorschlägen trennen.
9. Fehlende aktuelle Daten als `UNVERIFIED` markieren.

## Abgrenzung

Nicht verwenden für:

- konkrete Änderungen zurück zu einer bestätigten Zielallokation → `portfolio-rebalancing`;
- zukünftige Vermögensszenarien → `vermoegensprojektion`;
- Vergleich einzelner neuer Anlagen → `anlagevergleich`;
- Unternehmensfundamentaldaten → `unternehmensanalyse`;
- Unternehmensbewertung → `bewertungsanalyse`;
- Schulden-/Cashflowfragen → zuständige Finanzskills.

## Regeln

- Anzahl der Positionen ≠ Diversifikation.
- Diversifikation ≠ Verlustschutz.
- Vergangene Performance ≠ Qualitätsbeweis.
- Exakte aktuelle Gewichte/Fees/Holdings brauchen aktuelle Evidence.
- Zielabweichung sichtbar machen ≠ Rebalancing-Auftrag.
- Analyse standardmäßig read-only; Review ≠ Trade-Autorisierung.

## Ausgabe

Stichtag, Struktur, Konzentrationen/Overlap, Kosten, Liquidität, Risiken, gegebenenfalls Zielabweichungen, Missing Evidence und mögliche nächste Analysefragen.

## Leitfrage

> Welche gemeinsamen Risiken verstecken sich hinter scheinbar unterschiedlichen Positionen?