# Workflow – Datenbankänderung

## Zweck

Dieser Workflow verbindet die Datenbank-Skills für Änderungen an einem bestehenden operativen Datenspeicher.

Er ist engine-neutral. Konkrete Befehle und Guarantees kommen aus dem jeweiligen Projekt und der verwendeten Engine-Version.

## Ablauf

```text
Anforderung / Invariante
        ↓
database-design
        ↓
Zielmodell + Access Patterns
        ↓
schema-migration
        ↓
Migration / Backfill / Rollout
        ↓
transaction-review
(wenn Concurrency betroffen)
        ↓
database-query-review
        ↓
query-performance
(nur bei Performancebedarf / Evidence)
        ↓
database-operations
(wenn Betrieb / Backup / Restore betroffen)
        ↓
database-review
        ↓
Human Gate
        ↓
Ausführung im lokalen Projektprozess
        ↓
Post-Change-Verifikation
```

Nicht jeder Schritt ist für jede Änderung nötig.

## Minimaler Scope vor realer Änderung

- tatsächliche Zielumgebung;
- reale Engine und Version;
- aktuelles Schema;
- gewünschter Zielzustand;
- betroffene Daten;
- relevante App-/Query-Pfade;
- Risiko- und Gate-Klasse.

## Risk Gates

```text
READ
→ Diagnose innerhalb freigegebenen Scopes

WRITE
→ konkrete Operation und Wirkung vor Freigabe

MIGRATION
→ Diff + Daten-/Lock-/Rollback-Evidence + Human Gate

DESTRUCTIVE / RECOVERY
→ hartes Gate mit Zielidentität und Folgen
```

## Evidence Bundle

Vor Freigabe einer nichttrivialen Änderung möglichst:

```text
Ausgangsschema
Zielmodell
Migration Diff
Bestandsdatenprüfung
Concurrency-Bewertung
Query-/Performance-Evidence
Security-Auswirkungen
Rollout / Rollback / Forward Fix
Tests / Staging
Post-Change-Checks
```

## Abgrenzung

Laufende ETL-/CDC-/Replikationspipelines zwischen Systemen sind kein Bestandteil dieses Workflows; sie gehören in einen späteren Data-Engineering-Workflow.

## Leitgedanke

> Eine Datenbankänderung ist ein kontrollierter Zustandsübergang, kein einzelner Befehl.