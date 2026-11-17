#!/usr/bin/env python3
"""Build site/_data/adopted_tools/*.yml from the contributor-facing row sheet."""

import argparse
import csv
import pathlib
import re


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-") or "unnamed"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", default="tools/adoption_rows.tsv")
    parser.add_argument("--out", default="site/_data/adopted_tools")
    args = parser.parse_args()

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    with open(args.rows, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        written = 0
        for row in reader:
            name = (row.get("name") or "").strip()
            if not name or name.lower().startswith("placeholder"):
                continue
            payload = [
                f"name: {name}",
                f"url: {(row.get('url') or '').strip()}",
                f"stars: {(row.get('stars') or '').strip()}",
                f"note: {(row.get('note') or '').strip()}",
            ]
            target = out / f"{slugify(name)}.yml"
            target.write_text("\n".join(payload) + "\n", encoding="utf-8")
            written += 1

    print(f"wrote {written} data file(s) to {out}")


if __name__ == "__main__":
    main()
