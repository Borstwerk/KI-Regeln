---
name: acceptance-criteria-design
description: Entwirft beobachtbare Acceptance Criteria und Verification Intent für bestehende Requirements oder Szenarien, ohne bereits Testfälle oder Implementierungsdetails festzulegen. Verwenden wenn Erfüllungskriterien fehlen, vage oder unvollständig sind. Nicht als Testdesign-, E2E- oder Contract-Test-Skill verwenden.
---

# Acceptance Criteria Design

## Ziel

Für relevante Requirements klar machen, unter welchen beobachtbaren Bedingungen Erfüllung beurteilt werden kann und welche Verifikationsart prinzipiell passt.

## Eingaben

- Requirement mit Scope und Quelle;
- relevante Szenarien/Actors/Conditions;
- bestätigte fachliche Regeln und Zielwerte;
- bekannte Failure-/Edge Cases;
- lokale Acceptance-/Abnahmepolicy, falls vorhanden.

## Vorgehen

1. Requirement und beabsichtigtes Ergebnis verstehen.
2. relevante Preconditions/Trigger/Conditions bestimmen.
3. beobachtbare Outcomes formulieren.
4. kritische negative, alternative oder Grenzfälle ergänzen.
5. bestätigte Toleranzen/Zielwerte übernehmen; fehlende nicht erfinden.
6. passendes Darstellungsformat wählen: Checkliste, Given/When/Then, EARS-artig, Tabelle oder andere klare Form.
7. Verification Intent markieren: Test, Analyse, Inspektion, Demonstration oder Kombination.
8. an `Testing-und-QA/` übergeben, wenn konkrete Testfälle, Testdaten, Automation oder Testebenen benötigt werden.

## Nicht tun

- Acceptance Criterion mit Test Case gleichsetzen;
- Given/When/Then oder EARS erzwingen;
- interne Klassen, Tabellen, Frameworks oder Endpoints festschreiben, sofern sie nicht selbst Requirement/Constraint sind;
- fehlende Performance-/Security-/Availability-Ziele erfinden;
- aus grünem Test automatisch Requirement Validation ableiten.

## Ausgabe

```text
Requirement Reference
Acceptance Criteria
Relevant Preconditions / Alternatives / Failure Cases
Verification Intent
Open Values / Missing Evidence
Testing Handoff
```

## Related

- `requirements-specification`
- `requirements-validation`
- `requirements-traceability`
- `test-design`
- `contract-testing`
- `e2e-testing`

## Leitgedanke

> Erst festlegen, was beobachtbar erfüllt sein muss; danach entscheiden, wie es konkret getestet wird.