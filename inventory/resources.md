# Resources

Fungible stock — measured, drawn down, replaced. Schema and the routing test are in [index.md](index.md).

`| ID | Item | Qty | Where | Made | Last |`

`Made` is blank unless the thing degrades. `Last` is the day the quantity last changed. `×0` means the row is spent but the ID is kept so draws against it still resolve.

## Fuel and char

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CHAR-LANE` | Charcoal, oak · green | ~4.6 kg | Char lane | | d3441 |
| `CHAR-RESERVE-C` | Charcoal reserve | ~37 kg | Store C vault | | — |
| `WOOD-OAK-P5` | Oak, green | **~48.8 kg @ pile 5** · **~6.5 kg @ garage pad** | Pile 5 / pad | | d3439 |
| `SHIVE-FLAX` | Flax shive | ~8.1 kg | Storage wing | | d3401 |
| `SHIVE-HEMP-Y8` | Hemp shive | ~8.2 kg | Berm | | d3399 |
| `SLUMGUM-1` | Slumgum · firelighter | ~4 kg | Fire store | | d3265 |

## Clay, stone and aggregate

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CLAY-P1` | Clay, raw · green | ~13.2 kg | Pile 1 | | d3324 |
| `KAOLIN-M26-WET-1` | Kaolin, Koruhöyük **`M-26`** · wet | ×0 → slips | — | d3329 | d3331 |
| `QUARTZ-FACE-B` | Quartz, FACE-B | ~53.85 kg | `STORE-4` | | d3332 |
| `STONE-DRESS-P4` | Dressing / field stone | ~8.9 kg | Pile 4 north band, ×2 marked sacks | | d3073 |
| `RIPRAP-ARMOUR-1` | Riprap outer armour, angular — surplus after `CAMPUS-BRIDGE-APRON-1` · rounded cobble rejected, it rolls | surplus stack | T-2 face | | d3277 |
| `STONE-FLOOR-P8` | Floor stone | ×0 *(×8 laid in `PAD-1` ring)* | Pile 8 | | d3043 |
| `GRAVEL-1` | Gravel aggregate | ~19.2 kg | Pile 4 south band | | d3374 |
| `SAND-FILTER-1` | Filter / concrete sand · winter dry queue | ~22.2 kg | Pile 4 apron | | d3438 |
| `SAND-RIVER-GROG` | River sand / grog | ~2.1 kg | Fabrica SW margin | | d3438 |
| `POZZ-TUFF-1` | Pozzolan / tuff | ☠ **×0** — spent on the seventh block d3280 | Pile 4 north band | | d3280 |
| `POZZ-SLAB-TRIAL-1` | Pozzolan slab · reference | ~4.8 kg | Apron | | d1868 |
| `LIMESTONE-CHIP-TRAIL` | Limestone chip, trail assay | ~320 g | Pile 7 lip | | d2940 |
| `GHAB-STUB-SAMPLE` | Marl-limestone, Ghab stub sample | ~220 g | Pile 7 lip bag | | d2939 |
| `BITUMEN-BULK-1` | Bitumen · chem read PASS · ☠ **not food** | ~15.1 kg | `BITUMEN-POT-1`, cart yard | | d2943 |

## Lime

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CACO3-P7` | Limestone, raw · plus underburnt returns | ~19.6 kg | Pile 7, camp north face | d3374 | d3427 |
| `QUICKLIME-1` | Quicklime, dry · green · also `LIMELIGHT-1` feedstock | ~1.0 kg | Lime trough | d3390 | d3437 |
| `BLOCK-CAST-Y10-3280` | Cast block · BC-2 · 90-day break PASS d3370 | ×0 → **`WAGON-GARAGE-1` stem** | d3280 | d3375 |
| `LIME-PUTTY-1` | Lime putty | ~0.10 kg | Lime trough | | — |

Quicklime slakes on the air and is the one row here with a real clock — see the keep window in [processing.md](../government/procedures/processing.md).

## Clay bodies and slips

Washed slips are ranked, and the rank is the whole value of the row — a `#2-class bulk` and the `BEST` jar are not interchangeable even though both are kaolin.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `KAOLIN-SLIP-M26-1` | Kaolin slip · #2-class bulk — **`M-26` wash d3331** | ~12.1 kg | Chem porch jar | d3331 | d3332 |
| `KAOLIN-SLIP-M26-BEST-1` | Kaolin slip · best cut — **`M-26`** | ~0.15 kg | Chem porch jar | d3331 | d3332 |
| `MONT-M26-TRACE-1` | Montmorillonite trace · **`M-26` wash · field rank only** | ~0.35 kg wet | Chem porch separate peg | d3331 | d3331 |
| `KAOLIN-SLIP-4` | Kaolin slip · ★ **best** — CAND-4 wash | ~0.42 kg | Chem porch jar | | d3332 |
| `KAOLIN-SLIP-5` | Kaolin slip · #2-class bulk — CAND-4-EAST wash | ~10.07 kg | Chem porch jar | | d2591 |
| `KAOLIN-SLIP-2` | Kaolin slip · rank #2 · **lane primary** | ~2.0 kg | Chem porch jar | | d2830 |
| `KAOLIN-SLIP-1` | Kaolin slip · #2-class bulk — CAND-1 wash | ~1.4 kg | Chem porch jar | | d2580 |
| `KAOLIN-CAND-3S` | Kaolin candidate 3S · wet linen, secondary hold | ~2 kg | Chem porch dry queue | | d2527 |
| `MONT-CAND-1` | Montmorillonite candidate · unwashed, mont rank only | ~2.5 kg wet gross | Chem porch separate peg | | d2527 |

