---
name: schema-migration
description: Plant und prüft Schemaänderungen, Backfills, Rollout und Recovery für bestehende Datenbanken. Verwenden bei ALTER-/Schemaänderungen, Constraint-Verschärfung, Renames, Typänderungen, großen Backfills oder destruktiven Änderungen. Nicht für reine neue Modellierung ohne Bestandsmigration verwenden.
compatibility: Benötigt für belastbare Planung das reale Ausgangsschema, die konkrete Engine/Version und möglichst Datenvolumen/Deployment-Kontext. Reale Migrationen benötigen lokale Write-/Human-Gates.
---

# Schema Migration

## Ziel

Einen sicheren Weg vom realen Ausgangszustand zum gewünschten Zielzustand planen und verifizieren.

## Workflow

1. Ausgangsschema und Zielzustand verifizieren.
2. Migration Diff und betroffene Daten identifizieren.
3. Datenverlust-, Lock-, Rewrite- und Downtime-Risiken prüfen.
4. Kompatibilität mit alter/neuer App-Version prüfen.
5. Bestandsdaten gegen neue Constraints validieren.
6. Bei Bedarf Expand–Migrate–Contract planen.
7. Backfill auf Batch, Idempotenz, Retry, Last und Gleichzeitigkeit prüfen.
8. Rollback oder Forward-Fix festlegen.
9. Test-/Staging-Evidence erzeugen.
10. Vor realem Deploy Human Gate verlangen.
11. Post-Migration-Checks ausführen.

## Risikoregeln

- DROP/TRUNCATE/irreversible Konvertierung = hartes Gate.
- Große Datenänderung nicht als Nebeneffekt einer Schemaänderung verstecken.
- Migrationstool-Befehl nur gegen echte verwendete Version formulieren.
- Generierte Migration nie automatisch als sicher deklarieren.
- `go ahead` für eine konkrete Migration erlaubt keine zusätzlichen destruktiven Reparaturen außerhalb des gezeigten Scopes.

## Output

```text
Ausgangszustand
Zielzustand
Migration Diff
Bestandsdatenrisiko
Lock-/Downtime-Risiko
Rolloutplan
Backfillplan
Rollback / Forward Fix
Tests / Evidence
Human Gate
Post-Checks
```

## Stop

Wenn Ausgangsschema, Engine-Version oder Zielumgebung unklar sind, keine reale Migration ausführen.

## Leitgedanke

> Migration ist Zustandsübergang unter Last – nicht nur eine DDL-Datei.