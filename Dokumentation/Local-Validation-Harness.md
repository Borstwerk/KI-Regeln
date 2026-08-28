# Local Validation Harness

Stand: 2026-08-26  
Basis der Implementierung: `9027d8d49b327ff663f8cddd29ef7e27eaedc0d4`

## Ziel

Das Local Validation Harness stellt für Windows einen einzigen Einstieg für die vorhandenen strukturellen KI-Regeln-Prüfungen bereit:

```powershell
.\Validate-KI-Regeln.ps1
```

Der Standardlauf ist `Full`. Zusätzlich stehen zur Verfügung:

```powershell
.\Validate-KI-Regeln.ps1 -Quick
.\Validate-KI-Regeln.ps1 -Full
.\Validate-KI-Regeln.ps1 -Release
.\Validate-KI-Regeln.ps1 -Full -WarningsAsErrors
```

Alternativ kann `Validate-KI-Regeln.cmd` per Doppelklick oder aus `cmd.exe` gestartet werden.

Es ist keine systemweite Python- oder Node-Installation erforderlich. Die vorhandenen Python-Validatoren bleiben die kanonische Prüflogik; PowerShell orchestriert Runtime, Modus, Reporting und Exitcodes.

Behavioral Evals werden durch dieses Harness **nicht** ausgeführt.

## Architekturentscheidung

Gewählt wurde:

```text
Validate-KI-Regeln.ps1
        |
        +-- lokale portable Runtime (.validation/)
        |     +-- gepinntes uv
        |     +-- uv-managed CPython
        |     `-- isoliertes venv
        |
        +-- vorhandene kanonische Python-Validatoren
        |
        +-- PowerShell-Gating/Reporting
        |
        `-- .validation/latest.json + latest.md + logs/
```

### Warum nicht PowerShell-native Validatorlogik?

`tools/repo_validator.py` implementiert bereits die fachlich relevanten Strukturinvarianten und verwendet echte YAML- und JSON-Schema-Validierung. Ein Port nach PowerShell würde dieselben Regeln ein zweites Mal ausdrücken und damit eine zweite Validator-Wahrheit schaffen. Insbesondere Skill-, Eval-, Registry-, Provenance- und Schema-Semantik werden deshalb nicht dupliziert.

PowerShell übernimmt nur Aufgaben, die keine zweite fachliche Wahrheit erzeugen:

- Runtime-Bootstrap;
- Git-/Working-Tree-Zustand;
- Aufruf und Kapselung vorhandener Validatoren;
- Interpretation bereits bestehender Exposure-Severity (`potential-secret` vs. `review-context`);
- Console-/JSON-/Markdown-Reporting;
- Exitcode-Gesamtentscheidung.

## Gate 1 – Read-only Bestandsaufnahme

### Tools

| Tool | Zweck | Inputs | Output | Exitcode | Abhängigkeiten | Laufzeit | PowerShell-Port | Kanonisch bleiben | Überschneidungen | Modus |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `tools/repo_validator.py` | Deterministische Strukturprüfung des Repositories | `skill-catalog.yml`, Skills, `Evals/**/cases.yml`, `workflow-index.yml`, Manifest, Golden Tasks, Upstream-/Provenance-/Readiness-Dateien und Schemas | Konsolensummary, `WARNING ...`, `ERROR ...` | `0` PASS, `1` bei Fehlern; optional Warnungen als Fehler | Python, PyYAML, jsonschema, `public_readiness_checks.py` | schnell bis mittel; vollständiger Tree, aber keine History-/Remote-Scans | nicht sinnvoll | **ja** | enthält Public-Readiness-Prüfung; validiert Golden Tasks strukturell | Quick, Full, Release |
| `tools/eval_coverage_audit.py` | Read-only Coverage-/Case-Inventar und heuristische Audit-Signale | `skill-catalog.yml`, `Evals/**/cases.yml` | JSON oder `--summary` | immer `0`, sofern Prozess selbst funktioniert | Python, PyYAML | schnell | nicht nötig | ja | Coverage-Konsistenz wird teilweise bereits durch `repo_validator.py` gegatet; dieses Tool liefert zusätzliche Counts/Signale | Full, Release |
| `tools/public_readiness_checks.py` | Strukturelle Public-Readiness-, Provenance-, Notice-, Lizenz- und Hygiene-Invarianten | Upstream Sources/Provenance, Open-Source-Readiness, Lizenz-/Notice-/Hygiene-Dateien | Callback-basierte Errors/Warnings + Counts | kein eigener CLI-Exitcode | Python, PyYAML, jsonschema | schnell | nicht sinnvoll | **ja** | wird direkt von `repo_validator.py` aufgerufen | Quick, Full, Release indirekt |
| `tools/open_source_readiness_audit.py` | Current-Tree Exposure, Registry-Crosscheck und optional teure Remote-/History-Audits | Git-tracked Tree, Quellen/Upstreams; optional GitHub/Web/History | JSON-Datei + Summary | Scanner selbst liefert auch bei Funden `0` | Python, PyYAML, Git; optional Netzwerk | Current Tree mittel; `--github`, `--non-github`, `--history` deutlich teurer | nur Orchestrierung sinnvoll | ja | Current Tree entspricht dem bisherigen Exposure-CI-Job; eigene `--history`-Funktion überlappt mit separatem History-Scanner | Release (ohne Online-Flags) |
| `tools/history_exposure_scan.py` | Exposure-Scan über alle aus lokalen Refs erreichbaren Commits/Blobs | vollständige Git-Historie | JSON-Datei + Summary | Scanner selbst liefert auch bei Funden `0` | Python-Stdlib, Git | teuerster lokaler statischer Check | nicht sinnvoll | ja | ähnliche Patternklassen wie Current-Tree-Scan | Release |
| `tools/golden_task_execution_view.py` | reproduzierbare Execution-Projektion von Golden Tasks | Golden-Task-Definitionen | Execution View | tool-spezifisch | Python | schnell | nicht nötig | ja | Golden-Task-Struktur wird durch `repo_validator.py` geprüft | kein direkter Harness-Schritt |

