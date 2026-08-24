# Policy as Code und Guardrails

## Zweck

Policy as Code macht Regeln maschinenlesbar und automatisierbar. Die Regel kann Security, Compliance, Kosten, Naming, Architekturkonventionen oder andere Organisationsziele betreffen.

## Trennung

```text
Fach-/Security-Policy
→ Was ist erlaubt oder verboten?

Policy Enforcement
→ Wo, wann und wie wird diese Entscheidung technisch erzwungen?
```

Infrastructure/DevOps besitzt vor allem die zweite Frage.

## Enforcement-Modi

Je nach Risiko:

- advisory / informational;
- audit;
- warn;
- blocking/enforce.

Keine universelle Pflicht, jede Policy sofort blockierend zu machen.

## Enforcement-Punkte

Mögliche Stellen:

- lokal/pre-commit;
- Pull Request / CI;
- Plan/Preview;
- Admission;
- Deployment/Promotion;
- Runtime/Reconciliation.

## Policy Failure

Definieren:

- fail-open vs. fail-closed;
- Ausnahmen/Break-glass;
- Owner;
- Evidence;
- Versionierung;
- Umgang mit Policy-Engine-Ausfall.

## Security-Grenze

Security Policies selbst, Threat Models und Angriffsrisiken bleiben `Sicherheit/`. OPA, Gatekeeper, Kyverno, Sentinel oder Cloud Policies sind technische Adapter.

## Leitgedanke

> Automatisierte Policy ist ein Gate. Ihre Existenz beweist weder die Richtigkeit der Policy noch die Sicherheit des Gesamtsystems.