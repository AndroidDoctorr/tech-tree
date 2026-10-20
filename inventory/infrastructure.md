# Infrastructure

Installed plant — it stays put, it gets maintained, and it has a service history. Schema and the routing test are in [index.md](index.md).

Not a table. Each item is a block, because the thing that matters about a kiln is not a number in a cell.

```
### `ID` — what it is
Map: where · Built: d#### · Last service: d#### · Interval: —

Prose. Capacity, quirks, what breaks, what it feeds.
```

**Map vs here.** The [map](../map/index.md) says the thing is there and describes the space around it. This file says what condition it is in. Service *intervals* live here; the *due date* is a [periodic.md](../checklists/periodic.md) row, because dates are clocks and clocks are not inventory.

---

## Chemical

### `NITRE-BED-1` — nitre bed
Map: north lee · Interval: turn ~every 3 weeks

Clay pan and sump, oak crib, shake lean-to. **✓ Y15 leach + boil d4906–4907** — **~145 g crystal class** · bed recharged loose · tail strip optional in-band until 31 Oct. **Next turn ~d4924**

A slow biological process; a neglected bed does not catch up, it loses the year. Damp, never wet, never trodden. Weakening ammonia is the good sign, and no bloom in cold weather is expected rather than a failure. Turning is `NITRE-TURN` in [periodic.md](../checklists/periodic.md); the autumn conversion is `NITRE-BOIL` in [processing.md](../government/procedures/processing.md).

### `URINE-CROCK-1` — nitre feed crocks
Map: pen rail · domus north step · ×2

Charged d3195. Pour over `NITRE-BED-1` when full — `NITRE-FEED` in [triggers.md](../checklists/triggers.md).

### `ANNEAL-SAND-BATH-1` — annealing sand bath
Map: chem east

Load 13 cleared, ready for the next load.

### `CHEM-SLIP-SHELF-1` — slip jar shelf
Map: chem porch east cheek · Built: d2742

Slip jars ranked; fire-table pegs cleared.

### `VAC-BENCH-1` — mercury vacuum bench *(frame + pan LIVE)*
Map: **chem porch north cheek** · **`VAC-BENCH-SITE-Y14-1`** · Opened **d4454**

Oak **bolt-down frame** (`VAC-BENCH-FRAME-Y14-1`) per d4453 stake — column sill notch · cork-plate cleats. **`VAC-BENCH-PAN-Y14-1`** — **~0.72 × 0.55 m** lead-lined floor pan · **25 mm oak lip** · **NW sump**. **`VAC-BENCH-MANIFOLD-Y14-1`** — oak block · **`AIR-PUMP-2` @ shelf clamp** · column stub capped · **`P-LAB-STOPCOCK-1` bleed** · **`VAC-BENCH-CORK-PLATE-Y14-1`**. ✓ **Rough vac trial PASS d4455** — partial vac · cork-limited hold. ☠ **Spill containment only until Hg loop commissioned** · **`LAB-FUME-CABINET-1` blast-gate stop 3** when distill/Hg work starts. **`VAC-COLUMN-Y14-1`** — **mounted @ column stub** *(d4463)*. **`VAC-CISTERN-DISH-Y14-1`** — **@ lead pan sump · dry**. ✓ **Dry assembly LIVE** — **no Hg**. **`VAC-FALL-TRAP-Y14-1`** + **`VAC-FALL-HEADER-Y14-1`** *(d4466)* — trap plumbed above cistern. ✓ **`VAC-HG-LOOP-Y14-1` ~200 g** charged d4467 · ✓ **first fall test PASS d4467** — holds **~680 mm** class · beats rough pump on cork · ✓ **`VAC-FALL-OSCILLATOR-Y14-1`** long run **PASS d4468** — **~247 falls / ~10 h** · **~705 mm** hold · cork candle **~120 s** class · **not room blackout yet** trials. ⚑ **Long fall · envelope · bulb**.

### `LAB-FUME-CABINET-1` — bench fume hood
Map: **`CHEM-LAB-WING-1` south bench west bay** · Slated **d3840** · Live **d3843** · Proof **CLOSED d3876**

**~1.20 × 0.72 × ~0.92 m** oak frame · **tile-lined interior** · **fire-table tile floor inherited** · rear plenum throat **~118 × 96 mm**. **Duct** — **×8 `TILE-TF` flat liner** *(kaolin floor tile class · not brick · not **`TILE-TR` roof)* · N-wall run ~2.1 m + riser ~0.9 m → chase **LIVE**. **Interior walls** — **×14 `TILE-TF` cut** *(retcon [TILE-TR-TF-FUME-CABINET-Y12.md](../journal/retcons/TILE-TR-TF-FUME-CABINET-Y12.md))*. **Make-up inlet** @ east-door toe **LIVE** · **three-stop blast gate** @ plenum *(slide forged **`NAIL-IRON` ×8**)*. **Glass sash** — marver-blown lite ~1.16 × 0.45 m · ~12 cm working gap. **Smoke proof PASS** d3843 · **SO₂ roast PASS** d3875 · **iron tarnish PASS** d3876 · **distill lane LIVE** · **separation + arsenic immobilization FILED** d3876–3879.

### `VOLTAIC-BATTERY-TRAY-1` — voltaic battery tray
Map: chem-lab · Built: d3000

Carries `VOLTAIC-8-CELL-1`, one-deep, acid electrolyte. ☠ Not food.

`VOLTAIC-JAR-1` (storage wing N, pile assembled), `VOLTAIC-PILE-1` (×6 pairs, vinegar) and `PLATE-MOLD-TRAY-1` (forge staging peg) are all **PAUSE** as of d2312.

