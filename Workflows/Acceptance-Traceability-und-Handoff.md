# Workflow: Acceptance, Traceability und Handoff

## Ziel

Ein bestehendes Requirement-Set für Design, Testing oder andere Downstream-Disziplinen so vorbereiten, dass Erfüllungsabsicht, Herkunft und relevante Abhängigkeiten nachvollziehbar sind.

## Ablauf

```text
1. bestätigte Requirements / Scope
→ 2. acceptance-criteria-design
→ 3. Verification Intent
→ 4. requirements-traceability
→ 5. Coverage / Orphans / Missing Evidence
→ 6. requirements-validation
→ 7. lokaler Handoff
```

## Skills

- `acceptance-criteria-design`
- `requirements-traceability`
- `requirements-validation`

Danach je nach Ziel:

- Architecture → `system-design`;
- Testing → `test-strategy` / `test-design`;
- Interface → `interface-design`;
- Reliability → `slo-design` oder passende Reliability-Skills.

## Grenzen

```text
Acceptance Criterion
≠ Test Case

Traceability Coverage
≠ Requirement Correctness

Requirements Handoff
≠ Downstream Execution Authorization
```

## Leitgedanke

> Der Empfänger soll wissen, was gelten soll, warum es gilt und welche Unsicherheit noch übrig ist.