# Skill-Handbuch – Datenbanken

## Zweck

Dieses Dokument erklärt die sieben Skills aus `Datenbanken/` in menschlich lesbarer Form.

Alle Skills sind engine-neutral. Konkrete SQL-, MongoDB-, Redis-, ORM- oder Plattformmechanismen kommen aus dem jeweiligen Projekt und der tatsächlich verwendeten Version.

## Schnellauswahl

| Ich möchte ... | Skill |
|---|---|
| ein Datenmodell entwerfen oder strukturell prüfen | `database-design` |
| eine konkrete Query auf Korrektheit und Sicherheit prüfen | `database-query-review` |
| eine langsame Query evidenzbasiert diagnostizieren | `query-performance` |
| eine Schemaänderung oder einen Backfill sicher planen | `schema-migration` |
| Race Conditions, Isolation oder Deadlocks prüfen | `transaction-review` |
| Connections, Backup, Restore oder Betrieb prüfen | `database-operations` |
| eine größere Datenbankänderung unabhängig freigabereif reviewen | `database-review` |

## `database-design`

**Nutzen:** Domäne, Invarianten und Zugriffsmuster in ein tragfähiges Datenmodell übersetzen.

**Nicht dafür:** einzelne langsame Query oder reine Migrationsausführung.

**Wichtig:** Bei bestehenden Systemen erst reales Schema / Migrationen / Introspection prüfen. Keine Tabellen oder Felder erfinden.

## `database-query-review`

**Nutzen:** Eine konkrete Query auf fachliche Trefferlogik, Tenant-/Scope-Grenzen, Parametrisierung und Write-Wirkung prüfen.

**Nicht dafür:** tiefe Performanceanalyse bei ausdrücklich langsamem Querypfad.

**Wichtig:** Review ist keine Ausführungsfreigabe.

## `query-performance`

**Nutzen:** Query-Latenz oder hohen Ressourcenverbrauch über Baseline, vorhandene Indizes und Execution-/Diagnose-Evidence untersuchen.

**Nicht dafür:** normale Query-Erstellung ohne Performanceproblem.

**Wichtig:** Kein reflexhafter Indexbau; danach erneut messen.

## `schema-migration`

**Nutzen:** Den Übergang vom realen alten zum neuen Datenzustand inklusive Bestandsdaten, Locks, Backfill, Rollout und Recovery planen.

**Nicht dafür:** Greenfield-Datenmodell ohne bestehenden Zustand.

**Wichtig:** Destruktive oder reale Produktionsmigrationen brauchen ein passendes Human Gate.

## `transaction-review`

**Nutzen:** Fachliche Invarianten gegen konkurrierende Zugriffe, Isolation, Locking, Retry und Idempotenz prüfen.

**Nicht dafür:** Performanceanalyse einer normalen einzelnen Query.

**Wichtig:** Konkrete Isolationseigenschaften immer gegen Engine und Version verifizieren.

## `database-operations`

**Nutzen:** Connections, Pooling, Ressourcen, Backup, Restore, Recovery und Maintenance sicher planen oder diagnostizieren.

**Nicht dafür:** reine Query-Optimierung.

**Wichtig:** Read-only Diagnose bevorzugen; Restore über bestehende Daten ist eine harte Gate-Aktion.

## `database-review`

**Nutzen:** Unabhängiger Gesamtcheck größerer Datenbankdesigns oder Änderungen.

Prüft insbesondere:

- Source of Truth;
- Modell / Access Patterns;
- Integrität;
- Query-/Security-Aspekte;
- Performance-Evidence;
- Concurrency;
- Migration;
- Betrieb / Recovery;
- Gate-Status.

**Nicht dafür:** ungefragtes Redesign oder einzelne kleine Queryfrage.

## Typischer Workflow

Für eine größere Änderung:

```text
database-design
→ schema-migration
→ transaction-review (wenn nötig)
→ database-query-review
→ query-performance (wenn nötig)
→ database-operations (wenn nötig)
→ database-review
→ Human Gate
→ lokale Ausführung
→ Post-Change-Verifikation
```

Siehe `../Workflows/Datenbank-Aenderung.md`.

## Reifegrad

Alle sieben Skills starten mit:

```text
maturity: experimental
eval_coverage: partial
```

Das bedeutet: Quellenbasis und erste Evals sind vorhanden, aber reale Nutzung und Regressionserfahrung müssen erst wachsen.

## Leitgedanke

> Datenbank-Skills sollen nicht schneller SQL produzieren, sondern Datenänderungen nachvollziehbarer, sicherer und belastbarer machen.