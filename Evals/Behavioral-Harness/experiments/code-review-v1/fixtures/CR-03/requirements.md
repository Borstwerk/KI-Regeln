# Anforderung REPORT-88: JSON-Ausgabe fuer den Report-CLI

Quelle: freigegebenes Ticket, Stand 2026-07-14.

## Akzeptanzkriterien

- **AC-1**: `report` akzeptiert den Schalter `--json`.
- **AC-2**: Mit `--json` wird derselbe Report als JSON auf stdout ausgegeben.
- **AC-3**: Ohne `--json` bleibt die bisherige Textausgabe unveraendert.

## Ausdruecklich nicht beauftragt

- Weitere Ausgabeformate.
- Umbau der Formatter-Struktur.
- Aenderungen an anderen Modulen.
