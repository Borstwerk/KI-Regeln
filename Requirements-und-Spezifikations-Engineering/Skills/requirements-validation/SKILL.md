---
name: requirements-validation
description: Validiert Requirements gegen Stakeholderbedarfe, Ziele, Scope, Quellen, Konsistenz, Verifizierbarkeit, Feasibility-Risiken und relevante Szenarien. Verwenden vor Architektur-/Implementierungshandoff oder nach wesentlichen Requirement Changes. Nicht mit Product Validation, Testausführung oder bloßem Formatlint verwechseln.
---

# Requirements Validation

## Ziel

Prüfen, ob das Requirements-Set für den beabsichtigten Scope den richtigen Bedarf ausreichend klar, konsistent, nachvollziehbar und verifizierbar beschreibt.

## Eingaben

- Requirements-Set und Scope;
- Stakeholder-/Source-/Goal-Evidence;
- Domain-Begriffe und relevante Constraints;
- Acceptance Criteria / Verification Intent;
- Traceability;
- bekannte Architektur-/Feasibility-/Betriebsevidence, soweit zur Plausibilitätsprüfung nötig.

## Prüfachsen

1. Stakeholder- und Ziel-Fit;
2. Source/Provenance;
3. Scope, Non-Goals und Annahmen;
4. Klarheit und Eindeutigkeit;
5. Vollständigkeit für die anstehende Entscheidung;
6. Konsistenz / Konflikte / Dubletten;
7. Verifizierbarkeit und Acceptance Intent;
8. Feasibility-Risiken und unbelegte technische Annahmen;
9. nominale, alternative und relevante Failure-/Edge-Szenarien;
10. Traceability und offene Downstream-Fragen.

## Status

- `VALIDATED_WITHIN_SCOPE`
- `VALIDATED_WITH_GAPS`
- `BLOCKED`
- `UNVERIFIED`

## Nicht tun

- ausgefüllte Templates oder numerische Quality Scores als Validation-Beweis verwenden;
- fehlende Stakeholderentscheidungen selbst treffen;
- Product Verification oder Product Validation als ausgeführt behaupten;
- Tests erzeugen oder ausführen, wenn nur Requirements Validation beauftragt ist;
- Architektur zur Lösung offener Requirements erfinden;
- fehlende Zielwerte ergänzen.

## Ausgabe

```text
Scope / Validation Purpose
Sources / Stakeholder Fit
Findings by Quality Axis
Conflicts / Duplicates / Gaps
Acceptance / Verifiability Findings
Feasibility / Assumption Risks
Traceability Findings
Open Decisions / Required Handoffs
Validation Status
```

## Related

- `requirements-baseline`
- `requirements-elicitation`
- `requirements-specification`
- `acceptance-criteria-design`
- `requirements-traceability`
- `requirements-review`
- `test-strategy`
- `system-design`

## Leitgedanke

> Requirements Validation fragt, ob wir mit diesen Aussagen wahrscheinlich das richtige Problem bauen – nicht ob der fertige Code schon funktioniert.