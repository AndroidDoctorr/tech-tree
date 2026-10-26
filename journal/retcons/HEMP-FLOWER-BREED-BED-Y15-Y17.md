# RETCON — Hemp flower breeding bed vs fibre block

**Filed:** d5406 · **player directive**

## What was wrong

Spring sow summaries through **d5405** listed hemp **flower** only as **Bed A north-west ~4 m²** inside the fibre footprint (`HEMP-FLOWER-Y*n*` · “QoL / RESERVE peg”). **Player intent (d4672)** was a **separate flower-focused breeding bed**, isolated from the fibre cut block — same **`HEMP-CUT` time grammar**, but **not** the same drill strip.

## Correct grammar *(default @ `SPRING-SOW` from CY15 onward)*

| Bed | ID | ~m² | Seed charge | Notes |
|---|---|---:|---|---|
| **Bed A north** | **`HEMP-FIBRE-Y*n*`** | **~18** | **`FIBRE-SEED` / dense drill** | **15 Aug-class rim cut** · Ghab `P-22` line |
| **Headland NE** | **`HEMP-FLOWER-BREED-Y*n*`** | **~8** | **`FLOWER-SEED` · thin drill** | **Breeding / dual-trait select** · **RESERVE** peg · no fibre cut |
| ~~Bed A NW corner~~ | — | — | — | **Retired** — do not lump flower into fibre block |

## Cross-pollination *(player directive d5407)*

- **Distance alone does not isolate hemp** — pollen is wind-borne for kilometres.
- **Operational isolate:** **`HEMP-CUT` on fibre bed before flower-breeding bed sets pollen** · separate **`FIBRE-SEED` / `FLOWER-SEED` jars** · hard rogue in flower bed.
- **Outside genetics:** periodic **tagged import** (Ghab / `P-22`) — not accidental cross from the fibre strip.
- **`HEMP-POTENCY-ASSAY`:** dry · grind · combustion smoke read — **R&D queue** · no calibrated potency ladder yet.

## Backfill

| Season | Sown | Bed |
|---|---|---|
| **Y15** | **d4676** class *(unlogged in hero table)* | **`HEMP-FLOWER-BREED-Y15` @ headland NE** |
| **Y16** | **d5040** class *(unlogged in hero table)* | **`HEMP-FLOWER-BREED-Y16` @ headland NE** |
| **Y17** | **d5405** fibre only · **d5406** flower bed planted | **`HEMP-FIBRE-Y17` @ A north** · **`HEMP-FLOWER-BREED-Y17` @ headland NE** |

**d5405 day file** — remove **A north-west flower charge** from the fibre table; fibre debit **~12 g** only.