## Brick and tile

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BRICK-GREEN-P3` | Green brick | ×0 | Pile 3 | | d3110 |
| `BRICK-FIRED-B` | Fired brick, stackable · amber | ~205 | Kiln B | | d3324 |
| `TILE-TR` | TR tile, fired | ×76 *(+×19 laid Fabrica SW roof · ×3 to grog)* | Rack south | | d3049 |
| `TILE-FT` | FT tile | ×0 *(×108 laid, hub floor)* | Rack | | d2224 |
| `CLAY-RANK-REF` | Refractory rank tiles · fired reference set | ×6 | Bench | | d2447 |
| `CRUCIBLE-GROG` | Crucible grog, reclaim | ×0 | Berm | | d2504 |
| `FT-Y8-FLOOR-TILE` | FT-Y8 floor tile, fired PASS · ⚠ FT-Y8-4 and FT-Y8-12 marginal | ×25 *(−×16 laid, culina backsplash checker)* | Bench stack | | d2723 |
| `PORCELAIN-CHIP-SET-1` | Porcelain chip reference set · stoneware rank | ×10 | `CRAFT-CABINET-2` archive drawer | | d3073 |
| `PORC-M26-TRIAL-TILES-1` | **`M-26` body trial witness tiles ×3** · ◐ **high stoneware, not porcelain** | ×3 | Craft archive tray | d3332 | d3332 |

## Ore

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `O-1-MALACHITE` | Malachite, Y10 · *(+~0.48 kg tail at slag dish)* | ~17.55 kg | Pile 4 | | d3230 |
| `CINNABAR-1` | Cinnabar, HgS · ☠ **isolated storage** | ~34.75 kg | v1 chem, isolated | | d3008 |
| `GALENA-1` | Galena-class lead ore | ~12.2 kg | Forge staging | | — |
| `H-11-HEMATITE` | Hematite | ~8.85 kg | — | | d3108 |
| `SPH-1` | Sphalerite | ~6.12 kg | — | | d2987 |
| `AZURITE-1` | Azurite · smelts as copper **or** grinds as blue pigment | ~1.36 kg | Chem porch | | d3258 |
| `CU-SLAG-Y10` | Copper slag · re-charge stock, still holds metal | ~3.8 kg | Slag dish | | d3230 |
| `CASSITERITE-CONC` | Cassiterite concentrate · fines-heavy, deferred | ~0.5 kg | Forge staging tray | | d2933 |
| `PYRITE-KISECIK` | Pyrite, Kisecik fringe · *(+`PYRITE-SPARK-TIN-1` ~22 g at `FK-1`)* | ~0.38 kg | Ore shelf | | d3127 |
| `M-22-MAGNETITE` | Magnetite · ⚠ amber, low | ~0.38 kg | `FORGE-ORE-TRAY-1` staging | | d3161 |
| `NICKEL-LATERITE-TRACE-M24-1` | Red laterite dirt · **`M-24` scout** · surface | ~1.18 kg | Chem porch dry queue | d3338 | d3344 |
| `GARNIERITE-CHIP-M24-1` | Garnierite trace · fracture chip | ~80 g | Chem porch dry queue | d3338 | d3341 |
| `CHROMITE-POD-M24-1` | Chromite pod fragment · podiform | ~190 g | Chem porch dry queue | d3338 | d3344 |
| `NICKEL-LATERITE-TRACE-M24-2` | Red laterite dirt · gully **`M-24` pass 2** | ~980 g | Chem porch dry queue | d3339 | d3344 |
| `GARNIERITE-CHIP-M24-2` | Garnierite · north fracture · pass 2 | ~95 g | Chem porch dry queue | d3339 | d3347 |
| `GARNIERITE-BULK-M24-1` | Garnierite · **ribbon haul `M24-2`** · fracture chips | ~31 kg | Forge ore staging | d3350 | d3352 |
| `GARNIERITE-CHIP-M24-3` | Garnierite · **east bench crack** · prospect | ~73 g | Chem porch dry queue | d3350 | d3353 |
| `NICKEL-LATERITE-TRACE-M24-3` | Red laterite · gully lip · pass 3 | ~450 g | Chem porch dry queue | d3351 | d3351 |
| `NICKEL-HYPERACCUM-ASH-M24-1` | Ni-indicator plant ash · burned | ~16 g | Chem porch sealed shelf | d3339 | d3344 |
| `CU-NI-TRIAL-M24-A` | Cu–Ni trial button · **`M24-1` dirt** · weak drift | ~5 g | Bridge trial tray | d3344 | d3344 |
| `CU-NI-TRIAL-M24-B` | Cu–Ni trial button · **`M24-2` dirt** · ◐ drift | ~6 g | Bridge trial tray | d3344 | d3344 |
| `CU-NI-TRIAL-M24-C` | Cu–Ni trial button · **`GARNIERITE-M24-2`** · ✓ best drift | ~7 g | Bridge trial tray | d3344 | d3344 |
| `CU-NI-TRIAL-M24-D` | Cu–Ni trial button · **`GARNIERITE-M24-3`** · ◐ ≈ `C` | ~6 g | Bridge trial tray | d3353 | d3353 |
| `CACHE-MG1-1` | Ore, dressed and cairned **at the face** — head start on the next run | ~15 kg | MG-1 face | | d3227 |
| `KOZAN-CHAR-BANK` | Charcoal, Kozan · red | ~0.3 kg | Kiln lee | | — |

## Metal

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CU-BAR-Y10-1` | Copper bar · **poled, wire-grade** — ~58 m left in it at 0.9 mm | ~328 g | — | | d3431 |
| `IRON-BLOOM-1` | Iron bloom, mounted · green | ~190 g | — | | d3377 |
| `SN-BANK` | Tin | ~1.14 kg | — | | d3166 |
| `ZNO-CALCINE` | Zinc oxide calcine | ~836 g | — | | d3431 |
| `ZN-METAL-1` | Zinc, prill tail | ~81 g | Chem-lab lidded tray | | d2979 |
| `HG-METAL-1` | Mercury · ☠ **not food** · isolated | ~118 g | Purple lidded jar, v1 chem | | d3013 |
| `BRONZE-STOCK` | Bronze, sprue tail · red | ~75 g | Chill tray | | d3064 |
| `PB-METAL` | Lead, tail · red · galena restock queued | ~15 g | Forge jar | | d3202 |
| `BRASS-STOCK` | Brass stock · **`SUNGLASS-FRAME-WIRE-Y10` ~28 m @ peg** | ~42 g class @ tray | Chill tray | | d3435 |
| `NAIL-BRASS` | Brass nails | ×4 | `WOOD-CRATE-5` forge fastener | | d3103 |
| `NAIL-IRON` | Iron nails | ×8 | Bench peg tray | d3379 | d3379 |
| `WAGON-GARAGE-STRAP-1` | Iron strap, pierced · garage tie | ×0 → frame | `WAGON-GARAGE-1` | d3377 | d3378 |
| `HINGE-BRASS-REPAIR` | Brass strap hinges, repair pool | ×2 | Horreum peg tray | | d3081 |
| `WOOD-SCREW-STOCK-1` | Wood screws · marginal | ×2 | Bench tray | | d3087 |

