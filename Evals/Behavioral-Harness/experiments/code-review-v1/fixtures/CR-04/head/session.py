from dataclasses import dataclass

IDLE_TIMEOUT_SECONDS = 30 * 60


@dataclass
class Token:
    created_at: int
    last_seen: int


def is_expired(token: Token, now: int) -> bool:
    return (now - token.last_seen) > IDLE_TIMEOUT_SECONDS
