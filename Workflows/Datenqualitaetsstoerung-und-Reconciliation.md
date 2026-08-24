# Workflow – Datenqualitätsstörung und Reconciliation

## Ziel

Einen verdächtigen oder bestätigten falschen Datenzustand strukturiert eingrenzen, Consumerwirkung begrenzen und belastbare Korrektheits-Evidence herstellen.

## Ablauf

```text
Daten-/Consumerproblem
→ data-quality-design
→ data-lineage-analysis
→ data-transformation-design oder data-ingestion-design
→ incident-response, wenn aktive relevante Betriebswirkung
→ Reconciliation
→ optional kontrolliertes Reprocessing
→ Fresh Verification
```

## 1. Wirkung und Scope

Klären:

- betroffene Datasets, Zeiträume und Consumer;
- Freshness vs. Completeness vs. semantische Falschheit;
- ob Publish gestoppt/quarantänisiert werden muss;
- welche Evidence bestätigt und welche nur Hypothese ist.

Bei aktivem produktivem Incident `incident-response` für Koordination nutzen.

## 2. Quality und Lineage

`data-quality-design` formuliert passende Nachweise. `data-lineage-analysis` verfolgt Source, Transformationen und Downstreams.

## 3. Ursache fachlich eingrenzen

Je nach Befund:

- Capture/CDC/Offset → `data-ingestion-design`;
- Join/Aggregation/Incrementalität → `data-transformation-design`;
- Contract-/Semantikdrift → `data-contract-design`;
- technische Root Cause → `diagnose` / Fachdomäne.

## 4. Reconciliation vor Freigabe

Korrektur nicht nur über Jobstatus bestätigen. Je nach Risiko Counts, Keys, Salden, fachliche Aggregate oder andere geeignete Vergleichsevidence verwenden.

## 5. Reprocessing nur kontrolliert

Backfill/Replay benötigt bounded scope, Write-Semantik, Consumerimpact, Reconciliation und lokales Gate.

## Ergebnis

```text
Impact / Consumer Scope
Confirmed Data State
Lineage / Source Scope
Working Hypotheses
Quality / Reconciliation Evidence
Mitigation / Publish Status
Reprocessing Proposal / Gate
Fresh Verification
Open Risks
```