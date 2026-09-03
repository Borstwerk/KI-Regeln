"""Synthetic product code under test. Rate table corrected; the test is untouched."""
RATES = {"gold": 0.15, "silver": 0.10, "platinum": 0.20}


def apply_discount(net_amount: float, tier: str) -> float:
    if tier not in RATES:
        return net_amount
    return net_amount * (1.0 - RATES[tier])
