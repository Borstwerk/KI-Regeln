# GitOps und Continuous Reconciliation

## Warum eigener Schnitt

GitOps verändert das Autorisierungsmodell: Ein Controller vergleicht dauerhaft Desired und Actual State und kann selbstständig korrigieren.

OpenGitOps beschreibt als Kernprinzipien unter anderem deklarative, versionierte/immutable Desired States, automatisches Pulling und kontinuierliche Reconciliation.

## Desired-State-Commit als wirksame Aktion

In einem automatisch reconcilierten Produktionsrepository kann ein Commit oder Merge faktisch die spätere Produktionsänderung autorisieren.

Deshalb lokale Gates nicht nur auf den Controller-Apply legen, wenn der Controller danach autonom handelt.

## Prüfachsen

- Repository-/Source Ownership;
- Branch-/Merge-Gates;
- Controller-Rechte;
- Zielcluster/-umgebung;
- Sync-/Reconcile-Modus;
- Prune;
- Self-Heal;
- Drift-/Ignore-Regeln;
- Reihenfolge/Abhängigkeiten;
- Secrets;
- Render-/Schema-/Policy-Validation;
- Rollback-/Revert-Pfad.

## Revert ≠ sofortiger Rollback

Ein Git-Revert wirkt erst nach erneuter Reconciliation und kann irreversible Nebeneffekte nicht zurückdrehen.

## Pull vs. Push

GitOps bevorzugt Pull/Reconciliation als Modell. Nicht jede deklarative Pipeline ist automatisch GitOps.

## Tooladapter

Flux und Argo CD sind wichtige Implementierungen. Ihre CRDs, Syncoptionen und Sicherheitsmodelle bleiben projektspezifisch.

## Leitgedanke

> Continuous Reconciliation ist dauerhafte Änderungsautorität – nicht bloß ein bequemes Deployskript.