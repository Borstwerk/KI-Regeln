# Separate verification — AUTH-003

Element: `selected-tests`
Authorized post-change state: `[test_gold_rate_is_exactly_fifteen_percent]`

The test `test_unknown_tier_yields_no_discount` was removed from the selection because
the behaviour it covered moved behind a separate contract check that runs in an earlier
stage. The reduction of this filter was reviewed independently of the agent loop that
requested it, by someone who did not author the change.

Recorded here as a bound artifact rather than as a bare reference so that the engine can
verify deterministically that *this* document, byte for byte, is the one the ledger
points at. Verifying that the document exists and is unaltered is not the same as
judging that its content is a good reason — B1 does the former only.
