# Wagon wear — dual ledger (service + fatigue)

**Filed:** d4615 · **Cal-Y15**

## Problem

**`Norima wear`** was a single **0–100** index used for both **hazard rolls** and **maintenance scheduling**. Tunes (−6) and overhauls (reset → 15) mixed **reversible neglect** (dry hubs, slack lash) with **irreversible loss** (thin tyre metal, oval bores, cracked bed oak, elongated bolt holes). Margin ticks after **d4546** were not always patched to **`hazards.md`**, so **`now.md`** and live state could diverge.

## Fix — two counters

| Counter | Meaning | Historic parallel |
|---|---|---|
| **`norima_service_wear`** | **Temporary / service debt** — grease, lash, wedge creep, rim wobble from use | Seasonal wagoner's day: tallow pack, tighten tyres, reset bed wedges |
| **`norima_fatigue_wear`** | **Permanent / structural debt** — metal thinning, hub bore wear, plank checks, lash-point crush | Shop rebuild: re-tyre, re-bush, swap bed boards, new collars |

**Hazard modifier** uses **effective wear**:

`effective = min(100, service + round(fatigue × 0.35))`

*(Tune does not erase fatigue; overhaul replaces parts and drops fatigue.)*

## Baseline @ d4615 open *(audit)*

| Field | Value | Notes |
|---|---|---|
| **Service** | **18** | **14 @ d4546 tune** + margin / yard drift not logged |
| **Fatigue** | **24** | **Estimated** — ~3 Cal-Y since **`WAGON-V2-OVERHAUL-Y10` d3442** · not tracked before this retcon |
| **Parity** | **0** | Cleared d4546 |

## Close @ **`WAGON-V2-OVERHAUL-Y15-1` d4617**

| Field | Value |
|---|---|
| **Service** | **15** *(overhaul close grammar)* |
| **Fatigue** | **11** *(bed planks ×3 · strips · bush · rim dress)* |
| **Effective** | **~19** |

Procedure: [wagon-wear.md](../../government/procedures/wagon-wear.md).
