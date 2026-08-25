---
name: requirements-change-analysis
description: Analysiert Änderungen an bestehenden oder baselinierten Requirements auf semantische Differenz, Stakeholder-/Zielwirkung, Traceability, Downstream-Impact, Migration und Supersession. Verwenden vor relevanten Requirement Changes. Nicht als automatischer Rewrite-, Implementierungs-, Contract- oder Deployment-Skill verwenden.
---

# Requirements Change Analysis

## Ziel

Vor einer Requirements-Änderung sichtbar machen, was sich semantisch ändert, warum und welche nachgelagerten Entscheidungen oder Artefakte betroffen sein können.

## Eingaben

- aktuelle Requirements Baseline;
- vorgeschlagene Änderung und Quelle/Grund;
- betroffene Ziele/Stakeholder;
- Traceability-/Downstream-Artefakte;
- lokale Change-/Approval-/Versionierungs-Policy.

## Vorgehen

1. alten und vorgeschlagenen Requirement-Stand semantisch vergleichen.
2. Motivation, Source und Entscheidungskompetenz prüfen.
3. betroffene Acceptance Criteria, Annahmen, Constraints und Priorität markieren.
4. Upstream-Ziel-/Stakeholderwirkung prüfen.
5. Downstream-Impact über Traceability suchen: Architecture, Interfaces, Data, Security, Reliability, Tests, Dokumentation, Betrieb.
6. Compatibility-/Migration-/Rollout-Risiken an zuständige Fachdomänen übergeben.
7. Entscheidungsvorschlag formulieren: accept, revise, defer, reject oder blocked nach lokaler Policy.
8. Supersession/Versionierung und erneute Validation planen.

## Nicht tun

- Textdiff mit semantischem Impact gleichsetzen;
- baseliniertes Requirement still überschreiben;
- Downstream-Artefakte automatisch anpassen;
- Change Approval aus fachlicher Analyse ableiten;
- Scope-/Prioritätsänderung als redaktionelle Korrektur tarnen;
- Produktcode, Daten, Contract oder Deployment ungefragt verändern.

## Ausgabe

```text
Current / Proposed Requirement
Change Source / Rationale
Semantic Delta
Upstream Goal / Stakeholder Impact
Acceptance / Constraint / Assumption Impact
Downstream Impact / Traceability
Migration / Compatibility Handoffs
Supersession / Re-Validation Need
Recommendation / Decision Needed
```

## Related

- `requirements-baseline`
- `requirements-traceability`
- `requirements-validation`
- `contract-change-review`
- `architecture-evolution`
- `schema-migration`

## Leitgedanke

> Ein Requirement Change endet nicht am Satzende – seine Wirkung läuft durch das System.