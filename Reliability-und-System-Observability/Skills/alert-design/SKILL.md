---
name: alert-design
description: Entwirft oder prüft actionable Alerts aus Reliability-Zielen, realer Nutzer-/Systemwirkung, Signalbasis, Threshold-Begründung, Auswertungsfenster, Routing, Noise und Verifikation. Verwenden bei Paging-/Alerting-Fragen. Nicht zur Erfindung lokaler Severitymodelle, universeller Schwellen oder ungefragter produktiver Alertänderungen verwenden.
---

# Alert Design

## Ziel

Einen relevanten Betriebszustand so an eine erwartete Reaktion koppeln, dass das Signal rechtzeitig, verständlich und möglichst rauscharm ist.

## Eingaben

- Reliability Objective / kritischer Flow / Betriebsrisiko;
- vorhandene Signalquelle;
- SLO/Baseline/Capacity-Grenzen, falls vorhanden;
- erwartete Reaktion;
- Ownership / Routing;
- lokale Severity-/On-Call-Policy;
- vorhandene Runbooks.

## Arbeitsweise

1. Betroffenen Flow oder Objective benennen.
2. Definieren, welcher beobachtbare Zustand eine Reaktion benötigt.
3. Symptom-/Impact-Signal und mögliche Ursachen-Signale unterscheiden.
4. Threshold-Basis und Auswertungsfenster aus lokaler Evidence ableiten; bei fehlender Basis Gap markieren.
5. Actionability bestimmen: Was soll der Empfänger entscheiden oder tun?
6. Routing/Dringlichkeit aus lokaler Ownership/Policy übernehmen.
7. Runbook-/Evidence-Einstieg verknüpfen.
8. Noise-, Flapping-, Deduplizierungs- und Suppression-Risiken prüfen.
9. Test-/Verifikationsmethode für Signal, Routing und Resolve-Verhalten definieren.
10. Produktive Änderung nur nach lokalem Gate.

## Symptom / Cause

Paging bevorzugt normalerweise relevante Nutzer-/Consumerwirkung oder unmittelbar drohenden Impact.

Ursachen-Signale können trotzdem alertwürdig sein, wenn sie zuverlässig eine zeitkritische Reaktion erfordern.

Keine Dogmen:

- `CPU > 80 %` ist keine universelle Page-Regel;
- Cause Alerts sind nicht pauschal verboten;
- jeder Alert braucht nicht dieselbe Severityklasse.

## SLO / Burn Rate

Burn-Rate-Alerting kann sinnvoll sein, wenn SLO, Traffic und Entscheidungsmodell passen.

Keine festen Faktoren, Fenster oder Multiwindow-Kombinationen zentral erfinden.

Bei Low-Traffic-Systemen alternative Signalmodelle erwägen.

## Nicht tun

- Schwellen ohne SLO, Baseline, fachliche Deadline oder andere Begründung erfinden;
- SEV1–SEV4 oder Page/Ticket-Zeitfenster als universelle Wahrheit setzen;
- häufig ignorierte Alerts einfach als normal akzeptieren;
- Ursache aus Alertbedingung ableiten;
- Runbookinhalt ungeprüft erfinden;
- produktive Alert-/Pager-Konfiguration ohne Autorisierung verändern.

## Ausgabe

```text
Condition / Symptom
Affected Objective / Impact
Signal / Evidence Source
Threshold Basis
Evaluation Window
Actionability
Routing / Severity [local / unknown]
Noise / Dedup / Suppression
Runbook / First Evidence
Verification Method
Change Gate
Missing Evidence
```

## Related

- `slo-design`
- `system-observability-design`
- `incident-response`
- `runbook`
- `reliability-review`

## Leitgedanke

> Ein Alert soll eine begründete Reaktion auslösen – nicht nur zeigen, dass irgendwo eine Zahl existiert.