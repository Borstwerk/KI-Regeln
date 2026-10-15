# Technische Referenz: `customer_note`

## Zweck

Die Tabelle `customer_note` speichert textuelle Hinweise zu einem Kundenkontext. Archivierte Einträge bleiben als Datensätze erhalten und werden über `archived_at` gekennzeichnet.

## Spalten

| Spalte | Datentyp | NULL erlaubt | Standardwert | Bedeutung |
|---|---|---|---|---|
| `id` | `BIGINT` | Nein | Keiner | Primärschlüssel des Hinweises. Eine automatische ID-Vergabe ist im bereitgestellten Schema nicht definiert. |
| `customer_id` | `BIGINT` | Nein | Keiner | Kennung des Kundenkontexts. Eine Foreign-Key-Beziehung ist nicht definiert. |
| `body` | `TEXT` | Nein | Keiner | Text des Hinweises. |
| `visibility` | `VARCHAR(16)` | Nein | `'internal'` | Sichtbarkeitswert; erlaubt sind ausschließlich `internal` und `shared`. |
| `created_at` | `TIMESTAMPTZ` | Nein | `now()` | Erstellungszeitpunkt; wird beim Einfügen standardmäßig durch die Datenbank gesetzt. |
| `archived_at` | `TIMESTAMPTZ` | Ja | Keiner | Zeitpunkt der Archivierung; bei nicht archivierten Einträgen `NULL`. |

Ein Standardwert wird verwendet, wenn die betreffende Spalte beim Einfügen ausgelassen wird. Er ersetzt keinen ausdrücklich übergebenen `NULL`-Wert.

## Integritätsregeln

- **Primärschlüssel:** `id` ist eindeutig und darf nicht `NULL` sein.
- **Pflichtfelder:** `customer_id`, `body`, `visibility` und `created_at` dürfen nicht `NULL` sein.
- **Sichtbarkeit:** Der Check-Constraint `ck_customer_note_visibility` erzwingt `visibility IN ('internal', 'shared')`.
- **Textinhalt:** Für `body` ist keine zusätzliche Inhaltsprüfung definiert. Insbesondere verhindert `NOT NULL` keine leere Zeichenfolge.
- **Beziehungen:** Für `customer_id` ist kein Foreign Key definiert. Das bereitgestellte Schema erzwingt daher keine referenzielle Integrität zu einer anderen Tabelle.
- **Zeitpunkte:** Eine Prüfung der zeitlichen Reihenfolge von `created_at` und `archived_at` ist nicht definiert.

## Index

| Name | Spalten und Reihenfolge | Typ | Eindeutig |
|---|---|---|---|
| `ix_customer_note_customer_created` | `customer_id ASC`, `created_at DESC` | B-Tree, impliziter PostgreSQL-Standard | Nein |

Der zusammengesetzte Index unterstützt insbesondere Abfragen nach `customer_id` mit absteigender Sortierung nach `created_at`. Eine garantierte Ergebnisreihenfolge erfordert weiterhin ein ausdrückliches `ORDER BY`.

## Sichtbarkeit und Archivierung

`internal` ist der Standardwert für die Sichtbarkeit; `shared` ist der zweite zulässige Wert. Konkrete Zugriffsrechte oder Freigabemechanismen sind in den bereitgestellten Quellen nicht beschrieben.

Bei der Archivierung bleibt der Datensatz bestehen und erhält einen Wert in `archived_at`. Ein automatischer Archivierungsmechanismus ist im bereitgestellten Schema nicht definiert.

## Nicht festgelegte Eigenschaften

Retention- und Löschfristen sind ausdrücklich unbekannt. Aus den Quellen ergeben sich keine Vorgaben für eine automatische Löschung oder eine Aufbewahrungsdauer.

## Quellen

- `table-schema.sql`: Tabellendefinition, Constraints, Standardwerte und Index.
- `usage.md`: bestätigter Verwendungszweck, Sichtbarkeitswerte, Archivierungsverhalten sowie Angaben zu Beziehungen und Aufbewahrungsfristen.