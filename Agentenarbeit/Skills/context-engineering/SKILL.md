---
name: context-engineering
description: Wählt für einen Agentenlauf den kleinsten ausreichenden, aktuellen und signalstarken Kontext aus, schützt Sources of Truth und entscheidet zwischen aktivem Kontext, Working State, Compaction und gezieltem Nachladen.
---

# Context Engineering

Nutze `../../Context-Engineering.md`.

## Verwenden wenn

- Kontext für einen Agentenlauf zusammengestellt oder bereinigt werden muss;
- viele Dateien, Regeln, Tools oder historische Informationen verfügbar sind;
- ein langer Lauf Context Pressure oder Signalverlust zeigt;
- geklärt werden muss, was aktiv geladen, ausgelagert oder später nachgeladen wird.

Nicht verwenden als Ersatz für dauerhaftes Wissensmanagement oder fachliche Source of Truth.

## Prozess

1. Ziel und nächsten prüfbaren Zustand bestimmen.
2. Kanonische Sources of Truth identifizieren.
3. Benötigten Kontext nach Relevanz, Aktualität und Autorität auswählen.
4. Prüfen, was just-in-time geladen werden kann.
5. Active Context von Working State und Persistent Knowledge unterscheiden.
6. Duplikate, Altstände, große Tooloutputs und unnötig sichtbare Skills/Tools reduzieren.
7. Bei langem Verlauf prüfen, ob `context-compaction` oder `session-handoff` benötigt wird.
8. Wenn der Kontext selbst problematisch wirkt, `context-audit` verwenden.

## Regeln

- Relevanz vor maximaler Kontextmenge.
- Aktuelle kanonische Quelle vor alter Zusammenfassung.
- Referenz vor unnötiger Duplizierung.
- Stabile Ergebnisse von Arbeitshypothesen trennen.
- Kontextfenstergröße nicht als Qualitätsziel behandeln.
- Tokenreduktion nie ohne Outcome-/Qualitätsprüfung als Verbesserung behaupten.
- Große Rohoutputs bevorzugt deterministisch vorverarbeiten oder referenzieren, wenn Evidence erhalten bleibt.
- Irrelevante persönliche, geheime oder sensitive Daten nicht allein wegen Verfügbarkeit aufnehmen.
- Providerdetails wie Fenstergröße, Cacheverhalten oder Tokenpreise gegen die konkrete Runtime prüfen.

## Abschlusscheck

- Ist der Auftrag eindeutig?
- Sind alle notwendigen Sources of Truth vorhanden?
- Enthält der aktive Kontext Widersprüche oder Altstände?
- Gibt es unnötiges Rauschen oder Tooloutput-Bloat?
- Ist klar, welche Informationen nur Hypothesen sind?
- Ist Working State außerhalb des aktiven Fensters zuverlässig adressierbar?
- Ist eine Compaction/Handoff-Grenze erreicht?

Wenn eine notwendige Quelle fehlt, nicht durch plausible Annahmen ersetzen.