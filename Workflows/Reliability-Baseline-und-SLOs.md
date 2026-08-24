# Workflow – Reliability Baseline und SLOs

## Ziel

Für einen Service oder kritischen Flow erstmals eine belastbare Reliability-Baseline aus Zielen, Messbarkeit, Alerting und relevanten Capacity-/Dependency-Risiken aufbauen.

## Ablauf

```text
lokale Requirements / kritische Journeys
→ slo-design
→ system-observability-design
→ alert-design
→ optional capacity-planning
→ reliability-review
→ lokales Reliability-/Produkt-Gate
```

## 1. Lokale Wahrheit

Vorher klären:

- kritische Nutzer-/Consumerflows;
- Business-/Produkt-/Contract-Anforderungen;
- bestehende SLA/RTO/RPO, falls relevant;
- System-/Dependency-Grenzen;
- vorhandene Baseline und Runtime-Evidence;
- Owner / Stakeholder.

Keine Zielwerte aus allgemeinen Best Practices erfinden.

## 2. SLO Design

`slo-design` liefert:

- SLI-Spezifikation;
- Measurement-Ansatz;
- Ziel + Fenster als lokal freigegeben / Kandidat / unknown;
- optional Error Budget;
- Governance-/Evidence-Gaps.

## 3. Observability

`system-observability-design` prüft, ob relevante SLI-, Health- und Diagnosefragen tatsächlich beantwortbar sind.

Fehlende Telemetrie ist ein Gap, kein Grund, SLO-Messung zu simulieren.

## 4. Alerting

`alert-design` koppelt relevante Verschlechterung an eine erwartete Reaktion.

Schwellen aus lokaler Evidence ableiten; keine universellen Page-/Burn-Rate-Werte übernehmen.

## 5. Capacity optional

`capacity-planning`, wenn Peak, Wachstum, Scaling Lead Time, Quotas oder Failure-Domain-Verlust für den kritischen Flow entscheidungsrelevant sind.

Load-/Performance-Evidence kann dafür Voraussetzung sein.

## 6. Review

`reliability-review` prüft die Baseline unabhängig auf:

- Zielklarheit;
- Messbarkeit;
- Blind Spots;
- Alerting;
- Dependencies/Capacity;
- Recovery-/Resilience-Gaps;
- Missing Evidence.

## Gate

Reviewstatus und Error Budget sind keine automatische Freigabe.

Die lokale Produkt-/Betriebsgovernance entscheidet, welche Objectives und Policies verbindlich werden.

## Ergebnis

```text
Critical Journeys
Reliability Objectives
SLI / SLO Definitions
Observability Coverage
Alert Model
Capacity / Dependency Risks
Open Evidence Gaps
Review Verdict
Local Decision Status
```

## Leitgedanke

> Reliability beginnt mit einem relevanten Nutzererfolg und endet nicht beim Dashboard.