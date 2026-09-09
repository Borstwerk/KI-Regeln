# Wissensmanagement / Knowledge Bases

Dieser Bereich beschreibt allgemeine Regeln für den Aufbau, die Nutzung und die Pflege persistenter Wissensbasen.

Er ist bewusst toolneutral. Obsidian, Notion, Wikis, Vektorstores, Graphdatenbanken oder andere Systeme sind mögliche Implementierungen, aber nicht die zentrale Wahrheit dieses Bereichs.

## Grundprinzip

> Eine Wissensbasis soll nach einem Ingest nicht nur größer, sondern besser werden.

Wissen wird nicht durch bloßes Ablegen von Dateien erzeugt. Eine belastbare Wissensbasis braucht Herkunft, stabile Identität, Struktur, Verknüpfung, Unsicherheitsbehandlung, Wiederverwendung und Pflege.

## Scope

```text
Recherche
→ neues Wissen finden und verifizieren

Wissensmanagement
→ bestätigtes oder klar gekennzeichnetes Wissen dauerhaft strukturieren, verbinden und pflegen

Context Engineering
→ für eine konkrete Aufgabe den richtigen Ausschnitt daraus laden

Dokumentation
→ Wissen für eine Zielgruppe verständlich vermitteln

Retrieval / RAG
→ technische Mechanismen, um Wissenseinheiten auffindbar und abrufbar zu machen
```

Ein Vektorindex ist deshalb noch keine gute Wissensbasis. Gute Retrievaltechnik kann schlechte, veraltete oder widersprüchliche Inhalte nur schneller zurückgeben.

## Wissens-Lifecycle

```text
Quelle / Erfahrung
→ Capture
→ vorhandenes Wissen suchen
→ Provenance sichern
→ Triage
→ Distill
→ bestehende Einheit aktualisieren ODER neue Einheit anlegen
→ verlinken / strukturieren
→ bei Bedarf synthetisieren
→ abfragen / wiederverwenden
→ pflegen / prüfen
→ archivieren oder ersetzen
```

## Große Wissensbasen und aktiver Kontext

Die Größe der persistenten Wissensbasis soll nicht automatisch die Größe des aktiven Agentenkontexts bestimmen.

Für große Basen gilt deshalb der Workflow aus `Workflow-Grosse-Wissensbasen.md`:

```text
Index / MOC / Metadaten / Summary
→ relevante Wissenseinheiten
→ kleinstes ausreichendes Kontextpaket
→ Detail / Raw Source nur just-in-time
```

Der Workflow verbindet insbesondere `knowledge-query` mit `context-engineering` und nutzt bei Bedarf `knowledge-distill`, `context-audit` und `context-compaction`.

## Qualitätsachsen

Eine Wissensbasis wird unter anderem geprüft auf:

- Provenance und Nachvollziehbarkeit;
- fachliche Korrektheit und Source-of-Truth-Bezug;
- Eindeutigkeit und Dubletten;
- sinnvolle Granularität;
- Findability und Navigation;
- Beziehungen und Verlinkung;
- Aktualität und Staleness;
- sichtbare Unsicherheit und Widersprüche;
- Datenschutz, Rechte und Sichtbarkeit;
- Wiederverwendbarkeit.

## Fachdateien

- `Wissensmodell-und-Scope.md`
- `Capture-Ingest-und-Triage.md`
- `Provenance-Evidence-und-Source-of-Truth.md`
- `Wissenseinheiten-und-Granularitaet.md`
- `Verlinkung-Relationen-und-Taxonomien.md`
- `Synthese-Maps-of-Content-und-Navigation.md`
- `Widersprueche-Unsicherheit-und-Confidence.md`
- `Aktualitaet-Staleness-und-Lifecycle.md`
- `Retrieval-Findability-und-Wissensabfrage.md`
- `Workflow-Grosse-Wissensbasen.md`
- `Qualitaet-Dubletten-Orphans-und-Drift.md`
- `Datenschutz-und-sensitives-Wissen.md`
- `Quellen-und-Inspirationen.md`

## Skills

- `knowledge-base-design`
- `knowledge-ingest`
- `knowledge-distill`
- `knowledge-synthesis`
- `knowledge-maintenance`
- `knowledge-query`
- `knowledge-base-review`

## Tooladapter

Tool- oder formatspezifische Regeln bleiben Adapter oder lokale Projektregeln. Beispiele:

- Obsidian: Markdown, Properties, Wikilinks, Backlinks, Bases;
- Notion: Pages, Properties, Relations, Backlinks;
- RAG-Systeme: Chunking, Embeddings, Vektorsuche, Ranking;
- Graphsysteme: Knoten-, Kanten- und Querymodell.

Diese Mechanismen dürfen nicht als universelle Wissensmanagementregel verallgemeinert werden.

## Leitgedanke

> Persistentes Wissen ist kein Chatverlauf und kein Dateiarchiv. Es ist ein gepflegtes, nachvollziehbares System wiederverwendbarer Erkenntnisse.