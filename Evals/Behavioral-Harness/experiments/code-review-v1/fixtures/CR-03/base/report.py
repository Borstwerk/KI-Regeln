import argparse


def format_text(rows):
    return "\n".join(f"{r['name']}: {r['value']}" for r in rows)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="report")
    parser.add_argument("--source", required=True)
    args = parser.parse_args(argv)
    rows = load_rows(args.source)
    print(format_text(rows))
    return 0
