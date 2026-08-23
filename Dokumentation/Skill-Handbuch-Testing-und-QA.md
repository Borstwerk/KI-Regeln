# Skill-Handbuch – Testing und QA

Dieser Zusatz erklärt die Skills aus `../Testing-und-QA/` in menschenlesbarer Form.

## Schnellauswahl

| Aufgabe | Skill |
|---|---|
| Testportfolio für Feature/System planen | `test-strategy` |
| konkrete Testfälle entwerfen | `test-design` |
| reale technische Integrationen prüfen | `integration-testing` |
| Consumer-/Provider-Kompatibilität prüfen | `contract-testing` |
| kritischen Gesamtflow prüfen | `e2e-testing` |
| intermittierenden Test diagnostizieren | `flaky-test-diagnosis` |
| Fehler-/Recovery-Pfade prüfen | `failure-testing` |
| fokussierte explorative Session planen | `exploratory-testing` |
| bestehende Testsuite unabhängig auditieren | `test-suite-review` |

## `test-strategy`

Plant von Risiken ausgehend ein geeignetes Testportfolio. Der Skill entscheidet nicht nach starren Unit-/Integration-/E2E-Quoten, sondern nach benötigter Evidence.

Nicht verwenden, wenn nur ein einzelner konkreter Testfall geschrieben werden soll.

## `test-design`

Leitet konkrete Fälle aus Verhalten, Grenzwerten, Zuständen, Entscheidungstabellen, Failure Modes oder Properties ab.

Wichtig: Der Erwartungswert muss fachlich gestützt sein; Produktionslogik soll nicht einfach im Test dupliziert werden.

## `integration-testing`

Prüft reale Zusammenarbeit technischer Komponenten. Entscheidet risikobasiert zwischen Test Doubles und realen/realitätsnahen Dependencies.

Leitfrage:

> Ist genau das reale Verhalten dieser Dependency Teil des Risikos?

## `contract-testing`

Prüft Vereinbarkeit an einer Consumer-/Provider-Grenze. Contract Tests sind keine vollständigen Functional Tests und keine E2E-Tests.

## `e2e-testing`

Prüft ausgewählte kritische Nutzer-/Geschäftsflows über mehrere Systemgrenzen. E2E soll nicht jede kleine Fachregel duplizieren.

Für visuelle UI-Qualität zusätzlich `visual-verification` verwenden.

## `flaky-test-diagnosis`

Behandelt unzuverlässige Tests als Defekt am Qualitätssignal. Retry dient höchstens Diagnose oder temporärer Mitigation, nicht als Root-Cause-Fix.

## `failure-testing`

Prüft kontrollierte Fehler- und Recovery-Pfade wie Timeout, Teilfehler, Retry, Idempotenz oder Dependency-Ausfall.

Systemische Chaos-Experimente gehören später zu Reliability.

## `exploratory-testing`

Plant fokussierte lernende Sessions über Charter, Scope, Risiken und Zeitbox. Exploratives Testing ist nicht zufälliges Herumklicken.

## `test-suite-review`

Audit einer bestehenden Suite über Risikoabdeckung, Ebenen, Isolation, Flakiness, Doubles, Laufzeit, Coverage-/Mutation-Signale und Release-Evidence.

Review bedeutet nicht automatisch Rewrite.

# Zusammenspiel mit bestehenden Skills

```text
Implementierung:
tdd
→ verification-loop

Qualitätsplanung:
test-strategy
→ test-design
→ passende Testing-Skills
→ test-suite-review
→ verification-loop mit frischer Evidence
→ lokales Gate
```

# Reifegrad

Alle Testing-und-QA-Skills starten bewusst als `experimental` mit `partial` Evalabdeckung.

Eine spätere Hochstufung benötigt reale Nutzung und zusätzliche Regressionsevidence.