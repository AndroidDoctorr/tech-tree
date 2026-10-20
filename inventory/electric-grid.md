# Campus electric grid (`EC-1`)

Installed **generation · storage · distribution · grid-fed loads** on the HOME campus. Code: [electrical-code-1.md](../government/regulations/electrical-code-1.md) · expansion plan: [ec-1-campus-expansion.md](../plans/ec-1-campus-expansion.md). **Hydraulic prime mover** (`WW-2`, forebay, belt tree) stays in [infrastructure.md](infrastructure.md).

**Fixture IDs** (bulbs, switches, tap boxes, CP-G sockets) also appear in [tools.md](tools.md) — this file is **runs, taps, buses, and install state**.

## Live roster *(d5076)*

| Layer | IDs |
|---|---|
| **Source** | `GEN-WW-1` / `GEN-WW-2` @ `WW-2` wheelhouse · `PEDAL-GEN-1` @ chem porch |
| **Storage bus** | `LEAD-ACID-BANK-Y13-1` · `LEAD-ACID-BANK-Y13-2` *(jars in [resources.md](resources.md))* · `SW-STORAGE-TIE-1/2` |
| **Early DC** | `VOLTAIC-BATTERY-TRAY-1` / `VOLTAIC-8-CELL-1` |
| **Trunks** | `EC-1-GRID-FEEDER-1` chem · `EC-1-GRID-FEEDER-2` Officina · `EC-1-GRID-FEEDER-FABRICA-1` Fabrica · ~~`EC-1-GRID-FEEDER-3`~~ retired |
| **Master switches** | `SW-CHEM-FEEDER-1` · `SW-CRAFT-FEEDER-1` · `SW-FABRICA-FEEDER-1` · `SW-WING-N-FEEDER-1` deprecated OPEN |
| **Taps** | `GRID-TAP-CHEM-1` · `GRID-TAP-CRAFT-1` · `GRID-TAP-CRAFT-2` · `GRID-TAP-WING-N-1` · `GRID-TAP-DOMUS-1` · `GRID-TAP-FABRICA-1` |
| **Tap boxes** | `EC-1-TAP-BOX-STD-1` domus · `STD-2` craft S · `STD-3` wing N · `STD-4` Fabrica |
| **Motors on bus** | `MOTOR-1` @ chem · `MOTOR-2` @ wing N exhaust |
| **⚑ unwired** | Fabrica court lamp · forge fan · millhouse *(named on Feeder-Fabrica)* |

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

## Storage

### `VOLTAIC-BATTERY-TRAY-1` — voltaic battery tray
Map: chem-lab · Built: d3000

Carries `VOLTAIC-8-CELL-1`, one-deep, acid electrolyte. ☠ Not food.

`VOLTAIC-JAR-1` (storage wing N, pile assembled), `VOLTAIC-PILE-1` (×6 pairs, vinegar) and `PLATE-MOLD-TRAY-1` (forge staging peg) are all **PAUSE** as of d2312.

**Lead-acid banks** — four pilot jars on parallel trays @ wheelhouse / chem porch tree · **`LEAD-ACID-BANK-Y13-1`** (pilots 1–2, `SW-STORAGE-TIE-1`) · **`LEAD-ACID-BANK-Y13-2`** (pilots 3–4, `SW-STORAGE-TIE-2`). Cell jars, electrolyte, and SOC rows: [resources.md](resources.md) (`LEAD-ACID-PILOT-*`).

## Distribution

### ✓ **`EC-1-GRID-FEEDER-1`** — campus trunk *(d3890)*
Map: **`WW-2` wheelhouse → craft path → chem porch east** · Built: d3890 · **~5–6 h install class**

**~22 m run** · paired **0.9 mm bare** **`WIRE-CU-GEN2-1`** · **`SW-CHEM-FEEDER-1` @ porch entry** · **`GRID-TAP-CHEM-1`** bench-east bus.

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
Map: **`WW-2` wheelhouse → campus path → Officina `CRAFT-WING-1` east jamb** · Built: d3976 · **~6–7 h install class**

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

★ **Default: `SW-CRAFT-FEEDER-1` OPEN when bay idle** — **sole Officina building entry d4987** *(craft + storage + north work wing bus)*. ✓ **Domus margin branch d4563** · ⚑ **storage wing room lamps** · ⚑ **Horreum defer**.

### ✓ **`EC-1-GRID-FEEDER-FABRICA-1`** — Fabrica hub compound trunk *(d4986–4987)*

Map: **`WW-2` wheelhouse post tree → `WW-HUB-TOWER-1` south apron** · Built: **d4987** · **~44 m paired class** *(reclaim ex-Feeder-3 + pt1 splice)*

**`SW-FABRICA-FEEDER-1` @ hub south cheek** · **`EC-1-TAP-BOX-STD-4`** · **`GRID-TAP-FABRICA-1` LIVE** · **~7.9 GB @ gen ON** · **R ~2.1**.

★ **Separate entry from `EC-1-GRID-FEEDER-1` chem porch** — **two switches · one compound.** Branches (court lamp · forge fan · millhouse) **⚑ named · unwired**.

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

