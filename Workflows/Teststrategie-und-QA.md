# Workflow – Teststrategie und QA

## Zweck

Dieser Workflow verbindet die Testing-Skills zu einem nachvollziehbaren Qualitätspfad für ein Feature, eine größere Änderung oder einen Release-Kandidaten.

Er ist technologie- und frameworkneutral.

## Ablauf

```text
Anforderung / Änderung / Release-Kandidat
        ↓
test-strategy
        ↓
Risiken + Testportfolio
        ↓
test-design
        ↓
konkrete Kernfälle
        ↓
bei Bedarf parallel / selektiv:
├─ integration-testing
├─ contract-testing
├─ e2e-testing
└─ failure-testing
        ↓
exploratory-testing
(wenn zusätzliche lernende Prüfung sinnvoll ist)
        ↓
flaky-test-diagnosis
(nur bei unzuverlässigem Signal)
        ↓
test-suite-review
        ↓
verification-loop
→ Verification Discovery für Projekt/OS/Toolchain und Risiko
→ native, autorisierte Nachweise frisch ausführen
        ↓
Release-/Quality-Evidence
        ↓
lokales Projekt-/Human-Gate
```

Nicht jeder Schritt ist für jede Änderung nötig.

## Native Ausführung und Reportübergabe

Vor der Testausführung die projektlokalen Vorgaben, Sprache/Framework, OS-/Runtime-Capabilities und Ausführungsrechte ermitteln. Die Regeln in `../Testing-und-QA/Umgebungsabhaengige-Verifikation-und-Reports.md` führen zur kleinsten geeigneten Prüfung. Fehlende Umgebungen und übersprungene Tests bleiben sichtbar, statt durch grüne Teilchecks kompensiert zu werden.

Ein gemeinsamer `verification-run`-Report ist für CI, lokale Ausführung und Agentenumgebungen **optional**; er ersetzt weder native Tests noch Release-/Human-Gates. HTML kann später dieselben Daten ohne neue Bewertung darstellen.

## Handoff-Evidence

Zwischen Phasen möglichst weitergeben:

- getesteten Scope / Commit / Build;
- relevante Risiken;
- Testziele;
- verwendete Testebenen;
- Testdaten und Umgebung;
- ausgeführte Nachweise;
- Findings / Defekte;
- flaky oder blockierte Prüfungen;
- Restunsicherheit.

## Grenzen

- TDD bleibt Teil der Implementierung und kann innerhalb des Feature-Workflows verwendet werden.
- Visuelle Browserqualität bleibt `visual-verification`.
- tiefe Security-Tests bleiben `Sicherheit/`.
- Chaos Engineering, SLO-/Resilience-Experimente und systemische Störtests gehören später zu `Reliability/`.
- der Workflow autorisiert keine Releasefreigabe selbst.

## Leitgedanke

> Testing produziert Evidence über Qualität und Risiko. Das gültige Projekt-Gate entscheidet, was daraus folgt.