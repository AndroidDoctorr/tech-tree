# RETCON — fume hood tiles are **TF (kaolin)**, not **TR (roof)**

**Filed:** Day 3862 · Cal-Y12 D343 *(inventory audit · player correction)*

## Problem

1. Days **3841** and **3843** correctly used **`TILE-TF`** (flat kaolin) for **`LAB-FUME-CABINET-1`** — **×14 interior · ×8 duct**.
2. Days **3844**, **3845**, and **3859** were logged as **`TR-PRESS` / `TR-FIRE`** with **`CLAY-P1`** — **wrong class entirely**. Player intent:
   - **Press/firing Nov–Dec Y12 = kaolin TF for the fume hood**, not roof TR.
   - **Roof TR bank is hold-only** — **`ROOF-R&D-SHINGLE-Y10-1` / `FLAX-THREAD-SHINGLE-Y10-1`** supersedes new curved TR.

| Code | Shape | Body | Press |
|---|---|---|---|
| **TR** | Curved roof half-pipe | `CLAY-P1` terracotta | `TILE-FORM-1` **roof face** |
| **TF** | Flat floor square | Washed **kaolin** slip | `TILE-FORM-1` **floor face** / `MARVER-FLAT-PLATE-1` |

## Correction

| Was (invalid) | Now (canon) |
|---|---|
| **`TR-PRESS-3844/3845/3859`** | **`TF-PRESS-3844/3845/3859`** @ floor face · **`KAOLIN-SLIP-M26-1`** body |
| **`TR-FIRE-3844-3845-3859`** | **`TF-FIRE-3844-3845-3859`** @ **`KILN-B`** · **31/32 good** |
| **`CLAY-P1` −~14.4 kg** tile draws | **No clay draw** — kaolin only |
| **`TILE-TR` +×31 fired · `TR-3859` green** | **Reverted** — **`TILE-TR` ×54 hold @ rack south** |
| **`TR-TILE-REPLEN-Y12`** | **`TF-FUME-TILE-Y12`** — fume hood kaolin stock |

## Kaolin draw (×48 green · ~4.6 kg slip eq. per ×16 module)

| Day | Draw |
|---|---|
| **d3844** | **`KAOLIN-SLIP-M26-1` −~4.6 kg** · ×16 green **`TF-3844`** |
| **d3845** | **`KAOLIN-SLIP-M26-1` −~4.4 kg** + **`M26-BEST` −~0.2 kg** · ×16 **`TF-3845`** |
| **d3859 press** | **`KAOLIN-CAND-3S` wash −~2.0 kg wet** + **`M26-BEST` −~0.08 kg** · ×16 **`TF-3859`** |

## Stock post-fix

| ID | Qty |
|---|---|
| **`TILE-TR` fired** | **×54** @ rack south *(hold · shingle runway)* |
| **`TILE-TF` fired** | **×31** @ rack north *(+×108 hub laid · **−×22 fume d3841/3843**)* |
| **`TILE-TF-GREEN`** | **×16 `TF-3859`** @ north sand bed |
| **`FT-Y8-FLOOR-TILE`** | **×0** @ bench *(−×16 backsplash · −×9 fume partial)* |
| **`CLAY-P1`** | **~28.6 kg** *(no d3859 tile debit)* |
| **`KAOLIN-SLIP-M26-1`** | **trace** |
| **`KAOLIN-CAND-3S`** | **×0** — consumed d3859 wash |

## Patched

- `inventory/resources.md`
- `journal/days/year-011/week-549/day-3841.md` *(unchanged class)*
- `journal/days/year-011/week-549/day-3843.md` *(unchanged class)*
- `journal/days/year-011/week-550/day-3844.md`
- `journal/days/year-011/week-550/day-3845.md`
- `journal/days/year-011/week-552/day-3859.md`
- `journal/weeks/week-550.md` · `week-551.md` · `week-552.md`
- `now.md`
