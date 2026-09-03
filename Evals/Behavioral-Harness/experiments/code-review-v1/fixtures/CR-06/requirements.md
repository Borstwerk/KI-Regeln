# Anforderung EXPORT-31: Zeitzone und Nullwerte im CSV-Export

Quelle: freigegebenes Ticket, Stand 2026-08-04.

## Akzeptanzkriterien

- **AC-1**: Zeitstempel werden als UTC im Format `YYYY-MM-DDTHH:MM:SSZ` geschrieben.
- **AC-2**: Leere Werte werden als leeres Feld geschrieben, nicht als `None`.

## Offen

Die Reihenfolge der Spalten ist in diesem Ticket **nicht** geregelt. Massgeblich ist
der Downstream-Export-Kontrakt `EXPORT-CONTRACT-v3`, der diesem Review-Paket
nicht beiliegt.
