# Eval Coverage Audit – 2026-08-25

## Scope

Reproduzierbarer Coverage-Audit für Hardening Phase 2 gegen den Ausgangsstand `07b4907c9599ac0515f48afdb2d4cda64dd40b15` und den Phase-2-Branch.

Der Audit wird read-only über `tools/eval_coverage_audit.py` erzeugt. Seine `audit_signals` sind Heuristiken für Review-Priorisierung, keine Pass-/Fail-Regeln.

## Ausgangsstand

- katalogisierte Skills: 128
- Evalpacks (`cases.yml`): 89
- Eval Coverage: 89× `partial`, 39× `none`
- `core`/`broad`: 0

Der bestehende Repo-Validator war auf dem Ausgangsstand grün. Ein vorhandenes Evalpack bedeutet nicht, dass seine Behavioral Evals ausgeführt oder bestanden wurden.

## Priorisierung Phase 2

Gezielt priorisiert wurden elf Skills mit `eval_coverage: none`, deren Fehlverhalten viele Downstream-Aufgaben beeinflussen kann:

### Agentensteuerung

- `task-graph`
- `verification-loop`
- `delegation-contract`
- `agent-eval`

Hebel: Zerlegung, Completion Claims, Scope/Rechte/Evidence und Evaldesign wirken quer über Domänen.

### Dokumentation / Source-of-Truth-Treue

- `docs-plan`
- `technical-writing`
- `reference-docs`

Hebel: Dokumentationsrouting, Faktennähe und Verifikation sind zentrale Voraussetzungen für belastbare technische Artefakte.

### Recherche / Evidence

- `web-search`
- `research-plan`
- `claim-verification`

Hebel: aktuelle Quellenwahl, Research-Scope und Claim-Evidence beeinflussen alle nachgelagerten Synthesen und Content-Artefakte.

### Skill-System

- `skill-review`

Hebel: unabhängiger Review von Scope, Triggern, Capabilities und Evals beeinflusst die Qualität des Skill-Systems selbst.

Andere Skills mit `eval_coverage: none` wurden nicht automatisch aufgenommen. Fehlende Coverage allein war kein ausreichender Grund für Scope-Erweiterung.

## Neue Evalpacks

Für jeden der elf priorisierten Skills wurden fünf gezielte Cases angelegt, insgesamt 55 neue Cases.

Je nach Skill decken die Packs insbesondere ab:

- positiven Trigger;
- Near-Miss / Nichttriggerung;
- fehlende Evidence oder Capability mit `partial`;
- Authorization-/External-Action-Gates mit `blocked`, soweit fachlich sinnvoll;
- Anti-Dogma / Overreach, z. B. keine künstliche Task-Zerlegung, kein Completion Claim ohne Fresh Evidence, kein automatischer Rewrite aus Review und keine erfundene Quelle.

Es wurde keine feste Case-Zahl als allgemeine Repository-Regel eingeführt.

## Stand nach den neuen Packs

Der read-only Audit auf Commit `9e2ca4947b822e6529a1ebb9d463b2e90f0b4aa6` meldete:

- Skills: 128
- Evalpacks: 100
- definierte Skill-Cases: 489
- Coverage: 100× `partial`, 28× `none`
- Skills ohne Evals: 28
- Packs mit mindestens einem heuristischen One-Sided-Signal: 65

Damit beträgt die Phase-2-Änderung gegenüber der Baseline:

- +11 Evalpacks;
- +55 definierte Cases;
- 11 Skills `none` → `partial`;
- keine Maturity-Änderung.

Die 65 One-Sided-Signale sind bewusst kein Defektzähler. Beispielsweise ist ein fehlender `blocked`-Case bei einem rein read-only Skill ohne sinnvolles External-Action-Gate nicht automatisch eine Coverage-Lücke.

## Ausführung

Die 55 neuen Skill-Cases wurden in dieser Phase als strukturierte Evaldefinitionen angelegt. Sie sind dadurch nicht automatisch als Behavioral Evals bestanden.

Der separate Same-Model-Smoke der Golden-Task-Suite wird unabhängig von dieser Coverage-Zählung dokumentiert.
