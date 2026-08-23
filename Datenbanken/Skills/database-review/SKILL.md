---
name: database-review
description: Führt einen unabhängigen Gesamtcheck eines Datenbankdesigns oder einer geplanten Änderung über Modell, Integrität, Queries, Performance, Concurrency, Migration, Security und Betrieb durch. Verwenden vor Freigabe größerer Datenbankänderungen oder für gezielte Audits. Nicht ungefragt als Redesign-Auftrag verwenden.
compatibility: Für belastbare Freigabe möglichst reales Schema, Änderung/Diff, Engine-Version und relevante Betriebs-/Workload-Evidence bereitstellen.
---

# Database Review

## Ziel

Eine Datenbankänderung oder einen Datenbankbereich unabhängig prüfen, ohne die ursprüngliche Planung automatisch zu bestätigen.

## Prüfachsen

1. **Scope / Source of Truth** – reales Schema, Version, Zielumgebung.
2. **Modell / Access Patterns** – passt Struktur zur Domäne und Nutzung?
3. **Integrität** – sind wichtige Invarianten geschützt?
4. **Queries / Security** – fachlich korrekt, sicher, tenant-/scope-treu?
5. **Performance** – Evidence statt Tuningannahme?
6. **Concurrency** – Isolation, Locks, Retry, Race Conditions?
7. **Migration** – Bestandsdaten, Rollout, Backfill, Rollback?
8. **Betrieb / Recovery** – Connections, Monitoring, Backup/Restore?
9. **Gates** – sind riskante Aktionen korrekt freigegeben?

## Prioritäten

- **Blocker:** Datenverlust, falsche Daten, Security-/Tenant-Verstoß, nicht kontrollierbare destruktive Aktion.
- **Hoch:** erhebliche Integritäts-, Migration-, Concurrency- oder Betriebsrisiken.
- **Mittel:** relevante Performance-/Wartbarkeits-/Robustheitsprobleme.
- **Niedrig:** kleinere Verbesserungen ohne wesentliche Betriebswirkung.

## Regeln

- Review ist nicht automatisch Rewrite oder Redesign.
- Keine Freigabe auf Basis eines Modells, wenn reale Source of Truth fehlt und sie erforderlich wäre.
- Neueste Variante nicht automatisch als beste behandeln.
- Engine-spezifische Aussage gegen echte Primärquelle/Version prüfen.
- Fehlende Evidence als offene Verifikation benennen statt Sicherheit zu simulieren.

## Output

```text
Urteil
Blocker / hohe / mittlere / niedrige Findings
Evidence
fehlende Verifikation
Gate-Status
Restrisiken
Freigabeempfehlung
```

## Freigabestufen

```text
READY
READY WITH CONDITIONS
REWORK REQUIRED
BLOCKED / INSUFFICIENT EVIDENCE
```

## Leitgedanke

> Ein Datenbankreview prüft nicht, ob die Lösung plausibel klingt, sondern ob sie unter realen Daten und realem Betrieb trägt.