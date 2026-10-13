# Norima wagon — wear, tune, overhaul

**Asset:** `WAGON-V2-CHASSIS-1` (Norima) · live counters in [hazards.md](../../hazards.md) **Live state**

**Dual ledger** *(from d4615 · [retcon](../../journal/retcons/WAGON-WEAR-DUAL-LEDGER-Y15.md)):*

| Counter | What it is | Fixes |
|---|---|---|
| **`norima_service_wear`** | **Service debt** — dry hubs, lash slack, wedge creep, rim wobble, cover drain fuss | **`WAGON-V2-TUNE-*`** (−6 or −4) · scare grease **0** |
| **`norima_fatigue_wear`** | **Structural debt** — tyre thinning, hub bore oval, cracked bed oak, crushed lash points | **`WAGON-V2-OVERHAUL-*`** only *(replace metal · swap planks · re-bush)* |

**Hazard rolls** use **effective wear**, not service alone:

`effective_wear = min(100, service_wear + round(fatigue_wear × 0.35))`

Log both numbers in tune/overhaul close tables. Patch **`hazards.md`** same pass.

**Scale:** each counter **0–100** — index, **not** rim mm.

## Margin haul tick *(Y14 grammar)*

**One +1 wear = two qualifying margin haul days**, not one.

| Qualifies | Does not |
|---|---|
| **`WOOD-HAUL-*`** fell + 2-load @ T-1 ([HAUL-GRAMMAR-Y14](../../journal/retcons/HAUL-GRAMMAR-Y14.md)) | Block lift · char · kiln · garage · campus empty roll |
| **`SAND-HAUL-*`** 2-load + sieve @ weir | Single-lap legacy cart grammar |
| **`HAUL-LIME-*`** knap + 2-load @ pile 7 stub | Heavy manifest **+1** days (each counts as **one** haul toward the pair **and** may add **+1** immediately — see hazards ledger) |

**Procedure:**

1. On each qualifying haul close: increment **`norima_margin_haul_parity`** (0 → 1 → 0).
2. When parity returns **0** after increment *(i.e. completed the second haul)*: **`norima_service_wear +1`** · **`norima_fatigue_wear +1`** every **fourth** completed margin pair *(~annual structural tick class)*.
3. On **`WAGON-V2-TUNE-*`** or **`WAGON-V2-OVERHAUL-*` D3 close**: set **`norima_margin_haul_parity → 0`**.

Log in the day file post table: **`Norima service 16 hold · margin haul 1/2`** or **`15 → 16 · margin haul 2/2`** *(fatigue unchanged unless 4th pair)*.

## Tripwires *(agent + player)*

Tripwires use **effective wear** for mishap severity; **service** for “when to grease/tune”:

| Effective | Read | Action |
|---|---|---|
| **≤22** | Normal | Normal hauling |
| **23–30** | **Schedule tune** | Flag in `now.md` · book **`WAGON-V2-TUNE-*`** |
| **31–45** | **Due tune** | **Tune before next loaded margin haul** |
| **46–60** | Parts wearing | Tune **−4 only** · plan overhaul if **fatigue ≥ 28** |
| **61+** | Failure band | **No loaded haul** until tune or overhaul |

| Service alone | Read |
|---|---|
| **≤15** | Fresh / post tune or overhaul |
| **16–22** | Normal season |
| **23+** | Same tune schedule as effective **23+** even if fatigue is low |

| Fatigue alone | Read |
|---|---|
| **≤18** | Young chassis |
| **19–27** | Plan overhaul in next quiet band |
| **28+** | **Overhaul before long exped** — tune cannot buy rim/bed life back |

## Tune vs overhaul

| Event | Δ service | Δ fatigue | Consumes | Notes |
|---|---|---|---|---|
| **`WAGON-V2-TUNE-*`** full day @ `WAGON-GARAGE-1` | **−6** if service **≤45** · **−4** if **46–60** | **0** | ~15–20 g tallow hub pack · soap wash | Grease · lash · trim · cover · empty cert — **no plank/tyre swap** |
| **`WAGON-V2-OVERHAUL-*` D1–D3** | **set → 15** | **−8 to −15** *(per log)* | Forge iron · oak bed · nails · char | Strip · forged strips/collars · bush · rim dress · **plank swap** · cert D3 |
| **Farm-scare hub grease** (minutes) | **0** | trace | Not a substitute for tune |
| **Partial grease pass** | **0** | trace | Not a substitute for tune |

**Floor after tune:** `service_after = max(10, service_before − delta)` — fatigue unchanged.

**Legacy journal rows** saying **`Norima wear`** before d4615 mean **service wear** unless the day is an overhaul close (then note fatigue if logged).

## Hazard rolls on loaded hauls

When **effective wear ≥ 31** on a margin haul day, log **CART-WHEEL-MISHAP** / **WAGON-HUB-BIND** with modifier from [hazards.md](../../hazards.md):

`modifier = (effective_wear / 50) × load_mult × terrain_mult`

Below **31**, routine margin hauls may use the campaign’s abbreviated audit line; still **log wear parity**.

## Agent duty

On **day open** and after any **margin haul** or **tune**:

1. Read **service · fatigue · parity** from `hazards.md` · compute **effective**.
2. If **effective ≥ 23** or **service ≥ 23**: one-line warning in the player reply.
3. If **effective ≥ 31** and the planned day is a loaded haul: **warn** until tune logged (player override explicit only).
4. If **fatigue ≥ 28**: flag overhaul in `now.md` open arcs.
4. Patch **`hazards.md` Live state** same pass as the day file.
