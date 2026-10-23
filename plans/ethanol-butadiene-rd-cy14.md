# Ethanol → butadiene R&D pathway · CY14

**Filed:** d5227 planning read · **layout + dry frame:** d5256 · **glass kit:** d5257 · **components ×7:** d5258 · **live state:** [now.md](../now.md) · **inventory:** `ETHANOL-DEHYD-*` · `OLEFIN-TRAP-STOCK-Y14-1` · `C4-COUPLING-STOCK-Y14-1`

## Current bench chain (proven)

| Stage | Grammar | Status |
|---|---|---|
| Dehyd | `ETHANOL-DEHYD-BATCH` · calcined M26 + ZnO @ ~420 °C | **Routine** |
| Polish | `ETHANOL-REDISTILL` → **`ETHANOL-DEHYD-HIGH-Y14-1`** ~92 % | **Routine** |
| Olefin capture | `OLEFIN-CAPTURE` · tube + ice trap + air sweep (d5102 / d5118) | **Repeatable · ~24 ml trap** |
| C₄ coupling | `C4-COUPLING-BENCH` on trap cut (d5103 / d5119) | **Assay butadiene-class · ~4.2 ml jar** |

**Route A (default):** Lebedev-like — ethanol over mixed oxide → olefin / diene-rich vapour → trap → coupling bench. **Do not fork to Route B until Route A capture is boring.**

**Rubber horizon:** [ladder / goals](../government/archive/ladder.md) — fig latex local · **synthetic rubber** needs polymer-grade diene + initiator + sealed storage — **not current tier**.

## Target rig — `POLYMER-LANE-PILOT-1`

**Site:** chem wing · shared hood with **`LAB-FUME-CABINET-1`** · replaces ad-hoc tear-down of **`ETHANOL-DEHYD-TUBE-REACTOR-Y14-1`** between moods.

> **The pilot is a reproducibility machine before it is a throughput machine.** First freeze temperature · feed rate · residence time · fraction order · mass balance. Increase charge only after those readings repeat.

### d5256 staked envelope

**`POLYMER-LANE-FRAME-CY14-1`** is a removable **~1.04 × 0.52 m** oak rail frame inside the hood envelope. It leaves the rear plenum clear and puts the hot shell on a two-tile ceramic bridge: **no hot vessel bears directly on oak**.

```text
FLOW →

┌ feed 0.20 m ┬ hot cartridge 0.30 m ┬ knock-out 0.20 m ┬ traps 0.34 m ┐
│ reservoir   │ 420–500 °C shell     │ water / ethanol  │ oxygenate   │
│ metering    │ swappable bed tube   │ take-off + assay │ C4 / vent   │
└─────────────┴───────────────────────┴──────────────────┴─────────────┘
   front drip rail                       rear clamp rail + open relief

production: feed vapour or dried inert sweep → always-open hood vent
air pump: leak test / clearing only — not C4 production sweep
```

| Datum | Staked read |
|---|---|
| **Hood envelope** | **~1.20 × 0.72 × 0.92 m** existing tile-lined cabinet |
| **Pilot frame** | **~1.04 × 0.52 m** · mortise + oak peg · removable |
| **Hot isolation** | **`TILE-TF` ×2** loose bridge · **≥~100 mm** from oak rail |
| **Service side** | Front feed / assay access under sash |
| **Exhaust side** | Rear line to knock-out · traps · relief bubbler · plenum |
| **Pressure rule** | **No closed dead-end while warm** · relief path visible at all times |

- **Modular cartridges** — swap bed, not rebuild the lane.
- **Stub flange** for future **Route B** aldehyde condenser leg (no commit until step 6).
- **Separate fractions** — water / ethanol knock-out first; oxygenate cut second; **C₄ cold trap last**.
- **Cold requirement** — plain ice is a knock-out bath, not a reliable butadiene trap. Use reusable salt–ice brine **~−15 to −20 °C class** for the C₄ end.
- **Sweep rule** — `AIR-PUMP-2` is acceptable for cold leak soap and post-run clearing only. Production uses ethanol feed vapour or a dried inert sweep; oxygen in a scaled C₄ line is a fire and peroxide gate.

