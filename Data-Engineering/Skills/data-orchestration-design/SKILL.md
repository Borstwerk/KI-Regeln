---
name: data-orchestration-design
description: Entwirft oder prüft Scheduling, Datenabhängigkeiten, Data Intervals, Retries, Catchup, Reprocessing und Backfill-Orchestrierung für Datenpipelines. Verwenden bei DAG-/Scheduler-/Abhängigkeitsfragen. Nicht als fachliche Transformationslogik, allgemeiner Infra-Scheduler-Skill oder ungefragter produktiver Reprocessing-Skill verwenden.
---

# Data Orchestration Design

## Ziel

Ausführungsreihenfolge und Wiederholung so koordinieren, dass Runs zum richtigen Datenzustand gehören und sicher reprocessbar bleiben.

## Eingaben

- Pipeline-/Datasetabhängigkeiten;
- Cadence / Availability-Anforderungen;
- Data-Interval-/Zeitsemantik;
- Retry-/Failure-Verhalten;
- Source-/Target-Quotas und Ressourcen;
- Catchup-/Backfillbedarf;
- Publish-/Consumerregeln;
- vorhandener Scheduler, falls lokal festgelegt.

## Arbeitsweise

1. fachliche Datenabhängigkeiten vor Taskgraph bestimmen.
2. Triggerart bewusst wählen: Zeit, Asset/Data, Event, manuell oder abhängig.
3. Run-Zeit von verarbeitetem Data Interval trennen.
4. Voraussetzungen für vollständige Inputs definieren.
5. Retry nur für geeignete, wiederholbare Fehlerpfade planen.
6. Idempotenz und partielle Writes vor automatischer Wiederholung prüfen.
7. Catchup-/Backfill-Semantik mit bounded intervals, Parallelität und Source/Target Impact definieren.
8. Reprocessing von normalem Tageslauf unterscheiden, wo Risiko/Semantik abweicht.
9. Quality-/Reconciliation- und Publish-Gates an passenden Punkten platzieren.
10. konkrete Schedulerimplementierung erst aus lokalem Tooling ableiten.

## Stop-/Übergaberegeln

- Transformationssemantik → `data-transformation-design`;
- Datenqualität → `data-quality-design`;
- generische Infrastruktur-/Compute-/Schedulerbereitstellung → Infrastruktur und DevOps;
- produktiver Backfill/Offset-/Partition-Change → lokales Execution Gate.

## Nicht tun

- Airflow/Dagster/Prefect als universellen Standard setzen;
- DAG-Erfolg mit korrektem Dataset gleichsetzen;
- feste Retryanzahl, Timeout oder Backoffwerte erfinden;
- Uhrzeit als Beweis für Source-Vollständigkeit behandeln;
- Catchup aus Scheduler-Default ungeprüft aktivieren;
- Backfills ohne bounded scope und Reconciliation starten.

## Ausgabe

```text
Pipeline / Data Dependencies
Trigger Model
Data Interval / Time Semantics
Input Readiness
Retry / Failure Semantics
Catchup / Reprocessing
Backfill Scope / Parallelism
Quality / Publish Gates
Resource / Source Impact
Tool Adapter / Gates / Missing Evidence
```

## Related

- `data-pipeline-design`
- `data-ingestion-design`
- `data-transformation-design`
- `data-quality-design`
- `deployment-strategy`
- `capacity-planning`

## Leitgedanke

> Ein Scheduler koordiniert Datenarbeit; er entscheidet nicht, ob die Daten fachlich richtig sind.