## Copper wire

The wire bank is tracked by **gauge**, because gauge is what decides whether a length is usable for a given job — 0.3 mm will not carry a cell and 1.6 mm will not wind an armature.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CU-WIRE-Y10-3` | 0.3 mm · electrowon, tough-pitch, poled — **drew without a break** | ~72 m | — | d3261 | d3261 |
| `WIRE-CU-GEN2-1` | 0.9 mm gen-2 | ~48.65 m | Chem peg | | d3171 |
| `WIRE-CU-4` | 1.6 mm · lane B coil, hold | ~14 m | Chem porch | | d1982 |
| `CU-WIRE-Y10-COATED` | 0.9 mm coated · leads and tails only | ~9 m | — | d3245 | d3267 |
| `CU-WIRE-Y10-4` | ★ **best conductivity drawn to date** — off the glass-cover melt | — | Wire rack | d3266 | d3266 |
| `WIRE-DRY-1` | 0.75 mm legacy · untouched since d1979 | ~2.6 m | Chem cabinet | | d1979 |
| `COIL-BOBBIN-1` | Gen-2 tail scrap | ~2 m | Shell | | d3158 |
| `CU-CATHODE-DIRTY-1` | Cathode copper, spongy and iron-fouled · **re-melt stock, not wire-grade** | ~2 g | — | | d3229 |

⚠ The armature's 95 m was unwound and redrawn to 0.65 mm at d3267 — it is now `ARMATURE-2` in [infrastructure.md](infrastructure.md), not wire stock.

## Electrical plate and magnet stock

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ZN-VOLTAIC-PLATES` | Zinc voltaic plates, spare · `VOLTAIC-RESERVE` | ~39 | Storage wing | | d3238 |
| `CU-GEN2-VOLTAIC-PLATES-1` | Copper voltaic plates, spare *(+×8 live in `VOLTAIC-8-CELL-1`, ×1 in `DANIELL-CELL-1`)* | ×20 | Tray | | d3238 |
| `MAG-BOOT-EM` | EM boot rods #9 · #10 · #11 · #13 · #14 · #15 · #17 · #18 — ~168–176 g, ~35–38 mm | ×8 | Dry tray | | d3160 |
| `MAG-BOOT-SPARE-1…4` | Demoted rods, ~27–36 mm solo class | ×4 | Horreum B peg | | d3162 |

Rods #16 and #19 are in `MAG-STACK-2` and #6 rods are in `GEN-WW-1`'s yoke — both in [infrastructure.md](infrastructure.md).

## Glass and chemical

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `GP-Y8-C-LITE` | Glass pane, C-lite · spare, dividered | ×20 | Storage wing N upper shelf | | d3073 |
| `KELP-ASH-5` | Soda / kelp ash · green | ~225 g | v1 chem | | d3430 |
| `GLASS-TINT-LENS-Y10-D` | Tint lens spare | **`SUNGLASS-LENS-Y10-3` annealed · unlapped** | Spare peg | d3430 | d3435 |
| `PAPER-SHEET-Y9` | Paper, flax · `SHEET-Y9-FLAX-29…32` · coil interleaving stock | ~13 sheets | Chem-lab rack | | d3232 |

