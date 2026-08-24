# Skill-Handbuch – Reliability und System-Observability

## Wann dieser Bereich hilft

Bei SLI-/SLO-Fragen, System-Observability, Alerting, aktiven Incidents, Postmortems, Capacity Planning, Chaos/Game Days und größeren Reliability-/Operational-Readiness-Reviews.

Der Bereich behandelt **laufende Systeme**. Agentenlauf-Observability und Prozess-Traceability bleiben `Agentenarbeit/`.

## `slo-design`

Für die Operationalisierung von „zuverlässig genug“ in:

- kritischen Nutzer-/Consumererfolg;
- SLI-Spezifikation;
- Messimplementierung;
- Ziel + Fenster;
- optional Error Budget und lokale Governance.

Nicht verwenden, um ohne lokale Grundlage 99.x-Werte, SLAs oder RTO/RPO zu erfinden.

Wichtig:

```text
SLI-Spezifikation
≠
Messimplementierung
```

## `system-observability-design`

Für Betriebsfragen, Health-Modell, Signalbedarf, Korrelation, Coverage, Blind Spots und Telemetrieverifikation.

Der Skill beginnt mit Fragen wie:

> Können wir erkennen, ob der kritische Checkout funktioniert und wo ein Fehler im Flow entsteht?

Er beginnt nicht mit:

> Welches Monitoringprodukt installieren wir?

Metrics, Logs, Traces, Events, Profiles, Synthetic- oder Business-Signale sind mögliche Evidence. Kein fixes „Three Pillars“-Dogma.

## `alert-design`

Für Alerts, Paging oder andere betriebliche Reaktionen.

Prüft:

- betroffene Wirkung / Objective;
- Signal;
- Threshold-Basis;
- Auswertungsfenster;
- Actionability;
- Routing;
- Noise / Flapping;
- Runbook-Einstieg;
- Verifikation.

Der Skill erfindet keine universellen CPU-, Error-, Latenz-, Burn-Rate- oder Severity-Schwellen.

Produktive Pager-/Alertänderungen bleiben gated.

## `incident-response`

Für einen **aktiven** Outage oder eine reale Service-Degradation.

Kern:

```text
Impact
→ Incident State / Rollen
→ aktuelle Evidence
→ stabilisieren / mitigieren
→ Fachdiagnose
→ Gate für reale Aktion
→ Fresh Recovery Evidence
→ Handoff / Abschluss
```

Der Skill ersetzt nicht `diagnose` und besitzt keine impliziten Restart-, Failover-, Rollback- oder Produktionsrechte.

## `incident-postmortem`

Für Operational Learning **nach** einem stabilisierten Incident.

Behandelt:

- Timeline;
- Impact;
- Detection;
- Response;
- Recovery;
- beitragende Faktoren;
- Observability-/Alert-/Runbook-/Process-Gaps;
- Follow-ups mit Owner und späterer Verification.

Keine Pflicht zu einer einzigen Root Cause, fünf Whys oder Schuldzuweisung.

## `capacity-planning`

Für die Frage:

> Wie viel Capacity/Headroom brauchen wir unter Peaks, Wachstum, Failure-Domain-Verlust und realer Scaling-/Provisioning-Zeit?

Abgrenzung:

```text
Load-/Performance-Test
→ misst Ceiling / Degradation

capacity-planning
→ entscheidet über Reserve / Risiko / Kosten

Infra / DevOps
→ setzt Capacity technisch um
```

Keine universellen Headroom-, CPU- oder Autoscalingwerte.

## `resilience-experiment`

Für Chaos Engineering und Game Days mit:

- Steady State;
- falsifizierbarer Hypothese;
- realistischer Störung;
- Environment;
- Blast Radius;
- Observation;
- Abort;
- Recovery;
- Permission/Execution Gate;
- Ergebnis gegen die Hypothese.

Standardmodus ist **PLAN / REVIEW**.

Reale Fault Injection braucht explizite Autorisierung und passende Capability. Produktion ist kein notwendiges Reifeziel.

