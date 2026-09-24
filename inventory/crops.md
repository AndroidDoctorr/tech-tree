# Crops

What is standing in the ground right now. Harvested stock moves to [food.md](food.md) or [resources.md](resources.md) and comes off this file.

`| ID | Crop | Where | Sown | State |`

`Sown` rather than `Made`, and it is a schedule input rather than a keep window — everything downstream is read against [calendar.md](../checklists/calendar.md). This is the one inventory file where the date tells you what to *do* rather than what is still good.

Y12 sow **d3576**. Bed geometry is [map](../map/index.md); what to select for is [crop-selection-improvement-code-1.md](../government/regulations/crop-selection-improvement-code-1.md).

## Bed A

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `HEMP-SEL-Y12` | Hemp · ★ **Ghab line gen 5** · fibre block | Bed A north · **~18 m²** | d3576 | **Sown dense** · **15 Aug cut grammar** |
| `HEMP-GHAB-RESERVE-Y12` | Hemp · seed/disaster block | Bed A north-west · **~6 m²** | d3576 | **Sown thin** · pegged **RESERVE** |
| `FAVA-Y12` | Fava | Bed A west · **~6 m²** | d3576 | **Dibbed** · nodule ground |
| `P-18-CHICKPEA-Y12` | Chickpea | Bed A south · **~6 m²** | d3576 | **Row drill** |

☠ Hemp is an **obligate outcrosser** — isolate fibre vs seed blocks **by time** (fibre cut before seed block flowers). See `HEMP-CUT` in [harvest.md](../government/procedures/harvest.md).

## Bed B

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FLAX-FIELD-Y12` | Flax, field · fibre | Bed B centre · **~16 m²** | d3576 | **Dense drill** · brush-covered |
| `EMMER-Y12` | Emmer | Bed B south + centre · **~10 m²** | d3576 | **Broadcast** |
| `P-17-LENTIL-Y12` | Lentil | Bed B north + margin · **~6 m²** | d3576 | **Row drill** |
| `MADDER-BED-B` | Madder ×4 | Bed B west | — | Perennial · hands off |
| `GYPSUM-STRIP-TRIAL-2` | Gypsum strip trial · alternating blocks in lentil run | Bed B lentil run | d3576 | **Staked** · weigh by block at harvest |

## Bed C

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `SEED-INCREASE-BLOCK-Y12` | Emmer elite increase | Bed C south corner · **~3 m²** | d3576 | **Wide drill** · pegged **RESERVE** |
| `PULSE-DISASTER-Y12` | Lentil + chickpea disaster/regen | Bed C SW · **~8 m²** | d3576 | **`SEED-REGEN` blocks** |
| `EMMER-Y5-RESCUE-Y12` | Emmer elite Y5 rescue | Dedicated block · **~4 m²** | d3576 | **Thick sow** · harvest-as-seed |

Bed C north is the goat pen — `GOAT-KIDDING-STALL-1` NE ~2.5 × 2 m, billie tie west. See [animals.md](animals.md).

## Bed D

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FIG-C1…C4` | Fig ×4 | Bed D | d3368 | Dormant crowns · **Aug pick band** |
| `WOAD-BED-D` | Woad, rosette | Bed D | Y9 | Crown intact · window to 18 Aug |

## Herbs

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `CULINA-HERB-BED` | Coriander · rosemary trace · parsley · allium | Culina herb bed | d3576 / d3580 | **Emerging band** |
| `HERB-LAYER-2` | ×4 rosemary · ×4 thyme re-pegged | Herb margin | d3576 | Layering · sever autumn |
| `MINT-CROCK-2` | Mint ×2 divisions | Culina bed | d3576 | Sunk crock |

## Perennials — vine and tree

| ID | Crop | Where | Planted | State |
|---|---|---|---|---|
| `P-03-TRELLIS` | Grape, cordon-trained | P-03 trellis @ T-2 | — | ✓ **`GRAPE-PRUNE-Y12-1` d3579** · cluster thin Mar–Apr |
| `P-03-REGEN-Y12-1` | Grape select regen · Y8 bank grow-out | T-2 north lip · ~2 m strip | d3578 | **Sown thick** · seed pick Aug–Oct |
| `P-03-CUT-Y12-1` | Grape hardwood cuttings ×4 | T-2 north lip sand-mulch | d3579 | Buried heel · spring strike read |
| `P-02-OLIVE` | Olive terrace | P-02 | — | Standing · Nov pick and press band |

## Wild patches

| ID | Stand | Where | State |
|---|---|---|---|
| `P-04` · `P-05-A/B` · `P-06-A/B/C` | Wild grain | — | Standing |
| `FLAX-PATCH-1` | Wild flax band | Ditch W · T-1 lip | Window to 26 Jul |
| `P-01` | Pistachio | T-2, ~160 m | Standing |
| `P-22` | Wild hemp | Ghab plain | Patch standing |
| `P-12` | Fig | 650 m | Standing |
| `PINE-TAP-CUPS` | Pine, ×8 cupped | Pine stand | Collect on pass |

## Retting

| ID | Load | Where | Loaded | State |
|---|---|---|---|---|
| `P-RETT-32` | Flax field Y10 | — | d3487 | ✓ **CLOSED d3505** |

**Pool empty** · bars reset · no submerged bundle.
