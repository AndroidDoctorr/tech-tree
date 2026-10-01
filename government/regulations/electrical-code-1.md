# Electrical Code 1 *(EC-1)*

**Filed:** Day 3558 · **Cal-Y12 D39** · **~8 Feb Y12**
**Amended:** Day 3889 · **Cal-Y13 D17** · **~6 Jan Y13** — **EC-1-GAUGE · EC-1-GRID · `EC-1-WIRE-SAMPLE-SET-Y13-1`**
**Scope:** wire, resistance standards, cells, generator interface, campus distribution, and bench measurement @ HOME campus
**Related:** [measurement-code-1.md](measurement-code-1.md) · [manufacturing-code-1.md](manufacturing-code-1.md) · [building-code-2.md](building-code-2.md) BC-2-SERVICES

---

## Intent

Codify what the **`GEN-WW-2`** era already proved on the bench — **load lines, four-terminal measurement, wire QC by resistance** — so every new coil, cell, and conductor cites **stated standards**, not remembered volts.

> ★★ **Electrical sizing is arithmetic once resistance is a resource with a name.**

---

## EC-1-UNITS — campus electrical quantities

| Quantity | Symbol | Campus unit | Notes |
|---|---|---|---|
| **Electromotive force** | E | **GB** *(generator block)* | **`GEN-WW-2` load-line slope** · not a fixed "voltage" |
| **Current** | I | **I** | Measured through known shunt or cell rate |
| **Resistance** | R | **R** | **Ω-class naming deferred** — use **`R-STD-1` ratio** until frequency artifact exists |
| **Power** | P | **GB·I** | Peak when load matches internal R |

**Record format:** *E · I · R · T_bench · day · instrument*

---

## EC-1-REF — resistance standards @ 14 °C bench

| ID | Construction | Nominal R | Rule |
|---|---|---|---|
| **`R-STD-1`** | **10 m · 0.9 mm Cu · non-inductive** | From gauge × length | **Primary ratio standard** |
| **`R-BIG-1`** | **~106 m · 0.3 mm iron · non-inductive** | **~500 R class** | ⚠ **Iron drifts with heat** — read at one bench T only |
| **`SLIDE-WIRE-BRIDGE-1`** | Uniform wire + slider | Ratio | **Resistance → length** at balance |

**Trim rule:** ★ **Standards are trimmed to match, not manufactured to guess.**

⚑ **Constantan wire masters** — low TCR · hot/cold variance work · ⧗ **nickel / alloy lane** (Amanos class).

---

## EC-1-MEASURE — four-terminal doctrine

| Rule | Application |
|---|---|
| **Current in heavy outboard clips** | Shunts · plates · strips |
| **Voltage taps inboard** | **`FOUR-TERMINAL-JIG-1`** · taps carry ~no current |
| **Non-inductive winding** | Doubled back — a coil is not a resistor |
| **Null at balance** | Potentiometer / bridge — **zero current at null** |

☠ **A short between neighbouring turns reads sound end-to-end until it cooks.**

---

## EC-1-WIRE — copper conductor

| Rule | Standard |
|---|---|
| **Stock** | **`CU-BAR-Y10-1` · `CU-WIRE-Y10-*`** drawn sizes logged |
| **Insulation** | **Wax + pine rosin ×2 · paper between layers · thread only at leads** | Closed d3245 grammar |
| **QC** | **Known length + gauge → expected R** · thin spot = high R |
| **Scarcity** | ★ **Copper is conductor stock** — drain lines defer per BC-3 |

**Bench draw:** anneal between passes · wax in die · iron work-hardens and snaps.

---

## EC-1-GAUGE — campus copper wire series *(14 °C bench · vs `R-STD-1`)*

**Rule:** ★ **Gauge is mm diameter. Resistance is measured, not calculated — but must track area scaling within stated band.**

| Gauge (mm) | R per 10 m | R per 1 m | Use class | Campus stock |
|---|---|---|---|---|
| **0.9** | **1.00 R** | **0.100 R** | **Standard · shunt · feeder trunk** | **`R-STD-1` · `CU-WIRE-Y10-COATED`** |
| **0.65** | **~1.95 R** | **~0.195 R** | **Armature · motor windings** | **`ARMATURE-2` grammar** |
| **0.5** | **~3.25 R** | **~0.325 R** | **Field coil · branch feeder** | **`EC-1-WIRE-SAMPLE-Y13-0.5`** |
| **0.3** | **~9.0 R** | **~0.900 R** | **Instrument · fine lead · tap** | **`CU-WIRE-Y10-3` rack** |

**Sample set `EC-1-WIRE-SAMPLE-SET-Y13-1`:** ×4 trimmed lengths @ **10.00 m each** · four-terminal read @ **14 °C** · tagged @ **`REF-SHELF-1`**.

| Sample ID | Gauge | Measured R (10 m) | vs theory |
|---|---|---|---|
| **`EC-1-WIRE-SAMPLE-Y13-0.9`** | 0.9 mm | **1.00 R** | **`R-STD-1` confirm** |
| **`EC-1-WIRE-SAMPLE-Y13-0.65`** | 0.65 mm | **~1.97 R** | **PASS** |
| **`EC-1-WIRE-SAMPLE-Y13-0.5`** | 0.5 mm | **~3.28 R** | **PASS** |
| **`EC-1-WIRE-SAMPLE-Y13-0.3`** | 0.3 mm | **~8.95 R** | **PASS** |

