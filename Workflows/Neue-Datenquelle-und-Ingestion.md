# Workflow – Neue Datenquelle und Ingestion

## Ziel

Eine neue Quelle kontrolliert anbinden, ohne Source-Autorität, Änderungssemantik, Deletes, Replay und Consumerwirkung zu erraten.

## Ablauf

```text
Source-/Consumerkontext
→ data-ingestion-design
→ data-contract-design
→ data-quality-design
→ data-lineage-analysis
→ data-orchestration-design
→ optional data-pipeline-design
→ lokales Implementierungs-/Publish-Gate
```

## 1. Source verstehen

Klare Evidence zu:

- Source of Truth und Owner;
- Schema/Contract;
- Identität und Änderungsmodell;
- Inserts, Updates, Deletes;
- Timestamp-/Sequence-/Offset-Semantik;
- Rate Limits, Retention und Replay;
- Security/Privacy.

## 2. Capture entwerfen

`data-ingestion-design` legt Capture-Modus, Cursor/Offset, Ordering, Deduplizierung und Recovery fest.

Exactly-once niemals nur aus Toolnamen ableiten.

## 3. Zielvertrag und Quality

`data-contract-design` beschreibt den konsumierbaren Output. `data-quality-design` legt passende Ingest-/Pre-Publish-Evidence fest.

## 4. Lineage und Orchestrierung

`data-lineage-analysis` erfasst Source → Job → Output. `data-orchestration-design` definiert Data Intervals, Input Readiness, Retry und Catchup.

## Gate

Offsetreset, Source-Belastung, produktiver Start oder Publish bleiben reale Aktionen mit lokalen Gates.

## Ergebnis

```text
Source Authority
Capture / Change Semantics
Cursor / Offset / Replay
Target Contract
Quality Evidence
Lineage
Orchestration
Security / Source Impact
Execution Gate
```