---
name: architecture-conformance-review
description: Prüft read-only, ob die tatsächliche Systemstruktur mit gültigen Architekturentscheidungen, Modul-/Dependency-Regeln, Ownership und definierten Fitness Functions übereinstimmt. Verwenden bei Architekturdrift, Boundary-Verletzungen, ADR-Compliance oder strukturellen CI-/Lint-Regeln. Nicht als Code-Quality-Review oder automatischer Fixskill verwenden.
---

# Architecture Conformance Review

## Ziel

Abweichungen zwischen beabsichtigter und tatsächlicher Architektur mit konkreter Evidence sichtbar machen, ohne jede Abweichung automatisch als Defekt zu behandeln.

## Eingaben

- gültige Soll-Architektur, ADRs oder explizite Boundary-Regeln;
- Repository-/Dependency-Struktur;
- öffentliche/interne Moduloberflächen;
- Ownership-/State-Regeln;
- bestehende Fitness Functions oder Architecture Checks;
- relevante Runtime-/Deployment-Evidence, falls die Regel sie betrifft.

## Vorgehen

1. Referenzmodell und dessen Status bestätigen.
2. prüfbare Architekturregeln extrahieren.
3. tatsächliche Abhängigkeiten, Zugriffe und relevante Strukturen erfassen.
4. Soll/Ist-Abweichungen mit Fundort und Evidence dokumentieren.
5. unterscheiden: violation, accepted legacy, stale documentation, superseded decision oder unverified.
6. bestehende Fitness Functions prüfen: existieren sie, laufen sie, erkennen sie relevante Verstöße?
7. fehlende automatisierbare Guardrails nur dort vorschlagen, wo reale Architekturwirkung besteht.
8. Findings priorisieren, aber nicht ungefragt reparieren.

## Evidence Status

- `CONFIRMED`
- `LIKELY`
- `UNVERIFIED`
- `CONFLICTING`

## Finding-Typen

- `BOUNDARY_VIOLATION`
- `DEPENDENCY_DRIFT`
- `OWNERSHIP_DRIFT`
- `ADR_DRIFT`
- `STALE_ARCHITECTURE_DOC`
- `UNENFORCED_RULE`
- `ACCEPTED_LEGACY`

## Near-Miss-Grenze

- Klassen-/Methoden-/SOLID-Probleme → `code-review`;
- fachlich falsche Begriffe/Objekte → `domain-modeling`;
- konkrete API-Compatibility → `contract-change-review`;
- allgemeine Testsuitequalität → `test-suite-review`.

## Nicht tun

- fehlende Soll-Architektur aus persönlicher Patternpräferenz erfinden;
- jeden Cycle oder Shared Code als Architekturfehler einstufen;
- konfigurierte CI-Regel als wirksam behaupten, ohne Evidence, dass sie Verstöße erkennt;
- Findings ungefragt fixen;
- Accepted/Superseded-Status von ADRs ignorieren.

## Ausgabe

```text
Scope / Reference Architecture
Checks Run / Missing Checks
Findings [type, severity, evidence, location]
ADR / Boundary / Ownership Compliance
Fitness Function Coverage
Stale / Conflicting Evidence
Accepted Legacy
Recommended Guardrails
Verdict
```

## Verdict

- `CONFORMANT_WITHIN_SCOPE`
- `CONFORMANT_WITH_FINDINGS`
- `NON_CONFORMANT`
- `UNVERIFIED`

Das Verdict ist keine Refactoring- oder Merge-Autorisierung.

## Related

- `architecture-baseline`
- `architecture-evolution`
- `architecture-review`
- `code-review`
- `test-suite-review`
- `adr`

## Leitgedanke

> Conformance prüft die gültige lokale Architektur – nicht die Lieblingsarchitektur des Reviewers.