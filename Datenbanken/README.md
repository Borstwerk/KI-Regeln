# Datenbanken

Dieser Bereich beschreibt allgemeine, datenbankneutrale Arbeitsweisen für Entwurf, Änderung, Abfrage, Performance, Sicherheit und Betrieb von Datenbanken.

Er ist **nicht** auf SQL, PostgreSQL, MongoDB, Redis, Prisma oder eine andere konkrete Engine festgelegt.

## Grundprinzip

> Das reale Datenmodell, die tatsächlichen Zugriffsmuster und die verwendete Datenbankversion sind Quellen der Wahrheit – nicht plausible Annahmen des Agenten.

## Scope

`Datenbanken/` behandelt den Zustand und das Verhalten **innerhalb eines operativen Datenspeichers**:

- Datenmodellierung und Zugriffsmuster;
- Schema, Constraints und Datenintegrität;
- Abfragen und Query-Sicherheit;
- Indizes und Ausführungspläne;
- Transaktionen, Isolation und Concurrency;
- Schemaänderungen, Backfills und Rollback;
- Connections, Pooling und Ressourcen;
- Zugriffsschutz und Datenbanksicherheit;
- Backup, Restore und Recovery;
- Monitoring und Diagnose.

Nicht primär hierher gehören:

- ETL / ELT;
- laufende CDC und Replikationspipelines zwischen Systemen;
- Data-Lake-/Warehouse-Pipelines;
- Orchestrierung von Datenflüssen zwischen mehreren Systemen.

Diese Themen gehören in `../Data-Engineering/`. Dort werden Source-to-Consumer-Datenflüsse, Ingestion/CDC/Replay, Transformationen, analytische Datenmodelle, Datenqualität, Data Contracts, Lineage und Orchestrierung behandelt.

## Engine-neutral, aber nicht engine-blind

Allgemeine Regeln beschreiben das **Warum und den Prüfprozess**.

Konkrete Projekte müssen zusätzlich die reale Dokumentation ihrer Engine, ihres Drivers, ORM-/ODM-Tools und ihrer verwendeten Version beachten.

Beispiel:

```text
allgemein:
Execution Path messen und Engpass nachweisen

konkret:
Postgres → EXPLAIN / EXPLAIN ANALYZE
MongoDB  → explain()
Redis    → Slow Log / Commandstats / Latency
```

Engine-spezifische Mechanismen werden nicht zu universellen Regeln erklärt.

## Risikoklassen

Datenbankaktionen werden mindestens in vier Klassen gedacht:

```text
READ
→ Schema, Statistiken, Indizes, sichere Diagnose

WRITE
→ gezielte Daten- oder Metadatenänderung

MIGRATION
→ Schemaänderung, Backfill, Constraint-/Indexänderung

DESTRUCTIVE / RECOVERY
→ DROP, TRUNCATE, Massenlöschung, Reset, Restore über Daten
```

Mit steigendem Risiko steigen Evidence-, Preview- und Human-Gate-Anforderungen.

## Skills

- `database-design`
- `database-query-review`
- `query-performance`
- `schema-migration`
- `transaction-review`
- `database-operations`
- `database-review`

## Leitgedanken

> Zugriffsmuster formen das Datenmodell.

> Korrektheit, Performance und Sicherheit sind getrennte Prüfachsen.

> Eine Migration ist erst dann gut, wenn auch Bestandsdaten, Rollout, Rückwärtskompatibilität und Recovery bedacht wurden.

> Datenbankdiagnose beginnt mit Beobachtung – nicht mit reflexhaftem Tuning.