def _utc(value):
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def _blank(value):
    return "" if value is None else value


def to_row(record):
    return [
        record["id"],
        record["owner"],
        _utc(record["created_at"]),
        _blank(record["amount"]),
    ]
