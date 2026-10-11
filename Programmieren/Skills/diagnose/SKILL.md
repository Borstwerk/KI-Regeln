---
name: diagnose
description: Disziplinierte Fehlerdiagnose für KI-gestützte Softwarearbeit. Verwenden bei Bugs, Regressionen, sporadischem Verhalten oder Performanceproblemen, bevor ein Fix geraten wird.
---

# Fehlerdiagnose

Ziel ist ein Root-Cause-Fix mit belastbarem Nachweis.

## 1. Reproduzierbaren Nachweis bauen

Vor Hypothesen einen möglichst engen Pass/Fail-Nachweis erstellen, der das gemeldete Symptom tatsächlich treffen kann.

Bevorzugte Reihenfolge:

1. fehlender automatisierter Regressionstest an einer echten fachlichen Grenze;
2. bestehender Test mit minimalem neuen Fixture;
3. kleiner CLI-, Datei-, API- oder DB-Harness;
4. reproduzierbarer UI-Schritt, wenn Automatisierung nicht sinnvoll möglich ist;
5. bei Performanceproblemen ein Messharness statt bloßer Logausgabe.

Wenn kein belastbarer Repro möglich ist, bisherige Versuche und benötigte Information oder Umgebung benennen.

Nicht aus Code-Lektüre allein einen Fix erraten, wenn das Problem überprüfbar gemacht werden kann.

## 2. Repro minimieren

Den Fehlerfall auf das kleinste noch fehlschlagende Szenario reduzieren.

Eingaben, Daten, Schritte und Abhängigkeiten einzeln entfernen und nach jedem Schritt erneut prüfen.

## 3. Hypothesen bilden

Mehrere falsifizierbare Ursachen priorisieren.

Für jede Hypothese angeben:

- warum sie plausibel ist;
- welche Beobachtung sie bestätigen würde;
- welche Beobachtung sie widerlegen würde;
- wie sie möglichst direkt geprüft werden kann.

Keine Einzelhypothese als Tatsache behandeln, bevor der Repro sie stützt.

## 4. Gezielt instrumentieren

Nur Messungen oder Logs hinzufügen, die konkrete Hypothesen unterscheiden.

- keine flächendeckende Debug-Ausgabe ohne Fragestellung;
- keine Secrets oder personenbezogenen Geschäftsdaten in Logs;
- temporäre Instrumentierung markieren und vor Abschluss entfernen;
- bei Performanceproblemen messen oder profilen statt Logmengen zu erzeugen.

## 5. Regressionstest vor Fix

Wenn eine geeignete Testgrenze existiert:

1. minimalen Repro als Regressionstest festhalten;
2. rot bestätigen;
3. Ursache beheben;
4. Test grün bestätigen;
5. ursprünglichen breiteren Repro erneut ausführen.

Existiert keine sinnvolle Testgrenze, diese Nachweisgrenze ausdrücklich dokumentieren statt einen wertlosen Test gegen Interna zu erzwingen.

## 6. Reparaturplan bei risikoreichen Änderungen

Bei Daten-/Security-/Produktionswirkung, unklarer Ursache, breiten Änderungen oder Vertrags-/Architekturwirkung **vor dem Fix** einen überprüfbaren Plan festhalten: Repro, Root-Cause-Evidence, begrenzte Änderung, Regressionstest, Risiken, Backout, offene Fragen.

Ein unabhängiger Planreview kann fehlerhafte Ursachenannahmen entdecken, bevor sie implementiert werden. Wo der lokale Prozess eine Freigabe verlangt, **kein WRITE vor dem tatsächlichen Plan-Gate**. Same-Model-Review nicht als unabhängige Prüfung ausgeben.

Bei minimalem risikoarmem Fix genügt die proportionale Planung; **keine pauschale Pflicht zur Multi-Agent-Delegation**. Wesentliche neue Diagnose-/Scope-Fakten machen den alten Plan prüfbedürftig.

## 7. Fix-Regeln

- Ursache beheben, nicht Symptom verdecken.
- Keine Validierung abschalten.
- Keine Daten still reparieren oder heuristisch umdeuten, sofern die Anforderung das nicht ausdrücklich verlangt.
- Keine fremden Bereiche refactoren.
- Führt die Diagnose zu einer größeren Verhaltens- oder Architekturänderung, zurück in die Planungsphase.

## 8. Stagnation und Circuit Breaker

Bei wiederholt gleichem substanziellem Review-Finding, fehlender Konvergenz oder neuen gleich schweren Fehlern die Wiederholung stoppen. Statt „noch einmal raten“: Repro und Hypothesen prüfen, fokussierten Handoff erstellen und gegebenenfalls neuen Planreview/Human Gate einholen. Bereits ab einem kritischen Risiko kann sofortiger Stopp nötig sein. Zwei erfolglose materielle Runden sind eine Heuristik, keine starre globale Zahl.

Nicht die Test- oder Oracle-Definition ändern, um den aktuellen Fix passend zu machen. Ein begründeter Testfehler benötigt unabhängigen Review.

## 9. Brechprobe und Abschluss

Bei kritischen Regressionen den Fix oder Schutz probeweise wieder entfernen und bestätigen, dass der Regressionstest rot wird.

Im Abschlussbericht nennen:

- reproduziertes Symptom;
- bestätigte Ursache;
- wesentliche verworfene Hypothesen, soweit relevant;
- Regressionstest oder anderer Nachweis;
- Brechprobe;
- geänderte Bereiche;
- vollständigen Prüflauf;
- verbleibende manuelle Prüfungen.