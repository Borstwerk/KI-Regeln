# Workflow: Requirements Readiness Review

## Ziel

Ein Requirements-Paket vor einem lokalen Architecture-, Delivery- oder anderen Handoff-Gate unabhängig auf fachliche Tragfähigkeit, Evidence und offene Risiken prüfen.

## Ablauf

```text
1. Review Scope / Handoff Purpose
→ 2. requirements-baseline
→ 3. requirements-validation
→ 4. requirements-traceability
→ 5. unabhängiger requirements-review
→ 6. Findings / Missing Evidence / Conflicts
→ 7. lokales Approval-/Handoff-Gate außerhalb dieses Workflows
```

## Skills

- `requirements-baseline`
- `requirements-validation`
- `requirements-traceability`
- `requirements-review`

Bei Bedarf:

- `domain-modeling`;
- Security-/Interface-/Reliability-/Data-Skills für tiefe Fachfragen;
- `docs-review` nur für Darstellungsqualität.

## Verdicts

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_GAPS`
- `BLOCKED`
- `UNVERIFIED`

## Wichtige Grenze

`READY_FOR_LOCAL_GATE` sagt nur, dass der geprüfte Requirements-Stand ausreichend Evidence für die lokale nächste Entscheidung besitzt. Es ist keine Stakeholderfreigabe und keine Architektur-, Implementierungs-, Merge-, Deployment- oder Releaseautorisierung.

## Leitgedanke

> Readiness ist ein Evidence-Urteil über die Grundlage – die Entscheidung bleibt beim zuständigen lokalen Gate.