---
name: data-engineering-review
description: Auditiert Datenpipelines und analytische Datenprodukte unabhängig auf Source of Truth, Grain, Ingestion, Transformation, Quality, Contracts, Lineage, Orchestrierung, Replay, Publish, Lifecycle und Runtime-Evidence. Verwenden für größere Data-Engineering- oder Produktionsreife-Reviews. Nicht als Implementierungs-, DB-Tuning- oder produktiver Änderungsskill verwenden.
---

# Data Engineering Review

## Ziel

Systemische Lücken und fehlende Evidence eines Datenflusses sichtbar machen, ohne Findings ungefragt zu implementieren oder Toolpräferenzen als Architektururteil auszugeben.

## Eingaben

- Business-/Consumerziel;
- Sources of Truth und Ownership;
- Pipeline-/Job-/Transformationdefinitionen;
- Dataset-/Contract-/Schemaevidence;
- Quality-/Reconciliation-Ergebnisse;
- Lineage/Catalog;
- Runtime-/Freshness-/Backlog-Evidence;
- Backfill-/Recovery-/Incidenthistorie, falls relevant;
- Retention-/Security-/Privacy-Regeln.

## Prüfachsen

1. Intent, Consumer und Ownership;
2. Source of Truth / Source Limits;
3. Input-/Output-Grain und Schlüssel;
4. Ingestion / CDC / Delete / Replay;
5. Transformation / Incremental / History;
6. analytische Modellierung / Measures / Semantik;
7. Data Quality / Freshness / Reconciliation;
8. Data Contract / Evolution / Consumerimpact;
9. Lineage / Provenance / Impact Analysis;
10. Orchestrierung / Data Intervals / Retries / Backfills;
11. Batch-/Streaming-/Late-Data-Semantik;
12. Publish / Lifecycle / Retention;
13. Pipeline-Observability / Runtime Evidence;
14. Security-/Privacy-/Execution-Grenzen;
15. Missing, stale oder widersprüchliche Evidence.

## Arbeitsweise

- lokale Sources of Truth zuerst;
- Designabsicht, statische Config und Runtime-Evidence trennen;
- Findings mit Impact, Evidence-Status und passendem Fachhandoff formulieren;
- tiefe Themen an die spezialisierten Data-Engineering-Skills oder Nachbardomänen übergeben;
- keine Pipelineänderung, Backfill, Publish- oder Re-Architecture ungefragt ausführen.

## Evidence Status

- `CONFIRMED`
- `LIKELY`
- `UNVERIFIED`
- `CONFLICTING`

## Verdict

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_FINDINGS`
- `BLOCKED`
- `UNVERIFIED`

Das Verdict ist keine Produktions-, Publish- oder Backfill-Autorisierung.

## Stop-/Übergaberegeln

- einzelner Execution Plan/Index → Datenbanken;
- tiefe Softwareteststrategie → Testing und QA;
- systemweite SLO-/Incident-/Capacity-Frage → Reliability;
- Plattform-/Architekturentscheidung → Infra beziehungsweise spätere Software Architecture;
- produktive Datenänderung → lokales Gate.

## Nicht tun

- Repo-/DAG-/Contractdateien als Beweis für Live-Datenqualität behandeln;
- grünen Pipeline-Run als vollständiges Review-PASS verwenden;
- unbekannte Consumer/Lineage-Lücken als risikofrei behandeln;
- Star Schema, Airflow, dbt oder Kafka als vorgeschriebene Reparatur einsetzen;
- Reviewfinding ungefragt implementieren;
- Toolzugriff als Autorisierung für Publish/Backfill interpretieren.

## Ausgabe

```text
Scope / Consumers / Sources of Truth
Findings [priority, evidence status, impact]
Grain / Semantics Risks
Ingestion / Transformation Risks
Quality / Freshness / Reconciliation
Contract / Consumer Impact
Lineage / Provenance Gaps
Orchestration / Replay / Backfill Risks
Publish / Lifecycle Risks
Runtime Evidence / Operability
Missing / Conflicting Evidence
Required Handoffs
Verdict
```

## Related

- `data-pipeline-design`
- `data-ingestion-design`
- `data-transformation-design`
- `analytical-data-modeling`
- `data-quality-design`
- `data-contract-design`
- `data-lineage-analysis`
- `data-orchestration-design`
- `reliability-review`
- `database-review`
- `test-suite-review`

## Leitgedanke

> Ein gutes Data-Engineering-Review prüft, ob richtige Daten nachvollziehbar und wiederholbar beim richtigen Consumer ankommen – nicht nur, ob Jobs existieren.