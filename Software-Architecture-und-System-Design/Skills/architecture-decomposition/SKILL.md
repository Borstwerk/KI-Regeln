---
name: architecture-decomposition
description: Entwirft oder prüft System-, Modul-, Service- und Dependency-Grenzen aus Verantwortung, Invarianten, Ownership, Change-/Failure-Isolation und realen Drivers. Verwenden bei Modulzuschnitt, Service-Splits, Monolith-vs.-Services-Fragen oder Boundary-Problemen. Nicht für Klassen-/Methodendesign oder pauschale DDD-/Microservice-Empfehlungen verwenden.
---

# Architecture Decomposition

## Ziel

Verantwortung so schneiden, dass relevante Änderungen, Fehler und Ownership möglichst lokal bleiben, ohne unnötige verteilte Komplexität zu erzeugen.

## Eingaben

- System Context und Scope;
- Fachbegriffe/Invarianten;
- aktuelle Modul-/Service-/Dependency-Struktur;
- State-/Data-Ownership;
- kritische Flows;
- Change-, Scale-, Failure-, Security- und Team-/Lifecycle-Drivers.

## Vorgehen

1. Verantwortung und fachliche Capability klären.
2. bestehende Grenzen und reale Kopplung erfassen.
3. Boundary-Kandidaten aus Invarianten, Ownership, Änderungsrate und Failure-/Scale-Pressure ableiten.
4. öffentliche Oberfläche und Dependency Direction je Grenze definieren.
5. State-/Write-Ownership und Integrationsbedarf markieren.
6. prüfen, ob eine logische Modulgrenze genügt oder ein eigenes Deployable einen echten zusätzlichen Driver erfüllt.
7. Shared-Kernel/Common-/Utility-Flächen auf unkontrollierte Kopplung prüfen.
8. Auswirkungen auf Interfaces, Daten, Reliability, Betrieb und Migration an Nachbardomänen übergeben.

## Service-Split-Gate

Ein eigener Service braucht mindestens einen konkreten Driver, beispielsweise:

- notwendige unabhängige Ownership/Lifecycle-Steuerung;
- nachgewiesene Failure-Isolation;
- stark abweichendes Skalierungsprofil;
- Security-/Compliance-Grenze;
- andere konkrete Deployment-/Betriebsanforderung.

Ein Patternname oder Teamgröße allein genügt nicht.

## Nicht tun

- Bounded Context automatisch zu Microservice machen;
- Layered oder Domain-oriented Struktur global erzwingen;
- Shared Database automatisch als Architekturfehler behandeln;
- Zyklen nur wegen einer formalen Regel als kritisch einstufen;
- Fachmodellierung durch Ordner-/Service-Schnitt ersetzen;
- Quellcode ungefragt verschieben oder refactoren.

## Ausgabe

```text
Scope / Responsibilities
Current Boundaries / Coupling
Proposed Logical Boundaries
Ownership / Public Surfaces
Dependency Direction
Service-Split Drivers, if any
Shared / Cross-Cutting Risks
Trade-offs
Required Handoffs
Open Evidence
```

## Related

- `architecture-baseline`
- `system-design`
- `architecture-tradeoff-analysis`
- `architecture-evolution`
- `architecture-conformance-review`
- `domain-modeling`
- `interface-design`

## Leitgedanke

> Erst eine gute logische Grenze beweisen; erst danach entscheiden, ob sie über ein Netzwerk laufen muss.