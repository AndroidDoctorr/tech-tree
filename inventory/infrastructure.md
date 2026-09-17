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

Clay pan and sump, oak crib, shake lean-to. Turn 1 done d3213 — damp right, ammonia weak, cold-limited. Next turn ~d3231.

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

~+15% yield over an open pit.

### `CHAR-RETORT-2` — charcoal retort
Map: cell D · Built: d3032

Shares a wall with `CHAR-RETORT-1`. ~+17% on trial. The pair run as `CHAR-RETORT-TWIN-CELL-1`, a C/D parallel ×3 grammar.

### `KILN-D-PLENUM-1` — kiln D air plenum
Map: belt tree · Built: d2530

~4.5 L buffer, twin outlet, bleed cork. `WW-2` link PASS.

## Electrical generation

### ★★ `GEN-WW-1` — water-driven magneto
Map: `WW-2` wheelhouse · Built: d3248 · Air gap closed: d3249 · Field up: d3261 · Rewound: d3267

The campus generator. ×6 `MAG-BOOT-EM` rods in an iron yoke, closed-ring armature on a laminated core, 5-segment commutator with brushes tuned **under load**, concave pole faces shimmed to just over measured runout.

| Reading | Open | Loaded |
|---|---|---|
| d3249 build | ~1.85 GB | ~1.40 GB · ~0.55 I · ~2.4 R |
| d3261 field up *(×6 rods, yoke shortened)* | 2.28 GB | 1.72 GB **(+23%)** |
| d3267 `ARMATURE-2` | 4.31 GB | 8.6 R · peak 0.54 GB·I |

★★ **Epic closed d3258** — 6 h under real duty driving `CU-CELL-1`, no fault.

⚠ **On the water threshold, not over it.** The rewind traded voltage for current at unchanged peak power, which is what a rewind always does. Next step is a finer armature rewind.

Sub-assemblies: `GEN-WW-1-FRAME-1` (oak, sill-bolted, clear of splash, quick-release collar on WW-2 output) · `GEN-WW-1-BELT-TRAIN-1` (two ~4:1 stages = ~16:1, **crowned** pulleys, idler on stage 2, slack side up, ~12 rpm → ~190 rpm) · `GEN-WW-1-CORE-1` (laminations cut, **annealed after cutting**, deburred both faces, rosin-varnished) · `COMMUTATOR-2` (hardwood hub, 5 segments, plaster-jig seated, end-only ramps, adjustable brush gear, wire-bundle brushes).

### ★★★ `ARMATURE-2`
In service in `GEN-WW-1` · Wound: d3267

5 × 145 turns at 0.65 mm, ~182 m. Drawn down from `ARMATURE-1` with **no melt** and annealed each pass, which is why the copper survived the redraw.

⚠ `ARMATURE-3` — a coarse winding for `CU-CELL-1` — is **not built** and needs ~500 g. ★ No longer urgent and no longer a deadlock: the series pair recovers ~25% without it.

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

### `ELECTROLYSIS-CELL-1`
Map: chem porch

Crock, copper cathode, inverted `GLASS-BOTTLE-9` for capture. ⚠ **Anode needs lead or carbon.**

### `ANODE-NARROW-1`
Lead strip ~15 × 60 mm, brown PbO₂ formed, evolves O₂ steadily. Recast from `ANODE-PB-1` at d3205.

## Gas

### `GASHOLDER-1`
Map: atelier · Built: d3203

Bitumen oak bath. Bell A H₂ ~0.9 L, Bell B O₂ ~0.45 L — **full, about 85 s of flame**. Guides, hoods, keyed dip-tube lines, pinch clamps, fill line marked.

### `GASHOLDER-2`
Map: craft wing · ~60% built · Last: d3209

Tub ~0.55 × 0.45 m lined and scrimmed. Bell A ~9.5 L done, crown battened and air-tight. ⚠ Bell B ~4.8 L — bevels need re-cutting. Guides cut long. **Cocks blocked on `BRASS-POUR-1`.**

