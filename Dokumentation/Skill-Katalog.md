# Skill-Katalog und Maturity

## Zweck

`../skill-catalog.yml` ist das maschinenlesbare Inventar der zentralen Skills.

Das menschliche `Skill-Handbuch.md` beantwortet vor allem:

> Welcher Skill hilft mir bei welcher Aufgabe?

Der Skill-Katalog beantwortet zusätzlich:

> Welche Skills existieren, wo liegen sie, wie reif sind sie und welche Fähigkeiten benötigen sie?

## Maturity

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

### experimental

Neue oder wesentlich umgebaute Skilllogik. Quellen und Design sind plausibel, aber Praxis-/Evalabdeckung ist noch begrenzt.

### candidate

Bereits praktisch verwendet oder mehrfach geprüft, aber noch nicht durch ausreichende Regressionsevals als stabil abgesichert.

### stable

Wiederholt praktisch bewährt und mit relevanten Evalklassen abgesichert. Keine bekannten schweren Trigger-, Scope-, Sicherheits- oder Outputprobleme.

### deprecated

Für neue Nutzung nicht mehr empfohlen. Ersatz oder Migration ist dokumentiert.

### retired

Nicht mehr aktiv angeboten. Historie bleibt nachvollziehbar.

## Eval Coverage

Empfohlene Werte:

- `none` – keine formalen Evalfälle im zentralen Evalbestand;
- `partial` – einige zentrale Trigger-/Behavior-/Outcome-Fälle vorhanden;
- `core` – wesentliche positive, negative und schwierige Kernfälle vorhanden;
- `broad` – zusätzlich umfangreiche Regressionen und Varianten.

Maturity und Eval Coverage sind nicht identisch. Ein Skill kann viel Praxis haben und trotzdem noch unzureichende formale Evals besitzen.

## Capabilities

Der Katalog kann Fähigkeiten nennen, die für einen Skill relevant sind, z. B.:

- `web-required`;
- `browser-required`;
- `repository-read`;
- `code-execution`;
- `source-of-truth-access`.

Diese Angaben ersetzen nicht die detaillierten Fallback- und Rechte-Regeln des Skills.

## Pflege

Bei folgenden Änderungen `skill-catalog.yml` prüfen:

- neuer Skill;
- Skill umbenannt oder verschoben;
- Maturity geändert;
- Evalabdeckung verändert;
- Capability-Anforderung wesentlich geändert;
- Skill deprecated oder retired.

## Reife-Gate

Eine Hochstufung soll begründet werden.

Insbesondere `stable` erfordert mindestens:

1. wiederholte reale Nutzung oder belastbare Golden Tasks;
2. relevante positive und Near-Miss-Trigger-Evals;
3. Behavior-/Outcome-Prüfung der Kernfunktion;
4. keine offenen Blocker aus `skill-review`;
5. dokumentierte Capability-/Fallback-Grenzen;
6. Sicherheitsreview, wenn der Skill externe Inhalte, Tools oder Schreib-/Ausführungsrechte nutzt.

## Leitgedanke

> Der Katalog sagt nicht nur, was wir haben – sondern wie viel Vertrauen der aktuelle Reifegrad rechtfertigt.
