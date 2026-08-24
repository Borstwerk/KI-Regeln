# Ingestion, CDC und Replay

## Zweck

Ingestion übernimmt Daten aus einer Quelle so, dass Vollständigkeit, Reihenfolge, Änderungen und spätere Wiederholbarkeit bewusst behandelt werden.

## Capture-Modi

Mögliche Formen sind unter anderem:

- vollständiger Snapshot;
- inkrementeller Pull nach Cursor oder Watermark;
- Change Data Capture;
- Event-/Message-Consumption;
- Datei-/Object-Arrival;
- API-basierter Abruf.

Keiner dieser Modi ist universell überlegen.

## Vor dem Entwurf klären

- Was kennzeichnet einen Datensatz oder ein Event eindeutig?
- Wie werden Inserts, Updates und Deletes sichtbar?
- Gibt es stabile Sequenzen, Cursor, Offsets oder Änderungszeitpunkte?
- Kann die Quelle historische Daten erneut liefern?
- Wie weit reicht Retention oder Replayfähigkeit?
- Welche Ordering-Zusage existiert tatsächlich?
- Was passiert bei Duplikaten, Lücken und verspäteter Ankunft?
- Welche Rate-/Quota-/Source-Impact-Grenzen gelten?

## Delivery und Idempotenz

`at-most-once`, `at-least-once` und `exactly-once` sind keine Qualitätsstufen, sondern unterschiedliche Verarbeitungszusagen mit Voraussetzungen und Trade-offs.

Exactly-once darf nicht aus Toolnamen oder Marketingtext abgeleitet werden. Entscheidend ist die Ende-zu-Ende-Semantik inklusive Source, Processing und Sink.

Bei möglicher Wiederholung braucht der Zielpfad eine geeignete Strategie, zum Beispiel:

- idempotente Upserts;
- dedizierte Event-/Business-Keys;
- Merge mit eindeutiger Versionslogik;
- append-only plus nachgelagerte Deduplizierung;
- transaktionale oder checkpointbasierte Mechanismen, wenn lokal unterstützt.

## CDC

Bei CDC zusätzlich beachten:

- Initial Snapshot und Übergang in laufende Changes;
- Position/Offset des Übergangs;
- Delete-/Tombstone-Semantik;
- DDL-/Schemaänderungen;
- Transaktionsgrenzen und Ordering;
- Retention des Change Logs;
- Recovery nach längerer Unterbrechung.

## Replay

Replayfähigkeit ist eine Designentscheidung.

Ein Replayplan muss mindestens beantworten:

- welche Source erneut gelesen wird;
- welches Zeit-/Offset-/Partitionsfenster betroffen ist;
- ob Zielwrites append, merge oder replace sind;
- wie Duplikate und bereits publizierte Ergebnisse behandelt werden;
- welche Consumer währenddessen geschützt oder informiert werden müssen;
- wie Reconciliation erfolgt;
- welches lokale Gate reale Wiederverarbeitung freigibt.

## Nicht tun

- `updated_at` ohne Prüfung als sicheren Cursor voraussetzen;
- Source-Timestamps mit Processing Time verwechseln;
- Retries als Beweis für verlustfreie Verarbeitung ansehen;
- CDC automatisch mit vollständiger Historie gleichsetzen;
- Replay starten, bevor Write-Semantik und Zielzustand geklärt sind;
- produktive Offsets, Cursor oder Daten ungefragt verändern.