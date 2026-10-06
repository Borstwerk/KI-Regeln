---
name: verification-loop
description: Führt innerhalb eines freigegebenen Scopes einen kontrollierten Arbeiten-Prüfen-Diagnose-Korrigieren-Loop mit klaren Stop-Kriterien aus. Verwenden bei iterativer Umsetzung, wenn nach jedem Änderungsschritt reproduzierbare Nachweise möglich sind.
---

# Verification Loop

Nutze `../../Task-Graph-und-Loops.md` und `../../Human-Gates-und-Freigaben.md`.

## Voraussetzungen

Vor dem Start müssen klar sein:

- freigegebener Scope;
- erwarteter Ausgangszustand;
- konkrete Nachweise;
- relevante Checks, Gates oder Schwellenwerte, soweit sie den Completion Claim tragen;
- Stop- und Eskalationsbedingungen.

## Loop

```text
Arbeiten
→ Prüfen
→ bestanden? → fertig
→ nicht bestanden → Diagnose
→ Korrektur
→ erneut prüfen
```

## Regeln

- Nur innerhalb des freigegebenen Scopes korrigieren.
- Fehlerursache vor Symptombehandlung prüfen.
- Tests oder Validierungen nicht abschwächen, um den Loop zu beenden.
- Fehlende Spezifikation nicht eigenmächtig ersetzen.
- Einen nicht ausgeführten Nachweis nicht als bestanden behandeln.
- Nach jeder Korrektur denselben relevanten Nachweis erneut ausführen.
- Änderungen an Tests, Validatoren, Filtern, Schwellenwerten oder Gate-Konfigurationen als eigene relevante Änderung behandeln, wenn sie die Aussagekraft des Nachweises beeinflussen.

## Guardrail- und Quality-Floor-Integrität

Ein grüner Status ist nur mit dem vorherigen Qualitätsmaßstab vergleichbar, wenn der maßgebliche Check nicht still abgeschwächt wurde.

Typische Guardrail-Änderungen sind beispielsweise:

- Test oder Assertion entfernen beziehungsweise lockern;
- Test skippen, quarantänen oder aus dem relevanten Filter nehmen;
- Coverage-, Qualitäts- oder Fehlerschwelle senken;
- Lint-/Security-/Policy-Ausnahme ergänzen;
- Severity von blocking auf informational ändern;
- Retry oder Timeout so verändern, dass ein Defekt nur verdeckt wird;
- Validatorpfad, Fixture oder Scope so ändern, dass der problematische Fall nicht mehr geprüft wird.

Solche Änderungen können fachlich berechtigt sein. Sie sind aber **keine neutrale Fehlerbehebung**.

Wenn der Qualitätsmaßstab selbst geändert werden soll:

1. Änderung am Guard explizit benennen;
2. fachliche beziehungsweise lokale Begründung und Autorisierung prüfen;
3. Wirkung der Guard-Änderung separat verifizieren;
4. alte und neue Evidence nicht als direkt gleichwertig darstellen, wenn sich der Prüfmaßstab geändert hat;
5. bei fehlender Freigabe oder fehlender Begründung stoppen beziehungsweise eskalieren.

Leitregel:

> Agent darf einen Defekt beheben. Das autorisiert ihn nicht automatisch, die Definition von „bestanden“ passend zum Defekt zu verändern.

## Prüfung muss scheitern können

Ein grüner Check ist nur dann starke Evidence, wenn der Prüfweg einen falschen Zustand tatsächlich erkennen kann.

Bei wichtigen, deterministisch prüfbaren Claims deshalb soweit angemessen:

