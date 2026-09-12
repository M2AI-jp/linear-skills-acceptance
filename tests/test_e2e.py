import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class FulfillmentAcceptance(unittest.TestCase):
    def test_command_outputs_and_changed_input(self):
        command = Path(__file__).resolve().parents[1] / "fulfillment.py"
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            source, output = folder / "orders.csv", folder / "out"
            for status, expected in (
                ("confirmed", [["D1", "2"]]),
                ("canceled", []),
            ):
                source.write_text(
                    "id,status,method,boxes\n"
                    f"D1,{status},delivery,2\n"
                    "P1,confirmed,pickup,3\nX1,canceled,delivery,9\n",
                    encoding="utf-8",
                )
                subprocess.run(
                    [sys.executable, str(command), str(source), str(output)],
                    check=True,
                )
                for method, rows in (
                    ("delivery", expected), ("pickup", [["P1", "3"]])
                ):
                    with (output / f"{method}.csv").open(newline="") as stream:
                        self.assertEqual(list(csv.reader(stream)), [["id", "boxes"], *rows])
