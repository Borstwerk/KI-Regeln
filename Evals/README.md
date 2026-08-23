# Evals

Dieser Bereich enthält wiederholbare Testfälle für zentrale Skills.

## Ziel

> Skillqualität wird an beobachtbarem Verhalten geprüft, nicht nur an plausiblen Anweisungen.

Evals sollen insbesondere Regressionen erkennen bei:

- Triggerung und Nichttriggerung;
- Scope-Treue;
- Tool- und Capability-Verhalten;
- Evidence- und Quellenhygiene;
- Stop-/Eskalationsgates;
- Outputqualität;
- Sicherheitsgrenzen.

## Eval-Klassen

### Trigger

Prüft, ob ein Skill bei passenden Aufgaben gewählt wird und bei Near-Misses nicht.

### Behavior

Prüft den Arbeitsprozess, z. B.:

- öffnet Quellen statt nur Snippets zu verwenden;
- reproduziert einen Bug vor Hypothesenbildung;
- schreibt bei Review nicht ungefragt um;
- behauptet keine Capability, die nicht verfügbar ist.

### Outcome

Prüft das Ergebnis gegen konkrete Akzeptanzkriterien.

### Regression

Vergleicht bekannte Skillstände oder Verhalten vor/nach einer Änderung.

## Verzeichnisstruktur

```text
Evals/
├── README.md
├── eval-case.schema.yml
└── <Bereich>/
    └── <skill-id>/
        └── cases.yml
```

## Fallstruktur

Jeder Fall beschreibt mindestens:

- `id`;
- `class`;
- `input`;
- `should_trigger`;
- erwartete Verhaltenspunkte;
- verbotene Verhaltenspunkte;
- erwarteten Abschlussstatus.

Nicht jeder Eval muss vollautomatisch sein. Die Struktur soll jedoch so konkret sein, dass zwei Reviewer denselben Fall ähnlich beurteilen können.

## Minimalset für einen Kernskill

Mindestens:

1. typischer positiver Trigger;
2. paraphrasierter positiver Trigger;
3. Near-Miss-Negativfall;
4. fehlende Capability oder Pflichtinformation;
5. schwieriger fachlicher Fall.

## Bewertung

Empfohlene Statuswerte:

- `pass`;
- `partial`;
- `fail`;
- `blocked`.

Ein Skill gilt nicht automatisch als `stable`, nur weil wenige Beispielcases bestehen.

## Pflege

Bei verhaltensändernden Skilländerungen:

```text
betroffene Evals bestimmen
→ alten Stand ausführen / bekannte Baseline betrachten
→ neuen Stand ausführen
→ Regressionen prüfen
→ Skill-Maturity neu bewerten
→ Changelog
```

## Leitgedanke

> Ein Eval soll eine konkrete Fehlermöglichkeit sichtbar machen – nicht nur bestätigen, dass der Skill im Happy Path nett aussieht.
