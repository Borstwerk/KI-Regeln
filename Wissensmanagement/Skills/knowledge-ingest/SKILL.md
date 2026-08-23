---
name: knowledge-ingest
description: Nimmt neue Quellen oder Erfahrungen kontrolliert in eine bestehende Wissensbasis auf, sucht zuerst nach vorhandenem Wissen und entscheidet zwischen Verwerfen, Raw-Speicherung, Update, Neuanlage oder Konfliktstatus.
---

# Knowledge Ingest

Nutze `../../Capture-Ingest-und-Triage.md` und `../../Provenance-Evidence-und-Source-of-Truth.md`.

## Prozess

1. Quelle, Scope, Zeitbezug und Rechte prüfen.
2. Relevante Raw Source oder stabile Referenz sichern.
3. Bestehende Wissenseinheiten über Titel, Aliase, Metadaten und Inhalt suchen.
4. Neue Information gegen vorhandenes Wissen vergleichen.
5. Triage: verwerfen, raw-only, update, create oder conflict/quarantine.
6. Provenance und Aktualitätsinformationen erhalten.
7. Geänderte Einheiten verlinken beziehungsweise Navigation aktualisieren, soweit vorgesehen.
8. Ergebnis und offene Unsicherheit berichten.

## Verbote

- Nicht aus dem ersten fehlenden Treffer auf Abwesenheit schließen.
- Keine Quelle durch KI-Zusammenfassung als neue Source of Truth ersetzen.
- Keine ungeklärten Widersprüche still überschreiben.
- Keine sensiblen Daten allein wegen Verfügbarkeit persistieren.

## Gate

Bulk-Rewrites, massenhafte Merges oder Deletes nur innerhalb eines ausdrücklich autorisierten Scopes.