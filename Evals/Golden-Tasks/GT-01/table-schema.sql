CREATE TABLE customer_note (
    id BIGINT PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    body TEXT NOT NULL,
    visibility VARCHAR(16) NOT NULL DEFAULT 'internal',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    archived_at TIMESTAMPTZ NULL,
    CONSTRAINT ck_customer_note_visibility
        CHECK (visibility IN ('internal', 'shared'))
);

CREATE INDEX ix_customer_note_customer_created
    ON customer_note (customer_id, created_at DESC);
