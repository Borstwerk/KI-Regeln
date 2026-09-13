---
name: portfolio-rebalancing
description: Leitet aus einem bestehenden Portfolio und einer bestätigten Zielallokation einen read-only Rebalancing-Plan mit Drift, Cashflow-, Kosten-, Liquiditäts- und belegten Steuerfolgen ab. Verwenden bei "Portfolio neu gewichten", "Rebalancing" oder "wie komme ich zurück zu meiner Zielallokation"; nicht für reine Portfolioanalyse, erfundene Zielbänder oder automatische Kauf-/Verkaufsorders.
---

# Portfolio-Rebalancing

Dieser Skill nutzt `../../Finanzplanung-Grundsaetze.md`, `../../Portfolio-Risiko-Kosten-und-Diversifikation.md` und `../../Portfolio-Rebalancing.md`.

## Workflow

1. Aktuellen Portfoliozustand und Stichtag bestätigen.
2. Zielallokation und gegebenenfalls autorisierte Toleranzbänder bestätigen.
3. Drift je relevanter Anlageklasse beziehungsweise Exposure bestimmen.
4. Geplante Ein-/Auszahlungen und vorhandenes Cash als mögliche Anpassungshebel prüfen.
5. Nur bei Bedarf Änderungsvarianten berechnen und Kosten, Liquidität, Steuern und Turnover sichtbar machen.
6. Vorher-/Nachher-Allokation sowie verbleibende Abweichungen darstellen.
7. Unbekannte aktuelle Produkt-/Steuerdaten als `UNVERIFIED` markieren.
8. Reale Trades separat human-gaten.

## Abgrenzung

Nicht verwenden für:

- reine Struktur-/Risikoanalyse ohne Änderungsauftrag → `portfolioanalyse`;
- Vergleich einzelner neuer Anlageprodukte → `anlagevergleich`;
- Unternehmensfundamentaldaten → `unternehmensanalyse`;
- Bewertung eines Unternehmens → `bewertungsanalyse`.

## Regeln

- Rebalancing ohne bestätigtes Ziel ist keine belastbare Optimierung.
- Keine universelle `±3 %`, `±5 %` oder andere Rebalancing-Bandbreite erfinden.
- Neue Cashflows können Verkäufe vermeiden, sind aber kein automatischer Vorrang in jeder Situation.
- Steuer-/Kontoregeln nur mit aktueller jurisdiktionsspezifischer Evidence verwenden.
- Kleinere Drift bedeutet nicht automatisch Handlungsbedarf.
- Rebalancing-Plan ≠ Trade-Autorisierung.

## Ausgabe

Stichtag, Ziel, Drift, mögliche Änderungsvarianten, Kosten-/Liquiditäts-/Steuerfolgen soweit belegt, Vorher/Nachher, Missing Evidence und Human Gate.

## Leitfrage

> Welche kleinste belastbare Änderung reduziert die relevante Zielabweichung, ohne neue Nebenwirkungen zu verstecken?