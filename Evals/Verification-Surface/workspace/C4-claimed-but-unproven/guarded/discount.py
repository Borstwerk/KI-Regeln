"""Synthetic product code under test."""
RATES = {"gold": 0.15, "silver": 0.10}


def apply_discount(net_amount: float, tier: str) -> float:
    return net_amount * (1.0 - RATES.get(tier, 0.0))
