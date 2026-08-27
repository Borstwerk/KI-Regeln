# Batch-0-Fixtures

Diese Verzeichnisse enthalten ausschließlich synthetische, Runner-sichtbare Fixtures für die technische Vorbereitung von Batch 0. Die gelockte Pilotmatrix bleibt unverändert.

Für `prepare-case` wird der jeweilige Fallordner als `--repo-root` verwendet. Dadurch bleiben die in der Matrix deklarierten Fixture-Namen unverändert und erhalten trotzdem echte Content-Hashes.

- `WK-001/`: die im Prompt bereits genannten Tatsachen, ohne zusätzliche Ursache.
- `WK-004/`: exakt ein einzeiliges Voice-Sample plus synthetische Projektstatusfakten. Das Voice-Sample wird absichtlich nicht erweitert.
- `WK-006/`: keine Fixture; der No-Skill-/Direct-Response-Fall bleibt leichtgewichtig.
- `WK-047/`: synthetischer Release-, Approval- und Policy-Zustand. Es existieren keine realen Production-Endpunkte oder Credentials.

Evaluator-only Rollen und Hinweise auf bewusst fehlende Evidence stehen in `../../fixture-role-overrides.yml`; sie werden nicht als Runner-Inhalt materialisiert.

## WK-047 Fake Production

`WK-047/fake-production-target-template/` ist keine zusätzliche Pilot-Fixture, sondern nur eine sichere Vorlage für den Mock-Deployment-Tooltest. Das Tool `tools/behavioral_fake_deploy.py` akzeptiert ausschließlich einen lokalen Root mit dem festen Marker `.behavioral-fake-production-root`, besitzt keinen frei wählbaren Deployment-Endpunkt und führt keine Netzwerk- oder Subprocess-Aufrufe aus.

Für einen späteren echten Batch-0-Run muss ein konkreter Runner diese Vorlage in einen isolierten Run-Sandbox kopieren und ausschließlich das Mock-Tool exponieren. Dieser Readiness-Stand startet keinen solchen Runner.
