---
name: database-design
description: Entwirft oder prüft ein Datenmodell anhand von Domäne, Integritätsanforderungen und realen Zugriffsmustern. Verwenden bei neuem Datenbankschema, Modellierungsentscheidungen, Schema-Reviews oder strukturellen Performanceproblemen. Nicht für eine einzelne Query-Optimierung verwenden.
compatibility: Benötigt für bestehende Systeme möglichst Zugriff auf reales Schema, Migrationen, Modelle oder Introspection; engine-spezifische Entscheidungen müssen gegen lokale Dokumentation und Version geprüft werden.
---

# Database Design

## Ziel

Ein tragfähiges, enginegerechtes Datenmodell entwickeln, ohne eine konkrete Datenbankphilosophie als universelle Wahrheit zu behandeln.

## Inputs

Soweit verfügbar:

- Domänenbegriffe und Invarianten;
- reale Lese-/Schreibmuster;
- Datenmengen und Wachstum;
- bestehendes Schema / Migrationen / Modelle;
- Konsistenz- und Lifecycle-Anforderungen;
- konkrete Engine und Version.

## Workflow

1. Domäne und zentrale Invarianten klären.
2. Reale oder erwartete Access Patterns erfassen.
3. Read-/Write-Last und Wachstum berücksichtigen.
4. Reales bestehendes Schema prüfen statt Namen zu erraten.
5. Passende Modellierungsoptionen mit Trade-offs formulieren.
6. Integritätsstrategie festlegen.
7. Engine-spezifische Mechanismen gegen lokale Primärquelle prüfen.
8. Risiken und offene Annahmen dokumentieren.

## Regeln

- Keine Tabellen, Spalten, Collections, Keys oder Felder erfinden.
- Keine pauschale Normalisierungs- oder Denormalisierungsregel.
- Datenmodell und Zugriffsmuster gemeinsam betrachten.
- Keine Performancebehauptung ohne Workload-Evidence.
- Engine-/ORM-/Driver-Version nicht aus Erinnerung annehmen.

## Output

```text
Anforderungen / Invarianten
Access Patterns
bestehender Zustand
empfohlenes Modell
Alternativen / Trade-offs
Integritätsstrategie
Wachstumsrisiken
zu verifizierende Annahmen
```

## Stop / Eskalation

Wenn für eine bestehende produktive Datenbank weder Schema noch belastbare Beschreibung verfügbar sind, keine konkreten Schemaänderungen als sicher darstellen.

## Leitgedanke

> Erst verstehen, wie Daten gemeinsam leben und benutzt werden – dann ihre Struktur festlegen.