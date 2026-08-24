---
name: contract-change-review
description: Prüft eine geplante oder tatsächliche Schnittstellenänderung gegen Baseline, Consumer und Source-, Wire- sowie semantische Kompatibilität. Verwenden bei Schema-, API-, Event-, GraphQL-, Protobuf-, Default-, Pagination-, Error- oder Deprecation-Änderungen. Nicht als Contract-Testausführung verwenden.
---

# Contract Change Review

## Ziel

Änderungen klassifizieren, bevor stille Breaking Changes Consumer erreichen.

## Eingaben

- bisheriger kanonischer Contract;
- neuer/geplanter Contract oder Diff;
- bekannte Consumer und Deploymentmodell;
- lokale Compatibility-/Versionierungs-Policy;
- relevante Tool-Diffs, falls vorhanden;
- reale Nutzungs-/Telemetry-Evidence, falls verfügbar.

## Arbeitsweise

1. Baseline und Zielstand eindeutig bestimmen.
2. strukturellen Contract Diff ermitteln.
3. betroffene Consumer und deren Upgrade-/Deploymentfreiheit bestimmen.
4. Source Compatibility prüfen.
5. Wire Compatibility prüfen.
6. Semantic Compatibility prüfen: Bedeutung, Defaults, Ordering, Pagination, Errors, unbekannte Werte, Auth, Retry und Timing soweit relevant.
7. rolloutabhängige Änderungen separat markieren.
8. Verdict vergeben: `COMPATIBLE`, `ROLLOUT-SENSITIVE`, `BREAKING` oder `UNVERIFIED`.
9. bei Breaking/rollout-sensitive Migration, Deprecation, Reihenfolge und Gate benennen.
10. passende Contract-/Integrationstests als Evidence-Anforderung ableiten.

## Toolregel

Schema-Diff-, Buf-, OpenAPI- oder andere Compatibility-Tools liefern Evidence, aber kein vollständiges semantisches Urteil.

## Nicht tun

- `additive` automatisch mit `compatible` gleichsetzen;
- unbekannte Consumer als „keine Consumer“ behandeln;
- Wire Compatibility als Source Compatibility ausgeben;
- fehlende Baseline mit geratenem Altvertrag ersetzen;
- Breaking Change ohne Migration/Gate freigeben.

## Ausgabe

```text
Baseline
Target
Contract Diff
Affected Consumers
Source Compatibility
Wire Compatibility
Semantic Compatibility
Rollout Conditions
Verdict
Migration / Deprecation
Required Evidence
```

## Related

- `interface-design`
- `http-api-design`
- `event-contract-design`
- `contract-testing`
- `interface-review`