1. Gate oder Akzeptanzkriterium **vor** dem letzten Lösungs-/Tuning-Schritt festlegen;
2. Prüf-Evidence von Produktions-/Tuning-Evidence trennen;
3. eine bekannte gültige Probe durch denselben Prüfpfad laufen lassen;
4. eine absichtlich falsche oder perturbierte Probe durch denselben Pfad laufen lassen und sichtbar scheitern sehen;
5. bei besonders wichtigen Rechen-/Transformationsclaims nach Möglichkeit einen zweiten, fachlich unabhängigen Prüfweg verwenden;
6. gemeinsame Libraries, Daten, Caches oder Referenzwerte offenlegen, wenn dadurch die behauptete Unabhängigkeit geschwächt wird.

Ein zweiter Wrapper um dieselbe fehlerhafte Berechnung ist kein unabhängiger Nachweis.

### Held-out und kontaminierte Evidence

Evidence, die bereits zur Auswahl, Abstimmung oder Reparatur des Kandidaten benutzt wurde, ist nicht mehr vollständig unabhängig für dessen Zertifizierung.

Leitfrage:

> Hätte ein anderer Wert dieser Referenz die erzeugte Lösung verändert?

Wenn ja, hat die Referenz den Produktionsweg beeinflusst und soll nicht gleichzeitig als starke unabhängige Abschluss-Evidence ausgegeben werden.

### Null-/Open-Ergebnis ist zulässig

Wenn die definierte Prüfung keine belastbare Bestätigung liefert:

- nicht den Threshold passend verschieben;
- kein „wahrscheinlich bestanden“ erfinden;
- vorhandene Teil-Evidence nennen;
- Status offen, nicht verifiziert oder blockiert lassen.

## Fresh Evidence vor Completion Claims

Eine Erfolgs-, Fertig- oder Pass-Aussage benötigt einen **aktuellen Nachweis für genau den behaupteten Zustand**.

Nicht ausreichend sind:

- ein Testlauf vor der letzten relevanten Änderung;
- ein früherer CI-Lauf;
- nur ein Teilcheck, wenn der Claim die vollständige Prüfung betrifft;
- die Erfolgsmeldung eines anderen Agenten ohne unabhängige Verifikation;
- „sollte jetzt gehen“, „wahrscheinlich grün“ oder ähnliche Extrapolation;
- ein neuer grüner Lauf nach einer unbewerteten Abschwächung des tragenden Checks.

Vor einem Completion Claim:

1. bestimmen, welcher Nachweis den Claim tatsächlich trägt;
2. prüfen, ob dieser Nachweis seit der relevanten Baseline in Aussagekraft und Scope unverändert ist oder Änderungen daran explizit bewertet wurden;
3. diesen Nachweis frisch und vollständig ausführen;
4. Ergebnis, Fehlerzahl und Exit Status lesen;
5. prüfen, ob die Evidence den Claim wirklich stützt;
6. Claim auf die tatsächlich verifizierte Aussage begrenzen.

Wenn ein Nachweis nicht ausführbar ist, Status als `blocked`, `not run` oder entsprechend lokal definiert melden – nicht als bestanden.

## Stoppen und eskalieren, wenn

- eine neue Architektur- oder Produktentscheidung nötig wird;
- notwendiger Kontext fehlt;
- die Ursache außerhalb des Scopes liegt;
- mehrere Versuche ohne belastbare Annäherung scheitern;
- die Prüfung selbst unzuverlässig oder nicht ausführbar ist;
- eine relevante Abschwächung des Quality Floors nötig wäre, aber nicht separat begründet und autorisiert ist;
- eine riskante oder irreversible Aktion nötig würde.

## Abschluss

Ein Loop endet erfolgreich nur mit überprüfbarem, aktuellem Nachweis.

Angeben:

- erreichten Ausgangszustand;
- frisch ausgeführte Prüfungen;
- relevante Korrekturschritte;
- Änderungen an tragenden Checks/Gates/Schwellenwerten, falls vorhanden;
- nicht ausgeführte oder blockierte Prüfungen;
- verbleibende Risiken oder manuelle Prüfungen.

Ein erfolgreicher Verification Loop ersetzt kein nachgelagertes Review oder Human Gate.
