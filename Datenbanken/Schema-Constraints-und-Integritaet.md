# Schema, Constraints und Datenintegrität

## Zweck

Datenbanken sollen ungültige Zustände möglichst an der stärksten geeigneten Grenze verhindern statt sie nur nachträglich zu erkennen.

## Grundprinzip

> Integritätsregeln gehören so nah wie sinnvoll an die Daten, ohne die Fachlogik unnötig an eine konkrete Engine zu ketten.

## Source of Truth

Bei bestehenden Systemen zuerst den tatsächlichen Stand ermitteln:

- Schema / Collections / Keys;
- Constraints und Validatoren;
- Defaults und Nullability;
- Beziehungen und Referenzregeln;
- Migrationen;
- Anwendungscode, der zusätzliche Invarianten erzwingt.

Nicht aus ORM-Namen oder Konventionen auf nicht verifizierte Datenbankregeln schließen.

## Arten von Integrität

Je nach Datenbankmodell können relevant sein:

- Typ- und Formatregeln;
- Required / Nullability;
- Eindeutigkeit;
- Wertebereiche / Enums;
- Referenzielle Integrität;
- fachliche Invarianten über mehrere Attribute;
- Schema-/Dokumentvalidierung;
- Lebenszyklus- und Löschregeln.

Die konkrete technische Umsetzung bleibt enginespezifisch.

## Mehrschichtige Validierung

Application Validation und Database Validation sind keine automatischen Gegensätze.

Typisches Modell:

```text
UI / API
→ gute Fehlermeldung und frühe Prüfung

Domain / Service
→ fachliche Regel

Datenbank
→ letzte belastbare Integritätsgrenze, soweit technisch passend
```

Keine Schicht darf stillschweigend eine andere voraussetzen, wenn dadurch ungültige Daten möglich werden.

## Bestehende Daten vor Verschärfung prüfen

Bevor ein neuer strenger Constraint oder Validator aktiviert wird:

1. Bestandsdaten analysieren;
2. Verstöße quantifizieren;
3. Bereinigungs-/Backfill-Strategie festlegen;
4. Rollout-Reihenfolge bestimmen;
5. erst dann die Regel verbindlich machen.

## Fehlende vs. übermäßige Constraints

Zu wenige Regeln erzeugen Drift und Reparaturaufwand.

Zu viele oder falsch platzierte Regeln können:

- legitime Zustände blockieren;
- Migrationen unnötig erschweren;
- Schreibpfade koppeln;
- enginespezifische Grenzen unnötig in die Domäne ziehen.

Deshalb jeden Constraint an einer konkreten Invariante begründen.

## Schema Drift

Bei mehreren Environments prüfen:

- entspricht das reale Schema dem versionierten Sollzustand?;
- existieren manuelle Änderungen außerhalb des Migrationswegs?;
- sind ORM-/ODM-Modell und Datenbank auseinander gelaufen?;
- sind alte Felder/Indizes/Constraints nach Migrationen übrig geblieben?

## Qualitätscheck

1. Ist jede wichtige Integritätsregel einer fachlichen Invariante zuordenbar?
2. Sind bestehende Daten mit neuen Regeln kompatibel?
3. Wird die reale Datenbank statt nur ein Modellfile geprüft?
4. Sind Validierungsebenen bewusst verteilt?
5. Gibt es einen sicheren Weg für Bestandsdaten und Rollback?

## Leitgedanke

> Datenintegrität ist kein Stilmerkmal des Schemas, sondern Schutz vor fachlich ungültigem Zustand.