# Workflow – Post-Incident Learning

## Ziel

Nach einem stabilisierten Incident aus Evidence konkrete, fachlich richtig zugeordnete Verbesserungen ableiten und deren spätere Wirkung verifizierbar machen.

## Ablauf

```text
Incident abgeschlossen / stabilisiert
→ incident-postmortem
→ Timeline / Impact / Contributing Factors
→ Detection Gaps
→ Response Gaps
→ Recovery Gaps
→ fachliche Follow-ups
→ Owner / Priorisierung
→ spätere Fresh Verification
```

## 1. Evidence sammeln

Bevorzugt:

- Incident State / Timeline;
- Alerts und Telemetrie;
- Change-/Deploy-Historie;
- Runbooks;
- Nutzer-/Consumerimpact;
- Mitigation-/Recovery-Ergebnisse.

Hypothesen und widersprüchliche Evidence sichtbar lassen.

## 2. Postmortem

`incident-postmortem` untersucht:

- Impact;
- Detection;
- Response;
- Recovery;
- beitragende Faktoren;
- was funktioniert hat;
- was Bearbeitung erschwert hat;
- offene Fragen.

Keine Pflicht zu genau einer Root Cause oder einer bestimmten Anzahl Action Items.

## 3. Fachliche Follow-ups

Mögliche Handoffs:

```text
SLO / Objective Gap
→ slo-design

Telemetry Blind Spot
→ system-observability-design

Alert Noise / Miss
→ alert-design

Capacity / Saturation
→ capacity-planning

Systemic Failure Behavior
→ resilience-experiment / später Software Architecture

reproduzierbarer Failure Case
→ failure-testing

Runbook Gap
→ runbook

Infra / Deploy / DB / Interface / Security
→ jeweilige Fachdomäne
```

## 4. Owner und Wirkung

Follow-ups sollen enthalten:

- welches Risiko reduziert werden soll;
- Owner;
- Priorität / rationale Einordnung;
- gewünschte Evidence für Completion.

## 5. Spätere Verifikation

Nicht nur prüfen, ob Tickets geschlossen wurden.

Je nach Maßnahme beispielsweise:

- Alert test-fired;
- neue Telemetrie im echten Flow sichtbar;
- Failure-Test grün;
- Recovery-Rehearsal durchgeführt;
- Capacity neu gemessen;
- SLO/Runbook aktualisiert;
- Resilience-Experiment bestätigt geändertes Verhalten.

## Leitgedanke

> Lernen endet nicht beim Postmortemtext. Es endet dort, wo die relevante Risikoreduktion später tatsächlich nachgewiesen werden kann.