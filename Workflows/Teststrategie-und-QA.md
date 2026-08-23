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
→ relevante Nachweise frisch ausführen
        ↓
Release-/Quality-Evidence
        ↓
lokales Projekt-/Human-Gate
```

Nicht jeder Schritt ist für jede Änderung nötig.

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