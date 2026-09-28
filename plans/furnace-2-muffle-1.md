# `FURNACE-2` + `MUFFLE-1`

**Opened:** d3586 · **Revision:** 1.2 after ceramic forming and wall-path check d3587

Two machines because the requirements conflict:

- **`FURNACE-2`** maximizes temperature for crucible melts and reduction.
- **`MUFFLE-1`** isolates the work for annealing, carburizing and controlled-atmosphere soaks.

☠ **Neither vessel is sealed.** Atmosphere control is continuous flow at slight negative pressure. A closed hot reducing vessel is a pressure and carbon-monoxide hazard.

---

## Shared site and datum

| Item | Dimension / rule |
|---|---|
| Site | Forge terrace, outdoors under open lean-to · ≥1.5 m clear working radius |
| Common floor datum | Fired stone slab, **900 × 900 × 150 mm**, level to **≤2 mm** |
| Service side | South · doors, tuyère, valves and instruments all readable from one standing position |
| Gas hot-zone material | **Stoneware only** · metal begins ≥300 mm beyond the hot face |
| Hot/cold joint | Dry-sand packed annulus, **25 mm long** · cannot hold pressure |
| Smoke read | Fixed `SMOKE-SPOT` tile station at each exhaust |
| Instrument port | **14 mm ID**, accepting the thermocouple sleeve set below |

---

## `FURNACE-2` — crucible melt furnace

### Envelope

| Item | Dimension |
|---|---:|
| Overall shell | **Ø680 × 960 mm high** |
| Hot chamber | **Ø240 × 360 mm working height** |
| Crucible envelope | **≤Ø120 × 220 mm high** |
| Annular fuel space | **≥55 mm radial** around the largest crucible |
| Hot face | **90 mm** forsterite refractory |
| Insulating backup | **90 mm** low-density fired ceramic |
| Outer structural shell | **60 mm** fired brick + bands |
| Hearth hot face | **100 mm** |
| Ash / cleanout chamber | **180 × 180 × 140 mm** |
| Top lift opening | **Ø160 mm**, closed by two keyed refractory half-plugs |

### Air and exhaust

| Item | Dimension / setting |
|---|---|
| Tuyère | Stoneware · **32 mm ID · 46 mm OD · 280 mm long** |
| Tuyère centerline | **70 mm above grate**, tangent to a **Ø160 mm** circle, **10° upward** |
| Instrument port centerline | **220 mm above grate**, radial, off the flame tongue |
| Exhaust throat | **Ø90 mm** into hot-blast jacket |
| Stack | **Ø120 mm clear bore · ≥3.5 m above hearth datum** |
| Operating pressure | Slightly negative at lid seam under full blast |

### `BLAST-BLOWER-1`

| Item | Dimension / output |
|---|---|
| Type | Twin alternating box bellows off `WW-2` crank |
| Bellows internal | **500 × 350 × 120 mm each** · ~21 L/stroke |
| Crank | **60 mm radius · 120 mm stroke** |
| Drive | 1:1 from ~12 rpm wheel shaft |
| Nominal delivery | ~**500 L/min** before leakage |
| Non-return valves | **140 × 100 mm** leather flap, one inlet + one outlet per box |
| Plenum | Existing **4.5 L `KILN-D-PLENUM-1`** for trials; production replacement target **12 L** |
| Control | Adjustable bleed **Ø0–32 mm** · blast is set by bleed, not belt slip |

### Hot blast

Two straight stoneware ducts in the first exhaust run:

| Item | Dimension |
|---|---:|
| Ducts | **×2 · 28 mm ID · 40 mm OD · 900 mm hot length** |
| Merge | Cool-side Y into **40 mm ID** plenum feed |
| Clearance from exhaust wall | **≥25 mm** all round |
| Expansion | One dry-sand slip joint per duct |
| First-fire rule | Cold blast baseline first, then hot blast with the same charge and blast setting |

> **No oxygen lance.** Air blast is the production oxidizer. Pure O₂ at the tuyère would burn the charge and the furnace lining faster than it raises useful temperature.

### Charge atmosphere

The furnace chamber is combustion space. **The lidded, luted crucible controls the charge atmosphere:**

- charcoal pack for reducing
- pale glass cover for sealed melt protection
- loose sand lute at the lid so pressure vents before the pot fails

---

## `MUFFLE-1` — treatment furnace

### Envelope

| Item | Dimension |
|---|---:|
| Overall shell | **900 × 620 × 700 mm high** |
| Muffle working chamber | **480 × 160 × 160 mm** |
| Muffle wall | **25 mm** fired kaolin-forsterite body |
| Flame jacket | **40 mm clear** below, sides and crown |
| Hot face outside jacket | **75 mm** |
| Insulating backup | **75 mm** |
| Door opening | **180 × 180 mm** |
| Door plug | **75 mm** refractory, stepped **20 mm** into the reveal |
| Work support | Three removable bars, **20 × 20 × 150 mm**, at 80 / 240 / 400 mm |

