---
name: data-contract-design
description: Entwirft oder prüft Verträge für veröffentlichte Datasets mit Grain, Schema, Semantik, Quality, Freshness/Serviceeigenschaften, Ownership und Evolution. Verwenden bei Tabellen-/View-/File-/Topic-Contracts für Datenprodukte. Nicht als API-/Event-Message-Contract-Skill oder zur Erzwingung eines bestimmten Contractformats verwenden.
---

# Data Contract Design

## Ziel

Explizit machen, was Consumer von einem veröffentlichten Dataset erwarten dürfen und wie diese Zusage sicher evolviert.

## Eingaben

- Dataset-Zweck und Consumer;
- Grain und Schlüssel;
- Felder / Typen / Semantik;
- Quality-/Freshness-Anforderungen;
- Ownership;
- bekannte Consumerabhängigkeiten;
- Retention-/Privacy-/Lifecycle-Regeln;
- bestehende Contractversion, falls vorhanden.

## Arbeitsweise

1. Datasetidentität, Zweck und Consumer klären.
2. Grain und Schlüssel explizit definieren.
3. Schema mit Feldsemantik, Null-/Unknown-Verhalten und Einheiten beschreiben.
4. Quality- und Servicezusagen nur aus lokalen Requirements übernehmen.
5. Ownership und sensitive/classified Felder dokumentieren.
6. maschinenlesbares Format nur wählen, wenn es lokal passt.
7. Änderungen auf strukturelle, semantische und historische Compatibility prüfen.
8. bekannte Consumer und Lineage für Impact heranziehen.
9. Reprocessing-/Backfill-/Dual-Run-Bedarf bestimmen.
10. Breaking/rollout-sensitive Änderungen an Migration und lokales Gate übergeben.

## Verdicts

- `COMPATIBLE`
- `ROLLOUT-SENSITIVE`
- `BREAKING`
- `UNVERIFIED`

## Stop-/Übergaberegeln

- API-/Request-/Responsevertrag → `interface-design` / `http-api-design`;
- einzelner Event-/Messagevertrag → `event-contract-design`;
- Quality-Regeldesign → `data-quality-design`;
- Lineage-/Downstreamanalyse → `data-lineage-analysis`;
- produktive Contract-/Datasetänderung → lokales Gate.

## Nicht tun

- Data Contract mit DDL gleichsetzen;
- ODCS/dbt/anderes Format zentral erzwingen;
- additive Spalte automatisch als risikofrei bewerten;
- semantische Änderung nur nach Datentyp beurteilen;
- SLA/Freshnesswerte erfinden;
- unbekannte Consumer als nicht existent behandeln.

## Ausgabe

```text
Dataset Identity / Purpose
Consumers / Ownership
Grain / Keys
Schema / Field Semantics
Quality / Service Expectations
Sensitive / Lifecycle Rules
Machine-readable Representation [optional]
Evolution / Compatibility
Consumer / Lineage Impact
Migration / Reprocessing
Verdict / Gates / Missing Evidence
```

## Related

- `data-quality-design`
- `data-lineage-analysis`
- `analytical-data-modeling`
- `data-transformation-design`
- `contract-change-review`
- `event-contract-design`

## Leitgedanke

> Ein Datenvertrag schützt Bedeutung und Consumererwartung, nicht nur Spaltennamen.