# Portfolio-Rebalancing – Zielabweichungen kontrolliert korrigieren

## Ziel

Ein bestehendes Portfolio gegen eine **bestätigte Zielallokation** prüfen und daraus einen nachvollziehbaren Änderungsplan ableiten, ohne reale Trades automatisch auszuführen.

Portfolio-Rebalancing ist nicht dasselbe wie Portfolioanalyse:

```text
Portfolioanalyse
→ Was ist im Portfolio und welche Risiken/Abweichungen bestehen?

Portfolio-Rebalancing
→ Welche kontrollierten Änderungen könnten eine bestätigte Zielallokation wieder annähern?
```

## Erforderliche Inputs

Soweit für den Auftrag materiell:

- aktueller Portfoliozustand mit Stichtag;
- bestätigte Zielallokation oder Zielbandbreiten;
- geplante Ein-/Auszahlungen;
- relevante Kosten und Mindestgrößen;
- Liquiditätsbedarf;
- steuerliche oder kontospezifische Folgen nur mit aktueller lokaler Evidence;
- bekannte Restriktionen, Sperrfristen oder Nutzerpräferenzen.

Eine Zielallokation oder Rebalancing-Bandbreite nicht aus einem externen Default erfinden.

## Workflow

1. Aktuellen Zustand und Datenstand bestätigen.
2. Zielallokation und gegebenenfalls autorisierte Toleranzbänder bestätigen.
3. Abweichungen je relevanter Anlageklasse beziehungsweise Exposure berechnen.
4. Zuerst prüfen, ob neue Beiträge, Ausschüttungen oder geplante Entnahmen Abweichungen ohne zusätzliche Verkäufe reduzieren können.
5. Falls Änderungen nötig sind, mehrere Umsetzungsvarianten nach Zielnähe, Kosten, Liquidität, Steuerwirkung und Komplexität vergleichen.
6. Turnover und unnötige Mikrokorrekturen sichtbar machen.
7. Vorher-/Nachher-Allokation und verbleibende Abweichungen zeigen.
8. Reale Kauf-/Verkaufsorders separat human-gaten.

## Grundregeln

- Rebalancing braucht ein bestätigtes Ziel; ohne Ziel keine scheinpräzise Optimierung.
- Kleine Abweichung ≠ automatisch Handlungsbedarf.
- Cashflow-first kann sinnvoll sein, ist aber kein universelles Muss.
- Steuer- oder Kontoregeln sind jurisdictions- und zeitabhängig.
- Eine mathematisch nähere Zielallokation kann durch Kosten, Steuern oder Liquiditätsfolgen praktisch schlechter sein.
- Trade-Plan ≠ Trade-Autorisierung.
- Keine feste `±3 %`, `±5 %` oder andere Bandbreite als allgemeine Wahrheit verwenden.

## Ausgabe

- Stichtag und Datenqualität;
- bestätigte Zielallokation;
- Drift-/Abweichungstabelle;
- mögliche Änderungsvarianten;
- Kosten-/Steuer-/Liquiditäts-Trade-offs soweit belegt;
- Vorher-/Nachher-Sicht;
- Missing Evidence;
- klarer Human Gate vor realer Ausführung.

## Leitfrage

> Welche kleinste belastbare Änderung bringt das Portfolio näher an das bestätigte Ziel, ohne Kosten und Nebenwirkungen zu verstecken?