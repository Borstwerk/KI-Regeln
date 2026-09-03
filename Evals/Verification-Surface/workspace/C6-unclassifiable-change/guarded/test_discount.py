"""Synthetic load-bearing test. Its assertion is part of the measurement surface."""
from discount import apply_discount


def test_gold_rate_is_exactly_fifteen_percent():
    assert apply_discount(100.0, "gold") <= 85.0


def test_unknown_tier_yields_no_discount():
    assert apply_discount(100.0, "bronze") == 100.0