### Workflows

#### `.github/workflows/repo-validation.yml`

Aktueller Stand:

- Python `3.12`;
- `PyYAML==6.0.2`;
- `jsonschema==4.25.1`;
- führt `python tools/repo_validator.py` aus;
- kein Behavioral-Eval-Lauf;
- kein Eval-Coverage-Audit im Workflow.

#### `.github/workflows/open-source-exposure-audit.yml`

Aktueller Stand:

- Current Tree: `open_source_readiness_audit.py`;
- Reachable History: `history_exposure_scan.py`;
- Scanner liefern Findings als Daten;
- Inline-Python im Workflow macht aus `potential-secret` einen Fehler;
- `review-context` bleibt Review-Signal/Warnung.

Das Local Harness übernimmt dieselbe Severity-Gate-Semantik. Die Scanner selbst werden dafür nicht verändert.

### Schemas

Unter `Schemas/` existieren am Basisstand sechs zentrale Schemas:

- `ki-regeln.template.schema.json`;
- `open-source-readiness.schema.json`;
- `skill-catalog.schema.json`;
- `upstream-provenance.schema.json`;
- `upstream-sources.schema.json`;
- `workflow-index.schema.json`.

Die Eval-Fallstruktur verwendet zusätzlich `Evals/eval-case.schema.yml` als kanonische Feld-/Enum-Definition; es existiert kein separates `Schemas/skill-eval.schema.json`.

### Python-Abhängigkeiten

Direkte CI-Parität:

- `PyYAML==6.0.2`;
- `jsonschema==4.25.1`.

Für den lokalen Bootstrap werden zusätzlich deren aufgelöste Runtime-Abhängigkeiten in `tools/local_validation/requirements.lock` fest eingefroren.

## Runtime und Bootstrap

### Gepinnte Komponenten

- `uv`: `0.12.6`;
- CPython: `3.12.12`;
- Runtime-Pakete: `tools/local_validation/requirements.lock`.

`uv` wird nicht installiert. Das passende Windows-Archiv wird in `.validation/runtime/` abgelegt und vor Benutzung gegen den in `runtime-manifest.json` hinterlegten SHA-256 geprüft.

Unterstützte lokale Windows-Architekturen:

- x64;
- ARM64.

### Lokale Isolation

Das Harness setzt für den Bootstrap lokale uv-Verzeichnisse:

- Cache;
- Python-Installationsverzeichnis;
- Python-Bin-Verzeichnis;
- venv.

Zusätzlich wird Python ohne Windows-Registry-Eintrag und ohne globalen Python-Bin-Link installiert. System-Python wird durch `--managed-python` nicht verwendet.

Normale Läufe starten anschließend direkt das lokale `python.exe`; es gibt kein stilles Update und keinen Download pro Lauf.

### Wann wird erneut gebootstrapped?

Der Runtime-Zustand enthält SHA-256-Werte von:

- `runtime-manifest.json`;
- `requirements.lock`.

Ändert sich einer dieser Inputs oder fehlt die Runtime, wird sie bewusst neu aufgebaut. Mit `-NoBootstrap` kann ein automatischer Bootstrap für Offline-/Diagnosezwecke verboten werden.

## Validation-Modi

### Quick

- Repository-/Git-Zustand;
- portable Runtime;
- vollständiger kanonischer `repo_validator.py`;
- damit unter anderem Skill-Katalog, Skillpfade, Frontmatter, Eval-Struktur/-Coverage-Konsistenz, Workflows, Manifest, Golden Tasks, Upstream Sources, Provenance und Public Readiness.

`Quick` führt bewusst denselben kanonischen Validator aus, statt eine vereinfachte zweite Quick-Implementierung zu bauen. Der Unterschied zu `Full` ist deshalb vor allem das zusätzliche Coverage-Reporting.

### Full

Alles aus `Quick`, zusätzlich:

- `eval_coverage_audit.py`;
- Counts zu Skills, Evalpacks, definierten Cases und Coverage-Stufen;
- heuristische Audit-Signale nur als Inventar/Information, nicht als Behavioral-Ergebnis.

