# Campus electric grid (`EC-1`)

Installed **generation · storage · distribution · grid-fed loads** on the HOME campus. Code: [electrical-code-1.md](../government/regulations/electrical-code-1.md) · expansion plan: [ec-1-campus-expansion.md](../plans/ec-1-campus-expansion.md). **Hydraulic prime mover** (`WW-2`, forebay, belt tree) stays in [infrastructure.md](infrastructure.md).

**Fixture IDs** (bulbs, switches, tap boxes, CP-G sockets) also appear in [tools.md](tools.md) — this file is **runs, taps, buses, and install state**.

## Live roster *(d5076)*

| Layer | IDs |
|---|---|
| **Source** | **`GEN-WW-3-M` LIVE d5483** @ `WW-2` wheelhouse · **`GEN-WW-2` harvested d5508** *(Cu/lam → **`GEN-AC-1`**)* · `PEDAL-GEN-1` @ chem porch |
| **Storage bus** | `LEAD-ACID-BANK-Y13-1` · `LEAD-ACID-BANK-Y13-2` *(jars in [resources.md](resources.md))* · `SW-STORAGE-TIE-1/2` |
| **Early DC** | `VOLTAIC-BATTERY-TRAY-1` / `VOLTAIC-8-CELL-1` |
| **Trunks** | `EC-1-GRID-FEEDER-1` chem · `EC-1-GRID-FEEDER-2` Officina · `EC-1-GRID-FEEDER-FABRICA-1` Fabrica · ~~`EC-1-GRID-FEEDER-3`~~ retired |
| **Master switches** | `SW-CHEM-FEEDER-1` · `SW-CRAFT-FEEDER-1` · `SW-FABRICA-FEEDER-1` · `SW-WING-N-FEEDER-1` deprecated OPEN |
| **Taps** | `GRID-TAP-CHEM-1` · `GRID-TAP-CRAFT-1` · `GRID-TAP-CRAFT-2` · `GRID-TAP-WING-N-1` · `GRID-TAP-DOMUS-1` · `GRID-TAP-FABRICA-1` |
| **Tap boxes** | `EC-1-TAP-BOX-STD-1` domus · `STD-2` craft S · `STD-3` wing N · `STD-4` Fabrica |
| **Motors on bus** | `MOTOR-1` @ chem · `MOTOR-2` @ wing N exhaust · **`MOTOR-3` @ forge blast assist** *(✓ d5330)* · **`MOTOR-4` @ wing N blower R&D** *(✓ d5468)* |

### Room lighting roster *(intended install · d5323 close)*

★ **One room lamp knife switch per room** — multi-lamp rooms (**electronics lab · chem · mill · thermae**) use **one switch · both loads on its lugs**. **Feeder/margin masters** (`SW-DOMUS-LIGHT-1`, `SW-CRAFT-FEEDER-1`, `SW-FABRICA-FEEDER-1`, `SW-CHEM-FEEDER-1`) are **not** room switches. **Socket `Y14-n` ≠ spare bulb `CY14-n`.** Cubicula: sockets **9** (west) + **12** (east) — not 9–12.

| Room | Building | Lamps | Reflectors | Room switch | Tap | Commission |
|---|---|---:|---|---|---|---|
| **Electronics lab** *(north work wing)* | Officina | **2** | **2** · `WING-N-PORC-REFLECTOR-*` | **`SW-WING-N-LIGHT-1`** | `GRID-TAP-WING-N-1` | ✓ d4847 |
| **Craft wing** | Officina | **1** | **1** · `FEAST-PORC-REFLECTOR-CY14-5` | **`SW-FEAST-LAMP-1`** | `GRID-TAP-CRAFT-1` | ✓ d4558 |
| **`STORAGE-WING-1`** | Officina | **1** | — | **`SW-OFFICINA-STORAGE-LAMP-1`** | `GRID-TAP-CRAFT-1` | ✓ d5330 |
| **Chem lab** | Fabrica | **2** | **2** · `FEAST-PORC-REFLECTOR-CY14-1/2` | **`SW-CHEM-LAB-LAMP-1`** | `GRID-TAP-CHEM-1` | ✓ d5330 |
| **`MILLHOUSE-2`** | Fabrica | **2** | **2** · `FEAST-PORC-REFLECTOR-CY14-3/4` | **`SW-MILLHOUSE-LAMP-1`** | `GRID-TAP-FABRICA-1` | ✓ d5323 |
| **South court** | Fabrica | **1** | — *(exterior · no reflector)* | **`SW-FABRICA-COURT-LAMP-1`** | `GRID-TAP-FABRICA-1` | ✓ d5329 |
| **`STORE-4`** | Fabrica | **1** | — | **`SW-STORE-4-LAMP-1`** | `GRID-TAP-FABRICA-1` | ✓ d5330 |
| **Culina** | Domus | **1** | **1** · `FEAST-PORC-REFLECTOR-CY14-6` | **`SW-CULINA-LAMP-1`** | `GRID-TAP-DOMUS-1` | ✓ d4572 |
| **East / west cubiculum** | Domus | **2** *(1 per room)* | — | **`SW-CUBICULUM-LAMP-1/2`** | `GRID-TAP-DOMUS-1` | ✓ d5321 |
| **East thermae** | Domus | **2** | — | **`SW-THERMAE-LAMP-1`** | `GRID-TAP-DOMUS-1` | ✓ d5323 |

**Feast socket map** — fixture detail in [tools.md](tools.md):

| Socket | Room |
|---:|---|
| **1** | Craft wing |
| **2** | Culina |
| **3–4** | Electronics lab |
| **5** | Officina `STORAGE-WING-1` |
| **6** | Fabrica `STORE-4` |
| **7–8** | Chem lab |
| **9** | West cubiculum |
| **10–11** | Millhouse |
| **12** | East cubiculum |
| **13–14** | Thermae |
| **15** | Fabrica south court |

### Component balance *(feast lamp kit)*

| Class | In service | Spare / stock | Ledger |
|---|---:|---|---|
| **Sealed bulbs** | **14** @ fixtures above | **2** · `BULB-LAMP-SPARE-CY14-10/11` @ `VAC-BENCH-1` | [tools.md](tools.md) |
| **Feast sockets** | **14** · `BULB-FEAST-SOCKET-Y14-1…14` | — | integrated in fixtures |
| **Room lamp switches** | **10** rows below | — | [tools.md](tools.md) · *electronics lab: `SW-WING-N-LIGHT-2` @ cleat 2 built d4847 · **no load** · room feed is **`SW-WING-N-LIGHT-1` only* |
| **Pendant flex leads** | branch + drop runs | **`WIRE-CU-LAMP-LEAD-Y16-1`** · **×4 pair @ domus peg** *(domus/mill drops)* | [resources.md](resources.md) |
| **LAMP-H link fuses** | seated @ branches/taps | **`FUSE-LINK-Y14-1` · ×0 @ pouch** | [resources.md](resources.md) |
| **Porcelain reflectors** | **6** mounted *(wing ×2 · chem ×2 · mill ×2)* | **×2 green @ rack E/F** | ⚑ **CY14-5/6 dry → fire → mount** |