### `GAS-TERMINALS-1`
×4 copper binding posts, threaded at `LATHE-V2` · ×2 copper leaf clips · cathode post notched. Built d3203.

## Water and power

### `SLUICE-2-GATE-1` — sluice 2 gate
Map: `S2-0` · Built: d1878

Prefab kit mounted, bypass staged. Stream cheek `SLUICE-2-STREAM-CHEEK-1` ~10.2 kg; sill skim `SLUICE-2-SILL-SKIM-1` ~3.8 kg at the gate seat.

### `SLUICE-2-RACEWAY-1` — sluice 2 raceway
Map: `S2-0` → WW-yard pad · Built: d1879

~180 m.

### `WW-2-WHEEL-1` — water wheel 2
Map: north pad · Built: d1894

The prime mover. Belt tree live off it.

`BRONZE-BUSH-WW2-1` at the axle bed, cast d1884, ~320 g. `GS-2-FLYWHEEL-1` outboard on the shaft — ~9.8 kg oak with a ~290 g iron band, d1888. `LEATHER-FLAT-BELT-1` on the rim, ~4.2 m, **dressed weekly**.

### `BELT-TREE-1` — power distribution
Map: `WW-2` · Built: d1891–d1892

×3 idlers, ×3 pulleys, collar #3. `WW-2-BELT-COLLAR-1` is a set of ×4 quick-release collars on the shaft — #3 drives the kiln, #4 the cellar fan (added d3018).

`WW-MACHINE-FLYWHEEL-1` (MF-1) at idler B with clutch collar #3 — ~3.6 kg disk, `WW-MACHINE-SWITCH-1` live since d1973. `GRIND-TAKEOFF-2` is a cord branch to `GS-1`. `TRIP-HAMMER-BELT-1` is a ~1.8 m leather cam.

★ One wheel, one belt tree, and every powered tool on the campus hangs off it. A failure here stops the saw, the lathe, the drill press, the trip hammer, the cellar fan and the generator at the same time.

## Cold store

### `COLD-CELLAR-FAN-1` — cold cellar fan
Map: `WW-2` collar #4, duct to horreum ice vault · Last service: d3189

Flap balanced across both the old and the new niche.

### `ICE-VAULT-NICHE-2` — ice vault niche 2
Map: horreum north cella · Built: d3189

~1.2 × 1.0 m, lined c1–c5, straw/shive void, oak lid. Holding ~+40 kg. Cure to 8 Feb.

## Food processing

### `ACORN-LEACH-TROUGH-1`
Map: pool margin · Built: d2689

Idle. Rinse grammar live.

### `ACORN-LEACH-TROUGH-2`
Map: pool margin N · Built: d2718

Idle. Fill test PASS.

Both are the **fallback**, not the primary. Running water in the ditch leaches faster than serial still soaks ever will, because a still trough reaches equilibrium and stops working until it is changed. The troughs are for a batch that cannot be watched. See `ACORN-LEACH` in [processing.md](../government/procedures/processing.md).

### `EVAP-RACK-1` — salt evaporation rack
Map: — · Interval: seasonal

Trays empty. **Closed for the winter at D340, reopens in the March band.**

### `COOL-CELLAR-2-EVAP`
Map: cellar north margin

Trough flushed, drain clear.

## Storage fixtures

### `AMPHORA-5`
Map: — · Vinegar

Holds `VINEGAR-Y6-1` with the Y8 fork top-up. Mother live in a separate crock.

### `AMPHORA-6`
Map: — · Oil sediment

Sealed oil sediment at the foot, Y8 and Y9. **Never rinsed between years while sediment is held** — the settle is the point. Rinse deferred.

### `AMPHORA-7`
Map: cold tap branch · Built: d2567

Carries the `CULINA-POTABLE-FILTER-1` column. ★ **Potable — not grey.**

### `AMPHORA-8`
Map: cart yard · Built: d2286

Brackish and general. M-08 foot ring. Brackish haul staging runs through here and amphora #2; haul #13 queued as of d3109.

### `AMPHORA-9`
Map: rack hold

