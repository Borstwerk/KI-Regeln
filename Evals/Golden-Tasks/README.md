# Golden Tasks

Golden Tasks prüfen das Zusammenspiel von Bootstrap, Routing, lokaler Wahrheit, Workflows, Skills, Evidence, Gates und Verification an kleinen reproduzierbaren Aufgaben.

Sie sind **keine normalen Skill-Evals**. Skill-Evals prüfen eine einzelne Arbeitsdisziplin möglichst gezielt; Golden Tasks prüfen, ob ein Agent bei einer realistischen End-to-End-Aufgabe den kleinsten ausreichenden fachlichen Pfad findet und die Grenzen zwischen Disziplinen einhält.

## Struktur

- `golden-task.schema.json` – maschinenlesbares Format einer Taskdefinition;
- `suite.yml` – Index der zur Suite gehörenden Tasks;
- `GT-XX/task.yml` – Taskdefinition;
- weitere Dateien im jeweiligen `GT-XX/`-Ordner – lokale, selbst erzeugte Fixtures.

## Routing ohne Prompt-Skript

Eine Task definiert:

- `required_skills` für unverzichtbare Arbeitsdisziplinen;
- `allowed_optional_skills` für legitime zusätzliche Disziplinen;
- `forbidden_skills` nur für offensichtlich falsches oder scope-erweiterndes Routing;
- einen oder mehrere `allowed_workflows`, sofern ein Workflow sinnvoll ist.

Ein Agent muss daher nicht exakt eine vorgegebene interne Skillkette reproduzieren. Bewertet wird das beobachtbare Verhalten.

## Bewertungsachsen

Jede Task besitzt eine dimensionale Rubrik für:

- Routing;
- Grounding;
- Scope;
- Gates;
- Verification;
- Ergebnisqualität.

Es gibt keine opaque Gesamtnote. Findings bleiben pro Dimension sichtbar.

## Ausführung

Die Definition einer Golden Task ist **kein Pass-Nachweis**. Behavioral Runs werden separat unter `runs/` dokumentiert und müssen Modell, Commit, Sichtbarkeit der Rubrik sowie Selbst-/Fremdbewertung offenlegen.

Ein Same-Model-Smoke kann interne Inkonsistenzen zeigen, ist aber kein unabhängiger Benchmark und rechtfertigt keine Maturity-Hochstufung.