### `BITUMEN-POT-1` — bitumen pot
Map: cart yard

Holds `BITUMEN-BULK-1` — quantity in [resources.md](resources.md). Chem read PASS. ☠ Not food.

## Ceramics

### `POT-WHEEL-2` — potter's wheel
Map: v1 wheel lane · Built: d2604

Flywheel ~12 kg, splash pan, coast ~45 s.

### `PORC-BASIN-1` — culina main sink basin
Map: culina S · Built: d2725

~30 cm, drains to `DR-ST-01`. Glaze deferred.

### `CULINA-FAUCET-BRASS-1` — main sink tap
Map: culina S main sink · Built: d2726

Twin brass tap. Cold filter branch, hot mix.

## Fuel and fire

### `CHAR-RETORT-1` — charcoal retort
Map: pit lane north berm, cell C · Built: d1777

**`MUSKET-FIRE-CRADLE-Y13-1` @ d4224** — oak V-jaws · sand weights · muzzle → berm · **~2.4 m trigger cord** · standoff grammar per d4168.

~+15% yield over an open pit.

### `CHAR-RETORT-2` — charcoal retort
Map: cell D · Built: d3032

Shares a wall with `CHAR-RETORT-1`. ~+17% on trial. The pair run as `CHAR-RETORT-TWIN-CELL-1`, a C/D parallel ×3 grammar.

### `CHAR-RETORT-QUAD-CELL-1` — quad charcoal retort bank *(BUILD)*
Map: pit lane north berm · cells E/F · central flue between C/D and E/F · Started: d4297

**Phase 1 ✓ d4297:** north berm extension scrape · E/F dish pads · central flue trench · **×28 `BRICK-FIRED-B` base rings** · mortar cure overnight.

**Phase 2 ✓ d4299:** E/F shared meridian · flue cheek tie to C/D bank · **twin mound shells ~40 cm** · cap plugs staged · **~85%**.

**Phase 3 ✓ d4301:** E/F port set · central flue manifold · **`CHAR-OFFGAS-BURNER-1` LIVE** · **`CHAR-DRY-RACK-1` LIVE** · **~95%**.

**Commission ✓ d4302:** **~38 kg feed → ~11.8 kg char** · off-gas burner PASS · dry rack pre-dry PASS · **✓ LIVE**.

**Grammar:** **`CHAR-RETORT-QUAD-CELL-1` · ×3 parallel** — **~36–40 kg feed → ~11–13 kg char nominal** · pre-dry splits on `CHAR-DRY-RACK-1` when time allows · twin C/D remains valid for lighter days.

### ★★ `CUPEL-HEARTH-1` — cupellation hearth and litharge recovery
Map: **SW fume shelf below the forge** · Sited **d3297** · Built **d3299** · ✓ **Commissioned d3300** · ⚠ **draught adequate, little margin**

**Dished brick bed for a renewable bone-ash cupel · low cross-blast tuyère** *(the air must sweep the surface, not stir the bath)* · **close hood · ~23 m flue up the shelf slope · settling chamber ~1.2 × 0.8 m with a sweeping hatch, floor falling to one lip · damper · small adjustable draught fire at the stack base, past the chamber** · ⚑ ★★ **a SIZED LOW INLET at ~1.5× the throat — the first on this campus.** ~550 brick.

> ★★★ **THE FLUE DOES TWO OPPOSITE JOBS AND MUST DO THEM IN DIFFERENT PLACES.** *Cold at the near end where the vapour still carries its load; hot at the far end where the only job left is to pull.* ☠ **Never warm the cooling run to improve the draught — that is the product.**
> ★★ **Stack stands on top of the RISE, not on top of the flue** — *draw is the difference between the ends.*

> ☠ ★★★ **DRAW HAS A CEILING AS WELL AS A FLOOR.** *Fast gas carries dust past the chamber and out.* ★★★ **Set the damper by MASS BALANCE, never by eye** — **lead in · bead out · sweepings out · shortfall is the loss.** ✓ **d3300 baseline: ~400 g poor galena → ~150 g litharge, ~42%.**

⚒ **Rodding doors every ~2 m of the cooling run outstanding** — ★ *most of the shortfall is furred to the flue wall in the first few metres, recoverable, and there is no way in.* **~42% → ~⅔.**

☠ ★★★ **Sited for CAPTURE, not distance.** *A colony works a three-kilometre disc and this campus is a dot near the middle of it, so no arc of the compass is free of bee forage and "far enough away" is an empty category.*

> ★★★ **THE FLUE IS A RECOVERY FITTING THAT HAPPENS TO BE THE SAFETY.** *Litharge is nine-tenths of the charge — reducible to lead, a flux, a glaze, and the drier for linseed varnish.* ☠ **A hearth that vents cleanly has solved the poisoning by throwing away the charge.**

⚠ **Throughput is limited by `BONE-BANK-1`, not by the hearth** — *~20 cupels is one pass through `GALENA-1`.* ✓ **Used cupels are banked ore, kerbed with the galena, never discarded** — see [resources.md](resources.md).

☠ ⚑ **Lead gives no warning of any kind.** *Never eat or drink at the hearth · sweep wet, never dry · ⚠ **a flue sweep is a LEAD job, not a chimney job** · hearth clothes stay at the hearth · wash before the kitchen every time.*

### `KILN-D-STACK-2` — kiln D chimney, terminal and damper
Map: kiln terrace · Original stack: d2516–d2529 · Upgraded: d3324

