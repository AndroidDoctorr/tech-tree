# Resources

Fungible stock — measured, drawn down, replaced. Schema and the routing test are in [index.md](index.md).

★ **Identical fungible batches** *(dehyd condensate · bleach working stocks · etc.)* **→ one row + total qty** · fixture/bottle IDs stay in [tools.md](tools.md). Per-batch ledger IDs retire to the journal; draws use the aggregate ID.

`| ID | Item | Qty | Where | Made | Last |`

`Made` is blank unless the thing degrades. `Last` is the day the quantity last changed. `×0` means the row is spent but the ID is kept so draws against it still resolve.

## Fuel and char

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`CHAR-LANE`** | Charcoal, oak · green | **~18.4 kg** | Char lane | d5469 retort | d5494 kiln |
| **`CHAR-RESERVE-C`** | Charcoal, oak · sealed reserve | **~10.0 kg** | Char reserve drum | d5190 top-up | d5422 +2.5 kg seal |
| `WOOD-OAK-P5` | Oak, green · main stack | **~69.4 kg** @ pile 5 | Pile 5 | d5470 haul | d5486 Route A |
| **`FURNITURE-SELECT-1`** | Oak, green · furniture grade @ pile 5 north shade | **~3.23 kg** tail | Pile 5 north shade | d4818 | d5071 stake tags |
| **`BARREL-5-FERMENT`** | **Ferment barrel · ~25–30 L class · breath bung · food-oil interior · empty rinsed post d5343 distill** | **1 @ horreum A margin** | **Horreum A margin** | d3895 | d5343 |
| `WOOD-HORNBEAM-GEAR-1` | Hornbeam blank · gear stock · end-grain checked | **~0.10 kg** tail | Craft peg | d3520 | d5468 blower prop |
| `SHIVE-FLAX` | Flax shive | **~6.65 kg** | Storage wing | | d5355 paper |
| `SHIVE-HEMP-Y8` | Hemp shive | **~8.05 kg** | Berm | | d5180 harness loft |
| `SLUMGUM-1` | Slumgum · firelighter | ~4 kg | Fire store | | d3265 |

## Alcohol · ethanol organics pathway

Mash and potable hearts: **`GRAIN-FERMENT-*` · `SPIRIT-GRAIN-*`** @ [food.md](food.md). Ferment vessel: **`BARREL-5-FERMENT`** (fuel table above). Tube reactor + cold trap: **`ETHANOL-DEHYD-TUBE-REACTOR-Y14-1` · `ETHANOL-DEHYD-COLD-TRAP-Y14-1`** @ [tools.md](tools.md). Calcine feed slip: **`KAOLIN-SLIP-M26-1`** (clay bodies). Bed B ZnO boost: **`ZNO-CALCINE`** (metals table).

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`CATALYST-KAOLIN-CALCINE-Y13-1`** | Calcined M26 kaolin · metakaolin · dehyd bed A/B | **~428 g** | Chem porch catalyst peg | d5275 ×2 | d5423 coupling |
| **`ETHANOL-DEHYD-STOCK-1`** | Dehyd condensate · polymer lane rough · **~89 % class @ 14 °C** | **~0.63 L @ `P-LAB-DEHYD-MASTER-1`** | Chem spirit peg | d4933 | d5472 lam wipe |
| **`ETHANOL-DEHYD-RUN-NOTES-5408`** | Tube rig stage log · improvement flags | **@ chem shelf** | Chem porch | d5408 | ice · TC · drip |
| **`ETHANOL-DEHYD-RUN-NOTES-5410`** | Tweak validation · core TC · ×2 ice · drip clamp | **@ chem shelf** | Chem porch | d5410 | validated |
| **`ETHANOL-DEHYD-RUN-NOTES-5411`** | Lip trim · early sweep · run-4 short block | **@ chem shelf** | Chem porch | d5411 | yield HIT |
| **`ETHANOL-DEHYD-HIGH-Y14-1`** | Dehyd hearts · redistilled · **~92–93 % v/v @ 14 °C** | **~1.01 L @ `P-LAB-DEHYD-JAR-PURE-1`** | Chem spirit peg | d5091 | d5419 pilot feed |
| **`OLEFIN-TRAP-STOCK-Y14-1`** | Olefin / C₄ trap bank · stage-2 feed | **~42 ml @ `P-LAB-OLEFIN-TRAP-JAR-1`** | Chem spirit peg | d5102 | d5423 coupling draw |
| **`OLEFIN-RUN-NOTES-5417`** | Olefin tweak log · feed rate · sweep · brine | **@ chem shelf** | Chem porch | d5417 | assay HIT |
| **`C4-COUPLING-STOCK-Y14-1`** | C₄ coupling condensate · **butadiene-class assay** *(impure · not polymer-grade)* | **~12.0 ml @ `P-LAB-C4-TRAP-JAR-1`** | Chem spirit peg | d5103 | d5423 scaled merge |
| **`POLYMER-PILOT-C4-STOCK-1`** | Pilot C₄ trap cuts · runs 1–2 merge | **×0** *(merged d5419)* | Chem spirit peg | d5277 | d5419 bank |
Potable hearts **`SPIRIT-GRAIN-POTABLE-1`** @ [food.md](food.md). Legacy per-batch condensate IDs **`ETHANOL-DEHYD-CONDENSATE-*`** retired **d4936** — journal holds batch history.

## Clay, stone and aggregate

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CLAY-P1` | Clay, raw · green | **~316 kg** @ pile 1 · **~6.3 kg** @ `MATERIARUM` bay 4 | Pile 1 / yard | d5206 haul | d5206 haul |
| `QUARTZ-FACE-B` | Quartz, FACE-B | **~47.7 kg** | `STORE-4` | | d5257 polymer glass prep |
| `QUARTZ-GLASS-FINE-Y13-1` | Glass-grade silica fines · triple-skim levigate · **`QUARTZ-FACE-B`** | **~0.27 kg unallocated** | Chem porch dry tray | d3990 | d5257 polymer glass prep |
| `GLASS-CULLET-BIN-1` | Clean C-grade lab cullet · color-matched | **~84 g** | Chem porch bin | d5258 | d5259 trim |
| **`POLYMER-GLASS-BATCH-CY14-1`** | Polymer-lane lab glass kit · **DRY tail** after d5258–5259 blows | **~1.21 kg** in lidded jars | Chem porch batch shelf | d5257 | d5259 tail |
| `STONE-DRESS-P4` | Dressing / field stone | **~13.9 kg** @ pile 4 north · ×2 marked sacks | Pile 4 north band | | d5335 kerb |
| `RIPRAP-ARMOUR-1` | Riprap outer armour, angular — surplus after `CAMPUS-BRIDGE-APRON-1` · rounded cobble rejected, it rolls | surplus stack | T-2 face | | d3277 |
| **`FLUORITE-FLUX-COARSE-Y13-1`** | Fluorite · ≥2 mm · `M-29` Akkaya · forge flux | **~10.9 kg** @ ore bay `KF-FLUX-1` | Ore bay | d4153 | d4153 |
| **`FLUORITE-FINE-Y13-1`** | Fluorite · <2 mm · chem / optics reserve | **~2.75 kg** @ **`WING-N-CABINET-1`** sealed crock | North wing cabinet | d4153 | d4859 load |
| **`FLUORITE-ASSAY-Y13-1`** | Fluorite · batch cert chip · `M-29` | **~100 g** @ chem vial | Chem porch | d4153 | d4153 |
| **`GRAVEL-1`** | Gravel aggregate | **~2631 kg** @ `MATERIARUM` bays 2–3 + apron class | Yard bays 2–3 | d5458 haul | d5489 haul |
| `SAND-FILTER-1` | Filter / concrete sand · winter dry queue | **~1941 kg** @ `MATERIARUM` bay 4 | Yard bay 4 | d5207 haul | d5463 blocks |
| **`POZZ-TUFF-1`** | Pozzolan / tuff · **`M-27` Koruhöyük class** | **~1139 kg @ `MATERIARUM` bay 1** | Yard bay 1 | d5187 unload | d5463 blocks |

## Lime

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CACO3-P7` | Limestone, raw · plus underburnt returns | **~465.2 kg** @ pile 7 north face | Pile 7, camp north face | d3374 | d5494 kiln |
| `QUICKLIME-1` | Quicklime, dry · green · also `LIMELIGHT-1` feedstock | **~0.04 kg** @ sealed jar *(limelight tail)* | Lime trough | d5494 kiln | limelight pinch |
| **`BLOCK-Y10-DRY-STACK-1`** | BC-2 load-bearing · 90-day cure PASS · shaded stack | **×274 unused** *(**×92 dry @ `BLOCK-PAD-1` / `MATERIARUM` SE** · **×138 submerged** @ pit)* | Materiarum pad / pit | d5464 lift ×16 | d5486 Route A |
| `LIME-PUTTY-1` | Lime putty | **~7.8 kg** @ trough | Lime trough | d5494 slake | invert/mortar |

