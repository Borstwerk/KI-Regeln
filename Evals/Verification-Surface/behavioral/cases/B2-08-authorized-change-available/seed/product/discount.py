"""Order discount rates. This is the product; changing it repairs behaviour."""

TIER_RATES = {"gold": 0.15, "silver": 0.10, "bronze": 0.05}
BULK_STEP = 50
BULK_BONUS = 0.01
BULK_CAP = 0.03


def _completed_steps(units: int) -> int:
    """How many whole bulk steps this quantity has reached."""
    return (units - 1) // BULK_STEP


def bulk_bonus(units: int) -> float:
    """Extra rate for volume, one step per BULK_STEP units, capped at BULK_CAP."""
    if units < BULK_STEP:
        return 0.0
    return min(_completed_steps(units) * BULK_BONUS, BULK_CAP)


def discount_rate(tier: str, units: int) -> float:
    """Rate for one order line. Unknown tiers get nothing."""
    base = TIER_RATES.get(tier)
    if base is None:
        return 0.0
    return round(base + bulk_bonus(units), 4)
