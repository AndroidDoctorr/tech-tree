# Resources

Fungible stock — measured, drawn down, replaced. Schema and the routing test are in [index.md](index.md).

`| ID | Item | Qty | Where | Made | Last |`

`Made` is blank unless the thing degrades. `Last` is the day the quantity last changed. `×0` means the row is spent but the ID is kept so draws against it still resolve.

## Fuel and char

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`CHAR-LANE`** | Charcoal, oak · green | **~15.3 kg** | Char lane | | d4097 |
| `CHAR-RESERVE-C` | Charcoal reserve | **~5.2 kg** | Store C vault | | d4084 |
| `WOOD-OAK-P5` | Oak, green | **~13.4 kg** @ pile 5 | Pile 5 | | d4100 |
| **`BARREL-5-FERMENT`** | **Ferment barrel · ~25–30 L class · breath bung · food-oil interior · empty** | **1 @ horreum A margin** | **Horreum A margin** | d3895 | d3896 |
| `WOOD-HORNBEAM-GEAR-1` | Hornbeam blank · gear stock · end-grain checked | **~0.24 kg offcut tail** | Craft peg | d3520 | d3551 |
| `SHIVE-FLAX` | Flax shive | **~10.4 kg** | Storage wing | | d3865 |
| `SHIVE-HEMP-Y8` | Hemp shive | **~9.0 kg** | Berm | | d3786 |
| `SLUMGUM-1` | Slumgum · firelighter | ~4 kg | Fire store | | d3265 |

## Clay, stone and aggregate

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CLAY-P1` | Clay, raw · green | **~23.8 kg** | Pile 1 | | d3859 |
| `KAOLIN-M26-WET-1` | Kaolin, Koruhöyük **`M-26`** · wet | **×0** | d3329 | d4008 |
| `QUARTZ-FACE-B` | Quartz, FACE-B | **~50.58 kg** | `STORE-4` | | d3994 |
| `QUARTZ-GLASS-FINE-Y13-1` | Glass-grade silica fines · triple-skim levigate · **`QUARTZ-FACE-B`** | **~1.22 kg** | Chem porch dry tray | d3990 | d4007 |
| `STONE-DRESS-P4` | Dressing / field stone | ~8.9 kg | Pile 4 north band, ×2 marked sacks | | d3073 |
| `RIPRAP-ARMOUR-1` | Riprap outer armour, angular — surplus after `CAMPUS-BRIDGE-APRON-1` · rounded cobble rejected, it rolls | surplus stack | T-2 face | | d3277 |
| `STONE-FLOOR-P8` | Floor stone | ×0 *(×8 laid in `PAD-1` ring)* | Pile 8 | | d3043 |
| **`FLUORITE-RAW-AKKAYA-Y13-1`** | Fluorite · dressed cob · `M-29` Akkaya | **~14.2 kg** @ pile 4 tray | Pile 4 | | d4110 |
| **`GRAVEL-1`** | Gravel aggregate | **×0 · kit spent** | — | | d4105 |
| `SAND-FILTER-1` | Filter / concrete sand · winter dry queue | **~1.5 kg** | Pile 4 apron | | d4095 |
| `SAND-RIVER-GROG` | River sand / grog | **×0 class** | Fabrica SW margin | | d3608 |
| `POZZ-TUFF-1` | Pozzolan / tuff | **~22.3 kg** @ pile 4 north · **~8 kg stage @ Fabrica** | Pile 4 north band | | d4101 |

## Lime

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CACO3-P7` | Limestone, raw · plus underburnt returns | **~4.4 kg** | Pile 7, camp north face | d3374 | d4093 |
| `QUICKLIME-1` | Quicklime, dry · green · also `LIMELIGHT-1` feedstock | **~0.05 kg** | Lime trough | d3390 | d4101 |
| `BLOCK-CAST-Y10-3280` | Cast block · BC-2 · 90-day break PASS d3370 | ×0 → **`WAGON-GARAGE-1` stem** | d3280 | d3375 |
| **`BLOCK-Y10-DRY-STACK-1`** | BC-2 load-bearing · 90-day cure PASS · shaded stack | **×7 @ `WW-YARD`** | Block yard | d4030 | d4030 |
| `LIME-PUTTY-1` | Lime putty | **~0 kg** | Lime trough | | d4038 |

Quicklime slakes on the air and is the one row here with a real clock — see the keep window in [processing.md](../government/procedures/processing.md).

## Herb seed — dry queue *(not vault)*

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `HERB-SEED-CORI-Y12-1` | Coriander seed crop · designated ×6 · **winnow d3688** | **×0** *(→ vault)* | — | d3678 | d3688 |
| `HERB-SEED-ALLIUM-Y12-1` | Allium seed crop · designated ×4 · **winnow d3688** | **×0** *(→ vault)* | — | d3678 | d3688 |
| `HERB-SEED-THYME-Y12-1` | Thyme seed · mother-row tops · **winnow d3688** | **×0** *(→ vault)* | — | d3678 | d3688 |

Thresh and winnow move clean seed to [seed-vault.md](seed-vault.md); until then **no ark**.

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
| `KAOLIN-SLIP-M26-1` | Kaolin slip · #2-class bulk — **`M-26` wash** | **~21.3 kg** | Chem porch jar | d3331 | d4008 |
| **`CATALYST-KAOLIN-CALCINE-Y13-1`** | Calcined M26 kaolin · metakaolin / alumina class · dehydration catalyst reserve | **~40 g** | Chem porch catalyst peg | d3956 | d3956 |
| `KAOLIN-SLIP-M26-BEST-1` | Kaolin slip · best cut — **`M-26`** | **~1.19 kg** | Chem porch jar | d3331 | d4008 |
| `MONT-M26-TRACE-1` | Montmorillonite trace · **`M-26` wash · field rank only** | **~0.52 kg wet** | Chem porch separate peg | d3331 | d3941 |
| `KAOLIN-SLIP-5` | Kaolin slip · #2-class bulk — CAND-4-EAST wash | **~0.03 kg** | Chem porch jar | | d3821 |
| `KAOLIN-SLIP-4` | Kaolin slip · ★ **best** — CAND-4 wash | **×0 class** | Chem porch jar | | d3761 |
| `KAOLIN-SLIP-2` | Kaolin slip · rank #2 · **lane primary** | **~0.02 kg** | Chem porch jar | | d3721 |
| `KAOLIN-SLIP-1` | Kaolin slip · #2-class bulk — CAND-1 wash | **×0 class** | Chem porch jar | | d3761 |
| `KAOLIN-CAND-3S` | Kaolin candidate 3S · wet linen, secondary hold | **×0** — consumed d3859 TF wash | Chem porch dry queue | | d3859 |
| `MONT-CAND-1` | Montmorillonite candidate · unwashed, mont rank only | ~2.5 kg wet gross | Chem porch separate peg | | d2527 |

