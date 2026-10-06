# Retrieval, Findability und Wissensabfrage

## Grundprinzip

> Retrieval findet Kandidaten. Es entscheidet nicht automatisch, was wahr ist.

## Retrievalwege

Je nach System kombinierbar:

- Navigation / Index;
- exakte Textsuche;
- Titel und Aliase;
- Tags und Metadatenfilter;
- Relationen / Graphnavigation;
- semantische oder Vektorsuche;
- zeitliche Filter;
- hybride Suche und Ranking.

Keine Methode ist universell überlegen.

## Query-Prozess

```text
Frage klären
→ Scope / Zeitbezug bestimmen
→ geeignete Retrievalwege wählen
→ relevante Wissenseinheiten öffnen
→ Provenance und Aktualität prüfen
→ Widersprüche berücksichtigen
→ Antwort / Kontextpaket erzeugen
→ Wissenslücken sichtbar machen
```

## Tiered Retrieval

Für große Basen kann progressive Auswahl sinnvoll sein:

```text
Index / Metadaten / Summary
→ relevante Einheiten
→ Detailinhalt
→ Raw Source nur bei Bedarf
```

Das reduziert Context Bloat, ohne Evidence zu verlieren.

Für den vollständigen Ablauf von der Kandidatenauswahl bis zum kleinen aktiven Kontextpaket gilt `Workflow-Grosse-Wissensbasen.md`.

## Candidate Generation und Reranking getrennt bewerten

Mehrstufige Suche kann zwei unterschiedliche Qualitätsprobleme besitzen:

```text
Query
→ Candidate Generation
→ Kandidatenpool
→ Reranking
→ Top-K
```

### Candidate Generation

Die erste Stufe soll relevante Kandidaten überhaupt in Reichweite bringen.

Geeignete Evidence kann sein:

- Candidate Recall / Recall@K;
- Coverage relevanter Dokumente;
- Anteil von Queries, bei denen mindestens ein brauchbarer Kandidat im Pool liegt.

### Reranking

Die zweite Stufe ordnet bereits gefundene Kandidaten nach Relevanz, Kontext oder Nutzer-/Aufgabenmerkmalen neu.

Geeignete Evidence kann sein:

- NDCG;
- MRR;
- Precision@K;
- pairwise Ranking-Vergleiche;
- taskbezogene Outcome-Metriken.

Wichtige Grenze:

> Ein Reranker kann einen fehlenden Kandidaten nicht zurückholen.

Ein schlechter Endwert kann daher aus:

- schwacher Candidate Generation;
- schwachem Reranking;
- ungeeigneter Relevanzdefinition;
- oder mehreren dieser Ursachen

entstehen.

Deshalb die Stufen getrennt evaluieren, bevor Gewichte oder Modelle im Reranker weiter optimiert werden.

Konkrete Embeddingmodelle, Vektordatenbanken, Gewichtungen oder Candidate-Pool-Größen sind Implementierungsdetails und werden nicht universalisiert.

## RAG und Vektorstores

Chunking, Embeddings, Vektorstores und Ranking sind technische Retrievalmechanismen.

Sie gehören zur Implementierung beziehungsweise zu Adaptern. Die Wissensmanagementregeln bleiben:

- richtige Quellen;
- nachvollziehbare Provenance;
- gute Granularität;
- Aktualität;
- sichtbare Konflikte;
- Zugriffsschutz.

## Antworten aus der Wissensbasis

Eine Wissensabfrage soll klar unterscheiden:

- direkt gestütztes Wissen;
- Synthese;
- Inferenz;
- fehlendes Wissen.

Wenn die Basis die Antwort nicht trägt, nicht mit Modellwissen auffüllen und so tun, als stamme es aus der Basis.

## Leitgedanke

> Gute Findability bringt die richtige Evidence in Reichweite; sie ersetzt deren Bewertung nicht.