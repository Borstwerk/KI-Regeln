---
name: data-quality-design
description: Entwirft oder prüft datenfachliche Quality- und Reconciliation-Evidence aus Consumerinvarianten, Contracts, Freshness, Completeness, Validity, Uniqueness und bekannten Failure Modes. Verwenden bei Data-Quality-, Freshness- oder Reconciliation-Fragen. Nicht zur Erfindung universeller Thresholds oder als allgemeiner Software-Testskill verwenden.
---

# Data Quality Design

## Ziel

Quality-Evidence so definieren, dass sie konkrete Fehlermöglichkeiten eines Datasets erkennt und die Consumerfrage statt nur die Pipelineausführung schützt.

## Eingaben

- Dataset / Grain / Contract;
- Consumer-/Businessinvarianten;
- Source-Zusagen;
- bekannte Failure Modes;
- Baselines / historische Verteilungen, falls vorhanden;
- Freshness-/Publishanforderungen;
- sensible Daten / Debuggrenzen.

## Arbeitsweise

1. Consumerzweck und kritische Dateninvarianten bestimmen.
2. Passende Qualitätsachsen auswählen; keine Pflichtliste erzwingen.
3. Freshness mit dem richtigen Zeitbezug definieren.
4. Struktur-, Completeness-, Validity-, Uniqueness- und fachliche Regeln nur mit Begründung festlegen.
5. Wo möglich Reconciliation gegen geeignete unabhängige oder vorgelagerte Evidence definieren.
6. Thresholds/Toleranzen aus Requirement, Baseline oder Risiko ableiten; sonst als unknown markieren.
7. Checkpunkt im Datenfluss bewusst wählen: ingest, transform, pre-publish, post-publish oder mehrere.
8. Verhalten bei Failure nach lokaler Publish-/Incidentpolicy beschreiben.
9. Coverage und Blind Spots der Checks dokumentieren.
10. Sensitive Samples minimieren.

## Freshness

Event Time, Source Update Time, Ingestion Time und Publish Time nicht vermischen. `MAX(timestamp)` ist nur dann eine brauchbare Evidence, wenn es zur Vollständigkeitsfrage passt.

## Stop-/Übergaberegeln

- allgemeine Teststrategie → `test-strategy` / `test-design`;
- Alert-/Pagingregeln → `alert-design`;
- Datencontract → `data-contract-design`;
- laufender Datenincident → Incident-/Fachprozess.

## Nicht tun

- `row_count > 0` als generische Freigabe verwenden;
- 0 % Nulls, 100 % Uniqueness oder feste Anomalieschwellen erfinden;
- Anomaly Detection mit Accuracy gleichsetzen;
- Sourcefehler durch Targetchecks wegdefinieren;
- grüne Checks als vollständigen Consumerkorrektheitsbeweis ausgeben;
- komplette PII-/Secret-Samples in Reports kopieren.

## Ausgabe

```text
Dataset / Consumer Risk
Quality Dimensions
Rules + Rationale
Freshness Semantics
Reconciliation
Threshold Basis
Execution Point
Failure / Publish Policy [local / unknown]
Coverage / Blind Spots
Sensitive-Data Handling
Missing Evidence
```

## Related

- `data-contract-design`
- `data-pipeline-design`
- `data-transformation-design`
- `data-engineering-review`
- `test-design`
- `alert-design`

## Leitgedanke

> Ein Data-Quality-Check ist wertvoll, wenn er einen relevanten falschen Datenzustand zuverlässig sichtbar macht.