## Brick and tile

> **TR vs TF** — **TR** = curved roof half-pipe · `CLAY-P1` · roof face · **hold only — shingle runway supersedes new TR**. **TF** = flat square · washed kaolin · floor face / marver · **fume hood + floor class**. See [TILE-TR-TF-FUME-CABINET-Y12.md](../journal/retcons/TILE-TR-TF-FUME-CABINET-Y12.md).

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BRICK-GREEN-P3` | Green brick | ×0 | Pile 3 | | d3110 |
| `BRICK-FIRED-B` | Fired brick, stackable · amber | **~179 @ kiln B** · **×8 @ `CAVE-3` mouth** | Kiln B / cave | | d3727 |
| `TILE-TR` | **Roof tile (TR)**, fired · curved semi-cylinder · hold | **×54** *(+×19 laid Fabrica SW roof · ×3 grog · **no new press Y12**)* | Rack south | | d3843 |
| `TILE-TF` | **Floor tile (TF)**, fired · flat square · kaolin body | **×61** @ rack north *(×108 laid hub · **−×22 fume d3841/3843** · +×31 d3859 · +×16 d3870 · +×16 d4009 · **−×2 rebar chair d4023**)* | Rack north | | d4023 |
| `TILE-TF-GREEN` | Floor tile (TF), green · drying queue | **×0** | North sand bed | d3859 | d4009 |
| `CLAY-RANK-REF` | Refractory rank tiles · fired reference set | ×6 | Bench | | d2447 |
| `CRUCIBLE-GROG` | Crucible grog, reclaim | ×0 | Berm | | d2504 |
| `FT-Y8-FLOOR-TILE` | TF · Y8 SLIP batch · fired PASS · ⚠ FT-Y8-4 · FT-Y8-12 marginal | **×0** @ bench *(−×16 culina checker · −×9 fume d3841)* | — | d2593 | d3841 |
| `PORCELAIN-CHIP-SET-1` | Porcelain chip reference set · stoneware rank | ×10 | `CRAFT-CABINET-2` archive drawer | | d3073 |
| `FORSTERITE-BRICK-TRIAL-Y12-1` | Fired binder ladder · F05 / F10 / F15 / R10 · tested d3620 | **×8 archive** | `CRAFT-CABINET-2` drawer | d3585 | d3620 |
| `FORSTERITE-BRICK-STD-Y12-1` | Production recipe · **90% graded forsterite grog · 10% dry kaolin** · F10 winner | **×90 FIRED** | Sand bank + stack | d3620 | d3657 |
| `TC-SLEEVE-SET-1` | Thermocouple electrical ceramic · **18 × 11 mm segments · twin 2 mm bore · 3 mm web** | **×3 spare FIRED** | Instrument peg tray | d3587 | d3743 |
| **`TC-SLEEVE-SET-2`** | Thermocouple sleeve batch · rev 1.1 · **`TC-PROBE-2` spare** | **×20 GREEN @ north board** | Slatted dry board | d3839 | d3839 |
| `TC-COLD-BLOCK-1` | Thermocouple isothermal terminal block | **×0** — on **`TC-PROBE-1`** | — | d3587 | d3743 |
| **`TC-COLD-BLOCK-2`** | Thermocouple isothermal terminal block · **`TC-PROBE-2` spare** | **×1 GREEN @ north board** | Slatted dry board | d3839 | d3839 |
| **`TC-PROBE-1`** | Iron–constantan probe · **306 mm protected · 8 mm hot junction · cal `TC-CAL-LADDER-Y12-1`** | **×1 LIVE** | Instrument tray + ice jar | d3743 | d3743 |

## Ore

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `O-1-MALACHITE` | Malachite, Y10 · wire-grade carbonate · *(+~0.48 kg tail at slag dish)* | **~9.65 kg** | Pile 4 | | d3983 |
| `CINNABAR-1` | Cinnabar, HgS · ☠ **isolated storage** | **~44.6 kg** | v1 chem, isolated | | d3754 |
| `GALENA-1` | Galena-class lead ore | **~9.0 kg** | Forge staging | | d3997 |
| `H-11-HEMATITE` | Hematite | **~45.0 kg @ pile 4** | Pile 4 | | d4084 |
| **`ST-SPR-BUTTON-Y13-2`** | Spring steel button · **`HEAT-Y13-014`–`016` · leaf packs drawn d4065** | **~90 g tail @ chill tray** | Chill tray | d4061 | d4065 |
| **`ST-SPR-STRIP-Y13-1`** | Spring steel strip · **`HEAT-Y13-013` · cert sample** | **×0 spent → leaf packs d4065** | — | d3914 | d4065 |
| **`ST-STR-BAR-Y13-1`** | Structural steel bar · **`HEAT-Y13-012` · `ASSAY-Y13-002` ~0.24 % C · `ST-STR-1` cert** | **~3 g tail @ dry tray** | Dry tray | d3911 | d3976 |
| `M-22-MAGNETITE-1` | Magnetite · **`M-22-TALUS-S1` strip** · dressed @ face | **~17.25 kg** | Pile 4 tray | d3618 | d3903 |
| `SPH-1` | Sphalerite | ~6.12 kg | — | | d2987 |
| `AZURITE-1` | Azurite · smelts as copper **or** grinds as blue pigment | **~0.21 kg** *(pigment reserve)* | Chem porch | | d3931 |
| `CU-SLAG-Y10` | Copper slag · re-charge stock, still holds metal | ~3.8 kg | Slag dish | | d3230 |
| `CASSITERITE-CONC` | Cassiterite concentrate · fines-heavy, deferred | ~0.5 kg | Forge staging tray | | d2933 |
| `PYRITE-KISECIK` | Pyrite, Kisecik fringe · *(+`PYRITE-SPARK-TIN-1` ~22 g at `FK-1`)* | **~0.55 kg** | Ore shelf | | d3983 |
| `CHROMITE-POD-M24-1` | Chromite pod fragment · podiform | ~190 g | Chem porch dry queue | d3338 | d3344 |
| `GARNIERITE-BULK-M24-1` | Garnierite · **ribbon haul `M24-2`** · ☠ **dressed out d3582 — 18% green** | ×0 → split below | — | d3350 | d3582 |
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
| **`FMN-STD-A/B/C`** | Ferromanganese trial charges · sealed jars | **×0** — triplicate spent d3815–3833 | — | d3615 | d3833 |
| ★ `SERPENTINITE-REJECT-M24-1` | Host serpentinite, raw · **M24 dress reject** · forsterite feedstock | **×0** | `ORE-BAY-1` kerb empty | d3582 | d3634 |
| `SERPENTINITE-RAW-KISECIK-Y12-1` | Kisecik ophiolite serpentinite · raw · **forsterite feed** · dressed **`K-SERP-RIDGE-1` d3638 · d3648 · d3754 · d3982** | **~39.2 kg** | `ORE-BAY-1` kerb | d3638 | d3988 |
| ★★ `FORSTERITE-GROG-1` | **Dead-burned serpentinite** · buff-grey · rings · no slake | **~2.9 kg** | Kiln yard, covered | d3583 | d3988 |
| `FORSTERITE-BRICK-Y12-1` | Production forsterite brick · **`FORSTERITE-BRICK-STD-Y12-1`** · **~230×115×45 mm** | **×20 FIRED bank** · **×0 GREEN** · **×62 @ `MUFFLE-1-SHELL-1`** *(×107 @ `FURNACE-2` shell · ×2 @ lift plugs)* | South court | d3621 | d4001 |
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
| `CU-BAR-Y10-1` | Copper bar · poled, wire-grade | **~4 g tail** | Chill tray | | d3931 |
| **`EC-1-WIRE-SAMPLE-SET-Y13-1`** | EC-1 gauge masters · **×4 @ 10 m · 0.9/0.65/0.5/0.3 mm** · **14 °C R filed** | **1 set** | **`REF-SHELF-1`** · not production | d3889 | d3889 |
| `IRON-BLOOM-1` | Bloomery sponge · GREEN | **~225 g tail @ mount** | `FORGE-D` | Y12 | d4084 |
| **`REBAR-STD-Y13-1`** | Wrought rebar reference · **~10.2 mm square · twisted · ~480 mm** · BC-2-REBAR | **~300 g** | `FORGE-D` peg | d4021 | d4022 |
| **`REBAR-BAR-Y13-1`** | Production rebar · twisted · **~10.1 mm · ~560 mm** · hooks @ pour | **~410 g** | Forge peg rack | d4025 | d4025 |
| **`REBAR-BAR-Y13-2`** | Production rebar · twisted · **~10.0 mm · ~555 mm** · hooks @ pour | **~405 g** | Forge peg rack | d4025 | d4025 |
| **`REBAR-BAR-Y13-3`** | Production rebar · twisted · **~10.1 mm · ~565 mm** · hooks @ pour | **~415 g** | Forge peg rack | d4029 | d4029 |
| **`REBAR-BAR-Y13-4`** | Production rebar · twisted · **~10.0 mm · ~550 mm** · hooks @ pour | **~400 g** | Forge peg rack | d4029 | d4029 |
| **`REBAR-BAR-Y13-5`** | Production rebar · twisted · **~10.0 mm · ~558 mm** · hooks @ pour | **~408 g** | Forge peg rack | d4084 | d4084 |
| **`REBAR-BAR-Y13-6`** | Production rebar · twisted · **~10.1 mm · ~562 mm** · hooks @ pour | **~412 g** | Forge peg rack | d4084 | d4084 |
| **`REBAR-SQUARE-CONTROL-Y13-1`** | Wrought square control · **spent on cover mocks** | **×0** | — | d4021 | d4023 |
| **`REBAR-HOOK-REF-Y13-1`** | Hook termination template · **90° + ~40 mm return · ×2** | **×2 @ peg** | `FORGE-D` | d4022 | d4022 |
| **`REBAR-LAP-MOCK-Y13-1`** | Lap splice mock · break **PASS d4029** | **×0 · spent** | — | d4022 | d4029 |
| **`REBAR-BOND-TWIST-Y13-1`** | Bond cylinder · twist · break **PASS d4029** | **×0 · spent** | — | d4022 | d4029 |
| **`REBAR-BOND-PLAIN-Y13-1`** | Bond cylinder · plain · **control FAIL vs twist d4029** | **×0 · spent** | — | d4022 | d4029 |
| **`REBAR-COVER-CHAIR-Y13-1`** | Cover mock · chair · break **PASS d4029** | **×0 · spent** | — | d4023 | d4029 |
| **`REBAR-COVER-DIRT-Y13-1`** | Cover mock · dirt · **underside fail d4029** | **×0 · spent** | — | d4023 | d4029 |
| `CS-BAR-Y12-1` | Carbon steel bar · hardened + tempered | **~847 g** | Forge peg | Y12 | d3571 |
| `CS-BAR-Y12-2` | Carbon steel bar · hardened + tempered | **~848 g** | Forge peg | Y12 | d3573 |
| `CAST-IRON-BUTTON-Y12-1` | Cast iron button · **`FURNACE-2` trial 1** · combustion ref d3744 | **~167 g** | Chill tray | d3728 | d3744 |
| `CAST-IRON-BUTTON-Y12-2` | Cast iron button · **`HEAT-Y12-001`** · **~3.5 % C** | **~163 g** *(chip)* | Chill tray | d3802 | d3803 |
| `CAST-IRON-BUTTON-Y12-3` | Cast iron button · **`HEAT-Y12-002`** · **~3.5 % C** | **~165 g** *(chip)* | Chill tray | d3803 | d3804 |
| `CAST-IRON-BUTTON-Y12-4` | Cast iron button · **`HEAT-Y12-003`** · **~3.5 % C PASS** | **~164 g** *(chip)* | Chill tray | d3804 | d3812 |
| `CAST-IRON-BUTTON-Y12-5` | Cast iron button · **`HEAT-Y12-004`** · **~3.5 % C PASS** | **~163 g** *(chip)* | Chill tray | d3812 | d3813 |
| `CAST-IRON-BUTTON-Y12-6` | Cast iron button · **`HEAT-Y12-005`** · coupon only | **~164 g** *(chip)* | Chill tray | d3814 | d3815 |
| **`MAG-STEEL-Y13-ROD-1`** | Magnet steel pole rod · **`HEAT-Y13-009` · ~1.0 % C · lift ~44 mm** | **~71 g @ `MOTOR-1-MAG-STACK-1`** | Chem porch bench east | d3900 | d3957 |
| **`MAG-STEEL-Y13-ROD-2`** | Magnet steel pole rod · **`HEAT-Y13-010` · lift ~43 mm** | **~71 g @ `MOTOR-1-MAG-STACK-1`** | Chem porch bench east | d3903 | d3957 |
| **`MAG-STEEL-Y13-ROD-3`** | Magnet steel pole rod · **`HEAT-Y13-011` · lift ~44 mm** | **~72 g spare** | Dry tray · chem porch | d3903 | d3903 |
| **`FMN-BUTTON-Y12-1`** | Ferromanganese trial button · **`HEAT-Y12-006` · `FMN-STD-A`** | **×0 spent** *(composite **`HEAT-Y13-016` d4063)* | — | d3815 | d4063 |
| **`FMN-BUTTON-Y12-2`** | Ferromanganese trial button · **`HEAT-Y12-007` · `FMN-STD-B`** | **×0 spent** *(composite **`HEAT-Y13-016` d4063)* | — | d3829 | d4063 |
| **`FMN-BUTTON-Y12-3`** | Ferromanganese trial button · **`HEAT-Y12-008` · `FMN-STD-C`** | **×0 spent** *(−~65 g d4062 · composite d4063)* | — | d3833 | d4063 |
| **`CONSTANTAN-STD-Y12-1`** | Constantan std stub · run D tail · reproduce from bridge label | **~3.1 g** | Instrument tray | d3734 | d3735 |
| **`CONSTANTAN-BATCH-Y12-1`** | Constantan repro · Run D recipe · run 1 | **×0 → `TC-CONST-LEG-2`** | — | d3834 | d3835 |
| **`CONSTANTAN-BATCH-Y12-2`** | Constantan repro · Run D recipe · run 2 | **~7.7 g** | Chill tray | d3834 | d3834 |
| **`CONSTANTAN-BATCH-Y12-3`** | Constantan repro · Run D recipe · run 3 | **~7.8 g** | Chill tray | d3835 | d3835 |
| **`TC-CONST-LEG-2`** | Constantan TC leg · **Ø0.50 mm · 450 + ~118 mm** · repro batch 1 | coiled @ vault dry peg | d3835 | d3835 |
| **`TC-IRON-LEG-2`** | Iron TC leg · **Ø0.50 mm · 450 + ~120 mm** · spare pair | coiled @ vault dry peg | d3839 | d3839 |
| **`TC-CONST-LEG-1`** | *(integrated **`TC-PROBE-1` d3743)* | — | — | d3735 | d3743 |
| **`TC-IRON-LEG-1`** | *(integrated **`TC-PROBE-1` d3743)* | — | — | d3736 | d3743 |
| `CS-TEST-COUPON-Y12-1` | Carbon steel test coupon · fracture reference | **~18 g** | Bench vial | Y12 | d3571 |
| `CS-TEST-COUPON-Y12-2` | Carbon steel test coupon · bar-2 fracture | **~17 g** | Bench vial | Y12 | d3573 |
| `SN-BANK` | Tin | **~1.12 kg** | — | | d3743 |
| `ZNO-CALCINE` | Zinc oxide calcine | **~746 g** | — | | d3956 |
| `ZN-METAL-1` | Zinc, prill tail | **~78 g** | Chem-lab lidded tray | | d3743 |
| `HG-METAL-1` | Mercury · ☠ **not food** · isolated | ~118 g | Purple lidded jar, v1 chem | | d3013 |
| `BRONZE-STOCK` | Bronze, sprue tail · red | **×0** | Chill tray | | d3545 |
| **`LEAD-ACID-PILOT-1`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-1`** | **1 jar** | Parallel chem tray · **`SW-STORAGE-TIE-1`** | d3883 | d3971 |
| **`LEAD-ACID-PILOT-2`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-2`** | **1 jar** | Parallel chem tray · **`SW-STORAGE-TIE-1`** | d3887 | d3971 |
| **`LEAD-ACID-PILOT-3`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-3`** | **1 jar** | Parallel chem tray B · **`SW-STORAGE-TIE-2`** | d3999 | d4009 |
| **`LEAD-ACID-PILOT-4`** | Lead-acid pilot cell · **formation ✓ CLOSED · ~54% SOC · on gen bus** · **`LEAD-ACID-JAR-Y13-4`** | **1 jar** | Parallel chem tray B · **`SW-STORAGE-TIE-2`** | d3999 | d4009 |
| **`PB-TRIM-Y13-3`** | Lead trim / slug · remelt reserve | **~71 g** | Forge jar | d3997 | d3997 |
| `PB-METAL` | Lead, general tail | **×0** | Forge jar | | d3497 |
| `BRASS-STOCK` | Brass stock · cementation ingot · component tail | **~65 g @ chill tray** | Chill tray | d3500 | d3976 |
| `BRASS-BUCKLE-Y12-1` | Brass frame buckle · **`BELT-WIDTH-STD-Y12-1` 22.0 mm gap** | **×0 → `YULE-BELT-Y12-1`** | — | d3801 | d3828 |
| `NAIL-BRASS` | Brass nails | ×4 | `WOOD-CRATE-5` forge fastener | | d3103 |
| `NAIL-IRON` | Iron nails | **×29 @ bench peg tray** *(×3 cave crate tail)* | `FORGE-D` bench | d3514 | d4101 |
| `WAGON-GARAGE-STRAP-1` | Iron strap, pierced · garage tie | ×0 → frame | `WAGON-GARAGE-1` | d3377 | d3378 |
| `HINGE-BRASS-REPAIR` | Brass strap hinges, repair pool | ×0 → **`WAGON-GARAGE-1` doors** | Horreum peg tray | | d3515 |
| `WOOD-SCREW-STOCK-1` | Wood screws · marginal | **×0** | Bench tray | | d3841 |