## Fibre, cordage and hide

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FLAX-LINE-BANK` | Flax line | ×0 | — | | d3401 |
| `FLAX-TOW-BANK` | Flax tow | ~65 g | Wing shelf | | d3401 |
| `FLAX-THREAD-COVER-Y10-1` | Flax thread · wagon cover inner | ~55 m tail | Craft wing peg | d3401 | d3406 |
| `FLAX-THREAD-BANK` | Flax thread | ~13 m | Craft cabinet 2 | | d2565 |
| `HEMP-LINE-26` | Hemp line | ~10 g tail | `WOOD-CRATE-6` fibre | | d3384 |
| `P-HEMP-LINE-GHAB-Y10-1` | Hemp line · **`P-RETT-30` lap** | ×0 | — | d3383 | d3384 |
| `HEMP-THREAD-Y10-1` | Hemp thread · cover weft | ~75 m | Craft wing peg | d3382 | d3400 |
| `WAGON-V2-COVER-HEMP-FLAX-1` | Wagon cover · hemp shell + flax liner · air gap · **outer oilcloth d3408** · mounted Norima | ✓ CLOSED d3407 | `WAGON-V2-COVER-ARCH-1` | d3400 | d3408 |
| `HEMP-TOW-BANK` | Hemp tow | ~313 g | Storage wing tow bag | | d3399 |
| `HEMP-GREEN-GHAB-Y10-1` | Hemp stalk, green · **`P-22` wild · fibre haul** | ×0 → **`P-RETT-30`** | — | d3363 | d3365 |
| `ROPE-HEMP-STOCK-2` | Hemp rope · reserve / lash · **cover weave band** | ~35 m | WW peg | | d3407 |
| `ROPE-HEMP-HOME` | Hemp rope · good lay, **reserve for load work** | ~6.4 m | Pile 2 | d3221 | d3221 |
| `ROPE-HEMP-Y10` | Hemp rope · ⚠ **lash class only** — uneven lay, soft spots, never under load | ~28 m | Pile 2 | d3226 | d3226 |
| `ROPE-1` | 3-strand hemp · ⚠ **lashing grade only** — uneven lay | ~24 m | — | d3255 | d3255 |
| `ROPE-2` | 3-strand hemp · ★ **certified: loaded haul and lashing at breaking ÷ 6, spliced not knotted** · ⚠ **not life-bearing** | ~23 m | — | d3255 | d3264 |
| `ANTLER-SHED` | Antler, cast and hard · beats bone for anything taking a blow | ×6 | Craft wing | | d3269 |
| `CLOTH-WAGON-COVER` | Wagon cover cloth, tail stock | ~2.08 kg | `CART-YARD` south peg row | | d3092 |
| `THREAD-STOCK-2` | Thread · *coil serving — leads and crossovers only* | ~527 m | Craft wing peg | | d3232 |
| `THREAD-1` | Thread, general | ~307 m | — | | d3091 |
| `VENT-BELT-ROPE` | Rope, vent belt | ~123 m | — | | d1970 |
| `EXPED-ROPE` | Hemp rope · D-27 salvage | ~72 m | Cart peg | | d2945 |
| `FLAX-SHIVE-Y8-21` | Flax shive · **paper grade** | ~2.01 kg | Storage wing | Y8 | d3189 |
| `FEATHER-BAG` | Feather, bag | ~31 g | — | | d2470 |
| `LAB-LINEN-STOCK-1` | Lab linen — filters ×10 · jar wraps ×4 · voltaic separators ×24 · wipes ×9 · spill reserve ×4 | — | `CHEM-SPILL-PEG-1` | | d3054 |
| `P-FLAX-LINE-Y8-1` | Flax line, Y8 · `P-RETT-23` break/heckle | ~1.03 kg | WW peg | Y8 | d3135 |

## Hide, leather and bone

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `DEER-HIDE-1` | Deer hide, **tanned** | ~0.52 m² | Horreum B `LEATHER-STOCK-PEG-1` | | d3436 |
| `GOAT-HIDE-A03-2` | Goat hide, reserve · flap tail | ~0.09 m² | Horreum B | | d3169 |
| `HIDE-SCRAP` | Hide scrap, tail | ~0.14 m² | — | | d3436 |
| `WEATHER-STRIP-LEATHER-1` | Weather strip, ~25 mm | ~4.6 m | — | | d3167 |
| `MACHINE-BELT-LEATHER-KIT-1` | Machine belt stock — WW · drill · trip tail | — | `BELT` peg | | d3052 |
| `TRAIL-GEAR-LEATHER-1` | Belt v2 blank · waterskin patch · lash tabs ×4 | — | Vestiarium trail peg | | d2964 |
| `DEER-BONES` | Deer bone · bone-ash feedstock | ×0 — *burnt d3309* | Horreum tool peg | | d3309 |
| `GOAT-BONES` | Goat bone · bone-ash feedstock | ×0 — *burnt d3309* | Horreum tool peg | | d3309 |
| ✓ `BONE-ASH-1` | **Bone ash, white, calcined** · ★ **~40 cupels · ~2 passes through `GALENA-1`** | ~6.1 kg | Chem porch | d3309 | d3311 |

> ☠ ★★★ **THE MIDDEN DOES NOT GIVE IT BACK** *(d3309)*. *Nine years of it forked over for ~2.8 kg of usable fragment — weathered soft, gnawed, trodden into the ash, the small bones gone entirely.* ★★★ **It is not lost the way a mislaid tool is lost. It is GONE.** ★★ *The other half of d3303: the clocks ran while I was not reading them, and they do not run backwards.*

> ★★★ **`OXIDISING-COOL` — CALCINE ON THE COOLDOWN, NEVER ON THE CLIMB** *(d3309)*. ☠ **A stoked kiln is REDUCING, and carbon in a cupel reduces litharge straight back to lead** — *the exact reaction the hearth exists to run the other way.* ★★★ **Stop stoking, damper wide, trays shallow and high in the chamber: a kiln at ~800 °C full of moving air is a free oxidising furnace** — ☠ **and I threw those hours away after every firing for nine years.** ✓ *The soak burns midden charcoal out as a side effect.* ★ **Bone ash must be WHITE — grey means carbon, and carbon means no silver.**

> ☠ ★★★ **`BONE-BANK-1` opened d3297 — bone is the rate limit on SILVER, not the hearth.** *A cupel is a reagent consumed every run; ~4.7 kg of bone is ~3 kg of ash is ~20 cupels is ONE pass through `GALENA-1`.* ⚑ **Retain every bone from every butchery and every kitchen pot, dried, on the Horreum peg** — ☠ *nine years of it went on the midden.*
> ✓ ★★ **Used cupels are BANKED ORE, not waste** — *lead-soaked, richer than anything dug.* **They go in the kerbed galena bay at `ORE-BAY-1`.**
| `GOAT-HORN-BILLIE` | Goat horn, remnant | ~65 g | `WORKBENCH` peg | | d3015 |
| `SINEW-DRY` | Sinew, dry | ~32 g | Bench | | d3090 |

### `TAN-DEER-Y10-1` — in the pit

In the **weak** oak-bark pit since d3254. Weeks to run, liquor ladder logged, **weak to strong**.

☠ **Strong liquor on a raw hide case-hardens it.** Tannin seals the surface, the middle never tans, and the hide rots from the inside where it cannot be seen. The ladder is the procedure, not a refinement of it.

Destined for **belt leather** — butt cut, along the backbone, tallow-stuffed, pre-stretched.

Rope is here rather than in tools because it is measured and consumed. A rope rigged into a fixed installation belongs to that installation's entry — `CAVE-3-FIXED-LINE-1` is in [infrastructure.md](infrastructure.md), not this table.

★★ **Grade is the row, not a note.** A length of rope at lashing grade and a length certified for loaded haul are different materials that happen to look identical, so the grade rides in the item name where a grep cannot miss it. `ROPE-2` carries its first real working load on the record — ~130 kg of basalt over 14 km, clean. Working load is **breaking ÷ 6**, a knot costs another third, and shock multiplies enormously. The measured breaking load came from deliberately destroying a length and is written up as doctrine, not held as stock.

## Stone working

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BASALT-BLOCK-1/2/3` | Dyke basalt, fine-grained chilled-margin, Kisecik ophiolite · **all three ring sound** · cut generously oversize | ~130 kg rough | `WW-YARD` | d3264 | d3264 |
| `LAP-GRIT-1/2/3/4` | Lapping grit, four settled grades coarse → very fine · labelled crocks | ×4 crocks | — | d3264 | d3264 |