Für einen einzelnen reproduzierbaren Fault innerhalb eines Testscopes bleibt `failure-testing` zuständig.

## `reliability-review`

Unabhängiger Gesamtcheck über:

- Critical Journeys / Objectives;
- Observability / Alerts;
- Dependencies / Failure Domains;
- Capacity / Saturation;
- Degradation / Isolation;
- Recovery / RTO / RPO;
- Incident-/Runbook-Readiness;
- Postmortem-/Learning-Schleifen;
- Resilience Evidence;
- Toil;
- Deployment-/Security-/Permission-Grenzen;
- Missing Evidence.

Mögliche Verdicts:

```text
READY_FOR_LOCAL_GATE
READY_WITH_FINDINGS
BLOCKED
UNVERIFIED
```

Kein Verdict ist automatische Deploy-/Releasefreigabe.

## Fünf Standardworkflows

### Reliability Baseline und SLOs

`../Workflows/Reliability-Baseline-und-SLOs.md`

```text
Requirements / Critical Journeys
→ slo-design
→ system-observability-design
→ alert-design
→ optional capacity-planning
→ reliability-review
→ lokales Gate
```

### Produktionsincident

`../Workflows/Produktionsincident.md`

```text
Impact
→ incident-response
→ Fachdiagnose
→ Mitigation + Gate
→ autorisierte Aktion
→ Fresh Recovery
```

### Post-Incident Learning

`../Workflows/Post-Incident-Learning.md`

```text
Incident Evidence
→ incident-postmortem
→ Detection / Response / Recovery Gaps
→ fachliche Follow-ups
→ spätere Verification
```

### Resilience Game Day

`../Workflows/Resilience-Game-Day.md`

```text
Hypothese
→ Experimentdesign
→ Safety / Gate
→ optional Ausführung
→ Recovery
→ Hypothese bewerten
```

### Operational Readiness Review

`../Workflows/Operational-Readiness-Review.md`

```text
Objectives
+ Observability
+ Alerts
+ Capacity / Dependencies
+ Recovery / Runbooks
+ Testing / Resilience
+ Deployment
+ Security
+ Ownership
→ reliability-review
→ lokales Go / No-Go
```

Operational Readiness ist bewusst **Workflow statt Mega-Skill**.

## RTO/RPO

RTO/RPO gehören als Recovery-Ziele fachlich in den Reliability-Bereich, besitzen aber zunächst keinen eigenen Skill.

```text
Requirements / Business
→ akzeptable Recovery-Ziele

Reliability
→ operationalisiert und prüft die Ziele

DB / Infra
→ implementiert Backup, Restore, Replication, Failover
```

## Architekturgrenze

```text
Reliability
→ welches Verhalten unter Störung benötigt wird

Software Architecture
→ welche Struktur / Patterns dieses Verhalten erreichen
```

Beispiel:

Reliability darf fordern, dass Checkout trotz Ausfall einer optionalen Recommendation-Dependency weiter funktioniert.

Ob dafür Cache, Timeout, Bulkhead, Circuit Breaker, Fallback oder eine andere Struktur geeignet ist, entscheidet die Architektur im lokalen Kontext.

## Tooladapter

OpenTelemetry, Prometheus, Grafana, Datadog, PagerDuty, Elastic, Splunk, New Relic, CloudWatch, Azure Monitor, Google Cloud Operations, Kubernetes und andere Systeme bleiben konkrete Adapter.

## Maturity

Alle acht Skills starten `experimental` mit `partial` Evalabdeckung.

Für jeden Skill sind sechs Evalfälle definiert, insgesamt 48. Diese definierten Fälle sind **kein Nachweis, dass die Evals bereits ausgeführt oder bestanden wurden**.

## Leitgedanke

> Reliability ist die Verbindung aus relevanten Zielen, glaubwürdiger Runtime-Evidence, kontrollierter Reaktion und nachweisbarem Lernen – nicht ein bestimmter Toolstack.