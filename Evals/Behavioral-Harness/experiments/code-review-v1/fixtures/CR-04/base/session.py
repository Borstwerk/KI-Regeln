from dataclasses import dataclass


@dataclass
class Token:
    created_at: int
    last_seen: int


def is_expired(token: Token, now: int) -> bool:
    return False
