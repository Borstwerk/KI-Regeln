---
name: system-observability-design
description: Entwirft oder prüft die System-Observability eines laufenden Services aus kritischen Flows, Betriebsfragen, Health-Modell, benötigter Evidence, Signalquellen, Korrelation, Coverage und Blind Spots. Verwenden bei Monitoring-/Telemetry-/Instrumentation-Design. Nicht als OpenTelemetry-, Prometheus-, Grafana- oder Vendor-Konfigurationsskill verwenden.
---

# System Observability Design

## Ziel

Relevante Betriebsfragen eines Systems mit geeigneter, prüfbarer Evidence beantwortbar machen, ohne Tool- oder Signaltypen zum Selbstzweck zu machen.

## Eingaben

- kritische Nutzer-/Consumerflows;
- SLOs / Reliability Objectives, falls vorhanden;
- System-/Dependency-Grenzen;
- vorhandene Telemetrie;
- bekannte Incident-/Diagnosefragen;
- Datenschutz-/Security-/Retention-Regeln;
- technische Kosten-/Backendgrenzen.

## Arbeitsweise

1. Kritische Flows und konkrete Betriebsfragen bestimmen.
2. Health-Modell von Nutzer-/Businesswirkung bis zu Dependencies und Ressourcen skizzieren.
3. Für jede Frage die benötigte Evidence definieren.
4. Geeignete Signalquellen auswählen: zum Beispiel Metrics, Logs, Traces, Events, Profiles, Synthetic, Client-/Business-Signale.
5. Korrelation über relevante Grenzen definieren.
6. Coverage, Sampling, Cardinality, Kosten, Retention und Datenschutz prüfen.
7. Blind Spots und nicht glaubwürdig messbare Zustände ausdrücklich markieren.
8. Verifikation der Telemetrie selbst definieren.
9. Konkrete SDK-/Collector-/Backend-Implementierung an Programmierung/Infra/Adapter übergeben.

## Grenzen

- Telemetrie ist Evidence, nicht Wahrheit;
- Metrics + Logs + Traces sind keine Pflichtdefinition von Observability;
- OpenTelemetry ist eine wichtige mögliche Interoperabilitätsreferenz, keine Pflichtarchitektur;
- Agenten-Traceability bleibt `Agentenarbeit/`;
- Alertlogik im Detail gehört zu `alert-design`;
- konkrete Root-Cause-Diagnose gehört zu `diagnose` beziehungsweise Fachskills.

## Nicht tun

- pauschal Prometheus/Grafana/Datadog/OTel vorschreiben;
- jedes Feature mit denselben RED-/USE-Signalen erzwingen;
- High Cardinality pauschal verbieten, ohne Signaltyp/Backend zu betrachten;
- PII, Secrets oder vollständige Payloads als bequeme Debug-Telemetrie verlangen;
- einen grünen Dashboardzustand als bewiesene Servicegesundheit ausgeben;
- fehlende Runtime-Evidence durch Architekturannahmen ersetzen.

## Ausgabe

```text
Scope / Critical Flows
Operational Questions
Health Model
Required Evidence
Signal Sources
Correlation
Coverage / Blind Spots
Cardinality / Cost / Retention
Privacy / Security
Telemetry Verification
Implementation Gaps / Handoffs
```

## Related

- `slo-design`
- `alert-design`
- `incident-response`
- `reliability-review`
- `diagnose`

## Leitgedanke

> Gute Observability beginnt mit einer wichtigen Frage, nicht mit einem Dashboard oder SDK.