---
name: requirements-review
description: Auditiert ein Requirements-Paket unabhängig auf Sources, Stakeholder-/Goal-Fit, Scope, Requirement-Qualität, Acceptance, Traceability, Change-/Lifecycle-Status, Konflikte und Readiness. Verwenden für breite Requirements-/Specification- oder Handoff-Reviews. Nicht als Autor, Product-Approval, Architektur- oder Implementierungsskill verwenden.
---

# Requirements Review

## Ziel

Systemische Lücken, widersprüchliche Aussagen, unbelegte Annahmen und Downstream-Risiken vor dem nächsten lokalen Gate unabhängig sichtbar machen.

## Eingaben

- Review-Scope und beabsichtigter Handoff;
- Requirements-Paket / Baseline;
- Stakeholder-/Source-/Goal-Evidence;
- Scope, Constraints, Annahmen und Non-Goals;
- Acceptance-/Verification-Intent;
- Traceability und Change-/Statusinformation;
- relevante Fachartefakte, soweit für Reviewclaims erforderlich.

## Prüfachsen

1. Source-/Stakeholder-/Goal-Coverage;
2. Scope / Non-Goals / Dependencies;
3. Functional Requirements und relevante Szenarien;
4. Qualitätsanforderungen und bestätigte Zielwerte;
5. Constraints vs. unbegründete Lösungsvorgaben;
6. Requirement-Qualität und Terminologie;
7. Acceptance Criteria / Verification Intent;
8. Traceability / Provenance / Orphans;
9. Konflikte, Annahmen und Missing Evidence;
10. Status, Baseline, Supersession und Change-Impact;
11. Downstream-Handoff zu Architecture, Interfaces, Data, Security, Reliability und Testing;
12. Readiness für das lokale nächste Gate.

## Evidence Status

- `CONFIRMED`
- `INFERRED`
- `UNVERIFIED`
- `CONFLICTING`
- `SUPERSEDED`

## Verdict

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_GAPS`
- `BLOCKED`
- `UNVERIFIED`

Das Verdict autorisiert keine Stakeholderfreigabe, Architekturentscheidung, Implementierung, Merge, Deployment oder Release.

## Stop-/Übergaberegeln

- offene Fachbegriffe/Invarianten → `domain-modeling`;
- strukturelle Lösung → `system-design`;
- konkrete API/Event-Verträge → Interface-Skills;
- konkrete Teststrategie/-fälle → Testing und QA;
- Reliability-Mess-/Betriebsmodell → Reliability;
- Security Controls/Threats → Sicherheit;
- Dokumentlayout/-stil → Dokumentationserstellung.

## Nicht tun

- Requirements während unabhängigem Review ungefragt umschreiben;
- Pattern-/Toolpräferenz als Requirement-Lücke deklarieren;
- unbekannte Stakeholderziele oder Schwellen ergänzen;
- 100 Prozent Traceability oder volle Template-Belegung als Ready-Beweis verwenden;
- Product Validation oder Testausführung behaupten, wenn nur Requirements-Evidence vorliegt;
- Review-Verdict als Ausführungsautorisierung behandeln.

## Ausgabe

```text
Scope / Handoff Purpose / Evidence
Findings [priority, evidence status, impact]
Source / Stakeholder / Goal Gaps
Scope / Functional / Quality Findings
Acceptance / Traceability Findings
Conflicts / Assumptions / Lifecycle Findings
Required Handoffs
Missing Evidence
Verdict
```

## Related

- `requirements-baseline`
- `requirements-elicitation`
- `requirements-specification`
- `acceptance-criteria-design`
- `requirements-traceability`
- `requirements-change-analysis`
- `requirements-validation`
- `architecture-review`
- `test-suite-review`

## Leitgedanke

> Ein guter Requirements Review prüft die Grundlage für Entscheidungen – nicht die Schönheit des Dokuments.