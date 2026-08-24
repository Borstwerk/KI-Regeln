---
name: architecture-evolution
description: Plant evolutionäre Architekturänderungen mit Ist-/Zielbild, vertikalen Slices, Compatibility, Zwischenzuständen, Observability, Abort/Rollback und Retirement. Verwenden bei Re-Architecture, Service-Extraktion, Plattformwechsel oder größeren Boundary-Migrationen. Nicht als automatischer Rewrite-, Datenmigrations- oder Deploymentskill verwenden.
---

# Architecture Evolution

## Ziel

Eine Architekturänderung so planen, dass jeder Zwischenzustand erklärbar, beobachtbar und möglichst kontrolliert reversibel bleibt.

## Eingaben

- bestätigte Architecture Baseline;
- Zielentscheidung und Drivers;
- betroffene Komponenten, Contracts, Daten und Deployments;
- Compatibility-/Availability-/Recovery-Constraints;
- lokale Change-/Release-/Data-Gates.

## Vorgehen

1. Ist-Zustand und konkretes Problem festhalten.
2. Zielzustand und nicht verhandelbare Invarianten beschreiben.
3. kleinsten vertikalen Migrationsslice identifizieren.
4. pro Slice Reader/Writer, Contract-, Schema-, State- und Routingzustand beschreiben.
5. Koexistenz und Zwischenzustände explizit machen.
6. Success Evidence, Observability, Abort/Rollback und irreversible Effekte definieren.
7. Compatibility- und Deploymentreihenfolge an Interfaces/DB/Data/Infra übergeben.
8. Retirement des alten Pfads mit messbarem Kriterium planen.
9. produktive Ausführung nur über die zuständigen Fachprozesse und lokalen Gates.

## Muster

Strangler, Branch by Abstraction, Parallel Run, Shadowing, Adapter oder Dual-Path können Optionen sein. Kein Muster ist automatisch passend.

Dual Write, Dual Read oder Traffic Mirroring brauchen eigene Fehler-, Daten- und Privacy-Betrachtung.

## Status

- `PLAN_READY_FOR_LOCAL_GATE`
- `PLAN_WITH_OPEN_EVIDENCE`
- `BLOCKED`
- `UNVERIFIED`

Status autorisiert keine Code-, Daten-, Infrastruktur- oder Produktionsänderung.

## Nicht tun

- Big Rewrite als Default empfehlen;
- Migration als einen einzigen Cutover-Pfeil beschreiben;
- Compatibility oder Datenzustand während Koexistenz ignorieren;
- Rollback behaupten, wenn irreversible Seiteneffekte nicht adressiert sind;
- Sourcecode, Schema, Daten oder Produktion ungefragt verändern.

## Ausgabe

```text
Current / Target Architecture
Drivers / Invariants
Migration Slices
Per-Slice Intermediate State
Compatibility / Data / Routing Impact
Success Evidence / Observability
Abort / Rollback / Irreversible Effects
Retirement Criteria
Required Handoffs / Gates
Status
```

## Related

- `architecture-baseline`
- `system-design`
- `architecture-tradeoff-analysis`
- `architecture-conformance-review`
- `deployment-strategy`
- `schema-migration`
- `contract-change-review`
- `data-pipeline-design`
- `adr`

## Leitgedanke

> Architekturentwicklung ist eine Folge sicherer Zustände, nicht nur ein schönes Zielbild.