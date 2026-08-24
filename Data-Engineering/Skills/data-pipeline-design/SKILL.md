---
name: data-pipeline-design
description: Entwirft oder prüft einen systemübergreifenden Datenfluss von autoritativer Quelle bis Consumer mit Grain, Capture, Transformation, Quality, Publish, Replay, Ownership und Evidence. Verwenden bei neuen ETL-/ELT-/Batch-/Streaming-Pipelines oder größeren Pipelineänderungen. Nicht als Toolauswahl-, DB-Schema- oder ungefragter Ausführungsskill verwenden.
---

# Data Pipeline Design

## Ziel

Einen nachvollziehbaren Datenfluss entwerfen, dessen fachliche Semantik, Betriebsverhalten und Wiederholbarkeit vor Toolsyntax geklärt sind.

## Eingaben

- Business-/Consumerziel;
- autoritative Source(s);
- Ziel/Consumer;
- erwarteter Grain und Semantik;
- Freshness-/Qualitätsanforderungen;
- Volumen und Änderungsmuster;
- Security-/Privacy-/Retention-Kontext;
- lokale Plattform-/Kosten-/Betriebsgrenzen.

## Arbeitsweise

1. Business Intent, Consumer und erwarteten Output präzisieren.
2. Source of Truth und Ownership je Datenbereich bestimmen.
3. Input-/Output-Grain, Schlüssel, Zeitsemantik und Änderungsverhalten festhalten.
4. Capture-/Ingestion-Modell wählen und Replayfähigkeit prüfen.
5. Transformationsstufen und semantische Änderungen explizit machen.
6. Quality-/Reconciliation-Evidence vor Publish definieren.
7. Contract, Lineage und Consumerwirkung planen.
8. Orchestrierung, Zeit-/Abhängigkeitsmodell und Reprocessingbedarf definieren.
9. Betriebs-/Freshness-/Lag-/Backlog-Evidence mit Reliability-Grenze beschreiben.
10. Tool-/Plattformimplementierung erst aus lokalem Stack ableiten.

## Kernfragen

```text
Warum existiert der Datenfluss?
Welche Quelle ist autoritativ?
Was bedeutet genau ein Output-Datenelement?
Wie werden Änderungen, Deletes und Late Data behandelt?
Wie beweisen wir Vollständigkeit und Korrektheit?
Wie kann ein Zeitraum reproduzierbar neu erzeugt werden?
Wann darf veröffentlicht werden?
Wer besitzt Source, Pipeline, Dataset und Consumerbeziehung?
```

## Stop-/Übergaberegeln

- operatives DB-Schema/Querydesign → `database-design` / Datenbanken;
- API-/Message-Vertrag → `interface-design` / `event-contract-design`;
- tiefe Testmethodik → Testing und QA;
- Plattform-/Scheduler-/Storage-Auswahl als Architekturentscheidung → lokale Architektur/Infra;
- produktive Ausführung/Backfill → lokales Execution Gate.

## Nicht tun

- Airflow/dbt/Kafka/Spark als Defaultstack einsetzen;
- ELT vor ETL oder Streaming vor Batch pauschal bevorzugen;
- Source of Truth aus technischer Erreichbarkeit ableiten;
- erfolgreichen Jobstatus als Data Quality behandeln;
- Replay/Backfill erst nach einem Incident bedenken;
- fehlende Business-/Consumeranforderungen durch Best Practices ersetzen.

## Ausgabe

```text
Intent / Consumers
Sources of Truth / Ownership
Input + Output Grain
Capture / Ingestion
Transformations
Time / Change Semantics
Quality / Reconciliation
Contract / Lineage
Orchestration / Replay
Publish Model
Runtime Evidence
Open Decisions / Handoffs / Gates
```

## Related

- `data-ingestion-design`
- `data-transformation-design`
- `analytical-data-modeling`
- `data-quality-design`
- `data-contract-design`
- `data-lineage-analysis`
- `data-orchestration-design`
- `data-engineering-review`

## Leitgedanke

> Erst Datenbedeutung und Wiederholbarkeit, dann Pipelinecode und Tooling.