---
name: slo-design
description: Entwirft oder prüft messbare Reliability Objectives mit SLI-Spezifikation, Messimplementierung, SLO, Messfenster und optionalem Error Budget. Verwenden bei SLI-/SLO-/Error-Budget-Fragen oder wenn "zuverlässig genug" operationalisiert werden soll. Nicht zur Erfindung geschäftlicher Zielwerte, SLAs oder RTO/RPO verwenden.
---

# SLO Design

## Ziel

Einen kritischen Nutzer-/Consumererfolg in eine messbare Reliability-Aussage übersetzen, ohne lokale Business- oder Vertragsanforderungen zu erfinden.

## Eingaben

- kritischer Flow / Consumererfolg;
- lokale Requirement, SLA, Produkt-/Risikokontext, falls vorhanden;
- vorhandene Baseline;
- mögliche Messquellen;
- Stakeholder / Owner;
- vorhandene Reliability-Policy.

## Arbeitsweise

1. Scope und kritischen Erfolg präzisieren.
2. Prüfen, welche lokale Anforderung oder Entscheidungsfrage das SLO begründen soll.
3. SLI-Spezifikation formulieren: Was zählt als gut, schlecht, gültig beziehungsweise nicht abgedeckt?
4. SLI-Spezifikation von der konkreten Messimplementierung trennen.
5. Coverage, Bias, Sampling, Messlücken und Datenqualität der Implementierung prüfen.
6. Ziel und Messfenster aus lokaler Anforderung übernehmen oder Kandidaten mit Trade-offs ausdrücklich als Vorschlag markieren.
7. Falls das SLO-Modell passt, Error Budget und Bedeutung berechnen/beschreiben.
8. Error-Budget-Policy nur als lokale Governance formulieren; keine automatische Betriebsaktion ableiten.
9. Exclusions, Ownership, Reviewtrigger und Missing Evidence dokumentieren.

## Keine Pflichtschablone

Je nach System können Availability, Latency, Freshness, Correctness, Durability, Coverage, Completion oder andere fachliche Ergebnisse relevant sein.

Nicht jedes SLI muss in dieselbe Request-Ratio-Schablone gepresst werden.

## Stop-/Übergaberegeln

- fehlt eine autorisierte Zielvorgabe, keinen erfundenen Wert als Requirement ausgeben;
- bei vertraglichen Zusagen zusätzlich lokale Contract-/Legal-Sources-of-Truth prüfen;
- bei RTO/RPO an Recovery-/Requirements-Kontext übergeben;
- bei fehlender Messbarkeit an `system-observability-design` übergeben;
- bei benötigten Alerts an `alert-design` übergeben.

## Nicht tun

- pauschal 99.9/99.95/99.99 % wählen;
- 100 % als allgemeines Qualitätsziel setzen;
- feste Anzahl SLOs erzwingen;
- Rolling Window universell erzwingen;
- SLO und SLA gleichsetzen;
- SLA müsse immer einen bestimmten Abstand zum SLO haben;
- Error Budget als automatische Deployfreigabe oder Freeze-Autorisierung behandeln;
- RTO/RPO in das SLO hineinrechnen.

## Ausgabe

```text
Scope / Critical Journey
Reliability Requirement / Decision Context
SLI Specification
Measurement Implementation
Coverage / Bias / Gaps
Target + Window [approved / candidate / unknown]
Error Budget, if applicable
Error-Budget Policy Status
Exclusions
Owner / Stakeholder
Review Trigger
Missing Evidence
```

## Related

- `system-observability-design`
- `alert-design`
- `reliability-review`
- `capacity-planning`
- `contract-change-review`

## Leitgedanke

> Erst definieren, welchen relevanten Erfolg wir messen wollen. Danach entscheiden, wie gut er sein muss und wie die Evidence entsteht.