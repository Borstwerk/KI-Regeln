---
name: session-handoff
description: Erzeugt für einen neuen Agenten, Chat oder späteren Arbeitslauf einen eigenständig nutzbaren Fortsetzungszustand mit Ziel, Scope, Sources of Truth, Entscheidungen, Artefakten, Evidence, Risiken, Gates und nächstem Schritt. Verwenden bei Session-, Agenten- oder Zeitwechseln, wenn Arbeit zuverlässig fortgesetzt werden muss.
---

# Session Handoff

Nutze `../../Long-Horizon-Handoffs.md` und `../../Working-Memory-und-Persistenzgrenzen.md`.

## Verwenden wenn

- ein langer Task in einer neuen Session fortgesetzt wird;
- ein anderer Agent übernimmt;
- Kontext bewusst zurückgesetzt wird;
- ein Arbeitsstand für später zuverlässig übergeben werden muss.

Nicht verwenden als dauerhafte Wissensdatenbank oder bloßes Gesprächsprotokoll.

## Prozess

1. Auftrag, Ziel und aktuellen Scope erfassen.
2. kanonische Sources of Truth und Vorrangregeln referenzieren.
3. bestätigte Entscheidungen und aktuellen Artefaktzustand festhalten.
4. ausgeführte Evidence und tatsächlichen Gate-Status dokumentieren.
5. offene Fehler, Risiken, Blocker und relevante Sackgassen erhalten.
6. nächsten prüfbaren Schritt beschreiben.
7. große Artefakte referenzieren statt duplizieren.
8. Standalone-Test durchführen: Kann eine frische Instanz ohne alten Chat korrekt weiterarbeiten?

## Output

Ein Handoff sollte je nach Task mindestens enthalten:

- Ziel;
- Scope;
- Sources of Truth;
- bestätigte Entscheidungen;
- aktueller Zustand / Artefakte;
- Evidence;
- offene Punkte und Risiken;
- Gate-/Freigabestatus;
- nächster Schritt.

## Regeln

- Keine Freigaben erfinden.
- Keine Hypothese zu einer bestätigten Entscheidung machen.
- Nicht ausgeführte Tests nicht als bestanden darstellen.
- Historische Handoffs nicht als aktuelle Source of Truth behandeln.
- Sensitive Daten nur aufnehmen, wenn sie für die Übergabe erforderlich und zulässig sind.
- Ein Handoff soll verständlich sein, ohne den alten Gesprächsverlauf vorauszusetzen.

## Abschluss

Wenn eine frische Instanz Ziel, Zustand oder nächsten Schritt nur durch Raten bestimmen könnte, ist das Handoff unvollständig.