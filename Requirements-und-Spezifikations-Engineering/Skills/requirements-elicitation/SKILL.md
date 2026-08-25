---
name: requirements-elicitation
description: Gewinnt und klärt Stakeholderbedarfe, Ziele, Constraints, Scope und Requirement Candidates aus geeigneten Quellen mit fokussierten Interviews, Workshops, Dokument-/Systemanalyse oder anderen passenden Techniken. Verwenden bei neuen, unklaren oder widersprüchlichen Anforderungen. Nicht als Architektur-, Lösungsdesign- oder automatischer PRD-Generator verwenden.
---

# Requirements Elicitation

## Ziel

Die entscheidungsrelevanten Bedarfe und Constraints mit sichtbarer Herkunft erfassen und die wichtigsten Unsicherheiten beziehungsweise Konflikte auflösen.

## Eingaben

- Problem-/Initiativenkontext;
- vorhandene Stakeholder und Sources;
- bestehende Notes, RFPs, Tickets, Prozess-/Systemartefakte;
- bekannte Ziele, Risiken und Constraints;
- gewünschter nächster Handoff beziehungsweise Entscheidungszweck.

## Vorgehen

1. Ziel der Elicitation und benötigte Entscheidung klären.
2. relevante Requirements Sources und Stakeholder identifizieren.
3. vorhandene Evidence zuerst lesen, bevor bekannte Fragen erneut gestellt werden.
4. Elicitation-Technik nach Informationsproblem und Stakeholderzugang wählen.
5. Fragen progressiv nach Entscheidungswirkung priorisieren.
6. Bedarf, Requirement Candidate, Annahme, Constraint und Lösungsidee getrennt erfassen.
7. Inferenz aus Quellen ausdrücklich als `INFERRED` markieren.
8. Konflikte nach Ziel, Scope, Semantik, Constraint, Zeitstand oder Ownership einordnen.
9. ungelöste entscheidungsrelevante Fragen sichtbar weitergeben.

## Nicht tun

- alle denkbaren Fragen in einem Standardfragebogen abfeuern;
- fehlende Antworten mit plausiblen Branchenannahmen füllen;
- technische Lösung bereits als Requirement festschreiben, wenn der Bedarf offen ist;
- `100 % vollständig` oder numerische Clarity Scores als Beweis verwenden;
- aus einem bestehenden System jedes beobachtete Verhalten als gewollt ableiten;
- automatisch Architektur oder Implementierungsplan erzeugen.

## Ausgabe

```text
Elicitation Goal / Decision Context
Requirements Sources / Stakeholders
Confirmed Needs / Goals
Requirement Candidates
Constraints / Assumptions / Non-Goals
Conflicts / Dispositions
Inferred Items Requiring Validation
Open Questions by Impact
Recommended Next Requirements Step
```

## Related

- `requirements-baseline`
- `requirements-specification`
- `requirements-validation`
- `requirements-review`
- `domain-modeling`

## Leitgedanke

> Elicitation schließt die nächste relevante Wissenslücke – nicht jedes denkbare Fragefeld.