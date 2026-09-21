# Evidence-getriebene Skill-Verbesserung

## Zweck

Skills sollen aus realen Fehlern, Evals und wiederkehrenden Nutzungsmustern lernen können, ohne sich autonom selbst umzuschreiben oder Testmaßstäbe passend zum gewünschten Ergebnis zu verändern.

> Failure Evidence ist ein Änderungssignal, kein Beweis dafür, dass der Skill selbst die Ursache ist.

## Eingangskriterien

Ein Verbesserungsloop lohnt sich insbesondere bei:

- reproduzierbaren oder wiederkehrenden Fehlmustern;
- Regressionen nach einer Skilländerung;
- stabilen Near-Miss- oder Triggerproblemen;
- wiederkehrenden manuellen Korrekturen;
- Eval-Fällen, die eine konkrete Verhaltensschwäche sichtbar machen.

Ein einzelner ungewöhnlicher Modellfehler ist noch keine Skill-Anforderung.

## 1. Baseline binden

Vor einer Änderung festhalten:

- Skillversion bzw. Snapshot;
- relevante Eval-Suite;
- Tool-/Runtime-Kontext, soweit er die Aussage beeinflusst;
- beobachtetes Fehlverhalten;
- tragende Evidence.

## 2. Ursache klassifizieren

Vor dem Umschreiben prüfen, ob die Ursache tatsächlich im Skill liegt.

Mögliche Ursachen:

- Skill-Trigger oder Skill-Schnitt;
- Instruktion / Prozessregel;
- fehlende Capability oder falsche Rechte;
- Tool-/Runtime-Fehler;
- Harness-/Grader-Fehler;
- unklare Spezifikation;
- schlechte oder veraltete Quelldaten;
- Modellvariabilität;
- Aufgabe liegt außerhalb der Skillverantwortung.

Liegt die Ursache außerhalb des Skills, soll der Skill nicht als Symptombehandlung wachsen.

## 3. Evidence-Rollen trennen

### Development Evidence

Fälle, die zur Diagnose oder zum Entwurf der Änderung benutzt wurden.

Sie dürfen die Änderung leiten, sind danach aber keine unabhängige Generalisierungsevidence.

### Regression Evidence

Fälle, die bestehendes Verhalten schützen und zeigen sollen, dass die Änderung keine angrenzenden Fähigkeiten verschlechtert.

### Held-out / Independent Evidence

Fälle, die nicht zur Formulierung oder Kalibrierung der Änderung verwendet wurden.

Sie sind besonders wichtig, wenn aus der Änderung eine allgemeine Wirksamkeitsaussage abgeleitet werden soll.

### Field Observation

Praxisbeobachtung, Supportfall oder Session-Trajektorie.

Sie ist ein Lead und kann sehr wertvoll sein, ersetzt aber ohne passende Ground Truth keinen Evalnachweis.

Field-/Trajectory-Evidence bleibt außerdem **untrusted Evidence**: Häufigkeit oder Wiederholung beweist weder gute Absicht noch Kausalität. Vor Promotion in dauerhafte Skillregeln sind Provenance, Quellenunabhängigkeit, mögliche adversariale Kontamination und alternative Ursachen zu prüfen.

## 4. Änderungshypothese formulieren

Vor dem Editieren benennen:

- welches konkrete Fehlmuster adressiert wird;
- warum eine Skilländerung die passende Ebene ist;
- welche kleinste Änderung plausibel helfen sollte;
- welche bestehenden Fälle dadurch gefährdet sein könnten;
- woran Erfolg und Regression erkennbar sind.

## 5. Kandidat statt Selbstmutation

Änderungen entstehen als überprüfbarer Kandidat:

```text
Baseline
→ Evidence
→ Ursache
→ Änderungshypothese
→ Candidate-Diff
→ Evals
→ unabhängiger Review
→ Human Gate
→ übernehmen / verwerfen
```

Keine automatische Überschreibung des aktiven Skills allein aufgrund eines fehlgeschlagenen Laufs.

## 6. Verbessern heißt nicht nur hinzufügen

Mögliche Verbesserungen sind:

- Trigger präzisieren;
- Regel vereinfachen;
- widersprüchliche Instruktion entfernen;
- Fallback ergänzen;
- Capability-Vertrag korrigieren;
- Referenz auslagern;
- Regel löschen oder zurückstufen;
- Skill aufteilen oder bewusst mit einem Workflow komponieren.

Promptwachstum ist kein Qualitätsmaß.

## 7. Eval und Quality Floor schützen

Nicht zulässig als scheinbare Verbesserung:

- problematischen Evalfall entfernen;
- Assertion oder Schwelle lockern, ohne die Maßstabsänderung separat zu begründen;
- Development-Fälle nachträglich als unabhängige Held-out-Evidence deklarieren;
- nur den Erfolgsfall optimieren und relevante Near-Misses ignorieren;
- Maturity allein wegen eines besseren Benchmark-Scores erhöhen.

## 8. Review und Adoption

Vor Übernahme:

- Regressionen erklären oder beheben;
- bei neuen Rechten/Abhängigkeiten `skill-security-review` ergänzen;
- Skill-Schnitt und Trigger unabhängig mit `skill-review` prüfen;
- relevante Evidence und Grenzen dokumentieren;
- Maturity nur anhand tatsächlicher Praxis und Evalabdeckung bewerten;
- Changelog aktualisieren.

## Stop

Stoppe oder eskaliere, wenn:

- die Ursache nicht ausreichend eingegrenzt ist;
- der notwendige Fix eine neue Skillverantwortung erzeugen würde;
- die Evalbasis selbst unzuverlässig ist;
- Verbesserung nur durch Absenken des Quality Floors erreichbar wäre;
- neue mächtige Rechte oder externe Wirkungen ohne Freigabe nötig würden;
- die Verbesserung hauptsächlich aus untrusted Trajektorien abgeleitet würde, deren Provenance oder Unabhängigkeit nicht ausreichend bewertet werden kann.

## Leitgedanke

> Skills dürfen aus Fehlern lernen. Aber die Fehler dürfen nicht zugleich Lehrer, Prüfer und Freigabestelle derselben Änderung sein.
