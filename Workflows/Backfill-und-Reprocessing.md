# Workflow – Backfill und Reprocessing

## Ziel

Historische Daten kontrolliert neu verarbeiten, ohne Duplikate, unbemerkte Semantikänderungen oder Downstreamkorruption zu erzeugen.

## Ablauf

```text
Korrektur-/Reprocessingbedarf
→ data-transformation-design / data-ingestion-design
→ data-lineage-analysis
→ data-quality-design
→ data-orchestration-design
→ bounded Plan
→ lokales Execution Gate
→ Slice / Dry Run, wenn sinnvoll
→ Reprocessing
→ Reconciliation
→ Publish / Fresh Verification
```

## Pflichtfragen vor Ausführung

```text
Warum wird neu verarbeitet?
Welcher Zielzustand soll entstehen?
Welcher Zeitraum / welche Partitionen?
Welche Source of Truth?
Welche Code-/Contract-Version und historische Semantik?
Append / Merge / Replace?
Wie werden Duplikate verhindert?
Welche Consumer sind betroffen?
Welche Parallelität / Source-/Target-Last ist vertretbar?
Welche Reconciliation beweist den Zielzustand?
Wie wird abgebrochen oder recovered?
Wer autorisiert die reale Datenänderung?
```

## 1. Semantik

`data-transformation-design` beziehungsweise `data-ingestion-design` klärt, wie der Replaypfad fachlich funktioniert.

## 2. Impact

`data-lineage-analysis` identifiziert bekannte Downstreams und Lineage-Gaps.

## 3. Evidence

`data-quality-design` definiert Reconciliation vor Publish beziehungsweise Consumerfreigabe.

## 4. Orchestrierung

`data-orchestration-design` plant bounded intervals, Reihenfolge, Parallelität, Retries und Interaktion mit normalen Läufen.

## Gate

Planung oder Toolzugriff autorisieren keinen produktiven Backfill.

## Nachweis

Job-Erfolg genügt nicht. Fresh Data-/Reconciliation-Evidence muss den erwarteten Zielzustand bestätigen.

## Ergebnis

```text
Backfill Objective
Bounded Scope
Source / Version / Semantics
Write / Idempotency Strategy
Consumer / Lineage Impact
Execution / Parallelism Plan
Abort / Recovery
Reconciliation
Authorization Status
Fresh Result Evidence
```