# Workflow: Systemgrenze und Dekomposition

## Ziel

Verantwortungs-, Modul- und gegebenenfalls Servicegrenzen aus echten fachlichen und technischen Drivers ableiten.

## Ablauf

```text
1. System Context
→ 2. Domain / Invariants / Ownership
→ 3. aktuelle Kopplung
→ 4. logische Boundaries
→ 5. Public Surfaces / Dependency Direction
→ 6. Service-Split-Gate
→ 7. Trade-off / Review
```

## Skills

- `architecture-baseline` – bestehende Grenzen und Kopplung erfassen;
- `domain-modeling` – Fachobjekte/Invarianten klären;
- `architecture-decomposition` – Boundary-Design;
- `interface-design` – konkrete Provider-/Consumer-Verträge ausarbeiten;
- `architecture-tradeoff-analysis` – wenn mehrere viable Schnitte konkurrieren;
- `architecture-review` – breiter Gegencheck.

## Regeln

- logische Boundary vor Deployment Boundary;
- Bounded Context ist nicht automatisch Service;
- Shared DB oder Dependency Cycle wird nach Wirkung und lokaler Regel bewertet;
- keine Sourcecode-Verschiebung ohne separaten Implementierungsauftrag.

## Ergebnis

Ein nachvollziehbarer Boundary- und Dependency-Schnitt mit Ownership, öffentlichen Oberflächen, Service-Split-Drivers und klaren Handoffs.