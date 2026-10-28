#!/usr/bin/env python3
"""Validate offline resource metadata and synchronize the JSON index."""
import argparse
import csv
import json
from pathlib import Path
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["id", "kind", "area", "title", "year", "date", "url", "why", "code", "note"]
KINDS = {"paper", "survey", "benchmark", "project", "runtime", "guide", "related"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sync-json", action="store_true")
    args = parser.parse_args()
    with (ROOT / "data/resources.csv").open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            print("Invalid CSV header", file=sys.stderr)
            return 1
        rows = list(reader)
    errors, ids, urls = [], set(), set()
    for number, row in enumerate(rows, 2):
        if not row["id"] or row["id"] in ids:
            errors.append(f"row {number}: duplicate or missing id")
        ids.add(row["id"])
        if not row["url"] or row["url"] in urls:
            errors.append(f"row {number}: duplicate or missing URL")
        urls.add(row["url"])
        for key in ("url", "code"):
            if row[key]:
                parsed = urlparse(row[key])
                if parsed.scheme != "https" or not parsed.netloc:
                    errors.append(f"row {number}: invalid {key} URL")
        if row["kind"] not in KINDS:
            errors.append(f"row {number}: unknown kind")
        if not row["year"].isdigit() or not (2022 <= int(row["year"]) <= 2026):
            errors.append(f"row {number}: invalid year")
        if len(row["why"]) < 25:
            errors.append(f"row {number}: short description")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    for row in rows:
        row["year"] = int(row["year"])
    output = ROOT / "data/resources.json"
    if args.sync_json:
        output.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    elif not output.exists() or json.loads(output.read_text(encoding="utf-8")) != rows:
        print("JSON out of sync; run python scripts/validate.py --sync-json", file=sys.stderr)
        return 1
    print(f"OK: {len(rows)} entries validated (offline; not live URL check)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