Quicklime slakes on the air and is the one row here with a real clock — see the keep window in [processing.md](../government/procedures/processing.md).

## `FURNACE-2` green ware *(dry queue)*

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FURNACE-2-TUYERE-1` | Stoneware tuyère · seated @ south service | **×1 SET** | `FURNACE-2` wall | d3682 | d3703 |
| `FURNACE-2-HOT-BLAST-DUCT-1` | Hot-blast duct 1 · stoneware · **28 mm ID** · **A+B+C SET** | **×1 run @ annulus** | `FURNACE-2` jacket | d3712 | d3719 |
| `FURNACE-2-HOT-BLAST-DUCT-2` | Hot-blast duct 2 · stoneware · **28 mm ID** · **A+B+C SET** | **×1 run @ annulus** | `FURNACE-2` jacket | d3721 | d3725 |

## Clay bodies and slips

Washed slips are ranked, and the rank is the whole value of the row — a `#2-class bulk` and the `BEST` jar are not interchangeable even though both are kaolin.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `KAOLIN-SLIP-M26-1` | Kaolin slip · #2-class bulk — **`M-26` + east ranked** | **~16.68 kg** | Chem porch jar | d5137 wash | d5407 calcine prep |
| `KAOLIN-SLIP-M26-BEST-1` | Kaolin slip · best cut — **`M-26`** | **~0.02 kg** | Chem porch jar | d5137 wash skim | d5331 reflector |
| `MONT-M26-TRACE-1` | Montmorillonite trace · **`M-26` wash · field rank only** | **~0.61 kg wet** | Chem porch separate peg | d3331 | d5289 rank trace |
| `KAOLIN-SLIP-5` | Kaolin slip · #2-class bulk — CAND-4-EAST wash | **~0.03 kg** | Chem porch jar | | d3821 |
| `KAOLIN-SLIP-2` | Kaolin slip · rank #2 · **lane primary** | **~0.02 kg** | Chem porch jar | | d3721 |
| `MONT-CAND-1` | Montmorillonite candidate · unwashed, mont rank only | ~2.5 kg wet gross | Chem porch separate peg | | d2527 |

## Brick and tile

> **Loose stock only.** Masonry drawn into a build is debited on the pour day and leaves this file — the result is **`infrastructure.md`** / the map, not a second brick count. Demolition recovery is estimated when it happens; construction detail stays in the journal. **Fired green-batch IDs** retire when the kiln unloads — journal holds batch history.

