import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
DATA = ROOT / "data"


def read_csv(name):
    with (PROJECT / "reports" / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def number(value):
    if value is None or value == "":
        return value or ""
    try:
        return float(value) if "." in value else int(value)
    except ValueError:
        return value


def normalize(rows):
    return [{key.lower(): number(value) for key, value in row.items()} for row in rows]


def write(name, rows):
    DATA.mkdir(parents=True, exist_ok=True)
    (DATA / name).write_text(
        json.dumps(normalize(rows), ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


write("8u-hitting.json", read_csv("8u-hitting-2026.csv"))
write("9u-hitting.json", read_csv("combined-hitting.csv"))
write("9u-pitching.json", read_csv("combined-pitching.csv"))
write("10u-hitting.json", read_csv("10u-hitting-2026.csv"))
write("10u-pitching.json", read_csv("10u-pitching-2026.csv"))
