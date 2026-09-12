"""Fictional fixture for testing a protected GitHub merge."""
import csv
import sys
from pathlib import Path


def main(source, destination):
    with Path(source).open(newline="", encoding="utf-8") as stream:
        orders = list(csv.DictReader(stream))
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    for method in ("delivery", "pickup"):
        rows = [
            row for row in orders
            if row["status"] == "canceled" and row["method"] == method
        ]
        with (destination / f"{method}.csv").open(
            "w", newline="", encoding="utf-8"
        ) as stream:
            writer = csv.writer(stream)
            writer.writerow(("id", "boxes"))
            writer.writerows((row["id"], row["boxes"]) for row in rows)


if __name__ == "__main__":
    main(*sys.argv[1:])
