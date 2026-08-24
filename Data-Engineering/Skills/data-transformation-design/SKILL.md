---
name: data-transformation-design
description: Entwirft oder prüft Transformationen mit Input-/Output-Grain, Joins, Filter, Aggregationen, Zeit-/Nullsemantik, inkrementeller Verarbeitung und Backfillfähigkeit. Verwenden bei ETL-/ELT-Logik und Materialisierungsfragen. Nicht als allgemeiner SQL-Optimierungs-, Analytics-Modellierungs- oder ungefragter Backfill-Ausführungsskill verwenden.
---

# Data Transformation Design

## Ziel

Transformationslogik so definieren, dass Bedeutung, inkrementelles Verhalten und historische Reproduzierbarkeit nachvollziehbar bleiben.

## Eingaben

- Inputdatasets / Contracts;
- gewünschter Output und Consumer;
- Input-/Output-Grain;
- Schlüssel und Zeitsemantik;
- Änderungs-/Delete-/Late-Data-Verhalten;
- bekannte Quality-Invarianten;
- bestehende Incremental-/Materialization-Mechanik.

## Arbeitsweise

1. Inputs und deren Semantik verifizieren.
2. Output-Grain und Schlüssel vor Implementierungsdetails festhalten.
3. Filter, Joins, Aggregationen, Defaults und Ableitungen fachlich beschreiben.
4. Null/Unknown/Not-applicable explizit behandeln.
5. Zeit-/Gültigkeitslogik bestimmen.
6. Full-Refresh-Semantik als Referenz oder ausdrücklich abweichendes Ziel definieren.
7. Inkrementellen Pfad auf Updates, Deletes, Late Data, Deduplizierung und Referenzänderungen prüfen.
8. Quality-/Reconciliation-Evidence für den Output definieren.
9. Backfill-/Reprocessingsemantik inklusive Code-/Contract-Version beschreiben.
10. Publish-/Consumerwirkung und lokale Gates dokumentieren.

## Inkrementalität

Ein inkrementeller Lauf ist nicht automatisch korrekt, nur weil neue Zeilen entstehen. Entscheidend ist die fachliche Äquivalenz beziehungsweise eine explizit dokumentierte Abweichung zum gewünschten Gesamtzustand.

## Stop-/Übergaberegeln

- Grain/Measures/Historisierung des analytischen Zielmodells → `analytical-data-modeling`;
- Query-Performance einer DB → `query-performance`;
- Scheduler-/Backfill-Orchestrierung → `data-orchestration-design`;
- reale produktive Reprocessingaktion → lokales Gate.

## Nicht tun

- SQL-Kompilierung mit fachlicher Korrektheit gleichsetzen;
- Full Refresh als universelle Reparatur empfehlen;
- historische Daten still mit aktueller Logik neu deuten;
- Deletes oder Late Data im Incrementalpfad ignorieren;
- Backfill und Tageslauf ungeprüft als identisch behandeln;
- produktive Tabellen/Partitionen ungefragt überschreiben.

## Ausgabe

```text
Inputs / Contracts
Output Grain / Keys
Transformation Semantics
Join / Filter / Aggregate Logic
Null / Time / History Semantics
Full vs Incremental Behavior
Late Data / Deletes / Dedupe
Quality / Reconciliation
Backfill / Reprocessing
Publish / Consumer Impact
Gates / Missing Evidence
```

## Related

- `analytical-data-modeling`
- `data-quality-design`
- `data-orchestration-design`
- `data-contract-design`
- `query-performance`

## Leitgedanke

> Transformation ist eine Bedeutungsänderung mit Code – nicht bloß ein SQL-Statement.