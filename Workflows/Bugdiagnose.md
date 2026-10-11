# Workflow – Bugdiagnose

## Ziel

Ein reales Defektbild reproduzierbar diagnostizieren, minimal beheben und gegen Regression absichern.

## Skill-Kette

```text
diagnose
→ optional domain-modeling bei unklarer Fachbedeutung
→ risikobasierter Reparaturplan + Plan-Review-Gate
→ Fix innerhalb des akzeptierten Scopes
→ verification-loop
→ code-review bei nichttrivialer oder risikoreicher Codeänderung
```

## 1. Diagnose

`diagnose`

Priorität:

```text
Feedback-Loop bauen
→ tatsächliches Symptom reproduzieren
→ minimieren
→ mehrere falsifizierbare Hypothesen
→ gezielte Instrumentierung
→ Root Cause
```

Nicht zuerst Code lesen und eine plausible Geschichte erzählen.

## 2. Sicherheits-/Datenschutzgrenze

Logs, HARs, Traces und Dumps vor Weitergabe redigieren.

Bei Dritt-Scripts oder externen Reprotools ggf. Security Review.

## 3. Risikobasierter Reparaturplan – vor dem Fix

**Kein Pflicht-Meeting für Kleinkram:** Bei einem eng begrenzten, niedrig-riskanten und bereits belegten Fix kann ein kurzer dokumentierter Plan mit direkter Ausführung genügen. Nicht jeden Tippfehler als Multi-Agent-Hospital behandeln.

Ein **explizites Plan-Review-Gate vor dem ersten WRITE** ist insbesondere erforderlich, wenn:

- Datenmigration, Verlust-/Sicherheits-/Berechtigungsrisiko oder Produktionswirkung betroffen sind;
- mehrere Module, bestehende Verträge oder Architektur betroffen sind;
- der Fix invasive Refactorings statt eines engen Ursachenfixes verlangt;
- Root Cause, Repro oder Änderungswirkung noch wesentlich unsicher sind;
- der lokale Projektprozess ohnehin eine Planfreigabe verlangt.

### Minimaler Behandlungsplan

- belegtes Symptom und Repro-/Mess-Evidence, oder dokumentiertes Missingness;
- favorisierte Root-Cause-Hypothese **und** relevante verworfene Alternativen;
- betroffene Dateien/Komponenten, explizit nicht zu ändernder Scope;
- kleinster Fix und geplanter Regressionstest samt Brechprobe;
- Risiken, Backout und erforderliche READ/WRITE/ACTION-Gates;
- offene Fragen, unabhängiger Reviewer und Status.

Bei risikoreichem Scope: **Plan REVIEWED / APPROVED erst nach tatsächlicher Prüfung**, idealerweise durch andere Agenteninstanz oder Menschen mit eigenständigem Auftrag. Same-Model-Review als solchen ausweisen; kein erfundener unabhängiger Reviewer.

Review verwirft Pläne ohne belastbaren Zusammenhang zwischen Ursache, Eingriff und Acceptance. Bei ungenügender Evidence: zurück zur Diagnose statt einen spekulativen Fix zu bewilligen. Wenn während der Implementierung neue wesentliche Fakten oder Scope-Änderungen entstehen, **WRITE stoppen, Plan anpassen und das erforderliche Gate erneut durchlaufen**.

Ein Planreview erteilt noch keine Commit-/Merge-/Release- oder Produktionsfreigabe.

## 4. Fix

Kleinste Änderung, die die bestätigte Ursache adressiert.

Wo eine korrekte Testnaht existiert:

- Regressionstest vor oder gemeinsam mit Fix;
- ursprünglichen Repro danach erneut ausführen.

## 5. Verification Loop

`verification-loop`

Prüft:

- ursprüngliches Symptom beseitigt;
- Regressionstest grün;
- relevante Nachbartests grün;
- Debug-Instrumentierung entfernt;
- keine neue unerwartete Wirkung.

## 6. Review

`code-review` verwenden, wenn Quellcode geändert wurde und der Fix nicht trivial ist, relevante Nachbarlogik berührt oder ein zusätzlicher unabhängiger Review materiell Risiko senkt.

Prüft dann insbesondere:

- Fix trifft Root Cause statt Symptom;
- kein unnötiger Scope;
- keine fragile Sonderbehandlung ohne Begründung.

Bei einer eng begrenzten Konfigurations- oder Datendatei-Korrektur mit deterministischem Akzeptanzcheck und ohne Codeänderung ist `code-review` kein Pflichtschritt.

## 7. Circuit Breaker bei nicht konvergierenden Fixes

Wird dieselbe substanzielle Kritik **wiederholt** nicht gelöst, oder erzeugen Reparaturen neue gleich schwere Defekte, **nicht** endlos neu implementieren. Bei beispielsweise zwei erfolglosen materiell gleichen Reviewrunden:

1. Run/Plan/Tests/Findings in einem kompakten Handoff festhalten;
2. prüfen, ob Repro, Ursache, Prüforakel oder vereinbarter Scope falsch sind;
3. an Diagnose, Plan-Review oder erforderlichen menschlichen Entscheider eskalieren;
4. erst nach neuem begrenzten Plan weiterschreiben.

Die Zahl zwei ist ein **Warnsignal**, kein globales starres Maximum. Ein einzelnes kritisches Sicherheitsfinding kann sofort STOP erfordern. Dagegen ist eine normale kleine Reviewkorrektur kein Grund für Eskalation.

Keine Tests, Thresholds, Fixtures oder Reviewkriterien still abschwächen, nur damit ein Fix „grün“ erscheint. Ein tatsächlich defekter Test benötigt einen **eigenständigen begründeten Review**.

## Blocker

Wenn das echte Symptom nicht reproduziert oder anderweitig belastbar beobachtet werden kann, keine erfundene Root Cause als Ergebnis verkaufen.