> **TR vs TF** — **TR** = curved roof half-pipe · `CLAY-P1` · roof face · **hold only — shingle runway supersedes new TR**. **TF** = flat square · washed kaolin · floor face / marver · **fume hood + floor class**. See [TILE-TR-TF-FUME-CABINET-Y12.md](../journal/retcons/TILE-TR-TF-FUME-CABINET-Y12.md).

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BRICK-FIRED-B` | Fired brick, stackable · amber · *masonry wall brick* | **~343** | Kiln B pad | d5189 fire | d5189 fire |
| `TILE-TR` | **Roof tile (TR)**, fired · curved semi-cylinder · hold | **~×160** | Rack south | d5172 fire | d5172 fire |
| `TILE-TF` | **Floor tile (TF)**, fired · flat square · kaolin body | **×29 @ rack north** · **×122 floor** · **×14 bench tray** · **×16 backsplash** · **×4 exhaust duct** · **×2 polymer bridge** | Wing | | d5256 polymer frame |
| `CLAY-RANK-REF` | Refractory rank tiles · fired reference set | ×6 | Bench | | d2447 |
| `PORCELAIN-CHIP-SET-1` | Porcelain chip reference set · stoneware rank | ×10 | `CRAFT-CABINET-2` archive drawer | | d3073 |
| `FORSTERITE-BRICK-TRIAL-Y12-1` | Fired binder ladder · F05 / F10 / F15 / R10 · tested d3620 | **×8 archive** | `CRAFT-CABINET-2` drawer | d3585 | d3620 |
| `FORSTERITE-BRICK-STD-Y12-1` | Production recipe · **90% graded forsterite grog · 10% dry kaolin** · F10 winner | **×90 FIRED** | Sand bank + stack | d3620 | d3657 |
| `TC-SLEEVE-SET-1` | Thermocouple electrical ceramic · **18 × 11 mm segments · twin 2 mm bore · 3 mm web** | **×3 spare FIRED** | Instrument peg tray | d3587 | d3743 |
| **`TC-SLEEVE-SET-2`** | Thermocouple sleeve batch · rev 1.1 · **`TC-PROBE-2` spare** | **×20 GREEN @ north board** | Slatted dry board | d3839 | d3839 |
| **`TC-COLD-BLOCK-2`** | Thermocouple isothermal terminal block · **`TC-PROBE-2` spare** | **×1 GREEN @ north board** | Slatted dry board | d3839 | d3839 |
| **`TC-PROBE-1`** | Iron–constantan probe · **306 mm protected · 8 mm hot junction · cal `TC-CAL-LADDER-Y12-1`** | **×1 LIVE** | Instrument tray + ice jar | d3743 | d3743 |

## Ore

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `O-1-MALACHITE` | Malachite, Y10 · wire-grade carbonate | **~46.8 kg** | Pile 4 | | d5495 draw |
| **`CU-GEN2-SCRAP-CY15-1`** | Cu electrowon draw tail · strip + draw offcuts | **~265 g** | Chill tray | d5496 | 0.65 strip |
| **`WIRE-CU-ARM-REW-CY15-5488`** | 0.65 mm · armature tail *(superseded)* | **~52 m** @ parts peg | Craft north | d5488 | hold / redraw later |
| **`WIRE-CU-ARM-REW-CY15-070-5495`** | 0.70 mm · **`GEN-WW-3-M` stiffness wind tail** | **~16 m** @ parts peg | Craft north | d5495 | d5496 rewind tail |
| **`CU-ROD-BILLET-CY15-5432`** | Cu forge rod · malachite roast | **×0 @ forge peg** | Forge peg | d5432 | d5477 armature draw |
| `CINNABAR-1` | Cinnabar, HgS · ☠ **isolated storage** | **~46.2 kg** | v1 chem, isolated | | d5436 float lap |
| `GALENA-1` | Galena-class lead ore | **~24.2 kg** | Forge staging | | d4753 Kisecik |
| `H-11-HEMATITE` | Hematite | **~90.6 kg @ pile 4** | Pile 4 | d5197–5199 3-day camp haul | d5453 roast |
| **`M-22-MAGNETITE-1`** | Magnetite · raw · pile 4 tray | **~1.50 kg** @ pile 4 | Pile 4 tray | d5361 haul | d5364 ST-MAG |
| **`ST-SPR-BUTTON-Y13-4`** | Spring steel button · **`HEAT-Y13-020` · lock spring band · `ST-SPR-1` class** | **~120 g @ chill tray** | Chill tray | d4186 | d5481 gen brushes |
| **`ST-STR-BUTTON-Y13-3`** | Structural steel button · **`HEAT-Y13-019` · lock reserve** | **×0 tail** | — | d4183 | d5468 switch |
| `SPH-1` | Sphalerite | ~6.12 kg | — | | d2987 |
| `AZURITE-1` | Azurite · smelts as copper **or** grinds as blue pigment | **~0.21 kg** *(pigment reserve)* | Chem porch | | d4614 paint trace |
| `CU-SLAG-Y10` | Copper slag · re-charge stock, still holds metal | ~3.8 kg | Slag dish | | d3230 |
| **`IRON-SLAG-DISH-1`** | Bloomery tap slag · dish + apron | **~4.0 kg** class @ `FORGE-D` | Forge dish | d5443 haul | haul when heavy |
| `CASSITERITE-CONC` | Cassiterite concentrate · fines-heavy, deferred | ~0.5 kg | Forge staging tray | | d2933 |
| `PYRITE-KISECIK` | Pyrite, Kisecik fringe · *(+`PYRITE-SPARK-TIN-1` ~22 g at `FK-1`)* | **~0.55 kg** | Ore shelf | | d3983 |
| `CHROMITE-POD-M24-1` | Chromite pod fragment · podiform | ~190 g | Chem porch dry queue | d3338 | d3344 |
| ★ `GARNIERITE-DRESS-M24-1` | Garnierite, **dressed green fraction** · waxy fracture-fill · **~4.6% metal won** | **~5.05 kg** | `ORE-BAY-1` | d3582 | d3588 |
| `GARNIERITE-FEED-REF-Y12-1` | Homogenized garnierite composite reference · sealed fourth quarter | **75.00 g** | Assay shelf | d3588 | d3588 |
| `NI-REDUCTION-STD-Y12-1` | Standard nickel reduction charges A/B/C · each **75 ore / 15 Cu / 54 char / 12 lime g** | **×3 STAGED** | Chem porch dry jars + collector bags | d3588 | d3588 |
| ★ `M31-A1` | Manganese-class sample · cleanest dense black seam | **~4.15 kg** | Ore bay, separate sack | d3595 | d3603 |
| `M31-A2` | Manganese-class sample · banded black-brown ore | **~3.55 kg** | Ore bay, separate sack | d3595 | d3603 |
| `M31-A3` | Manganese-class sample · wall / lower-grade boundary | **~2.75 kg** | Ore bay, separate sack | d3595 | d3603 |
| `M31-FLOAT-1` | Manganese-class float sequence · fan to source | **~1.15 kg** | Ore bay, separate sack | d3595 | d3603 |
| ★ **`M31-A1-DRESS-Y12-1`** | Manganese ore · dressed production head @ `M-31-A` | **~37 kg** | `ORE-BAY-1` kerb | d3612 | d3615 |
| **`M31-A2-DRESS-Y12-1`** | Manganese ore · dressed blend sack | **~17 kg** | `ORE-BAY-1` kerb | d3612 | d3614 |
| **`M31-FEED-COMPOSITE-Y12-1`** | Roasted Mn feed · homogenized · sealed reference | **~100 g** | Chem porch | d3615 | d3615 |
| `SERPENTINITE-RAW-KISECIK-Y12-1` | Kisecik ophiolite serpentinite · raw · **forsterite feed** · dressed **`K-SERP-RIDGE-1` d3638 · d3648 · d3754 · d3982** | **~39.2 kg** | `ORE-BAY-1` kerb | d3638 | d3988 |
| ★★ `FORSTERITE-GROG-1` | **Dead-burned serpentinite** · buff-grey · rings · no slake | **~0.07 kg** | Kiln yard, covered | d3583 | d5331 ×2 reflector |
| `FORSTERITE-BRICK-Y12-1` | Production forsterite brick · **`FORSTERITE-BRICK-STD-Y12-1`** · **~230×115×45 mm** | **×20 FIRED bank** | South court spare stack | d3621 | d4001 |
| `SERPENTINITE-RAW-CONTROL-1` | Raw serpentinite, unfired · **comparison control — do not use** | ~0.40 kg | Bench shelf, labelled | d3583 | d3583 |
| ★ `NI-CU-BUTTON-Y12-1` | Cu-Ni-**Fe** button · first nickel won · ⚠ **magnetic — iron came with it** | **~61.4 g** | Bench vial | d3582 | d3582 |
| ★ **`NI-STD-A`** | Ni reduction std charge A · **`NI-REDUCTION-STD-Y12-1-3616`** | **~8.1 g** | Chem vial A | d3616 | d3834 |
| **`NI-STD-B`** | Ni reduction std charge B | **~4.2 g** | Chem vial B | d3616 | d3834 |
| **`NI-STD-C`** | Ni reduction std charge C | **~7.5 g** | Chem vial C | d3616 | d3835 |
| `NICKEL-HYPERACCUM-ASH-M24-1` | Ni-indicator plant ash · burned · archive only | ~16 g | Chem porch sealed shelf | d3339 | d3510 |
| `CACHE-MG1-1` | Ore, dressed and cairned **at the face** — head start on the next run | ~15 kg | MG-1 face | | d3227 |

## Metal

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`EC-1-WIRE-SAMPLE-SET-Y13-1`** | EC-1 gauge masters · **×4 @ 10 m · 0.9/0.65/0.5/0.3 mm** · **14 °C R filed** | **1 set** | **`REF-SHELF-1`** · not production | d3889 | d3889 |
| `IRON-BLOOM-1` | Bloomery sponge · GREEN · **rebar / transition bank** | **~0.31 kg @ mount** | Forge mount | d5167 smelt | d5480 yoke |
| **`CROSSFLOW-SHAFT-1`** | *(in runner assembly)* | **`WW-2-CROSSFLOW-RUNNER-1`** | WW yard | d5380 | d5393 stack |
| **`CROSSFLOW-DISC-1/2`** | *(in runner assembly)* | **`WW-2-CROSSFLOW-RUNNER-1`** | WW yard | d5388–5391 | d5393 stack |
| **`CROSSFLOW-BLADE-SET-1`** | **×20 riveted · ~4.58 kg** | **`WW-2-CROSSFLOW-RUNNER-1`** | WW yard | d5390 | d5393 stack |
| **`WW-2-CROSSFLOW-RUNNER-1`** | Off-line runner · shaft + discs + blades · stacked · **QC d5399** | **@ WW yard rack** | WW yard | d5393 | d5399 align tweak |
| **`CROSSFLOW-NOZZLE-LAYOUT-1`** | Throat template · **24 × 105 mm** ×2 cell | **@ WW yard layout peg** | WW yard | d5395 | slider forge |
| **`CROSSFLOW-HEADBOX-MOCK-1`** | Oak dry-fit mock · sill + cheeks · spill trimmed | **~90% @ WW yard** | WW yard | d5395 | d5425 spill cut |
| **`CROSSFLOW-NOZZLE-WAYS-1`** | Oak slider ways · lap 2 true | **@ WW yard bench** | WW yard | d5395 | iron shoes |
| **`CROSSFLOW-NOZZLE-SLIDER-1`** | Two-cell wrought slider · **~1.08 kg** | **On ways · dry-fit PASS** | WW yard | d5401 | link drill · liners |
| **`CROSSFLOW-NOZZLE-2CELL-1`** | Two-cell nozzle + gate hardware · **~1.4 kg** class | **✓ bench-complete** | WW yard | d5395 | d5440 spin witness |
| **`REBAR-STD-Y13-1`** | Wrought rebar reference · **~10.2 mm square · twisted · ~480 mm** · BC-2-REBAR | **~300 g** | `FORGE-D` peg | d4021 | d4022 |
| **`REBAR-PRODUCTION-RACK-1`** | Production rebar · twisted · ~10 mm · ~555–565 mm · pour hooks · **`REBAR-BAR-CY14-37`…`44` + prior CY13 stock** | **×24** | Forge peg rack | d4744 | d5156 ×4 |
| **`REBAR-R&D-Y13-1`** | Rebar QC ladder · twist/lap/bond/cover · **break PASS d4029** | **cert on file** | — | d4029 | d4029 |
| **`REBAR-HOOK-REF-Y13-1`** | Hook termination template · **90° + ~40 mm return · ×2** | **×2 @ peg** | `FORGE-D` | d4022 | d4022 |
| `CS-BAR-Y12-1` | Carbon steel bar · hardened + tempered | **~383 g tail** @ forge peg | Forge peg | Y12 | d5381 cutters |
| `CS-BAR-Y12-2` | Carbon steel bar · hardened + tempered | **~848 g** | Forge peg | Y12 | d3573 |
| `CAST-IRON-BUTTON-Y12-1` | Cast iron button · **`FURNACE-2` trial 1** · combustion ref d3744 | **~167 g** | Chill tray | d3728 | d3744 |
| `CAST-IRON-BUTTON-Y12-2` | Cast iron button · **`HEAT-Y12-001`** · **~3.5 % C** | **~163 g** *(chip)* | Chill tray | d3802 | d3803 |
| `CAST-IRON-BUTTON-Y12-3` | Cast iron button · **`HEAT-Y12-002`** · **~3.5 % C** | **~165 g** *(chip)* | Chill tray | d3803 | d3804 |
| `CAST-IRON-BUTTON-Y12-4` | Cast iron button · **`HEAT-Y12-003`** · **~3.5 % C PASS** | **~164 g** *(chip)* | Chill tray | d3804 | d3812 |
| `CAST-IRON-BUTTON-Y12-5` | Cast iron button · **`HEAT-Y12-004`** · **~3.5 % C PASS** | **~163 g** *(chip)* | Chill tray | d3812 | d3813 |
| `CAST-IRON-BUTTON-Y12-6` | Cast iron button · **`HEAT-Y12-005`** · coupon only | **~164 g** *(chip)* | Chill tray | d3814 | d3815 |
| **`MAG-STEEL-Y13-ROD-1`** | Magnet steel pole rod · **`HEAT-Y13-009` · ~1.0 % C · lift ~44 mm** | **~71 g @ `MOTOR-1-MAG-STACK-1`** | Chem porch bench east | d3900 | d3957 |
| **`MAG-STEEL-Y13-ROD-2`** | Magnet steel pole rod · **`HEAT-Y13-010` · lift ~43 mm** | **~71 g @ `MOTOR-1-MAG-STACK-1`** | Chem porch bench east | d3903 | d3957 |
| **`CONSTANTAN-STD-Y12-1`** | Constantan std stub · run D tail · reproduce from bridge label | **~3.1 g** | Instrument tray | d3734 | d3735 |
| **`CONSTANTAN-BATCH-Y12-2`** | Constantan repro · Run D recipe · run 2 | **~7.7 g** | Chill tray | d3834 | d3834 |
| **`CONSTANTAN-BATCH-Y12-3`** | Constantan repro · Run D recipe · run 3 | **~7.8 g** | Chill tray | d3835 | d3835 |
| **`TC-CONST-LEG-2`** | Constantan TC leg · **Ø0.50 mm · 450 + ~118 mm** · repro batch 1 | coiled @ vault dry peg | d3835 | d3835 |
| **`TC-IRON-LEG-2`** | Iron TC leg · **Ø0.50 mm · 450 + ~120 mm** · spare pair | coiled @ vault dry peg | d3839 | d3839 |
| `CS-TEST-COUPON-Y12-1` | Carbon steel test coupon · fracture reference | **~18 g** | Bench vial | Y12 | d3571 |
| `CS-TEST-COUPON-Y12-2` | Carbon steel test coupon · bar-2 fracture | **~17 g** | Bench vial | Y12 | d3573 |
| `SN-BANK` | Tin | **~0.920 kg** | — | | d5450 transition cast |
| `ZNO-CALCINE` | Zinc oxide calcine | **~1.650 kg** | Chem peg | | d5423 coupling |
| `ZN-METAL-1` | Zinc, prill tail | **~78 g** | Chem-lab lidded tray | | d3743 |
| `HG-METAL-1` | Mercury · ☠ **not food** · isolated | **~83 g** | Purple lidded jar · vac reserve | | d4467 loop charge |
| **`VAC-HG-LOOP-Y14-1`** | Mercury · ☠ **in `VAC-BENCH-1` loop only** | **~199.3 g** | Dish + column + trap path | d4467 | d4479 spill trace |
| **`LEAD-ACID-PILOT-1`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-1`** | **1 jar** | Parallel chem tray · **`SW-STORAGE-TIE-1`** | d3883 | d3971 |
| **`LEAD-ACID-PILOT-2`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-2`** | **1 jar** | Parallel chem tray · **`SW-STORAGE-TIE-1`** | d3887 | d3971 |
| **`LEAD-ACID-PILOT-3`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-3`** | **1 jar** | Parallel chem tray B · **`SW-STORAGE-TIE-2`** | d3999 | d4009 |
| **`LEAD-ACID-PILOT-4`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-4`** | **1 jar** | Parallel chem tray B · **`SW-STORAGE-TIE-2`** | d3999 | d4009 |
| `BRASS-STOCK` | Brass stock · cementation ingot · component tail | **~35 g** @ chill tray | Chill tray | d5342 smelt | d5347 colander |
| **`BRONZE-STOCK`** | Bronze stock · ~10 % Sn · wire/cast tail | **~90 g** @ chill tray | Chill tray | d1526 class | d5450 sprue |
| **`BRONZE-TRANSITION-STOCK-CY15-1`** | Clutch liners + collar stubs · transition pour | **~120 g** tail @ peg | WW yard | d5450 cast | d5455 pin bushes |
| **`WW-2-TURBINE-JACKSHAFT-1`** | Runner jackshaft · ø27.95 mm · pulleys keyed | **in `WW-2-TURBINE-TRANSITION-1` kit** | WW yard | d5452 finish | d5455 d3 |
| **`WW-2-TURBINE-TRANSITION-1`** | Jackshaft · clutches · chain · guards · off-line | **✓ bench-complete @ WW yard** | WW yard | d5455 d3 | Route A install |
| **`HINGE-BRASS-STRAP-CY13-4687`** | Brass strap hinges · construction buffer | **×4 @ craft peg tray** | Craft peg | d4687 | d4687 |
| **`HINGE-BRASS-CABINET-CY13-4740`** | Brass cabinet butt hinges · north wing buffer | **×6 @ craft peg tray** | Craft peg | d4740 | d4850 cabinet |
| **`FUSE-LINK-Y14-1`** | EC-1 link fuse · **0.3 mm × ~8 cm** class | **×0 @ pouch** *(seated d5016)* | Chem peg | d4561 | d5016 lamps |
| `NAIL-BRASS` | Brass nails | ×4 | `WOOD-CRATE-5` forge fastener | | d3103 |
| `NAIL-IRON` | Iron nails / rivet shanks | **×15 @ bench peg tray** | `FORGE-D` bench | d5392 rivet | d5425 hardware |
| `WOOD-SCREW-STOCK-1` | Wood screws · brass all-body · coarse slot | **×2 @ bench tray** *(×1 MARGINAL slot)* | Bench tray | | d4874 stool |

## Copper wire

The wire bank is tracked by **gauge**, because gauge is what decides whether a length is usable for a given job — 0.3 mm will not carry a cell and 1.6 mm will not wind an armature.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CU-WIRE-Y10-3` | 0.3 mm · electrowon, tough-pitch, poled — **drew without a break** | **×0 @ rack** · **~6.07 m @ cave spool** | Wire rack / cave | d3261 | d5294 socket |
| `WIRE-CU-GEN2-1` | 0.9 mm gen-2 · bare · file-bright · feeder tail | **×0 @ chem peg** | Chem peg | d5435 electrowon draw | d5477 redraw spent |
| `WIRE-CU-4` | 1.6 mm · lane B coil, draw feed | **×0 @ chem porch** | Chem porch | | d5480 field draw |
| **`WIRE-CU-FEEDER-4-TAIL-1`** | 1.2 mm · bare · Feeder-4 spare | **~6 m @ G2 peg** | G2 east jamb peg | d5485 | feeder install |
| **`WIRE-CU-LAB-0.5-CY13-1`** | 0.5 mm · bare · lab branch / field tail | **~34 m @ parts peg** | Craft north · parts peg | d4984 | d5481 brushes |
| **`WIRE-CU-LAMP-LEAD-Y16-1`** | 0.5 mm · paired leads · **×3 ~2.0 m class** | **@ domus lighting peg** | Craft north · domus peg | d5319 | d5329 court |
| **`WIRE-CU-LAB-0.65-CY14-1`** | 0.65 mm · bare · motor / armature class | **×0** *(merged d5488)* | — | d4985 | d5488 → arm rewind spool |
| **`WIRE-CU-LAB-0.3-CY14-1`** | 0.3 mm · bare · fuse / trim spool | **~0.41 m @ `PARTS-PEG-BOARD-1` wire bay** | Craft north · parts peg | d4985 | d5468 fuse |
| `CU-WIRE-Y10-COATED` | 0.9 mm coated · wax + rosin ×2 · paper · leads and tails only | **~8.1 m** | Chem peg | d3245 | d4997 leads |
| `CU-WIRE-Y10-4` | ★ **best conductivity drawn to date** — off the glass-cover melt | — | Wire rack | d3266 | d3266 |
| `TC-GALV-LEAD-PAIR-1` | Matched galvanometer copper pair · **2 × 2.50 m · one turn / 20 mm · served** | ×1 on **`TC-PROBE-1`** | Instrument peg | d3587 | d3587 |
| **`TC-GALV-LEAD-PAIR-2`** | Matched galvanometer copper pair · **`TC-PROBE-2` spare** | ×1 @ **`WING-N-CABINET-1`** lower | d3839 | d4859 move-in |
| `TC-BINDING-POST-1` | Brass BN-06 binding posts · 24 mm · Ø1.5 mm lead hole | ×2 on **`TC-PROBE-1`** | d3587 | d3743 |
| **`TC-BINDING-POST-2`** | Brass BN-06 binding posts · **`TC-PROBE-2` spare** | ×2 + washers / nuts @ peg | d3839 | d3839 |

