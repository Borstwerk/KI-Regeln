# Stakeholder, Bedarf, Ziele und Quellen

## Zweck

Requirements entstehen nicht aus einem leeren Dokument. Sie werden aus Stakeholderbedarfen, Zielen, Regeln, bestehendem Verhalten, Verträgen, Risiken und anderen autoritativen Quellen abgeleitet.

## Requirement Sources

Mögliche Quellen sind unter anderem:

- Nutzer und andere betroffene Stakeholder;
- Product-/Business-Owner und Entscheidungsträger;
- Gesetze, Verträge, Policies und Normen;
- bestehende Systeme und beobachtetes Verhalten;
- Fachprozesse, Domänenmodelle und Betriebsregeln;
- Support-, Incident-, Research- oder Nutzungsdaten;
- bestehende Requirements, ADRs, Interfaces und Datenverträge.

Eine Quelle wird nicht allein durch ihre Existenz autoritativ. Relevanz, Aktualität, Scope und Entscheidungskompetenz müssen bekannt sein.

## Bedarf vor Requirement

Hilfreiche Trennung:

```text
Problem / Ziel / Stakeholder-Erwartung
→ warum etwas gebraucht wird

Requirement
→ welche beobachtbare Eigenschaft oder welcher Constraint erfüllt sein muss

Design
→ wie das System dies technisch erreicht
```

Ein Stakeholderwunsch ist zunächst Evidence für einen Bedarf. Er wird nicht automatisch zu einem verbindlichen Requirement.

## Stakeholder Mapping

Für relevante Stakeholder klären:

- Rolle und betroffener Kontext;
- Ziele und erwarteter Nutzen;
- relevante Entscheidungen oder Freigaben;
- Wissen über Fachprozess/System;
- mögliche Konflikte mit anderen Stakeholdern;
- benötigte Beteiligung bei Validation oder Change.

Keine universelle RACI-, Power/Interest- oder Persona-Pflicht. Solche Modelle sind Hilfsmittel, wenn sie die konkrete Aufgabe verbessern.

## Ziele und Outcomes

Ziele sollten getrennt von Requirements gepflegt werden, damit mehrere Requirements auf dasselbe Ziel zurückgeführt und Änderungen nachvollzogen werden können.

Bei messbaren Zielaussagen sind mindestens Quelle, Messgröße, Scope und Zeitraum zu klären, sofern diese für Entscheidungen relevant sind. Fehlende Werte werden nicht erfunden.

## Provenance

Für ein Requirement sollte nachvollziehbar sein:

- aus welcher Quelle oder welchem Bedarf es stammt;
- welche Annahmen bei der Ableitung verwendet wurden;
- wer die Aussage bestätigt hat oder noch bestätigen muss;
- welcher Stand der Quelle verwendet wurde.

## Konflikte

Unterschiedliche Quellen dürfen widersprechen. Dann:

1. Konflikt explizit machen;
2. betroffene Aussage und Sources benennen;
3. Scope-, Zeit- oder Definitionsunterschiede prüfen;
4. zuständige Entscheidung klären;
5. Disposition und Begründung dokumentieren.

Ein Konflikt wird nicht durch stilles Bevorzugen der technisch bequemeren Quelle gelöst.

## Leitgedanke

> Gute Requirements behalten die Spur zurück zu dem Problem, das sie rechtfertigt.