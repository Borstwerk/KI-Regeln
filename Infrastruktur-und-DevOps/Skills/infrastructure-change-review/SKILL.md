---
name: infrastructure-change-review
description: Prüft einen Infrastruktur-Plan, Diff, Change Set oder andere Preview gegen Desired State, Actual State, Blast Radius, Replacement/Destroy, Permissions, State und Recovery. Verwenden vor realen IaC-/Cluster-/Cloud-Änderungen. Nicht als Apply- oder Deploy-Autorisierung verwenden.
---

# Infrastructure Change Review

## Ziel

Die geplante reale Wirkung einer Infrastrukturänderung vor dem Gate nachvollziehbar bewerten.

## Eingaben

- kanonischer Desired State;
- aktuelle Preview / Plan / Diff;
- aktueller State/Actual-State-Kontext;
- Zielumgebung;
- relevante Architektur-, Security- und Recoveryregeln.

## Arbeitsweise

1. Preview-Freshness und Toolaussagekraft bestimmen.
2. Zielaccount/-cluster/-region/-environment bestätigen.
3. create/update/replace/delete klassifizieren.
4. unerwartete Änderungen und Drift markieren.
5. Blast Radius, stateful Ressourcen und Dependencies prüfen.
6. Permission-/Network-/Identity-/Secret-Auswirkungen prüfen.
7. Recovery-/Rollbackpfad und nicht rückgängig machbare Nebenwirkungen prüfen.
8. fehlende Evidence sichtbar machen.
9. Verdict vergeben.

## Verdicts

- `SAFE_TO_PROCEED_TO_GATE`
- `REVIEW_REQUIRED`
- `DESTRUCTIVE`
- `UNVERIFIED`

`SAFE_TO_PROCEED_TO_GATE` bedeutet ausdrücklich nicht `APPLY AUTHORIZED`.

## Nicht tun

- alte Preview nach zwischenzeitlicher Zustandsänderung als frisch ausgeben;
- Replacement statefuler Ressource übersehen;
- fehlenden Actual State erfinden;
- Destroy/Prune/Recovery automatisch ausführen;
- grüne Policychecks als vollständige Freigabe behandeln.

## Ausgabe

```text
Target
Preview Freshness
Change Summary
Replacement / Delete
Blast Radius
State / Drift
Security / Permissions
Recovery
Missing Evidence
Verdict
Required Gate
```

## Related

- `infrastructure-as-code`
- `deployment-strategy`
- `infrastructure-review`
- `verification-loop`