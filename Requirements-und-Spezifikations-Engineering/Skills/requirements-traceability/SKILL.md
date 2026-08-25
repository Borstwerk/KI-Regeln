---
name: requirements-traceability
description: Baut oder prüft nachvollziehbare Links von Stakeholdern, Quellen und Zielen über Requirements zu Acceptance Criteria, Architektur, Contracts, Tests und anderer relevanter Evidence. Verwenden für Traceability, Coverage, Orphans oder Impact-Vorbereitung. Nicht als Beweis für fachliche Korrektheit oder automatischer Change-Skill verwenden.
---

# Requirements Traceability

## Ziel

Begründung und Downstream-Wirkung von Requirements nachvollziehbar machen, ohne Linkvollständigkeit mit Requirement-Qualität gleichzusetzen.

## Eingaben

- Requirements mit stabilen Referenzen/IDs soweit vorhanden;
- Sources, Stakeholder, Ziele und Entscheidungen;
- Acceptance Criteria / Verification Intent;
- relevante Architecture-/Interface-/Data-/Security-/Reliability-Artefakte;
- Test-/Evidence-Artefakte, soweit relevant;
- lokale Traceability-Policy.

## Vorgehen

1. gewünschte Traceability-Frage und Scope bestimmen.
2. Linktypen und autoritative Artefakte festlegen.
3. Upstream-Provenance pro Requirement erfassen.
4. Downstream-Links erfassen, ohne fehlende Beziehungen zu erfinden.
5. Orphans, stale Links und Links zu supersedeten Requirements markieren.
6. Coverage nur mit definiertem Nenner/Scope berechnen.
7. bidirektionale Impact-Pfade für relevante Change-Fälle sichtbar machen.
8. Tool-/ID-spezifische Darstellung lokal halten.

## Status

- `LINKED`
- `PARTIAL`
- `ORPHANED`
- `STALE`
- `UNVERIFIED`

## Nicht tun

- 100 Prozent Coverage als Korrektheitsbeweis behandeln;
- Requirements ohne Source automatisch als falsch löschen;
- fehlende Tests/ADRs/Contracts erfinden, nur um Matrixlücken zu füllen;
- Jira, ReqIF, DOORS, YAML oder ein bestimmtes ID-Schema erzwingen;
- Downstream-Artefakte ungefragt ändern.

## Ausgabe

```text
Traceability Scope / Link Types
Source / Goal → Requirement Links
Requirement → Acceptance / Design / Test Links
Coverage by Defined Question
Orphans / Stale / Superseded Links
Impact Paths
Missing Evidence
```

## Related

- `requirements-baseline`
- `requirements-specification`
- `acceptance-criteria-design`
- `requirements-change-analysis`
- `requirements-review`

## Leitgedanke

> Ein Link hilft beim Navigieren und Ändern – er beweist nicht, dass beide Enden richtig sind.