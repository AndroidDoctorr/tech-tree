# Crops

What is standing in the ground right now. Harvested stock moves to [food.md](food.md) or [resources.md](resources.md) and comes off this file.

`| ID | Crop | Where | Sown | State |`

`Sown` rather than `Made`, and it is a schedule input rather than a keep window — everything downstream is read against [calendar.md](../checklists/calendar.md). This is the one inventory file where the date tells you what to *do* rather than what is still good.

Y17 sow **d5405** · Y16 harvest **d5314–5317** · prior Y15 harvest **d4949–4952**. Bed geometry is [map](../map/index.md); what to select for is [crop-selection-improvement-code-1.md](../government/regulations/crop-selection-improvement-code-1.md).

## Bed A

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `HEMP-FIBRE-Y17` | Hemp · ★ **Ghab `P-22` import · fibre charge** | Bed A north · **~18 m² drill** | d5405 | **Dense drill · bird watch** |
| `HEMP-FLOWER-BREED-Y17` | Hemp · **flower breeding · `FLOWER-SEED`** | **`HEMP-FLOWER-BREED-1` headland NE · ~8 m²** | d5406 | **Thin drill · RESERVE peg** |
| `FAVA-Y17` | Fava · elite + working | Bed A west · **~8 m²** | d5405 | **Dibbed deep** |
| `P-18-CHICKPEA-Y17` | Chickpea | Bed A south · **~6 m²** | d5405 | **Row drill** |

☠ Hemp is an **obligate outcrosser** — isolate fibre vs flower breeding **by time** (fibre cut before flower bed sets) **and by bed** (**`HEMP-FIBRE-*` @ Bed A north** · **`HEMP-FLOWER-BREED-*` @ headland NE**). See `HEMP-CUT` in [harvest.md](../government/procedures/harvest.md) · [retcon](../journal/retcons/HEMP-FLOWER-BREED-BED-Y15-Y17.md).

## Bed B

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FLAX-FIELD-Y17` | Flax, field · fibre | Bed B centre · **~16 m²** | d5405 | **Dense drill · brushed** |
| `EMMER-Y17` | Emmer | Bed B south + centre · **~10 m²** | d5405 | **Broadcast · rolled** |
| `BARLEY-TRIAL-Y17` | Barley trial · **expanded** | Bed B east margin · **~7 m²** | d5405 · expand **d5406** | **Row drill** |
| `P-17-LENTIL-Y17` | Lentil | Bed B north + margin · **~6 m²** | d5405 | **Row drill** |
| `MADDER-BED-B` | Madder ×4 | Bed B west | — | Perennial · hands off |
| `GYPSUM-STRIP-TRIAL-2` | Gypsum strip trial · alternating blocks in lentil run | Bed B lentil run | d5405 | **Staked · in crop** |

## Bed C

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `SEED-INCREASE-BLOCK-Y17` | Emmer elite increase | Bed C south corner · **~3 m²** | d5405 | **Wide drill · RESERVE peg** |
| `PULSE-SELECTION-Y17` | Lentil thick stand · selection + regen | Bed C SW · **~8 m²** | d5405 | **Thick drill · disaster block** |

Bed C north is the goat pen — `GOAT-KIDDING-STALL-1` NE ~2.5 × 2 m, billie tie west. See [animals.md](animals.md).

## Bed D

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `FIG-C1–C4` | Fig cluster | Bed D | — | Perennial · **✓ Y15 tail d4875** · band close |
| `WOAD-BED-D` | Woad | Bed D | — | Perennial · hands off |

## Culina margin

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| `CULINA-HERBS-Y17` | Coriander · rosemary · thyme · mint · parsley · allium | Culina margin | d5405 | **Drilled / layered / divided** |

## Retting · fibre queue

| ID | Crop | Where | Sown | State |
|---|---|---|---|---|
| **`P-RETT-33`** | Hemp Bed A Y12 | — | d3770 | **✓ CLOSED d3786** |
| **`P-RETT-36`** | Hemp Bed A Y13 | — | d4111 | **✓ FIBRE CLOSED d4236** |
| **`P-RETT-40`** | Hemp Bed A Y16 | — | d5253 | **✓ FIBRE CLOSED d5265** · **`HEMP-THREAD-Y16-1` ✓ d5351** |
| **`P-RETT-41`** | Flax Bed B Y16 | — | d5317 | **✓ FIBRE CLOSED d5344** · **`FLAX-THREAD-Y16-1` ✓ d5350** |
