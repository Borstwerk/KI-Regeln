# Pipeline-Observability und Betriebsgrenzen

## Zweck

Datenpipelines brauchen Evidence über Verarbeitung und Datenzustand. Diese Evidence ergänzt System-Observability, ersetzt sie aber nicht.

## Zwei Ebenen

### Technische Pipelinegesundheit

Zum Beispiel:

- Run-/Taskstatus;
- Laufzeit und Queuezeit;
- Retry-/Failure-Rate;
- Throughput;
- Backlog / Consumer Lag;
- Resource-/Quota-Saturation.

### Datenzustand

Zum Beispiel:

- Freshness;
- erwartete Partitionen/Intervalle;
- Completeness;
- Volume;
- Schema-/Contractstatus;
- Quality-/Reconciliation-Ergebnis;
- Publishstatus.

Ein grüner Scheduler kann fachlich falsche oder alte Daten produzieren. Umgekehrt kann ein technisch fehlgeschlagener Retry trotzdem bereits partielle Daten geschrieben haben.

## Correlation

Wo sinnvoll, Evidence korrelierbar machen über:

- Pipeline/Job-ID;
- Run-ID;
- Datenintervall/Partition;
- Dataset-Version;
- Code-/Deployment-Version;
- Source-/Offset-/Snapshot-Referenz;
- Quality-/Publish-Ergebnis.

OpenLineage ist eine mögliche Referenz für Job-/Run-/Dataset-Metadaten, aber keine Pflicht.

## Reliability-Grenze

`Reliability-und-System-Observability/` definiert systemweite Healthmodelle, SLOs, Alerting und Incident Response.

Data Engineering liefert dafür pipeline-spezifische Signale und fachliche Datenzustände. Ein Freshness-SLO kann im Reliability-Kontext operationalisiert werden, während die fachliche Definition des Datenzeitpunkts aus dem Datenprodukt kommt.

## Alerts

Pipelinealerts sollen wie andere Alerts actionability-orientiert sein. Nicht jede Taskwarnung braucht Paging.

Bei Datenpipelines können Nutzerwirkung und technische Ursache zeitlich auseinanderliegen: eine Quelle kann ausfallen, obwohl der letzte veröffentlichte Stand noch innerhalb des erlaubten Freshnessfensters liegt.

## Recovery

Nach Pipelinefehlern nicht nur Jobstatus prüfen, sondern je nach Risiko:

- partielle Writes;
- fehlende/duplizierte Daten;
- Offsets/Cursor/Checkpoints;
- Backlog;
- Quality/Reconciliation;
- Consumerpublish;
- notwendiges Reprocessing.

## Nicht tun

- Scheduler-Dashboard als Beweis für korrekte Daten behandeln;
- reine CPU-/Memory-Metriken als Data Quality ausgeben;
- Consumer Lag ohne fachlichen Zeit-/Volumenkontext universell bewerten;
- technische Recovery mit fachlicher Datenrecovery gleichsetzen;
- globale Alertschwellen im Data-Engineering-Bereich erfinden.