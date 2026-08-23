# Skill-Handbuch – Wissensmanagement

Dieses Handbuch erklärt die Skills des Bereichs `Wissensmanagement/`.

## Grundmodell

```text
knowledge-base-design
→ Struktur und Lifecycle planen

knowledge-ingest
→ neue Quellen kontrolliert aufnehmen

knowledge-distill
→ Raw Information in wiederverwendbares Wissen verdichten

knowledge-synthesis
→ mehrere Wissenseinheiten verbinden

knowledge-query
→ vorhandenes Wissen grounded abfragen

knowledge-maintenance
→ Staleness, Dubletten, Orphans und Drift pflegen

knowledge-base-review
→ Gesamtqualität unabhängig auditieren
```

## `knowledge-base-design`

Für neue Wissensbasen oder größere Umbauten. Definiert Wissensobjekte, Provenance, Metadaten, Beziehungen, Retrieval, Lifecycle und Datenschutz – vor der Toolwahl.

## `knowledge-ingest`

Für neue Quellen oder Erfahrungen. Sucht zuerst nach vorhandenem Wissen und entscheidet zwischen Verwerfen, Raw-Speicherung, Update, Neuanlage oder Konfliktstatus.

> Ingest ist ein Merge-Problem, kein Kopierproblem.

## `knowledge-distill`

Für die Umwandlung source-naher Inhalte in wiederverwendbare Claims, Konzepte und Entitäten. Erhält Provenance und bevorzugt Enrichment vorhandener Identitäten gegenüber Dubletten.

## `knowledge-synthesis`

Für übergreifende Erkenntnisbilder aus mehreren vorhandenen Wissenseinheiten. Gegenbelege und Unsicherheit bleiben sichtbar.

## `knowledge-query`

Für Fragen an die Knowledge Base. Retrievalscores sind keine Wahrheitswerte; kritische Antworten prüfen Provenance, Aktualität und Konflikte.

## `knowledge-maintenance`

Für Content Health: stale candidates, Dubletten, Orphans, kaputte Links, Metadaten-/Taxonomiedrift und sichere Repair-Slices.

## `knowledge-base-review`

Read-only Gesamtprüfung über Wissensmodell, Provenance, Granularität, Verlinkung, Findability, Aktualität, Konflikte, Datenschutz und Wartbarkeit.

## Grenzen

```text
Recherche
→ findet und verifiziert neues externes Wissen

Wissensmanagement
→ persistiert und pflegt Wissen

Context Engineering
→ lädt den richtigen Ausschnitt für eine Aufgabe

Dokumentation
→ erklärt Wissen für eine Zielgruppe
```

Obsidian, Notion, Vector Stores, RAG und Knowledge Graphs sind mögliche Implementierungen oder Adapter.

## Maturity

Alle neuen Wissensmanagement-Skills starten `experimental` mit `partial` Eval-Coverage. Sie benötigen reale Nutzung und weitere Evals, bevor eine Hochstufung sinnvoll ist.