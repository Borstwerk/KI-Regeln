from session import Token, is_expired


def test_fresh_token_is_valid():
    token = Token(created_at=1000, last_seen=1000)
    assert is_expired(token, now=1060) is False


def test_old_token_is_expired():
    token = Token(created_at=1000, last_seen=1000)
    assert is_expired(token, now=1000 + 60 * 60) is True
