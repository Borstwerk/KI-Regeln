# Reliability und System-Observability

## Zweck

Dieser Bereich beschreibt allgemeine, tool- und providerneutrale Regeln dafür, wie laufende Systeme akzeptable Zuverlässigkeit definieren, ihren tatsächlichen Gesundheitszustand sichtbar machen, relevante Verschlechterungen erkennen, Incidents kontrolliert behandeln und aus Betriebsstörungen lernen.

Kernidee:

> Reliability beschreibt gewünschtes Verhalten unter realen Betriebsbedingungen. System-Observability liefert die Evidence, mit der dieses Verhalten beurteilt werden kann.

## Scope

Behandelt werden insbesondere:

- Reliability-Ziele, SLIs, SLOs und Error Budgets;
- System-Observability, Telemetrie und Health-Modelle;
- Alerting und Actionability;
- Incident Response und Koordination;
- Postmortems und Operational Learning;
- Capacity, Saturation und Dependency Health;
- Recovery-Ziele wie RTO/RPO und Disaster-Recovery-Readiness;
- Failure Domains, Graceful Degradation und Resilience;
- kontrollierte Resilience-Experimente, Chaos Engineering und Game Days;
- Toil und nachhaltiger Betrieb;
- Operational Readiness als zusammengesetzte Evidence.

## Nicht der Scope

- **Requirements / Specification Engineering:** definiert später geschäftliche oder vertragliche Zuverlässigkeitsanforderungen. Dieser Bereich darf konkrete Zielwerte nicht erfinden.
- **Software Architecture:** entscheidet später, welche Struktur, Topologie oder technischen Patterns Reliability-Anforderungen erfüllen.
- **Infrastruktur und DevOps:** baut, deployt, skaliert, reconciliert und rollt technische Zielzustände zurück.
- **Data Engineering:** definiert in `../Data-Engineering/` die fachliche Semantik von Datenflüssen und pipeline-spezifische Evidence wie Freshness, Completeness, Data Quality, Consumer Lag, Backlog und Reconciliation. Reliability kann daraus systemweite Objectives, Alerts oder Incidentwirkung ableiten, erfindet aber nicht die Datenbedeutung.
- **Testing und QA:** entwirft reproduzierbare Tests und Failure Cases innerhalb eines Testscopes.
- **Programmieren / Diagnose:** analysiert konkrete technische Ursachen und implementiert Fixes.
- **Datenbanken:** besitzt DB-spezifische Backup-, Restore-, Replication-, Query- und Operationsmechanik.
- **Schnittstellen und Verträge:** definiert Idempotenz-, Retry-, Delivery- und Concurrency-Zusagen.
- **Sicherheit:** besitzt Security Incidents, Forensik, Credential-/Secret-Schutz und Security Policies im Detail.
- **Agentenarbeit:** behandelt Observability und Traceability von Agentenläufen und Arbeitsprozessen, nicht die Runtime-Observability eines Produktsystems.
- **Dokumentationserstellung:** besitzt den allgemeinen `runbook`-Skill.
- **Provider-/Toolsyntax:** OpenTelemetry, Prometheus, Grafana, Datadog, PagerDuty, CloudWatch, Azure Monitor, Google Cloud Operations und andere Systeme bleiben Adapter.

## Zentrale Modelle

```text
Requirement / Critical Journey
→ messbare Reliability Objective
→ Runtime Evidence
→ Bewertung
→ Entscheidung / Aktion über lokales Gate
```

```text
Telemetry
≠
Observability
```

```text
Alert
≠
Incident
≠
automatische Autorisierung einer Produktionsaktion
```

```text
Incident erkannt
→ Impact verstehen
→ stabilisieren / mitigieren
→ Recovery frisch verifizieren
→ danach vollständig erklären und lernen
```

```text
Failure Test
→ reproduzierbarer Failure Mode im Testscope

Resilience Experiment
→ systemische Hypothese unter kontrollierter realistischer Störung
```

## Zentrale Grundsätze

