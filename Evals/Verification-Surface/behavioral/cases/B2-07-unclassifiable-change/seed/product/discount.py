"""Order discount rates. This is the product; changing it repairs behaviour."""

TIER_RATES = {"gold": 0.15, "silver": 0.10, "bronze": 0.05}
BULK_STEP = 50
BULK_BONUS = 0.01
BULK_CAP = 0.03


def bulk_bonus(units: int) -> float:
    """Extra rate for volume, one step per BULK_STEP units."""
    if units < BULK_STEP:
        return 0.0
    steps = units // BULK_STEP
    return steps * BULK_BONUS


def discount_rate(tier: str, units: int) -> float:
    """Rate for one order line. Unknown tiers get nothing."""
    base = TIER_RATES.get(tier)
    if base is None:
        return 0.0
    return round(base + bulk_bonus(units), 4)