⚠ **The basalt is rough now and must season through summer on three points, to be lapped in autumn.** **`BASALT-DATUM` turn d3342 — still settling; first datum d3268.**

Grits were graded by elutriation, so the settling times are **arbitrary but identical every batch**: repeatable rather than known. Wash between grades.

## Pigment, dye and reagent

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `MADDER-ROOT-DRY` | Madder root, dry | ~238 g | Chem shelf | | d3116 |
| `WOAD-RESERVE` | Woad, dry | ~385 g | Storage wing dye shelf | | d3351 |
| `WOAD-LEAF-Y10-1` | Woad leaves, fresh · **window pull 1** | ×0 spent | — | d3345 | d3351 |
| `MADDER-DRY-V1` | Madder, dry | ~79 g | v1 chem | | — |
| `PRUSSIAN-BLUE-1` | Prussian blue pigment · ☠ **not food** | ~24 g | Craft cabinet 2 pigment shelf | | d3021 |
| `GREEN-VITRIOL` | Green vitriol crystals · tail | ~17 g | Reagent shelf | | d3020 |

Madder needs an alum mordant. Woad does not — it is a vat dye and fixes mechanically. See `WOAD-VAT` in [processing.md](../government/procedures/processing.md).

## Mineral and salt

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `M-14-SULFUR` | Sulfur · ~15.6 kg block plus ~116 g flour | ~15.7 kg | — | | d2911 |
| `M-11-ALUM` | Alum, crude | ~1.39 kg | — | | d3101 |
| `M-12-NITER` | Niter crystal | ~495 g | Dry jar | d3424 | d3424 |
| `BITTER-SALT-1` | Epsom-class bitter salt · identity narrowed | ~5 g | Chem porch | | d3223 |
| `QUARTZ-FRIT` | Quartz frit | ~40 g | Vial `G-FRIT` | | d3332 |