**~4.15 m**, constant bore. Original weather hood was the choke: total side free area only ~0.7× bore, so wind suction sometimes masked weak still-air draw. Upgrade re-levelled the cap ring, added a modest tied course, and rebuilt the hood with symmetric free area **~1.6× bore**.

`KILN-D-STACK-DAMPER-1`: fired-tile upper slide, stops at **full · working-mid · minimum-safe**. ☠ **No closed position.**

★★★ **The plenum pushes and the stack pulls; the chamber must remain slightly negative.** Height supplies pressure margin. Damper + plenum bleed set the operating point.

✓ Cold smoke and low draught fire PASS d3324. ◐ Partial hot proof d3331 at bisque band. ✓ **Full hot proof PASS d3332 at stoneware hold** — cone · seam · plenum · damper · fuel curve logged together.

### `KILN-D-PLENUM-1` — kiln D air plenum
Map: belt tree · Built: d2530

~4.5 L buffer, twin outlet, bleed cork. `WW-2` link PASS.

## Electrical generation

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

★ **`SW-WING-N-FEEDER-1` DEPRECATED d4987** — use **`SW-CRAFT-FEEDER-1` only.** Layout: [officina-n-work-wing-layout.md](../plans/officina-n-work-wing-layout.md).

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

### ✓ **`WING-N-MOVE-IN-CY13-4859`** — shelf · curtain · cabinet · spill peg *(d4859)*

West shelf · hub curtain · south boot mat · **`WING-N-SPILL-PEG-1` + waste crocks ×2** · **`WING-N-LAB-STOOL-1`** · **`WING-N-CABINET-1` loaded** · RH read **~57 %** · exhaust **✓ d4860**.

### `MATERIARUM-PAD-1` *(pile 4 north · kiln B margin)*

**Staked d4878** · **~10×3 m ghost · ×4 bays** · subgrade **✓ d4879** · **`MATERIARUM-BLIND-DRAIN-1` ✓ d4880** · **~35 mm gravel bed ✓ d4880** · **pozz wear slab ✓ d4882** · **✓ `MATERIARUM-PHASE1` d4891** — **×3 separators course 1** · **✓ back + outer sides course 1 d4901** *(×60 wythe · south mouths open)* · **course 2 gate: bay fill nears lip / spill over wythe** · ⚑ **`BLOCK-PAD-1`** small pour pad for block stack · **`BLOCK-BENCH-PAD-1` ✓ wear slab d4916 · cure PASS d4923** *(~3.2×2.1 m · **`BLOCK-BENCH-LINE-SHAFT-1` LIVE d4918** · **`BLOCK-BENCH-FRAME-1` LIVE d4926** · plan [block-bench-water-wheel.md](../plans/block-bench-water-wheel.md))* · **`SHOVEL-BULK-1` ✓** · **`WHEELBARROW-2` ✓ d4895** @ pile 4 north peg · **`MATERIARUM-STOCK-1` d4896** — bay 1 pozz · bay 2–3 gravel · bay 4 sand **~62 kg class post-d4914** · apron gravel **~12 kg**.

### ✓ **`EC-1-GRID-BRANCH-WING-N-MOTOR-1`** — north exhaust fan *(d4860)*

Map: **`GRID-TAP-WING-N-1` → `Z-MOTOR` sleeve → `WING-N-EXHAUST-1` / `MOTOR-2`**

**~4.1 m** paired **0.5 mm** · **`SW-WING-N-MOTOR-1` @ east jamb** · motor-class fuse **~0.22 I** · **commission T1–T5 PASS d4860** · **exhaust ON before lead-acid charge @ north bench**.

### ✓ **`WING-N-EXHAUST-1`** — north work wing exhaust *(d4860)*

**`TILE-TF` duct ~1.6 m** · north cheek vent · **`MOTOR-2` direct-drive prop** · **`SW-WING-N-MOTOR-1`**.

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

### ★★★ `ARMATURE-2`
In service in `GEN-WW-1` · Wound: d3267

5 × 145 turns at 0.65 mm, ~182 m. Drawn down from `ARMATURE-1` with **no melt** and annealed each pass, which is why the copper survived the redraw.

⚠ `ARMATURE-3` — a coarse winding for `CU-CELL-1` — is **not built** and needs ~500 g. ★ No longer urgent and no longer a deadlock: the series pair recovers ~25% without it.

### `MOTOR-1` — bench motor *(LIVE)*
Map: chem porch bench east · **`GRID-TAP-CHEM-1`** · Opened: d3951 · **✓ LIVE d3964**

**PM-field bench motor** · **`ST-MAG-1` field** · **`ST-STR-1` frame** · **first grid-fed campus consumer**. ✓ **`MOTOR-1-FRAME-1` d3952** · **`MOTOR-1-YOKE-1` + `MOTOR-1-MAG-STACK-1` d3957** · **`MOTOR-1-CORE-1` d3958** · **`MOTOR-1-COMMUTATOR-1` d3958** · **`MOTOR-1-ARMATURE-1` d3963** · **`MOTOR-1-BRUSH-1` d3964**. **Measured d3964:** **R ~3.8 · stall torque ~100 mN·m @ 55 mm arm · ~0.13 I @ ~100 g load**. ⚑ **load fixture · pole-gap shave optional**. Reference: **`PEDAL-GEN-1`** · **`GEN-WW-1-CORE-1`** · **`EC-1-GRID-FEEDER-1`**.

### `PEDAL-GEN-1` — pedal generator
Map: chem porch · Built: d3198

`EM-COIL-3` armature, ~3 mm gap, `COMMUTATOR-1`, ~5–11° needle. Output scales with pedal.

