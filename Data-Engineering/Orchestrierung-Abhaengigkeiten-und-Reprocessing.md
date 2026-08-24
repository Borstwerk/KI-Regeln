# Orchestrierung, Abhängigkeiten und Reprocessing

## Zweck

Orchestrierung koordiniert, wann Datenarbeit ausgeführt werden darf und welche Voraussetzungen dafür erfüllt sein müssen. Sie ersetzt weder fachliche Datenlogik noch Quality Verification.

## Abhängigkeiten

Abhängigkeiten möglichst nach dem realen Datenzustand modellieren:

- benötigtes Inputdataset verfügbar;
- Partition/Zeitraum vollständig genug;
- vorgelagerter Contract/Quality Gate erfüllt;
- Referenzdaten in passender Version vorhanden;
- Consumer-/Publishfenster geöffnet.

Eine Uhrzeit allein ist oft nur ein Proxy für Datenverfügbarkeit.

## Scheduling

Mögliche Trigger:

- Zeit-/Kalenderplan;
- Daten-/Asset-Verfügbarkeit;
- Event;
- expliziter manueller Start;
- abhängiger Workflow.

Kein Trigger ist universell vorzuziehen.

## Data Interval

Bei periodischen Pipelines klar trennen:

- wann ein Run startet;
- welchen Datenzeitraum er verarbeitet;
- welche Event-/Source-Zeit relevant ist;
- welche verspäteten Daten noch berücksichtigt werden.

`run_date` und fachlicher Datenzeitraum sind nicht automatisch identisch.

## Retries

Retry ist geeignet für potenziell temporäre technische Fehler, wenn Wiederholung sicher ist.

Vor Retry prüfen:

- Write-Idempotenz;
- externe Side Effects;
- partielle Writes;
- Source-/API-Quotas;
- Backoff/Jitter entsprechend lokalem System;
- ob der Fehler überhaupt transient ist.

Ein Retry repariert keine falsche Datenlogik.

## Reprocessing / Backfill

Orchestrierung für historische Wiederholung muss zusätzlich berücksichtigen:

- begrenzte Intervalle/Partitionen;
- Parallelität und Source-/Target-Last;
- Reihenfolge bei stateful/historisierten Daten;
- Abhängigkeiten zwischen Zeitfenstern;
- Pause oder Schutz normaler Publishpfade;
- Reconciliation vor Freigabe.

## Catchup

Automatisches Nachholen verpasster Intervalle kann sinnvoll oder gefährlich sein. Es hängt von Datenvolumen, Source-Retention, Idempotenz, Consumerwirkung und Ressourcen ab.

Nie allein aus Scheduler-Default übernehmen.

## Toolgrenze

Airflow, Dagster, Prefect, Argo Workflows, cron oder Cloud-Scheduler sind Implementierungen. Der zentrale Skill beschreibt Abhängigkeiten, Intervalle, Retry-/Reprocessing-Semantik und Gates.

## Nicht tun

- DAG-Erfolg als Beweis für Datenqualität ansehen;
- feste Retryanzahlen oder Zeitouts global setzen;
- Uhrzeit mit Source-Vollständigkeit gleichsetzen;
- automatische Catchup-/Backfill-Ausführung ungeprüft aktivieren;
- Schedulerzugriff als Freigabe für produktives Reprocessing behandeln.