# `THERMOCOUPLE-1`

**Filed:** d3587 · **Status:** **`TC-PROBE-1` LIVE d3743** · cal **`TC-CAL-LADDER-Y12-1`** (ice · boil · Sn · Zn) · ⚑ **`MUFFLE-1` cone cross-check**

## Scope

First probe is **iron–constantan**, not copper–constantan.

- continuous working target: **200–750 °C**
- brief protected comparisons above that only after calibration
- primary use: `MUFFLE-1` anneal / normalize / temper holds
- not authoritative for `FURNACE-2` melt temperature

Copper–constantan is useful below roughly 400 °C, but copper oxidation and drift make it the wrong probe for steel-treatment heat. `FURNACE-2` keeps its cone ladder and later gains an optical sight method.

## Hot pair

| Part | Dimension |
|---|---:|
| Iron leg | **Ø0.50 mm × 450 mm** |
| Constantan leg | **Ø0.50 mm × 450 mm** |
| Protected insertion | **306 mm** |
| Exposed hot junction | **8 mm** beyond last segment |
| Cold tails | **~120 mm** beyond sleeve |

Hot legs and junction are consumables. A replacement pair receives a new probe ID and calibration row.

## Ceramic sleeve set

| Item | Dimension |
|---|---:|
| Segments | **×17 working + ×3 spare** |
| Each segment | **18 mm long × 11 mm OD** |
| Bores | **×2 · 2.0 mm ID** |
| Centre web | **3.0 mm minimum** |
| Working protected length | **306 mm** |
| Body | **85% M26 kaolin solids · 15% fine forsterite grog** |

Revision 1.0 used 36 mm segments and a 2 mm web. The first piece split when one mandrel released before the other. Shorter pieces and a thicker web are the working design.

**Build state:** ×12 green d3587. **×8 more owed** before firing: ×5 to complete the working length and ×3 spares. The 306 mm stack spans the muffle's ~215 mm roof package and reaches close to chamber centre.

## Cold-junction block

| Part | Dimension |
|---|---:|
| Ceramic block | **60 × 35 × 12 mm** |
| Post spacing | **24.0 mm centres** |
| Mount holes | **×2 Ø4.0 mm · 48 mm centres** |
| Brass posts | **BN-06 · 24 mm long** |
| Lead cross-hole | **Ø1.5 mm**, 5 mm below head |
| Washers | **Ø12 × 1 mm** |

The block sits dry inside a **≥60 mm ID × 100 mm** glass jar immersed in **≥1 L stirred ice-water**, with both ice and water present. Equalize for at least ten minutes.

## Galvanometer lead pair

- matched 0.3 mm copper, **2 × 2.50 m**
- matched within **5 mm**
- one twist per **20 mm**
- wax-rosin coated and flax served
- route ≥300 mm from power wiring and iron tools
- copper leaf clips at the potentiometer end

The copper transitions are acceptable only because both occur together on one isothermal terminal block.

## Readout

`POTENTIOMETER-1` opposes a divided fraction of `DANIELL-CELL-1`. `TANGENT-GALVANOMETER-1` is the null detector only. At null, the thermocouple supplies no current and lead/contact resistance drops out.

## Calibration

1. Ice bath: **0 °C reference junction**
2. Boiling water: low-point check, pressure noted
3. Tin melt arrest: **~232 °C**
4. Zinc melt arrest: **~420 °C**
5. Upper range: repeated comparison with the existing cone ladder in `MUFFLE-1`

Do not extrapolate an uncertified straight line from zinc to steel heat and call it measured.
