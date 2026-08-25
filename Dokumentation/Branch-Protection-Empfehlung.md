# Branch-Protection-Empfehlung für einen später öffentlichen Stand

Stand: 2026-08-25

Diese Datei dokumentiert nur die Empfehlung. Phase 3 ändert **keine** Repository- oder Branch-Protection-Einstellungen.

## Empfohlene Baseline für `main`

- Änderungen an `main` grundsätzlich über Pull Requests.
- `Repo validation` als Required Status Check.
- Force Push für `main` deaktivieren.
- Branch-Löschung für `main` deaktivieren.
- Mindestens ein Review für normale Änderungen, sofern das Team organisatorisch mehr als eine verfügbare Reviewperson hat.
- Stale Approvals nur dann automatisch verwerfen, wenn das Team die zusätzliche Reviewlast bewusst tragen will; kein Default aus Prinzip.
- Maintainer/Admins sollten Schutzregeln im Normalbetrieb ebenfalls respektieren. Ein dokumentierter Break-Glass-Weg darf für echte Recovery-Fälle bestehen, sollte aber Ausnahme statt Arbeitsweise sein.

## Warum nicht mehr Regeln?

Das Repository braucht eine überprüfbare Integrationsgrenze, aber keine Governance um ihrer selbst willen. Zusätzliche Regeln wie mehrere Pflichtreviewer, signierte Commits, lineare Historie oder Deployment-Gates sollten nur eingeführt werden, wenn reale Team- oder Risikogründe sie tragen.

## Public-Release-Gate

Vor einer tatsächlichen Veröffentlichung sollte geprüft werden, dass:

1. der Required Status Check auf den aktuellen Workflow-Namen zeigt;
2. Pull Requests aus Forks den read-only Validator ohne Secrets sicher ausführen können;
3. die gewählte Reviewregel zur realen Teamgröße passt;
4. kein automatisches Merge ungeprüfter Dependency-PRs aktiviert ist.