## Build order

| Phase | Hero | Deliverable | Gate |
|---|---|---|---|
| **A** | **`POLYMER-LANE-STAKE-FRAME-5256`** | **✓ frame + ceramic hot bridge LIVE** | Plenum clear · sash travel · no-hot-on-oak |
| **A2** | **`POLYMER-LANE-GLASS-PREP-5257`** | **✓ ~2.86 kg dry glass kit STAGED** | Existing apparatus reserved · melt serially |
| **A3** | **`POLYMER-LANE-GLASS-COMPONENTS-5258`** | **✓ ×7 annealed** · kit **~1.72 kg** remain | Feed · meter · C₄ ×2 · oxy · relief · ×1 transfer |
| **B** | **`POLYMER-LANE-HOT-MODULE-1`** | **FIRED d5272** · **bands LIVE** · **cooling** | **`POLYMER-LANE-HOT-BLANK-1`** empty-heat **420–500 °C** |
| **C** | **`POLYMER-LANE-FEED-SWEEP-1`** | Reservoir · metering capillary · inert/feed-vapour manifold | Cold soap test · visible relief bubbles |
| **D** | **`POLYMER-LANE-TRAP-TRAIN-1`** | Knock-out · oxygenate receiver · C₄ cold trap · waste / vent | Each vessel removes independently |
| **E** | **`POLYMER-LANE-COLD-COMMISSION-1`** | No-heat flow test · measured delivery / loss | Ten-minute hold · no sash haze · no pressure creep |
| **F** | **`POLYMER-LANE-HOT-BLANK-1`** | Hot shell + clean carrier, no ethanol | Temperature map · seal/lute read |
| **G** | **`POLYMER-LANE-PILOT-RUN-1`** | First **~50–75 ml** feed balance | Input = liquid cuts + tail estimate within useful error |

## Material slate

### Phase A — committed d5256

| Material | Draw | Result |
|---|---:|---|
| **`WOOD-OAK-P5`** | **−~6.4 kg** | Rail frame · feet · clamp rail · oak pegs |
| **`TILE-TF`** | **−×2** | Loose ceramic bridge under hot-module footprint |
| Chalk / flax line | trace | Four-zone datum + plenum keep-clear |

### Glass stock — committed d5257

| Stock | State |
|---|---|
| **`POLYMER-GLASS-BATCH-CY14-1`** | **~1.72 kg DRY remain** after d5258 ×7 charges |
| **Annealed @ polymer peg** | Feed jar · meter cap · C₄ traps ×2 · oxy receiver · relief bubbler · transfer ×1 |
| **Still to blow** | Guard receiver · **×2–3** transfer sections |
| Reuse set | Existing reactor · cold trap · boil flask · condensers · stopcocks · joints · stands |
| Melt rule | Serial charges; neck trim → **`GLASS-CULLET-BIN-1`** |

### Remaining pilot build — component BOM, not yet drawn

**Basis:** one non-pressurized pilot handling **~50–150 ml feed/run** on the d5256 frame. Finished-part estimates are **±~25%**. Glass batch needs another **~20–30%** over finished mass for gathers, neck trim and rejects.

#### B · Hot module

| Part | Count / size | Material | Finished amount | Reason |
|---|---|---|---:|---|
| **Split heater shell** | 2 keyed halves · ~320 mm hot length | M26 kaolin body + fired grog | ~4–5 kg | Reusable furnace; opens without breaking the cartridge |
| **Bed cartridges** | ×3 · ~280–320 mm · ~28–35 mm bore | High-fired stoneware / porcelain | ~1.2–1.6 kg total | ×1 dehyd · ×1 coupling/tune · ×1 blank |
| **Bed retainers** | ×6–8 perforated discs / cups | Porcelain | ~0.15–0.25 kg | Keeps catalyst out of transfer line |
| **TC wells** | ×2 | Porcelain sleeves | ~0.10–0.20 kg | Bed inlet + core/outlet comparison |
| **Shell bands and pins** | ×4 bands + hinge/latch set | Forged iron strip | ~0.35–0.55 kg | Brass stays out of the 500 °C zone |
| **Hot-seat packing** | 2 saddles + replaceable crumbs | Fired grog / kaolin | ~0.4–0.7 kg | Supports tube without hard point loading |

