# Zielprofil – Agentische Coding-Werkzeuge

Nur für explizite Prompt-Erstellung oder -Adaption an Claude Code, Codex CLI/IDE,
Cursor oder vergleichbare Datei-/Tool-Agenten laden.

## Invarianten

- Ausgangszustand / echte Dateien / lokale Sources of Truth benennen **oder** vor einer Änderung gezielt finden lassen.
- Zielzustand als beobachtbares Artefakt/Verhalten beschreiben.
- Erlaubte Änderungen und ausdrückliche Nicht-Scope-Grenzen nicht erweitern.
- Prüfen, welche Runtime-Befugnisse tatsächlich vorliegen; keine nur sprachlich behauptete Sandbox.
- Installationen, gefährliche Befehle, Änderungen an Produktionsressourcen, externe Sends,
  Releases und Löschungen an passende menschliche Gates koppeln. Bereits existierende
  wirksame Gates nicht im neuen Prompt abschwächen.
- Tests und Checks: tatsächlich ausgeführt `PASS/FAIL`, nicht ausführbar `NOT RUN`;
  keine „alles getestet“-Floskel ohne Evidence.
- Bei unklarer Zielarchitektur oder fehlenden Pflichtdaten `STOP` / Rückfrage statt stiller Entscheidung.
- Keine künstlich strikte „eine Datei“-Grenze erfinden, wenn der Nutzer mehrere
  freigegebene Dateien erwartet.

## Unterschiede in der Ausgabe

- **Claude Code / Codex CLI:** Dateipfade, Scope, Toolrechte, Verifikation und
  Stop-Kriterien sind meist relevanter als Persona, XML-Show oder
  modellinterne Denk-Anweisungen. Lokale `AGENTS.md`-/Projektregeln erhalten.
- **Cursor / IDE-Assistent:** Betroffene Dateien, Symbol-/Funktionsnamen und
  zu bewahrendes Verhalten präzisieren, sofern vorhanden. Keine
  repo-weiten Rechte erfinden.
- **Nur Chat (kein Dateitool):** Kein `git`, keine CI und keine Dateiedits
  als tatsächlich ausführbar versprechen. Stattdessen Patch/Diff-Vorschlag
  oder Anweisung zum manuellen Prüfen liefern lassen.

## Minimaler Prompt-Schnitt

Ziel / bestätigter Kontext und kanonische Quellen / Änderungs-Scope /
Akzeptanzbedingungen / Prüfungen und Evidence / Rechte und Stop-Gates.

Nicht jedes kleine Refactoring benötigt eine riesige Checkliste.
Toolversion, Modell, Effort oder spezielle Kommandozeilenflags nur nennen,
wenn aus aktueller Quelle oder Zielruntime belegt.
