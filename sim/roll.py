#!/usr/bin/env python3
"""
Deterministic hazard rolls for the tech-tree journal.

Roll space: 0 .. DENOM-1  (DENOM = 1_000_000_000 — billion-scale, not percent)
Hit when: roll < effective_threshold

Same day + hazard_id + index -> same roll every time (audit / retcon safe).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys

DENOM = 1_000_000_000
CAMPAIGN_SEED = "tech-tree-orontes-y1"

VOLATILITY_MULT = {
    "low": 0.65,
    "normal": 1.0,
    "high": 1.35,
}


def roll_u(day: int, hazard_id: str, index: int = 0) -> int:
    msg = f"{CAMPAIGN_SEED}|{day}|{hazard_id}|{index}"
    digest = hashlib.sha256(msg.encode("utf-8")).hexdigest()
    return int(digest[:16], 16) % DENOM


def effective_threshold(base: int, volatility: str, modifier: float = 1.0) -> int:
    mult = VOLATILITY_MULT.get(volatility.lower(), 1.0)
    value = int(base * mult * modifier)
    return min(DENOM - 1, max(0, value))


def one_in_n(threshold: int) -> str:
    if threshold <= 0:
        return "never (threshold 0)"
    if threshold >= DENOM:
        return "always"
    n = DENOM // threshold
    if DENOM % threshold != 0:
        n += 1
    return f"1 in {n:,}"


def pct(threshold: int) -> str:
    return f"{threshold / DENOM * 100:.6f}%"


def check(
    day: int,
    hazard_id: str,
    threshold: int,
    *,
    volatility: str = "normal",
    modifier: float = 1.0,
    index: int = 0,
) -> dict:
    roll = roll_u(day, hazard_id, index)
    eff = effective_threshold(threshold, volatility, modifier)
    return {
        "day": day,
        "hazard": hazard_id,
        "index": index,
        "roll": roll,
        "threshold": eff,
        "base_threshold": threshold,
        "denom": DENOM,
        "volatility": volatility,
        "modifier": modifier,
        "hit": roll < eff,
        "p_eff": pct(eff),
        "odds_eff": one_in_n(eff),
    }


def parse_threshold(raw: str) -> int:
    """Accept integer threshold, fraction like 1/500000000, or ppm like 0.5ppm."""
    raw = raw.strip().lower()
    if raw.endswith("ppm"):
        ppm = float(raw[:-3])
        return max(0, min(DENOM - 1, int(DENOM * ppm / 1_000_000)))
    if "/" in raw:
        num, den = raw.split("/", 1)
        return max(0, min(DENOM - 1, int(DENOM * float(num) / float(den))))
    return max(0, min(DENOM - 1, int(raw)))


def cmd_check(args: argparse.Namespace) -> int:
    threshold = parse_threshold(args.threshold)
    result = check(
        args.day,
        args.hazard,
        threshold,
        volatility=args.volatility,
        modifier=args.modifier,
        index=args.index,
    )
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        verdict = "HIT" if result["hit"] else "MISS"
        print(
            f"ROLL d{result['day']} · {result['hazard']} · "
            f"{result['roll']:,} / {result['threshold']:,} ({result['p_eff']}) · {verdict}"
        )
        print(f"  odds_eff={result['odds_eff']} · volatility={result['volatility']} · mod={result['modifier']}")
    return 0


def cmd_peek(args: argparse.Namespace) -> int:
    roll = roll_u(args.day, args.hazard, args.index)
    print(f"PEEK d{args.day} · {args.hazard} · roll={roll:,} / {DENOM:,}")
    return 0


def cmd_batch(args: argparse.Namespace) -> int:
    lines = []
    for spec in args.spec:
        # hazard_id:threshold[:modifier]
        parts = spec.split(":")
        hazard_id = parts[0]
        threshold = parse_threshold(parts[1])
        modifier = float(parts[2]) if len(parts) > 2 else 1.0
        result = check(
            args.day,
            hazard_id,
            threshold,
            volatility=args.volatility,
            modifier=modifier,
            index=args.index,
        )
        lines.append(result)
    if args.format == "json":
        print(json.dumps(lines, indent=2))
    else:
        for r in lines:
            verdict = "HIT" if r["hit"] else "MISS"
            print(
                f"{r['hazard']}: {r['roll']:,} < {r['threshold']:,}? {verdict} ({r['p_eff']})"
            )
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Deterministic hazard rolls (tech-tree journal)")
    sub = p.add_subparsers(dest="command", required=True)

    chk = sub.add_parser("check", help="Compare roll to threshold; print HIT/MISS")
    chk.add_argument("--day", type=int, required=True)
    chk.add_argument("--hazard", required=True, help="Hazard ID from hazards.md")
    chk.add_argument(
        "--threshold",
        required=True,
        help="Base threshold (int), fraction (1/500000000), or ppm (0.5ppm)",
    )
    chk.add_argument("--volatility", default="normal", choices=list(VOLATILITY_MULT))
    chk.add_argument("--modifier", type=float, default=1.0, help="Wear/load/state multiplier")
    chk.add_argument("--index", type=int, default=0, help="Second roll same day/hazard")
    chk.add_argument("--format", choices=("text", "json"), default="text")
    chk.set_defaults(func=cmd_check)

    peek = sub.add_parser("peek", help="Show raw roll only")
    peek.add_argument("--day", type=int, required=True)
    peek.add_argument("--hazard", required=True)
    peek.add_argument("--index", type=int, default=0)
    peek.set_defaults(func=cmd_peek)

    batch = sub.add_parser("batch", help="Multiple checks; spec hazard:threshold[:modifier]")
    batch.add_argument("--day", type=int, required=True)
    batch.add_argument("--volatility", default="normal", choices=list(VOLATILITY_MULT))
    batch.add_argument("--index", type=int, default=0)
    batch.add_argument("--format", choices=("text", "json"), default="text")
    batch.add_argument("spec", nargs="+")
    batch.set_defaults(func=cmd_batch)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
