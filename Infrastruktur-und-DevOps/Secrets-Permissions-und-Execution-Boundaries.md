# Secrets, Permissions und Execution Boundaries

## Grundsatz

Automationsjobs und Controller sollen nur die Rechte besitzen, die ihr konkreter Schritt benötigt.

## Trennen

Wo möglich separate Identitäten für:

- Read/Validate;
- Build;
- Plan/Preview;
- Deploy/Apply;
- destructive/recovery Aktionen.

Ein Planjob braucht nicht automatisch Destroy-Rechte.

## Secrets

Secrets:

- nicht im normalen Repository speichern;
- nicht in Logs ausgeben;
- nicht unnötig in Artefakte oder Plans einbetten;
- nur an Jobs/Environments liefern, die sie wirklich benötigen;
- bei untrusted Inputs/Forks besonders schützen.

## Execution Boundary

Vor realen Aktionen klären:

- Zielaccount/-subscription/-cluster;
- Region;
- Environment;
- Namespace/Project;
- verwendete Identität;
- erlaubter Ressourcenscope.

## State und Planfiles

IaC-State und gespeicherte Plan-/Preview-Artefakte können Secretmaterial oder sensitive Infrastrukturdetails enthalten. Schutzbedarf unabhängig vom Dateinamen prüfen.

## Break Glass

Notfallrechte können nötig sein, müssen aber zeitlich, personell und auditierbar begrenzt werden. Ein fehlgeschlagener Automationsschritt autorisiert kein automatisches Hochstufen auf mächtigere Credentials.

## Security-Grenze

Detaillierte IAM-Modelle, Secret-Rotation, Workload Identity, Supply-Chain-Signing und Angriffsschutz gehören in `Sicherheit/`.

## Leitgedanke

> Automationsreichweite ist Teil des Blast Radius.