---

## Generation

### ★★ `GEN-WW-1` — water-driven magneto
Map: `WW-2` wheelhouse · Built: d3248 · Air gap closed: d3249 · Field up: d3261 · Rewound: d3267

The campus generator. ×6 `MAG-BOOT-EM` rods in an iron yoke, closed-ring armature on a laminated core, 5-segment commutator with brushes tuned **under load**, concave pole faces shimmed to just over measured runout.

| Reading | Open | Loaded / notes |
|---|---|---|
| d3249 build | ~1.85 GB | ~1.40 GB · ~0.55 I · ~2.4 R |
| d3261 field up *(×6 rods, yoke shortened)* | 2.28 GB | 1.72 GB **(+23%)** |
| d3267 `ARMATURE-2` *(magneto)* | 4.31 GB | ~8.6 R · peak **~0.54 GB·I** |
| ✓ **d3336 `GEN-WW-2` shunt field** | **~8.5 GB** | **~8.6 R** · **~0.99 I** short · peak **~2.1 GB·I** @ ~8.6 R · **`WATER-CELL-1` supply-class** |

★★ **Epic closed d3258** — 6 h under real duty driving `CU-CELL-1`, no fault.

⚠ **On the water threshold, not over it.** The rewind traded voltage for current at unchanged peak power, which is what a rewind always does. Next step is a finer armature rewind.

> ✓ ★★★ **`GEN-WW-2` LIVE d3310 — SELF-EXCITED, SHUNT-WOUND.** *~4× the magneto output, steady, and none of the sag the steel rods gave after an hour.* ★★★ **The field stopped being something the machine CARRIES and became something it EARNS, for as long as the water runs.** ✓ **×6 `MAG-BOOT-EM` rods freed — no permanent magnet on the machine at all.**

**Mechanical service d5381:** commutator dry-clean · brush spring/track read · belt alignment · no-load field build **PASS** — brushes retained.
> ★★★ **Coils matched by DIFFERENTIAL WEIGHING, not by counting** — *same wire, same gauge, so equal weight is equal length is equal turns.* ✓ **Cross-tested against each other for a shorted turn** — ☠ **a short between neighbouring turns reads perfectly sound end to end, and will cook.**
> ☠ ★★★ **IT SITS DEAD FOR ~8 SECONDS ON EVERY START.** *A self-exciting machine looks broken while it is building out of the residual, and nothing distinguishes that from broken except waiting.* ⚑ **`COUNT TWENTY BEFORE YOU DECIDE` — chiselled on the yoke beside the polarity mark.**
> ⚠ **Not potted. Linen strip between layers, air paths open** — *a shunt field is the one winding that never rests.* ⧗ **Watch coil heat on long runs.**
> ★★★ **NEW CEILING IS THE WHEEL, NOT THE FIELD.** *The race loads now in a way it never did; the magneto was so weak the water never knew it was working.* ★ **The limit was moved, not removed.**
>
> ✓ **`HYDRO-ELEC-1` — +3 m crest locked d4112 · forebay **~35 × ~10 m** · scour pass 2 PASS · **✓ bench cut d4534** · **✓ crest/spillway d4532** · **✓ penstock live + flood test d4524** · **✓ forebay wing CLOSED d4540** · **✓ dam fill CLOSED d4550** · **✓ forebay intake LIVE d4552** · **✓ `HYDRO-ELEC-1-RACE-FEED-1` LIVE d4555** · **`GEN-WW-2` on forebay header + stream @ SUMMER**
>
> *(superseded — original spec)* ⧗ **`GEN-WW-2` — SHUNT-FIELD CONVERSION, opened d3295.** *Replace the ×6 `MAG-BOOT-EM` permanent rods with pole coils fed from the machine's own output.* ★★ **The field stops being a fixed asset that decays and becomes one the machine earns continuously; the ceiling moves from what steel holds to what the iron will take.**
> **Spec:** ~600 m at ~0.5 mm, **many turns at low current**, air between layers, **not potted** — ⚠ *the wax-rosin coating softens hot and a shunt field is the one winding that never rests.* ★ **Fine wire is simultaneously the thermally safe, electrically correct and cheapest choice.**
> ☠ **Polarity is chiselled into the yoke.** *Wired against the residual it does not merely fail to build — it erases the residual and makes the next attempt worse.* ★ **Flash from `DANIELL-CELL-1` if it will not start.**
> ⧗ **Wire-rate limited: ~600 g to draw at ~50 g/day off `CU-CELL-1`+`CU-CELL-2`. Field up ~d3307.**

Sub-assemblies: `GEN-WW-1-FRAME-1` (oak, sill-bolted, clear of splash, quick-release collar on WW-2 output) · `GEN-WW-1-BELT-TRAIN-1` (two ~4:1 stages = ~16:1, **crowned** pulleys, idler on stage 2, slack side up, ~12 rpm → ~190 rpm) · `GEN-WW-1-CORE-1` (laminations cut, **annealed after cutting**, deburred both faces, rosin-varnished) · `COMMUTATOR-2` (hardwood hub, 5 segments, plaster-jig seated, end-only ramps, adjustable brush gear, wire-bundle brushes).

### `GEN-WW-3-M` — scale **M** dynamo *(✓ LIVE @ wheel d5483)*

Map: **`WW-2` wheelhouse** · **`GEN-WW-1-FRAME-1` + `GEN-WW-1-BELT-TRAIN-1`** · scale per [gen-ww-3-scale-cy15.md](../plans/gen-ww-3-scale-cy15.md)

| Reading | Open | Loaded / notes |
|---|---|---|
| **d5481 bench** | **~9.6 GB** | **~8.15 R** · **~1.52 I** short · peak **~2.83 GB·I** |
| **d5483 hydro @ summer** | **~9.5 GB** | spot read @ mount |
| **d5484 hydro load line** | **~9.55 GB** | **~8.14 R** · **~1.51 I** short · peak **~2.80 GB·I** |
| **d5486 crossflow cut-over** | **~9.58 GB** | **~8.14 R** · matched **~2.72 GB·I** @ summer · **clutch G** |
| **d5491 rewind remount** | **~9.56 GB** | **~8.08 R** · matched **~2.76 GB·I** · **clutch G** |
| **d5492 brush + d5493 hydro** | **~9.56 GB** | **~8.08 R** · matched **~2.78 GB·I** · spill/nozzle tune |
| **d5496 stiffness rewind** | **~9.54 GB** | **~7.68 R** · **~1.58 I** short · matched **~2.84 GB·I** · peak **~2.92 GB·I** |

