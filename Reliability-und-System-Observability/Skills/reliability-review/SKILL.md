---
name: reliability-review
description: Auditiert einen Service, ein Systemdesign oder einen Betriebsstand unabhängig auf Reliability Objectives, Observability, Alerting, Failure Domains, Dependencies, Capacity, Degradation, Recovery, Incident Readiness, Toil und Evidence. Verwenden für größere Reliability-/Operational-Readiness-Reviews. Nicht als Implementierungs-, Pentest- oder Produktionsaktionsskill verwenden.
---

# Reliability Review

## Ziel

Reliability eines Systems über mehrere Prüfachsen unabhängig bewerten und Lücken mit Evidence, Impact und passender Fachübergabe sichtbar machen.

## Eingaben

- lokaler Scope und kritische Flows;
- Requirements / SLOs / Recovery-Ziele;
- Architektur-/Dependency-Kontext;
- Runtime-Telemetrie und Health-Evidence;
- Alerting / Runbooks;
- Capacity-/Load-Evidence;
- Incident-/Postmortem-Historie, falls relevant;
- Testing-/Recovery-/Resilience-Evidence;
- Infra-/Deployment-/Security-Informationen.

## Prüfachsen

1. Scope, Critical Journeys und Ownership;
2. Reliability Objectives / SLI/SLO-Basis;
3. System-Observability und Blind Spots;
4. Alerting / Actionability / Noise;
5. Dependencies und Failure Domains;
6. Capacity / Saturation / Headroom / Quotas;
7. Graceful Degradation / Failure Isolation;
8. RTO/RPO / Recovery Readiness;
9. Incident Response / Runbooks / Handoffs;
10. Postmortem-/Learning-Schleifen;
11. Failure-/Resilience-Evidence;
12. Toil / nachhaltiger Betrieb;
13. Deployment-/Rollback-/Promotion-Evidence;
14. Security-/Permission-Grenzen;
15. Missing / stale / widersprüchliche Evidence.

## Arbeitsweise

- lokale Sources of Truth zuerst;
- tatsächliche Runtime-Evidence von Designabsicht trennen;
- keine Zielwerte, Thresholds oder Severitymodelle erfinden;
- Findings nach Nutzer-/Businessimpact, Blast Radius, Recoveryrisiko und Evidence priorisieren;
- tiefe Fachanalyse an `slo-design`, `alert-design`, `capacity-planning`, `incident-postmortem`, `resilience-experiment` oder Nachbardomänen übergeben;
- keine Reparatur, Re-Architecture oder Produktionsaktion aus dem Review ableiten.

## Architekturgrenze

Reliability Review darf feststellen:

> Kritischer Flow bricht unnötig vollständig bei Dependency-Ausfall; gewünschtes Degradationsverhalten fehlt.

Es soll nicht ungefragt entscheiden:

> Deshalb muss Pattern X mit Produkt Y implementiert werden.

Diese Designentscheidung gehört später zu Software Architecture beziehungsweise zum lokalen Projekt.

## Evidence

Mögliche Status pro Finding:

- `CONFIRMED` – direkte passende Evidence;
- `LIKELY` – starke Indizien, aber unvollständig;
- `UNVERIFIED` – plausible Frage ohne ausreichende Evidence;
- `CONFLICTING` – Quellen/Evidence widersprechen sich.

Keine Repo-/Config-Evidence als Live-Systemzustand ausgeben.

## Verdict

Empfohlene Review-Verdicts:

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_FINDINGS`
- `BLOCKED`
- `UNVERIFIED`

Verdict ist keine Deploy-/Release-/Produktionsautorisierung.

## Nicht tun

- „alles grün“ aus Dashboards allein ableiten;
- SLO-Lücke durch erfundene 99.x-Werte reparieren;
- konkrete DB-/Infra-/Security-Mechanik als Reliability-Universalregel bewerten;
- fehlende Production Evidence als PASS behandeln;
- Reviewfinding ungefragt implementieren;
- Toolzugriff als Autorisierung einer Betriebsänderung behandeln.

## Ausgabe

```text
Scope
Sources of Truth
Critical Flows / Objectives
Findings [priority, evidence status, impact]
Observability / Alerting Gaps
Dependency / Failure-Domain Risks
Capacity / Saturation Risks
Degradation / Resilience Gaps
Recovery / RTO / RPO Gaps
Incident / Runbook / Learning Gaps
Toil / Sustainability Gaps
Missing / Conflicting Evidence
Required Handoffs
Verdict
```

## Related

- `slo-design`
- `system-observability-design`
- `alert-design`
- `incident-response`
- `incident-postmortem`
- `capacity-planning`
- `resilience-experiment`
- `infrastructure-review`
- `test-suite-review`
- `database-review`

## Leitgedanke

> Ein Reliability Review findet systemische Lücken und fehlende Evidence. Es wird nicht dadurch besser, dass es heimlich alle Fachdomänen selbst übernimmt.