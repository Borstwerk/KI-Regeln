# Transformationen, Inkrementalität und Backfills

## Zweck

Transformationen ändern Struktur oder Bedeutung von Daten. Deshalb müssen sie über reine SQL-/Codekorrektheit hinaus fachlich nachvollziehbar, reproduzierbar und reprocessing-sicher sein.

## Transformationsvertrag

Für eine relevante Transformation klären:

- Inputdatasets und erwartete Version/Semantik;
- Output Grain und Schlüssel;
- Filter, Joins, Aggregationen und Ableitungen;
- Null-/Unknown-/Default-Semantik;
- Zeit- und Gültigkeitslogik;
- erwartete Invarianten und Quality Checks;
- Consumerwirkung.

## Full Refresh vs. inkrementell

Inkrementelle Verarbeitung ist eine Optimierung oder Betriebsentscheidung, keine andere fachliche Wahrheit.

Ein inkrementeller Pfad muss zum Full-Refresh-Ergebnis fachlich äquivalent sein oder die Abweichung ausdrücklich spezifizieren.

Zu prüfen sind insbesondere:

- Cursor/Watermark und Lookback;
- Updates und Deletes;
- Late-arriving Data;
- geänderte Dimensionen/Referenzdaten;
- Deduplizierung;
- Merge-/Overwrite-Semantik;
- State/Checkpoint;
- Verhalten nach Code- oder Schemaänderung.

## Backfills

Ein Backfill ist eine reale historische Datenänderung und kein normaler Retry.

Vor Ausführung mindestens:

```text
Grund / Zielzustand
Affected Window / Partitions
Source of Truth
Code-/Contract-Version
Write Mode
Idempotency / Duplicate Strategy
Consumer / Publish Impact
Resource / Source Impact
Validation / Reconciliation
Rollback / Recovery
Authorization Gate
```

Große Backfills bevorzugt in begrenzten, verifizierbaren Slices planen, wenn die lokale Plattform das sinnvoll erlaubt.

## Codeversion und historische Semantik

Bei Reprocessing muss klar sein, ob historische Daten mit:

- damaliger Logik;
- aktueller korrigierter Logik;
- einer explizit versionierten Übergangslogik

neu erzeugt werden sollen.

Ein heutiger Pipelinecode ist nicht automatisch die korrekte historische Semantik.

## Nicht tun

- erfolgreichen Jobstatus mit fachlich korrektem Output gleichsetzen;
- Incremental Models nur anhand geringerer Laufzeit bewerten;
- einen Backfill ungeprüft parallel zum normalen Publishpfad starten;
- Full Refresh als universelle Reparatur verwenden;
- historische Daten stillschweigend mit neuen Geschäftsregeln überschreiben;
- produktive Partitionen/Tabellen ohne lokales Gate löschen oder ersetzen.