**Sub-assemblies:** `GEN-WW-3-M-CORE-1` · `GEN-WW-3-M-ROTOR-1` *(**0.70 mm** stiffness wind **d5496**)* · `GEN-WW-3-M-YOKE-1` · `GEN-WW-3-M-FIELD-1` · `GEN-WW-3-M-BRUSH-1` *(tune d5492)* · ⚑ **row L · kiln tap · `ELEC-PROCESS-HEAT-1`** · crossflow · Feeder-4 margin.

### `GEN-WW-2` — shunt dynamo *(harvested d5508 · assembly ×0)*

Map: **stripped d5508** · Cu → **`CU-GEN2-STOCK-CY15-5`** · lam → **`GEN-AC-1-LAM-SEED-1`** · line file d3336 archived · rollback **not** rebuildable without full re-fab.

## Storage

### `VOLTAIC-BATTERY-TRAY-1` — voltaic battery tray
Map: chem-lab · Built: d3000

Carries `VOLTAIC-8-CELL-1`, one-deep, acid electrolyte. ☠ Not food.

`VOLTAIC-JAR-1` (storage wing N, pile assembled), `VOLTAIC-PILE-1` (×6 pairs, vinegar) and `PLATE-MOLD-TRAY-1` (forge staging peg) are all **PAUSE** as of d2312.

**Lead-acid banks** — four pilot jars on parallel trays @ wheelhouse / chem porch tree · **`LEAD-ACID-BANK-Y13-1`** (pilots 1–2, `SW-STORAGE-TIE-1`) · **`LEAD-ACID-BANK-Y13-2`** (pilots 3–4, `SW-STORAGE-TIE-2`). Cell jars, electrolyte, and SOC rows: [resources.md](resources.md) (`LEAD-ACID-PILOT-*`).

## Distribution

### ✓ **`EC-1-GRID-FEEDER-1`** — campus trunk *(d3890)*
Map: **`WW-2` wheelhouse → craft path → chem porch east** · Built: d3890 · **~5–6 h install class**

**~22 m run** · paired **0.9 mm bare** **`WIRE-CU-GEN2-1`** · **`SW-CHEM-FEEDER-1` @ porch entry** · **`GRID-TAP-CHEM-1`** bench-east bus · **feeder awning ✓ d5333**.

| Install | Spec |
|---|---|
| **Route** | **Pegged aerial run · oak cleats @ ~1.5 m** · **not buried · not in conduit** |
| **Clearance** | **Away from char retort pad · away from water-race splash · craft-path shoulder** |
| **Conductor** | **Gen-2 draw** *(d3157 · file-bright)* · **+ and − separated by cleat spacing** · **✓ weather wrap d3979–3980 · wax+rosin×2+paper full trunk** · **~10 cm bare service tails @ wheelhouse splice** |
| **Branch** | **~3.05 m · 0.5 mm bare stub** to component box · **✓ installed d3972** · **fuse tail ~0.3 mm × ~8 cm @ tap** *(d3890)* |
| **Polarity** | **Tags @ every splice · + toward source** |
| **Materials logged d3890** | **`WIRE-CU-GEN2-1` −46 m · `CU-WIRE-Y10-3` −~0.5 m fuse conflation · `SW-KNIFE-BLANK-1` −×1 · `NAIL-IRON` −×2** |
| **Materials logged d3979–3980** | **Wrap: `WAX-Y10-RENDER-1` −~70 g · `ROSIN-1` −~25 g · `FLAX-SHIVE-Y8-21` −~44 g paper · `WAX-ROSIN-COMPOUND-2` pot spent** |
| **Materials logged d3972** | **Branch stub close · `O-1-MALACHITE` −3.5 kg → draw → `WIRE-CU-BRANCH-0.5-3972` −3.05 m installed** |

| Read @ d3890 | Wheelhouse | Chem porch tap |
|---|---|---|
| **Open** | **~8.5 GB** | **~7.6 GB** |
| **Loaded · `CU-CELL` on tap** | **~8.4 GB** | **~7.2 GB · cell runs** |
| **Run R** | — | **~2.3 R · ~46 m paired 0.9 mm** · **audit ~2.35 R d4565** |

★ **Default: `SW-CHEM-FEEDER-1` OPEN when bench idle · closed for named load only.** ✓ **`MOTOR-1` first named load d3971.**

### ✓ **`EC-1-GRID-BUS-TIE-1`** — gen ↔ storage *(d3971)*
Map: **`WW-2` wheelhouse gen post** · Built: d3971 · **~3.5 h install + test class**

**`LEAD-ACID-BANK-Y13-1` parallel + → `SW-STORAGE-TIE-1` → gen +** · **common − → frame strap** · **~2.4 m · 0.9 mm bare pair · oak cleats @ post · not buried.**

| Materials logged d3971 | |
|---|---|
| **`WIRE-CU-GEN2-1`** | **−~2.0 m · tail → ×0** |
| **`CU-WIRE-Y10-COATED`** | **−~0.4 m · shortfall after tail spent** |
| **`CU-WIRE-Y10-3`** | **−~0.08 m · fuse tail refresh** |
| **`SW-KNIFE-BLANK-1`** | **−×1 → `SW-STORAGE-TIE-1`** |
| **`NAIL-IRON`** | **−×1 · post cleat** |

| Mode | Read |
|---|---|
| **Gen ON · tie ON** | Bank floats · charges from wheel |
| **Gen OFF · tie ON · feeder ON** | **`GRID-TAP-CHEM-1` ~1.58 GB class @ ~54% SOC** |
| **Tie OFF** | Bank isolated for service |

### ✓ **`EC-1-GRID-BUS-TIE-2`** — gen ↔ storage bank B *(d4009)*
Map: **`WW-2` wheelhouse post tree east · chem tray B** · Built: d4009 · **~3.5 h install + test class**

**`LEAD-ACID-BANK-Y13-2` parallel + → `SW-STORAGE-TIE-2` → gen +** · **common − → frame strap** · **~2.5 m · 0.9 mm bare pair · oak cleats · not buried.**

| Materials logged d4009 | |
|---|---|
| **`WIRE-CU-GEN2-1`** | **−~2.5 m** |
| **`ST-STR-BAR-Y13-1` tail** | **−~16 g · `SW-KNIFE-BLANK-1` forge** |
| **`NAIL-IRON`** | **−×1 · post cleat** |

