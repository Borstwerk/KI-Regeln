# Quellen und Inspirationen – Wissensmanagement

Dieser Bereich synthetisiert allgemeine Prinzipien aus Standards, Knowledge-Management-Praxis, aktuellen Knowledge-Base-Skills und Tooldokumentation. Externe Quellen sind Inspiration und Evidence, keine automatisch verbindliche Projektspezifikation.

## Knowledge-Centered Service (KCS)

Der Consortium for Service Innovation beschreibt Knowledge-Centered Service als laufenden Kreislauf aus Capture, Structure, Reuse und Improve sowie Content-Health-Praktiken. Besonders übernommen werden:

- Wissen im Arbeitsfluss erfassen;
- vor Neuerstellung vorhandenes Wissen suchen und wiederverwenden;
- Wissen durch Nutzung verbessern;
- einfache, konsistente Struktur für Findability;
- Dubletten, Linkqualität, Metadaten und Lifecycle als Content-Health-Themen;
- WIP, validierte und archivierte Zustände als Inspiration für sichtbare Wissensreife.

Quellen:

https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide
https://library.serviceinnovation.org/KCS/Knowledge-Centered_Success_Practices_Guide/301-Evolve_Loop/Practice_5_Content_Health

KCS ist stark auf Service-/Support-Wissen ausgerichtet. Seine Organisations- und Rollenmodelle werden deshalb nicht ungeprüft universalisiert.

## W3C PROV

W3C PROV liefert ein allgemeines Modell für Provenance: Entitäten, Aktivitäten und beteiligte Akteure sowie deren Herkunftsbeziehungen.

Übernommen wird nicht die Pflicht zu RDF oder PROV-O, sondern das allgemeinere Prinzip, dass abgeleitetes Wissen auf Ursprung und Transformation zurückführbar sein soll.

Quellen:

https://www.w3.org/TR/prov-overview/
https://www.w3.org/TR/prov-primer/

## ISO 30401

ISO 30401 beschreibt Anforderungen an Aufbau, Betrieb, Review und Verbesserung eines Knowledge-Management-Systems unabhängig von Organisationstyp und Größe.

Quelle:

https://www.iso.org/standard/68683.html

Der kostenpflichtige Standard wird hier nicht reproduziert. Verwendet wird nur seine öffentlich beschriebene Einordnung von Knowledge Management als zu pflegendem Managementsystem.

## Obsidian

Die offizielle Obsidian-Hilfe zeigt Properties, Tags, Links, Backlinks und Bases als konkrete Mechanismen für strukturierte Markdown-Wissensbestände.

Quellen:

https://obsidian.md/help/properties
https://obsidian.md/help/tags
https://obsidian.md/help/Plugins/Backlinks
https://obsidian.md/help/bases/syntax

Diese Funktionen sind Tooladapter. YAML-Frontmatter, Wikilinks oder Bases sind keine universelle Wissensmanagementpflicht.

## Notion

Notion nutzt Seiten, Datenbank-Properties, Relations und Backlinks als andere konkrete Umsetzung strukturierter Wissensbestände.

Quellen:

https://www.notion.com/help/intro-to-databases
https://www.notion.com/help/create-links-and-backlinks

## Retrieval / RAG

OpenAI Vector Stores und Knowledge Retrieval zeigen aktuelle technische Mechanismen für Ingest, Chunking, Metadatenfilter, semantische Suche und zitierbare Retrieval-Antworten.

Quellen:

https://platform.openai.com/docs/api-reference/vector-stores
https://openai.com/solutions/blueprints/knowledge-retrieval/

Diese Mechanismen werden bewusst von der allgemeinen Knowledge-Base-Qualität getrennt.

## Aktuelle Agent-Skills

### Obsidian Wiki

`Ar9av/obsidian-wiki` trennt unter anderem Ingest, Query, Lint, Dedup, Cross-Linking, Taxonomie, Synthese und Context Packs. Besonders wertvoll ist die Trennung von permanentem Ingest und bloßem Session-Retrieval.

Quelle:

https://github.com/Ar9av/obsidian-wiki

### Obsidian Second Brain

`eugeniughelbur/obsidian-second-brain` behandelt eine Wissensbasis als lebendes System: search before create, Raw Sources erhalten, Provenance und Aktualität führen, bestehende Seiten verbessern, Konflikte sichtbar behandeln und Orphans vermeiden.

Quelle:

https://github.com/eugeniughelbur/obsidian-second-brain

### Knowledge Distill

`cogni-work/insight-wave` trennt Source Ingest von einer späteren Distillation in wiederverwendbare Concept-/Entity-Einheiten und dedupliziert Claims beim Merge.

Quelle:

https://github.com/cogni-work/insight-wave

## Einordnung

> Toolfeatures zeigen mögliche Mechanismen. Zentrale Regeln beschreiben den langlebigeren Wissens-Lifecycle dahinter.