1. **Service- und Nutzerwirkung vor Komponentenstatus.** Ein grüner Prozess oder Host beweist keinen gesunden Service.
2. **100 % ist kein universelles Ziel.** Zielwerte entstehen aus lokaler Anforderung, Risiko und Kosten.
3. **SLOs sind Entscheidungsinstrumente.** Sie sind keine Trophäen und dürfen nicht ohne reale Konsequenz oder Stakeholder proliferieren.
4. **SLI-Spezifikation und Messimplementierung trennen.** Erst definieren, was gemessen werden soll, dann wie und wo die Evidence entsteht.
5. **Error Budget braucht lokale Governance.** Mathematik allein autorisiert weder Freeze noch Deploy.
6. **Telemetrie ist Evidence, nicht Wahrheit.** Fehlende oder fehlerhafte Instrumentierung kann einen scheinbar gesunden Zustand erzeugen.
7. **Observability beantwortet Fragen.** Mehr Daten sind nicht automatisch mehr Erkenntnis.
8. **Alerts brauchen eine erwartete Reaktion.** Paging sollte normalerweise relevante Wirkung anzeigen; Ursachen-Signale bleiben wichtig für Diagnose und Frühwarnung.
9. **Alert Noise ist selbst ein Reliability-Problem.** Ein Signal, das regelmäßig ignoriert wird, verliert Betriebswert.
10. **Im Incident zuerst stabilisieren.** Vollständige Root-Cause-Erklärung darf die Wiederherstellung nicht unnötig blockieren.
11. **Koordination und technische Ausführung trennen.** Ein Incident-Lead besitzt nicht automatisch alle technischen Rechte.
12. **Incident-Dringlichkeit erweitert keine Autorisierung.** Restart, Failover, Traffic Switch, Restore oder Rollback bleiben reale Aktionen mit lokalen Gates.
13. **Recovery braucht Fresh Evidence.** Ein abgeschlossener Befehl oder ein einzelner grüner Check beweist keine wiederhergestellte Nutzerfunktion.
14. **Postmortems untersuchen beitragende Faktoren.** Eine künstlich erzwungene Einzelursache ist kein Qualitätsmerkmal.
15. **Capacity, Saturation und Dependency Health gehören zur Reliability.** Ressourcen- und Abhängigkeitsgrenzen können Nutzerwirkung erzeugen, bevor Komponenten hart ausfallen.
16. **Graceful Degradation und Failure Isolation sind gewünschtes Verhalten.** Welche Architekturpatterns dieses Verhalten erzeugen, entscheidet Software Architecture.
17. **Chaos Engineering ist ein kontrolliertes Hypothesenexperiment.** Steady State, Blast Radius, Abort und Recovery gehören vor die Störung.
18. **Operational Readiness ist zusammengesetzte Evidence.** Kein einzelnes Dashboard, Testgrün oder Review ersetzt die Gesamtsicht.
19. **Toil ist ein Nachhaltigkeitssignal.** Konkrete Quoten oder Zeitbudgets bleiben lokale Organisationsentscheidung.
20. **Konkrete Wahrheit bleibt lokal.** SLO-Werte, Alertschwellen, Severity-Modelle, On-Call-Wege, RTO/RPO, Capacity Limits, Runbooks und Failover-Regeln sind keine universellen Defaults.

## Operative Skills

- `slo-design`
- `system-observability-design`
- `alert-design`
- `incident-response`
- `incident-postmortem`
- `capacity-planning`
- `resilience-experiment`
- `reliability-review`

## Workflows

- `../Workflows/Reliability-Baseline-und-SLOs.md`
- `../Workflows/Produktionsincident.md`
- `../Workflows/Post-Incident-Learning.md`
- `../Workflows/Resilience-Game-Day.md`
- `../Workflows/Operational-Readiness-Review.md`

## Leitgedanken

> Allgemeine Arbeitsweise zentral, konkrete Reliability-Ziele lokal.

> Ein System ist nicht zuverlässig, weil wir viele Signale besitzen, sondern weil wir relevantes Verhalten messen, Störungen kontrolliert behandeln und belastbar daraus lernen.