| Mode | Read |
|---|---|
| **Gen ON · tie-2 ON** | Bank B floats · charges from wheel |
| **Tie-2 OFF · tie-1 ON** | Bank B isolated · Bank A on bus |
| **Both ties ON** | **Independent float · no cross-feed** |

### ✓ **`EC-1-GRID-FEEDER-2`** — Officina craft wing trunk *(d3976)*
Map: **`WW-2` wheelhouse → campus path → Officina `CRAFT-WING-1` east jamb** · Built: d3976 · **~6–7 h install class** · **`OFFICINA-EAST-MUDROOM-1` splash hood ✓ d5336**

**~40 m run** · paired **0.9 mm bare** **`WIRE-CU-GEN2-1`** · **`SW-CRAFT-FEEDER-1` @ east entry** · **`GRID-TAP-CRAFT-1` north bay**.

| Install | Spec |
|---|---|
| **Route** | **Pegged aerial · oak cleats @ ~1.5 m · not buried** |
| **Clearance** | **Campus path shoulder · away from island hearth smoke lane · separate breaker from chem** |
| **Conductor** | **Gen-2 draw** *(d3157 · file-bright)* · **+ and − separated by cleat spacing** · **✓ weather wrap d3985 · wax+rosin×2+paper full trunk** · **~10 cm bare service tails @ taps** |
| **Branch** | **~3 m · 0.5 mm bare stub · fuse tail ~0.3 mm × ~8 cm @ tap** |
| **Materials logged d3976** | **`WIRE-CU-GEN2-1` −80 m · `CU-WIRE-Y10-3` −~3.5 m · `ST-STR-BAR-Y13-1` −~18 g · `BRASS-STOCK` −~4 g · `NAIL-IRON` −×4** |
| **Materials logged d3985** | **Wrap: `WAX-Y10-RENDER-1` −~58 g · `ROSIN-1` −~95 g · `FLAX-SHIVE-Y8-21` −~42 g paper** |

| Read @ d3976 | Wheelhouse | Craft tap |
|---|---|---|
| **Gen ON** | **~8.5 GB** | **~6.7 GB** |
| **Loaded · `CU-CELL` on tap** | **~8.4 GB** | **~6.3 GB · cell runs** |
| **Bank only · gen OFF** | — | **~1.48 GB** |
| **Run R** | — | **~4.0 R · ~80 m paired 0.9 mm** · **audit ~4.05 R d4565** |

★ **Default: `SW-CRAFT-FEEDER-1` OPEN when bay idle** — **sole Officina building entry d4987** *(craft + **`STORAGE-WING-1`** + north work wing bus)*. ✓ **Domus margin branch d4563** · ✓ **storage wing lamp d5330** · ⚑ **Horreum defer**.

### ✓ **`EC-1-GRID-FEEDER-FABRICA-1`** — Fabrica hub compound trunk *(d4986–4987)*

Map: **`WW-2` wheelhouse post tree → `WW-HUB-TOWER-1` south apron** · Built: **d4987** · **~44 m paired class** *(reclaim ex-Feeder-3 + pt1 splice)* · **hub tee drip tray + tail boots ✓ d5333**

**`SW-FABRICA-FEEDER-1` @ hub south cheek** · **`EC-1-TAP-BOX-STD-4`** · **`GRID-TAP-FABRICA-1` LIVE** · **~7.9 GB @ gen ON** · **R ~2.1**.

★ **Separate entry from `EC-1-GRID-FEEDER-1` chem porch** — **two switches · one compound.** **Hub lamp loads ✓ d5329–5330** · **millhouse ✓ d5323** · **chem lamps ✓ d5330**.

### ✓ **`EC-1-GRID-FEEDER-4`** — G2 machine-shop trunk *(d5485)*

Map: **wheelhouse post tree → `PATH-CROWN` → `PARK-MFG-1` / G2 east jamb chase** · **~51 m paired · 1.2 mm bare** · Built: **d5485**

**`SW-FEEDER-4-1` @ G2 east jamb** · **`EC-1-TAP-BOX-STD-5`** · **`GRID-TAP-G2-MS-1` stub** *(no **`MOTOR-IND-1`** yet)*.

| Read @ **~0.42 I** d5485 | |
|---|---|
| **V_open @ tap** | **~9.46 GB** |
| **V_loaded @ tap** | **~5.50 GB** |
| **R_pair** | **~1.52 R** |
| **Margin** | **✓ ≥ ~0.35 GB** vs **`MOTOR-IND`** stall floor · **thin vs 6.5 GB wet-shaft aspirational** |

★ **Default: `SW-FEEDER-4-1` OPEN until MS motor commissioned.**

### ~~**`EC-1-GRID-FEEDER-3`**~~ — trunk **RETIRED d4987** *(copper → Fabrica-1)*

Map: **Was wheelhouse tee → north jamb** · **Aerial trunk stripped d4987.**

**`SW-WING-N-FEEDER-1` DEPRECATED · wired OPEN** · **`EC-1-TAP-BOX-STD-3` / `GRID-TAP-WING-N-1`** **fed from `GRID-TAP-CRAFT-1`** via **`OFFICINA-BUS-JUMPER-4987`** **~7.2 m paired 0.5 mm** · north branches unchanged.

| Install | Spec |
|---|---|
| **Route** | **Pegged aerial · oak cleats · not buried** · **clear of hearth smoke lane** |
| **Wrap** | **Wax+rosin+paper full trunk d4808–4809** |
| **Zones** | **Z-LIGHT ×2 · Z-BENCH ×2 · Z-MOTOR ×1** — sleeves d4746 |
| **Materials logged** | **d4808:** **`O-1-MALACHITE` −~1.15 kg · switch/brass/fuse/cleats** · **d4809:** **`O-1-MALACHITE` −~1.05 kg · wrap · `NAIL-IRON` −×5** |

| Read @ d4809 | Wheelhouse | Wing tap |
|---|---|---|
| **Gen ON** | **~8.5 GB** | **~7.1 GB** |
| **Run R** | — | **~2.7 R · ~48 m paired 0.9 mm** |
| **Branches** | — | **✓ `LIGHT-1/2` d4847 · BENCH d4848 · MOTOR d4860** |

★ **`SW-WING-N-FEEDER-1` DEPRECATED d4987** — use **`SW-CRAFT-FEEDER-1` only.** Layout: [officina-n-work-wing-layout.md](../government/archive/plans/officina-n-work-wing-layout.md).

## Branches · taps · fixtures

Lamp sockets, knife switches, CP-G outlets, and fuse seats on branches — **fixture rows** in [tools.md](tools.md).