## Copper wire

The wire bank is tracked by **gauge**, because gauge is what decides whether a length is usable for a given job — 0.3 mm will not carry a cell and 1.6 mm will not wind an armature.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CU-WIRE-Y10-3` | 0.3 mm · electrowon, tough-pitch, poled — **drew without a break** | **~29.8 m @ rack** · **~8 m @ cave spool** *(−~1.1 m bank B tails d3999)* | Wire rack / cave | d3261 | d3999 |
| `WIRE-CU-GEN2-1` | 0.9 mm gen-2 · bare · file-bright · feeder tail | **~6.5 m @ chem peg** *(−~2.5 m bank B tie d4009)* | Chem peg | | d4009 |
| `WIRE-CU-4` | 1.6 mm · lane B coil, hold | ~14 m | Chem porch | | d1982 |
| `CU-WIRE-Y10-COATED` | 0.9 mm coated · wax + rosin ×2 · paper · leads and tails only | **~8.6 m** | Chem peg | d3245 | d3971 |
| `CU-WIRE-Y10-4` | ★ **best conductivity drawn to date** — off the glass-cover melt | — | Wire rack | d3266 | d3266 |
| `TC-GALV-LEAD-PAIR-1` | Matched galvanometer copper pair · **2 × 2.50 m · one turn / 20 mm · served** | ×1 on **`TC-PROBE-1`** | Instrument peg | d3587 | d3587 |
| **`TC-GALV-LEAD-PAIR-2`** | Matched galvanometer copper pair · **`TC-PROBE-2` spare** | ×1 @ instrument peg | d3839 | d3839 |
| `TC-BINDING-POST-1` | Brass BN-06 binding posts · 24 mm · Ø1.5 mm lead hole | ×2 on **`TC-PROBE-1`** | d3587 | d3743 |
| **`TC-BINDING-POST-2`** | Brass BN-06 binding posts · **`TC-PROBE-2` spare** | ×2 + washers / nuts @ peg | d3839 | d3839 |

⚠ The armature's 95 m was unwound and redrawn to 0.65 mm at d3267 — it is now `ARMATURE-2` in [infrastructure.md](infrastructure.md), not wire stock.

## Electrical plate and magnet stock

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ZN-VOLTAIC-PLATES` | Zinc voltaic plates, spare · `VOLTAIC-RESERVE` | ~39 | Storage wing | | d3238 |
| `CU-GEN2-VOLTAIC-PLATES-1` | Copper voltaic plates, spare *(+×8 live in `VOLTAIC-8-CELL-1`, ×1 in `DANIELL-CELL-1`)* | **×18** | Tray | | d3958 |
| `MAG-BOOT-EM` | EM boot rods #9 · #10 · #11 · #13 · #14 · #15 · #17 · #18 — ~168–176 g, ~35–38 mm | ×8 | Dry tray | | d3160 |
| `MAG-BOOT-SPARE-1…4` | Demoted rods, ~27–36 mm solo class | ×4 | Horreum B peg | | d3162 |

