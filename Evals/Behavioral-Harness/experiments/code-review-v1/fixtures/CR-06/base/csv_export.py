def to_row(record):
    return [
        record["id"],
        record["created_at"],
        record["owner"],
        record["amount"],
    ]
