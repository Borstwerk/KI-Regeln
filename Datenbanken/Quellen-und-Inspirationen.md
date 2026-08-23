# Quellen und Inspirationen – Datenbanken

## Zweck

Diese Datei dokumentiert öffentliche Quellen und Hersteller-Skills, die beim Aufbau des allgemeinen Bereichs `Datenbanken/` berücksichtigt wurden.

Externe Quellen sind Inspiration und Vergleichsbasis. Engine-spezifische Regeln werden nicht ungeprüft zu allgemeinen Regeln erhoben.

Letzte inhaltliche Prüfung: **2026-08-23**.

## Supabase – Postgres Best Practices

Quelle:

`https://github.com/supabase/agent-skills/blob/main/skills/supabase-postgres-best-practices/SKILL.md`

Beobachteter Stand:

- Branch: `main`
- Blob SHA: `6400792389dfcc82c81953054e546bd72ebcd259`
- ausgewiesene Version: `1.1.1`

Nützliche Konzepte:

- Query Performance, Connection Management und Security als hochpriorisierte Achsen;
- Schema Design, Concurrency/Locking, Access Patterns und Monitoring getrennt betrachten;
- detaillierte Regeln per Progressive Disclosure statt Monster-Skill;
- Performanceempfehlungen mit Query-Plan-/Mess-Evidence verbinden.

Postgres-spezifische Mechanismen wie RLS oder konkrete Indextypen werden nicht verallgemeinert.

## Neon – Postgres Best Practices

Quelle:

`https://github.com/neondatabase/postgres-skills/blob/main/skills/postgres-best-practices/SKILL.md`

Beobachteter Stand:

- Branch: `main`
- Blob SHA: `43f3468765949e3db85a3782d90d4826b6c585bd`

Nützliche Konzepte:

- Schema Design, Indexing, Query Optimization und Migration als getrennte Arbeitsgebiete;
- Referenzen nur nach Bedarf laden.

## MongoDB – Schema Design

Quelle:

`https://github.com/mongodb/agent-skills/blob/main/plugins/mongodb/skills/mongodb-schema-design/SKILL.md`

Beobachteter Stand:

- Branch: `main`
- Blob SHA: `e2237d15ead78ce33a4753ca8dc8e6e0bba854cf`
- ausgewiesene Version: `1.0.0`

Nützliche Konzepte:

- Schema anhand realer Read-/Write-Workloads statt relationalem Dogma gestalten;
- Access Patterns vor Schemaempfehlung analysieren;
- reale Query Stats, Slow Logs, Code oder Nutzerwissen als Evidence kombinieren;
- Schema Validation, Lifecycle und Schema Versioning;
- read-only Diagnose von schreibenden/destruktiven Aktionen trennen;
- vor realen Writes explizite Freigabe verlangen.

MongoDB-spezifische Regeln wie Embed-vs-Reference oder Dokumentgrößenlimits bleiben lokale Engine-Regeln.

## MongoDB – Query Optimizer

Quelle:

`https://github.com/mongodb/agent-skills/blob/main/plugins/mongodb/skills/mongodb-query-optimizer/SKILL.md`

Beobachteter Stand:

- Branch: `main`
- Blob SHA: `c71f2f5e9afd8b6cd73380169e0ff5c3f9402944`
- ausgewiesene Version: `1.0.0`

Nützliche Konzepte:

- Performance-Skill nur bei tatsächlichem Performanceintent triggern;
- vorhandene Indizes, `explain` und reale Query-/Slow-Log-Evidence zuerst untersuchen;
- Optimierungen nach Impact priorisieren;
- keine starken Performancebehauptungen ohne Evidence;
- Indexerstellung nicht automatisch als Folge der Diagnose ausführen.

## Redis – Core / Connections / Security

Quellen:

- `https://github.com/redis/agent-skills/blob/main/skills/redis-core/SKILL.md`
- `https://github.com/redis/agent-skills/blob/main/skills/redis-connections/SKILL.md`
- `https://github.com/redis/agent-skills/blob/main/skills/redis-security/SKILL.md`

Beobachtete Blob-SHAs:

- Core: `a62be86377ad672f5f9f2301a492cc4ee726d3cc`
- Connections: `53f367a9a4ed6a4bf9c3c29a441dcfa1ee91a114`
- Security: `661ba11f06c9a31203dfe6b828bd2c714d0a258e`

Nützliche Konzepte:

- Datenstruktur passend zum Zugriffsmuster wählen;
- Connection Pooling/Multiplexing, Batching und Timeouts als eigene Betriebsachse;
- Least Privilege und getrennte Credentials;
- Datenmodell-, Connection- und Securityfragen nicht in einen einzigen Skill pressen.

Redis-spezifische Datentypen und ACL-Syntax werden nicht als allgemeine Datenbankregeln übernommen.

## Prisma – Skills README

Quelle:

`https://github.com/prisma/prisma/blob/main/skills/README.md`

Beobachteter Stand:

- Branch: `main`
- Blob SHA: `889bb5e1cf410c7751b51fc6c529f5fe3d44aec1`

Nützliche Konzepte:

- Tool-/ORM-Skills an die tatsächlich verwendete Runtime-/CLI-Version koppeln;
- Capability Gaps ausdrücklich benennen statt plausible APIs zu erfinden;
- project-local statt globale Version als Source of Truth verwenden.

Daraus wurde die allgemeine Regel abgeleitet, Engine-/Driver-/ORM-Verhalten gegen die reale Projektversion zu prüfen.

## PostgreSQL Dokumentation

Relevante lebende Primärquelle:

`https://www.postgresql.org/docs/current/`

Besonders relevant für allgemeine Ableitungen:

- Transaktionen und Isolation;
- Locking;
- `ALTER TABLE` und DDL-Wirkung;
- `EXPLAIN` / `EXPLAIN ANALYZE`.

Die Dokumentation dient als Postgres-Primärquelle, nicht als allgemeiner Datenbankstandard.

## Prisma Migrate Dokumentation

Relevante lebende Quelle:

`https://www.prisma.io/docs/orm/prisma-migrate`

Nützliche Konzepte:

- Entwicklungs- und Produktionsmigrationen getrennt behandeln;
- Migrationen versionieren und kontrolliert deployen;
- reale Daten- und Rolloutfolgen berücksichtigen.

## Eigene Synthese

Aus dem Vergleich sehr unterschiedlicher Systeme wurde dieser engineübergreifende Kern abgeleitet:

```text
Domäne + Workload
→ Datenmodell
→ Integrität
→ Query-/Access Pattern
→ physische Optimierung
→ Concurrency
→ Migration
→ Ressourcen
→ Security
→ Betrieb / Recovery / Diagnose
```

Ebenso die Scope-Grenze:

```text
Datenbanken
= Zustand und Verhalten innerhalb eines operativen Datenspeichers

Data Engineering
= systematische Bewegung, Replikation, Transformation und Orchestrierung zwischen Systemen
```

## Übernahmekriterien

Eine externe Datenbankregel wird nur zentralisiert, wenn sie:

1. über mehrere Datenbankmodelle sinnvoll abstrahierbar ist;
2. Korrektheit, Sicherheit, Performance oder Recovery verbessert;
3. nicht von einem einzelnen Engine-Feature abhängig ist;
4. ihre enginespezifischen Voraussetzungen klar erkennen lässt;
5. reale Evidence vor plausible Modellannahmen stellt.

## Leitgedanke

> Herstellerwissen liefert konkrete Mechanismen. Das zentrale Repository abstrahiert daraus belastbare Arbeitsprinzipien.