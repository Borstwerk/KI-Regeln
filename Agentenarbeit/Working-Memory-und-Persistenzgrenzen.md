# Working Memory und Persistenzgrenzen

## Zweck

Nicht jede Information, die ein Agent länger als einen Turn benötigt, gehört automatisch in eine dauerhafte Wissensbasis.

Dieser Bereich trennt aktiven Kontext, taskbezogenen Arbeitszustand und dauerhaftes Wissen.

## Drei Ebenen

```text
ACTIVE CONTEXT
→ aktuell modell-sichtbare Informationen

WORKING STATE
→ task-/threadbezogener Zustand, der über Schritte oder Sessions fortbestehen darf

PERSISTENT KNOWLEDGE
→ dauerhaft gepflegtes, wiederverwendbares Wissen über einzelne Tasks hinaus
```

## Active Context

Gehört zu Context Engineering.

Beispiele:

- aktuelle Instruktionen;
- gerade benötigte Dateien oder Quellen;
- relevante Toolergebnisse;
- aktueller Gesprächsausschnitt.

Er soll klein, aktuell und signalstark bleiben.

## Working State

Gehört zur Agentenarbeit.

Beispiele:

- Taskplan;
- To-do-Status;
- aktueller Implementierungsstand;
- offene Fehler und Blocker;
- Handoff-Artefakte;
- temporäre strukturierte Notizen für einen längeren Lauf.

Working State darf außerhalb des aktiven Kontextfensters persistiert werden, bleibt aber an Auftrag, Projekt oder Thread gebunden.

## Persistent Knowledge

Wird im späteren Bereich `Wissensmanagement/` behandelt.

Beispiele:

- dauerhaft gültige fachliche Erkenntnisse;
- gepflegte Wissensnoten;
- Taxonomien und Wissensgraph-Beziehungen;
- langfristige Quellen- und Provenance-Strukturen;
- wiederverwendbare Synthesen über mehrere Aufgaben hinweg.

Ein Handoff oder eine Sessionnotiz soll nicht allein durch Alterung zu kanonischem Wissen werden.

## Promotionsregel

Information wird nicht automatisch von Working State zu Persistent Knowledge befördert.

Vor dauerhafter Übernahme prüfen:

- ist sie bestätigt oder weiterhin Hypothese?
- ist sie außerhalb des aktuellen Tasks wiederverwendbar?
- gibt es bereits eine kanonische Wissenseinheit?
- ist Provenance nachvollziehbar?
- enthält sie sensitive oder unnötig personenbezogene Daten?
- gibt es Ownership- und Aktualitätsanforderungen?

## Retrieval-Grenze

Eine persistente Wissensbasis kann Material für Context Engineering liefern.

```text
Wissensbasis
→ Retrieval / Auswahl
→ aktiver Kontext
```

Das bedeutet nicht, dass die gesamte Wissensbasis in den Kontext gehört.

## Leitgedanke

> Arbeitszustand hält einen Task am Leben. Wissensmanagement hält überprüftes Wissen über Tasks hinweg nutzbar.