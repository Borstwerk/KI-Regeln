---
name: analytical-data-modeling
description: Entwirft oder prüft analytische Datasets aus Consumerfragen, Grain, Schlüsseln, Measures, Dimensionen, Zeitbezug und Historisierung. Verwenden bei Warehouse-/Mart-/Semantic-Model-Fragen. Nicht als operatives Datenbankdesign oder automatische Star-Schema-/Data-Vault-Vorgabe verwenden.
---

# Analytical Data Modeling

## Ziel

Ein analytisches Datenmodell mit eindeutiger Bedeutung und belastbarem Grain entwerfen, ohne ein bestimmtes Schema-Pattern zu dogmatisieren.

## Eingaben

- Consumer-/Analysefragen;
- fachliche Begriffe und Invarianten;
- verfügbare Source-Daten;
- erwartete Measures / Dimensionen;
- Zeit-/Historisierungsbedarf;
- bekannte Query-/Performanceanforderungen;
- bestehende semantische Definitionen.

## Arbeitsweise

1. Consumerfragen und relevante fachliche Ereignisse/Entitäten klären.
2. Für jedes Dataset den Grain in einem Satz definieren.
3. Stabile Identität und Schlüssel festlegen.
4. Measures mit Einheit, Population, Aggregierbarkeit und Zeitbezug definieren.
5. Beschreibende Dimensionen/Attribute und Unknown-Semantik bestimmen.
6. Current-State- vs. Historisierungsbedarf entscheiden.
7. Änderungs-/Korrekturverhalten für historisierte Attribute/Ereignisse festhalten.
8. Consumer-Joinpfade und semantische Wiederverwendung prüfen.
9. Pattern und physische Form erst anhand lokaler Anforderungen wählen.
10. Contract, Quality und Lineage für veröffentlichte Modelle ergänzen.

## Patterns

Star/Snowflake, Wide Table, Data Vault, normalisierte Modelle oder Semantic Layer sind Optionen. Keine davon ist zentrale Pflicht.

## Stop-/Übergaberegeln

- operatives Persistenz-/Transaktionsmodell → `database-design`;
- reine Transformations-/Incrementallogik → `data-transformation-design`;
- fachliche Domainmodellierung der Anwendung → `domain-modeling`;
- physische Queryoptimierung → `query-performance`.

## Nicht tun

- Grain aus vorhandenem Primärschlüssel erraten;
- jede Analyticsanforderung in ein Star Schema zwingen;
- Measures ohne Aggregationssemantik definieren;
- Zeit-/Historisierung stillschweigend weglassen;
- `unknown`, `not applicable` und `missing` vermischen;
- operative Tabellen 1:1 als gutes Consumer-Modell annehmen.

## Ausgabe

```text
Consumer Questions
Dataset Grain
Keys / Identity
Measures [definition, unit, aggregation]
Dimensions / Attributes
Time / History Semantics
Unknown / Null Semantics
Relationships / Join Paths
Pattern Choice + Rationale
Contract / Quality / Lineage Handoffs
Open Questions
```

## Related

- `data-transformation-design`
- `data-contract-design`
- `data-quality-design`
- `data-lineage-analysis`
- `database-design`
- `domain-modeling`

## Leitgedanke

> Wenn der Grain nicht eindeutig ist, ist das Modell noch nicht eindeutig.