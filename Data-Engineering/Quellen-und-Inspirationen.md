# Quellen und Inspirationen – Data Engineering

Dieser Bereich ist bewusst tool- und plattformneutral. Externe Quellen dienen als Referenz für belastbare Konzepte und Gegenbeispiele; sie werden nicht ungeprüft zu lokalen Regeln erklärt.

## Apache Airflow

- Core Concepts: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/
- Backfill: https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/backfill.html

Nützlich für:

- explizite Workflow-/Task-Abhängigkeiten;
- Data Intervals;
- Retries und Re-runs;
- Backfill als eigene kontrollierte Operation.

Nicht übernommen wird die Annahme, dass DAG-basierte Orchestrierung oder Airflow selbst für jede Pipeline nötig ist.

## Apache Beam

- Basics of the Beam model: https://beam.apache.org/documentation/basics/
- Programming Guide: https://beam.apache.org/documentation/programming-guide/

Nützlich für:

- bounded vs. unbounded data;
- Event Time vs. Processing Time;
- Windows, Watermarks, Triggers und Late Data;
- bewusste Trade-offs zwischen Latenz und Vollständigkeit.

Nicht übernommen wird Beam-spezifische SDK-/Runnermechanik als zentrale Pflicht.

## Apache Kafka

- Kafka Streams configuration: https://kafka.apache.org/documentation/#streamsconfigs

Nützlich als Gegenbeispiel gegen pauschale Aussagen zu Delivery-/Processing Guarantees: selbst bei einem verbreiteten Streamingstack sind at-least-once und exactly-once konkrete konfigurations- und umgebungsabhängige Zusagen.

Kafka ist kein Pflichtbestandteil des Bereichs.

## OpenLineage

- About / Specification: https://openlineage.io/docs/
- Object Model: https://openlineage.io/docs/spec/object-model/

Nützlich für:

- Dataset-/Job-/Run-Modell;
- Design- und Runtime-Lineage;
- interoperable Lineage-Metadaten.

OpenLineage wird als wichtige offene Referenz betrachtet, nicht als vorgeschriebener Collector oder Backendstack.

## Open Data Contract Standard / Data Contract CLI

- ODCS overview: https://docs.datacontract.com/open-data-contract-standard
- Schema: https://docs.datacontract.com/schema
- Quality Rules: https://docs.datacontract.com/quality-rules
- Service Levels: https://docs.datacontract.com/service-levels

Nützlich für die Erkenntnis, dass ein Data Contract mehr als DDL sein kann und Struktur, Semantik, Quality, Service Levels und Ownership explizit machen kann.

ODCS ist eine vendor-neutrale Referenz, aber kein zentrales Pflichtformat.

## AWS Well-Architected – Data Analytics Lens

- https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/

Nützlich für:

- Source-Data-Quality vor Transfer;
- Betriebsmetriken für Processing Jobs und Source Availability;
- Versionierung, Staging, Validierung, Rollback und Backfill als Teil operativer Reife.

Providerkonkrete AWS-Mechanik wird nicht übernommen.

## Öffentliche Agent-Skills

### vaquarkhan/data-engineering-agent-skills

- `skills/data-specification/SKILL.md`
- `skills/safe-backfill-and-replay-orchestration/SKILL.md`

Nützliche Impulse:

- Spec vor Pipelinecode;
- Grain, Source, Destination, Quality, Ownership und Replay explizit machen;
- Backfill als risikoreiche Datenoperation mit bounded scope, Idempotenz, Reconciliation und Publish-Gate behandeln.

Bewusst nicht übernommen:

- die sehr feingranulare 70+-Skill-Taxonomie;
- konkrete Hook-/Templatepflichten;
- bestimmte Tool-/Plattformpresets;
- pauschale Mindestchecks oder Schwellen als universelle Vorgabe.

## Grundsatz für Quellenübernahme

> Externe Best Practices sind Hypothesen für gute lokale Regeln. Übernommen wird nur, was technologieübergreifend, begründbar und mit den Repository-Grenzen vereinbar ist.

Mutable Referenzen mit direkter lokaler Wirkung werden zusätzlich in `../Dokumentation/upstream-sources.yml` registriert.