**Hot-module total:** ceramics **~5.9–7.8 kg** · iron **~0.35–0.55 kg**.

#### C · Feed and sweep module

| Part | Count / size | Material | Finished amount | Reason |
|---|---|---|---:|---|
| **Feed reservoir** | ×1 · ~300 ml | Annealed lab glass | ~0.25–0.35 kg | Graduated charge jar above vaporizer |
| **Metering column + capillary** | ~0.35–0.45 m | Glass · ~2–3 mm metering bore | ~0.10–0.16 kg | Freezes ml/min instead of hand pouring |
| **Vaporizer bulb** | ×1 · ~200–250 ml | Annealed lab glass | ~0.20–0.30 kg | Separates liquid feed from the hot bed |
| **Drying / wash jars** | ×2 · ~150–200 ml | Glass | ~0.35–0.50 kg total | Conditions inert sweep; removable bypass |
| **Cold stopcocks** | ×3 | Glass bodies · cork plugs | ~0.12–0.20 kg glass + ~30 g cork | Feed isolate · purge select · sample take-off |
| **Manifold stubs** | ~0.4–0.6 m total | Glass tube | ~0.18–0.28 kg | Short replaceable runs |

**Feed-module total:** glass **~1.2–1.8 kg** · cork **~30 g**.

#### D · Product and trap train

| Part | Count / size | Material | Finished amount | Reason |
|---|---|---|---:|---|
| **Heat-break + transfer sections** | ~1.5–2.0 m total · ~8–12 mm bore | Annealed glass · 4–6 short pieces | ~0.60–0.90 kg | Replace one cracked section, not the whole train |
| **Water / ethanol knock-out** | ×1 · ~350–450 ml | Glass | ~0.35–0.50 kg | First liquid cut |
| **Oxygenate receiver** | ×1 · ~200 ml | Glass | ~0.20–0.30 kg | Keeps aldehyde / oxygenate cut separate |
| **C₄ cold traps** | ×2 · ~100–150 ml · thick wall | Glass | ~0.40–0.60 kg total | One on line; one cold and ready to swap |
| **Guard / waste receiver** | ×1 · ~250–300 ml | Glass | ~0.25–0.40 kg | Catches carry-over before vent |
| **Relief bubbler** | ×1 · ~250 ml | Glass | ~0.25–0.35 kg | Visible always-open pressure path |
| **Cold-bath crocks** | ×2 nested baths | Glazed stoneware | ~3–4 kg total | Salt–ice around C₄ traps; brine off glass joints |
| **Drip / fragment pan** | ×1 · shallow | Glazed stoneware | ~1.5–2.5 kg | Secondary containment under cold train |

**Trap-module total:** glass **~2.1–3.1 kg** · glazed stoneware **~4.5–6.5 kg**.

#### Mounting, joints and service parts

| Part | Material | Amount | Placement |
|---|---|---:|---|
| Hot clamps / uprights | Forged iron | ~0.25–0.40 kg beyond shell bands | Hot cartridge and heat-break only |
| Cool clamp pads / thumbscrews | Brass | ~0.08–0.15 kg | Reservoirs and receivers; external contact only |
| Receiver cradles / cleats | Oak | ~1–2 kg | Cool side of frame |
| Cork washers and plugs | Cork bark | ~0.10–0.15 kg total | Cold joints only |
| Packing / gasket paper | Flax tow | ~40–60 g | Under cork; no loose fibre in bore |
| Joint dressing | Wax / tallow / rosin | ~15–25 g | Cold leak seal only |
| TC conductors | Iron–constantan wire | ~15–25 g | Second probe; first probe remains reference |

> **Wetted-path rule:** hot vapour sees porcelain / stoneware; cooled vapour and liquids see glass. Iron and brass are structural hardware outside the bore. Cork, flax and wax stay downstream of the heat break.

### Build totals