⚠ The armature's 95 m was unwound and redrawn to 0.65 mm at d3267 — it is now `ARMATURE-2` in [electric-grid.md](electric-grid.md), not wire stock.

## Electrical plate and magnet stock

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ZN-VOLTAIC-PLATES` | Zinc voltaic plates, spare · `VOLTAIC-RESERVE` | ~39 | Storage wing | | d3238 |
| `CU-GEN2-VOLTAIC-PLATES-1` | Copper voltaic plates, spare *(+×8 live in `VOLTAIC-8-CELL-1`, ×1 in `DANIELL-CELL-1`)* | **×1** | Tray | | d5476 GEN-WW-3 comm |
| `MAG-BOOT-EM` | EM boot rod tray bank · ~171–175 g, ~37–39 mm solo · **#20–#23 consumed in culina rails** | **×8** | Dry tray | | d5367 culina strips |
| **`MAG-STEEL-Y15-ROD-1`** | Magnet steel pole · **`HEAT-Y15-009` · `ST-MAG-1`** · lift ~45 mm | **@ `MOTOR-4-MAG-STACK-1`** | North bench | d5362 | d5465 motor |
| **`MAG-STEEL-Y15-ROD-2`** | Magnet steel pole · **`HEAT-Y15-010` · `ST-MAG-1`** · lift ~44 mm | **@ `MOTOR-4-MAG-STACK-1`** | North bench | d5363 | d5465 motor |
| **`MAG-STEEL-Y15-ROD-3`** | Magnet steel pole · **`HEAT-Y15-011` · `ST-MAG-1`** · lift ~44 mm | **~72 g @ dry tray** | Chem porch dry tray | d5364 | triplicate cert |
| `MAG-BOOT-SPARE-1…4` | Demoted rods, ~27–36 mm solo class | ×4 | Horreum B peg | | d3162 |

Rods #16 and #19 are in `MAG-STACK-2` and #6 rods are in `GEN-WW-1`'s yoke — see [electric-grid.md](electric-grid.md).

## Glass and chemical

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `GP-Y8-C-LITE` | Glass pane, C-lite · general spare, dividered | **×8 spare** | Storage wing N upper shelf | | d4726 margin |
| `GLASS-CLARITY-A/B/C-3994` | Y13 clarity ladder disks · ~3.4–3.5 mm · labelled | **×1 @ sand bed** *(A remelt d4577 · C → `LOUPE-Y13-1` d4224)* | Chem east anneal lane | d3994 | d4577 |
| `KELP-ASH-5` | Soda / kelp ash · refined + coast burn batch | **~404 g** | v1 chem | | d5404 titre |
| `LEAD-ACID-JAR-Y13-3` | Lead-acid cell jar · glass · wide mouth · **~418 ml** · **`LEAD-ACID-PILOT-3`** | **→ pilot cell** | Parallel chem tray B | d3995 | d3999 |
| `LEAD-ACID-JAR-Y13-4` | Lead-acid cell jar · glass · wide mouth · **~422 ml** · **`LEAD-ACID-PILOT-4`** | **→ pilot cell** | Parallel chem tray B | d3995 | d3999 |
| `PB-PLATE-NEG-Y13-3` | Lead plate blank · negative · jar #3 | **~105 g** | Forge peg · tagged | d3997 | d3997 |
| `PB-PLATE-POS-Y13-3` | Lead plate blank · positive · jar #3 | **~104 g** | Forge peg · tagged | d3997 | d3997 |
| `PB-PLATE-NEG-Y13-4` | Lead plate blank · negative · jar #4 | **~104 g** | Forge peg · tagged | d3997 | d3997 |
| `PB-PLATE-POS-Y13-4` | Lead plate blank · positive · jar #4 | **~105 g** | Forge peg · tagged | d3997 | d3997 |
| `GLASS-TINT-LENS-Y10-D` | Tint lens spare | **`SUNGLASS-LENS-Y10-3` lapped · tint D matched · spare peg** | Spare peg | d3430 | d3517 |
| `PAPER-SHEET-Y9` | Paper, flax · tail sheet | **×1** *(merged bank)* | Chem-lab rack | | d4994 bank |
| **`PAPER-SHEET-Y14-FLAX-1…10`** | Paper, flax · chem-lab stock · couch d4994 | **×4 @ chem-lab rack** | Chem-lab rack | d4994 | d4998 chart |
| **`KITCHEN-PARCHMENT-Y15-1`** | Flax parchment · beeswax/rosin size · bake/release | **×4 @ culina peg board** | Domus culina | d5356 | |
| **`KITCHEN-WAXPAPER-Y15-1`** | Wax-dipped flax wrap roll | **×1 roll (~6 sheets)** | Culina drawer | d5356 | |
| `PAPER-SHEET-Y10-FLAX-1…3` | Paper, flax · roof R&D pulls | ×2 drying @ rack · ×1 on panel | Chem-lab rack | d3472 | d3472 |
| `ROOF-R&D-PANEL-1` | Roof coupon deck · coupons **A0–F2** | **11 coupons** @ chem porch south lean · **rain read d3873 F2 PASS** | Chem porch | d3472 | d3873 |
| `BITUMEN-ROOF-TRIAL-1` | Bitumen · roof-grade trial crock · skimmed bulk | **~0.95 kg** | Chem porch | d3472 | d3869 |
| `SAND-ROOF-FINE-1` | Sand, screened fine · roof surfacing | **~700 g** | Chem porch jar | d3472 | d3869 |

## Fibre, cordage and hide

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FLAX-TOW-BANK` | Flax tow | **~227 g** | Wing shelf | | d5424 forge plugs |
| `FLAX-THREAD-COVER-Y10-1` | Flax thread · wagon cover inner | **~43.9 m** tail | Craft wing peg | d3401 | d5178 harness |
| `FLAX-THREAD-SHINGLE-Y10-1` | Flax thread · roof / shingle mat bank | **×0 tail spent** | Craft wing peg | d3505 | d5176 harness |
| `ROOF-SHINGLE-FINISHED-Y12-1` | Flax shingle strips · impregnated · sanded · ~10 × 18 cm | **×7** | Chem porch peg | d3869 | d3869 |
| **`FLAX-LINE-Y12-1`** | Flax line · field Y12 · **`P-RETT-34` heckle** | **~1.28 kg** @ `WOOD-CRATE-6` fibre | Storage wing | d3865 | d4962 spin |
| **`FLAX-LINE-Y13-1`** | Flax line · field Y13 · **`P-RETT-37` heckle** | **~1.03 kg** @ `WOOD-CRATE-6` fibre | Storage wing | d4236 | d4974 hang wire |
| **`FLAX-LINE-Y14-1`** | Flax line · field Y14 · **`P-RETT-38` heckle** | **~1.68 kg** @ `WOOD-CRATE-6` fibre | Storage wing | d4623 | d5180 harness tweak |
| **`FLAX-LINE-Y15-1`** | Flax line · field Y15 · **`P-RETT-39` heckle** | **~2.42 kg** @ `WOOD-CRATE-6` fibre | Storage wing | d4966 | spin defer |
| **`FLAX-THREAD-Y16-1`** | Flax thread · field Y16 · motor-assist spin d5350 | **~641 m** @ craft peg | Craft wing peg | d5350 | d5496 gen serve |
| **`CULINA-HAND-TOWEL-Y16-1`** | Hand towel · plain linen · **~42×28 cm** | **×2 @ culina peg board** | Domus culina | d5354 | |
| **`CARBON-FILAMENT-STOCK-Y14-1`** | Carbon filament · hand-drawn flax | **~8.1 g** · ×12 lengths @ chem peg | Chem porch | d4452 | d4481 matrix |
| **`WING-LAMP-FILAMENT-CY13-1`** | Carbon filament · **wing lamp · ~0.22–0.28 mm · extra-dry redraw** | **~3.95 g** · ×6 lengths @ chem peg *(spare)* | Chem porch | d4845 | d4846 A/B spent |
| **`CARBON-FILAMENT-FINE-Y14-1`** | Carbon filament · **elite fine · ~0.26–0.32 mm** | **~3.8 g** · ×3 lengths @ chem peg | Chem porch | d4481 | d5009 gauge |
| **`IRON-FILAMENT-WIRE-Y14-1`** | Iron wire · lamp draw trial · **~0.22 mm** | **~0.89 m** @ chem peg | Chem porch | d4452 | d4480 cork trial |
| **`REED-CARBON-FILAMENT-STOCK-Y14-1`** | Reed ribbon char · hand-drawn · scout | **~3.2 g** · ×5 lengths @ chem peg | Chem porch | d4575 | d5009 redraw feed |
| **`REED-FILAMENT-DRY-Y14-2`** | Reed carbon · extra-fine draw · spare @ chem peg | **~0.44 g · `SPARE-Y14-2`** *(~×1 hairpin)* | Chem porch peg | d5009 | d5272 open-5 |
| **`FLAX-WILD-LINE-Y13-L1`** | Wild flax line · lap 1 · **`P-RETT-35` heckle** | **~0.46 kg** @ `WOOD-CRATE-6` fibre | Storage wing | d4236 | d4601 |
| **`HEMP-LINE-Y13-1`** | Hemp line · Bed A Y13 · **`P-RETT-36` heckle** | **~0.32 kg** @ `WOOD-CRATE-6` fibre | Storage wing | d4236 | d5189 trace |
| **`HEMP-FIBRE-Y14-1`** | Hemp stalk · Bed A north Y14 · **`HEMP-CUT` d4485** · dry @ rafter | **~7.90 kg** @ `W-1` north | Barn | d4485 | d5336 lash |
| **`HEMP-THREAD-Y16-1`** | Hemp thread · Bed A Y16 · spin d5351 | **~583 m** @ craft wing peg | Craft wing peg | d5351 | d5352 lash |
| **`THISTLE-HEAD-DRIED-Y13-1`** | Cardoon-type heads · full-flower cut · rennet stock | **×9 @ horreum herb peg** | Horreum | d4074 | d4074 |
| **`THISTLE-HEAD-DRIED-Y14-1`** | Cardoon-type heads · Y14 cut · dry queue @ `W-1` | **×8 heads** | `W-1` north rafter | d4407 | d4407 |
| **`THISTLE-HEAD-DRIED-Y15-1`** | Cardoon-type heads · Y15 lap 1 · rennet stock | **×9 heads** dry @ herb peg | Horreum | d4824 | d4824 |
| **`THISTLE-HEAD-DRIED-Y16-1`** | Cardoon-type heads · Y16 lap · full-flower cut | **×10 heads** wet-cut @ `W-1` | `W-1` north rafter | d5160 | d5160 gather |
| **`FLAX-THREAD-Y13-1`** | Flax thread · motor-assist spin d3977 | **×0 @ craft peg** | Craft wing peg | d3977 | d5176 harness |
| **`MOUTH-FLOSS-Y13-1`** | Waxed floss · 3-ply flax · **`DEER-TALLOW`** | **~12 m @ craft peg** | Craft wing peg | d4239 | d4239 |
| **`TOOTH-BRUSH-Y13-1`** | Oak handle · frayed flax line head | **@ culina peg** | Culina | d4239 | d4239 |
| **`MINT-INFUSE-OIL-Y13-1`** | Mint macerate in clear cook oil · **not steam distill** | **~35 ml @ culina shelf** | Culina | d4239 | d4239 |
| **`HEMP-THREAD-Y12-1`** | Hemp thread · Bed A Y12 spin | **~296 m** | Craft wing peg | d3787 | d5189 trace |
| `ROPE-HEMP-Y12-1` | Hemp rope · 3-strand · Y12 yarn · even lay · ⚑ break test + ÷6 cert defer | **~48 m** | WW peg | d3788 | d3789 |
| `HEMP-THREAD-Y10-1` | Hemp thread · cover weft | ~75 m | Craft wing peg | d3382 | d3400 |
| `WAGON-V2-COVER-HEMP-FLAX-1` | Wagon cover · hemp shell + flax liner · air gap · **outer oilcloth refresh d5352** · mounted Norima | ✓ CLOSED d3407 | `WAGON-V2-COVER-ARCH-1` | d3400 | d5352 refresh |
| `HEMP-TOW-BANK` | Hemp tow | **~299 g** | Storage wing tow bag | | d5265 heckle |
| `ROPE-HEMP-STOCK-2` | Hemp rope · reserve / lash · **cover weave band** | **~16.0 m** | WW peg | | d5336 nitre lash |
| `ROPE-HEMP-HOME` | Hemp rope · good lay, **reserve for load work** | **~3.6 m** | Pile 2 | d3221 | d4617 overhaul |
| `ROPE-HEMP-Y10` | Hemp rope · ⚠ **lash class only** — uneven lay, soft spots, never under load | ~28 m | Pile 2 | d3226 | d3226 |
| `ROPE-1` | 3-strand hemp · ⚠ **lashing grade only** — uneven lay | ~24 m | — | d3255 | d3255 |
| `ROPE-2` | 3-strand hemp · ★ **certified: loaded haul and lashing at breaking ÷ 6, spliced not knotted** · ⚠ **not life-bearing** | ~23 m | — | d3255 | d3264 |
| `ANTLER-SHED` | Antler, cast and hard · beats bone for anything taking a blow | ×6 | Craft wing | | d3269 |
| `CLOTH-WAGON-COVER` | Wagon cover cloth, tail stock | **~0.37 kg** | `CART-YARD` south peg row | | d5352 patch |
| `THREAD-STOCK-2` | Thread · *coil serving — leads and crossovers only* | **×0** | Craft wing peg | | d5496 spent |
| `THERMAE-FULL-Y14-1` | Full-width thermae towel · purple · gold end vines | **×1 @ felt** | Atelier felt | d4604 | d4633 |
| `THERMAE-FULL-Y14-2` | Full-width thermae towel · purple · gold end vines | **×1 @ felt** | Atelier felt | d4613 | d4633 |
| `THERMAE-FULL-Y14-3` | Full-width thermae towel · purple · gold end vines | **×1 @ felt** | Atelier felt | d4623 | d4633 |
| `THERMAE-FULL-Y14-4` | Full-width thermae towel · purple · gold end vines | **×1 @ felt** | Atelier felt | d4630 | d4633 |
| `THREAD-1` | Thread, general | **~239 m** | Craft peg bank | | d4869 curtain E |
| **`OFFICINA-N-CURTAIN-W-1`** | Linen curtain · west window · **~130×145 cm** · Prussian | **LIVE @ window** | north wing W | d4873 | |
| **`OFFICINA-N-CURTAIN-E-1`** | Linen curtain · east window · **~130×145 cm** · Prussian | **LIVE @ window** | north wing E | d4873 | |
| **`OFFICINA-N-CURTAIN-ROD-W-1`** | Oak curtain rod · west head | **LIVE** | north wing W | d4873 | |
| **`OFFICINA-N-CURTAIN-ROD-E-1`** | Oak curtain rod · east head | **LIVE** | north wing E | d4873 | |
| **`OFFICINA-N-CURTAIN-BRACKET-CY13-4872`** | Brass wall brackets · rings installed @ headers | **×4 LIVE** | north wing W+E | d4873 | d4873 |
| `VENT-BELT-ROPE` | Rope, vent belt | ~123 m | — | | d1970 |
| `EXPED-ROPE` | Hemp rope · D-27 salvage | ~72 m | Cart peg | | d2945 |
| `FLAX-SHIVE-Y8-21` | Flax shive · **paper grade** | **~0.058 kg** | Storage wing | Y8 | d5484 shim |
| `FEATHER-BAG` | Feather, bag | ~71 g | — | | d3509 |
| `LAB-LINEN-STOCK-1` | Lab linen — filters ×8 · jar wraps ×4 · voltaic separators ×19 · **`LA-SEP-RESERVE-Y13-1` ×1** · wipes ×7 · spill reserve ×2 @ porch · ×2 @ **`WING-N-SPILL-PEG-1`** | — | Chem porch + wing | | d4874 refill |
| `P-FLAX-LINE-Y8-1` | Flax line, Y8 · `P-RETT-23` break/heckle | ~1.03 kg | WW peg | Y8 | d3135 |

