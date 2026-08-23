# Migrationen, Backfills und Rollback

## Zweck

Schema- und Datenänderungen sollen mit Bestandsdaten, laufender Anwendung, Locking, Rollout und Recovery gemeinsam geplant werden.

## Grundprinzip

> Migration generiert ≠ Migration sicher.

## Vor jeder Migration

Prüfen:

- aktuelles reales Schema;
- gewünschter Endzustand;
- betroffene Datenmengen;
- vorhandene Daten, die neue Regeln verletzen könnten;
- Lock-/Rewrite-/Downtime-Risiken;
- Kompatibilität mit alter und neuer Anwendungsversion;
- Auswirkungen auf Reads, Writes, Indizes und Replikation;
- Rollback oder Forward-Fix-Strategie.

## Risikoklassen

### Niedrigeres Risiko

Beispielsweise additive, rückwärtskompatible Änderungen ohne große Datenbewegung.

Auch hier: reale Engine-/Versionsdokumentation prüfen.

### Mittleres / hohes Risiko

Beispielsweise:

- Spalten/Felder verpflichtend machen;
- Typänderungen;
- große Backfills;
- Index-/Constraint-Änderungen;
- Rename mit laufender alter App-Version;
- Datenverdichtung oder -aufteilung;
- Löschung alter Struktur.

Diese Änderungen brauchen explizite Rollout- und Verifikationsplanung.

## Expand – Migrate – Contract

Für nichttriviale Online-Änderungen ist häufig sinnvoll:

```text
EXPAND
→ neue kompatible Struktur hinzufügen

MIGRATE
→ Anwendung und Bestandsdaten schrittweise umstellen

CONTRACT
→ alte Struktur erst entfernen, wenn sie sicher unbenutzt ist
```

Das ist ein bevorzugtes Muster, kein universelles Engine-Gebot.

## Backfills

Backfills innerhalb einer operativen DB gehören hierher, wenn sie Teil einer Schema-/Datenmodelländerung sind.

Prüfen:

- Batch-Größe;
- Idempotenz;
- Retry-Fähigkeit;
- Last und Locking;
- Fortschrittsmessung;
- Pause/Resume;
- Umgang mit gleichzeitig neuen Writes;
- Validierung nach Abschluss.

Historische Datenbewegung zwischen Systemen gehört dagegen typischerweise zu `Data Engineering/`.

## Rollback vs. Forward Fix

Rollback ist nicht immer technisch oder fachlich sinnvoll.

Vor Deployment festlegen:

- kann Schema sicher zurückgerollt werden?;
- wurden bereits Daten in neuer Form geschrieben?;
- ist ein Forward Fix sicherer?;
- existiert ein getesteter Restore-/Recovery-Weg?;

Keine pauschale Rollback-Behauptung ohne reale Prüfung.

## Produktions-Gate

Vor realer Migration mindestens Evidence für:

```text
Zielzustand
aktueller Zustand
Migration Diff
Risikoanalyse
Bestandsdatenprüfung
Rolloutplan
Rollback / Forward Fix
Tests / Staging-Evidence
Post-Migration-Checks
```

Dann explizite Freigabe gemäß Projektprozess.

## Destruktive Änderungen

DROP, TRUNCATE, irreversible Konvertierung oder massenhafte Löschung benötigen ein hartes Gate mit genauer Zielidentität und Wirkung.

> „Mach die Migration“ ist keine pauschale Freigabe für zusätzliche destruktive Reparaturen.

## Leitgedanke

> Eine sichere Migration plant nicht nur das neue Schema, sondern den gesamten Weg vom alten zum neuen Zustand.