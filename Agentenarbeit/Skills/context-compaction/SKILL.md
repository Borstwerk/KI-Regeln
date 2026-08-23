---
name: context-compaction
description: Verdichtet gewachsenen Agentenkontext mit hoher Fidelity, erhält Constraints, Entscheidungen, Sources of Truth, offenen Zustand und Evidence und prüft die Fortsetzungsfähigkeit nach der Kompression.
---

# Context Compaction

Nutze `../../Context-Compaction.md` und `../../Working-Memory-und-Persistenzgrenzen.md`.

## Verwenden wenn

- ein langer Agentenlauf Context Pressure erreicht;
- eine abgeschlossene Phase aus dem aktiven Verlauf verdichtet werden soll;
- große historische Tooloutputs oder Wiederholungen den Kontext dominieren;
- eine Runtime Compaction verlangt oder anbietet.

Nicht verwenden, um dauerhaftes Wissen zu kuratieren; dafür ist später Wissensmanagement zuständig.

## Prozess

1. aktuellen Taskzustand und nächsten Schritt bestimmen.
2. Erhaltenspflichten sammeln: Ziel, Scope, Constraints, Sources of Truth, Entscheidungen, Artefaktzustand, offene Probleme, Evidence, Gates.
3. redundante Historie und wiederabrufbare Rohoutputs identifizieren.
4. kompakte Fortsetzungsrepräsentation erzeugen.
5. Fakten, Hypothesen und historische Altstände sauber unterscheiden.
6. Verlustprüfung durchführen.
7. wenn möglich einen Fortsetzungs-/Paartest gegen denselben Ausgangszustand durchführen.

## Erhalten

- harte Constraints;
- bestätigte Entscheidungen;
- offene Blocker und Risiken;
- relevante gescheiterte Ansätze;
- Source-of-Truth-Referenzen;
- aktuelle Artefakte und Evidence;
- Gate-Status;
- nächsten prüfbaren Schritt.

## Regeln

- Keine maximale Kompressionsrate anstreben.
- Zuerst Recall/Fidelity schützen, dann unnötige Details entfernen.
- Nicht ausgeführte Prüfungen nicht als bestanden zusammenfassen.
- Unbestätigte Vermutungen nicht zu Fakten verdichten.
- Rohzustand nicht allein aus Spargründen löschen, wenn Audit-/Recovery-Bedarf besteht und Aufbewahrung zulässig ist.
- Provider-native Compaction darf verwendet werden, ersetzt aber nicht die Outcome-/Fidelity-Prüfung.

## Abschluss

Angeben:

- was erhalten wurde;
- was entfernt, ausgelagert oder referenziert wurde;
- welche Unsicherheiten bestehen;
- wie die Fortsetzungsfähigkeit geprüft wurde.

> Gute Compaction ist erfolgreich, wenn die nächste Arbeit korrekt weitergeht – nicht wenn die Zusammenfassung besonders kurz ist.