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