# Golden Tasks

Golden Tasks prüfen das Zusammenspiel von Bootstrap, Routing, lokaler Wahrheit, Workflows, Skills, Evidence, Gates und Verification an kleinen reproduzierbaren Aufgaben.

Sie sind **keine normalen Skill-Evals**. Skill-Evals prüfen eine einzelne Arbeitsdisziplin möglichst gezielt; Golden Tasks prüfen, ob ein Agent bei einer realistischen End-to-End-Aufgabe einen kleinen ausreichenden fachlichen Pfad findet und die Grenzen zwischen Disziplinen einhält.

## Struktur

- `golden-task.schema.json` – maschinenlesbares Format der vollständigen Judge View;
- `suite.yml` – Index der zur Suite gehörenden Tasks;
- `GT-XX/task.yml` – vollständige Taskdefinition inklusive evaluator-only Erwartungen;
- weitere Dateien im jeweiligen `GT-XX/`-Ordner – lokale, selbst erzeugte Fixtures.

Der Repo-Validator prüft nur die Struktur: Schema, IDs, Pfade, Skill-/Workflowreferenzen und widerspruchsfreie Skillmengen. Er bewertet ausdrücklich nicht, ob ein Modell einen Golden Task behaviorally bestanden hat.

## Routing ohne Prompt-Skript

Eine vollständige Task kann definieren:

- `required_skills` für unverzichtbare Arbeitsdisziplinen;
- `allowed_optional_skills` für legitime zusätzliche Disziplinen;
- `forbidden_skills` nur für offensichtlich falsches oder scope-erweiterndes Routing;
- einen oder mehrere zulässige Workflows, sofern ein Workflow sinnvoll ist.

Ein Agent muss daher nicht exakt eine vorgegebene interne Skillkette reproduzieren. Bewertet wird das beobachtbare Verhalten.

## Execution View und Judge View

Behavioral-Smokes trennen zwei Sichten.

### Execution View

Der ausführende Agent erhält in der direkten Golden-Task-Projektion nur:

- `schema_version`;
- `assignment`;
- `fixtures`;
- `required_capabilities`.

`id`, `title`, `goal` und `sources_of_truth` bleiben aus der Runner-View heraus. Diese Felder sind fachlich nützlich für Autoren/Judges, können aber in natürlicher Sprache bereits die erwartete Route, einen Skillnamen oder die gewünschte Testeigenschaft verraten.

Die Projektion wird reproduzierbar erzeugt mit:

```bash
python tools/golden_task_execution_view.py Evals/Golden-Tasks/GT-01/task.yml --assert-blind
```

Nicht in die Execution View gelangen insbesondere:

- `id`, `title`, `goal`, `sources_of_truth`;
- `expected_domain`;
- `allowed_secondary_domains`;
- `workflow`;
- `required_skills`;
- `allowed_optional_skills`;
- `forbidden_skills`;
- `expected_evidence`;
- `expected_artifacts`;
- `expected_verification`;
- `allowed_uncertainty`;
- `expected_status`;
- `forbidden_behaviors`;
- `rubric`.

Der Runner soll über normale KI-Regeln, `AGENTS.md`, lokale Sources of Truth und den Repository-Router selbst zu einem fachlich sinnvollen Weg kommen.

### Blindes Runner-Paket

Für echte Behavioral Runs reicht eine YAML-Projektion allein nicht. Der Runner darf auch nicht durch rekursive Dateisuche auf `Evals/**`, alte Runberichte, Changelog-Einträge oder evaluator-nahe Metadokumente stoßen.

Dafür baut `tools/golden_task_behavioral_harness.py` ein vorbereitetes Paket auf Basis des vorhandenen Behavioral Harness:

```bash
python tools/golden_task_behavioral_harness.py prepare-case \
  Evals/Golden-Tasks/GT-09/task.yml \
  --repo-commit <commit-sha> \
  --out <temp-dir>/GT-09
```

Das Runner-Paket enthält:

- die Assignment als `user_prompt`;
- Fixtures unter neutralen Pfaden wie `workspace/task/fixture-01-options.md`;
- `workspace/repository/AGENTS.md`, Katalog, Overlay-Registry, Workflow-Index und die operativen Domain-/Skill-/Workflow-Dateien;
- **nicht**: `Evals/**`, `.git/**`, `.github/**`, `tests/**`, `tools/**`, Root-Changelog/README sowie bekannte eval-beschreibende Metadokumente.

Der Workspace wird dateiweise gehasht. `verify_prepared_integrity` lehnt einen vor dem Run veränderten Runner-Workspace ab.

Der vorhandene Claude-Code-Adapter kann aus erfolgreichen `Read`-Toolereignissen objektive `skill_events: read` und `workflow_events: read` erzeugen. Er leitet daraus **nicht** `selected`, `applied`, `CANDIDATE_REJECTED`, Refinement oder Checkpoint-Reihenfolge ab.

### Judge View

Erst nach der Task-Ausführung wird die vollständige `task.yml` inklusive evaluator-only Feldern zur Bewertung herangezogen.

## Bewertungsachsen

Jede Task besitzt eine dimensionale Rubrik für:

- Routing;
- Grounding;
- Scope;
- Gates;
- Verification;
- Ergebnisqualität.

Es gibt keine opaque Gesamtnote. Findings bleiben pro Dimension sichtbar.

## Suite v1

