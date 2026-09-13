"""Thin driver for the held-out oracle. This file enters the isolated view; nothing else does.

It knows the shape of an input and how to load the product. It does not know what any answer
is supposed to be: expectations live outside the view and the comparison happens there. Code
that reads this file learns the input shape and nothing about what is expected of it.

Protocol: one JSON object per line on stdin, one JSON object per line on stdout.
"""
import json
import sys


def main() -> int:
    sys.path.insert(0, "/workspace")
    try:
        from product.discount import discount_rate
    except Exception as exc:  # a product that will not import is an observable output
        for line in sys.stdin:
            if line.strip():
                case = json.loads(line)
                print(json.dumps({"id": case["id"], "error": f"{type(exc).__name__}: {exc}"}))
        return 0
    for line in sys.stdin:
        if not line.strip():
            continue
        case = json.loads(line)
        try:
            value = discount_rate(case["tier"], case["units"])
            out = {"id": case["id"], "value": value}
        except Exception as exc:
            out = {"id": case["id"], "error": f"{type(exc).__name__}: {exc}"}
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
