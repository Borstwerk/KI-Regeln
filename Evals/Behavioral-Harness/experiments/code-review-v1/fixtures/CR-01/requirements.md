# Anforderung PRICING-114: Tarifrabatt im Warenkorb

Quelle: freigegebenes Ticket, Stand 2026-07-02.

## Akzeptanzkriterien

- **AC-1**: `apply_discount` gewährt Tier `gold` 15 Prozent und Tier `silver` 10 Prozent Rabatt.
- **AC-2**: Der gewährte Rabatt überschreitet nie 15 Prozent.
- **AC-3**: Ein unbekannter Tier führt zu 0 Prozent Rabatt. Die Funktion wirft dabei keine Ausnahme.
- **AC-4**: Der Rabatt wird auf den Nettobetrag angewendet.

Nicht Teil dieses Auftrags: Gutscheine, Staffelpreise, Steuerlogik.
