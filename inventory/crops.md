# Crops

What is standing in the ground right now. Harvested stock moves to [food.md](food.md) or [resources.md](resources.md) and comes off this file.

`| ID | Crop | Where | Sown | State |`

`Sown` rather than `Made`, and it is a schedule input rather than a keep window — everything downstream is read against [calendar.md](../checklists/calendar.md). This is the one inventory file where the date tells you what to *do* rather than what is still good.

Y13 sow **d3940**. Bed geometry is [map](../map/index.md); what to select for is [crop-selection-improvement-code-1.md](../government/regulations/crop-selection-improvement-code-1.md).

## Bed A

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `HEMP-SEL-Y13` | Hemp · ★ **Ghab line gen 5** · fibre block | Bed A north | d3940 | **✓ cut d4111 · stubble · ~9.4 kg @ W-1 rafter** |
| `HEMP-GHAB-RESERVE-Y13` | Hemp · seed/disaster block | Bed A north-west · **~6 m²** | d3940 | **Sown thin** · pegged **RESERVE** |
| `FAVA-Y13` | Fava · elite + working | Bed A west · **~8 m²** | d3940 | **First breaks d3952** |
| `P-18-CHICKPEA-Y13` | Chickpea | Bed A south · **~6 m²** | d3940 | **✓ Cut d4218 · stubble · bulk @ horreum** |

☠ Hemp is an **obligate outcrosser** — isolate fibre vs seed blocks **by time** (fibre cut before seed block flowers). See `HEMP-CUT` in [harvest.md](../government/procedures/harvest.md).

## Bed B

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FLAX-FIELD-Y13` | Flax, field · fibre | Bed B centre · **~16 m²** | d3940 | **✓ Pulled d4219 · `P-RETT-37` pulled d4228 · @ W-1 dry queue** |
| `EMMER-Y13` | Emmer | Bed B south + centre · **~10 m²** | d3940 | **✓ Harvest d4216–4217 · bulk @ horreum** |
| `BARLEY-TRIAL-Y13` | Barley trial | Bed B east margin · **~2.5 m²** | d3940 | **✓ Cut d4217 · bulk @ horreum** |
| `P-17-LENTIL-Y13` | Lentil | Bed B north + margin · **~6 m²** | d3940 | **✓ Cut d4217 · bulk @ horreum** |
| `MADDER-BED-B` | Madder ×4 | Bed B west | — | Perennial · hands off |
| `GYPSUM-STRIP-TRIAL-2` | Gypsum strip trial · alternating blocks in lentil run | Bed B lentil run | d3940 | **Staked · in crop** |

## Bed C

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `SEED-INCREASE-BLOCK-Y13` | Emmer elite increase | Bed C south corner · **~3 m²** | d3940 | **✓ Hand strip d4216 · ~196 g elite → vault** |
| `PULSE-DISASTER-Y13` | Lentil regen · **`P-17-ELITE-Y10`** | Bed C SW · **~8 m²** | d3940 | **`SEED-REGEN-Y13` block** |

Bed C north is the goat pen — `GOAT-KIDDING-STALL-1` NE ~2.5 × 2 m, billie tie west. See [animals.md](animals.md).

## Bed D

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FIG-C1…C4` | Fig ×4 | Bed D | d3368 | **✓ pass 1 picked d4098 · repeat pick OK in band** |
| `WOAD-BED-D` | Woad, rosette | Bed D | Y9 | Crown intact · window to 18 Aug |

## Herbs

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `CULINA-CORIANDER-Y13` | Coriander | Culina margin | d3940 | **×6 designated d3970 · `HERB-DES-CORI-Y13-1…6`** |
| `CULINA-ROSEMARY-Y13` | Rosemary | Culina · layers ×4 | d3940 | **Mother rows flagged d3970 · layer route** |
| `CULINA-THYME-Y13` | Thyme | Culina · layers ×4 | d3940 | **Mother rows flagged d3970** |
| `CULINA-MINT-Y13` | Mint | Culina · crock ×2 | d3940 | **`MINT-CROCK-1` divide queued** |
| `CULINA-PARSLEY-Y13` | Parsley | Culina S band | d3940 | **×3 designated d3970 · `HERB-DES-PARSLEY-Y14-1…3` · Y14 seed cut** |
| `CULINA-ALLIUM-Y13` | Allium | Culina N edge | d3940 | **×4 designated d3970 · `HERB-DES-ALLIUM-Y13-1…4`** |

## Perennials · vine

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `P-03-CORDON` | Grape cordon | Bed B west trellis | d3368 | **Winter tidy d3827 · renewal tied** |
| `P-03-REGEN-Y12-1` | Grape regen lip | T-2 | d3578 | **Hold · pick replaces bank Aug–Oct** |

## Retting · fibre queue

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `P-RETT-33` | Hemp Bed A Y12 | — | d3770 | **✓ CLOSED d3786** |
| `P-RETT-32` | Flax field Y10 | — | d3487 | **✓ CLOSED d3505** |
| `P-RETT-34` | Flax field Y12 | — | d3852 | **✓ CLOSED d3865** — line @ crate · spin defer |
| **`P-RETT-35`** | Wild flax Y13 lap 1 | — | d4075 | **✓ PULLED d4088 · @ W-1 dry queue** |
| **`P-RETT-36`** | Hemp Bed A Y13 | — | d4111 | **@ W-1 north rafter · load defer** |
| **`P-RETT-37`** | Flax field Y13 | — | d4219 | **✓ PULLED d4228 · @ W-1 dry queue** |

**`RETT-TROUGH-FLAX-1`** empty @ ditch W · break/heckle defer.
