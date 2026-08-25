#!/usr/bin/env python3
from pathlib import Path


def insert_once(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if block.strip().splitlines()[0] in text:
        print(f"already updated: {path}")
        return
    if text.count(marker) != 1:
        raise SystemExit(f"expected one marker in {path}: {marker!r}")
    path.write_text(text.replace(marker, block + "\n\n" + marker, 1), encoding="utf-8")


evals_block = '''## Hardening Phase 2 – Coverage und Golden Tasks

Der reproduzierbare Coverage-Audit unter `../tools/eval_coverage_audit.py` meldet für den Phase-2-Stand:

- 128 katalogisierte Skills;
- 100 Evalpacks;
- 489 definierte Skill-Cases;
- Eval Coverage: 100× `partial`, 28× `none`;
- 28 Skills ohne formales Evalpack;
- 65 vorhandene Packs mit mindestens einem heuristischen One-Sided-Signal.

Die One-Sided-Signale sind Review-Hinweise und keine Pass-/Fail-Regeln. Insbesondere ist ein fehlender `blocked`-Fall nicht automatisch ein Defekt, wenn ein Skill kein sinnvolles External-Action-Gate besitzt.

Phase 2 ergänzt gezielt elf systemisch wirksame Evalpacks mit je fünf Fällen, insgesamt 55 neue Cases: `task-graph`, `verification-loop`, `delegation-contract`, `agent-eval`, `docs-plan`, `technical-writing`, `reference-docs`, `web-search`, `research-plan`, `claim-verification` und `skill-review`. Diese Skills wechseln dadurch ausschließlich von `none` auf `partial`; Maturity bleibt unverändert. Die Priorisierung ist in `Coverage-Audit-2026-08-25.md` dokumentiert.

Zusätzlich besteht unter `Golden-Tasks/` eine getrennte systemweite Suite mit acht lokalen, reproduzierbaren End-to-End-Aufgaben (`GT-01` bis `GT-08`). Der Repo-Validator prüft deren Struktur, nicht das Modellverhalten.

Für Behavioral-Smokes wird eine Execution View reproduzierbar aus `task.yml` projiziert. Der Runner sieht Auftrag, Fixtures, Sources of Truth und Capability-Setup, aber keine Routing-/Skill-Erwartungen, Statusvorgaben, Forbidden-Kriterien oder Rubrik. Erst anschließend bewertet die Judge View gegen die vollständige Taskdefinition. Details stehen in `Golden-Tasks/README.md`.

`GT-04` erwartet bewusst `partial`, weil die Fixture keine bestätigte Root Cause beweist. Dieser Status ist dort epistemisch korrektes Zielverhalten, kein automatischer Golden-Task-Fehlschlag.

Die Existenz der 55 neuen Skill-Cases und acht Golden Tasks ist kein Behavioral-Pass-Nachweis. Ausgeführte Smokes werden separat dokumentiert.'''

catalog_block = '''## Hardening Phase 2 – Eval Coverage

Der reproduzierbare Coverage-Audit für Phase 2 ergibt aktuell:

- 128 Skills insgesamt;
- 100 Skills mit `partial` Eval Coverage;
- 28 Skills mit `none`;
- 0 Skills mit `core` oder `broad`;
- 100 Evalpacks mit insgesamt 489 definierten Skill-Cases.

Gegenüber dem Ausgangsstand `07b4907c9599ac0515f48afdb2d4cda64dd40b15` wurden elf systemisch wirksame Skills gezielt von `none` auf `partial` gebracht: `task-graph`, `verification-loop`, `delegation-contract`, `agent-eval`, `docs-plan`, `technical-writing`, `reference-docs`, `web-search`, `research-plan`, `claim-verification` und `skill-review`. Dafür wurden 55 passende Cases angelegt. Keine Maturity wurde verändert.

Die Auswahl folgt dem systemischen Hebel auf Routing, Evidence, Completion Claims, Dokumentation, Recherche und Skill-Review; andere Skills mit `none` wurden nicht allein aus Vollständigkeitsdogma aufgenommen. Details stehen in `../Evals/Coverage-Audit-2026-08-25.md`.

Die acht Golden Tasks unter `../Evals/Golden-Tasks/` ergänzen Skill-Evals um systemweite Aufgaben. Ihre Definition und strukturelle Validität sind kein Beweis für Behavioral-Erfolg und keine Grundlage für eine automatische Maturity-Hochstufung.'''

insert_once(Path("Evals/README.md"), "## Fallstruktur", evals_block)
insert_once(Path("Dokumentation/Skill-Katalog.md"), "## Capabilities", catalog_block)
