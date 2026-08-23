# Workflow – Bugdiagnose

## Ziel

Ein reales Defektbild reproduzierbar diagnostizieren, minimal beheben und gegen Regression absichern.

## Skill-Kette

```text
diagnose
→ optional domain-modeling bei unklarer Fachbedeutung
→ Fix
→ verification-loop
→ code-review
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

## 3. Fix

Kleinste Änderung, die die bestätigte Ursache adressiert.

Wo eine korrekte Testnaht existiert:

- Regressionstest vor oder gemeinsam mit Fix;
- ursprünglichen Repro danach erneut ausführen.

## 4. Verification Loop

`verification-loop`

Prüft:

- ursprüngliches Symptom beseitigt;
- Regressionstest grün;
- relevante Nachbartests grün;
- Debug-Instrumentierung entfernt;
- keine neue unerwartete Wirkung.

## 5. Review

`code-review`

Prüft insbesondere:

- Fix trifft Root Cause statt Symptom;
- kein unnötiger Scope;
- keine fragile Sonderbehandlung ohne Begründung.

## Blocker

Wenn das echte Symptom nicht reproduziert oder anderweitig belastbar beobachtet werden kann, keine erfundene Root Cause als Ergebnis verkaufen.
