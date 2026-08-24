---
name: data-ingestion-design
description: Entwirft oder prüft Ingestion aus Dateien, APIs, Snapshots, CDC oder Streams mit Identität, Änderungs-/Delete-Semantik, Cursor/Offsets, Ordering, Duplikaten, Late Data und Replay. Verwenden bei Source-Anbindung und Capture-Fragen. Nicht als Source-DB-Tuning-, Event-Contract- oder produktiver Offset-/Replay-Skill verwenden.
---

# Data Ingestion Design

## Ziel

Quelldaten so erfassen, dass Vollständigkeit, Änderungen und Wiederholung unter den realen Source-Zusagen kontrollierbar bleiben.

## Eingaben

- Source of Truth und Owner;
- Source-Vertrag / Schema / API / Log;
- Änderungsmuster einschließlich Deletes;
- Schlüssel / Eventidentität;
- Volumen / Rate / Quotas;
- Retention / Replayfenster;
- erwartete Freshness;
- Target-/Landing-Semantik.

## Arbeitsweise

1. Autorität und reale Source-Capabilities prüfen.
2. Snapshot, inkrementellen Pull, CDC, Event-Consumption oder Arrival-Modell bewusst wählen.
3. Eindeutige Identität und Version/Sequence bestimmen.
4. Inserts, Updates, Deletes und Korrekturen modellieren.
5. Cursor/Offset/Checkpoint und dessen Recoverysemantik definieren.
6. Ordering-Garantien nur aus Source-/Transport-Evidence übernehmen.
7. Duplikate, Gaps und Late Data behandeln.
8. Ende-zu-Ende-Delivery-/Idempotenz-Semantik mit Sink abgleichen.
9. Replaypfad und Source-Retention prüfen.
10. Source Impact, Rate Limits, Security und lokale Execution Gates dokumentieren.

## Guarantees

`at-most-once`, `at-least-once` und `exactly-once` nicht als Reifestufen behandeln. Exactly-once nur behaupten, wenn die relevante Ende-zu-Ende-Semantik nachweisbar ist.

## Stop-/Übergaberegeln

- operativer Message-/Eventvertrag → `event-contract-design`;
- DB-interne Replikation/Enginebetrieb → Datenbanken;
- Zieltransformation → `data-transformation-design`;
- Scheduler-/Dependencydesign → `data-orchestration-design`;
- reale Offset-/Cursoränderung oder Replay → lokales Gate.

## Nicht tun

- `updated_at` ungeprüft als verlustfreien Cursor einsetzen;
- Retries mit genau-einmaliger Verarbeitung gleichsetzen;
- CDC automatisch als vollständige Audit-Historie behandeln;
- Delete-Semantik ignorieren;
- Source Event Time und Ingestion Time vermischen;
- produktive Offsets oder Daten ungefragt zurücksetzen.

## Ausgabe

```text
Source / Authority
Capture Mode
Identity / Version / Ordering
Insert / Update / Delete Semantics
Cursor / Offset / Checkpoint
Delivery / Idempotency
Late Data / Gap Handling
Replay / Retention
Source Impact / Quotas
Security / Gates
Missing Evidence
```

## Related

- `data-pipeline-design`
- `data-transformation-design`
- `data-orchestration-design`
- `event-contract-design`
- `data-quality-design`

## Leitgedanke

> Ingestion ist erst robust, wenn wir wissen, was bei Wiederholung, Lücke, Delete und verspäteter Ankunft passiert.