Rods #16 and #19 are in `MAG-STACK-2` and #6 rods are in `GEN-WW-1`'s yoke — both in [infrastructure.md](infrastructure.md).

## Glass and chemical

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `GP-Y8-C-LITE` | Glass pane, C-lite · spare, dividered | **×28 spare** *(25…28 tapped d4009 · 21…24 tapped d3994)* | Storage wing N upper shelf | | d4009 |
| `GLASS-CLARITY-A/B/C-3994` | Y13 clarity ladder disks · ~3.4–3.5 mm · labelled | **×3 @ sand bed** | Chem east anneal lane | d3994 | d3994 |
| `KELP-ASH-5` | Soda / kelp ash · refined + coast burn batch | **~517 g** | v1 chem | | d4007 |
| `GLASS-CULLET-BIN-1` | Lab glass cullet · clean return · sorted | **~1.04 kg** | Chem porch bin | | d4007 |
| `LEAD-ACID-JAR-Y13-3` | Lead-acid cell jar · glass · wide mouth · **~418 ml** · **`LEAD-ACID-PILOT-3`** | **→ pilot cell** | Parallel chem tray B | d3995 | d3999 |
| `LEAD-ACID-JAR-Y13-4` | Lead-acid cell jar · glass · wide mouth · **~422 ml** · **`LEAD-ACID-PILOT-4`** | **→ pilot cell** | Parallel chem tray B | d3995 | d3999 |
| `PB-PLATE-NEG-Y13-3` | Lead plate blank · negative · jar #3 | **~105 g** | Forge peg · tagged | d3997 | d3997 |
| `PB-PLATE-POS-Y13-3` | Lead plate blank · positive · jar #3 | **~104 g** | Forge peg · tagged | d3997 | d3997 |
| `PB-PLATE-NEG-Y13-4` | Lead plate blank · negative · jar #4 | **~104 g** | Forge peg · tagged | d3997 | d3997 |
| `PB-PLATE-POS-Y13-4` | Lead plate blank · positive · jar #4 | **~105 g** | Forge peg · tagged | d3997 | d3997 |
| `GLASS-TINT-LENS-Y10-D` | Tint lens spare | **`SUNGLASS-LENS-Y10-3` lapped · tint D matched · spare peg** | Spare peg | d3430 | d3517 |
| `PAPER-SHEET-Y9` | Paper, flax · `SHEET-Y9-FLAX-29…32` · coil interleaving stock | ~9 sheets | Chem-lab rack | | d3503 |
| `PAPER-SHEET-Y10-FLAX-1…3` | Paper, flax · roof R&D pulls | ×2 drying @ rack · ×1 on panel | Chem-lab rack | d3472 | d3472 |
| `ROOF-R&D-PANEL-1` | Roof coupon deck · coupons **A0–F2** | **11 coupons** @ chem porch south lean · **rain read d3873 F2 PASS** | Chem porch | d3472 | d3873 |
| `BITUMEN-ROOF-TRIAL-1` | Bitumen · roof-grade trial crock · skimmed bulk | **~0.95 kg** | Chem porch | d3472 | d3869 |
| `SAND-ROOF-FINE-1` | Sand, screened fine · roof surfacing | **~700 g** | Chem porch jar | d3472 | d3869 |