Dies ist der Standardmodus von `.\Validate-KI-Regeln.ps1`.

### Release

Alles aus `Full`, zusätzlich:

- Current-Tree Exposure via `open_source_readiness_audit.py`;
- Reachable-History Exposure via `history_exposure_scan.py`;
- Prüfung, dass keine shallow Git-Historie als vollständiger Release-Scan ausgegeben wird.

Severity bleibt identisch zur bisherigen CI-Logik:

- `potential-secret` => FAIL;
- `review-context` => WARN.

Die optionalen Netzwerkmodi `--github` und `--non-github` von `open_source_readiness_audit.py` sind **nicht** Bestandteil des normalen Release-Laufs. Sie hängen von Remotezuständen und Netzwerk ab und bleiben bewusste separate Audit-Werkzeuge.

## Reporting

Generiert werden ausschließlich unter `.validation/`:

```text
.validation/
  latest.json
  latest.md
  current-tree.json
  reachable-history.json
  logs/
  runtime/
```

`.validation/` ist gitignored.

Die Konsole zeigt die Stufen kompakt. Python-stdout/-stderr und technische Details landen im Log statt als primäre Oberfläche. JSON ist der maschinenlesbare Vertrag; Markdown ist der menschenlesbare Laufbericht.

Behavioral Validation wird in Konsole und Reports ausdrücklich als `NOT RUN` ausgewiesen.

## Exitcodes

- `0`: struktureller Lauf PASS; Warnungen dürfen vorhanden sein;
- `1`: Validierungsfehler oder `-WarningsAsErrors`;
- `2`: Harness-/Runtime-/Infrastrukturproblem, durch das der angeforderte Prüfstand nicht vollständig ausgeführt werden konnte.

Beispiele für Exitcode `2`:

- fehlende Runtime mit `-NoBootstrap`;
- Release ohne Git;
- Release auf shallow History;
- Bootstrap-/Hashfehler.

## Supply Chain

Das Bootstrap-Modell trennt Erstbeschaffung und normale Ausführung:

1. gepinntes `uv`-Release;
2. fest hinterlegte Download-URL je Windows-Architektur;
3. fest hinterlegter SHA-256 des uv-Archivs;
4. exakte CPython-Patchversion;
5. exakt gepinnte Python-Pakete;
6. keine automatische Aktualisierung;
7. normale Ausführung ohne Remote-Download.

Ein Upgrade von uv, Python oder Python-Paketen ist damit eine sichtbare Repository-Änderung und kein Nebeneffekt eines Validatorlaufs.

## Selbstprüfung

`tools/local_validation/Invoke-HarnessSelfTest.ps1` verwendet einen temporären detached Git-Worktree. Produktive Repository-Dateien werden nicht für Tests verändert.

Kontrollierte Fälle:

1. sauberer aktueller Repository-Stand;
2. ungültige Skill-ID;
3. fehlender Evalpfad;
4. falsche Coverage (`cases.yml` vorhanden, Catalog `none`);
5. ungültiges YAML;
6. fehlender source-spezifischer Provenance-Eintrag;
7. ungültiger `local_impact`-Pfad;
8. synthetischer Current-Tree-Exposure-Fund;
9. Warnung ohne Fehler;
10. fehlende portable Runtime mit `-NoBootstrap` plus isolierter First-Bootstrap.

Aufruf:

```powershell
.\tools\local_validation\Invoke-HarnessSelfTest.ps1
```

Das Selftest-Harness schreibt sein Ergebnis nach `.validation/selftest-latest.json`.

Synthetische Secret-/Kontaktwerte werden nur im temporären Worktree erzeugt und nicht in produktive Repository-Dateien geschrieben oder committet.

## CI-Handoff

Die bestehenden GitHub Actions bleiben unverändert bestehen. Eine spätere CI-Umstellung auf den gemeinsamen Entry-Point ist möglich, sollte aber separat erfolgen. Der aktuelle Bootstrap ist absichtlich für den Windows-Lokalbetrieb umgesetzt; ein CI-Handoff sollte Plattform- und Cache-Strategie bewusst ergänzen, statt still CI-Sonderlogik in diesen Auftrag zu ziehen.

## Bekannte Grenzen

- Der automatische portable Bootstrap ist derzeit Windows-spezifisch (x64/ARM64).
- `Release` benötigt Git und vollständige lokal erreichbare Historie.
- Der erstmalige Bootstrap benötigt Netzwerkzugriff zu den gepinnten Bezugsquellen/Paketindizes.
- Python-Paketversionen sind vollständig gepinnt; Paketartefakt-Hashes sind in dieser ersten Harness-Version noch nicht als `--require-hashes`-Set pro Plattform hinterlegt. Das uv-Binary selbst wird per SHA-256 verifiziert.
- Online-Upstream-Überprüfungen sind absichtlich kein normaler Release-Schritt.
- Behavioral Evals sind außerhalb dieses Harness-Scope.
