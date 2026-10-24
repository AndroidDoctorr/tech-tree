# WW-2 power upgrade

**Opened:** d5028 · **measured:** d5029

## Objective

Recover useful power from the **~7.15 m measured gross site head** and seasonal **~10–25 L/s** flow without disrupting the existing wheel until a replacement path is proven.

## Transition architecture — turbine replaces the wheel

**Decision:** keep WW-2 working while every turbine component is built and bench-tested, then make one planned cut-over. After commissioning, the crossflow turbine is the prime mover for both mechanical and electrical work.

```text
FOREBAY → preserved-head route → turbine isolation gate → CROSSFLOW
                                                        ├─ clutch G + pulley match → generator
                                                        └─ clutch M → reduction
                                                                     → retained flywheel
                                                                     → BELT-TREE-1
         └────────────────────────────── spill / bypass
```

The turbine is not electricity-only. Its shaft can drive the existing belt tree directly through reduction, so motors are not a prerequisite.

**Cut-over doctrine:** build and bench-test the runner, shaft, reduction, generator clutch, mechanical clutch, guards and gate hardware while WW-2 remains untouched. The only outage is the final hydraulic / belt-tree tie-in. Commission turbine mechanical mode first, then generator mode.

**Flywheel constraint:** reuse `GS-2-FLYWHEEL-1` only on the **reduced low-speed mechanical shaft** near its present ~10 rpm class. It is an oak wheel with an iron band, not a turbine-speed rotor; never mount it directly on the several-hundred-rpm runner shaft.

### Operating modes

| Mode | Water | Shaft state | Use |
|---|---|---|---|
| **Mechanical** | Turbine live | clutch M · G open | Existing belt-driven machines |
| **Electric** | Turbine live | clutch G · M open | Generator + battery charging |
| **Changeover / idle** | Turbine gated or unloaded | both open | Stop, change clutch state, restart |
| **Mixed later** | Turbine live | M + G only after load proof | Light generation beside mechanical work |

**Interlock:** default to one loaded output at a time. Do not engage a stopped belt tree or generator hard against a live shaft; unload, clutch, then admit flow.

**Battery role:** bridge gate changes, field build and lighting; do not size batteries as the ordinary source for forge, saw, mill or compressor duty.

### Fate of WW-2

Do not move it downstream. It remains the proven prime mover until cut-over, then retires in place after turbine mechanical and generator modes both pass. The old race can remain as a bypass / spill path; permanent dual-prime-mover coupling is unnecessary.

### Added transition hardware

| Draw | Planning class |
|---|---:|
| Turbine headbox · isolation + spill control | ~12–20 blocks · ~10–20 kg oak · ~2–4 kg wrought |
| Common jackshaft / reduction / two selectable clutches | ~4–7 kg wrought/steel · ~0.4–0.7 kg bronze |
| Belts / guards / brake | Machine-belt stock + oak guards |

This is additional to the runner itself. Freeze the arrangement before final ore banking.

## Existing works

- **Intake:** `SLUICE-2-GATE-2` complete · indexed SUMMER / NORMAL / FLOOD · bypass live.
- **Forebay:** ~35 × ~10 m · +3 m crest · spillway · wing · fill · intake all complete.
- **Outlet:** `HYDRO-ELEC-1-PENSTOCK-1` is an **~8 m dam culvert**, not a pressure penstock to WW-2.
- **Conveyance:** the outlet feeds the old **~180 m descending open race**.
- **Wheel:** undershot impulse class · broad shallow drive faces · no pocketed bucket set in the build record.
- **Generator:** shunt dynamo · ~16:1 belt train · likely becomes the next bottleneck after hydraulic capture improves.

## Measured baseline — d5029

| Quantity | Existing | Temporary apron + cheeks |
|---|---:|---:|
| Flow | ~25.4 L/s | same |
| Gross static head · forebay to tailrace | ~7.15 m | same |
| Useful water-surface drop at existing wheel | ~0.85 m class | ~0.85 m class |
| Loaded wheel speed | ~8.9 rpm | ~9.7 rpm |
| Brake torque | ~330 N·m | ~350 N·m |
| Shaft power | ~0.31 kW | ~0.36 kW |
| Generator peak | ~2.18 GB·I | ~2.30 GB·I |

Gross site resource at current flow is **~1.78 kW**. Existing wheel capture is therefore **~17% class**; the entry close reaches **~20% class**. The difference is real, but the large loss remains the descending race and undershot geometry.

## Phase 1 — entry apron and side cheeks

**✓ BUILT d5030 · `WW-2-ENTRY-APRON-1` LIVE.**

The gate and bypass can isolate the wheel branch for a workday. Use the existing pad and FS keys; blocks are optional anchors, not the apron surface.

| Draw | Estimate | In hand |
|---|---:|---:|
| `WOOD-OAK-P5` | ~8–12 kg | ~42.8 kg after d5029 |
| `NAIL-IRON` | ×6–8 | ×18 |
| M-08 pitch | ~80–150 g | check jar at build gate |
| Tallow / beeswax | ~20–30 g | service stock |
| `BLOCK-Y10-DRY-STACK-1` | **×0 required** · optional ×2–4 anchors | ×32 dry @ WW yard |
| Labour | ~1 full day | — |

**Build:** tapered oak apron · two close side cheeks · removable debris lip · preserve bypass and axle access.

**Gate:** repeat rpm + brake torque before and after. Keep only if gain remains ≥~5%.

