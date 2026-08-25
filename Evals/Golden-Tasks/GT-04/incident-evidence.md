# Incident Evidence

## Timeline

- 12:00 – Checkout-Fehlerrate 0,4 %.
- 12:03 – Checkout-Fehlerrate steigt auf 8–11 %, überwiegend HTTP 502.
- 12:04 – App-Log zeigt bei betroffenen Requests wiederholt `inventory request timed out after 2000ms`.
- 12:06 – Drei verfügbare Trace-IDs zeigen jeweils einen langen `inventory.reserve`-Span; vollständige verteilte Traces stehen nicht zur Verfügung.

## Metriken

- Checkout-App CPU: 42–55 %, kein ungewöhnlicher Sprung.
- Checkout-DB p95: 18–24 ms, entspricht dem üblichen Bereich.
- Inventory-Service: keine direkten Dashboards in dieser Fixture verfügbar.

## Runbook-Ausschnitt

1. Impact und betroffene Route bestätigen.
2. Trace-IDs und Upstream-Fehler sammeln.
3. Upstream-Health und Timeout-/Error-Metriken prüfen.
4. Ein Restart oder Traffic-Switch benötigt Freigabe des Incident Commanders.
5. Ohne Recovery-Evidence keinen Incident als resolved markieren.

Die Root Cause ist in diesem Evidence-Stand bewusst nicht bestätigt.
