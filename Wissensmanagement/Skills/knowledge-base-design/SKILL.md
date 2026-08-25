---
name: knowledge-base-design
description: Entwirft oder prüft die toolneutrale Struktur einer persistenten Wissensbasis einschließlich Wissensobjekten, Metadaten, Provenance, Navigation, Lifecycle und Datenschutzgrenzen. Verwenden bei einer neuen Wissensbasis, größerem Umbau oder ungeklärtem Wissensmodell, nicht für das bloße Schreiben einer einzelnen Notiz.
---

# Knowledge Base Design

Nutze `../../Wissensmodell-und-Scope.md` und die angrenzenden Regeldateien.

## Trigger

Nutzen bei neuer Wissensbasis, größerem Umbau oder ungeklärtem Wissensmodell.

Nicht für das bloße Schreiben einer einzelnen Notiz verwenden.

## Prozess

1. Zweck, Nutzer und wiederkehrende Retrievalfragen klären.
2. Sources of Truth und Raw-Source-Strategie bestimmen.
3. Wissenseinheiten und stabile Identität definieren.
4. minimale notwendige Metadaten und Provenance festlegen.
5. Beziehungen, Taxonomie und Navigation planen.
6. WIP/Validated/Stale/Archived-Lifecycle passend zum Risiko festlegen.
7. Datenschutz-, Sichtbarkeits- und Löschgrenzen bestimmen.
8. Retrievalmechanismen erst danach als Implementierungsoption wählen.

## Regeln

- Kein Obsidian-, Notion- oder RAG-Schema als universellen Default ausgeben.
- Keine Metadaten sammeln, für die kein Nutzungszweck existiert.
- Retrievalfragen und Pflegefähigkeit in das Design einbeziehen.
- Raw Source, Derived Knowledge und Navigation logisch unterscheiden.

## Output

Ein begründetes Wissensmodell mit Scope, Objekttypen, Kernmetadaten, Beziehungen, Lifecycle, Datenschutz und offenen Toolentscheidungen.