`BITTER-SALT-1` is the sulfate of an earth that is **not lime** — lime water precipitates it, hepar confirms sulfate, and a clean hydrogen flame rules out soda.

## Gypsum and plaster

The Samandağ face turned a one-off haul into a bank. Grades are not interchangeable and the row names say which is which.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| ✓ ★★★ `ACID-VITRIOL-1` | **OIL OF VITRIOL, strong** · ★★ **~1.8× the weight of water** · ⚠ **chars on contact** | small bottle | `ACID-BOTTLE-1`, grooved glass stopper · chem porch | d3317 | d3317 |
| `ACID-VITRIOL-2` | Oil of vitriol, strong · batch 2 · `RETORT-B` compare run | small bottle | Spare narrow-neck + grooved stopper · chem porch | d3335 | d3335 |
| `VITRIOL-FEED-CROCK-1` | Copperas feed · Kisecik-class green · calcined as needed | ~4.2 kg | Chem porch feed crock | d3317 | d3335 |
| `COLCOTHAR-2` | Raw red ferric residue · `RETORT-B` batch 1 | small dish | Chem porch · unwashed | d3335 | d3335 |
| `COLCOTHAR-1` | Raw red ferric-oxide residue · ✓ **washed and levigated d3318** | ×0 → `ROUGE-FINE-1` + `IRON-OXIDE-PIGMENT-1` | — | d3317 | d3318 |
| ✓ ★★★ `ROUGE-FINE-1` | **Washed, levigated hematite finishing polish** · ★★ **clears final glass haze; does not remove deeper scratches** | small crock | Lap bench | d3318 | d3318 |
| ✓ `IRON-OXIDE-PIGMENT-1` | Clean red hematite, coarser early-settling fraction · **pigment, not trusted on finished glass** | small crock | Pigment shelf | d3318 | d3318 |
| `GYPSUM-CLEAN-POWDER-1` | Gypsum, clean powder · **raw stone — burn small batches on demand** | ~24 kg | Chem porch dry store | | d3225 |
| `GYPSUM-FIELD-GRADE-1` | Gypsum, field grade · gritty · strip-trial stock | ~15.4 kg | Pile 7 | | d3225 |
| `GYP-STOCK-1` | Gypsum, raw · `SC-GYP-SAMANDAG-1` face open | ~14.2 kg | Chem porch peg | | d2823 |
| `GYPSUM-RESIDUE-1` | Gypsum, confirmed — thumbnail-soft, no vinegar fizz, gritty | ~2.1 kg | Chem porch | | d3223 |
| `PLASTER-CALCINED-1` | Plaster, calcined · ⚠ **stales in damp air — use it** | ~1.85 kg | Working stock | d3225 | d3230 |
| `SELENITE-1` | Selenite, clear sheets, wrapped · ⚠ **fragile** · pane and lantern glazing | ×13 | — | | d3225 |
| `PLASTER-TEST-1` | Plaster proof slab | ~120 g | — | d3223 | d3223 |
| `PLASTER-WALL-SWATCH-1` | Wall swatch · set hard, burnished | ~0.24 m² | Craft wing | d3225 | d3225 |


★★★ **The cooldown is not a temperature — it is a DESCENT THROUGH ALL OF THEM** *(d3311)*. Bone calcines early at ~800 with the damper wide; gypsum burns late at ~150–200 on the same descent. ✓ **Anything below the kiln's peak can be made on the way down if it is charged at the right hour, for no fuel at all.**

★★ **Calcined plaster is the only row in this file with a short fuse.** It stales in damp air, so it is burnt in small batches on demand from `GYPSUM-CLEAN-POWDER-1` rather than stockpiled. Twenty-four kilos of raw powder is a bank; 1.85 kg of calcined is a deadline.

⚠ **Roast gently. Over-roast is dead** — it will not re-set at all. A correctly roasted slab re-wets and goes hard in minutes, which is what `PLASTER-TEST-1` exists to prove.

The first wall swatch **failed on a dry wall** — the substrate drank the water before the plaster could set. Wet the wall. Gauging with whey doubles working time to ~25 min ([food.md](food.md)).

`SELENITE-DESK-1`, `AZURITE-MUS-1`, `MALACHITE-MUS-1` and `PLASTER-TEST-1` are **museum-reserved and not available to consume** — [museum.md](museum.md).

## Powder

