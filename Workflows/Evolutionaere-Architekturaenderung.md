# Workflow: Evolutionäre Architekturänderung

## Ziel

Eine größere Architekturänderung über sichere, beobachtbare Zwischenzustände planen und an die zuständigen Umsetzungsprozesse übergeben.

## Ablauf

```text
1. Architecture 0
→ 2. Zielentscheidung / Drivers
→ 3. betroffene Contracts / Daten / Deployments
→ 4. kleinster vertikaler Slice
→ 5. Zwischenzustand / Compatibility
→ 6. Success Evidence / Abort / Rollback
→ 7. weitere Slices
→ 8. Cutover / Retirement über lokale Gates
```

## Skills

- `architecture-baseline`;
- `architecture-evolution` als Kern;
- `contract-change-review` für Contract Compatibility;
- `schema-migration` beziehungsweise Data-Engineering-Skills für Datenänderungen;
- `deployment-strategy` für technische Rolloutmechanik;
- `architecture-conformance-review` für strukturelle Zielerreichung;
- `architecture-review` vor großem Cutover.

## Gates

- Plan ≠ Ausführung.
- Dual Write/Read oder Shadowing braucht eigene Failure-/Data-/Privacy-Betrachtung.
- Produktiver Cutover, Datenänderung, Deploy oder Retirement bleibt separat autorisiert.
- Rollback nur behaupten, wenn irreversible Seiteneffekte berücksichtigt sind.

## Ergebnis

Ein migrationsfähiger Architekturplan mit Slices, Zwischenzuständen, Compatibility, Evidence, Abort/Rollback und Retirement-Kriterien.