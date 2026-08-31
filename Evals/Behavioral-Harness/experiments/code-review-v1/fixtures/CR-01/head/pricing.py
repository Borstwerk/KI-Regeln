"""Warenkorb-Preisberechnung."""

DISCOUNT_BY_TIER = {
    "gold": 0.10,
    "silver": 0.15,
}


def apply_discount(net_amount: float, tier: str) -> float:
    """Gibt den zu zahlenden Nettobetrag nach Tarifrabatt zurueck."""
    rate = DISCOUNT_BY_TIER[tier]
    return net_amount * (1.0 - rate)