☠ `SAFETY` class. Stored apart and low, per [storage-code-1.md](../government/regulations/storage-code-1.md).

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BLAST-CAP` | Blast caps | ×4 | HOME powder safe | | d3030 |
| `CHARCOAL-FLOUR` | Charcoal flour · one batch thin | ~17 g | Powder jar | | d2911 |
| `GUNPOWDER-MEALED` | Mealed gunpowder · tail | ~3 g | Chem-lab lidded tray | | d2912 |

## Resin, wax and sealant

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BITUMEN-ASI-1` | Bitumen, Asi seeps · 4 crocks, sand-dusted · ⚠ heavy end only | ~40 kg | Chem porch | d3270 | d3270 |
| `BITUMEN-BULK-1` | Bitumen · *(+~1.5 kg chip at cart trial tin)* · ☠ not food | ~9.7 kg | `BITUMEN-POT-1`, cart yard | | d3209 |
| `CORK-BARK` | Cork bark | ~1.02 kg | — | | d3171 |
| `BEESWAX-V1` | Beeswax · *(plus ~1.04 kg at the wax store — see below)* | ~238 g | v1 chem · craft cabinet 2 | | d3274 |
| `TALLOW-1` | Tallow | ~78 g | v1 trough jar | | d3203 |
| `WAX-DROSS-1` | Slumgum / wax dross · fire starter | ~45 g | Hearth | | d3234 |
| `ROSIN-1` | Rosin · pale, brittle | ~29 g | Chem porch | | d3237 |
| `WAX-ROSIN-COMPOUND-2` | Wire-coating compound · ⚠ **low** | ~25 g | Melt pot | | d3245 |
| `TURPENTINE-1` | Turpentine · ☠ **flammable — cool, away from fire** | ~17 ml | Stoppered glass, chem rack | d3237 | d3237 |

Rosin dissolved in turpentine is a cold brushable varnish, and turpentine is the linseed-varnish thinner. `PINE-TAP-CUPS` — ×8 trees scored and cupped at the pine stand — are a standing resource and live in [crops.md](crops.md); collect on the pass.

★ **`BITUMEN-ASI-1` clears the damp-proof course gate for the August plaster.** ~40 kg from three staked seeps on the Asi margin bench, ~6 km out.

## Acid

☠ Every row here is a `SAFETY`-class handling item. PPE, fume hood and rehearsed spill response are prerequisites, not precautions — `CHEM-SPILL-KIT-1` and `CHEM-SPILL-PEG-1`.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `HYDROCHLORIC-ACID-1` | Muriatic acid · cassiterite wash green | ~40 ml | `P-LAB-ACID-BOTTLE-1` | d2961 | d2961 |
| `NITRIC-ACID-1` | Aqua fortis, batch 1 | ~34 ml | `P-LAB-ACID-BOTTLE-4` | d2793 | d2793 |
| `STRONG-ACID-BANK` | Sulphuric acid · ⚠ **low** — ~4 ml of it is live in the kept cell | ~4.3 ml | Bottles 2 · 3 · 5 · 6 | | d3238 |

⚠ **The sulphuric bank is off by about a thousandfold for its intended job.** A bulk leach needs kilograms; there are four millilitres, most of which is committed to `DANIELL-CELL-1`. Treat the bank as a reagent supply, not a process input, until there is a lead-chamber or contact route.

## Wax

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `WAX-Y10-RENDER-1` | Beeswax, clean cake — ~850 g `SKEP-1` + ~190 g `SKEP-2` | ~0.62 kg | Wax store | | d3408 |
| `COMB-TO-RENDER` | Comb awaiting render · the two torn on the cut-out, plus `SKEP-2`'s | ~90 g | Wax queue | | d3265 |

Y10's binding constraint, closed. Yield per kg of comb is low because old brood comb is mostly cocoon and propolis — honey comb off top bars is the rich fraction. See [bees.md](../government/procedures/bees.md).

## Routed elsewhere

Rows that sat in the v1 sections ported so far but are not resources. Recorded so the port is auditable and nothing is silently dropped.

| Went to | Rows |
|---|---|
| [vehicles.md](vehicles.md) | `COVERED-WAGON-1` · `Norima` · all `WAGON-*` fittings |
| [tools.md](tools.md) | All `P-LAB-*` · `THERMOMETER-1/2` · `GLASS-TUBE-*` · `GLASS-CUP-1…4` · `GLASS-BOTTLE-*` · `CULINA-*` · `GLASS-MOLD-KIT-1` · `MARVER-FLAT-PLATE-1` · `LAB-STAND-1-A/B/C` · `GLASS-PLIERS-1` · `HELICAL-MANDREL-1` · `PORC-BOWL-1…4` · `PORC-PLATE-1/2` · `PORC-VASE-Y8-1` · `PORC-PROBE-SET-1` · `DRY-TRAY-1/2` |
| [infrastructure.md](infrastructure.md) | `NITRE-BED-1` · `URINE-CROCK-1` · `CHAR-RETORT-1/2` · `ANNEAL-SAND-BATH-1` · `KILN-D-PLENUM-1` · `COLD-CELLAR-FAN-1` · `ICE-VAULT-NICHE-2` · `WW-2-BELT-COLLAR-4` · `SLUICE-2-*` · `AMPHORA-5…10` · `NUT-SHELF-EXT-1` · `CHEM-SLIP-SHELF-1` · `WORK-TABLE-*` · `CAVE-3-FIXED-LINE-1` · `HIVE-SCALE-1` · `SCARECROW-1` · `BIRD-RATTLE-LINE-1` · `HAWK-KITE-1` · `POT-WHEEL-2` · `PORC-BASIN-1` · `CULINA-FAUCET-BRASS-1` · `ACORN-LEACH-TROUGH-1/2` · `EVAP-RACK-1` · `VOLTAIC-*` · `BITUMEN-POT-1` · `P-μ-*` · `P-ξ-*` |
| [animals.md](animals.md) | `TOP-BAR-HIVE-3…7` · `SKEP-1/2` · `SPARE-HIVE-1` · `TOP-BAR-SET-SPARE` |
| [food.md](food.md) | Honey · smoked meat and fish · stew jars · oil · vinegar · brined olives · salt · ice · grain and pulse eating stock |
| [seed-vault.md](seed-vault.md) | All elite and select banks · `EMMER-SOW-Y9` · `P-FAVA-Y9` · `HEMP-SEL-Y10` · herb reserves |
| [processing.md](../government/procedures/processing.md) | `MELT-PROTOCOL-2` — a method, never stock |
| [now.md](../now.md) | `BAIT-BOX` **not built** — a task, not an item |

