# Electrical Code 1 *(EC-1)*

**Filed:** Day 3558 · **Cal-Y12 D39** · **~8 Feb Y12**
**Scope:** wire, resistance standards, cells, generator interface, and bench measurement @ HOME campus
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
