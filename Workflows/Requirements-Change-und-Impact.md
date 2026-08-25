# Workflow: Requirements Change und Impact

## Ziel

Eine relevante Änderung an bestehenden oder baselinierten Requirements kontrolliert analysieren, entscheiden und für Downstream-Änderungen vorbereiten.

## Ablauf

```text
1. requirements-baseline
→ 2. Change Source / Rationale
→ 3. requirements-change-analysis
→ 4. requirements-traceability / Downstream Impact
→ 5. bei Bedarf erneute Elicitation / Specification
→ 6. requirements-validation
→ 7. lokales Change-/Approval-Gate
→ 8. autorisierte Downstream-Prozesse
```

## Skills

- `requirements-baseline`
- `requirements-change-analysis`
- `requirements-traceability`
- `requirements-validation`

Optional:

- `requirements-elicitation`
- `requirements-specification`
- `acceptance-criteria-design`

## Downstream-Handoffs

Je nach Impact unter anderem:

- `architecture-evolution`;
- `contract-change-review`;
- `schema-migration`;
- Data-Engineering-Skills;
- Reliability-Skills;
- Testing-und-QA.

## Gate

```text
Change Analysis
≠ Change Approval

Requirement Approval
≠ Implementierungs-/Deploy-Autorisierung
```

## Leitgedanke

> Requirement Changes zuerst als Bedeutungs- und Impactänderung behandeln, erst danach als Codeänderung.