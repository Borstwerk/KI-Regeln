---
name: requirements-specification
description: Formuliert bestätigte Bedarfe, Ziele und Constraints als klare funktionale, qualitative, operative oder transitionale Requirements mit sichtbaren Annahmen, Quellen und geeigneter Artefaktform. Verwenden zum Erstellen oder Überarbeiten einer Spezifikation. Nicht für Architekturdesign, Testfalldesign oder das Erfinden fehlender Zielwerte verwenden.
---

# Requirements Specification

## Ziel

Requirement Candidates so spezifizieren, dass Bedeutung, Scope, Herkunft und erwartete Erfüllung für relevante Downstream-Entscheidungen ausreichend klar sind.

## Eingaben

- bestätigte oder klar markierte Stakeholderbedarfe/Ziele;
- Requirements Sources und Provenance;
- Scope, Non-Goals und Constraints;
- Domain-Begriffe/Invarianten;
- relevante Szenarien und offene Annahmen;
- lokaler Dokument-/ID-/Priorisierungsrahmen, falls vorhanden.

## Vorgehen

1. Bedarf, Ziel und Requirement voneinander trennen.
2. Requirement-Typ und passende Darstellungsform wählen.
3. Actor/Condition/Verhalten/Ergebnis beziehungsweise Qualitätsziel konkretisieren.
4. relevante Alternativ-/Failure Cases ergänzen.
5. bestätigte Constraints und Zielwerte mit Herkunft übernehmen.
6. fehlende entscheidungsrelevante Werte als offen markieren statt erfinden.
7. Acceptance-/Verification-Intent vorbereiten oder an `acceptance-criteria-design` übergeben.
8. IDs, Status, Quelle, Annahmen und Traceability nach lokaler Policy pflegen.
9. Lösungsdetails entfernen, sofern sie keine echten Constraints sind.

## Qualitätscheck

Prüfen auf:

- Notwendigkeit / Herkunft;
- Eindeutigkeit im Scope;
- Konsistenz;
- ausreichende Vollständigkeit;
- Verifizierbarkeit;
- sichtbare Bedingungen und Annahmen;
- unnötige Lösungsfestlegung;
- Traceability.

## Nicht tun

- PRD/BRD/SRS oder User Stories als Pflichtformat erzwingen;
- jedem Requirement künstlich `shall` oder Given/When/Then aufzwingen;
- `schnell`, `sicher`, `skalierbar` ohne konkreten Kontext als fertige NFRs akzeptieren;
- SLO-, RTO/RPO-, Performance- oder Retention-Werte erfinden;
- Architektur-, Datenbank- oder API-Design als Requirement tarnen;
- Implementierung oder Tests ungefragt erzeugen.

## Ausgabe

```text
Scope / Goals / Sources
Requirements by Type
Requirement IDs / Status
Conditions / Scenarios / Exceptions
Quality Targets / Open Targets
Constraints / Assumptions
Acceptance / Verification Intent
Traceability Hooks
Open Questions / Conflicts
```

## Related

- `requirements-elicitation`
- `acceptance-criteria-design`
- `requirements-traceability`
- `requirements-validation`
- `domain-modeling`
- `system-design`

## Leitgedanke

> Spezifizieren heißt Bedeutung festhalten – nicht möglichst viele Felder füllen.