### ✓ **`EC-1-GRID-BRANCH-WING-N-LIGHT-1`** — north bench lamp *(d4847)*

Map: **`GRID-TAP-WING-N-1` → `Z-LIGHT` sleeve 1 → `WING-N-CEILING-CLEAT-1`** · **`BULB-WING-N-LAMP-1`**

**~4.2 m** paired **0.5 mm** · **`SW-WING-N-LIGHT-1` @ cleat** · **~1.15 m drop** · **✓ insulate + commission d4847**.

| Materials logged d4847 | |
|---|---|
| **`O-1-MALACHITE`** | **−~1.02 kg** *(×2 draws)* |
| **`ST-STR-BUTTON-Y13-3`** | **−~44 g** → **`SW-WING-N-LIGHT-1/2`** |
| **`FUSE-LINK-Y14-1`** | **−×2** · **LAMP-H** |
| **`WAX-Y10-RENDER-1` / `ROSIN-1` / `FLAX-SHIVE-Y8-21`** | **−~16 g / −~8 g / −~14 g** |
| **`NAIL-IRON`** | **−×8** |

★ **`SW-CRAFT-FEEDER-1` = Officina building master d4987** · **`SW-WING-N-FEEDER-1` DEPRECATED** · **`SW-WING-N-LIGHT-1` = north work wing room lamp** *(both fixtures)* · **building + room switch OPEN** to glow.

### ✓ **`EC-1-GRID-BRANCH-WING-N-LIGHT-2`** — centre table lamp *(d4847)*

Map: **`GRID-TAP-WING-N-1` → `Z-LIGHT` sleeve 2 → `WING-N-CEILING-CLEAT-2`** · **`BULB-WING-N-LAMP-2`**

**~4.0 m** paired **0.5 mm** · **load → `SW-WING-N-LIGHT-1` lugs** · **`SW-WING-N-LIGHT-2` @ cleat 2 · OPEN · no load** · **commission T1–T5 PASS d4847**.

### ✓ **`EC-1-GRID-BRANCH-WING-N-BENCH-1`** — north bench CP-G *(d4848)*

Map: **`GRID-TAP-WING-N-1` → `Z-BENCH` sleeve → `WORK-BENCH-N-1` rear rail** · **`CP-G-SOCKET-WING-N-1`**

**~3.8 m** paired **0.5 mm** · **`SW-WING-N-BENCH-1` @ bench cheek** · **BENCH-class fuse** · **commission T1–T5 PASS d4848** · **second machine-lug pair d4859**.


### ✓ **`EC-1-GRID-BRANCH-WING-N-MOTOR-1`** — north exhaust fan *(d4860)*

Map: **`GRID-TAP-WING-N-1` → `Z-MOTOR` sleeve → `WING-N-EXHAUST-1` / `MOTOR-2`** · duct: [infrastructure.md](infrastructure.md) (`WING-N-EXHAUST-1`)

**~4.1 m** paired **0.5 mm** · **`SW-WING-N-MOTOR-1` @ east jamb** · motor-class fuse **~0.22 I** · **commission T1–T5 PASS d4860** · **exhaust ON before lead-acid charge @ north bench**.

## Grid-fed motors

### `MOTOR-2` — wing exhaust motor *(LIVE)*
Map: **`WING-N-EXHAUST-1`** · **`EC-1-GRID-BRANCH-WING-N-MOTOR-1`** · Opened: **d4860**

**Fan-duty PM motor** · field from **`MAG-STEEL-Y13-ROD-3`** · brushes from **`ST-SPR-BUTTON-Y13-4`** · **second grid-fed motor on campus** · **`MOTOR-1` remains @ chem porch**.

**Measured d5081:** **R ~4.1 · stall ~190 mN·m · ~0.085 I @ exhaust duty** · Feeder-2 drop **~0.23 GB** @ fan load.

| Materials logged d4848 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.38 kg** |
| **`ST-STR-BUTTON-Y13-3`** | **−~22 g** |
| **`FUSE-LINK-Y14-1`** | **−×1** |
| **`FURNITURE-SELECT-1` / `TILE-TF`** | **bench + tray** |

★ **Portable loads via `CP-G-WING-N-PORTABLE-1`** (`CP-G-PLUG-PROTOTYPE-Y14-1` @ bench hook) — **remove plug when wing idle** · **`WING-N-EXHAUST-1` ON before bench energize** · lead-acid @ north bench only with exhaust running.

### ✓ **`EC-1-GRID-BRANCH-DESK-1`** — craft-wing room lamp *(d4558)*
Map: **`GRID-TAP-CRAFT-1` → north bay desk rafter cleat** · **`BULB-FEAST-LAMP-Y14-1`** *(socket **1** · `CRAFT-WING-1`)*

**~1.8 m** paired **0.5 mm** · oak cleats · **`SW-FEAST-LAMP-1` @ cleat** · fuse tail @ tap unchanged · **~6.6 GB class @ tap gen ON**.

| Materials logged d4558 | |
|---|---|
| **`WIRE-CU-GEN2-1`** | **−~3.8 m** |
| **`ST-STR-BAR-Y13-1` tail** | **−~14 g → `SW-FEAST-LAMP-1`** |
| **`NAIL-IRON`** | **−×3** |

★ **Default: `SW-FEAST-LAMP-1` OPEN only when bulb is meant to glow** — leave-on for Yule feast grammar.

### ✓ **`EC-1-GRID-BRANCH-DOMUS-1`** — domus lighting margin *(d4563)*

Map: **horreum south jamb tee on Feeder-1 cleat → domus south porticus → culina entry stud**

**~11 m** paired **0.5 mm** · oak cleats · **`SW-DOMUS-LIGHT-1` @ porticus post** · **`GRID-TAP-DOMUS-1`**.

| Materials logged d4563 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.85 kg** → branch draw |
| **`ST-STR-BAR-Y13-1` tail** | **−~6 g** → **`SW-DOMUS-LIGHT-1`** |
| **`WAX-Y10-RENDER-1` / `ROSIN-1`** | **−~15 g / −~8 g** cheek wrap |
| **`NAIL-IRON`** | **−×3** |

★ **Dry loads only · lighting class · not a second trunk.**

### ✓ **`EC-1-TAP-BOX-STD-1`** @ domus *(d4563)*

Map: **porticus east stud @ culina door** · **`GRID-TAP-DOMUS-1`**

**Max ~0.35 I · ~0.25 GB·I dim · LAMP-H / BENCH** · CP-G shutter socket · machine lugs · **`FUSE-LINK-Y14-1`** in seat.

### ✓ **`EC-1-GRID-BRANCH-CULINA-1`** — culina pendant *(d4571)*

