# Trigger und Description Design

## Zweck

Die Description ist nicht nur Dokumentation. Sie ist ein Teil der Aktivierungslogik eines Skills.

Sie soll beantworten:

1. Was tut der Skill?
2. Wann soll er verwendet werden?
3. Welche nahe liegenden Aufgaben gehören ausdrücklich nicht dazu?

## Gute Trigger

Trigger sollen auf **Nutzerintention und Aufgabenform** zielen, nicht bloß auf einzelne Schlüsselwörter.

Schwach:

```text
Use when the user says "review".
```

Besser:

```text
Prüft einen konkreten Code-Diff gegen Anforderungen und Repository-Standards. Verwenden bei PR-, Branch- oder Diff-Reviews; nicht für allgemeine Architekturberatung ohne tatsächliche Änderung.
```

## Positive und negative Beispiele

Für wichtige Skills sollen Evalfälle beide Seiten enthalten:

### Positive Trigger

- klare typische Anfrage;
- paraphrasierte Anfrage;
- Anfrage ohne Skillnamen;
- Grenzfall, bei dem der Skill trotzdem nötig ist.

### Near-Miss Negatives

- ähnlicher Begriff, aber andere Aufgabe;
- Input ist nur Quelle statt gewünschter Output;
- reine Beratung statt Durchführung;
- kleiner Fakt statt Deep Research;
- Designkritik statt Design-to-Code.

## Übertriggerung vermeiden

Ein Skill ist schlecht geschnitten, wenn er jede Anfrage eines großen Themenfelds an sich zieht.

Beispiele:

- `technical-writing` darf nicht jede Frage zu Technik übernehmen;
- `deep-research` darf nicht jeden Faktenlookup kapern;
- `frontend-design` darf nicht bei jeder React-Datei triggern.

## Untertriggerung vermeiden

Description nicht nur mit internen Fachbegriffen formulieren.

Ein Nutzer kann sagen:

- „prüf die Quellen“ statt `citation-audit`;
- „warum ist das langsam?“ statt `diagnose`;
- „mach die Seite weniger generisch“ statt `frontend-design`.

## Description-Hygiene

Descriptions sollen:

- konkret;
- kompakt;
- handlungsorientiert;
- ohne Marketing;
- ohne unnötige Toolnamen

formuliert werden.

Sie sollen nicht versuchen, den vollständigen Skillprozess in Metadaten zu quetschen.

## Trigger-Konflikte

Wenn zwei Skills dieselbe Anfrage plausibel beanspruchen:

1. prüfen, ob ihre Grenzen falsch geschnitten sind;
2. Prioritäts- oder Routingregel dokumentieren;
3. ggf. einen Workflow statt eines Meta-Skills verwenden;
4. Konflikt mit Evalfällen absichern.

## Leitgedanke

> Ein Skill ist gut auffindbar, wenn er bei seiner Aufgabe zuverlässig erscheint – und bei der Nachbaraufgabe zuverlässig schweigt.
