---
name: data-lineage-analysis
description: Analysiert oder prüft Herkunft und Abhängigkeiten von Datasets über Sources, Jobs, Runs, Outputs und Consumer hinweg und nutzt Lineage für Impact Analysis. Verwenden bei Provenance-, Downstream-/Upstream- und Change-Impact-Fragen. Nicht als Diagramm-Selbstzweck oder zur Behauptung vollständiger Runtime-Lineage aus statischem Code verwenden.
---

# Data Lineage Analysis

## Ziel

Nachvollziehbar machen, wie Daten entstehen und welche bekannten Auswirkungen eine Quelle, Transformation oder Änderung auf Downstreams hat.

## Eingaben

- betroffene Datasets/Felder;
- Pipeline-/Jobdefinitionen;
- Runtime-/Run-Metadaten, falls vorhanden;
- Contracts / Catalog / Consumerwissen;
- Code-/Versionsevidence;
- gewünschte Frage: Herkunft, Impact, Incident oder Audit.

## Arbeitsweise

1. Analysefrage und benötigte Granularität bestimmen.
2. Dataset-, Job-/Transformation- und gegebenenfalls Run-Entitäten identifizieren.
3. Design Lineage von Runtime Lineage trennen.
4. Upstream- und Downstreamkanten aus geeigneter Evidence sammeln.
5. Herkunft/Transformation bis zum benötigten Punkt nachvollziehen.
6. bei Change Impact bekannte Consumer, Materialisierungen und Contractabhängigkeiten erfassen.
7. Lineage-Lücken und unbekannte Downstreams explizit markieren.
8. Code-/Contract-/Run-Versionen bei Provenancefragen verbinden.
9. sensible Metadaten/Payloads minimieren.
10. Ergebnis nach `CONFIRMED`, `LIKELY`, `UNVERIFIED` oder `CONFLICTING` kennzeichnen, wo sinnvoll.

## Granularität

Dataset-/Table-Level genügt oft für Impact. Column-Level ist sinnvoll, wenn die konkrete Frage es benötigt. Mehr Metadaten ohne Entscheidungsnutzen sind kein Qualitätsgewinn.

## Stop-/Übergaberegeln

- Contractänderung → `data-contract-design`;
- technische Root-Cause-Diagnose → `diagnose` / Fachdomäne;
- Runtime-Systemobservability → `system-observability-design`;
- Consumer-/API-Vertrag → Schnittstellen und Verträge.

## Nicht tun

- statische DAGs als vollständige Runtime-Evidence ausgeben;
- fehlende Lineage als Beweis für fehlende Downstreams behandeln;
- Column-Level-Lineage überall erzwingen;
- Herkunft aus Namensähnlichkeit erraten;
- komplette produktive Payloads für Lineage persistieren;
- OpenLineage oder anderes Tool als Pflichtstack setzen.

## Ausgabe

```text
Question / Scope
Entity Granularity
Upstream Lineage
Transformations / Jobs
Runtime Runs / Versions [if available]
Downstream / Consumers
Evidence Status
Lineage Gaps
Change / Incident Impact
Required Handoffs
```

## Related

- `data-contract-design`
- `data-pipeline-design`
- `data-engineering-review`
- `system-observability-design`
- `knowledge-query`

## Leitgedanke

> Lineage beantwortet Herkunft und Wirkung mit Evidence – nicht mit einem vermuteten Pfeildiagramm.