# Workflow: Requirements Baseline und Spezifikation

## Ziel

Aus einem bestehenden oder neuen Vorhaben einen belastbaren Requirements-Stand erzeugen, ohne Ist-Verhalten, Stakeholderbedarf und technische Lösung miteinander zu vermischen.

## Ablauf

```text
1. Scope / beabsichtigter Handoff
→ 2. requirements-baseline, falls Bestand existiert
→ 3. requirements-elicitation für relevante Lücken
→ 4. Domain-/Source-Konflikte klären
→ 5. requirements-specification
→ 6. acceptance-criteria-design für kritische Requirements
→ 7. requirements-traceability
→ 8. requirements-validation
→ 9. lokales Approval-/Handoff-Gate
```

## Skills

- `requirements-baseline`
- `requirements-elicitation`
- `requirements-specification`
- `acceptance-criteria-design`
- `requirements-traceability`
- `requirements-validation`

Bei offenen Fachbegriffen/Invarianten: `domain-modeling`.

## Handoff

Ein geeigneter Handoff an Architecture enthält mindestens, soweit relevant:

- Scope / Non-Goals;
- bestätigte funktionale und qualitative Requirements;
- Constraints;
- Ziele/Stakeholder-/Source-Bezug;
- Acceptance-/Verification-Intent;
- Annahmen und offene Gaps;
- Status/Approval-Evidence nach lokaler Policy.

## Gate

`VALIDATED_WITHIN_SCOPE` oder `READY_FOR_LOCAL_GATE` bedeutet nicht automatisch `APPROVED`. Die tatsächliche Freigabe bleibt lokal.

## Leitgedanke

> Erst eine belastbare Sollgrundlage erzeugen, dann Design entscheiden.