**QC band:** measured R within **±5%** of gauge-table expectation at same length · else reject length or downgrade to scrap anode.

**Draw order for new stock:** anneal · die wax · **one gauge per pass** · measure before coat · log on kitchen slate.

---

## EC-1-GRID — campus distribution *(GEN-WW-2 era)*

### Source hierarchy

| Priority | Source | Role |
|---|---|---|
| **1** | **`GEN-WW-2` @ wheelhouse** | Primary · runs while water flows |
| **2** | **`LEAD-ACID-BANK-Y13-1`** | Storage · overnight sink · bench peak loads |
| **3** | **`DANIELL-CELL-1` · voltaic bench** | Reference · measurement · flash/bootstrap only |
| **4** | **`PEDAL-GEN-1`** | Portable bench · tuning · emergency |

☠ **Never parallel mismatched sources without a knife switch — two generators on one bus fight.**

### Bus grammar

| Element | Rule |
|---|---|
| **Generation bus** | **`GEN-WW-2` + terminal · frame ground = −** · **`CU-CELL` may stay on parallel gen bus** |
| **Storage bus** | **`LEAD-ACID-BANK` + to gen + · common − to frame** · isolate when servicing |
| **Campus feeder** | **Single trunk from wheelhouse · polarity marked @ every splice** |
| **Building tap** | **Knife switch @ entry · fuse link = thin wire tail or belt-slip class** |
| **Return path** | **Frame ground + dedicated copper strap — not water pipe · not char retort** |

### Feeder sizing *(first pass)*

| Run | Max length | Min gauge | Notes |
|---|---|---|---|
| **Wheelhouse → chem porch** | **~25 m class** | **0.9 mm trunk · 0.5 mm branch** | First live feeder target |
| **Bench tap** | **~3 m** | **0.5 mm** | Motor · stirrer · lamp class |
| **Instrument tap** | **~1 m** | **0.3 mm** | Meter · bridge · potentiometer only |

★ **Voltage drop is real even at GB scale — size feeders from measured R, not hope.**

### Switches and isolation

| Rule | Standard |
|---|---|
| **Knife switch** | **Break + only · never load-break under motor spin-down** |
| **Polarity mark** | **Chisel or tag @ bus · + toward source** |
| **Chem isolation** | **Separate tray from food wing · acid bench on own tap** |
| **Gas isolation** | **`WATER-CELL-1` · `GASHOLDER-*` never on indoor bus** |
| **Storage read** | **Battery bank daily when on bus · separator + electrolyte level** |

### Building entry targets *(queued)*

1. ✓ **Chem porch / `CHEM-LAB-WING-1`** — **`EC-1-GRID-FEEDER-1` LIVE d3890** · **`GRID-TAP-CHEM-1`** · cells · bench · future hood fan
2. **Craft wing** — **`GASHOLDER-2` gas pad adjacent · not same breaker as chem**
3. **Horreum margin** — defer · no gas · no heat loads until conduit chase proven

Chases: [building-code-2.md](building-code-2.md) BC-2-SERVICES — **leave route · minimal install.**

---

## EC-1-CELL — voltaic / electroplating

| Rule | Standard |
|---|---|
| **Anode choice** | Soluble Cu = transfer · inert C = source · consumable |
| **Current density** | ☠ **Sponge = too much A per area** — area reconciles generator vs cell |
| **Series vs parallel** | Series reuses current · parallel splits it — load line picks optimum |
| **Liquid path** | ☠ **Cascade through air gaps** — full pipe between series cells bypasses one |

---

## EC-1-GEN — `GEN-WW-2` interface

| Rule | Standard |
|---|---|
| **Load line** | Open-circuit point + short-circuit point · straight line between |
| **Internal R** | Slope of line · measured from outside |
| **Max power** | Load R = internal R · fixed window — **rewind rotates line, not ceiling** |
| **Belt fuse** | Flat belt slips before tooth strips — see manufacturing gear doctrine |

Chases and sleeves: [building-code-2.md](building-code-2.md) — **leave route · minimal install.**

---

## EC-1-FUTURE — temperature-stable electrical refs

| Target | Purpose | Gate |
|---|---|---|
| **Constantan R-wire masters** | Compare drift vs **`R-BIG-1`** across T | Nickel alloy stock |
| **Invar length refs** | Mechanical + electrical fixture stability | Fe-Ni · MC-1 §future |
| **Frequency artifact** | Pendulum → monochord → fork → **Hz** | MC-1 chain step 6–7 |

---

## EC-1-SAFETY *(minimal — full safety code TBD)*

| Hazard | Rule |
|---|---|
| **Open hydrogen / oxygen** | Lit tip protocol · invisible flame · never hand test |
| **Lead fume** | Hood suction live · starved fire = CO |
| **Charging cells** | Downwind · outdoor for gas evolution |
