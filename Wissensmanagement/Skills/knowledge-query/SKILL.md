---
name: knowledge-query
description: Beantwortet Fragen aus einer vorhandenen Wissensbasis durch gezieltes Retrieval, Prüfung von Provenance, Aktualität und Widersprüchen und kennzeichnet klar, was die Basis nicht trägt. Verwenden bei Fragen, die aus einer bestehenden Wissensbasis grounded beantwortet werden sollen, ohne Modellwissen als Basisinhalt auszugeben.
---

# Knowledge Query

Nutze `../../Retrieval-Findability-und-Wissensabfrage.md`.

## Prozess

1. Frage, Scope und Zeitbezug klären.
2. Geeignete Retrievalwege nutzen: Index, Text, Metadaten, Relationen, semantische Suche oder Kombination.
3. Relevante Einheiten öffnen; nicht bei Snippets oder Treffertiteln stehenbleiben.
4. Provenance, Gültigkeit und Status kritischer Aussagen prüfen.
5. Widersprüche und Lücken berücksichtigen.
6. Antwort mit nachvollziehbarem Bezug auf die verwendeten Wissenseinheiten erzeugen.
7. Fehlendes Wissen klar markieren.

## Regeln

- Retrievalscore ist kein Wahrheitswert.
- Aus fehlendem Treffer nicht sofort auf fehlendes Wissen schließen.
- Modellwissen nicht als Inhalt der Knowledge Base ausgeben.
- Bei notwendiger externer Aktualisierung an passende Recherche eskalieren.

## Output

Grounded Antwort plus relevante Unsicherheiten, Konflikte oder Wissenslücken.