**Dropped, not lost.** Closed batches and spent kits — `ACORN-LEACH-Y6-1` through `Y8-6`, `TRAIL-GRAVEL-KIT-1/4/7`, `KAOLIN-CAND-1/2/4-EAST`, `PORCELAIN-BODY-MIX-3/4/5`, `FELDSPAR-CHIP-SET-1`, `KELP-DRY-STAGING`, `CU-WIRE-STOCK-1`, `WIRE-CU-3`, `EM-COIL-2`, the Y6–Y9 bread bakes, and the d2818–d2830 construction read rows — are journal records, not stock. See the retirement rule in [index.md](index.md).

## ⚠ Doctrine rows — these are not inventory

The v1 §Metals section had accumulated a second kind of row entirely: **things learned**, filed as though they were things owned. They have no quantity and no location, and they are the most valuable content in the file, which is exactly why they should not be sitting in a stock table where a grep for a material will never surface them.

| Row | Belongs in | Claim |
|---|---|---|
| `WAX-MOTH-DOCTRINE-1` | [bees.md](../government/procedures/bees.md) | Larvae eat **cocoons, not wax** — they take dark brood comb and ignore pale. Render a driven skep at last brood hatch, **not on a date**; store comb in light and draft. Cost of learning: ~500 g at `SKEP-2` |
| `INBREEDING-METER` | [bees.md](../government/procedures/bees.md) | Excess brood loss **doubled** = share of the queen's mates that were kin. `HIVE-6` d3275: 412 eggs → 351 sealed, ~15% loss → ~1 in 5. Run on one hive each spring; keep a queen at 15%, replace one near 50% |
| `PEMMICAN-DOCTRINE-1` | [food-menu.md](../government/procedures/food-menu.md) | Dry lean hard → pound → work rendered fat back in **at the end**. A pack is measured in fat / protein / starch, not kilograms |
| `NICKEL-TARGET-1` | [resources.md](../map/region/resources.md) *(map)* | ☠ **Not pentlandite** — wrong target for an ophiolite. The ore is the **red-brown dirt on top of weathered serpentinite**, found by vegetation: a sparse, stunted, bald patch on a green hillside. Garnierite is apple-green and waxy in the fractures — ☠ *and the bald patch alone is a precondition, not a deposit: Kisecik passed the vegetation test and carries no nickel at all.* Burn hyperaccumulator plants and assay the ash. ★ Reduce **in contact with copper** → constantan direct; nickel metal was never needed |
| `ROPE-STRENGTH-TABLE-1` | [processing.md](../government/procedures/processing.md) | Working load = breaking ÷ 6 · a knot costs another third · shock multiplies enormously. Measured by deliberately destroying a length |
| `RESISTIVITY-TABLE-1` | [processing.md](../government/procedures/processing.md) | Cu · Pb · Fe · brass · bronze, in own units. ★ **Alloys conduct worse than both parents** |
| `CU-ASSAY-1/2/3` | journal | d3262 controlled: electrowon copper conducts **~11% better** than smelted. The drawing hid 3 points and the melt cost 4. `CU-ASSAY-2` superseded — its uncontrolled 4% was wrong, not merely vague |
| `MELT-PROTOCOL-2` | [processing.md](../government/procedures/processing.md) | Glass on the metal, charcoal on the glass. Tax ~4% → ~1.3%. ⚠ Palest iron-free glass only |
| `BASALT-DATUM-1` | [periodic.md](../checklists/periodic.md) | Three-point support · turn and re-check every ~3 weeks · lap when two successive checks agree |
| `TRIP-KIT-KISECIK` | [conditional.md](../checklists/conditional.md) | Bait box · sacks for laterite · crocks · probe and plumb · rations counted as fat/protein/starch |
| `STORAGE-CODE-1` | [storage-code-1.md](../government/regulations/storage-code-1.md) | Already a regulation — the inventory row was a duplicate pointer |

These have **not** been moved yet. The claims above are recorded here so nothing is lost while the target documents are still being written.

## ⚠ Conflicts found in the v1 source

Three rows appeared twice with different numbers. The later day was taken in each case, but they are worth a physical count.

| Item | v1 said | Taken |
|---|---|---|
| Quartz FACE-B @ `STORE-4` | ~54.1 kg (d2880) **and** ~51.1 kg (d2825) | ~54.1 kg |
| Bitumen bulk | ~15.1 kg (d2943) **and** ~9.7 kg (d3209) | ~9.7 kg |
| Flax line ~425 g | `WOOD-CRATE-6` (d3075) **and** storage wing N lower shelf (d2709) | `WOOD-CRATE-6` |