`COMMUTATOR-1`: oak boss, ×2 copper split segments in wax, copper leaf brushes ×2 plus ×1 spare, timed to the neutral plane. `MAG-STACK-2`: rods #8 · #12 · #16 · #19 plus yoke, lift ~65 mm — the field. `EM-COIL-3`: ~280 turns gen-2 on a ~185 g iron core, bench fixture at chem porch, leads C/D.

## Electrochemistry

### ★★ `CU-CELL-1` — copper electrowinning cell
Map: chem porch, on `GEN-WW-1` · Built: d3258

Big-area cathode, **carbon anode** — inert, so oxygen comes off at the anode and the acid is regenerated. The tip erodes and is consumable. Stirred, iron-sweetened.

★ Doubles as a **coulometer** — it weighs charge. Runs continuously at ~40 g/day of wheel time and needs two looks a day and nothing else. Those looks are `CU-CELL-TEND` in [daily.md](../checklists/daily.md).

⚠ A spongy deposit means **too much current in too little area**, not a bad bath.

### ★★ `CU-CELL-2`
Map: chem porch · Built: d3268

In **series** with `CU-CELL-1` for ~+25% copper per day at no extra power. Two is the optimum — three or more spends more headroom than it buys.

### ★★ `LIQUOR-CASCADE-1` — inter-cell launder
Map: between the cells · Built: d3268

☠ **Never a full pipe.** A continuous column of electrolyte is a wire, and it shorts out the cell it bypasses. The air gap is the whole design.

### ★★★ `WATER-CELL-1` — electrolysis cell
Map: **outdoors** · Built: d3267

Divided. ~2.0 GB at ~0.27 I, both electrodes gassing steadily.

⚠ **No storage yet, and hydrogen leaks through everything.** Outdoors is not a preference.

### `CHLOR-ALKALI-CELL-1` — undivided brine bleach cell
Map: chem porch **south outdoor pad** · Built: d3454

~4 L stoneware crock · saturated brine · carbon anode · iron cathode · open downwind. **`GEN-WW-2` supply-class.** Makes hypochlorite in liquor — not separated Cl₂. ☠ **Outdoor only · downwind · never the enclosed porch.**

### `ELECTROLYSIS-CELL-1`
Map: chem porch

Crock, copper cathode, inverted `GLASS-BOTTLE-9` for capture. ⚠ **Anode needs lead or carbon.**

### `ANODE-NARROW-1`
Lead strip ~15 × 60 mm, brown PbO₂ formed, evolves O₂ steadily. Recast from `ANODE-PB-1` at d3205.

## Gas

### `GASHOLDER-1`
Map: officina · Built: d3203

Bitumen oak bath. Bell A H₂ ~0.9 L, Bell B O₂ ~0.45 L — **full, about 85 s of flame**. Guides, hoods, keyed dip-tube lines, pinch clamps, fill line marked.

### `GASHOLDER-2`
Map: craft wing · ~60% built · Last: d3209

Tub ~0.55 × 0.45 m lined and scrimmed. Bell A ~9.5 L done, crown battened and air-tight. ⚠ Bell B ~4.8 L — bevels need re-cutting. Guides cut long. **Cocks blocked on `BRASS-POUR-1`.**

### `GAS-TERMINALS-1`
×4 copper binding posts, threaded at `LATHE-V2` · ×2 copper leaf clips · cathode post notched. Built d3203.

## Water and power

### `SLUICE-2-GATE-2` — sluice 2 gate *(upgraded d4046)*
Map: `S2-0` · Built: d1878 · **indexed d4046**

Three-stop intake: **SUMMER · NORMAL · FLOOD** — iron pintle + latch · rack pin stops · **`SLUICE-2-STAFF-GAUGE-1`** @ south cheek *(0 · 10 · 20 cm · ties to `T-1` stain)*. Bypass spill board west cheek · seasonal swap grammar unchanged.

| Stop | Q to race *(June low fork · d4046)* |
|---|---|
| **SUMMER** | **~11 L/s** |
| **NORMAL** | **~17 L/s** |
| **FLOOD** | **~3 L/s** *(bypass carries rest)* |

Stream cheek `SLUICE-2-STREAM-CHEEK-1` ~10.2 kg; sill skim `SLUICE-2-SILL-SKIM-1` ~3.8 kg at the gate seat.

### `SLUICE-2-RACEWAY-1` — sluice 2 raceway
Map: `S2-0` → WW-yard pad · Built: d1879

~180 m · **~7.2 m head** lip → wheel pad · **✓ forebay feed `HYDRO-ELEC-1-RACE-FEED-1` @ south wing bench d4555**.

| Q read | Date | Flow | Notes |
|---|---|---|---|
| d1881 | Cal-Y6 D184 · ~23 Jun | **~16 L/s** | Summer-low baseline · bypass + seep honest |
| d4045 | Cal-Y13 D173 · ~11 Jun | **~17 L/s** | June class · not spring peak · bypass **~1.2 L/s** |
| d4555 | Cal-Y14 D315 · ~29 Oct | **~10.9 L/s** | Autumn nadir · **forebay feed LIVE** · gate **SUMMER** |

### `HYDRO-ELEC-1-PENSTOCK-1` — forebay outlet culvert
Map: gorge filter toe → gate footing ghost · Installed: d4512

**~8 m** buried run · **`PT-22-A` ×4 @ ~2.0 m** · socket + oak wedge + M-08 wipe · rodding eye @ mid-bend. ✓ **Live @ filter toe d4524** · blind cap **stowed @ gorge kit peg**. ✓ **`OUTLET-GATE-HARDWARE-Y14-1` mounted d4520** · ✓ **outlet flood test d4524** · ✓ **crest/spillway pour d4532**.

