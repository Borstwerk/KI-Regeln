**`customer_note` – Tabellenreferenz**

`customer_note` speichert textuelle Hinweise zu einem Kundenkontext.

Die Struktur ist durch `table-schema.sql` definiert. Die bestätigte Nutzung stammt aus `usage.md`. Eine Schema- oder Produktversion ist nicht angegeben.

**Spalten**

Quelle: `table-schema.sql`. „Nicht angegeben“ bedeutet, dass die Spaltendefinition keinen expliziten Default enthält.

| Spalte | SQL-Typ | NULL erlaubt | Default | Bedeutung / Eigenschaft |
|---|---|---|---|---|
| `id` | `BIGINT` | Nein | Nicht angegeben | Primärschlüssel; keine automatische ID-Erzeugung definiert. |
| `customer_id` | `BIGINT` | Nein | Nicht angegeben | Zuordnung zum Kundenkontext; kein Foreign Key definiert. |
| `body` | `TEXT` | Nein | Nicht angegeben | Text des Hinweises. |
| `visibility` | `VARCHAR(16)` | Nein | `'internal'` | Erlaubte Werte: `internal`, `shared`. |
| `created_at` | `TIMESTAMPTZ` | Nein | `now()` | Erstellungszeitpunkt. |
| `archived_at` | `TIMESTAMPTZ` | Ja | Nicht angegeben | Archivierungszeitpunkt. |

**Constraints**

Quelle: `table-schema.sql`.

| Constraint | Definition | Wirkung |
|---|---|---|
| Primärschlüssel; Name nicht explizit angegeben | `PRIMARY KEY (id)` | `id` ist eindeutig und darf nicht `NULL` sein. |
| `ck_customer_note_visibility` | `CHECK (visibility IN ('internal', 'shared'))` | Beschränkt `visibility` auf die beiden angegebenen Werte. Zusätzlich gilt `NOT NULL`. |

Für `customer_id` ist in der bereitgestellten Source of Truth keine Foreign-Key-Beziehung zu einer anderen Tabelle definiert.

**Index**

Quelle: `table-schema.sql`.

| Name | Spaltenreihenfolge | Eindeutig |
|---|---|---|
| `ix_customer_note_customer_created` | `customer_id`, anschließend `created_at DESC` | Nein |

**Bestätigte Nutzung und offene Angaben**

Quelle: `usage.md`.

- `internal` ist die Standardsichtbarkeit; `shared` ist der zweite erlaubte Wert. Weitere Zugriffs- oder Freigabesemantiken sind nicht beschrieben.
- Bei der Archivierung bleibt der Datensatz erhalten und erhält einen Wert in `archived_at`.
- Retention- und Löschfristen sind unbekannt.

Die Dokumentation wurde mit den eingebetteten Fixtures abgeglichen. Das SQL wurde nicht ausgeführt.