★ **`SW-CRAFT-FEEDER-1` = Officina building master d4987** · **`SW-WING-N-FEEDER-1` DEPRECATED** · **`SW-WING-N-LIGHT-*` = local lamps** · **building + lamp switch OPEN** to glow.

### ✓ **`EC-1-GRID-BRANCH-WING-N-LIGHT-2`** — centre table lamp *(d4847)*

Map: **`GRID-TAP-WING-N-1` → `Z-LIGHT` sleeve 2 → `WING-N-CEILING-CLEAT-2`** · **`BULB-WING-N-LAMP-2`**

**~4.0 m** paired **0.5 mm** · **`SW-WING-N-LIGHT-2` @ cleat** · **separate branch** · **commission T1–T5 PASS d4847**.

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

| Materials logged d4848 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.38 kg** |
| **`ST-STR-BUTTON-Y13-3`** | **−~22 g** |
| **`FUSE-LINK-Y14-1`** | **−×1** |
| **`FURNITURE-SELECT-1` / `TILE-TF`** | **bench + tray** |

★ **Portable loads via `CP-G-WING-N-PORTABLE-1`** (`CP-G-PLUG-PROTOTYPE-Y14-1` @ bench hook) — **remove plug when wing idle** · **`WING-N-EXHAUST-1` ON before bench energize** · lead-acid @ north bench only with exhaust running.

### ✓ **`EC-1-GRID-BRANCH-DESK-1`** — craft-wing desk lamp *(d4558)*
Map: **`GRID-TAP-CRAFT-1` → desk rafter cleat** · **`BULB-FEAST-LAMP-Y14-1`**

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

### ✓ **`EC-1-GRID-BRANCH-STORAGE-WING-LIGHT-1`** — storage north shelf lamp *(d5012 · fuse d5016)*

Map: **`GRID-TAP-CRAFT-1` → turris west → storage N rafter** · **`BULB-STORAGE-WING-LAMP-Y14-1`** *(hung d5015 · bulb d5019)*

**~3.5 m** paired **0.5 mm** · **`SW-STORAGE-LAMP-1` @ cleat** · **partial insulate** · **LAMP-H fused d5016** · **not commissioned**.

| Materials logged d5012 | |
|---|---|
| **`O-1-MALACHITE`** | **−~0.46 kg** |
| **`WAX-Y10-RENDER-1` / `ROSIN-1`** | **−~8 g / −~4 g** |
| **`FLAX-SHIVE-Y8-21`** | **−~10 g** |
| **`NAIL-IRON`** | **−×3** *(cave)* + peg |

| Materials logged d5016 | |
|---|---|
| **`FUSE-LINK-Y14-1`** | **−×1** · branch seat |

### ✓ **`EC-1-GRID-BRANCH-STORAGE-WING-LIGHT-2`** — storage south bench lamp *(d5013 · fuse d5016)*

Map: **`GRID-TAP-CRAFT-1` → turris S → S bench rafter** · **`BULB-STORAGE-WING-LAMP-Y14-2`** *(hung d5015 · bulb d5019)*

**~3.2 m** paired **0.5 mm** *(dress d5013)* · **`SW-STORAGE-LAMP-2` @ cleat** · **partial insulate** · **LAMP-H fused d5016** · **not commissioned**.

| Materials logged d5013 | |
|---|---|
| **`WAX-Y10-RENDER-1` / `ROSIN-1`** | **−~7 g / −~3 g** *(S share)* |
| **`FLAX-SHIVE-Y8-21`** | **−~6 g** |

| Materials logged d5016 | |
|---|---|
| **`FUSE-LINK-Y14-1`** | **−×1** · branch seat |

★ **Chem lab room lights:** **×2 interior only** · **even spacing · wing-N pair grammar** · **`SW-CHEM-LAB-LAMP-1` only** · [retcon](../journal/retcons/CHEM-LAB-LIGHTS-Y14.md).

### ✓ **`EC-1-GRID-BRANCH-CHEM-LAB-LIGHT-1`** — chem lab lamp 1 *(d5013 · hang d5015)*

Map: **`GRID-TAP-CHEM-1` → east jamb → rafter 1** · **`BULB-CHEM-LAB-LAMP-Y14-1`** · **`BULB-LAMP-CHEM-LAB-Y14-1` seated**

**~3.8 m** paired **0.5 mm** · **feed → `SW-CHEM-LAB-LAMP-1` @ interior east cleat** · **partial insulate**.

### ✓ **`EC-1-GRID-BRANCH-CHEM-LAB-LIGHT-2`** — chem lab lamp 2 *(d5017 · hang d5015)*

Map: **`GRID-TAP-CHEM-1` → rafter 2** · **`BULB-CHEM-LAB-LAMP-Y14-2`** · **`BULB-LAMP-CHEM-LAB-Y14-2` seated**

**~3.7 m** paired **0.5 mm** · **load → same `SW-CHEM-LAB-LAMP-1` lugs** · **partial insulate**.

| Chem room | |
|---|---|
| **Switch** | **`SW-CHEM-LAB-LAMP-1` only** · **OPEN default** |
| **Fuse** | **LAMP-H @ chem tap · d5016** · **not commissioned** |

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

