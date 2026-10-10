# Norima wagon — wear, tune, overhaul

**Asset:** `WAGON-V2-CHASSIS-1` (Norima) · live counter in [hazards.md](../../hazards.md) **Live state**

**Scale:** **0–100** maintenance-debt index — **not** rim mm. Tracks deferred work on **hubs · iron tyres · bed wear strips · lash · cover · hitch**.

## Margin haul tick *(Y14 grammar)*

**One +1 wear = two qualifying margin haul days**, not one.

| Qualifies | Does not |
|---|---|
| **`WOOD-HAUL-*`** fell + 2-load @ T-1 ([HAUL-GRAMMAR-Y14](../../journal/retcons/HAUL-GRAMMAR-Y14.md)) | Block lift · char · kiln · garage · campus empty roll |
| **`SAND-HAUL-*`** 2-load + sieve @ weir | Single-lap legacy cart grammar |
| **`HAUL-LIME-*`** knap + 2-load @ pile 7 stub | Heavy manifest **+1** days (each counts as **one** haul toward the pair **and** may add **+1** immediately — see hazards ledger) |

**Procedure:**

1. On each qualifying haul close: increment **`norima_margin_haul_parity`** (0 → 1 → 0).
2. When parity returns **0** after increment *(i.e. completed the second haul)*: **`Norima wear +1`**.
3. On **`WAGON-V2-TUNE-*`** or **`WAGON-V2-OVERHAUL-*` D3 close**: set **`norima_margin_haul_parity → 0`**.

Log in the day file post table: **`Norima wear 16 hold · margin haul 1/2`** or **`15 → 16 · margin haul 2/2`**.

## Tripwires *(agent + player)*

| Wear | Read | Action |
|---|---|---|
| **≤15** | Fresh / post tune or overhaul | Normal hauling |
| **16–22** | Normal season | No hero required |
| **23–30** | **Schedule tune** | Flag in `now.md` header · book **`WAGON-V2-TUNE-*`** on next HOME week or after exped return |
| **31–45** | **Due tune** | **Tune before next loaded margin haul** · mishap tiers worsen |
| **46–60** | Parts wearing | **`WAGON-V2-TUNE-*` buys −4 only** (not −6) · plan **`WAGON-V2-OVERHAUL-*`** |
| **61+** | Failure band | **No loaded haul** until tune or overhaul · bind / rim slip tier live |

## Tune vs overhaul

| Event | Δ wear | Consumes | Notes |
|---|---|---|---|
| **`WAGON-V2-TUNE-*`** full day @ `WAGON-GARAGE-1` | **−6** if wear **≤45** · **−4** if **46–60** | ~15–20 g tallow hub pack · soap wash | Grease · lash · trim · cover · empty cert — **does not replace metal** |
| **`WAGON-V2-OVERHAUL-*` D1–D3** | **set → 15** | Forged / stock parts per overhaul log | Strip · replace tyres / strips / bushings · cert D3 |
| **Farm-scare hub grease** (minutes) | **0** | trace | Not a substitute for tune |
| **Partial grease pass** | **0** | trace | Not a substitute for tune |

**Floor after tune:** `wear_after = max(10, wear_before − delta)` — an old wagon does not read “factory new” without overhaul.

## Hazard rolls on loaded hauls

When wear **≥ 31** on a margin haul day, log **CART-WHEEL-MISHAP** / **WAGON-HUB-BIND** with modifier from [hazards.md](../../hazards.md):

`effective_threshold = base_threshold × (wear / 50) × load_mult × terrain_mult`

Below **31**, routine margin hauls may use the campaign’s abbreviated audit line; still **log wear parity**.

## Agent duty

On **day open** and after any **margin haul** or **tune**:

1. Read **Norima wear** + **parity** from `hazards.md`.
2. If wear **≥ 23**: one-line warning in the player reply (not only in files).
3. If wear **≥ 31** and the planned day is a loaded haul: **block or warn** until tune logged (player override explicit only).
4. Patch **`hazards.md` Live state** same pass as the day file.
