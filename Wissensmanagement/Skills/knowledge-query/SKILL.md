---
name: knowledge-query
description: Beantwortet Fragen aus einer vorhandenen Wissensbasis durch gezieltes Retrieval, Prüfung von Provenance, Aktualität und Widersprüchen und kennzeichnet klar, was die Basis nicht trägt. Verwenden bei Fragen, die aus einer bestehenden Wissensbasis grounded beantwortet werden sollen, ohne Modellwissen als Basisinhalt auszugeben.
---

# Knowledge Query

Nutze `../../Retrieval-Findability-und-Wissensabfrage.md`.

Bei großen Wissensbasen oder erkennbarem Context Bloat zusätzlich `../../Workflow-Grosse-Wissensbasen.md` verwenden.

## Prozess

1. Frage, Scope und Zeitbezug klären.
2. Geeignete Retrievalwege nutzen: Index, Text, Metadaten, Relationen, semantische Suche oder Kombination.
3. Bei großen Basen progressiv vorgehen: zuerst Index / Metadaten / Summary, danach nur relevante Wissenseinheiten und Details öffnen.
4. Relevante Einheiten öffnen; nicht bei Snippets oder Treffertiteln stehenbleiben.
5. Provenance, Gültigkeit und Status kritischer Aussagen prüfen.
6. Widersprüche und Lücken berücksichtigen.
7. Für umfangreiche Aufgaben mit `context-engineering` den kleinsten ausreichenden aktiven Kontext bilden; größere Raw Sources nur just-in-time laden.
8. Antwort mit nachvollziehbarem Bezug auf die verwendeten Wissenseinheiten erzeugen.
9. Fehlendes Wissen klar markieren.

## Regeln

- Retrievalscore ist kein Wahrheitswert.
- Aus fehlendem Treffer nicht sofort auf fehlendes Wissen schließen.
- Den Vollbestand einer großen Wissensbasis nicht vorsorglich in den aktiven Kontext laden.
- Modellwissen nicht als Inhalt der Knowledge Base ausgeben.
- Bei notwendiger externer Aktualisierung an passende Recherche eskalieren.

## Output

Grounded Antwort plus relevante Unsicherheiten, Konflikte oder Wissenslücken.