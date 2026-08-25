# Migration Context

## Quelle

`legacy_events(id BIGINT PRIMARY KEY, account_id BIGINT NOT NULL, payload TEXT NOT NULL, created_at TIMESTAMPTZ NOT NULL)`

## Ziel

`events_v2(event_id BIGINT PRIMARY KEY, tenant_id BIGINT NOT NULL, payload_json JSONB NOT NULL, occurred_at TIMESTAMPTZ NOT NULL, migration_batch VARCHAR(64) NOT NULL)`

## Bestätigtes Mapping

- `id` → `event_id`
- `account_id` → `tenant_id`
- `payload` enthält in dieser Fixture valides JSON und wird geparst → `payload_json`
- `created_at` → `occurred_at`
- `migration_batch` wird durch den Backfill gesetzt.

## Constraints

- Ein Backfill-Batch darf höchstens 50000 Quellzeilen enthalten.
- Quelle und Ziel müssen nach Beginn des Backfills sieben Tage koexistieren.
- Der finale Cutover benötigt ausdrückliche menschliche Freigabe.
- Gesamtzahl der Datensätze und erwartete Laufzeit sind **nicht** angegeben.
