# Outcome-Pilot – HypeRadar (synthetisch, offline)

## Zweck und Grenze

Kleiner methodischer Pilot nach dem Outcome-Prinzip aus
[FDE Gym](https://github.com/deeplethe/fde-gym): Entscheidend ist die
beobachtete Ergebnisqualität einer Abgabe, nicht ob der Agent eine plausible
Begründung oder syntaktisch korrektes JSON erzeugt hat.

**Kein zweiter Behavioral Harness, keine neue Skill-ID, kein Live-System.**
Der bestehende [Behavioral Harness](../Behavioral-Harness/README.md) bleibt
Owner für Routing, Toolnutzung, Autorisierung, Scope und tatsächliche
Prozesstelemetrie. Dieser Pilot misst ausschließlich ein handhabbares
**Outcome** gegen vorab kuratierte, synthetische Bewertungslabels.

Die Bewertung ist ein F1-Score über exakt zugeordnete Kandidaten-IDs (0–100).
Historische Dubletten einschließlich Alias, unbekannte IDs, wiederholte
Empfehlungen sowie fehlende/erfundene Evidenzlinks sind **harte Blocker**
(Score 0), nicht kompensierbar durch andere richtige Vorschläge.
Dies sind **lokale Pilotregeln**, keine allgemeinen Skill-Qualitätsmetriken.

## Inhalte

- `runner-input/`: synthetische Kandidaten und Aufgabe, **einziger** dem Agenten
  bereitgestellter Input; alle URLs sind reservierte Platzhalter unter
  `example.invalid`, keine echte Recherche-Evidence.
- `judge-only/labels.json`: vorab kuratierte Entwicklungslabels; **nicht**
  zum Runner mounten, nicht als Promptkontext hinzufügen.
- `controls/`: bekannte Referenz (100), Nullbaseline (0) und absichtlich
  historische Dublette (BLOCKED).
- `../../tools/outcome_pilot.py`: ausschließlich lokale Standardbibliothek,
  keine Netzwerkzugriffe, keine Installation, keine Writes.
- `../../tests/test_outcome_pilot.py`: positive und kontrollierte negative
  Grader-Gegenproben sowie CLI- und Input-Integritätsprüfungen.

**Wichtig:** In einem öffentlichen Repository sind Judge-Dateien nicht
geheim. Das getrennte Verzeichnis ist nur ein **Packaging-Vertrag**.
Für einen fairen realen Lauf muss der Agent eine separate Arbeitskopie
**nur** aus `runner-input/` erhalten, ohne Zugriff auf Repository, Judge,
Controls, Reviewer-Notizen oder den Evaluator. Einem Agenten mit Zugriff
auf das ganze GitHub-Repository diese Dateien nur nicht im Prompt zu nennen
ist keine echte Blindheit. Die hier eingecheckten Labels sind
*Development/Regression Evidence*, keine unabhängigen Held-out-Daten.

## Lokaler Ablauf

1. Agentenlauf in separatem Arbeitsordner ausschließlich mit dem Inhalt
   von `runner-input/` durchführen. Keine Skripte im realen HypeRadar starten
   und nichts per Telegram senden.
2. JSON-Abgabe als Datei, z. B. `submission.json`, ablegen.
3. Außerhalb des Runner-Arbeitsbereichs bewerten:

    ~~~bash
    python tools/outcome_pilot.py \
      --case Evals/Outcome-Pilot/runner-input/candidates.json \
      --judge Evals/Outcome-Pilot/judge-only/labels.json \
      --submission Evals/Outcome-Pilot/controls/reference.json \
      --agent synthetic-reference
    ~~~

4. Gegenproben und Unit Tests:

    ~~~bash
    python -m unittest tests.test_outcome_pilot
    python tools/outcome_pilot.py \
      --case Evals/Outcome-Pilot/runner-input/candidates.json \
      --judge Evals/Outcome-Pilot/judge-only/labels.json \
      --submission Evals/Outcome-Pilot/controls/historical-duplicate.json
    ~~~

Der Referenz-CLI-Aufruf soll 100 Punkte und Exit 0 ergeben. Die Dublette
muss `BLOCKED`, Score 0 und Exit 1 liefern. Ungültige Eingaben liefern
`INVALID` und Exit 2. **Das sind erwartete Kontrollen, noch keine
behaupteten realen Agentenläufe.**

Der JSON-Output enthält SHA-256-Fingerprints über kanonische JSON-Inhalte
der drei Inputs und meldet `process_verification: NOT_RUN`. Die Hashes
fixieren den **beobachteten** Input für den Vergleich, nicht die Sicherheit
der Bewertungsbasis gegen einen Angreifer mit Schreibrechten.

## Fairer späterer Modellvergleich

Vor dem ersten unabhängigen Vergleich:

1. Neuen, getrennten nichtöffentlichen **Held-out**-Fall mit eigener
   Ground Truth und Review/Provenance erzeugen. Die bekannten synthetischen
   Entwicklungslabels nicht als Held-out ausgeben.
2. Baseline/Snapshot, Dublettenhistorie, Evalcode, Grader-Schwellen und
   erlaubte Tools vorab pinnen und für beide Modelle gleich halten.
3. Runtime- und Modellversion, Toolzugriffe, Prompt, Budget, Temperatur
   soweit verfügbar, Ausführungskosten und Runs je Modell erfassen.
4. Das Ergebnis **separat** von Prozess-/Autorisierungs- und
   Verification-Surface-Prüfungen bewerten. Bei fehlender Telemetrie
   `NOT_RUN`/`UNVERIFIED` statt eines Gesamt-PASS melden.
5. Unabhängige Cases getrennt von Development/Regression halten;
   vor der Messung keine Grader- oder Label-Anpassung zugunsten eines Modells.

**Nicht beansprucht:** produktiver HypeRadar-Test, reale Empfehlungsqualität,
statistische Signifikanz, echter Live-Traffic, Agenten-/Skill-Lift,
Prompt-Injection-Resistenz oder ein Behavioral-Eval-Pass.

## Quellen / Provenance

- Methode angeregt durch [DeepLethe/FDE Gym](https://github.com/deeplethe/fde-gym)
  (README/Harness-Dokumentation, konsultiert am 14.10.2026; Upstream
  Apache-2.0). **Keine Quellcodedatei oder Benchmark-Case übernommen.**
- Lokale Grundlage: [Agent Evals](../../Agentenarbeit/Agent-Evals.md),
  [Behavioral Harness](../Behavioral-Harness/README.md),
  [Verification Surface](../Verification-Surface/README.md).
