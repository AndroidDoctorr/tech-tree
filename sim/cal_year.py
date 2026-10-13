#!/usr/bin/env python3
"""Civil calendar from absolute campaign day — see journal/retcons/CAL-Y-EPOCH-Y13.md."""

from __future__ import annotations

import argparse

# Canonical anchor: d4620 = Cal-Y13 D1 (~1 Jan Y13).
ANCHOR_DAY = 4620
ANCHOR_YEAR = 13
DAYS_PER_YEAR = 365


def civil(d: int) -> tuple[int, int]:
    if d < ANCHOR_DAY:
        raise ValueError(
            f"day {d} is before anchor d{ANCHOR_DAY}; use journal headers or extend anchor table"
        )
    offset = d - ANCHOR_DAY
    year = ANCHOR_YEAR + offset // DAYS_PER_YEAR
    doy = 1 + offset % DAYS_PER_YEAR
    return year, doy


def main() -> None:
    p = argparse.ArgumentParser(description="Civil Cal-Y / D from absolute day d####")
    p.add_argument("--day", type=int, required=True, help="Absolute campaign day")
    args = p.parse_args()
    y, doy = civil(args.day)
    print(f"d{args.day}  ->  Cal-Y{y} D{doy}  (tag new IDs: CY{y})")


if __name__ == "__main__":
    main()
