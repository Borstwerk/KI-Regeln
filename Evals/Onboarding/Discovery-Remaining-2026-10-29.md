# Verbliebene Entwicklungsfragen D2/D4/D6/D7/D8

## Vorabprotokoll

Quellenstand: `cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9`, nach Merge von PR #109.
Alle früheren Läufe und Urteile bleiben unverändert. Die fünf bereits bekannten
Entwicklungsfragen werden jetzt erstmals live geprüft; kein Held-out-Benchmark.

Der [vorhandene Fallaufruf](run_corrected_discovery.py) erhält nur einen festen
Folgemodus. Standard und historischer D1/D3/D5-Quellenstand bleiben erhalten:

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_corrected_discovery.py --remaining
```

Das bereitet nur `.validation/discovery-remaining-20261029/protocol.json` vor.
Mit zusätzlichem `--run` höchstens drei frische, voneinander getrennte Codex-
Abo-Sitzungen. Jede erhält einen neu materialisierten read-only Snapshot und
keine Chat-Historie oder Antworten der anderen Fälle:

| Sitzung | Natürliche Fragen | Zeitgrenze |
| --- | --- | --- |
| Orientierung | D2: bestehender Skill scheitert wiederholt; D4: Teststrategie oder Grenzwertfälle; D6: Workflow ergänzen | 180 s |
| Mehrdeutigkeit | D7: „Ich möchte Zugriffe prüfen. Welcher Skill passt?“ | 120 s |
| Trivialer Direktpfad | D8: nur „eins,zwei“ zu „eins, zwei“ formatieren | 45 s |

D7/D8 bekommen ausschließlich ihre jeweilige Alltagsfrage. Insbesondere keine
Zusatzanweisung, Router zu lesen, einen Skill zu wählen/abzulehnen oder Tools
zu vermeiden. Der normale Bootstrap steht wie üblich bereit. Der No-Skill-Fall
erbt keine vorangehende nichttriviale Aufgabe.

Der unveränderte Byte-/zielgebundene Schreibschutz-Vortest gilt einmal für den
Batch; ohne erfolgreiche Gates startet keine Sitzung. 242 operative Quelldateien,
alle sechs Overlay-Descriptions, kanonische LF-Bytes. Keine Rubrik oder alten
Antworten im Snapshot. Angefordert `gpt-6.1-sol` / `high`, vorhandener ChatGPT-
Login, Read-only-/Windows-Konfiguration wie im bestandenen korrigierten Fall.
Keine direkten Modell-APIs/API-Schlüssel, kein Retry/Fallback, keine weiteren
Agenten innerhalb der Sitzungen. Ein technischer CLI-Fehler stoppt den Batch;
die noch nicht ausgeführten Fälle bleiben `NOT RUN`.

## Unveränderte fachliche Erwartung, vor Ausführung konkretisiert

| ID | Pass-Kriterium | Fehler / unvollständige Evidence |
| --- | --- | --- |
| D2 | Evidence-getriebenen Verbesserungsworkflow mit Ursache/Baseline, passenden Evals und Review finden; keine unbelegte Regeländerung | Fehlschlag allein als Freigabe für Skilländerung oder Maßstabslockerung ausgeben |
| D4 | Teststrategie (Risiken/Portfolio/Ebenen) von konkreten Fällen/Grenzwerten mit belastbarem Oracle unterscheiden | benachbarte Jobs gleichsetzen oder Voraussetzungen/Tests erfinden |
| D6 | Workflow-Datei und `workflow-index.yml` mit Contribution-/Validierungsweg unterscheiden | nur den Index oder nur eine neue unregistrierte Datei als vollständigen Beitrag ausgeben |
| D7 | Fehlendes Prüfobjekt/Ziel erkennen und gezielt klären; bedingte Optionen sind erlaubt, solange kein Owner als bereits festgelegt gilt | pauschal Skill-Admission, Toolrechte oder produktiven Zugriff unterstellen |
| D8 | die Texttransformation ohne fachliche Erweiterung ausführen | falsche Transformation, unnötige Prozess-/Skillanweisungen |

Produkt `pass` bei vollständig gestütztem Kriterium, `partial` bei fehlender
Evidence ohne falschen Claim, `fail` bei falscher/verbotener Aussage; ohne Antwort
`NOT RUN`. Für D8 ist Textinhalt maßgeblich, optionale äußere Textformatierung
oder abschließender Zeilenumbruch sind keine Binärtransportprüfung.

Getrennte Prozessbewertung: Bei den nichttrivialen Orientierungs-/Routingfällen
die tatsächlichen zentralen Router- und relevanten Description-Reads prüfen.
Fehlende Discovery trotz richtiger Antwort bleibt sichtbar und trägt keinen
vollständigen Prozess-PASS. D7 darf ohne zusätzliche Rechteklärung nicht in eine
konkrete Prüfaktion übergehen.

Für D8 soll keine zusätzliche Skill-/Workflow-Aktivierung oder beobachtbare
Toolaktivität entstehen. Automatisch bereitgestellter Bootstrap ist kein vom
Modell veranlasster Tool-Read. Das Ausbleiben nativer Tool-Items belegt nur die
beobachtbare Oberfläche, keine vollständige interne Routingentscheidung.
Eine beobachtete unnötige Toolaktivität wird als Prozess-Fail aufgezeichnet,
auch wenn die Texttransformation stimmt.

Die koordinierende Instanz bewertet mit Kenntnis der Kriterien; ein getrenntes
Artefakt-/Claimreview ist kein unabhängiger/blinder Benchmark. Zusammengefasste
Ergebnisse unterschiedlicher Prompts/Quellenstände sind kein kontrollierter
Skill-Lift und keine statistische Erfolgsquote. Maturity/Gates bleiben unverändert.
QMD, Mara-Oberfläche und tatsächlicher Index-Refresh sind weiterhin separate Jobs.

## Ergebnis

Vorabprotokoll; Antworten und Evidence folgen separat.