| Material class | Fully dedicated rig | Current read |
|---|---:|---|
| **Lab glass, finished** | ~3.5–4.8 kg | Reuse audit reduces the first-build need to **~1.8–2.5 kg** |
| **Glass batch / clean cullet charged** | ~4.5–6.0 kg fully dedicated | **`POLYMER-GLASS-BATCH-CY14-1` ~2.86 kg raw STAGED** for the reuse-first build |
| **High-fired ceramic** | ~10.5–14.3 kg | M26 bulk ample; `FORSTERITE-GROG-1` ~1.5 kg covers the critical hot fraction but leaves little reject margin |
| **Forged iron hardware** | ~0.60–0.95 kg | Draw competes with the crossflow iron bank |
| **Brass hardware** | ~0.08–0.15 kg | `BRASS-STOCK` ~206 g — enough if reserved for cool-side pads and screws |
| **Oak after Phase A** | ~1–2 kg | Ample |
| **Cork** | ~0.10–0.15 kg | ~0.91 kg in hand |
| **Flax tow** | ~40–60 g | ~281 g in hand |
| **Wax / tallow / rosin** | ~15–25 g | Wax/tallow ample; rosin is thin, so do not specify rosin-heavy lute |

**Likely installed mass:** another **~17–24 kg** on the existing frame, depending on whether the cold baths and drip pan are dedicated or borrowed.

### Run consumables — not part of the fixed build

| Need | First commission | In hand / gate |
|---|---:|---|
| Catalyst bank | ~150–250 g calcine + ZnO tuning cuts | Calcine only ~58 g now · M26 + `ZNO-CALCINE` feed ample |
| Hot commission | Char ~4–6 kg | `CHAR-LANE` ~25 kg — one commission plus margin |
| C₄ cold bath | Ice ~4–6 kg + salt ~1.5–2 kg | Ice ~128.5 kg · salt ~10.8 kg; recover/reuse brine |
| Process feed | ~50–75 ml, then ~100–150 ml | `ETHANOL-DEHYD-HIGH-Y14-1` ~1.32 L — scale in steps |

## Commissioning readings

Every pilot run logs:

1. Feed charged · feed delivered · time · **ml/min**.
2. Bed inlet / bed core / bed outlet temperature band.
3. Knock-out, oxygenate, C₄ and waste volumes separately.
4. Tail-gas relief behavior — steady bubbles, no blocked line, no sash haze.
5. Catalyst mass before / after and visible coke.
6. C₄ assay ticket by fraction; **never merge a weak cut into the best jar blindly**.
7. Cold-trap bath temperature at start and finish.

## Ordered ladder (player + agent default)

| # | Step | Type | Gate |
|---|---|---|---|
| **1** | **Build `POLYMER-LANE-PILOT-1`** | ⚒ | **Phase A ✓ d5256** · hot module → manifold → trap train → commission |
| **2** | **Olefin capture laps** | ⚒ | **`OLEFIN-TRAP-STOCK-Y14-1` ≥ ~100 ml** · assay **repeatable** (not one HIT day) |
| **3** | **C₄ coupling on trap cuts only** | ⚒ | Merge **`C4-COUPLING-STOCK-Y14-1`** until butadiene-class assay **run-to-run** |
| **4** | **Catalyst tune between laps** | ⚒ | Calcine / ZnO loading · bed geometry — **not bigger feeds** |
| **5** | **Polymer proof** | ⚒ NOVEL | Micro-initiator on **best C₄ cut** · expect **gum**, not tyre rubber |
| **6** | **Route B scout** | ⚒ NOVEL | Acetaldehyde condensate @ pilot stub · assay vs Route A cut |
| **7** | **Rubber** | ⚒→⧗ | Only after **dry, sealed diene storage** grammar (cold · dark · O₂-free) |

## Do not

- Pivot main lane to acetaldehyde before **step 2** gate clears.
- Scale feed before **step 4** stops improving assay.
- Log **rubber** without **step 7** infrastructure.

## Journal anchors

- Phase A mechanism: d3956 · tube live d4598
- Olefin: d5102 · d5118
- C₄: d5103 · d5119
- Planning slate: d5227 **`POLYMER-LANE-READ-5227`**