Map: **`EC-1-TAP-BOX-STD-1` machine lugs → porticus → culina north rafter @ `WORK-TABLE-CULINA-1`** · **`BULB-CULINA-LAMP-Y14-1`**

**~3.6 m** paired **0.5 mm** · **`SW-CULINA-LAMP-1` @ rafter cleat** · **~1.0 m drop** · **✓ wrap d4572**.

| Materials logged d4571 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.48 kg** → branch draw |
| **`ST-STR-BAR-Y13-1` tail** | **−~11 g** → switch + hook |
| **`BRASS-STOCK`** | **−~3 g** |
| **`NAIL-IRON`** | **−×4** |

| Materials logged d4572 (insulate + commission) | |
|---|---|
| **`WAX-Y10-RENDER-1` / `ROSIN-1`** | **−~14 g / −~9 g** |
| **`FLAX-SHIVE-Y8-21`** | **−~18 g** paper |
| **`FUSE-LINK-Y14-1`** | **−×2** · **LAMP-H** in tap seat |
| **`NAIL-IRON`** | **−×2** steam skirt |

**Label @ tap box:** **`BULB-CULINA-LAMP-Y14-1` · max ~1.15 I LAMP-H** · **commission T1–T5 PASS d4572**.

★ **`SW-DOMUS-LIGHT-1` @ porticus = margin master** · **`SW-CULINA-LAMP-1` = local lamp** · **both OPEN** to energize.

### ✓ **`EC-1-GRID-BRANCH-CUBICULUM-1`** — cubicula ×2 *(d5321)*

Map: **`EC-1-TAP-BOX-STD-1` machine lugs → porticus east → cubiculum corridor → east + west jamb tees**

**~7.0 m** paired **0.5 mm** · **`SW-CUBICULUM-LAMP-1` / `SW-CUBICULUM-LAMP-2`** · **`BULB-CUBICULUM-LAMP-Y14-1/2`** · **commission ✓ d5321**.

| Materials logged d5321 | |
|---|---|
| **`WIRE-CU-LAB-0.5-CY13-1` / `WIRE-CU-GEN2-1`** | **−~6.4 m / −~1.2 m** branch |
| **`WIRE-CU-LAMP-LEAD-Y16-1`** | **−×2 pair** drops |
| **`WAX-Y10-RENDER-1` / `ROSIN-1` / `FLAX-SHIVE-Y8-21`** | cleat wrap |
| **`ST-STR-BAR-Y13-1` tail** | **−~12 g** switches |
| **`FUSE-LINK-Y14-1`** | **−×2** · **LAMP-H** seats |

★ **`SW-DOMUS-LIGHT-1` master** · **one cubiculum switch OPEN** per lamp · **max ~1.15 I each @ tap label**.

### ✓ **`EC-1-GRID-BRANCH-THERMAE-1`** — east thermae ×2 *(d5321 hang · d5323 commission)*

Map: **porticus south stub → tepidarium lintel → caldarium lip drop**

**~3.8 m** paired **0.5 mm** · **`SW-THERMAE-LAMP-1`** · **`BULB-THERMAE-LAMP-Y14-1/2`** · **insulate + commission ✓ d5323** · **max ~1.25 I combined · LAMP-H** @ domus tap.

| Materials logged d5321 | |
|---|---|
| **`WIRE-CU-GEN2-1`** | **−~4.6 m** draw |
| **`WIRE-CU-LAMP-LEAD-Y16-1`** | **−×2 pair** |
| **`ST-STR-BAR-Y13-1` tail** | **−~6 g** |

| Materials logged d5323 | |
|---|---|
| **`WAX-Y10-RENDER-1` / `ROSIN-1` / `FLAX-SHIVE-Y8-21`** | steam wrap |
| **`FUSE-LINK-Y14-1`** | **−×1** · T5 reseat |

### ✓ **`EC-1-GRID-BRANCH-MILLHOUSE-1`** — `MILLHOUSE-2` ×2 *(d5323)*

Map: **`EC-1-TAP-BOX-STD-4` machine lugs → south court cleat → mill north rafter**

**~4.4 m** paired **0.5 mm** · **`SW-MILLHOUSE-LAMP-1`** · **`BULB-MILLHOUSE-LAMP-Y14-1/2`** · **commission ✓ d5323**.

| Materials logged d5323 | |
|---|---|
| **`WIRE-CU-GEN2-1`** | **−~5.4 m** draw |
| **`WIRE-CU-LAMP-LEAD-Y16-1`** | **−×2 pair** |
| **`ST-STR-BAR-Y13-1` tail** | **−~6 g** |
| **`FUSE-LINK-Y14-1`** | **−×1** · mill seat |

★ **`SW-FABRICA-FEEDER-1` ON** · **`SW-MILLHOUSE-LAMP-1` local** · **~1.14 / ~1.08 I** each dim @ gen ON.

### ✓ **`EC-1-GRID-BRANCH-FABRICA-COURT-1`** — south court lamp *(d5329)*

Map: **`EC-1-TAP-BOX-STD-4` → south court lamp post** · **`BULB-FABRICA-COURT-LAMP-Y14-1`** *(socket **15** · no reflector)*

**~3.6 m** paired **0.5 mm** · **`SW-FABRICA-COURT-LAMP-1`** · **commission ✓ d5329** · **~1.12 I dim @ gen ON**.

| Materials logged d5329 | |
|---|---|
| **`WIRE-CU-GEN2-1`** | **−~3.6 m** *(court share)* |
| **`WIRE-CU-LAMP-LEAD-Y16-1`** | **−×1 pair** |
| **`FUSE-LINK-Y14-1`** | **−×1** · court seat |

### ✓ **`EC-1-GRID-BRANCH-FABRICA-FORGE-FAN-1`** — `FORGE-D` blast assist *(d5329)*

Map: **`GRID-TAP-FABRICA-1` → `FORGE-D` east jamb → `MOTOR-3` stub** · **`BLAST-BLOWER-1` belt ✓ d5330**

**~5.2 m** paired **0.5 mm** · **`SW-FORGE-FAN-1`** · motor fuse **~0.15 I** · **commission ✓ d5330**.

| Materials logged d5329 | |
|---|---|
| **`WIRE-CU-GEN2-1`** | **−~5.2 m** |
| **`FUSE-LINK-Y14-1`** | **−×1** · fan seat |

### `MOTOR-3` — forge blast-assist motor *(LIVE)*
Map: **`FORGE-D` east assist pad** · **`EC-1-GRID-BRANCH-FABRICA-FORGE-FAN-1`** · **`BLAST-BLOWER-1` belt coupled d5330** · Opened: **d5329** · Commission: **d5330**