Ferment vessel. Currently under `GRAPE-MUST-Y9-1` — quantity in [food.md](food.md), not here. Harvest buffer swaps post-Dec.

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
Map: `LATHE-V2` · Built: d2856

`LS-SCREW-1` plus `LS-HALF-NUT-1`, ~1.0 mm/rev hand feed.

### `ROPEWALK-1`
Map: `WW-YARD` long run · Built: d3255

Geared 3-hook whirler, grooved top, **travelling** far hook, ~40 m pegged run.

⚠ **The traveller slot needs about a third of the laid length** — a rope shortens ~25% as it closes. A run pegged to finished length will jam.

### `DRILL-PRESS-1`
Map: — · Built: d1894 · Live ~95%

With `BORE-JIG-1`. Repeat bore to ~0.08 mm class. Upgrade path from `CRANK-DRILL-1`, which is still at `WORKBENCH-1` on a belt stub.

### `LATHE-1` and `LATHE-V2`
Map: `WORKBENCH-1`

`DEAD-CENTER-1` · `SPRING-CENTER-1` · `TOOL-POST-SQUARE-1`. The V2 leadscrew is below.

### `WIRE-COATING-RIG-1`
Map: craft wing · Built: d3232

Melt pot, felt wiper, take-up reel.

### `LIQUID-PUMP-2`
Map: wagon liquid-insert pump peg · Built: d3170

Copper barrel, brass checks, hose paired.

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

### `ASPHALT-TEST-1`
Map: hub S apron · Built: d2583

~0.6 × 0.4 m strip, ~18 mm crown. ☠ Not a food path.

## Benches

### `WORK-STAGING-TABLE-1`
Map: storage wing E · Built: d2400

~1180 × 620 × 880 mm. Lower shelf staging.

### `WORK-TABLE-ATELIER-1`
Map: atelier west cheek · Built: d2407

~900 × 450 × 760 mm. Craft knee.

### `WORK-TABLE-CULINA-1`
Map: culina S prep · Built: d2408

~1000 × 550 × 860 mm. Wipe-down top.

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

### `RETT-TROUGH-FLAX-1`
Map: ditch W · Live

Pool clear, ready for the next load.

### `RETT-TROUGH-HEMP-1`
Map: ditch W · Live

Empty, rinse clear. Next load when named.

The old mud pool is **retired**. The dual trough plus rinse branch runs the two fibres in parallel, which the single pool could not. Live arcs are [crops.md](crops.md); finished line is [resources.md](resources.md).

## Farm and holding

### `HOLDING-WIND-BREAK-1`
Map: north lee · Built: d3098

Brush, straw, shive pack.

### `NITRE-BED-COVER-1`
Map: north lee · Built: d3223

Dark sun-side cover over `NITRE-BED-1`.

## Trail and outposts

### `CAVE-3-FIXED-LINE-1` — fixed line, CAVE-3 approach
Map: `CAVE-3` approach · Built: d3221

~9 m hemp on ×2 rock spikes. Live.

The rope is not a `resources.md` row — once it is rigged and load-bearing it belongs to the installation, and it is inspected rather than counted.

### `CAVE-3-PATH-1`
Map: `CAVE-3` approach · Built: d3221

×11 out-canted steps · ~4 m diversion trench · drip lip · fixed line · ×2 skid stones in the crawl.

The steps are canted **outward** deliberately — an in-canted step holds water and ices.

### `CAVE-3-SHELF-1`
Map: `CAVE-3` · Built: d3221

Dry-stone. Slab ~1.1 × 0.5 m on ×3 corbel piers, ~0.5 m up, a hand's width clear of the wall. Load-tested.

★ The wall gap is the design. Stored goods touching cave rock wick moisture out of it — cave storage is certified by 12,000 years of standing, but ⚠ **standing is not dry**. See [storage-code-1.md](../government/regulations/storage-code-1.md).

### `KOZAN-HUT-1`
Map: gate · Built: d1832

Door live. ×18 spare brick on site, mortar ~0.7 kg.

Deployed bridges, caches and waystations are [trails-and-bridges.md](../map/region/trails-and-bridges.md).
