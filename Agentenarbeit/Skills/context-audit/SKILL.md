---
name: context-audit
description: Prüft einen Agentenkontext oder Harness auf Token-/Größenverteilung, Relevanz, Staleness, Duplikate, Context Rot, Tooloutput-Bloat und unnötig sichtbare Skills oder Tools und leitet messbare Optimierungen ab.
---

# Context Audit

Nutze `../../Context-Budget-und-Token-Effizienz.md`, `../../Context-Rot-und-Signalqualitaet.md` und `../../Tool-Outputs-und-Context-Offloading.md`.

## Verwenden wenn

- Kontextfenster ungewöhnlich schnell wächst;
- Tokenverbrauch, Latenz oder Agentenqualität schlechter werden;
- ein Harness auf Context Bloat geprüft werden soll;
- unklar ist, welche Kontextbestandteile wirklich nötig sind.

Nicht verwenden für bloße Kostenkalkulation ohne Kontextanalyse.

## Inputs

Möglichst erfassen:

- Ziel/Taskklasse;
- aktive Kontextquellen;
- System-/Projektinstruktionen;
- geladene Skills/Tools;
- Tooloutputs;
- Verlauf/Working State;
- Token-/Größen- und Latenzmetriken, soweit verfügbar;
- beobachtete Fehlverhalten oder Outcomes.

## Prozess

1. Kontextinventar erstellen.
2. Größen-/Tokenanteile bestimmen oder transparent approximieren.
3. Quellen nach Relevanz, Autorität, Aktualität und Wiederholungsgrad prüfen.
4. Duplikate, Staleness, Widersprüche und große Rohoutputs markieren.
5. prüfen, was just-in-time geladen oder außerhalb des Modells verarbeitet werden kann.
6. Compaction-/Handoff-Kandidaten erkennen.
7. Optimierungen nach erwarteter Wirkung und Risiko priorisieren.
8. Vorher-/Nachher-Evidence definieren.

## Output

- Context-Inventar;
- größte Verbrauchs-/Bloatquellen;
- Signalqualitätsprobleme;
- konkrete Optimierungsvorschläge;
- benötigte Provider-/Runtimeprüfung;
- Messplan für die Wirkung.

## Regeln

- Keine universellen Token- oder Prozentgrenzen erfinden.
- Zeichen-/Dateigröße nur als Approximation ausgeben, wenn echte Tokenmetriken fehlen.
- Weniger Tokens nicht automatisch als bessere Qualität werten.
- Sensitive Inhalte nicht unnötig für den Audit duplizieren.
- Wenn die Ursache nicht belegbar ist, zwischen Beobachtung und Hypothese unterscheiden.

## Abschluss

Ein Audit ist erst belastbar, wenn klar ist, **was** reduziert oder anders geladen werden soll und **wie** geprüft wird, ob Outcome und Zuverlässigkeit mindestens erhalten bleiben.