---
name: architecture-baseline
description: Erfasst die bestehende Softwarearchitektur evidenzbasiert aus Repository, Dokumentation, ADRs, Contracts, Daten-/State-Ownership und relevanten Runtime-Artefakten. Verwenden, wenn der aktuelle Systemkontext, Komponenten, Abhängigkeiten, kritische Flows oder Architekturkonflikte zuerst verstanden werden müssen. Nicht als Re-Architecture- oder Implementierungsskill verwenden.
---

# Architecture Baseline

## Ziel

Die aktuelle Architektur als prüfbare Ausgangslage erfassen, bevor neue Strukturen vorgeschlagen oder alte bewertet werden.

## Eingaben

- Nutzerauftrag und Scope;
- Repository-/Code-Struktur;
- Architektur-/Projekt-/Betriebsdokumentation;
- ADRs und andere Entscheidungen;
- APIs, Events, Daten-/Schemaartefakte;
- Deployment-/Runtime-/Observability-Evidence, soweit relevant und verfügbar;
- bekannte Requirements, Drivers und Constraints.

## Arbeitsweise

1. Scope und Systemgrenze bestimmen.
2. Quellen nach Aktualität und Autorität einordnen.
3. Akteure, externe Systeme und wesentliche Deployables/Module erfassen.
4. Capability-, State- und Datenownership kartieren.
5. relevante Dependency Directions und öffentliche Grenzen beschreiben.
6. kritische End-to-End- und Failure-Flows nachvollziehen.
7. accepted/superseded/stale ADRs und dokumentierte Entscheidungen zuordnen.
8. Widersprüche zwischen Docs, Code, Config und Runtime-Evidence explizit markieren.
9. offene Architekturfragen und Missing Evidence festhalten.

## Evidence Status

- `CONFIRMED`
- `LIKELY`
- `UNVERIFIED`
- `CONFLICTING`

## Nicht tun

- Ordnerstruktur automatisch mit fachlicher Architektur gleichsetzen;
- alte Diagramme oder ADRs als aktuelle Wahrheit behandeln;
- aus fehlender Dokumentation eine neue Architektur erfinden;
- Microservices, DDD, Hexagonal oder andere Styles allein anhand des Tech-Stacks behaupten;
- Findings ungefragt implementieren oder refactoren.

## Ausgabe

```text
Scope / System Boundary
Actors / External Systems
Current Components / Deployables / Modules
Ownership / Sources of Truth
Dependency Directions / Public Boundaries
Critical Runtime / Failure Flows
Existing Decisions / ADR Status
Evidence Conflicts
Missing Evidence / Open Questions
Baseline Confidence
```

## Related

- `system-design`
- `architecture-decomposition`
- `architecture-conformance-review`
- `architecture-review`
- `domain-modeling`
- `interface-review`
- `database-review`
- `reliability-review`

## Leitgedanke

> Architektur 0 zuerst verstehen, bevor Architektur 1 entworfen wird.