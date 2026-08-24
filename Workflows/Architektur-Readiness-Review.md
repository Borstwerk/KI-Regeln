# Workflow: Architektur-Readiness-Review

## Ziel

Ein Systemdesign oder eine größere Architekturänderung vor lokalem Umsetzungs-/Release-Gate unabhängig auf strukturelle Vollständigkeit, Risiken und Evidence prüfen.

## Ablauf

```text
1. Scope / gültige Requirements
→ 2. Architecture Baseline / Zielbild
→ 3. Conformance / Drift
→ 4. kritische Fachhandoffs
→ 5. unabhängiger Architecture Review
→ 6. Findings / Missing Evidence
→ 7. lokales Gate außerhalb dieses Workflows
```

## Skills

- `architecture-baseline` – aktuelle Struktur und Evidence;
- `architecture-conformance-review` – Soll/Ist und Fitness Functions;
- `architecture-review` – breiter unabhängiger Schlussaudit;
- bei Bedarf: `reliability-review`, `infrastructure-review`, `interface-review`, `database-review`, `data-engineering-review`, `test-suite-review`.

## Verdicts

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_FINDINGS`
- `BLOCKED`
- `UNVERIFIED`

## Regeln

- Repo- und Dokumentationsgrün ist kein Ersatz für erforderliche Runtime-/Behavior-Evidence.
- Patternreinheit ist kein Readiness-Kriterium.
- Findings werden nicht aus dem Review heraus implementiert.
- `READY_FOR_LOCAL_GATE` bedeutet ausdrücklich nicht Deploy-, Merge-, Migration- oder Releasefreigabe.

## Ergebnis

Priorisierte Findings, Evidence-Status, notwendige Fachhandoffs und ein klar abgegrenztes Readiness-Verdict.