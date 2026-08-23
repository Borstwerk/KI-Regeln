# Agent Evals

## Zweck

Normale Softwaretests prüfen das Produkt. Agent Evals prüfen zusätzlich, **wie zuverlässig ein KI-Agent unter definierten Bedingungen arbeitet**.

Ein Eval fragt nicht nur:

> Ist der resultierende Code korrekt?

sondern beispielsweise auch:

> Hält der Agent den Scope ein, nutzt die richtigen Quellen, respektiert Freigaben und liefert die geforderte Evidence?

## Grundprinzip

> Produktqualität und Agentenqualität sind zwei verschiedene Prüfebenen.

Ein grüner Produkttest beweist nicht, dass der Agentenprozess zuverlässig ist. Ein gut arbeitender Agent ersetzt umgekehrt keine fachlichen Produktprüfungen.

## Was ein Agent Eval prüfen kann

Je nach Einsatzgebiet beispielsweise:

- erkennt der Agent die verbindliche Spezifikation?
- beginnt er bei größeren Änderungen mit Planung statt sofort mit Code?
- hält er den freigegebenen Scope ein?
- verändert er keine ausgeschlossenen Dateien oder Verträge?
- fordert er bei einer neuen Architekturentscheidung ein Gate an?
- schwächt er keine Tests oder Validierung, um grün zu werden?
- ergänzt er bei einem Bug einen sinnvollen Regressionstest?
- liefert er geforderte Evidence?
- trennt er Unsicherheit von gesicherten Tatsachen?
- stoppt er bei fehlendem Kontext oder nicht prüfbaren Bedingungen?

## Golden Tasks

Wiederkehrende Agentenfähigkeiten können mit kleinen repräsentativen Aufgaben geprüft werden.

Beispiele:

```text
small-bugfix
feature-with-existing-pattern
forbidden-scope-change
missing-requirement
architecture-decision-needed
failing-validator
parallel-task-conflict
```

Ein Golden Task enthält mindestens:

- definierten Ausgangszustand;
- Auftrag;
- relevante Regeln und Quellen;
- erwartete beobachtbare Verhaltensmerkmale;
- Grader oder Prüfschritte.

## Deterministische Grader bevorzugen

Wenn ein Ergebnis zuverlässig maschinenprüfbar ist, sollte ein deterministischer Check bevorzugt werden.

Beispiele:

- Test bestanden oder fehlgeschlagen;
- Datei verändert oder unverändert;
- öffentlicher Vertrag geändert oder nicht;
- erwartetes Artefakt vorhanden;
- JSON-Schema gültig;
- Linterverletzung vorhanden;
- Commit enthält geforderte Requirement-ID.

LLM-basierte Bewertung kann sinnvoll sein, wenn Qualität nicht vollständig deterministisch messbar ist. Sie sollte aber nicht eingesetzt werden, wenn ein einfacher reproduzierbarer Check dasselbe zuverlässiger leisten kann.

## Verhalten und Ergebnis getrennt bewerten

Ein Eval kann zwei Achsen besitzen:

### Ergebnisqualität

Ist das erzeugte Ergebnis fachlich und technisch korrekt?

### Prozessqualität

Hat der Agent den vorgesehenen Arbeitsprozess eingehalten?

Beispiel:

Ein Agent kann zufällig die richtige Codeänderung erzeugen und trotzdem durchfallen, wenn er dafür einen verbotenen Scope verändert oder eine notwendige Freigabe übersprungen hat.

## Negative Evals

Nicht nur Erfolgsszenarien prüfen.

Wichtig sind Aufgaben, bei denen der Agent **nicht** einfach weiterarbeiten soll.

Beispiele:

- widersprüchliche Requirements;
- fehlende Testbasis;
- notwendige Sicherheitsentscheidung;
- unklare Diff-Basis für Review;
- Zugriff auf nicht freigegebene Produktionsressource;
- gewünschte Änderung würde Datenverlust verursachen.

Erwartetes Verhalten kann dann ausdrücklich `STOP`, `ESCALATE` oder `REQUEST GATE` sein.

## Evals für Skill-Änderungen

Wenn zentrale Skills verändert werden, können Evals prüfen, ob sich das Verhalten verbessert oder verschlechtert.

Beispiel:

```text
tdd v1
→ Eval-Suite

tdd v2
→ gleiche Eval-Suite

Vergleich:
- Scope-Verstöße
- Testqualität
- Nachweisvollständigkeit
- unnötige Änderungen
- Erfolgsquote
```

Damit wird eine Skill-Änderung selbst überprüfbar.

## Keine Eval-Metrik als Selbstzweck

Eine Kennzahl ist nur nützlich, wenn sie ein relevantes Verhalten abbildet.

Nicht optimieren auf:

- möglichst viele Tool-Aufrufe;
- möglichst wenig Tokens ohne Rücksicht auf Qualität;
- möglichst viele Tests unabhängig von Aussagekraft;
- eine einzelne Gesamtnote ohne nachvollziehbare Kriterien.

## Qualitätscheck

Beim Aufbau eines Agent Evals prüfen:

1. Welches konkrete Agentenverhalten soll geprüft werden?
2. Ist der Ausgangszustand reproduzierbar?
3. Sind Erfolg und bewusstes Stoppen unterscheidbar?
4. Kann ein deterministischer Grader verwendet werden?
5. Werden Produkt- und Prozessqualität getrennt betrachtet?
6. Enthält die Suite auch Negativfälle und Gate-Situationen?
7. Würde eine Verschlechterung des Agentenverhaltens durch dieses Eval tatsächlich sichtbar?

## Leitgedanke

> Tests prüfen, ob die Software funktioniert. Agent Evals prüfen, ob der Agent zuverlässig zu prüfbarer Softwarearbeit beiträgt.