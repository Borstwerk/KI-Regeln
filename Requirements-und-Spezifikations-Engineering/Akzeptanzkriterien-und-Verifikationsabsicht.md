# Akzeptanzkriterien und Verifikationsabsicht

## Zweck

Acceptance Criteria konkretisieren, unter welchen beobachtbaren Bedingungen ein Requirement als erfüllt beurteilt werden kann. Sie sind noch keine vollständige Teststrategie oder Testimplementierung.

## Gute Acceptance Criteria

Sie sollten, soweit relevant:

- auf ein konkretes Requirement oder Szenario zurückführbar sein;
- beobachtbares Ergebnis statt interne Implementierung beschreiben;
- relevante Preconditions oder Bedingungen nennen;
- positive und wichtige negative/alternative Fälle abdecken;
- klare Grenzen oder Toleranzen nur aus bestätigter Quelle verwenden;
- unabhängig genug sein, dass ein Reviewer die Erfüllung beurteilen kann.

## Formate

Mögliche Formen:

- kurze Checkliste;
- Given / When / Then;
- EARS-artige Formulierung;
- Beispieltabelle / Example Mapping;
- mathematische oder tabellarische Bedingung;
- Verweis auf autoritative Policy/Contract-Eigenschaft.

Kein Format ist Pflicht. Syntaxqualität ersetzt keine fachliche Richtigkeit.

## Verification Intent

Schon beim Requirement sollte geklärt werden, wie Erfüllung prinzipiell belegbar wäre, zum Beispiel durch:

- Test;
- Analyse;
- Inspektion;
- Demonstration;
- Kombination daraus.

Diese Einordnung ist Planungs- und Qualitäts-Evidence. `Testing-und-QA/` entscheidet anschließend über konkrete Testebene, Testdesign, Daten, Automation und Ausführung.

## Acceptance Criterion ≠ Test Case

```text
Acceptance Criterion
→ welche beobachtbare Bedingung erfüllt sein muss

Test Case
→ konkrete Stimuli, Daten, Environment, Schritte und Oracle zur Prüfung
```

Ein Criterion kann mehrere Tests benötigen; ein Test kann mehrere Criteria berühren.

## Nicht tun

- aus fehlenden Requirements eigene Schwellen erfinden;
- Implementation Details als Acceptance Criteria festschreiben, solange sie nicht selbst Constraint sind;
- `Given/When/Then` als Qualitätsbeweis behandeln;
- nur Happy Path abdecken, wenn relevante Failure Cases bekannt sind;
- grüne Tests mit vollständiger Requirement Validation gleichsetzen.

## Leitgedanke

> Acceptance Criteria machen Erfüllung beurteilbar – Testing macht daraus belastbare Prüfung.