**Fan-duty PM** · **~0.11 I @ assist duty** · **`SW-FORGE-FAN-1` local kill**.

### ✓ **`EC-1-GRID-BRANCH-WING-N-BLOWER-R&D-1`** — `MOTOR-4` blower R&D *(d5468)*

Map: **`GRID-TAP-WING-N-1` → `Z-BLOWER-R&D` sleeve → `MOTOR-4` @ `WORK-BENCH-N-1` · `BLOWER-R&D-TEST-1`**

**~4.6 m** paired **0.5 mm** · **`SW-WING-N-BLOWER-1` @ bench apron** · motor-class fuse **~0.28 I** · **commission T1–T5 PASS d5468** · **`WING-N-EXHAUST-1` ON before energize** · **do not run with `SW-WING-N-MOTOR-1` ON**.

| Materials logged d5468 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.42 kg** |
| **`ST-STR-BUTTON-Y13-3`** | **−~5 g tail** → **`SW-WING-N-BLOWER-1`** |
| **`WIRE-CU-LAB-0.3-CY14-1`** | **−~0.10 m** fuse |

### `MOTOR-4` — high-torque process / blower R&D motor *(LIVE · d5468)*
Map: **`WORK-BENCH-N-1`** · **`EC-1-GRID-BRANCH-WING-N-BLOWER-R&D-1`** · **`BLOWER-R&D-TEST-1` throat** · Opened: **d5465** · Grid: **d5468**

**Blower R&D = generator R&D stand-in** · field **`MAG-STEEL-Y15-ROD-1/2`** · **`MOTOR-4-BRUSH-1` d5467** · **Measured d5467:** **R ~4.05 · stall ~255 mN·m** · **d5468 duty:** **~0.12 I @ `BLOWER-R&D-TEST-1` card pull**. ⚑ **load curves · `GEN-WW-3` · `ELEC-PROCESS-HEAT-1` muffle**.

### ✓ **`EC-1-GRID-BRANCH-OFFICINA-STORAGE-LIGHT-1`** — Officina `STORAGE-WING-1` *(d5012 · fuse d5016)*

Map: **`GRID-TAP-CRAFT-1` → turris west → N shelf rafter** · **`BULB-OFFICINA-STORAGE-LAMP-Y14-1`** *(socket **5** · hung d5015 · bulb d5019)*

**~3.5 m** paired **0.5 mm** · **`SW-OFFICINA-STORAGE-LAMP-1` @ cleat** · **✓ full wrap + door flash d5333** · **LAMP-H fused d5016** · **commission ✓ d5330**.

| Materials logged d5012 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.46 kg** |
| **`WAX-Y10-RENDER-1` / `ROSIN-1`** | **−~8 g / −~4 g** |
| **`FLAX-SHIVE-Y8-21`** | **−~10 g** |
| **`NAIL-IRON`** | **−×3** *(cave)* + peg |

| Materials logged d5016 | |
|---|---|
| **`FUSE-LINK-Y14-1`** | **−×1** · branch seat |

### ✓ **`EC-1-GRID-BRANCH-STORE-4-LIGHT-1`** — Fabrica `STORE-4` *(d5013 · fuse d5016)*

Map: **`GRID-TAP-FABRICA-1` → south jamb cheek → centre shelf rafter** · **`BULB-STORE-4-LAMP-Y14-1`** *(socket **6** · hung d5015 · bulb d5019)*

**~3.2 m** paired **0.5 mm** · **`SW-STORE-4-LAMP-1` @ cleat** · **✓ full wrap + eave flash d5333** · **LAMP-H fused d5016** · **commission ✓ d5330**.

| Materials logged d5013 | |
|---|---|
| **`WAX-Y10-RENDER-1` / `ROSIN-1`** | **−~7 g / −~3 g** *(S share)* |
| **`FLAX-SHIVE-Y8-21`** | **−~6 g** |

| Materials logged d5016 | |
|---|---|
| **`FUSE-LINK-Y14-1`** | **−×1** · branch seat |

★ **Chem lab:** **×2 interior pendants** · **one switch** · **no porch fixture**.

### ✓ **`EC-1-GRID-BRANCH-CHEM-LAB-LIGHT-1`** — chem lab lamp 1 *(d5013 · hang d5015)*

Map: **`GRID-TAP-CHEM-1` → east jamb → rafter 1** · **`BULB-CHEM-LAB-LAMP-Y14-1`** · **`BULB-LAMP-CHEM-LAB-Y14-1` seated**

**~3.8 m** paired **0.5 mm** · **feed → `SW-CHEM-LAB-LAMP-1` @ interior east cleat** · **✓ full exterior wrap d5333**.

### ✓ **`EC-1-GRID-BRANCH-CHEM-LAB-LIGHT-2`** — chem lab lamp 2 *(d5017 · hang d5015)*

Map: **`GRID-TAP-CHEM-1` → rafter 2** · **`BULB-CHEM-LAB-LAMP-Y14-2`** · **`BULB-LAMP-CHEM-LAB-Y14-2` seated**

**~3.7 m** paired **0.5 mm** · **load → same `SW-CHEM-LAB-LAMP-1` lugs** · **✓ full exterior wrap d5333**.

| Chem room | |
|---|---|
| **Switch** | **`SW-CHEM-LAB-LAMP-1` only** · **OPEN default** |
| **Fuse** | **LAMP-H @ chem tap · d5016** · **commission ✓ d5330** |

| Materials logged d5013 / d5017 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.44 kg / −~0.43 kg** |
| **`WAX-Y10-RENDER-1` / `ROSIN-1` / `FLAX-SHIVE-Y8-21`** | per day files |
| **`FUSE-LINK-Y14-1`** | **−×1** · room seat d5016 |

### ✓ **`GRID-TAP-CRAFT-2`** + **`EC-1-TAP-BOX-STD-2`** @ Officina south bay *(d4563)*

Map: **`CRAFT-WING-1` south bay east stud** · bus split **`GRID-TAP-CRAFT-1` → ~3.2 m stub** · **`SW-CRAFT-BRANCH-2` @ jamb**

**Max ~0.35 I socket · ~0.9 GB·I @ gen ON · LAMP-H / BENCH** · **`EC-1-TAP-BOX-STD-2`** wall-mounted.

| Materials logged d4563 | |
|---|---|
| **`BRASS-STOCK`** | **−~5 g** tap posts |
| **`FUSE-LINK-Y14-1`** | **−×2** *(domus + craft seats)* |
| **`ST-STR-BAR-Y13-1` tail** | **−~6 g** → **`SW-CRAFT-BRANCH-2`** |
| **`NAIL-IRON`** | **−×3** |