### `WW-2-WHEEL-1` — water wheel 2
Map: north pad · Built: d1894

The prime mover. Belt tree live off it.

`BRONZE-BUSH-WW2-1` at the axle bed, cast d1884, ~320 g. `GS-2-FLYWHEEL-1` outboard on the shaft — ~9.8 kg oak with a ~290 g iron band, d1888. `LEATHER-FLAT-BELT-1` on the rim, ~4.2 m, **dressed weekly**.

### `BELT-TREE-1` — power distribution
Map: `WW-2` · Built: d1891–d1892

×3 idlers, ×3 pulleys, collar #3. `WW-2-BELT-COLLAR-1` is a set of ×4 quick-release collars on the shaft — #3 drives the kiln, #4 the cellar fan (added d3018). **`WW-2-BELT-COLLAR-5`** **✓ d4918** → **`BLOCK-BENCH-LINE-SHAFT-1`** **LIVE** on **`PATH-CROWN`** *(full run · brake @ post 4 · bench hub stub · no frame load)*.

`WW-MACHINE-FLYWHEEL-1` (MF-1) at idler B with clutch collar #3 — ~3.6 kg disk, `WW-MACHINE-SWITCH-1` live since d1973. `GRIND-TAKEOFF-2` is a cord branch to `GS-1`. `TRIP-HAMMER-BELT-1` is a ~1.8 m leather cam.

**Clutch A–D** *(d3553)* — **one live:** **A** lathe direct · **B** `LATHE-TORQUE-GB-1` reduced · **C** `BORING-MILL-1` direct · **D** `MILL-TORQUE-GB-1` reduced. Collar **#4** stays cellar fan.

★ One wheel, one belt tree, and every powered tool on the campus hangs off it. A failure here stops the saw, the lathe, the drill press, the trip hammer, the cellar fan and the generator at the same time.

## Cold store

### `COLD-CELLAR-FAN-1` — cold cellar fan
Map: `WW-2` collar #4, duct to horreum ice vault · Last service: d3189

Flap balanced across both the old and the new niche.

### `ICE-VAULT-NICHE-2` — ice vault niche 2
Map: horreum north cella · Built: d3189

~1.2 × 1.0 m, lined c1–c5, straw/shive void, oak lid. Holding ~+40 kg. Cure to 8 Feb.

### `ORE-BAY-1` — covered ore store and vitriol catch
Map: `WW-YARD` west of the forge · Built: **d3291**

**Puddled clay pan sloped to one corner · coarse stone bed · one-course dry-laid kerb · sunk lidded catch pot at the low corner · roofed lean-to off the forge wall.** ⚑ **Galena in its own kerbed bay, marked, handled separately.**

☠ **Built because sulfide ore left in the weather makes acid, and the yard slopes to TRIB-1.** *The same design as `VITRIOL-HEAP-1` at Kisecik, scaled down and roofed — the heap wants rain, this does not.*

> ★★★ **The catch pot is an instrument, not a drain fitting.** *`VITRIOL-HEAP-1` is a farm that cannot be observed between visits; this is the same reaction at a tenth of the scale, under the eye, daily.* ✓ **Pale liquor after 4 wet days (d3294)** — ⧗ **whatever it teaches about rate arrives ~90 days before the Kisecik sump is opened.**

⚠ **The liquor carries arsenic as well as acid** — see [resources.md](../map/region/resources.md) district hazards.

## Food processing

### `ACORN-LEACH-TROUGH-1`
Map: pool margin · Built: d2689

**Empty @ d4226** — **`ACORN-LEACH-Y13-1` PASS · triple-rinse** · **`ACORN-ROAST-Y12-1` ~615 g @ Horreum A nut tray** *(prior batch · d3787)*.

### `ACORN-LEACH-TROUGH-2`
Map: pool margin N · Built: d2718

**Empty @ d4227** — batch 2 moved to **ditch-flow sack @ ditch W**.

### `ACORN-DITCH-FLOW-SACK-1`
Map: ditch W · below `RETT-TROUGH-FLAX-1` rinse lip · ad hoc d4227

**LIVE @ d4533** — **`ACORN-LEACH-Y14-1` soak 3 ~680 g @ ditch W flow** · peg below rinse lip.

Both are the **fallback**, not the primary. Running water in the ditch leaches faster than serial still soaks ever will, because a still trough reaches equilibrium and stops working until it is changed. The troughs are for a batch that cannot be watched. See `ACORN-LEACH` in [processing.md](../government/procedures/processing.md).

### `EVAP-RACK-1` — salt evaporation rack
Map: — · Interval: seasonal

**`SALT-EVAP-SPRINT-Y14-2` cycle 2 CLOSED d4578** — trays empty · rinse-dry · pour #3 if band allows. *(Cycle 1 ✓ d4205.)*

### `COOL-CELLAR-2-EVAP`
Map: cellar north margin

Trough flushed, drain clear.

## Storage fixtures

### `AMPHORA-5`
Map: — · Vinegar

Holds `VINEGAR-Y6-1` with the Y8 fork top-up. Mother live in a separate crock.

### `AMPHORA-6`
Map: `OLIVE-PRESS-1` cool-step · Oil

**`OIL-Y15-1` decant ✓ d4953** · clear @ bottle rack · **`OIL-Y15-2` ~0.59 L crude settling** @ cool-step · **`OIL-SEDIMENT-Y15-1` ~125 ml @ foot** · **`OLIVE-BRINE-Y15-1` @ `OLIVE-JAR-Y15-1`**.

### `AMPHORA-7`
Map: cold tap branch · Built: d2567