- `GT-01` – Datenbanktabelle dokumentieren;
- `GT-02` – Code-/PR-Review;
- `GT-03` – Requirements → Interface Contract;
- `GT-04` – Incidentanalyse mit absichtlich unvollständiger Root-Cause-Evidence;
- `GT-05` – Requirement Change / Impact;
- `GT-06` – Datenmigration / Backfill planen;
- `GT-07` – Web-Qualitätsreview;
- `GT-08` – Research → Social Content;
- `GT-09` – Architekturtradeoff mit automatisch entdecktem `visual-answer`;
- `GT-10` – No-Skill-Control für eine einfache stabile Faktenfrage;
- `GT-11` – Communication-Overlay verfeinert den Primärowner statt Rewrite-Bloat zu addieren;
- `GT-12` – später `citation-audit` am Pre-Completion-Checkpoint;
- `GT-13` – frische Completion-Evidence nach einer kleinen Korrektur, ohne Loop-Pflicht (testet die allgemeine Completion-Regel, nicht die Aktivierung von `verification-loop`);
- `GT-14` – Security-Admission mit Deduplizierung von `tool-permission-review`;
- `GT-15` – zweite No-Skill-Control: lokale Kurz-Zusammenfassung trotz Fixture;
- `GT-16` – Add-Zweig: `adressatengerechte-kommunikation + natuerliches-schreiben` bei eigenständiger Voice-Evidence;
- `GT-17` – positiver `tool-permission-review`-Fall ohne Skill-Bundle.

Golden Tasks dürfen bewusst `required_skills: []`, leere Fixtures/Sources und `expected_domain: none` verwenden, wenn ein **No-Skill-Routing** das gewünschte Verhalten ist. Das ist ein Regressionstest gegen Skill-Bloat, kein unvollständiger Task.

Alle Fixtures sind lokal und selbst erzeugt. Die Suite hängt nicht von aktuellen Webseiten, Social-Trends oder ungepinnten Repositories ab.

`GT-04` erwartet bewusst `partial`: Die Fixture reicht für belastbare Fakten, Hypothesen und nächste Diagnose, aber nicht für eine bestätigte Root Cause.

`GT-14` erwartet bewusst `blocked`: Ein ungepinnter externer Skill mit mutablem Remote-Nachladen erhält ohne vollständigen prüfbaren Snapshot keine Admission.

## Ausführung

Die Definition einer Golden Task ist **kein Pass-Nachweis**. Behavioral Runs werden separat unter `runs/` dokumentiert und müssen Modell, Commit, Sichtbarkeit der Rubrik sowie Selbst-/Fremdbewertung offenlegen.

### Routing-Trace für Behavioral Runs

Ein Routing-Urteil darf nicht nur auf einer vom ausführenden Modell formulierten Zeile wie „Selected route“ beruhen.

Für neue Behavioral Runs soll der Runner beziehungsweise Harness, soweit technisch verfügbar, einen **maschinenlesbaren Routing-Trace** auf Basis von `../../Agentenarbeit/trace-event.schema.yml` erzeugen:

- `CHECKPOINT_REACHED` für tatsächlich erreichte Routing-Checkpoints;
- `SKILL_ACTIVATED` nur wenn die konkrete `SKILL.md` tatsächlich geladen/aktiviert wurde;
- `ROUTING_REFINED` wenn ein vorläufiger Owner ersetzt oder der aktive Skill-Satz materiell geändert wurde;
- `SKILL_DEACTIVATED` wenn ein zuvor aktiver Skill durch Refinement entfernt wird;
- `ROUTING_REENTERED` wenn ein ereignisgesteuertes Re-Entry einen bereits geprüften Kandidaten erneut bewertet; `trigger_ref` verweist auf das auslösende Ereignis;
- `CANDIDATE_REJECTED` wenn der Harness eine Kandidatenprüfung selbst sieht und der Kandidat nicht aktiviert wird.

Strukturierte Felder: `checkpoint_id`, `candidate_skill_id`, `replaced_skill_id`, `trigger_ref` (siehe `Agentenarbeit/Trace-Datenmodell.md`). Ohne `CANDIDATE_REJECTED` ist ein Nicht-Aktivieren im Trace nicht von einer nie erfolgten Prüfung unterscheidbar; die Absenz eines Skills bleibt dann eine qualitative Beurteilung und gilt nicht als trace-verifiziert.

Die Events sollen vom Runner/Harness aus tatsächlichen Loads und Routingaktionen erzeugt werden, nicht als freie Selbstauskunft im Antworttext. Fehlt diese Instrumentierung, darf die Routing-Dimension weiterhin qualitativ beurteilt werden, aber nicht als **trace-verifiziert** bezeichnet werden.

Für jeden Lauf ist insbesondere zu dokumentieren:

- Modell und Repo-Commit;
- welche Execution View und Fixtures der Runner tatsächlich sah;
- ob Execution und Judging getrennte Modellkontexte waren;
- ob der Runner an der Erstellung der Tasks beteiligt war;
- welche evaluator-only Felder verborgen waren;
- pro Task dimensionale Findings;
- erwarteter und beobachteter Abschlussstatus;
- Forbidden-Verstöße;
- Klassifikation von Mismatches.

Ein Same-Model-Smoke kann interne Inkonsistenzen zeigen, ist aber kein unabhängiger Benchmark und rechtfertigt keine Maturity-Hochstufung.

Wenn der gleiche Modellkontext zuvor an Taskdefinitionen beteiligt war, muss der Lauf als `same-model / non-blind / author-contaminated` gekennzeichnet werden. Ein solcher Smoke darf Routing nicht als unabhängigen Generalisierungsnachweis darstellen.
