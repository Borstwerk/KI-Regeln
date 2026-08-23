---
name: knowledge-maintenance
description: Prüft und pflegt eine Wissensbasis auf Staleness, Dubletten, Orphans, kaputte Links, fehlende Provenance, Taxonomie- oder Schema-Drift und führt nur sichere, nachvollziehbare Repair-Slices durch.
---

# Knowledge Maintenance

Nutze `../../Qualitaet-Dubletten-Orphans-und-Drift.md` und `../../Aktualitaet-Staleness-und-Lifecycle.md`.

## Prozess

1. Prüfbereich und erlaubte Schreibwirkung festlegen.
2. Health-Signale sammeln: duplicate candidates, orphans, broken links, stale candidates, fehlende Provenance, Konflikte, Metadaten-/Taxonomiedrift.
3. Funde klassifizieren statt automatisch reparieren.
4. Bei Dubletten Identität, Scope, Zeitbezug und Historie prüfen.
5. Kleine sichere Repair-Slices durchführen, wenn autorisiert.
6. Nach jedem Slice Links, Navigation und Provenance erneut prüfen.
7. Riskante oder massenhafte Eingriffe als Plan + Gate ausgeben.

## Regeln

- Orphan ≠ automatisch löschen.
- Similarity ≠ automatisch Dublette.
- Stale ≠ automatisch falsch.
- Archivieren bevorzugen, wenn Historie oder eingehende Referenzen wichtig sind.
- Keine automatische Großsanierung.

## Output

Health-Befund mit Reparaturen, offenen Risiken und nicht ausgeführten gatepflichtigen Aktionen.