### Fire path

| Item | Dimension / rule |
|---|---|
| Firebox | **250 × 250 × 300 mm** at west end |
| Flame entry | **60 × 100 mm** below muffle floor |
| Exit | **Ø100 mm** at opposite upper corner |
| Path | Under → both sides → crown → exit; no direct flame into chamber |
| Damper | Full · working-mid · minimum-safe stops; **no closed position** |

### Atmosphere circuit

| Item | Dimension / rule |
|---|---|
| Gas inlet | Stoneware **10 mm ID**, low west rear |
| Gas exhaust | Stoneware **12 mm ID**, high east front · **always open** |
| Thermocouple port | **14 mm ID**, roof center at **240 mm** from door · ~295 mm outside-to-chamber-centre path |
| Cold-side valves | Air · future flue gas · future H₂/O₂ manifold, one source at a time |
| Purge | Minimum **3 chamber volumes** before admitting a reducing gas to a hot chamber |

**Useful atmospheres:**

- air flow: oxidizing / scale trial
- isolated muffle with exhaust open: near-neutral
- charcoal-packed sealed box inside muffle: reducing / carburizing
- flue-gas purge: low-oxygen anneal

⚠ **H₂ and O₂ are never connected simultaneously.** Oxygen is for a deliberate oxidizing trial, not routine steel heating.

---

## `THERMOCOUPLE-1` interface

Full probe specification: [thermocouple-1.md](thermocouple-1.md). The first hot pair is **iron–constantan** for muffle work; copper–constantan is not the steel-heat probe.

### Ceramic sleeve set

Revision 1.0 called for five **36 mm** sleeves. First forming split the center web while the twin mandrels were withdrawn. Revision 1.1 shortens the pieces and thickens the web.

| Item | Revision 1.1 dimension |
|---|---:|
| Sleeve segments | **×17 working + ×3 spare** · **×12 first batch green d3587** |
| Each segment | **18 mm long · 11 mm OD** |
| Bores | **×2 · 2.0 mm ID** |
| Center web | **3.0 mm minimum** |
| Working insulated length | **306 mm** |
| Body | **85% kaolin solids · 15% fine forsterite grog** |
| Hot junction exposure | Last **8 mm** beyond sleeve · junction bare |

### Cold terminal block

| Item | Dimension |
|---|---:|
| Ceramic block | **60 × 35 × 12 mm** |
| Post centers | **24.0 mm** |
| Mount holes | **×2 Ø4 mm**, 48 mm centers |
| Binding posts | **×2 brass · BN-06 thread · 24 mm long** |
| Lead cross-hole | **Ø1.5 mm**, 5 mm below post head |
| Washers | **Ø12 × 1 mm** |

Both dissimilar-metal transitions sit on the same ceramic block. Its temperature is the **cold-junction temperature** and is logged with every reading.

For certification, place the block in a dry inner glass jar immersed in a stirred **ice-water bath**:

| Item | Dimension / rule |
|---|---|
| Outer bath | **≥1 L** · crushed ice + water, both phases present |
| Dry inner jar | **≥60 mm ID × 100 mm deep** · terminal block remains dry |
| Equalization | **10 min minimum** before a calibration reading |
| Reference | **0 °C by state**, no thermometer required |

### Galvanometer lead pair

| Item | Dimension / rule |
|---|---|
| Conductor | Matched copper, **0.3 mm** |
| Length | **2 × 2.50 m**, matched within **5 mm** |
| Lay | Twisted pair · **one turn per 20 mm** |
| Insulation | Wax-rosin coat + served flax |
| Routing | ≥300 mm from iron tools and power wiring |
| Instrument end | Copper leaf clips, polarity marked |

The copper transitions are acceptable only because both occur together on one isothermal terminal block.

### Readout

☠ **Do not read thermocouple current directly on the tangent galvanometer.** The source is only millivolts and the instrument would load it.

Use `POTENTIOMETER-1` to oppose a divided fraction of `DANIELL-CELL-1`; use `TANGENT-GALVANOMETER-1` only as the **null detector**. At null, the thermocouple supplies no current, so lead and contact resistance fall out of the reading.

---

## Test and certification order

1. Fire refractory-prism ladder and select hot-face formula.
2. Build a short wall coupon and run cold smoke.
3. `FURNACE-2` empty heat · cold blast.
4. Same heat with hot blast · compare fuel and cone climb.
5. Crucible with expendable cast-iron charge.
6. `MUFFLE-1` empty temperature-uniformity run at five stations.
7. Thermocouple fixed-point ladder against the 0 °C cold bath: boiling water · **tin 232 °C · zinc 420 °C**, then repeated upper-range comparison against the existing cone ladder.
8. No production alloy heat until temperature curve, charge mass and coupon record agree.
