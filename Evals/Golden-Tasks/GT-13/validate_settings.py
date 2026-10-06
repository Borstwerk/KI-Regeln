from pathlib import Path
import sys

path = Path(sys.argv[1])
values = {}
for raw in path.read_text(encoding="utf-8").splitlines():
    if ":" not in raw:
        continue
    key, value = raw.split(":", 1)
    values[key.strip()] = value.strip()

errors = []
if values.get("mode") != "safe":
    errors.append("mode must be safe")
if values.get("retry_limit") != "3":
    errors.append("retry_limit must remain 3")

if errors:
    for error in errors:
        print(error)
    raise SystemExit(1)

print("PASS")
