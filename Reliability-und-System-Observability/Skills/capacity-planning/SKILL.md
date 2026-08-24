---
name: capacity-planning
description: Entwickelt oder prüft einen Capacity Plan aus realer Last, Peaks, gemessenen Grenzen, Saturation, Wachstum, Failure Domains, Scaling-/Provisioning-Lead-Time und Kosten-/Risikotrade-offs. Verwenden bei Headroom-, Peak-, Quota-, Skalierungs- oder Kapazitätsfragen. Nicht als Load-Test- oder tatsächlicher Scaling-/Provisioning-Skill verwenden.
---

# Capacity Planning

## Ziel

Aus belastbarer Workload- und Capacity-Evidence eine begründete Reserve- und Kapazitätsentscheidung ableiten, ohne universelle Headroom- oder Autoscalingwerte zu erfinden.

## Eingaben

- aktuelle Last, Peaks und Workloadform;
- bekannte Events / saisonale Spitzen;
- Wachstum / Forecast;
- gemessene Degradation-/Capacity-/Breaking-Points;
- Saturation-Signale;
- kritische Dependencies und Quotas;
- Failure Domains;
- Scaling-/Provisioning-Lead-Time;
- SLO-/Reliability-Ziele;
- Kosten-/Budgetkontext, falls relevant.

## Arbeitsweise

1. Scope und kritischen Flow bestimmen.
2. aktuelle Last und relevante Peaks aus realer Evidence erfassen.
3. vorhandene gemessene Kapazitäts-/Degradationsgrenze prüfen; bei fehlender Messung Gap markieren.
4. limitierenden Constraint beziehungsweise relevante Downstream-Grenze bestimmen.
5. Wachstum und bekannte Events getrennt modellieren; Unsicherheit sichtbar machen.
6. Failure-Domain-Szenarien berücksichtigen, wenn lokal relevant.
7. Scaling-/Provisioning-Lead-Time und Warm-up/Cold-Start berücksichtigen.
8. erforderlichen Headroom aus Failure Cost, Variabilität, Lead Time und Unsicherheit begründen.
9. Kosten, Quotas und Downstream-Folgen als Trade-off dokumentieren.
10. technische Scaling-/Provisioning-Umsetzung an Infra/Architektur übergeben.

## Grenzen

```text
Load-/Performance-Test
→ liefert gemessene Belastungsgrenzen

capacity-planning
→ macht daraus eine Betriebs-/Risikokapazitätsentscheidung

Infra / DevOps
→ setzt technische Kapazität oder Scaling um
```

## Nicht tun

- 20/30/50 % Headroom pauschal festlegen;
- CPU als universellen Constraint behandeln;
- feste Forecast-Historienlängen verlangen;
- Autoscaling als Ersatz für Headroom ausgeben;
- „scale up fast, down slow“ als zentrale Pflichtregel setzen;
- Produktionscapacity ungefragt verändern;
- fehlende Load-Evidence als gemessenen Ceiling ausgeben;
- Downstream-Limits bei horizontalem Scaling ignorieren.

## Ausgabe

```text
Scope / Critical Flow
Demand Baseline
Peak / Variability
Known Events
Measured Capacity / Ceiling
Constraining Resource / Dependency
Growth Assumptions + Uncertainty
Failure-Domain Scenario
Scaling / Provisioning Lead Time
Current Headroom
Required Headroom + Rationale
Cost / Quota / Downstream Trade-offs
Missing Evidence
Capacity Recommendation
Execution Handoff / Gate
```

## Related

- `slo-design`
- `system-observability-design`
- `reliability-review`
- `failure-testing`
- `deployment-strategy`
- `infrastructure-as-code`

## Leitgedanke

> Capacity Planning entscheidet über Reserve unter realen Risiken. Ein Load-Test misst nur, wo die Grenzen liegen.