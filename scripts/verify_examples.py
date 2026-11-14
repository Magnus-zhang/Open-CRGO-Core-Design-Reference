#!/usr/bin/env python3
"""Recompute the illustrative CRGO core mass and loss examples."""

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "core_design_examples.csv"
MM2_TO_M2 = Decimal("0.000001")
OUTPUT_PRECISION = Decimal("0.0001")


def main():
    errors = []
    count = 0
    with DATA_FILE.open(encoding="utf-8", newline="") as csv_file:
        for row in csv.DictReader(csv_file):
            count += 1
            net_area = Decimal(row["gross_area_mm2"]) * Decimal(row["stacking_factor"])
            volume = net_area * MM2_TO_M2 * Decimal(row["equivalent_path_m"])
            mass = volume * Decimal(row["assumed_density_kg_per_m3"])
            baseline_loss = mass * Decimal(row["assumed_strip_loss_w_per_kg"])
            core_loss = baseline_loss * Decimal(row["assumed_building_factor"])
            expected = {
                "net_area_mm2": net_area,
                "estimated_steel_mass_kg": mass.quantize(OUTPUT_PRECISION, ROUND_HALF_UP),
                "strip_loss_baseline_w": baseline_loss.quantize(OUTPUT_PRECISION, ROUND_HALF_UP),
                "estimated_core_loss_w": core_loss.quantize(OUTPUT_PRECISION, ROUND_HALF_UP),
            }
            for column, value in expected.items():
                actual = Decimal(row[column])
                if actual != value:
                    errors.append(f"{row['case_id']} {column}: expected {value}, found {actual}")

    if not count:
        raise SystemExit("No examples found.")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Verified {count} core design examples.")


if __name__ == "__main__":
    main()
