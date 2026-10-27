# PT-01 – Ponytail vs. KI-Regeln: vier getrennte Arbeitsweisen

**Stand:** 27.10.2026 · **Status:** `FIXTURES + OFFLINE GRADER READY / AGENT NOT RUN / SKILL NOT ADMITTED`

[Quell-/Risiko-Vorprüfung](../../../Dokumentation/Reviews/Ponytail-2026-10-27.md) ·
[Runner-Fälle](runner-input/cases.json) ·
[Entwicklungslabels (Judge-only)](judge-only/labels.json) ·
[Minimaler interner Checkpoint](variants/minimal-checkpoint.md)

## Ziel

Prüfen, ob [Ponytails](https://github.com/DietrichGebert/ponytail)
**kleinste vollständige Änderung**, **Consumer-basierter Diffreview**,
**risk-first Repo-Audit** und **sichtbarer Shortcuts-Schuldenstand**
bei echten Aufgaben einen **inkrementellen Qualitäts-/Effizienzgewinn**
gegenüber dem schon vorhandenen KI-Regeln-Routing bringen.
**Keine** neue Super-Skill-Sammlung und **kein** vorgezogener
Skill-Import.

| Spur | Inhalt | Vorhandener Owner | Vorrang |
| --- | --- | --- | --- |
| **A – Minimalism** | Bestehende Helfer/stdlib/Plattform vor Neubau, aber vollständige Lösung | `Workflows/Software-Feature.md`, `tdd`, `verification-loop` | 1 |
| **B – Diffreview** | Indirekte Aufrufer/Bruchstellen, Safety, Tests, konkrete Review-Findings | `Programmieren/Skills/code-review/SKILL.md` | 1 |
| **C – Repo-Audit** | Kritische End-to-End-Pfade statt Stil-Checkliste; belegte Risiken priorisieren | `architecture-review`, `code-review`, Fachreviews | 2 |
| **D – Debt** | `shortcut:`-Kommentar mit Grenze und Upgrade-Trigger vs. bloßes TODO | projektbezogene Issues, lokaler Prozess | 2 |

**Wichtig:** In KI-Regeln gibt es bereits KISS-/Scope-Creep-
und Testregeln. Das ist eine **starke Baseline**.

## Versuchsarme je Spur (A/B/C sind Armnamen, nicht Spur-IDs)

| Arm | Gleicher Coding-Auftrag, unterschiedliche Zusatzinformation |
| --- | --- |
| **0 – Baseline** | Bestehende KI-Regeln-Owner und Pflicht-Bootstrap; kein Ponytail und kein neuer Text |
| **1 – KI-Regeln-Checkpoint** | Dasselbe plus unsere [kurze eigene Methode](variants/minimal-checkpoint.md), ausschließlich beim gewählten Testfall |
| **2 – Original-Ponytail-Skill** | Dasselbe plus **nur den relevanten**, gepinnten externen `SKILL.md`-Text. **BLOCKED**, solange dessen vollständig relevanter Bundle-/Prompt-/Tool-Scope nicht unabhängig zugelassen ist |

Das Offline-Werkzeug bezeichnet **Arm 0 als `A` und Arm 1 als `B`**.
Arm 2 heißt dort `C`, ist **bewusst gesperrt**. Damit ist nicht
`PT01-A1` (Spur A, Fall 1) mit dem Arm A zu verwechseln.

Das originale **Ponytail-Plugin inklusive Hooks, Band und
User-/Subagent-Injection ist in keinem Arm erlaubt.**
Ein möglicher späterer C-Test arbeitet in einer
freigegebenen isolierten Umgebung ausschließlich
mit dem überprüften Skill-Text, ohne Installation.
Keinen Eintrag in `skill-catalog.yml`,
`routing-overlays.yml`, globale oder projektlokale
`AGENTS.md`-Änderung veranlassen.

## Acht vorbereitete synthetische Fälle

| ID | Typ | Objective |
| --- | --- | --- |
| **PT01-A1** | Implementierung | Suche mit vorhandenem `normalize`-Helper verbessern; Verhalten und minimale Diffgröße |
| **PT01-A2** | Implementierung | Centgenau rechnen mit vorhandenem `to_cents`, keine Float-Mathematik |
| **PT01-B1** | Diffreview | Renamed Return-Key: bisheriger Consumer crasht, alter Test übersieht das |
| **PT01-B2** | Diffreview | Per-Nutzer-Limit fälschlich durch gemeinsamen Counter durchgesetzt |
| **PT01-C1** | Repo-Audit | SQL-Interpolation und als Erfolg gemeldeter Schreibfehler |
| **PT01-C2** | Repo-Audit | 1.200er-Charge fälschlich abgewiesen, unbekannte SKU still übersprungen |
| **PT01-D1** | Debt | Zwei echte `shortcut:`-Quellkommentare, einer ohne Upgrade-Trigger; Doku-Decoy |
| **PT01-D2** | Debt (Near-Miss) | Nur Dokumentation erwähnt `shortcut:`; **keine** echte Schuldenmarkierung |

Entwicklungslabels sind **öffentlich im Repository**,
aber nicht Agenteninput. Sie sind nur Development-/Regression-
Evidence und **kein unabhängiger held-out Test**.

## Offline ausführbarer Vorbereitungsschritt (ohne Installation)

**Voraussetzung:** Python 3 mit Standardbibliothek in einem
geeigneten Entwicklungs-/Runner-System. Auf dem normalen
Nutzer-PC ist **keine Installation nötig**: dieselben
Befehle können bei späterer Freigabe in einer vorhandenen
Codex-/Claude-Umgebung ausgeführt werden.

```sh
python tools/pt01_pilot.py selftest

# In frisch isolierte, noch NICHT vorhandene Ordner:
python tools/pt01_pilot.py prepare --case PT01-B1 --arm A --out /tmp/pt01-b1-baseline
python tools/pt01_pilot.py prepare --case PT01-B1 --arm B --out /tmp/pt01-b1-checkpoint
```

Das Paket enthält **nur** `TASK.md`, synthetische
Quelldateien, `manifest.json` mit Quellhashes und,
ausschließlich bei Arm B, `OPTIONAL_CHECKPOINT.md`.
**Kein** `judge-only`, keine Benchmarkzahlen,
keine Bewertungserwartungen. Es **führt keinen Agenten aus**.

**Wichtig für echte Agentenläufe:** Die Task-Verzeichnisse
sind nicht selbst ein KI-Regeln-Vault. Der Operator
stellt jedem frischen Agenten dieselbe **geprüfte,
versionsgebundene Read-only-Kopie** des
KI-Regeln-Bootstraps/erforderlicher Owner zur Verfügung
(`AGENTS.md`, Skill-Handbuch, Katalog, Overlays,
Workflow-Index falls relevant, fachliche `SKILL.md`).
Nicht einfach **das vollständige GitHub-Repository**
mounten: sonst sind `judge-only`, Entwicklungslabels
und die Prüfskripte sichtbar und die Blindheit zerstört.
Die einzige geplante Variation zwischen Arm 0 und 1
ist `OPTIONAL_CHECKPOINT.md`. Keine Änderungen an
Tools, Modellversion, Effort, Aufgabentext,
Budget oder sonstiger Instruction-Hierarchie.

### Review / Audit / Debt: Entwicklungs-Grader

Das Agentenergebnis als `REPORT.json` speichern,
**außerhalb** der Task-Workspace prüfen:

```json
{
  "case_id": "PT01-B1",
  "findings": [
    {"path": "app/sample.py", "line": 3, "category": "bug"}
  ]
}
```

Dies ist **nur ein Schema-Beispiel**, kein erwarteter Fund.
Zulässige Kategorien:
`bug`, `security`, `data_loss`, `tracked`,
`no_trigger`. Leerer Fall: `"findings": []`.

```sh
python tools/pt01_pilot.py grade-report \
  --case PT01-B1 --submission /tmp/pt01-b1-review.json
```

Gemessen werden exakt bestätigte Entwicklungs-Anker
`(path, line, category)`, fehlende und zusätzliche
Meldungen sowie Precision/Recall gegen öffentliche
Entwicklungslabels. **Ein alternativer gültiger
Zeilenanker darf nicht allein wegen eines engen
Exact-Matches fachlich als falsch gelten**; Reviewer
muss reale Codepfade und Effekte nachprüfen. Dieses
Tool **ersetzt keinen unabhängigen Code-Review**.

### Implementierung: ausführbarer Oracle, aber nur in Sandbox

Die beiden A-Fälle haben getrennte Verhaltenschecks
unter [`judge-only/test_implementation.py`](judge-only/test_implementation.py).
**Dieser Test importiert und führt den vom Agenten
produzierten Python-Code aus.** Deshalb ausschließlich
in einem isolierten, wegwerfbaren Container/Runner
**nach separater Ausführungsfreigabe**, nicht
auf produktiven Projektdateien oder Nutzersystemen:

```sh
python Evals/Agentenarbeit/Ponytail-Pilot/judge-only/test_implementation.py \
  --case PT01-A1 --workspace /tmp/pt01-a1-baseline
```

A1/A2-Behaviortests prüfen konkrete fachliche
Anforderungen; **zusätzlich** müssen Scope,
Codeverständlichkeit, unnötige Abhängigkeiten,
rückwirkende Kompatibilität, notwendige Tests
und Änderungen in unerlaubten Dateien
unabhängig beurteilt werden. Die beiden
A-Quellstands-Stubs sind absichtlich unvollständig/
fehlerhaft; **nicht** als grüne Referenz deklarieren.

## Grading und Stop-Gates

**Hard Fail unabhängig von Codeeinsparung:**
- Nutzeranforderung oder bekannte Consumer bricht;
- fehlende Trust-Boundary-Validierung, Sicherheits-
  oder Datenschutzhürde;
- fehlerhafte Geld-/Persistenz-/Lastfälle;
- Review/Audit schreibt unerlaubt Code;
- nicht ausgeführter Test wird als `PASS` bezeichnet;
- Parser/Grader wird auf die Agentenantwort hin
  gelockert oder Judge-Labels gelangen zum Agenten;
- geänderter `AGENTS.md`-Bootstrap oder
  nicht freigegebene global/hook-/plugin-Rechte.

**Ergebnisse getrennt messen:**
- funktionale Behaviortests und echte Regressionen;
- reale relevante Findings und False Positives;
- geänderte LOC **ohne** Tests, neue
  Dependencies, unnötige Abstraktionen,
  Diff-Scope und gewachsene Wartungslast;
- Tests, die bei Mutation der kritischen Logik
  **tatsächlich** fehlschlagen;
- frische Input-/Output-Tokens, Toolcalls,
  Zeit, Retry-/Review-Runden und Kosten,
  **nur soweit in der Runnerumgebung messbar**.

Falls echte Abodaten fehlen:
`TOKENS_NOT_MEASURED`, keine aus
Textzeichen erfundenen Kosten.

## Budget- und Ausführungsplan (noch NICHT ausgeführt)

1. **Jetzt:** Nur Offline-Fixtures/Tests in der bestehenden
   GitHub-Repository-CI; **kein zusätzlicher Scheduler,
   keine Modell-Calls, kein API-Key**.
2. **Kleiner Pilot nach Freigabe:** zunächst
   `PT01-A1` und `PT01-B1` im direkten Paar
   (0 vs. 1), höchstens **zwei frische Agentläufe
   pro Fall** im jeweiligen lokalen CLI-Abo
   bei gleichwertigem Scope und Snapshot.
   Nicht acht Fälle × drei Arme ungeprüft starten.
3. Nur bei verwertbaren Signalen `PT01-C1`,
   `PT01-D1` und weitere Negativfälle.
   Original-Arm 2 **erst nach** separatem
   `skill-security-review` und Source-Freeze.
4. Danach unabhängiger Review der Grader,
   Development-/Held-out-Trennung, Ergebnis-
   report und `KEEP BASELINE` /
   `ADOPT SMALL CHECKPOINT` /
   `REVIEW ORIGINAL SKILL ADMISSION` /
   `INCONCLUSIVE` / `REJECT`.
5. Mögliche Aufnahme nur nach belastbarem
   Lift: zunächst bestehende `code-review`-
   und Software-Feature-Owner verbessern.
   **Keine** automatische Übernahme von
   `ponytail-review`, `ponytail-audit`,
   `ponytail-debt` oder globalem Persona-
   /SessionStart-Hook.

## Aktueller Nachweisstand

| Bestandteil | Status |
| --- | --- |
| Quell-/Sicherheits-Vorprüfung | `PARTIAL / NOT ADMITTED` |
| Acht synthetische Tasks, getrennte Entwicklungslabels | `READY FOR PACKAGING` |
| Offline-Packer/Grader + Unit-Gegenproben | `IMPLEMENTED; CI TO VERIFY` |
| Original-Ponytail-Skill/Plugin installiert | `NO` |
| A/B/C-Modellruns oder nachgewiesener Token-/Qualitäts-Lift | `NOT RUN / UNVERIFIED` |
| Unabhängige Held-out-Evals | `NOT PREPARED` |

[Praktische Startkarte](RUN-CARD.md).
