---
name: database-query-review
description: Prüft Datenbankabfragen auf fachliche Korrektheit, Schema-Bezug, Scope und Sicherheit. Verwenden für SELECT-/Find-/Aggregate-/Write-Queries, Query-Builder oder ORM-Abfragen. Nicht als primären Performance-Tuning-Skill verwenden, wenn das Problem ausdrücklich Latenz oder Indexierung ist.
compatibility: Für belastbaren Review möglichst reales Schema und konkrete Engine/Library-Version verfügbar machen.
---

# Database Query Review

## Ziel

Eine konkrete Query unabhängig von Performance auf Korrektheit, Datenzugriff und Wirkung prüfen.

## Workflow

1. Intent der Query festhalten.
2. Reales Schema/Felder/Typen verifizieren.
3. Filter-, Join-/Reference-, Null-/Missing- und Kardinalitätslogik prüfen.
4. Autorisierungs-/Tenant-Grenzen prüfen.
5. Parametrisierung und untrusted Input prüfen.
6. Bei Writes Zielmenge und Wirkung separat prüfen.
7. Performance-Risiken markieren, aber bei tiefer Diagnose an `query-performance` übergeben.

## Findings priorisieren

- **Blocker:** falsche Daten, unbounded/destruktive Wirkung, Injection-/Tenant-Risiko.
- **Hoch:** relevante Korrektheits- oder Scopefehler.
- **Mittel:** Robustheits-, Wartbarkeits- oder plausible Performanceprobleme.
- **Niedrig:** Lesbarkeit / kleinere Strukturverbesserung.

## Regeln

- Keine Query gegen ein vermutetes Schema freigeben.
- `SELECT *` / vollständige Dokumente nicht automatisch als Fehler behandeln; prüfen, ob unnötig sensible oder große Daten geladen werden.
- ORM/Query Builder nicht als automatische Sicherheits- oder Performancegarantie betrachten.
- Write-Query ohne klaren Filter/Scope als hohes Risiko behandeln.
- Review ist kein Auftrag zur Ausführung.

## Output

```text
Intent
Schema-Evidence
Findings nach Priorität
Wirkungsbereich
Security-/Tenant-Befund
Performance-Hinweise
offene Verifikation
```

## Leitgedanke

> Eine Query wird zuerst auf Wahrheit und Wirkung geprüft – nicht auf Eleganz.