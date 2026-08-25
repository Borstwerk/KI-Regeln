#!/usr/bin/env python3
from pathlib import Path

path = Path('CHANGELOG.md')
text = path.read_text(encoding='utf-8')
marker = '### Hardening Phase 1\n'
heading = '### Hardening Phase 2 – Evals & Golden Tasks'
if heading in text:
    print('changelog already updated')
    raise SystemExit(0)
if text.count(marker) != 1:
    raise SystemExit('expected exactly one Hardening Phase 1 marker')
block = '''### Hardening Phase 2 – Evals & Golden Tasks

- reproduzierbaren read-only Coverage-Audit für alle 128 katalogisierten Skills ergänzt;
- elf systemisch wirksame Eval-Lücken gezielt geschlossen (`task-graph`, `verification-loop`, `delegation-contract`, `agent-eval`, `docs-plan`, `technical-writing`, `reference-docs`, `web-search`, `research-plan`, `claim-verification`, `skill-review`): 11 neue Evalpacks mit 55 definierten Cases; Eval Coverage dadurch 89→100× `partial` und 39→28× `none`, ohne Maturity-Änderung;
- systemweite Golden-Task-Suite mit acht lokalen reproduzierbaren Aufgaben, maschinenlesbarem Schema und struktureller Validatorprüfung ergänzt;
- Execution View und Judge View für Golden Tasks getrennt; evaluator-only Routing-, Status-, Forbidden- und Rubrikfelder werden aus der reproduzierbaren Execution-Projektion ausgeblendet;
- Same-Model-Smoke mit GPT-5.6 Sol über GT-01 bis GT-08 ausgeführt: final 8/8 aligned, davon 7× `pass` und GT-04 erwartungsgemäß `partial`, 0 Forbidden-Verstöße; ausdrücklich `same-model / non-blind / author-contaminated` und daher kein unabhängiger Generalisierungs- oder Routing-Benchmark;
- Smoke-Fund in GT-07 als zu enge Bewertungsrubrik klassifiziert: gerenderter `web-design-review` war ohne Render-Evidence fälschlich Pflicht; ausschließlich evaluator-only Taskdefinition minimal korrigiert und re-judged, kein Fachskill geändert;
- `tools/repo_validator.py` um read-only Strukturprüfung der Golden Tasks erweitert; definierte Cases oder strukturell gültige Golden Tasks werden dadurch nicht als behavioral bestanden behandelt.

'''
path.write_text(text.replace(marker, block + marker, 1), encoding='utf-8')