Carries the `CULINA-POTABLE-FILTER-1` column. ★ **Potable — not grey.**

### `AMPHORA-8`
Map: cart yard · Built: d2286

**Empty rinse-dry** @ cart yard post **pour d4575**. M-08 foot ring.

### `AMPHORA-9`
Map: horreum A margin ghost · Built: d2744

**Empty harvest buffer** — rinsed **d4573** · M-08 foot · prior **d3926 / d4202** grammar.

### `BARREL-5-FERMENT`
Map: **horreum A margin ghost** · Built: d3895 · **✓ finished d3896**

**~25–30 L class** · spirit/beer lane · **×4 iron hoops** · **BUNG-TAP-4 breath bung** · **food-oil interior** · **leak weir PASS** · **`GRAIN-FERMENT-Y15-2` ~10 L day 0 LIVE d4959** @ horreum A margin.

### `AMPHORA-10`
Map: horreum A margin ghost · Built: d2744

Harvest / general buffer. M-08 foot ring.

### `NUT-SHELF-EXT-1` — nut bay shelf extension
Map: horreum A nut bay west · Built: d2742

Upper peg rail plus lower split tray, ~1 m.

### Storage jars — `P-μ` and `P-ξ` series

| ID | Duty | Map |
|---|---|---|
| `P-μ-9` · `P-μ-11` | Salt | Horreum A margin |
| `P-μ-10` | Spice | Horreum A margin |
| `P-μ-12` | Parched grain | — |
| `P-μ-13` · `P-μ-14` | Trail pack · pegs dry | — |
| `P-ξ-4` | Vinegar | — |
| `P-ξ-5` | Oil, working draw | v1 / culina |

The jar is the fixture and the duty is stable; what is in it right now is [food.md](food.md). A jar that changes duty gets edited here — a jar that changes level does not.

## Machines

### `TABLE-SAW-1` — powered rip saw
Map: `FABRICA-CARPENTRY-ALCOVE-1` · Built: d3053

Powered rip PASS. `TABLE-SAW-ARBOR-1` ~22 mm shaft on ×2 bronze pillows · `TABLE-SAW-BLADE-1` ×28T, balance PASS · `TABLE-SAW-BELT-BRANCH-1` ~11.2 m leather from `WW-2` via idler B · `TABLE-SAW-FENCE-1` sliding oak, cam lock, square to blade · `TABLE-SAW-GUARD-1` splitter and crown hood, throat clear · `TABLE-SAW-COVER-1` oilcloth flap at the open south side · `TABLE-SAW-FRAME-1` roofed with ×19 TR tiles.

☠ The guard and splitter are not optional furniture. This is the highest-energy tool on the campus and the only one that can take a hand faster than a reaction.

### `LATHE-V2-LEADSCREW-1`
Map: `LATHE-V2` · Built: d2856 · Wear read: d3525 · Gearbox: d3526

`LS-SCREW-1` plus `LS-HALF-NUT-1`, **~1.02 mm/rev** · backlash **~0.42 mm** @ power nut · **hand + power feed live** · **1:1 BN pitch threading certified d3529** · **`SCREW-LATHE-1` retrofit CLOSED**. **`LATHE-TORQUE-GB-1` LIVE d3553** — **~3:1** · spindle **~58 rpm** reduced · clutch **B**.

### `ROPEWALK-1`
Map: `WW-YARD` long run · Built: d3255

Geared 3-hook whirler, grooved top, **travelling** far hook, ~40 m pegged run.

⚠ **The traveller slot needs about a third of the laid length** — a rope shortens ~25% as it closes. A run pegged to finished length will jam.

### `DRILL-PRESS-1`
Map: — · Built: d1894 · Live ~95%

With `BORE-JIG-1`. Repeat bore to ~0.08 mm class. Upgrade path from `CRANK-DRILL-1`, which is still at `WORKBENCH-1` on a belt stub.

### `BORING-MILL-1`
Map: `WORKBENCH-1` east cheek · Opened: d3542 · **LIVE d3553**

`BORING-MILL-BED-FRAME-1` + **`BASALT-BLOCK-2` wear plate** + **`BORING-MILL-HEADSTOCK-1`** + **`BORING-MILL-SADDLE-1`** + **`BORING-MILL-BELT-BRANCH-1`** @ idler B. First **`RC-10`** scrap bore PASS d3547 · **`BORING-BAR-1` PoC** @ peg. **`MILL-TORQUE-GB-1` LIVE d3553** — direct **~145 rpm** clutch **C** · reduced **~36 rpm** clutch **D**. Brass bar pilots defer.

### `LATHE-1` and `LATHE-V2`
Map: `WORKBENCH-1`

`DEAD-CENTER-1` · `SPRING-CENTER-1` · `TOOL-POST-SQUARE-1`. The V2 leadscrew is below.

### `WIRE-COATING-RIG-1`
Map: craft wing · Built: d3232

Melt pot, felt wiper, take-up reel.

### `LIQUID-PUMP-2`
Map: wagon liquid-insert pump peg · Built: d3170

Copper barrel, brass checks, hose paired.

### `AIR-PUMP-1` — bench air pump
Map: craft peg / **`WORKBENCH-1`** clamp · Built: d3930

**`PT-10-A-PROD-1`** WI barrel **~175 mm** · brass twin-flap head · oak piston + leather cup · **~14 ml/stroke class** · hand trial **PASS** d3930.

### `AIR-PUMP-2` — scale bench air pump
Map: **`VAC-BENCH-1` manifold shelf** *(was `WORKBENCH-1` clamp)* · Built: d3949 · **Relocated d4455**