## Hide, leather and bone

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| ✓ **`DEER-HIDE-Y15-1`** | Red deer hide · tanned spring block | **×0 → `DRAFT-HARNESS-NORIMA-1`** | — | d5156 pull | d5176 cut |
| ✓ **`DEER-HIDE-Y15-2`** | Red deer yearling · tanned | **×0 → `DRAFT-HARNESS-NORIMA-1`** | — | d5172 pull | d5176 cut |
| ✓ **`DEER-HIDE-Y15-3`** | Red deer · tanned | **×0 → `DRAFT-HARNESS-NORIMA-1`** | — | d5174 pull | d5176 cut |
| **`YULE-BELT-Y12-1`** | Deer belt · **`BELT-WIDTH-STD-Y12-1` 22.0 mm** · **`BRASS-BUCKLE-Y12-1`** · gift wrap | **~1.05 m** | Vestiarium Yule shelf | d3828 | d3828 |
| `SINEW-DRY` | Sinew, dry | **~16 g** | Bench | | d5178 harness |
| `GOAT-HIDE-A03-2` | Goat hide, reserve · flap tail | **~0.05 m²** | Horreum B | | d4794 seal |
| `HIDE-SCRAP` | Hide scrap, tail | **~0.22 m²** | Harness bench | | d5180 loft |
| `WEATHER-STRIP-LEATHER-1` | Weather strip, ~25 mm | ~4.6 m | — | | d3167 |
| `MACHINE-BELT-LEATHER-KIT-1` | Machine belt stock — WW · drill · trip tail | — | `BELT` peg | | d3052 |
| `TRAIL-GEAR-LEATHER-1` | Belt v2 blank · waterskin patch · lash tabs ×4 | — | Vestiarium trail peg | | d2964 |
| **`DEER-BONE-Y12-1`** | Red deer bone · **`DEER-BUTCHER-Y12-3796`** | **~11 kg** | **`BONE-BANK-1`** peg | d3796 | d3796 |
| **`DEER-BONE-Y15-1`** | Red deer bone · spring block **`DEER-BUTCHER-Y15-5108`** | **~14 kg** | **`BONE-BANK-1`** peg | d5108 | d5108 |
| **`RED-STAG-BONE-Y10-1`** | Stag bone · **`RED-STAG-Y10-1` sort d4958** | **~3.2 kg** | **`BONE-BANK-1`** peg | d4958 | d4958 |
| ✓ **`TAN-DEER-Y15-2`** | Tan clock · yearling | **CLOSED d5172** · **`DEER-HIDE-Y15-2`** | — | d5109 | d5172 pull |
| ✓ **`TAN-DEER-Y15-3`** | Tan clock · **~0.81 m² raw class** | **CLOSED d5174** · **`DEER-HIDE-Y15-3`** | — | d5109 | d5174 pull |
| **`TAN-BOAR-Y15-1`** | Tan clock · boar **~0.92 m²** | **Frame queue · rung 1 hold** | Horreum B frame | d5109 | d5109 load |
| **`BOAR-BONE-Y15-1`** | Wild boar bone · frames | **~8.4 kg** | **`BONE-BANK-1`** peg | d4911 | d4911 |
| ✓ `BONE-ASH-1` | **Bone ash, white, calcined** · ★ **~28 cupels · ~1.5 passes through `GALENA-1`** | **~3.08 kg @ porch** · **~0.5 kg @ cave** | Chem porch / cave | d3309 | d4454 renewals |