★ **North tap unchanged:** **`EC-1-GRID-BRANCH-DESK-1` + feast lamp** stay on **`GRID-TAP-CRAFT-1`**.

**Repeat jig:** **`EC-1-TAP-BOX-JIG-Y14-1`** @ craft bench peg.

### ★★★ `ARMATURE-2` *(in `GEN-WW-1`)*

Wound: d3267 · 5 × 145 turns at 0.65 mm, ~182 m. Drawn down from `ARMATURE-1` with **no melt** and annealed each pass, which is why the copper survived the redraw.

⚠ `ARMATURE-3` — a coarse winding for `CU-CELL-1` — is **not built** and needs ~500 g. ★ No longer urgent and no longer a deadlock: the series pair recovers ~25% without it.

### `MOTOR-1` — bench motor *(LIVE)*
Map: chem porch bench east · **`GRID-TAP-CHEM-1`** · Opened: d3951 · **✓ LIVE d3964**

**PM-field bench motor** · **`ST-MAG-1` field** · **`ST-STR-1` frame** · **first grid-fed campus consumer**. ✓ **`MOTOR-1-FRAME-1` d3952** · **`MOTOR-1-YOKE-1` + `MOTOR-1-MAG-STACK-1` d3957** · **`MOTOR-1-CORE-1` d3958** · **`MOTOR-1-COMMUTATOR-1` d3958** · **`MOTOR-1-ARMATURE-1` d3963** · **`MOTOR-1-BRUSH-1` d3964**. **Measured d3964:** **R ~3.8 · stall torque ~100 mN·m @ 55 mm arm · ~0.13 I @ ~100 g load**. ⚑ **load fixture · pole-gap shave optional**. Reference: **`PEDAL-GEN-1`** · **`GEN-WW-1-CORE-1`** · **`EC-1-GRID-FEEDER-1`**.

### `PEDAL-GEN-1` — pedal generator
Map: chem porch · Built: d3198

`EM-COIL-3` armature, ~3 mm gap, `COMMUTATOR-1`, ~5–11° needle. Output scales with pedal.

`COMMUTATOR-1`: oak boss, ×2 copper split segments in wax, copper leaf brushes ×2 plus ×1 spare, timed to the neutral plane. `MAG-STACK-2`: rods #8 · #12 · #16 · #19 plus yoke, lift ~65 mm — the field. `EM-COIL-3`: ~280 turns gen-2 on a ~185 g iron core, bench fixture at chem porch, leads C/D.

---

## Loss & torque ledger *(CY14 industrial drive study)*

*Plan: [industrial-mech-drive-cy14.md](../plans/industrial-mech-drive-cy14.md) · **survey ✓ d5081***

**`WW-2-Q` spring CY14:** d5043 **~25.2 L/s** · d5086 **~24.6 L/s** *(pre-crest · d5086)* — [ww-2-power-upgrade.md](../plans/ww-2-power-upgrade.md)

### Feeder loss model *(GB·I at load)*

| Run | Length | Gauge | R measured | V_src | V_tap | I_load | Notes |
|---|---:|---|---:|---:|---:|---:|---|
| **Feeder-1** chem | **~46 m** paired | **0.9 mm** | **~2.35 R** | **~8.52** | **~7.18** | **~0.14** | d5081 audit · open **~7.62** |
| **Feeder-2** craft | **~80 m** paired | **0.9 mm** | **~4.05 R** | **~8.52** | **~6.51** | **~0.085** | d5081 · `MOTOR-2` ON · open **~6.74** |
| **Feeder-Fabrica-1** | **~44 m** paired | class | **~2.1 R** | **~8.52** | **~7.88** | — | d5081 open read |
| **Feeder-4** G2 MS | **~51 m** | **1.2 mm paired** | **~1.52 R** | **~9.54** | **~5.50** | **~0.42** | **d5485 LIVE** · **`GRID-TAP-G2-MS-1`** |

★ **Derive:** ΔV ≈ I × R_pair · P_loss ≈ I²R · compare to **`GEN-WW-2`** peak **~2.1 GB·I** @ ~8.6 R.

### Machine shaft torque budget *(belt tree · N·m)*

| Load | Mode | rpm class | Torque demand | Source read | Day |
|---|---|---:|---:|---|---|
| **WW-2** shaft | Prony / apron | **~9–10** | **~330–350** | d5029 | ✓ |
| **Lathe** | Clutch A direct | **~145** | slip **~38** | strap d5081 | ✓ |
| **Lathe** | Clutch B reduced | **~58** | slip **~85** | strap d5081 | ✓ |
| **Mill / bench** | Clutch D reduced | **~36** | slip **~125** | **budget row** | ✓ |
| **Block bench** | collar **#5** | **~62** | peak **~68** | cam d5081 | ✓ |
| **Boring mill** | Clutch C | **~145** | slip **~32** | strap d5081 | ✓ |
| **WW-2** shaft | Prony | **~9.8** | **~365** | d5041 ref d5081 | ✓ |

### Motor torque & electrical budget

| ID | R arm | Stall / rated torque | I @ load | Fed from | Notes |
|---|---:|---:|---:|---|---|
| **`MOTOR-1`** | **~3.8** | **~100 mN·m** stall d3964 | **~0.13** @ ~100 g | Feeder-1 | bench class |
| **`MOTOR-2`** | **~4.1** | **~190 mN·m** stall | **~0.085** exhaust | Feeder-2 | **d5081** |
| **`MOTOR-IND-1`** *(target)* | — | **≥ ~130 N·m @ line shaft** · **I_run ≤ ~0.42** | — | Feeder-4 class | **d5081 slate** · paired **`GEN-MOTOR-IND-R&D-1`** |

### Mechanical bridge *(belt drive @ current site)*

| Element | Spec | Status |
|---|---|---|
| **Prime** | Crossflow → clutch M → **`BELT-TREE-1`** | [ww-2-power-upgrade.md](../plans/ww-2-power-upgrade.md) |
| **Electric prime** | Crossflow → clutch G → upgraded gen | same |
| **Shop drive** | **`MOTOR-IND-1` → line shaft → belts** | **@ current sites first** d5081 |
| **Move gate** | Relocate tools to **G2 MS** only when **Feeder-4** + shaft PASS | ∥ [g2-ms1-machine-shop-cy14.md](../plans/g2-ms1-machine-shop-cy14.md) |
| **`EC-1-GRID-FEEDER-4`** | **✓ LIVE d5485** · **`SW-FEEDER-4-1` · `GRID-TAP-G2-MS-1`** @ G2 east jamb | **R_pair ~1.52** · margin **PASS @ ~0.42 I** |