**`PT-22-A-PROD-1`** WI barrel **~175 mm** · brass twin-flap head · oak piston + leather cup · **~68 ml/stroke class** · delivery + rough inlet vac · hand trial **PASS** d3949. ⚑ **vac-specialized duplicate** · compressor duplicate when refrigeration arc names loop. **`AIR-PUMP-CRANK-1`** defer. Not **`LIQUID-PUMP-2`** *(wagon liquid only)*.

## Sanitary

### `PORC-TOILET-1`
Map: east thermae · Built: d2830

Glazed porcelain. Bisque, glaze, install, flush ×4 all PASS. `PORC-TOILET-MOLD-1` retained at the bench — backup cast OK.

## Drainage

### ★★ `BACKDRAINS-T1-T3`
Map: terraces T-1 to T-3 · Built: d3274–d3275

`T-2` ~11 m and `T-3` ~9 m filter drains, graded fill, rodding eyes. **`T-1` was re-graded and needed no drain at all.** All three benches now fall to a chosen outfall.

★★★ **Dug to the layer, not to a depth.** The seepage sits on an impermeable horizon rather than at a fixed depth, so a drain cut to a number misses it. Finding the layer is the job; the trench is the easy part.

### `TIGHT-LAYER-1` — impermeable horizon
Map: under the campus hillside · Located: d3275

Found by following the seepage line. ★ **Where water wants to stand — the probable cistern or pond site.** A liability read as an asset.

### `DUCK-POND-1` — habituation pond
Map: `TIGHT-LAYER-1` · Built: d3494 · Finished: d3504

~4.2 × 4.8 m shallow dish · **~35–40 cm** to tight pan · uphill berm · chip spillway to backdrain line. Seep-fed · slow fill class.

✓ **Reed margin** · **`DUCK-NEST-PLATFORM-1`** on berm · **`DUCK-SCRATCH-STATION-1`** grit/grain tray. ☠ **Habituation only — Mar–May nest watch · not a trap Y1.**

### `ASPHALT-TEST-1`
Map: hub S apron · Built: d2583

~0.6 × 0.4 m strip, ~18 mm crown. ☠ Not a food path.

## Benches

### `WORK-STAGING-TABLE-1`
Map: storage wing E · Built: d2400

~1180 × 620 × 880 mm. Lower shelf staging.

### `WORK-TABLE-ATELIER-1`
Map: officina west cheek · Built: d2407

~900 × 450 × 760 mm. Craft knee.

### `WORK-TABLE-CULINA-1`
Map: culina S prep · Built: d2408

~1000 × 550 × 860 mm. Wipe-down top.

### `GYROS-SPIT-HEARTH-1` — hearth rotisserie *(gyros-class)*
Map: culina south hearth · Built: d4913

Oak fork uprights · **`REBAR-STD-Y13-1` class spit rod** · drip tray · hand quarter-turn · counterweight string. **Not** a vertical shop spit — honest **leg roast + shave** for emmer flat wraps per [food-menu.md](../government/procedures/food-menu.md).

### `BLOCK-BENCH-FRAME-1` — vibratory block press frame *(phase 3)*
Map: **`BLOCK-BENCH-PAD-1` @ `MATERIARUM-1` SE** · Built: d4926

Oak sill + **×4 legs** · **dual mould nest A/B** for **`BLOCK-MOULD-1/2`** · hub tie to **`BLOCK-BENCH-LINE-SHAFT-1`** · drain to apron gutter. **`BLOCK-BENCH-CAM-1` ✓ d4927** · **`BLOCK-BENCH-HOPPER-1` ✓ d4928** · **`BLOCK-BENCH-EJECT-1` ✓ d4930** · **✓ ×8 trial d4931** *(~5 h 40 min · ~⅓ under hand ×8 full day · ⚑ pit chute · hopper gate · ×12 sprint)*

## Field and apiary

### `HIVE-SCALE-1` — hive weight scale
Map: under `TOP-BAR-HIVE-3` · Built: d3265

Platform, three-point, levelled, beam and counterpoise. Baseline logged d3265.

★ **Read at the same hour every day.** A hive weighs less at noon with its foragers out than at dusk, so a reading at a drifting hour is noise. Climbing means flow on, falling means dearth, and a sudden drop on a fine day means it swarmed. Daily row is `HIVE-SCALE-READ` in [daily.md](../checklists/daily.md).

### `SCARECROW-1`
Map: Beds B–D · Built: d3216

Cross frame, loose tunic, straw and shive, rag streamers. **Move it every few days** — birds learn a static device in about four. `BIRD-DEVICE-RESET` in [periodic.md](../checklists/periodic.md).

### `BIRD-RATTLE-LINE-1`
Map: emmer beds · Built: d3216

Cord, shell and bone. Re-run across the scarecrow.

### `HAWK-KITE-1`
Map: Beds B–D · Built: d3217

Split-reed frame, sooted cloth, hung on cord under a bowed sapling. Keel and tail streamer. Needs wind to work at all.

## Retting

### `RETT-TROUGH-HEMP-1`
Map: ditch W · Live

✓ **`P-RETT-33` FIBRE CLOSED d3786** — **`HEMP-LINE-Y12-1` ~860 g** · **`W-1` north cleared** · trough **empty**.

### `RETT-TROUGH-FLAX-1`
Map: ditch W · Live

✓ **`P-RETT-32` CLOSED d3505** — break/heckle/spin · **`FLAX-THREAD-SHINGLE-Y10-1` ~760 m** @ craft peg.

