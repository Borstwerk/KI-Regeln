# Skill-Verbesserung aus Evals und Fehlern

## Zweck

Wiederkehrende Fehler, Eval-Funde oder belastbare Praxisbeobachtungen in kontrollierte Skillverbesserungen überführen, ohne aktive Skills autonom selbst zu verändern.

## Einstieg

Geeignet, wenn:

- ein Skill wiederholt ähnlich scheitert;
- ein Eval eine konkrete Verhaltensschwäche zeigt;
- ein Upstream-/Methodenfund eine bestehende Skillregel plausibel verbessert;
- mehrere Praxisfälle auf dieselbe Skill-Lücke hinweisen.

Nicht verwenden, wenn nur ein einzelner unspezifischer Modellfehler vorliegt oder die Ursache erkennbar außerhalb des Skills liegt.

## Workflow

```text
Baseline + Evidence
        ↓
Ursache klassifizieren
        ↓
Skillproblem?
├─ nein → richtige Ebene bearbeiten / stoppen
└─ ja
    ↓
Änderungshypothese
    ↓
Candidate-Diff
    ↓
Development-/Regression-/Held-out-Evidence trennen
    ↓
Evals + Verification
    ↓
unabhängiger Skill-Review
    ↓
ggf. Security Review
    ↓
Human Gate
    ↓
übernehmen / verwerfen / weiter beobachten
```

## 1. Baseline und Evidence

Festhalten:

- aktueller Skill-Snapshot;
- betroffene Eval-/Praxisfälle;
- aktueller Output bzw. Fehlmodus;
- relevante Tool-/Runtimebedingungen;
- vorhandene Regression-Suite.

## 2. Ursache prüfen

Mit `Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md` klären, ob der Fehler aus Skill, Tooling, Runtime, Daten, Harness, Spezifikation oder anderer Ebene stammt.

Keine Skilländerung nur deshalb, weil sie der bequemste Edit wäre.

## 3. Änderungskandidat

`skill-authoring` für eine kleine, klar begründete Änderung verwenden.

Vorab formulieren:

- Failure Pattern;
- Root-Cause-Hypothese;
- erwartete Wirkung;
- mögliche Nebenwirkungen;
- Prüfkriterien.

## 4. Evidence partitionieren

- Development-Fälle dürfen die Änderung leiten.
- Regression-Fälle schützen bestehendes Verhalten.
- Held-out-/Independent-Fälle dürfen nicht aus denselben Fällen bestehen, anhand derer die Änderung entworfen wurde, wenn daraus ein Generalisierungsclaim folgen soll.

## 5. Prüfen

`agent-eval` und bei iterativer Umsetzung `verification-loop` verwenden.

Dabei:

- tragende Checks nicht still abschwächen;
- gleiche relevante Baseline vor/nach der Änderung verwenden;
- neue Evals nur dort ergänzen, wo das Fehlmuster eine echte wiederkehrende Anforderung belegt;
- bei fehlender unabhängiger Evidence den Claim entsprechend begrenzen.

## 6. Review

`skill-review` unabhängig auf Scope, Trigger, Verträge, Komposition und Regressionen anwenden.

Wenn neue Rechte, Scripts, Remote-Abhängigkeiten oder Außenwirkungen entstehen, zusätzlich `skill-security-review`.

## 7. Human Gate und Lifecycle

Vor Adoption:

- Diff und Evidence sichtbar machen;
- offene Unsicherheiten benennen;
- Maturity separat bewerten;
- Changelog pflegen;
- bei extern beeinflusster Methode Quellen-/Upstream-Klassifikation prüfen.

## Harte Grenzen

- kein automatisches Merge oder Self-Update aufgrund eines Fehlers;
- kein „Eval bestanden“ durch Lockern des Evalmaßstabs;
- keine Maturity-Hochstufung allein aufgrund eines besseren Scores;
- keine unendliche Anreicherung des Prompts ohne Scope-/Komplexitätsprüfung;
- keine Nutzung derselben Fälle als Entwicklungsinput und unabhängige Erfolgsevidence ohne klare Kennzeichnung.

## Ergebnis

Mindestens:

- Failure Pattern;
- Root-Cause-Klassifikation;
- Änderungshypothese;
- Candidate-Diff;
- Evidence-Rollen;
- Regression-/Held-out-Status;
- Reviewfunde;
- Entscheidung: übernehmen / verwerfen / beobachten;
- verbleibende Unsicherheit.

## Leitgedanke

> Aus Fehlern lernen heißt nicht, jedem Fehler hinterherzupatchen. Es heißt, wiederkehrende Evidence kontrolliert in bessere Regeln zu übersetzen.
