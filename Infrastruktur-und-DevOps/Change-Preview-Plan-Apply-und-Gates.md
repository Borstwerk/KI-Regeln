# Change Preview, Plan, Apply und Gates

## Grundsatz

Eine belastbare Preview macht geplante Wirkung sichtbar, bevor Außenwirkung entsteht.

Beispiele:

- Terraform/OpenTofu Plan;
- CloudFormation Change Set;
- Pulumi Preview;
- `kubectl diff`;
- Ansible Check/Diff Mode;
- gerenderte Manifeste oder Policy-Diffs.

Die Aussagekraft unterscheidet sich je Tool.

## Preview ≠ Garantie

Eine Preview kann unvollständig oder veraltet sein durch:

- unbekannte Werte;
- Runtime-/Providerverhalten;
- nicht unterstützte Dry-Run-Pfade;
- parallele Änderungen;
- Drift zwischen Preview und Apply;
- externe Controller.

Deshalb Previewqualität und Zeitpunkt transparent machen.

## Review-Achsen

Vor realer Änderung prüfen:

- create / update / replace / delete;
- unerwartete Änderungen;
- Blast Radius;
- Stateful Resources;
- Identity/Network/Permission-Effekte;
- Provider-/Region-/Environment-Ziel;
- Abhängigkeiten;
- Rollout-/Recoveryfähigkeit;
- sensible Outputs/Artefakte;
- Policy-/Security-Funde.

## Autorisierung

```text
Plan erstellt
≠ Plan geprüft
≠ Apply autorisiert
```

Eine Freigabe für Review oder Commit autorisiert keinen Deploy, sofern lokale Regeln diese Gates trennen.

## Fresh Preview

Wenn zwischen Review und Apply relevante Änderungen an Code, Inputs, State oder Actual State auftreten, alte Preview nicht als unveränderte Evidence behandeln.

## Destructive Changes

Destroy, Replacement statefuler Ressourcen, Prune und Recovery benötigen erhöhte Review- und Gate-Strenge.

## Leitgedanke

> Prüfe die geplante Wirkung so spät wie nötig und autorisiere die reale Wirkung so eng wie möglich.