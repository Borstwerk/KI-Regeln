# Workflow – Data Pipeline Baseline und Design

## Ziel

Einen neuen oder wesentlich geänderten Datenfluss von Source of Truth bis Consumer fachlich und betrieblich spezifizieren, bevor Tooling oder Pipelinecode die Entscheidungen verdecken.

## Ablauf

```text
lokaler Business-/Consumerkontext
→ data-pipeline-design
→ data-ingestion-design
→ data-transformation-design
→ optional analytical-data-modeling
→ data-quality-design
→ data-contract-design
→ data-lineage-analysis
→ data-orchestration-design
→ data-engineering-review
→ lokales Implementierungs-/Publish-Gate
```

## 1. Lokale Wahrheit

Klare Inputs:

- Business Intent und Consumer;
- Sources of Truth und Owner;
- gewünschter Output/Grain;
- Freshness-/Quality-Anforderungen;
- Volumen und Änderungsmuster;
- lokale Plattform, Security, Retention und Kosten.

Fehlende fachliche Anforderungen nicht aus Best Practices erfinden.

## 2. End-to-End-Design

`data-pipeline-design` strukturiert Source, Capture, Transformation, Quality, Contract, Lineage, Replay und Publish.

## 3. Fachliche Vertiefung

- `data-ingestion-design` für Capture/CDC/Offsets/Replay;
- `data-transformation-design` für fachliche Ableitungen und Incrementalität;
- `analytical-data-modeling` wenn ein analytisches Consumer-Modell entworfen wird;
- `data-quality-design` für Quality-/Reconciliation-Evidence;
- `data-contract-design` für veröffentlichte Consumerzusagen;
- `data-lineage-analysis` für Herkunft und Impact;
- `data-orchestration-design` für Abhängigkeiten, Data Intervals und Reprocessing.

## 4. Review

`data-engineering-review` prüft den Gesamtentwurf unabhängig und markiert Missing Evidence.

## Gate

Ein gutes Design ist keine Freigabe für reale Pipeline-, Publish- oder Backfill-Aktionen.

## Ergebnis

```text
Intent / Consumer
Sources of Truth / Ownership
Grain / Semantics
Ingestion / Transformation
Quality / Reconciliation
Contract / Lineage
Orchestration / Replay
Publish / Lifecycle
Review Verdict
Local Decision Status
```

## Leitgedanke

> Erst definieren, welche Datenwahrheit beim Consumer ankommen soll; danach automatisieren.