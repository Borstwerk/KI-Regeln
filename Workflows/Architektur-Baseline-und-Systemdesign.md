# Workflow: Architektur-Baseline und Systemdesign

## Ziel

Ein bestehendes oder neues System aus belastbarer Evidence heraus entwerfen, ohne aktuelle Architektur, Requirements und Zielbild miteinander zu vermischen.

## Ablauf

```text
1. Scope / Requirements / Constraints
→ 2. Architecture Baseline, falls Bestand existiert
→ 3. Drivers / Invariants / Critical Flows
→ 4. Decision-Relevant Envelope
→ 5. Simplest Viable Candidate
→ 6. echte Alternativen, falls nötig
→ 7. Trade-off / Review
→ 8. Decision / ADR-Handoff
```

## Skills

1. `architecture-baseline` – Ist-Zustand, Ownership, Dependencies und Evidence erfassen.
2. `domain-modeling` – fachliche Begriffe/Invarianten vertiefen, wenn nötig.
3. `system-design` – Systementwurf aus Drivers und Evidence entwickeln.
4. `architecture-tradeoff-analysis` – nur bei mehreren ernsthaften Kandidaten.
5. `architecture-review` – vor bindender Entscheidung oder größerem Gate unabhängig prüfen.
6. `adr` – langfristige Entscheidung dauerhaft dokumentieren, wenn gerechtfertigt.

## Gates

- Fehlende Requirements oder Qualitätsziele werden nicht erfunden.
- Pattern oder Technologie ersetzen keinen Driver.
- `READY_FOR_LOCAL_GATE` autorisiert keine Implementierung.
- Code-, Daten-, Infrastruktur- oder Produktionsänderungen laufen über die jeweiligen Fachprozesse.

## Ergebnis

- nachvollziehbare Architecture 0 beziehungsweise Greenfield-Baseline;
- begründeter Zielentwurf;
- sichtbare Trade-offs und Missing Evidence;
- klare Handoffs für Detaildesign und Umsetzung.