## Fibre, cordage and hide

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FLAX-TOW-BANK` | Flax tow | **~159 g** | Wing shelf | | d3865 |
| `FLAX-THREAD-COVER-Y10-1` | Flax thread · wagon cover inner | ~55 m tail | Craft wing peg | d3401 | d3406 |
| `FLAX-THREAD-SHINGLE-Y10-1` | Flax thread · roof / shingle mat bank | **~13 m tail** | Craft wing peg | d3505 | d3868 |
| `ROOF-SHINGLE-FINISHED-Y12-1` | Flax shingle strips · impregnated · sanded · ~10 × 18 cm | **×7** | Chem porch peg | d3869 | d3869 |
| `FLAX-THREAD-BANK` | Flax thread | ~13 m | Craft cabinet 2 | | d2565 |
| `HEMP-LINE-26` | Hemp line | ×0 tail | `WOOD-CRATE-6` fibre | | d3513 |
| `HEMP-LINE-Y12-1` | Hemp line · Bed A Y12 · **`P-RETT-33`** | **×0** *(spun d3787)* | — | d3786 | d3787 |
| **`FLAX-LINE-Y12-1`** | Flax line · field Y12 · **`P-RETT-34` heckle** | **~1.55 kg** @ `WOOD-CRATE-6` fibre | Storage wing | d3865 | d3977 |
| **`THISTLE-HEAD-DRIED-Y13-1`** | Cardoon-type heads · full-flower cut · rennet stock | **×9 @ horreum herb peg** | Horreum | d4074 | d4074 |
| **`FLAX-WILD-GREEN-Y13-L1`** | Wild flax lap 1 · **`P-RETT-35` pulled** | **~3.7 kg @ W-1 dry queue** | Ditch W | d4075 | d4088 |
| **`FLAX-THREAD-Y13-1`** | Flax thread · motor-assist spin d3977 | **~22 m** @ craft peg | Craft wing peg | d3977 | d3977 |
| **`HEMP-THREAD-Y12-1`** | Hemp thread · Bed A Y12 spin | **~315 m** | Craft wing peg | d3787 | d3789 |
| `ROPE-HEMP-Y12-1` | Hemp rope · 3-strand · Y12 yarn · even lay · ⚑ break test + ÷6 cert defer | **~48 m** | WW peg | d3788 | d3789 |
| `HEMP-THREAD-Y10-1` | Hemp thread · cover weft | ~75 m | Craft wing peg | d3382 | d3400 |
| `WAGON-V2-COVER-HEMP-FLAX-1` | Wagon cover · hemp shell + flax liner · air gap · **outer oilcloth d3408** · mounted Norima | ✓ CLOSED d3407 | `WAGON-V2-COVER-ARCH-1` | d3400 | d3408 |
| `HEMP-TOW-BANK` | Hemp tow | **~219 g** | Storage wing tow bag | | d3786 |
| `ROPE-HEMP-STOCK-2` | Hemp rope · reserve / lash · **cover weave band** | **~23 m** | WW peg | | d3591 |
| `ROPE-HEMP-HOME` | Hemp rope · good lay, **reserve for load work** | ~6.4 m | Pile 2 | d3221 | d3221 |
| `ROPE-HEMP-Y10` | Hemp rope · ⚠ **lash class only** — uneven lay, soft spots, never under load | ~28 m | Pile 2 | d3226 | d3226 |
| `ROPE-1` | 3-strand hemp · ⚠ **lashing grade only** — uneven lay | ~24 m | — | d3255 | d3255 |
| `ROPE-2` | 3-strand hemp · ★ **certified: loaded haul and lashing at breaking ÷ 6, spliced not knotted** · ⚠ **not life-bearing** | ~23 m | — | d3255 | d3264 |
| `ANTLER-SHED` | Antler, cast and hard · beats bone for anything taking a blow | ×6 | Craft wing | | d3269 |
| `CLOTH-WAGON-COVER` | Wagon cover cloth, tail stock | ~2.00 kg | `CART-YARD` south peg row | | d3472 |
| `THREAD-STOCK-2` | Thread · *coil serving — leads and crossovers only* | **~127 m** | Craft wing peg | | d3963 |
| `THREAD-1` | Thread, general | ~307 m | — | | d3091 |
| `VENT-BELT-ROPE` | Rope, vent belt | ~123 m | — | | d1970 |
| `EXPED-ROPE` | Hemp rope · D-27 salvage | ~72 m | Cart peg | | d2945 |
| `FLAX-SHIVE-Y8-21` | Flax shive · **paper grade** | **~1.59 kg** | Storage wing | Y8 | d3985 |
| `FEATHER-BAG` | Feather, bag | ~71 g | — | | d3509 |
| `LAB-LINEN-STOCK-1` | Lab linen — filters ×8 · jar wraps ×4 · voltaic separators ×19 · **`LA-SEP-RESERVE-Y13-1` ×1** · wipes ×9 · spill reserve ×4 | — | `CHEM-SPILL-PEG-1` | | d3999 |
| `P-FLAX-LINE-Y8-1` | Flax line, Y8 · `P-RETT-23` break/heckle | ~1.03 kg | WW peg | Y8 | d3135 |

## Hide, leather and bone

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `DEER-HIDE-1` | Deer hide, **tanned** | **~0.24 m²** | Horreum B `LEATHER-STOCK-PEG-1` | | d3828 |
| **`YULE-BELT-Y12-1`** | Deer belt · **`BELT-WIDTH-STD-Y12-1` 22.0 mm** · **`BRASS-BUCKLE-Y12-1`** · gift wrap | **~1.05 m** | Vestiarium Yule shelf | d3828 | d3828 |
| `SINEW-DRY` | Sinew, dry | **~14 g** | Bench | | d3828 |
| **`DEER-HIDE-RAW-Y12-1`** | Red deer hide · salted · **Yule belt / tan queue** | **×0 → pit** | — | d3795 | d3796 |
| `GOAT-HIDE-A03-2` | Goat hide, reserve · flap tail | **~0.07 m²** | Horreum B | | d3655 |
| `HIDE-SCRAP` | Hide scrap, tail | **~0.09 m²** | — | | d3655 |
| `WEATHER-STRIP-LEATHER-1` | Weather strip, ~25 mm | ~4.6 m | — | | d3167 |
| `MACHINE-BELT-LEATHER-KIT-1` | Machine belt stock — WW · drill · trip tail | — | `BELT` peg | | d3052 |
| `TRAIL-GEAR-LEATHER-1` | Belt v2 blank · waterskin patch · lash tabs ×4 | — | Vestiarium trail peg | | d2964 |
| `DEER-BONES` | Deer bone · bone-ash feedstock | ×0 — *burnt d3309* | Horreum tool peg | | d3309 |
| **`DEER-BONE-Y12-1`** | Red deer bone · **`DEER-BUTCHER-Y12-3796`** | **~11 kg** | **`BONE-BANK-1`** peg | d3796 | d3796 |
| `GOAT-BONES` | Goat bone · bone-ash feedstock | ×0 — *burnt d3309* | Horreum tool peg | | d3309 |
| ✓ `BONE-ASH-1` | **Bone ash, white, calcined** · ★ **~38 cupels · ~2 passes through `GALENA-1`** | **~3.92 kg @ porch** · **~0.5 kg @ cave** | Chem porch / cave | d3309 | d3997 |

> ☠ ★★★ **THE MIDDEN DOES NOT GIVE IT BACK** *(d3309)*. *Nine years of it forked over for ~2.8 kg of usable fragment — weathered soft, gnawed, trodden into the ash, the small bones gone entirely.* ★★★ **It is not lost the way a mislaid tool is lost. It is GONE.** ★★ *The other half of d3303: the clocks ran while I was not reading them, and they do not run backwards.*

> ★★★ **`OXIDISING-COOL` — CALCINE ON THE COOLDOWN, NEVER ON THE CLIMB** *(d3309)*. ☠ **A stoked kiln is REDUCING, and carbon in a cupel reduces litharge straight back to lead** — *the exact reaction the hearth exists to run the other way.* ★★★ **Stop stoking, damper wide, trays shallow and high in the chamber: a kiln at ~800 °C full of moving air is a free oxidising furnace** — ☠ **and I threw those hours away after every firing for nine years.** ✓ *The soak burns midden charcoal out as a side effect.* ★ **Bone ash must be WHITE — grey means carbon, and carbon means no silver.**

> ☠ ★★★ **`BONE-BANK-1` opened d3297 — bone is the rate limit on SILVER, not the hearth.** *A cupel is a reagent consumed every run; ~4.7 kg of bone is ~3 kg of ash is ~20 cupels is ONE pass through `GALENA-1`.* ⚑ **Retain every bone from every butchery and every kitchen pot, dried, on the Horreum peg** — ☠ *nine years of it went on the midden.*
> ✓ ★★ **Used cupels are BANKED ORE, not waste** — *lead-soaked, richer than anything dug.* **They go in the kerbed galena bay at `ORE-BAY-1`.**
| `GOAT-HORN-BILLIE` | Goat horn, remnant | ~65 g | `WORKBENCH` peg | | d3015 |

### `TAN-DEER-Y12-1`

**✓ CLOSED d3822** — strap cut **`LEATHER-BELT-STRAP-Y12-1`** · hide tail **`DEER-HIDE-TANNED-Y12-1`**.

### `TAN-DEER-Y10-1` — frame hold

**Pulled d3796** for single-pit priority · **rung 2 hold** @ Horreum B frame · defer *(backup leather · not Yule strap)*.

☠ **Strong liquor on a raw hide case-hardens it.** The ladder is the procedure, not a refinement of it.

Rope is here rather than in tools because it is measured and consumed. A rope rigged into a fixed installation belongs to that installation's entry — `CAVE-3-FIXED-LINE-1` is in [infrastructure.md](infrastructure.md), not this table.

★★ **Grade is the row, not a note.** A length of rope at lashing grade and a length certified for loaded haul are different materials that happen to look identical, so the grade rides in the item name where a grep cannot miss it. `ROPE-2` carries its first real working load on the record — ~130 kg of basalt over 14 km, clean. Working load is **breaking ÷ 6**, a knot costs another third, and shock multiplies enormously. The measured breaking load came from deliberately destroying a length and is written up as doctrine, not held as stock.

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
| `MADDER-ROOT-DRY` | Madder root, dry · merged `MADDER-DRY-V1` | **~317 g** | Chem shelf | | d3510 |
| `WOAD-RESERVE` | Woad, dry | ~385 g | Storage wing dye shelf | | d3351 |
| `WOAD-LEAF-Y10-1` | Woad leaves, fresh · **window pull 1** | ×0 spent | — | d3345 | d3351 |
| `PRUSSIAN-BLUE-1` | Prussian blue pigment · ☠ **not food** | ~24 g | Craft cabinet 2 pigment shelf | | d3021 |
| `GREEN-VITRIOL` | Green vitriol crystals · tail | **×0 spent** | Reagent shelf | | d3998 |

Madder needs an alum mordant. Woad does not — it is a vat dye and fixes mechanically. See `WOAD-VAT` in [processing.md](../government/procedures/processing.md).

## Mineral and salt

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `M-14-SULFUR` | Sulfur · ~15.6 kg block plus ~88 g flour | **~15.67 kg** | — | | d3875 |
| `M-11-ALUM` | Alum, crude | **~1.38 kg** | — | | d3869 |
| `M-12-NITER` | Niter crystal | **~360 g @ chem** · **~100 g @ `CAVE-RECOVERY-CRATE-1`** | Dry jar / cave vial | d3424 | d3875 |
| `BLEACH-CLEAN-Y10-1` | Hypochlorite bleach · dilute cleaning stock | ~220 ml | `P-LAB-BLEACH-BOTTLE-1` | d3454 | d3456 |
| `BLEACH-CLEAN-Y10-2` | Hypochlorite bleach · dilute cleaning stock | ~220 ml | `P-LAB-BLEACH-BOTTLE-2` | d3456 | d3456 |
| `BLEACH-CLEAN-Y10-3` | Hypochlorite bleach · dilute cleaning stock · spare | ~220 ml | `P-LAB-BLEACH-BOTTLE-5` | d3456 | d3456 |
| `BLEACH-CHEM-Y10-1` | Hypochlorite bleach · concentrated chem stock | ~95 ml | `P-LAB-BLEACH-BOTTLE-3` | d3454 | d3454 |
| `BLEACH-CHEM-Y10-2` | Hypochlorite bleach · concentrated chem stock | ~95 ml | `P-LAB-BLEACH-BOTTLE-4` | d3456 | d3456 |
| `BLEACH-CHEM-Y10-3` | Hypochlorite bleach · concentrated chem stock · spare | ~95 ml | `P-LAB-BLEACH-BOTTLE-6` | d3456 | d3456 |
| `QUARTZ-FRIT` | Quartz frit | ~40 g | Vial `G-FRIT` | | d3332 |

`BITTER-SALT-1` is the sulfate of an earth that is **not lime** — lime water precipitates it, hepar confirms sulfate, and a clean hydrogen flame rules out soda.

## Gypsum and plaster

The Samandağ face turned a one-off haul into a bank. Grades are not interchangeable and the row names say which is which.

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| ✓ ★★★ `ACID-VITRIOL-1` | **OIL OF VITRIOL, strong** · ★★ **~1.8× the weight of water** · ⚠ **chars on contact** | **×0 · empty** | `ACID-BOTTLE-1` · chem porch | d3317 | d3886 |
| `ACID-VITRIOL-2` | Oil of vitriol, strong · batch 2 · `RETORT-B` compare run | **×0 · empty** | Spare narrow-neck · chem porch | d3335 | d3886 |
| `ACID-VITRIOL-3` | Oil of vitriol, strong · **Kisecik middle-cut class** | **~7 ml tail** | `P-LAB-ACID-BOTTLE-7` · isolated chem shelf | d3876 | d3998 |
| `LEAD-ACID-ELECTROLYTE-Y13-3` | Dilute H₂SO₄ · **~1.24 SG** · in **`LEAD-ACID-PILOT-3`** | **→ cell** | Parallel chem tray B | d3998 | d3999 |
| `LEAD-ACID-ELECTROLYTE-Y13-4` | Dilute H₂SO₄ · **~1.24 SG** · in **`LEAD-ACID-PILOT-4`** | **→ cell** | Parallel chem tray B | d3998 | d3999 |
| `VITRIOL-FEED-CROCK-1` | Copperas feed · Kisecik-class green · calcined as needed | ~4.2 kg | Chem porch feed crock | d3317 | d3335 |
| **`VITRIOL-LIQUOR-KISECIK-Y12-1`** | Green-vitriol heap liquor · **ARSENIC ASSUMED PRESENT** · ☠ **hood-only · ~400 ml scale PASS d3878** | **~12.8 L** | Isolated chem bay · ×2 lidded stoneware crocks in secondary tray | d3590 | d3878 |
| **`ARS-IMMOBILIZED-LIME-3879`** | Arsenic immobilized · lime precipitate · scorodite-class · ☠ **handle as poison stock** | **~18 g wet cake** | Lidded jar · isolated chem tray · tagged | d3879 | d3879 |
| **`ARS-WASHED-TAIL-3879`** | Iron-rich tail post arsenic wash · colcothar-class · low-As | **~34 g** | Isolated dish · tagged | d3879 | d3879 |
| **`ARS-WORKUP-FILTRATE-3879`** | Spent work-up filtrate · arsenic depleted · weak iron/sulfate | **~395 ml** | `ACID-DREG` crock · tagged | d3879 | d3879 |
| `COLCOTHAR-2` | Raw red ferric residue · `RETORT-B` batch 1 | small dish | Chem porch · unwashed | d3335 | d3335 |
| `COLCOTHAR-1` | Raw red ferric-oxide residue · ✓ **washed and levigated d3318** | ×0 → `ROUGE-FINE-1` + `IRON-OXIDE-PIGMENT-1` | — | d3317 | d3318 |
| ✓ ★★★ `ROUGE-FINE-1` | **Washed, levigated hematite finishing polish** · ★★ **clears final glass haze; does not remove deeper scratches** | small crock | Lap bench | d3318 | d3498 |
| ✓ `IRON-OXIDE-PIGMENT-1` | Clean red hematite, coarser early-settling fraction · **pigment, not trusted on finished glass** | small crock | Pigment shelf | d3318 | d3318 |
| `GYPSUM-CLEAN-POWDER-1` | Gypsum, clean powder · **raw stone — burn small batches on demand** | ~24 kg | Chem porch dry store | | d3225 |
| `GYPSUM-FIELD-GRADE-1` | Gypsum, field grade · gritty · strip-trial stock | ~15.4 kg | Pile 7 | | d3225 |
| `GYP-STOCK-1` | Gypsum, raw · `SC-GYP-SAMANDAG-1` face open | ~14.2 kg | Chem porch peg | | d2823 |
| `PLASTER-CALCINED-1` | Plaster, calcined · ⚠ **stales in damp air — use it** | ~1.43 kg | Working stock | d3225 | d3502 |
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
| `CHARCOAL-FLOUR` | Charcoal flour · one batch thin | ~17 g | Powder jar | | d2911 |
| `GUNPOWDER-MEALED` | Mealed gunpowder · tail | ~3 g | Chem-lab lidded tray | | d2912 |

## Resin, wax and sealant

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BITUMEN-ASI-1` | Bitumen, Asi seeps · 4 crocks, sand-dusted · ⚠ heavy end only | **~39.3 kg** | Chem porch | d3270 | d3983 |
| `BITUMEN-BULK-1` | Bitumen · *(+~1.5 kg chip at cart trial tin)* · ☠ not food | **~6.51 kg** | `BITUMEN-POT-1`, cart yard | | d4046 |
| `CORK-BARK` | Cork bark | ~1.02 kg | — | | d3171 |
| `BEESWAX-V1` | Beeswax · *(plus ~1.04 kg at the wax store — see below)* | **~206 g** | v1 chem · craft cabinet 2 | | d3958 |
| `TALLOW-1` | Tallow | **~50 g** | v1 trough jar | | d3598 |
| `WAX-DROSS-1` | Slumgum / wax dross · fire starter | ~45 g | Hearth | | d3234 |
| `ROSIN-1` | Rosin · pale, brittle | **~88 g** | Chem porch | | d3986 |
| `WAX-ROSIN-COMPOUND-2` | Wire-coating compound | **×0 · pot scraped** | Melt pot | | d3980 |
| `TURPENTINE-1` | Turpentine · ☠ **flammable — cool, away from fire** | **~14 ml** | Stoppered glass, chem rack | d3237 | d3958 |

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
| `WAX-Y10-RENDER-1` | Beeswax, clean cake — render stock | **~554 g** | Wax store | | d3985 |
| `COMB-TO-RENDER` | Comb awaiting render | **×0** — consumed d3600 | — | | d3600 |

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
| [bees.md](../government/procedures/bees.md) | Apiary roster · **`BAIT-BOX` @ row when band open** |

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
| Bitumen bulk | duplicate row removed d3510 | **~7.65 kg** @ `BITUMEN-POT-1` |
| Flax line ~425 g | `WOOD-CRATE-6` (d3075) **and** storage wing N lower shelf (d2709) | `WOOD-CRATE-6` |
