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

Der ausführende Agent erhält nur:

- `schema_version`;
- `id`;
- `title`;
- `goal`;
- `assignment`;
- `fixtures`;
- `sources_of_truth`;
- `required_capabilities`.

Die Projektion wird reproduzierbar erzeugt mit:

```bash
python tools/golden_task_execution_view.py Evals/Golden-Tasks/GT-01/task.yml --assert-no-evaluator-fields
```

Nicht in die Execution View gelangen:

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
- `GT-08` – Research → Social Content.

Alle Fixtures sind lokal und selbst erzeugt. Die Suite hängt nicht von aktuellen Webseiten, Social-Trends oder ungepinnten Repositories ab.

`GT-04` erwartet bewusst `partial`: Die Fixture reicht für belastbare Fakten, Hypothesen und nächste Diagnose, aber nicht für eine bestätigte Root Cause. `partial` ist dort der erwartete Erfolg epistemisch korrekten Verhaltens und kein fehlgeschlagener Golden Task.

## Ausführung

Die Definition einer Golden Task ist **kein Pass-Nachweis**. Behavioral Runs werden separat unter `runs/` dokumentiert und müssen Modell, Commit, Sichtbarkeit der Rubrik sowie Selbst-/Fremdbewertung offenlegen.

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
