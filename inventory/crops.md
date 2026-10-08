# Crops

What is standing in the ground right now. Harvested stock moves to [food.md](food.md) or [resources.md](resources.md) and comes off this file.

`| ID | Crop | Where | Sown | State |`

`Sown` rather than `Made`, and it is a schedule input rather than a keep window — everything downstream is read against [calendar.md](../checklists/calendar.md). This is the one inventory file where the date tells you what to *do* rather than what is still good.

Y14 sow **d4307**. Bed geometry is [map](../map/index.md); what to select for is [crop-selection-improvement-code-1.md](../government/regulations/crop-selection-improvement-code-1.md).

## Bed A

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `HEMP-SEL-Y14` | Hemp · ★ **Ghab line gen 5** · fibre block | Bed A north | d4307 | **Sown · dense drill** |
| `HEMP-GHAB-RESERVE-Y14` | Hemp · seed/disaster block | Bed A north-west · **~6 m²** | d4307 | **Sown thin** · pegged **RESERVE** |
| `FAVA-Y14` | Fava · elite + working | Bed A west · **~8 m²** | d4307 | **Dibbed deep** |
| `P-18-CHICKPEA-Y14` | Chickpea | Bed A south · **~6 m²** | d4307 | **Row drill** |

☠ Hemp is an **obligate outcrosser** — isolate fibre vs seed blocks **by time** (fibre cut before seed block flowers). See `HEMP-CUT` in [harvest.md](../government/procedures/harvest.md).

## Bed B

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FLAX-FIELD-Y14` | Flax, field · fibre | Bed B centre · **~16 m²** | d4307 | **Dense drill** |
| `EMMER-Y14` | Emmer | Bed B south + centre · **~10 m²** | d4307 | **Broadcast · rolled** |
| `BARLEY-TRIAL-Y14` | Barley trial | Bed B east margin · **~2.5 m²** | d4307 | **Row drill** |
| `P-17-LENTIL-Y14` | Lentil | Bed B north + margin · **~6 m²** | d4307 | **Row drill** |
| `MADDER-BED-B` | Madder ×4 | Bed B west | — | Perennial · hands off |
| `GYPSUM-STRIP-TRIAL-2` | Gypsum strip trial · alternating blocks in lentil run | Bed B lentil run | d4307 | **Staked · in crop** |

## Bed C

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `SEED-INCREASE-BLOCK-Y14` | Emmer elite increase | Bed C south corner · **~3 m²** | d4307 | **Wide drill · RESERVE peg** |
| `PULSE-SELECTION-Y14` | Lentil thick stand · selection | Bed C SW · **~8 m²** | d4307 | **Thick drill** |

Bed C north is the goat pen — `GOAT-KIDDING-STALL-1` NE ~2.5 × 2 m, billie tie west. See [animals.md](animals.md).

## Bed D

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FIG-C1–C4` | Fig cluster | Bed D | — | Perennial · **✓ pass 1 d4098** |
| `WOAD-BED-D` | Woad | Bed D | — | Perennial · hands off |

## Culina margin

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `CULINA-HERBS-Y14` | Coriander · rosemary · thyme · mint · parsley · allium | Culina margin | d4307 | **Drilled / layered / divided** |

## Retting · fibre queue

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `P-RETT-33` | Hemp Bed A Y12 | — | d3770 | **✓ CLOSED d3786** |
| `P-RETT-32` | Flax field Y10 | — | d3487 | **✓ CLOSED d3505** |
| `P-RETT-34` | Flax field Y12 | — | d3852 | **✓ CLOSED d3865** — line @ crate · spin defer |
| **`P-RETT-35`** | Wild flax Y13 lap 1 | — | d4075 | **✓ FIBRE CLOSED d4236** |
| **`P-RETT-36`** | Hemp Bed A Y13 | — | d4111 | **✓ FIBRE CLOSED d4236** |
| **`P-RETT-37`** | Flax field Y13 | — | d4219 | **✓ FIBRE CLOSED d4236** |

**`RETT-TROUGH-FLAX-1`** empty @ ditch W · break/heckle defer.
