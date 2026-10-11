# Delivery- und Review-Metriken für Coding-Agenten

## Fragestellung

> Was wurde **funktionierend und akzeptiert** geliefert, mit welchem Aufwand, in welcher Zeit und mit welchen späteren Korrekturen?

Mehr Code, mehr Commits oder mehr Pull Requests sind **Aktivitätssignale**, keine ausreichenden Outcome-Kennzahlen.

## Minimalmodell

Ein Claim benötigt klaren Scope, Messzeitraum, Basislinie und Denominator. Optional nach Risiko- oder Aufgabenklasse segmentieren.

| Metrik | Operationalisierung | Nicht daraus ableiten |
|---|---|---|
| **akzeptierte Aufgaben** | fachlich abgenommene Issues/Anforderungen im betrachteten Zeitraum | PR-Zahl = gelieferter Wert |
| **End-to-End-Durchlaufzeit** | von angenommenem Auftrag bis freigegebener, nachweisbarer Lieferung; Wartezeit separat | reine Modell-Laufzeit = Lead Time |
| **Reviewrunden** | Rückgaben mit substantieller Änderung / abgeschlossene Aufgabe | viele Runden sind per se schlechte Qualität |
| **Rework / Reverts** | erneut geöffnet, zurückgerollt oder nach Auslieferung korrigiert | niedrige Zahl ohne Betrachtung der Nachbeobachtungszeit = fehlerfrei |
| **Verification / Akzeptanz** | gültige Gates, echte unabhängige Tests und nachweisbarer Outcome | CI grün = Nutzerproblem gelöst |
| **Kosten** | Modell-/Toolkosten, menschliche Reviewzeit, Runtime, wiederholte Runs; unbekannte Kosten explizit | Tokenkosten allein = Gesamtkosten |
| **Review-Wartezeit** | Warten auf menschliche/maschinelle Freigaben getrennt von aktiver Arbeit | hohe Latenz = langsame Implementierung |

## Vergleichsregeln

- Gleichartige Aufgaben und gleiche Risiko-/Reviewkategorie vergleichen.
- Ein baselinefreier Vorher/Nachher-Vergleich ist nur explorativ.
- Nicht nur erfolgreiche Fälle zählen: abgebrochene, blockierte und verworfene Aufgaben im Denominator sichtbar halten.
- Ein späterer Revert ist retrospektives Signal, nicht automatisch Beweis einer bestimmten Ursache.
- Metrikdefinitionen **vor** der Ergebnisprüfung festlegen; nicht nachträglich dem gewünschten Ergebnis anpassen.
- Review-Qualität und Reviewer-Unabhängigkeit getrennt messen. Same-Model-Review nicht als unabhängig ausgeben.
- Outcome-Metriken nicht durch mehr selbstgenerierte Subissues/PRs künstlich erhöhen.

## Kompakte Delivery-Evidence

```yaml
measurement_window: "2026-W41"
scope: "eine repräsentative Klasse von Bugfixes"
admitted_tasks: 12
accepted_tasks: 8
blocked_tasks: 2
abandoned_tasks: 2
review_rounds_total: 15
reverts_in_followup_window: 1
lead_time: "gemessen mit definiertem Start-/Endereignis"
costs:
  model: "erfasst oder unknown"
  human_review: "erfasst oder unknown"
claim_limit: "Beobachtungsdaten, kein randomisierter Produktivitätseffekt"
```

Das ist ein **Beispielformat**, keine Beobachtung zu KI-Regeln.

## Evals und Release

Für Agentenänderungen Outcome- und Prozesssignale getrennt halten:

1. **Struktur**: Validator/Schema/Packaging PASS?
2. **Verhalten**: Fresh-Agent-Task bestanden? Bei n=1 nur begrenzte Evidenz.
3. **Lieferung**: fachlich akzeptiert, nicht nur Code geschrieben?
4. **Wirkung**: Defekt weg, Qualität stabil, geringe Nacharbeit?
5. **Kosten**: Gesamtaufwand und Review-Engpass transparent?

Keine synthetische Metrik als reale Produktivität ausgeben.

## Quellen- und Evidenzgrenze

Das [Cockroach-Labs-Experiment vom 09.10.2026](https://www.cockroachlabs.com/blog/experiment-running-hospital-code/) zeigt hohen Output **und** hohen Review-/Tokenaufwand. Einzelfallberichte belegen keine universelle Überlegenheit von Multi-Agent-Orchestrierung.

Untersuchungen zu KI-Coding-Einsatz weisen ebenfalls auf eine mögliche Entkopplung von Code-/PR-Volumen und tatsächlicher Lieferung hin; Effektgrößen nicht ohne geprüfte Studienpopulation und Methodik generalisieren.

## Leitgedanke

> Wir optimieren ausgelieferte, geprüfte Wirkung pro Aufwand – nicht sichtbare Agentenbeschäftigung.
