# Skill-Handbuch – Data Engineering

Dieses Handbuch hilft bei der Auswahl der neun Skills aus `Data-Engineering/`.

## Schnellauswahl

| Wenn die Aufgabe lautet … | Primärer Skill |
|---|---|
| einen kompletten Datenfluss von Quelle bis Consumer entwerfen | `data-pipeline-design` |
| eine Quelle per Snapshot, API, CDC oder Stream anbinden | `data-ingestion-design` |
| Join-/Filter-/Aggregations-/Incrementallogik entwerfen | `data-transformation-design` |
| Grain, Measures, Dimensionen und Historie eines Analyticsmodells entwerfen | `analytical-data-modeling` |
| Quality-, Freshness- oder Reconciliation-Nachweise definieren | `data-quality-design` |
| Consumerzusagen für ein veröffentlichtes Dataset definieren/evolvieren | `data-contract-design` |
| Herkunft, Downstreams oder Change Impact analysieren | `data-lineage-analysis` |
| Scheduling, Data Intervals, Retries, Catchup oder Backfills planen | `data-orchestration-design` |
| einen Datenfluss breit und unabhängig auditieren | `data-engineering-review` |

## 1. `data-pipeline-design`

**Nutzen:** End-to-End-Design eines systemübergreifenden Datenflusses.

**Typische Trigger:** ETL/ELT, neue Pipeline, Source-to-Consumer, größere Pipelineänderung, Batch-vs.-Streaming-Frage im Gesamtkontext.

**Nicht dafür:** operatives DB-Schema, einzelne API-/Message-Contracts, reine Toolinstallation.

**Wichtige Evidence:** Source of Truth, Consumer, Grain, Freshness/Quality, Änderungsmuster, Ownership.

## 2. `data-ingestion-design`

**Nutzen:** sichere Erfassung von Source-Daten mit Updates, Deletes, Cursor/Offsets und Replay.

**Typische Trigger:** CDC, Incremental Pull, Snapshot, File Arrival, Stream Consumption, Offset/Checkpoint.

**Nicht dafür:** Event-Payload-Vertrag oder produktiver Offsetreset.

**Warnsignal:** „Kafka = exactly once“ oder „updated_at ist immer sicher“.

## 3. `data-transformation-design`

**Nutzen:** fachliche Transformations- und Incrementallogik.

**Typische Trigger:** Joins, Filter, Aggregationen, Materialisierung, Incremental Models, historische Neuberechnung.

**Nicht dafür:** Grain-/Measure-Design eines Analyticsmodells oder Query-Tuning.

**Warnsignal:** SQL kompiliert oder Job grün als Korrektheitsbeweis.

## 4. `analytical-data-modeling`

**Nutzen:** analytische Datasets mit eindeutigem Grain, Measures, Dimensionen und History.

**Typische Trigger:** Warehouse, Mart, Semantic Model, Facts/Dimensions, Kennzahlmodell.

**Nicht dafür:** operative DB-Normalisierung.

**Warnsignal:** Patternwahl vor Grain, etwa „immer Star Schema“.

## 5. `data-quality-design`

**Nutzen:** fachlich begründete Quality-/Freshness-/Reconciliation-Evidence.

**Typische Trigger:** Completeness, Uniqueness, Freshness, Source-vs.-Target, Kontrollsummen, Datenanomalien.

**Nicht dafür:** allgemeine Softwareteststrategie.

**Warnsignal:** universelle Schwellen ohne Requirement oder Baseline.

## 6. `data-contract-design`

**Nutzen:** explizite Consumerzusagen für Datasets.

**Typische Trigger:** Tabellenschema plus Semantik, Quality, Freshness, Ownership, Evolution.

**Nicht dafür:** API-, Request-/Response- oder operativer Eventvertrag.

**Warnsignal:** gleiche Datentypen mit semantischer Compatibility verwechseln.

## 7. `data-lineage-analysis`

**Nutzen:** Herkunft, Provenance und Change Impact.

**Typische Trigger:** „Woher kommt das?“, „Was hängt davon ab?“, „Welche Runs/Versionen erzeugten das?“

**Nicht dafür:** generische Runtime-Observability.

**Warnsignal:** statischer DAG als vollständige Runtime-Lineage.

## 8. `data-orchestration-design`

**Nutzen:** Datenabhängigkeiten, Data Intervals, Retry, Catchup und Reprocessing koordinieren.

**Typische Trigger:** Scheduler, DAG, Abhängigkeiten, Backfillplanung, verpasste Intervalle.

**Nicht dafür:** fachliche Transformationslogik oder Scheduler-Infrastruktur selbst.

**Warnsignal:** Uhrzeit = Input vollständig oder feste Retrywerte als Universalregel.

## 9. `data-engineering-review`

**Nutzen:** unabhängiger Gesamtcheck vor Go-Live/Cutover oder bei größeren Risiken.

**Prüft:** Source, Grain, Ingestion, Transformation, Modeling, Quality, Contracts, Lineage, Orchestration, Replay, Publish, Lifecycle und Runtime-Evidence.

**Verdicts:** `READY_FOR_LOCAL_GATE`, `READY_WITH_FINDINGS`, `BLOCKED`, `UNVERIFIED`.

**Wichtig:** Das Verdict ist keine Ausführungsfreigabe.

## Häufige Grenzen

```text
operativer Datenspeicher / Query / Index
→ Datenbanken

API / Message / Event Contract
→ Schnittstellen und Verträge

Softwareteststrategie
→ Testing und QA

systemweite SLOs / Incidents / Capacity
→ Reliability und System-Observability

Runtime / Scheduler / Storage / Deploy
→ Infrastruktur und DevOps

System-/Plattformstruktur
→ spätere Software Architecture
```

## Leitgedanke

> Data Engineering beginnt bei fachlicher Datenbedeutung und endet bei nachvollziehbarer Consumer-Evidence – nicht beim grünen DAG.