#!/usr/bin/env python3
"""
Annual ice-vault draw — one number per civil year, not daily melt logs.

Calibrated to journal retcons:
  - ICE-VAULT-DRAW-Y12-Y13.md  (~125.8 → ~87 kg before peak haul)
  - ICE-VAULT-DRAW-Y13-Y14.md  (~128.5 → ~88.7 kg before peak haul)

Napkin physics (commentary only — the game uses the fitted components):
  Q_passive ≈ U_eff · A_vault · Σ degree-days_above_melt
  m_melt = Q_passive / L_f   (L_f ≈ 334 kJ/kg for ice)
  U_eff is dominated by straw/shive/earth insulation + lid discipline;
  the fitted ~11.5 kg/yr "summer edge" at full pack is ~30 W average Jun–Sep class.

Usage:
  python sim/ice_vault.py annual --start 128.2
  python sim/ice_vault.py annual --start 128.2 --hero-draw 0.8
  python sim/ice_vault.py annual --start 88.7 --no-ice-break
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

# Practical pack cap (both niches + trays) — precedents d3189, d3921, d4657
CAP_FULL_KG = 130.0

# Component draws at start_kg == CAP_FULL (kg ice mass out in one civil year)
# Sum ≈ 37.5 kg — matches ~30–40 kg/yr doctrine in retcons
COMPONENTS_FULL = {
    "summer_edge_melt": 11.5,  # Jun–Sep lip/slush tray culls (mostly passive)
    "milk_niche_cheese": 8.5,  # goat milk crock · cheese cool mass · niche refresh
    "cellar_turnover": 18.0,  # hard blocks consumed in repack · net mass out
}


@dataclass
class AnnualDraw:
    start_kg: float
    scale: float
    lines: list[tuple[str, float]]
    hero_draw_kg: float
    ice_break_cull_kg: float
    total_kg: float
    end_kg: float
    headroom_kg: float


def _scale(start_kg: float) -> float:
    """Linear in pack mass — half-full vault loses mass slower."""
    if start_kg <= 0:
        return 0.0
    return min(1.0, start_kg / CAP_FULL_KG)


def ice_break_cull(start_kg: float) -> float:
    """East-tray slush cull at pre-peak prep (Feb class)."""
    return round(1.0 + 0.006 * start_kg, 1)


def annual_draw(
    start_kg: float,
    *,
    hero_draw_kg: float = 0.0,
    apply_ice_break: bool = True,
) -> AnnualDraw:
    scale = _scale(start_kg)
    lines: list[tuple[str, float]] = []
    subtotal = 0.0
    for name, full in COMPONENTS_FULL.items():
        amt = round(full * scale, 1)
        lines.append((name, amt))
        subtotal += amt
    subtotal = round(subtotal, 1)
    cull = ice_break_cull(start_kg) if apply_ice_break else 0.0
    hero = round(hero_draw_kg, 2)
    total = round(subtotal + cull + hero, 1)
    end = round(max(0.0, start_kg - total), 1)
    headroom = round(max(0.0, CAP_FULL_KG - end), 1)
    return AnnualDraw(
        start_kg=start_kg,
        scale=scale,
        lines=lines,
        hero_draw_kg=hero,
        ice_break_cull_kg=cull,
        total_kg=total,
        end_kg=end,
        headroom_kg=headroom,
    )


def _print_report(d: AnnualDraw) -> None:
    print(f"Ice vault annual draw (start {d.start_kg:.1f} kg · scale {d.scale:.3f} @ cap {CAP_FULL_KG:.0f} kg)")
    print()
    print("| Component | kg |")
    print("|---|---:|")
    for name, amt in d.lines:
        label = name.replace("_", " ")
        print(f"| {label} | {amt:.1f} |")
    if d.ice_break_cull_kg:
        print(f"| ice-break slush cull (Feb prep) | {d.ice_break_cull_kg:.1f} |")
    if d.hero_draw_kg:
        print(f"| hero draws (logged) | {d.hero_draw_kg:.1f} |")
    print(f"| **total** | **{d.total_kg:.1f}** |")
    print()
    print(f"End mass (pre-haul): {d.end_kg:.1f} kg hard")
    print(f"Headroom to ~{CAP_FULL_KG:.0f} kg cap: {d.headroom_kg:.1f} kg")


def main() -> None:
    parser = argparse.ArgumentParser(description="Annual ice vault melt + use model")
    sub = parser.add_subparsers(dest="cmd", required=True)

    annual = sub.add_parser("annual", help="One civil year of draw from ice-close mass")
    annual.add_argument("--start", type=float, required=True, help="kg hard @ last ice close or Aug read")
    annual.add_argument(
        "--hero-draw",
        type=float,
        default=0.0,
        help="Extra kg from logged heroes (TC bath, etc.)",
    )
    annual.add_argument(
        "--no-ice-break",
        action="store_true",
        help="Omit Feb pre-peak slush cull (mid-year read only)",
    )

    args = parser.parse_args()
    if args.cmd == "annual":
        d = annual_draw(
            args.start,
            hero_draw_kg=args.hero_draw,
            apply_ice_break=not args.no_ice_break,
        )
        _print_report(d)


if __name__ == "__main__":
    main()