> ☠ ★★★ **THE MIDDEN DOES NOT GIVE IT BACK** *(d3309)*. *Nine years of it forked over for ~2.8 kg of usable fragment — weathered soft, gnawed, trodden into the ash, the small bones gone entirely.* ★★★ **It is not lost the way a mislaid tool is lost. It is GONE.** ★★ *The other half of d3303: the clocks ran while I was not reading them, and they do not run backwards.*

> ★★★ **`OXIDISING-COOL` — CALCINE ON THE COOLDOWN, NEVER ON THE CLIMB** *(d3309)*. ☠ **A stoked kiln is REDUCING, and carbon in a cupel reduces litharge straight back to lead** — *the exact reaction the hearth exists to run the other way.* ★★★ **Stop stoking, damper wide, trays shallow and high in the chamber: a kiln at ~800 °C full of moving air is a free oxidising furnace** — ☠ **and I threw those hours away after every firing for nine years.** ✓ *The soak burns midden charcoal out as a side effect.* ★ **Bone ash must be WHITE — grey means carbon, and carbon means no silver.**

> ☠ ★★★ **`BONE-BANK-1` opened d3297 — bone is the rate limit on SILVER, not the hearth.** *A cupel is a reagent consumed every run; ~4.7 kg of bone is ~3 kg of ash is ~20 cupels is ONE pass through `GALENA-1`.* ⚑ **Retain every bone from every butchery and every kitchen pot, dried, on the Horreum peg** — ☠ *nine years of it went on the midden.*
> ✓ ★★ **Used cupels are BANKED ORE, not waste** — *lead-soaked, richer than anything dug.* **They go in the kerbed galena bay at `ORE-BAY-1`.**

