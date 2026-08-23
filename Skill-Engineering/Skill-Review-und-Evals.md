# Skill Review und Evals

## Grundsatz

> Ein Skill wird nicht dadurch gut, dass seine Anweisungen plausibel klingen.

Er muss gegen typische Aufgaben, Grenzfälle und Fehlanwendungen geprüft werden.

## Review-Achsen

### 1. Scope

- Ist die Verantwortung klar?
- Überlappt der Skill unnötig mit anderen?
- enthält er Projektwahrheit?

### 2. Trigger

- triggert er bei typischen positiven Fällen?
- bleibt er bei Near-Miss-Fällen inaktiv?
- ist die Description verständlich ohne interne Skillnamen?

### 3. Prozess

- sind harte Gates und Stop-Regeln vorhanden?
- wird fehlende Evidenz ehrlich behandelt?
- vermeidet der Skill unnötige Schritte?

### 4. Capabilities

- sind Voraussetzungen realistisch?
- existieren Fallbacks?
- verlangt der Skill mehr Rechte als nötig?

### 5. Output / Evidence

- ist ein prüfbares Ergebnis definiert?
- werden Erfolg und bloße Durchführung unterschieden?

### 6. Komposition

- sind Abhängigkeiten nachvollziehbar?
- startet der Skill versteckt weitere Aufgaben?

## Eval-Klassen

### Trigger-Evals

Prüfen Aktivierung und Nichtaktivierung.

### Behavior-Evals

Prüfen konkrete Arbeitsweise:

- Scope-Treue;
- Quellen-/Evidence-Verhalten;
- Stop-Gates;
- Tooldisziplin;
- Umgang mit Unsicherheit.

### Outcome-Evals

Prüfen Ergebnisqualität gegen Akzeptanzkriterien oder Golden Tasks.

### Regression-Evals

Vergleichen Skillversionen, damit eine Verbesserung nicht an anderer Stelle Verhalten verschlechtert.

## Positive und negative Fälle

Jeder wichtige Skill sollte mindestens enthalten:

- typischen Erfolgsfall;
- paraphrasierten Erfolgsfall;
- Near-Miss, der nicht triggern darf;
- Fall mit fehlender Capability;
- Fall mit fehlender Pflichtinformation;
- mindestens einen schwierigen oder widersprüchlichen Fall.

## Deterministisch vor subjektiv

Was automatisiert oder regelbasiert geprüft werden kann, sollte nicht ausschließlich durch freie LLM-Bewertung erfolgen.

Beispiele:

- gültiges Frontmatter;
- erlaubte Dateipfade;
- fehlende Pflichtfelder;
- nicht erlaubte Toolrechte;
- erwartete Outputdatei;
- ausgeführter Teststatus.

Subjektive Qualitätsurteile bleiben dort sinnvoll, wo echte Wirkung, Stil oder fachliche Angemessenheit beurteilt werden muss.

## Änderungsgate

Bei wesentlichen Skilländerungen:

```text
Änderung
→ betroffene Evals identifizieren
→ vorher/nachher vergleichen
→ Regressionen erklären oder beheben
→ Maturity prüfen
→ Changelog
```

## Leitgedanke

> Skills werden an Verhalten gemessen, nicht an der Eleganz ihrer Prompt-Prosa.
