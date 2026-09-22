# Crops

What is standing in the ground right now. Harvested stock moves to [food.md](food.md) or [resources.md](resources.md) and comes off this file.

`| ID | Crop | Where | Sown | State |`

`Sown` rather than `Made`, and it is a schedule input rather than a keep window — everything downstream is read against [calendar.md](../checklists/calendar.md). This is the one inventory file where the date tells you what to *do* rather than what is still good.

Y10 sow ran **d3211–d3219**. Bed geometry is [map](../map/index.md); what to select for is [crop-selection-improvement-code-1.md](../government/regulations/crop-selection-improvement-code-1.md).

## Bed A

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `HEMP-SEL-Y10` | Hemp · ★ **the Ghab line, gen 4 since Y7** | Bed A north · **stubble ~10 cm post cut d3381** | d3381 | ✓ **`HEMP-CUT-Y10-1` d3381** · **`P-RETT-31` CLOSED d3399** |
| `FAVA-Y10` | Fava | Bed A west | d3214 | ✓ **Seed strip harvested d3345** · **`P-FAVA-Y10` banked** · ground **fallow / nodules left** |
| `BARLEY-TRIAL-Y10` | Barley, trial | Bed A south, ~3 m² | Y10 | Standing |
| — | Chickpea ground | Bed A | — | Fallow · hands off |

☠ The Ghab hemp is an **obligate outcrosser** and its spare seed died at d3218. This standing crop is the only copy of gen 4 in existence. Isolate by **time, not distance** — pollen carries for kilometres and there is no corner of the campus far enough away. See `HEMP-CUT` in [harvest.md](../government/procedures/harvest.md).

## Bed B

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FLAX-FIELD-Y10` | Flax, field · expansion | Bed B centre, ~10 m² | Y10 | Standing |
| `EMMER-Y10` | Emmer | Bed B south | Y10 | Standing |
| `P-17-LENTIL-Y10` | Lentil | Bed B north margin | d3212 | Standing |
| `MADDER-BED-B` | Madder ×4 | Bed B west | — | Perennial · hands off |
| `GYPSUM-STRIP-TRIAL-1` | Gypsum strip trial · ×6 alternating ~2 m blocks, ~150 g/m², staked | Bed B lentil run | d3225 | Live · **weigh by block** |

`GYPSUM-STRIP-TRIAL-1` reads on rain-crust and flowering, and it is a `CI-1` observation row — the comparison only works if the blocks are weighed separately at harvest. An unweighed trial is a wasted season.

## Bed C

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `SEED-INCREASE-BLOCK-Y10` | Emmer elite increase · ~95 g drawn from `EMMER-ELITE-Y9` | Bed C SW | d3211 | Standing |
| `P-18-CHICKPEA-Y10` | Chickpea | — | d3212 | Standing |

Bed C north is the goat pen, not crop ground — `GOAT-KIDDING-STALL-1` NE ~2.5 × 2 m, billie tie west. See [animals.md](animals.md).

## Bed D

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FIG-C1…C4` | Fig ×4 | Bed D | d3368 | **Aug pick in progress** · third pass d3380 · repeat through 15 Sep |
| `WOAD-BED-D` | Woad, year-two rosette | Bed D | Y9 | ✓ **`WOAD-LEAF-Y10-1` pulled d3345** · crown intact · window to 18 Aug |

Figs run **1 Aug – 15 Sep** and are flagged on every `FARM-CARE` pass in band — pick or leather on the pass rather than queuing a separate hero.

## Herbs

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `CULINA-HERB-BED` | Rosemary · coriander · allium · mint · parsley S band | Culina herb bed, ~14 m² | d3219 | Standing |
| `HERB-LAYER-1` | ×4 rosemary · ×4 thyme, pegged and stoned | Herb margin | d3219 | Layering · **sever in autumn once rooted** |
| `MINT-CROCK-1` | Mint, bottomless crock sunk to the rim | Culina bed | d3219 | Runners contained |

Mint in open ground takes the bed. The sunk bottomless crock is the containment, and it only works while the rim stays proud.

## Perennials — vine and tree

| ID | Crop | Where | Planted | State |
|---|---|---|---|---|
| `P-03-TRELLIS` | Grape, cordon-trained | P-03 trellis | — | Budbreak · shoot-thinned d3235 |
| `P-02-OLIVE` | Olive terrace | P-02 | — | Standing · Nov pick and press band |

★ **`P-03` has one cordon arm winter-killed.** The renewal shoot is tow-tied and must be trained along the wire all season — ⚠ **do not thin it off.** That shoot is the arm. Most shoots carry two inflorescences; cluster-thin after fruit set to ~12–15 leaves per cluster.

## Wild patches

Stands drawn on but not tended. Where they are is [map region resources](../map/region/resources.md); this file says only that they exist and what condition they are in.

| ID | Stand | Where | State |
|---|---|---|---|
| `P-04` · `P-05-A/B` · `P-06-A/B/C` | Wild grain | — | Standing |
| `FLAX-PATCH-1` | Wild flax band | Ditch W · T-1 lip | ✓ **Laps 1–2 d3333–d3343 · ~6.5 kg green Y10 · window to 26 Jul** |
| `P-01` | Pistachio | T-2, ~160 m | **Y10 primary picked d3409 · hull drying** |
| `P-22` | Wild hemp | Ghab plain · east string | **Seed strip d3413 · partial heads · patch standing** |
| `P-12` | Fig | 650 m | Standing |
| `PINE-TAP-CUPS` | Pine, ×8 trees scored and cupped | Pine stand | **Standing — collect on the pass** |

★ **Mark the wild grain stands in March while they are green.** In June they are indistinguishable from everything around them.

`P-01`, `P-12` and `P-02` are **calendar heroes, not scare-pass items** — they do not get flagged automatically on a farm check.

## Retting

Retting is a crop process rather than a stock, so the live arc lives here and the finished line goes to [resources.md](resources.md).

| ID | Load | Where | Loaded | State |
|---|---|---|---|---|
| `P-RETT-28` | Flax wild · lap 1 | ✓ **CLOSED d3401** · spun to cover thread | d3333 | — |
| `P-RETT-29` | Flax wild · lap 2 | ✓ **CLOSED d3401** · spun to cover thread | d3343 | — |
| `P-RETT-30` | Hemp wild · **`HEMP-GHAB-FIBRE-Y10`** | ✓ **CLOSED d3383** · ~1.89 kg line class | d3365 | — |
| `P-RETT-31` | Hemp Bed A · **`HEMP-CUT-Y10-1`** | ✓ **CLOSED d3399** · ~1.08 kg line → ~695 m thread | d3383 | — |

Last arc **`P-RETT-28/29`**, closed d3401 — **~1,050 m @ `FLAX-THREAD-COVER-Y10-1`**. Hemp **`P-RETT-31`** closed d3399. Troughs empty · **`W-1` clear**.

⚠ The rett clock is **10–14 days from pool load** and it is checked on every farm scare pass, not on a calendar — see [farm-scare-rett-pull](../.cursor/rules/farm-scare-rett-pull.mdc). A bundle left submerged past its window is over-retted and the fibre is lost.

## Care

`FARM-CARE` runs scare-only on live rows. Perennial flags, bird devices and the sow gate are in [calendar.md](../checklists/calendar.md), [periodic.md](../checklists/periodic.md) and [conditional.md](../checklists/conditional.md).