☠ **Strong liquor on a raw hide case-hardens it.** The ladder is the procedure, not a refinement of it.

Rope is here rather than in tools because it is measured and consumed. A rope rigged into a fixed installation belongs to that installation's entry — `CAVE-3-FIXED-LINE-1` is in [infrastructure.md](infrastructure.md), not this table.

★★ **Grade is the row, not a note.** A length of rope at lashing grade and a length certified for loaded haul are different materials that happen to look identical, so the grade rides in the item name where a grep cannot miss it. `ROPE-2` carries its first real working load on the record — ~130 kg of basalt over 14 km, clean. Working load is **breaking ÷ 6**, a knot costs another third, and shock multiplies enormously. The measured breaking load came from deliberately destroying a length and is written up as doctrine, not held as stock.

## Atelier art

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`PAINTING-Y14-1`** | Egg-tempera on linen panel · horizon + memory portrait · north-light study | **×1** | M2 WORK north wall | d4306 retcon | d4306 retcon |
| **`FRAME-OAK-Y14-1`** | Oak slip frame · ~280×360 mm · keyed corners | **×1** | M2 WORK north wall | d4306 retcon | d4306 retcon |
| **`FRAME-OAK-Y14-2`** | Oak slip frame · ~280×360 mm · mate to **`PAINTING-Y14-1`** | **×1** | M2 WORK north wall | d4306 retcon | d4306 retcon |
| **`FRAME-OAK-Y15-POKER-1`** | Oak stretcher · ~360×480 mm · **`PAINTING-DONKEYS-PLAYING-POKER-Y15-1`** | **mounted @ domus ante** | Domus ante | d4610 | d4974 hang |
| **`FRAME-OAK-Y15-POKER-OUTER-1`** | Oak outer frame · carved ogee · **`YULE-GIFT-Y15-DONKEYS-POKER-1`** | **✓ hung domus ante east wall** | Domus ante | d4969 | d4974 hang |
| **`PAINTING-DONKEYS-PLAYING-POKER-Y15-1`** | Donkeys Playing Poker homage · egg-tempera WIP | **~40% @ `EASEL-1`** | M2 WORK north light | d4610 | d4677 |

*Prior: **`PAINT-CANVAS-1`** @ **`EASEL-1`** · swatch studies d1701+ · **`EASEL-1`** @ infrastructure/M2.*

