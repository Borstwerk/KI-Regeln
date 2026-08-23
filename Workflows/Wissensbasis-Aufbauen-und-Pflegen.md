# Workflow – Wissensbasis aufbauen und pflegen

## Ziel

Eine persistente Wissensbasis so aufbauen und weiterentwickeln, dass neue Quellen vorhandenes Wissen verbessern statt nur Dateien anzuhäufen.

## Grundablauf

```text
Zweck / Retrievalfragen
→ knowledge-base-design
→ Quellen / Erfahrungen
→ knowledge-ingest
→ knowledge-distill
→ bei mehreren reifen Einheiten optional knowledge-synthesis
→ Nutzung über knowledge-query
→ wiederkehrend knowledge-maintenance
→ bei größeren Meilensteinen knowledge-base-review
```

Nicht jeder Ingest benötigt eine neue Synthese.

## Research-to-Knowledge

Wenn neues Wissen erst extern recherchiert werden muss:

```text
research-plan / deep-research
→ source-evaluation
→ research-synthesis
→ knowledge-ingest
→ knowledge-distill
→ persistente Knowledge Base
```

Research-Evidence und persistente Wissensstruktur bleiben dabei getrennte Verantwortungen.

## Search before Create

Vor jeder Neuanlage:

```text
bestehende Identität / Aliase / Beziehungen suchen
→ passt vorhandene Einheit?
   ├─ ja → enrich / update
   └─ nein → neue Einheit
```

## Risk Gates

Normalerweise niedrige Wirkung:

- read-only Query;
- einzelne neue Einheit;
- gezieltes Update mit nachvollziehbarer Provenance.

Höhere Wirkung:

- Bulk-Ingest mit automatischen Rewrites;
- Massen-Merge;
- Taxonomie-/Schemawechsel;
- große Link-Rewrites;
- Archive/Delete vieler Einheiten;
- Import sensibler Daten.

Diese Schritte brauchen expliziten Scope, Sample/Preview und gegebenenfalls Human Gate.

## Verbindung zu Context Engineering

```text
Persistent Knowledge
→ knowledge-query / Retrieval
→ context-engineering
→ Active Context
```

Eine Knowledge Base darf nicht ungefiltert komplett in den Agentenkontext geladen werden.

## Abschluss-Evidence

Bei größeren Änderungen mindestens:

- geänderte/neu angelegte Wissenseinheiten;
- erhaltene Provenance;
- Merge-/Duplicate-Entscheidungen;
- offene Konflikte;
- Stale-/Archive-Funde;
- nicht ausgeführte gatepflichtige Aktionen.

## Leitgedanke

> Die Wissensbasis ist ein lebendes System – aber nicht autonomer Besitzer ihrer eigenen Wahrheit.