# Anforderung EXPORT-19: Projektexport

Quelle: freigegebenes Ticket, Stand 2026-07-28.

## Akzeptanzkriterien

- **AC-1**: `GET /projects/{project_id}/export` liefert die Datensaetze des Projekts.
- **AC-2**: Der Endpunkt darf **ausschliesslich** von Mitgliedern genau dieses Projekts
  aufgerufen werden. Angemeldet zu sein genuegt nicht.
- **AC-3**: `limit` ist optional, ganzzahlig und liegt zwischen 1 und 1000.
