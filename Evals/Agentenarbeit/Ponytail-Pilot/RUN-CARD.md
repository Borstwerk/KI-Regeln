# PT-01 – Kleine Startkarte für Codex / Claude Code

**Status:** `PREPARED / NOT RUN`. Diese Karte ist für einen
späteren **bewusst gestarteten** lokalen Abo-CLI- oder
freigegebenen isolierten Runnerdurchlauf, **kein**
Befehl an einen Agenten, direkt alle Fälle zu starten.

## Erster Pilot: PT01-A1 und PT01-B1

**Nicht** das ganze Ponytail-Plugin installieren, keine
Hooks/MCP/Statusband/Telemetrie einschalten und keine
fremden Modell-APIs bezahlen. Für den ersten Versuch
reicht die lokale Python-Standardbibliothek in der
bereits verfügbaren Runnerumgebung; auf dem
Nutzerrechner selbst ist keine Installation notwendig.

### 1. Aufgabenpakete im zugelassenen Runner vorbereiten

```sh
python tools/pt01_pilot.py selftest
python tools/pt01_pilot.py prepare --case PT01-A1 --arm A --out /tmp/pt01-a1-baseline
python tools/pt01_pilot.py prepare --case PT01-A1 --arm B --out /tmp/pt01-a1-checkpoint
python tools/pt01_pilot.py prepare --case PT01-B1 --arm A --out /tmp/pt01-b1-baseline
python tools/pt01_pilot.py prepare --case PT01-B1 --arm B --out /tmp/pt01-b1-checkpoint
```

Windows PowerShell: Statt `/tmp/...` passende **neue**
isolierte lokale Zielverzeichnisse verwenden.

### 2. Auftrag an einen Agenten (jeweils neue Session)

> Bearbeite ausschließlich die Aufgabe in `TASK.md` dieses
> isolierten Projektverzeichnisses. Verwende den separat
> freigegebenen, für alle Arme identischen
> KI-Regeln-Snapshot (`AGENTS.md`, Pflicht-Router,
> passende Fachskills und Workflow). Führe dessen
> Discovery wirklich durch; ändere keine Agentenregeln.
> Schreibe ausschließlich bei `implementation` und
> nur in die bereitgestellten Quelldateien.
> Bei `review`, `audit` oder `debt`:
> **nur lesen** und `REPORT.json` mit
> `case_id`, `findings` (path, line, category)
> liefern. Nicht vorhandene Checks als `NOT RUN`
> markieren; keine globalen Hooks, externe Provider,
> Installs oder produktive Systeme ansprechen.
> Bei Variante B zusätzlich die zugelassene
> `OPTIONAL_CHECKPOINT.md` berücksichtigen.
> Arbeite vollständig, sicher und nachvollziehbar;
> knappe Codeänderungen sind kein Ersatz für Tests.

Beim Paket ohne den Bootstrap fehlt die KI-Regeln-
Baseline; mit dem ganzen Originalrepo im Agentenzugriff
sind Judge-Labels sichtbar. **Beides ist kein gültiger
blind vergleichbarer Modelltest.** Operator stellt
denselben minimalen, read-only Bootstrap-Snapshot
isoliert zur Verfügung.

### 3. Auswerten, ohne die Agenten zu informieren

Bei **PT01-A1** kann ein separater Sandbox-Runner
`judge-only/test_implementation.py` gegen den
abgegebenen Code ausführen. Das importiert Agentencode:
**nicht in der normalen GitHub-Docs-CI oder einem
Produktivworkspace**.

Bei **PT01-B1** außerhalb des Agentenordners
`tools/pt01_pilot.py grade-report` verwenden.
Der genaue Zeilenanker ist ein **Development-Grader**;
ein unabhängiger Reviewer prüft fehlende/zusätzliche
tatsächliche Fehler zusätzlich.

### 4. Ergebnisprotokoll – erst nach echten Runs

| Feld | Einzutragen |
| --- | --- |
| Repo-/Tool-/Modell-/Skill-SHA und Effort | [bei Ausführung] |
| Arm, Case-ID, Zeitbudget und Rechtegrenzen | [bei Ausführung] |
| Output-/Diff-/Report-Hash | [bei Ausführung] |
| Echter Behavior-PASS bzw. Treffer/Fehlalarme | NOT RUN |
| Unerlaubte Writes / fehlende Freigaben | NOT RUN |
| Input/Outputtokens, Cache, Toolaufrufe | NOT MEASURED |
| Zeit, Kosten, Korrekturrunden | NOT MEASURED |
| Unabhängiger Outcome-Review | NOT RUN |

**Nächster Schritt nach Ausführung:** Den
`PT-01`-Draft-PR mit den echten Evidence-Links,
Fehlerbildern und begrenzter Schlussfolgerung
ergänzen. Keine „50 % bessere KI“-Behauptung
aus einzelnen synthetischen Development-Fällen.