**Actual:** ~10.2 kg oak · nails ×8 · bitumen ~120 g · beeswax/tallow ~18 g each · **no blocks**. Commission read **~9.6 rpm · ~348 N·m · ~0.35 kW**, about **14%** above the d5029 baseline.

## Phase 2 — removable bucket experiment

Build **one test module**, not a full wheel conversion.

| Draw | Estimate |
|---|---:|
| Oak | ~2.5–4 kg |
| Nails / small straps | ×2–4 |
| M-08 / wax | ~30–50 g |
| Labour | ~1 day build + test |

Try a **backward-inclined curved pocket** with a clean vent / drain path. Compare at the same gate stop and brake load. If one module shows no clean torque gain, stop; a full set would consume **~15–25 kg oak** and fasteners without recovering the lost head.

**d5031 trial:** removable steam-bent module produced a clear positive pulse and **~6% phase-averaged shaft gain** without entry shock. Removed after test to avoid one-sector torque ripple; banked as the full-set pattern. Full retrofit is worthwhile as an interim option, but waits on a wood refill and sow priority.

## Phase 3 — preserve the head

This is the large civil gain and the part best tied into the **summer nadir**.

### Preferred route

Cut or line a **near-level contour headrace** from the forebay outlet to a headbox near WW-2, then take the final **~6–7 m** through a short large chute / stave penstock.

Provisional civil budget:

| Draw | Planning class |
|---|---:|
| Dry blocks | ~×16–30 |
| Fired brick / lining | ~×20–40 |
| Oak · headbox / gates / forms | ~15–30 kg |
| Sand / pozz / lime mortar | ~80–140 kg wet aggregate class |
| Short large penstock / chute | Size after route survey |
| Labour | ~8–15 hero-days, staged |

### Rejected default

A full **~180 m stave pressure penstock** would require hundreds of kilograms of oak plus many tens of kilograms of hoop iron. It is not the economical first route with current stocks.

## Phase 4 — two-cell crossflow runner

**✓ Design issued d5379** — frozen dims + Route A civil: [ww-2-crossflow-design-y15.md](ww-2-crossflow-design-y15.md). **Off-line fab GO** · **`IRON-BLOOM-1` ~16 kg** banked.

Design basis:

- Net design head: **~6.6–7.0 m** after headbox / conduit losses.
- Seasonal flow: **~10–25 L/s**.
- Two-cell adjustable nozzle: small cell for nadir · both cells for winter/spring.
- Preliminary runner envelope only: **~250–300 mm OD · ~200–300 mm width · ~18–24 curved blades**. Do not freeze dimensions before conduit and nozzle measurements.
- Expected shaft output: **~0.4–0.5 kW at nadir** · **~1.0–1.2 kW at current winter flow**, before generator losses.

Provisional machine budget:

| Draw | Planning class | Current constraint |
|---|---:|---|
| Wrought / steel · shaft, discs, blades, nozzle, hardware | ~12–20 kg | **~0.32 kg mount — blocked on smelts** |
| Bronze · two bearing shells | ~0.6–1.0 kg | **~0.22 kg stock — short** |
| Oak · frame / casing / headbox | ~20–35 kg | In hand only if apron stays modest |
| Fasteners | ~×20–30 | Forge batch required |
| Labour | ~8–14 machine days + civil install | After sow / preferably nadir tie-in |

## Phase 5 — generator match

After the turbine has a measured shaft curve:

1. Match pulley ratio to runner speed.
2. Repeat generator load line.
3. Adjust brushes and field.
4. Rewind only if shaft power remains unused.

Do not rewind against the present wheel: the hydraulic source is still the dominant bottleneck.

## Calendar

- **Now / before sow:** entry apron · one bucket module · route survey · material banking.
- **26 Feb – 16 Mar:** spring sow takes priority.
- **Spring:** repeat Q/head series; freeze two-cell design range.
- **Summer nadir:** headrace/headbox cut and hydraulic tie-in.
- **After civil PASS:** runner build · install · generator rematch.

## Expedition and material bank

### Iron

Crossflow machine estimate **~12–20 kg wrought / steel**, plus **~4–7 kg** for the transitional jackshaft and clutches. Historical bloom yield is **~0.67 kg from ~2.8 kg `H-11-HEMATITE`** with **~5.5 kg char**.

- Ore target: **~65–115 kg hematite** before refinement losses.
- Historical H-11 haul: **~10–11 kg per same-day lap** → roughly **6–11 haul days**.
- Char implication at old yield: **~130–225 kg**. Run retorts between smelts; do not treat ore haul as the only supply problem.

### Pozzolan

Current `POZZ-TUFF-1`: **~3.5 kg**. Civil planning class is **~80–140 kg wet aggregate**, though final lining may use less after route design.

- Koruhöyük precedent: **~48 kg per expedition haul**.
- Planning target: **2–3 heavy pozz trips**, staged before nadir construction.

### Tin and bearing bronze

- `CASSITERITE-CONC`: **~0.5 kg**, fines-heavy and not yet reduced.
- `BRONZE-STOCK`: **~220 g**.
- Bearing budget: **~0.6–1.0 kg bronze**, needing roughly **~60–100 g tin** at 10% Sn.

The cassiterite concentrate is probably enough tin for this project if assay/reduction yield is ordinary; `O-1-MALACHITE` **~7.27 kg** supplies the copper side. **Kozan is not required yet for WW-2 alone.** Run a small tin recovery assay before deciding: queue Kozan only if recovery is poor or a broader bronze reserve is wanted.