## Stone working

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BASALT-BLOCK-1/3` | Dyke basalt triplet · Blocks 1 + 3 · ring sound | ~87 kg rough class | `WW-YARD` | d3264 | d3543 |
| `BASALT-BLOCK-2` | Dyke basalt · **wear plate @ `BORING-MILL-1` bed** | ~43 kg | `WORKBENCH-1` east | d3264 | d3543 |
| `LAP-GRIT-1/2/3/4` | Lapping grit, four settled grades coarse → very fine · labelled crocks | ×4 crocks | — | d3264 | d3264 |
| `LAP-GRIT-5` | Lapping grit, finest elutriation tail · crock | small crock | Lap bench | d3468 | d3498 |

✓ **`BASALT-DATUM` triplet CLOSED @ d3469 · fine lap d3498** — Blocks 1/3 @ yard · **Block 2 @ mill bed** · reference @ Block 1 primary.

Grits were graded by elutriation, so the settling times are **arbitrary but identical every batch**: repeatable rather than known. Wash between grades.

## Pigment, dye and reagent

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `MADDER-ROOT-DRY` | Madder root, dry · merged `MADDER-DRY-V1` | **~241 g** | Chem shelf | | d5313 Y16 dig |
| `WOAD-RESERVE` | Woad, dry | **~308 g** | Storage wing dye shelf | | d4800 awning dips |
| `WOAD-LEAF-Y10-1` | Woad leaves, fresh · **window pull 1** | ×0 spent | — | d3345 | d3351 |
| `PRUSSIAN-BLUE-1` | Prussian blue pigment · ☠ **not food** | **~10 g** | Craft cabinet 2 pigment shelf | | d4870 curtains W |

Madder needs an alum mordant. Woad does not — it is a vat dye and fixes mechanically. See `WOAD-VAT` in [processing.md](../government/procedures/processing.md).

## Mineral and salt

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `M-14-SULFUR` | Sulfur · ~15.6 kg block plus ~88 g flour | **~15.60 kg** | — | | d4237 |
| `M-11-ALUM` | Alum, crude | **~1.22 kg** | — | | d4870 mordant |
| `M-12-NITER` | Niter crystal | **~913 g @ chem** · **~100 g @ `CAVE-RECOVERY-CRATE-1`** | Dry jar / cave vial | d3424 | d5260 boil Y16-2 |
| **`BLEACH-CLEAN-1`** | Hypochlorite bleach · dilute cleaning stock | **~660 ml** | Bleach peg · `P-LAB-BLEACH-BOTTLE-1/2/5` | d3454 | d4936 ledger |
| **`BLEACH-CHEM-1`** | Hypochlorite bleach · concentrated chem stock | **~285 ml** | Bleach peg · `P-LAB-BLEACH-BOTTLE-3/4/6` | d3454 | d4936 ledger |
| `QUARTZ-FRIT` | Quartz frit | ~40 g | Vial `G-FRIT` | | d3332 |

`BITTER-SALT-1` is the sulfate of an earth that is **not lime** — lime water precipitates it, hepar confirms sulfate, and a clean hydrogen flame rules out soda.

## Gypsum and plaster

The Samandağ face turned a one-off haul into a bank. Grades are not interchangeable and the row names say which is which.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ACID-VITRIOL-3` | Oil of vitriol, strong · **Kisecik middle-cut class** | **~41 ml** | `P-LAB-ACID-BOTTLE-7` · isolated chem shelf | d5434 distill | d5489 leach |
| `LEAD-ACID-ELECTROLYTE-Y13-3` | Dilute H₂SO₄ · **~1.24 SG** · in **`LEAD-ACID-PILOT-3`** | **→ cell** | Parallel chem tray B | d3998 | d3999 |
| `LEAD-ACID-ELECTROLYTE-Y13-4` | Dilute H₂SO₄ · **~1.24 SG** · in **`LEAD-ACID-PILOT-4`** | **→ cell** | Parallel chem tray B | d3998 | d3999 |
| `VITRIOL-FEED-CROCK-1` | Copperas feed · Kisecik-class green · calcined as needed | **~6.6 kg** | Chem porch feed crock | d5436 fringe | d5434 calcine |
| **`VITRIOL-LIQUOR-KISECIK-Y12-1`** | Green-vitriol heap liquor · **ARSENIC ASSUMED PRESENT** · ☠ **hood-only · ~400 ml scale PASS d3878** | **~13.3 L** read @ d5436 turn | Isolated chem bay · ×2 lidded stoneware crocks in secondary tray | d3590 | d5436 heap turn |
| **`ARS-IMMOBILIZED-LIME-3879`** | Arsenic immobilized · lime precipitate · scorodite-class · ☠ **handle as poison stock** | **~18 g wet cake** | Lidded jar · isolated chem tray · tagged | d3879 | d3879 |
| **`ARS-WASHED-TAIL-3879`** | Iron-rich tail post arsenic wash · colcothar-class · low-As | **~34 g** | Isolated dish · tagged | d3879 | d3879 |
| **`ARS-WORKUP-FILTRATE-3879`** | Spent work-up filtrate · arsenic depleted · weak iron/sulfate | **~395 ml** | `ACID-DREG` crock · tagged | d3879 | d3879 |
| `COLCOTHAR-2` | Raw red ferric residue · `RETORT-B` batch 1 | small dish | Chem porch · unwashed | d3335 | d3335 |
| ✓ ★★★ `ROUGE-FINE-1` | **Washed, levigated hematite finishing polish** · ★★ **clears final glass haze; does not remove deeper scratches** | small crock | Lap bench | d3318 | d3498 |
| ✓ `IRON-OXIDE-PIGMENT-1` | Clean red hematite, coarser early-settling fraction · **pigment, not trusted on finished glass** | small crock | Pigment shelf | d3318 | d3318 |
| `GYPSUM-CLEAN-POWDER-1` | Gypsum, clean powder · **raw stone — burn small batches on demand** | **~21.1 kg** | Chem porch dry store | | d4806 calcine |
| `GYPSUM-FIELD-GRADE-1` | Gypsum, field grade · gritty · strip-trial stock | ~15.4 kg | Pile 7 | | d3225 |
| `GYP-STOCK-1` | Gypsum, raw · `SC-GYP-SAMANDAG-1` face open | ~14.2 kg | Chem porch peg | | d2823 |
| `PLASTER-CALCINED-1` | Plaster, calcined · ⚠ **stales in damp air — use it** | **~0.13 kg** tail | Working stock | d3225 | d4806 skim |
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
| `BLAST-CAP` | Blast caps | **×3** | HOME powder safe | | d3716 |
| `CHARCOAL-FLOUR` | Charcoal flour · one batch thin | **~4 g tail** | Powder jar | | d4224 |
## Resin, wax and sealant

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BITUMEN-ASI-1` | Bitumen, Asi seeps · 4 crocks, sand-dusted · ⚠ heavy end only | **~38.25 kg** · **pot stowed** | Chem porch / wagon | d3270 | d4750 exped lash |
| `BITUMEN-BULK-1` | Bitumen · *(+~1.5 kg chip at cart trial tin)* · ☠ not food | **~5.76 kg** | `BITUMEN-POT-1`, cart yard | | d5041 buckets |
| `CORK-BARK` | Cork bark | **~0.91 kg** | — | | d4480 cork plate |
| `BEESWAX-V1` | Beeswax · *(plus ~1.04 kg at the wax store — see below)* | **~38 g** | v1 chem · craft cabinet 2 | | d5477 armature |
| `TALLOW-1` | Tallow | **~50 g** | v1 trough jar | | d3598 |
| `WAX-DROSS-1` | Slumgum / wax dross · fire starter | **~63 g** | Hearth / lean jar | | d4726 render |
| `ROSIN-1` | Rosin · pale, brittle | **~73 g** | Chem porch | | d5484 belt |
| `TURPENTINE-1` | Turpentine · ☠ **flammable — cool, away from fire** | **~18 ml** | Stoppered glass, chem rack | d5473 distill | d5480 field tack |

Rosin dissolved in turpentine is a cold brushable varnish, and turpentine is the linseed-varnish thinner. `PINE-TAP-CUPS` — ×8 trees scored and cupped at the pine stand — are a standing resource and live in [crops.md](crops.md); collect on the pass.

★ **`BITUMEN-ASI-1` clears the damp-proof course gate for the August plaster.** ~40 kg from three staked seeps on the Asi margin bench, ~6 km out.

## Acid

☠ Every row here is a `SAFETY`-class handling item. PPE, fume hood and rehearsed spill response are prerequisites, not precautions — `CHEM-SPILL-KIT-1` and `CHEM-SPILL-PEG-1`.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `HYDROCHLORIC-ACID-1` | Muriatic acid · cassiterite wash green | ~40 ml | **`WING-N-CABINET-1` upper** | d2961 | d4859 load |
| `NITRIC-ACID-1` | Aqua fortis, batch 1 | ~34 ml | **`WING-N-CABINET-1` upper** | d2793 | d4859 load |
| `STRONG-ACID-BANK` | Sulphuric acid · cell + leach draw stock | **~82 ml** | Bottles 5 · 6 *(2–3 sealed)* | d5434 distill | d5489 leach |

⚠ **The sulphuric bank is off by about a thousandfold for its intended job.** A bulk leach needs kilograms; there are four millilitres, most of which is committed to `DANIELL-CELL-1`. Treat the bank as a reagent supply, not a process input, until there is a lead-chamber or contact route.

## Wax

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `WAX-Y10-RENDER-1` | Beeswax, clean cake — render stock | **~288 g** | Wax store | d5456 band tail | d5356 culina paper |
Y10's binding constraint, closed. Yield per kg of comb is low because old brood comb is mostly cocoon and propolis — honey comb off top bars is the rich fraction. See [bees.md](../government/procedures/bees.md).

## Routed elsewhere

Rows that sat in the v1 sections ported so far but are not resources. Recorded so the port is auditable and nothing is silently dropped.

| Went to | Rows |
|---|---|
| [vehicles.md](vehicles.md) | `COVERED-WAGON-1` · `Norima` · all `WAGON-*` fittings |
| [tools.md](tools.md) | All `P-LAB-*` · `THERMOMETER-1/2` · `GLASS-TUBE-*` · `GLASS-CUP-1…4` · `GLASS-BOTTLE-*` · `CULINA-*` · `GLASS-MOLD-KIT-1` · `MARVER-FLAT-PLATE-1` · `LAB-STAND-1-A/B/C` · `GLASS-PLIERS-1` · `HELICAL-MANDREL-1` · `PORC-BOWL-1…4` · `PORC-PLATE-1/2` · `PORC-VASE-Y8-1` · `PORC-PROBE-SET-1` · `DRY-TRAY-1/2` · **`MUSKET-1` Sentanár kit** |
| [infrastructure.md](infrastructure.md) | `NITRE-BED-1` · `URINE-CROCK-1` · `CHAR-RETORT-1/2` · `ANNEAL-SAND-BATH-1` · `KILN-D-PLENUM-1` · `COLD-CELLAR-FAN-1` · `ICE-VAULT-NICHE-2` · `WW-2-BELT-COLLAR-4` · `SLUICE-2-*` · `AMPHORA-5…10` · `NUT-SHELF-EXT-1` · `CHEM-SLIP-SHELF-1` · `WORK-TABLE-*` · `CAVE-3-FIXED-LINE-1` · `HIVE-SCALE-1` · `SCARECROW-1` · `BIRD-RATTLE-LINE-1` · `HAWK-KITE-1` · `POT-WHEEL-2` · `PORC-BASIN-1` · `CULINA-FAUCET-BRASS-1` · `ACORN-LEACH-TROUGH-1/2` · `EVAP-RACK-1` · `BITUMEN-POT-1` · `P-μ-*` · `P-ξ-*` |
| [electric-grid.md](electric-grid.md) | `GEN-WW-*` · `EC-1-GRID-*` · `GRID-TAP-*` · `LEAD-ACID-BANK-*` · `MOTOR-1/2` · `VOLTAIC-BATTERY-TRAY-1` |
| [animals.md](animals.md) | `TOP-BAR-HIVE-3…7` · `SKEP-1/2` · `SPARE-HIVE-1` · `TOP-BAR-SET-SPARE` |
| [food.md](food.md) | Honey · smoked meat and fish · stew jars · oil · vinegar · brined olives · salt · ice · grain and pulse eating stock |
| [seed-vault.md](seed-vault.md) | All elite and select banks · `EMMER-SOW-Y9` · `P-FAVA-Y9` · `HEMP-SEL-Y10` · herb reserves |
| [processing.md](../government/procedures/processing.md) | `MELT-PROTOCOL-2` — a method, never stock |
| [bees.md](../government/procedures/bees.md) | Apiary roster · **`BAIT-BOX` @ row when band open** |
| [goats.md](../government/procedures/goats.md) | Goat roster · lineage · rut/slaughter gates *(d4270)* |

**Dropped, not lost.** Closed batches and spent kits — `ACORN-LEACH-Y6-1` through `Y8-6`, `TRAIL-GRAVEL-KIT-1/4/7`, `KAOLIN-CAND-1/2/4-EAST`, `PORCELAIN-BODY-MIX-3/4/5`, `FELDSPAR-CHIP-SET-1`, `KELP-DRY-STAGING`, `CU-WIRE-STOCK-1`, `WIRE-CU-3`, `EM-COIL-2`, the Y6–Y9 bread bakes, and the d2818–d2830 construction read rows — are journal records, not stock. **`ETHANOL-DEHYD-CONDENSATE-*` per-batch jars** · **`BLEACH-*-Y10-*` per-bottle ledger IDs** consolidated **d4936** → **`ETHANOL-DEHYD-STOCK-1` · `BLEACH-CLEAN-1` · `BLEACH-CHEM-1`**. See the retirement rule in [index.md](index.md).

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
