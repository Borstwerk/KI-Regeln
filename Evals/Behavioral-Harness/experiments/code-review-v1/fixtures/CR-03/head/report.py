import argparse

import orjson  # neue externe Abhaengigkeit

from formatters import FormatterRegistry


def format_text(rows):
    return "\n".join(f"{r['name']}: {r['value']}" for r in rows)


def format_json(rows):
    return orjson.dumps(rows).decode("utf-8")


REGISTRY = FormatterRegistry()
REGISTRY.register("text", format_text)
REGISTRY.register("json", format_json)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="report")
    parser.add_argument("--source", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    rows = load_rows(args.source)
    formatter = REGISTRY.get("json" if args.json else "text")
    print(formatter(rows))
    return 0
