# Data Engineering

Dieser Bereich beschreibt allgemeine, tool- und plattformneutrale Arbeitsweisen für systemübergreifende Datenflüsse, analytische Datenprodukte und deren sichere Veränderung.

## Grundprinzip

> Eine Pipeline ist nicht korrekt, nur weil sie erfolgreich gelaufen ist. Entscheidend ist, ob die richtigen Daten mit der richtigen Semantik, Vollständigkeit, Aktualität und nachvollziehbarer Herkunft beim vorgesehenen Consumer ankommen.

## Scope

`Data-Engineering/` behandelt insbesondere:

- Quellen, Ziele und Verantwortung eines Datenflusses;
- Batch-, Micro-Batch- und Streaming-Verarbeitung;
- Ingestion, CDC, Cursor, Checkpoints und Replay;
- Transformationen, inkrementelle Verarbeitung und Backfills;
- analytische Datenmodellierung, Grain und Historisierung;
- Datenqualität, Freshness, Vollständigkeit und Reconciliation;
- Data Contracts für veröffentlichte Datasets;
- Schema- und Semantikevolution von Datenprodukten;
- Lineage, Provenance und Impact Analysis;
- Orchestrierung, Abhängigkeiten, Retries und Reprocessing;
- Zeitsemantik, Event Time, Processing Time und Late Data;
- Publish-, Retention- und Lifecycle-Regeln;
- Pipeline-spezifische Betriebs- und Observability-Anforderungen.

## Abgrenzung

- **Datenbanken:** Zustand und Verhalten innerhalb eines operativen Datenspeichers, Query-Performance, Constraints, DB-Migrationen und DB-Betrieb.
- **Schnittstellen und Verträge:** operative APIs, Messages, Webhooks und Event-Contracts zwischen Systemen. Data Engineering behandelt dagegen veröffentlichte Datasets und ihre Nutzung in Datenflüssen.
- **Testing und QA:** allgemeine Teststrategie und Testmethodik. Data Engineering definiert datenfachliche Invarianten, Reconciliation und Publish-Evidence.
- **Reliability und System-Observability:** systemweite SLOs, Incidents, Capacity und Resilience. Data Engineering definiert pipeline-spezifische Freshness-, Completeness-, Lag- und Replay-Evidence.
- **Infrastruktur und DevOps:** stellt Runtime, Scheduler, Storage, Compute und Deploymechanik bereit. Data Engineering definiert den Datenfluss und dessen fachliche Verarbeitung.
- **Software Architecture:** entscheidet in `../Software-Architecture-und-System-Design/` über Systemgrenzen, Plattform-/Deployable-Grenzen, Ownership und strukturelle Patterns. Data Engineering besitzt danach die fachliche Semantik und Betriebslogik des Datenflusses.
- **Requirements Engineering:** definiert später geschäftliche und nichtfunktionale Anforderungen. Data Engineering operationalisiert freigegebene Anforderungen für Datenflüsse.

## Kein Pflichtstack

Airflow, Dagster, dbt, Kafka, Flink, Spark, Beam, Snowflake, BigQuery, Databricks, Iceberg, Delta Lake oder andere Produkte sind mögliche Adapter, keine universelle Architektur.

Ebenso sind keine zentralen Dogmen:

- ELT sei immer besser als ETL;
- Streaming sei reifer als Batch;
- exactly-once sei überall notwendig oder überhaupt verfügbar;
- jedes analytische Modell müsse ein Star Schema sein;
- jeder Backfill dürfe einfach denselben Pfad wie der Tageslauf verwenden;
- jede Datenqualitätsregel brauche denselben Threshold.

## Risikomodell

```text
READ / DESIGN
→ Quellen, Verträge, Lineage und Pipelineverhalten analysieren

VALIDATE
→ Datenqualität, Reconciliation, Dry Runs und bounded Reprocessing prüfen

PUBLISH-SENSITIVE
→ Daten oder Semantik so ändern, dass Consumer neue Ergebnisse sehen

REPLAY / BACKFILL
→ historische Daten erneut verarbeiten oder bestehende Ergebnisse überschreiben/ergänzen

DESTRUCTIVE / CUTOVER
→ Partitionen löschen/ersetzen, Consumer umschalten oder Datenhistorie weitreichend verändern
```

Mit steigender Wirkung steigen Evidence-, Reconciliation-, Preview- und Human-Gate-Anforderungen.

## Zentrale Skills

- `data-pipeline-design`
- `data-ingestion-design`
- `data-transformation-design`
- `analytical-data-modeling`
- `data-quality-design`
- `data-contract-design`
- `data-lineage-analysis`
- `data-orchestration-design`
- `data-engineering-review`

## Leitgedanken

> Source of Truth vor Pipelinekomfort.

> Grain und Semantik vor SQL oder Toolsyntax.

> Replaybarkeit muss entworfen werden, nicht erst beim Incident erfunden.

> Freshness, Vollständigkeit und Korrektheit sind getrennte Qualitätsachsen.

> Lineage ist Evidence über Entstehung und Abhängigkeiten – keine bloße Diagrammdekoration.

> Publish und Backfill sind reale Datenänderungen und brauchen lokale Gates.