# Anforderung SESSION-42: Ablauf bei Inaktivitaet

Quelle: freigegebenes Ticket, Stand 2026-07-21.

## Akzeptanzkriterien

- **AC-1**: Ein Token gilt als abgelaufen, wenn seit der **letzten Aktivitaet**
  mehr als 30 Minuten vergangen sind.
- **AC-2**: Die Erstellungszeit des Tokens ist fuer den Ablauf ausdruecklich **nicht**
  massgeblich. Ein Token, das seit Stunden besteht, aber vor einer Minute genutzt wurde,
  ist gueltig.
- **AC-3**: Die Eigenschaft aus AC-2 ist durch einen automatischen Test abgesichert.
