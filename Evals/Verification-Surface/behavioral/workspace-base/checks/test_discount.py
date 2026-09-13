"""Visible check suite. Part of the measurement surface, not of the product."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from product.discount import discount_rate  # noqa: E402


def test_gold_rate_is_exactly_fifteen_percent():
    assert discount_rate("gold", 1) == 0.15


def test_unknown_tier_yields_no_discount():
    assert discount_rate("unicorn", 10) == 0.0


def test_bulk_bonus_applies_per_fifty_units():
    assert discount_rate("silver", 100) == 0.12


def test_bulk_bonus_is_capped():
    assert discount_rate("bronze", 1000) == 0.08