✓ **`P-RETT-34` FIBRE CLOSED d3865** — **`FLAX-LINE-Y12-1` ~1.58 kg line @ `WOOD-CRATE-6`** · spin defer · **`W-1` cleared**.

✓ **`P-RETT-35` FIBRE CLOSED d4236** — **`FLAX-WILD-LINE-Y13-L1` ~0.60 kg @ `WOOD-CRATE-6`**.

✓ **`P-RETT-36` FIBRE CLOSED d4236** — **`HEMP-LINE-Y13-1` ~0.89 kg @ `WOOD-CRATE-6`**.

**`P-RETT-37` ✓ FIBRE CLOSED d4236** — **`FLAX-LINE-Y13-1` ~1.73 kg** · **`ACORN-DITCH-FLOW-SACK-1` empty post batch 2 PASS**.

**`P-RETT-39` ✓ FIBRE CLOSED d4966** — **`FLAX-LINE-Y15-1` ~2.42 kg @ `WOOD-CRATE-6`** · **`W-1` cleared** · **`RETT-TROUGH-FLAX-1` empty**.

The old mud pool is **retired**. The dual trough plus rinse branch runs the two fibres in parallel, which the single pool could not. Live arcs are [crops.md](crops.md); finished line is [resources.md](resources.md).

### `FURNACE-2` — melt furnace *(build)*
Map: Fabrica **south court** · **`FORGE-D`** lean-to margin · Opened **d3658**

**Common datum:** **900 × 900 × 150 mm** @ plan d3586 · **✓ `MUFFLE-1` LIVE d3777** — empty heat PASS · TC seated · **`FURNACE-2`** shell separate · **`CAST-IRON-BUTTON-Y12-1`**

### `FURNACE-2-STACK-1` — melt-furnace exhaust stack
Map: Fabrica **south court** @ **`FURNACE-2`** · Live **d3727**

**Ø120 mm** clear bore · **≥3.5 m** above hearth datum · inner **`BRICK-FIRED-B` stackable** liner · outer forsterite split wrap · tied weather hood. Jacket **Ø90** throat collar · cold draw cert **PASS** d3727 · **`SMOKE-SPOT`** station paired.

### `BLAST-BLOWER-1` — melt-furnace blast
Map: Fabrica **south court** @ **`FURNACE-2`** service · Live **d3721**

Twin alternating box bellows off **`WW-2`** **`MF-1`** south stub (~12 rpm class). Discharge → **`KILN-D-PLENUM-1`** (~4.5 L trial buffer) → tuyère service hose. Bleed sets blast; hand bellows path retired d3721. Cold spin @ tuyère **PASS** *(no stoke)*.

### `WAGON-GARAGE-1` — wagon garage
Map: `CART-YARD` south · Built: **stem d3375 · frame d3376–3378 · roof d3379** · Pad/drain: d3283

**~3 × 6 m bay** — block socle ×7 · **DPC band d3515** · oak frame + **×4 iron straps** · **BC-2 timber walls d3513** · **board-and-batten front + double doors d3515** · **shake/M-08 roof d3379** · **Norima default park under cover.** Utility CLOSED · **`WAGON-GARAGE-2` future.** Ring beam N/A.

---

## Farm and holding

### `HOLDING-WIND-BREAK-1`
Map: north lee · Built: d3098

Brush, straw, shive pack.

### `NITRE-BED-COVER-1`
Map: north lee · Built: d3223

Dark sun-side cover over `NITRE-BED-1`.

## Trail and outposts

### `METROLOGY-CELLAR-1` — reference cellar @ `CAVE-1` upslope
Map: `CAVE-1` dry niche **~8 m upslope** · Built: d3502 · Last service: d3502

Lime-washed · plaster-skinned mouth cavity @ **~9 °C** stable. Drain lip keeps seep below floor. **`REF-CELLAR-SHELF-1`** levelled for reference duplicates and long-season checks.

☠ **Not food · not seed · not general cool store** — metrology lane only. Rear pool and seep horizon unchanged.

### `CAVE-3-FIXED-LINE-1` — fixed line, CAVE-3 approach
Map: `CAVE-3` approach · Built: d3221

~9 m hemp on ×2 rock spikes. Live.

The rope is not a `resources.md` row — once it is rigged and load-bearing it belongs to the installation, and it is inspected rather than counted.

### `CAVE-3-PATH-1`
Map: `CAVE-3` approach · Built: d3221

×11 out-canted steps · ~4 m diversion trench · drip lip · fixed line · ×2 skid stones in the crawl.

The steps are canted **outward** deliberately — an in-canted step holds water and ices.

### `CAVE-3-SHELF-1`
Map: `CAVE-3` · Built: d3221 · **lip strip d3458**

Dry-stone. Slab ~1.1 × 0.5 m on ×3 corbel piers, ~0.5 m up, a hand's width clear of the wall. Load-tested. **Oak lip pinned d3458.**

★ The wall gap is the design. Stored goods touching cave rock wick moisture out of it — cave storage is certified by 12,000 years of standing, but ⚠ **standing is not dry**. See [storage-code-1.md](../government/regulations/storage-code-1.md).

### `CAVE-RECOVERY-CACHE-1`
Map: `CAVE-3` · Built: d3458

**`CAVE-RECOVERY-CRATE-1`** on shelf · **×8 brick @ mouth stack** — disaster-recovery lane separate from ark jars. ☠ **No acids in the cave cache** — chem porch remains primary for vitriol/bleach.

### `KOZAN-HUT-1`
Map: gate · Built: d1832

Door live. ×18 spare brick on site, mortar ~0.7 kg.

Deployed bridges, caches and waystations are [trails-and-bridges.md](../map/region/trails-and-bridges.md).
