# Industrial mechanical drive — power before machine-shop move *(CY14)*

**Status:** **Phase 0 ✓ d5081** · **scale slate ✓ d5469** → [gen-ww-3-scale-cy15.md](gen-ww-3-scale-cy15.md) · **next:** crossflow wet · **`GEN-WW-3-M`** lam program  
**Ledger:** [inventory/electric-grid.md](../inventory/electric-grid.md) § Loss & torque  
**Hydraulic:** [ww-2-power-upgrade.md](ww-2-power-upgrade.md) · **Shop shell:** [g2-ms1-machine-shop-cy14.md](g2-ms1-machine-shop-cy14.md)

## Problem

**Chicken and egg:** machine shop @ `PARK-MFG-1` needs **heavy feeder + motor torque**; campus tools today need **`BELT-TREE-1`** @ the wheel. Moving tools before power is ready idles work; waiting on the full G2 shell delays usable space.

## Strategy *(player d5080)*

```text
MEASURE → CROSSFLOW + TURBINE → GEN/MOTOR R&D (paired)
              ↓
    MOTOR-IND on grid @ CURRENT tool locations (belt line shaft)
              ↓
    G2 MS construction in PARALLEL (shell + feeder stub)
              ↓
    MOVE machines when MS feeder + drive PASS
```

| Track | Work | Machines usable? |
|---|---|---|
| **A — R&D** | Torque survey · loss model · crossflow cut-over · **`GEN-WW-3` / `MOTOR-IND-1`** class | **Yes** — wheel / belt tree until turbine live; then gen+motor @ present sites |
| **B — Build** | **G2-MS1** stockpile · footings · block shell | **Yes** — tools not moved yet |
| **C — Move** | Relocate lathe/mill/bench line to MS | **After** C track feeder + shaft commissioned |

## Phase map

| Phase | ID | Deliverable |
|---|---|---|
| **0** | **`DRIVE-SURVEY-CY14`** ✓ **d5081** | Torque table · feeder audit · **`MOTOR-2`** read · **Feeder-4** stake |
| **1** | **`WW-2-CROSSFLOW-COMMISSION`** | Turbine mechanical + electric modes per upgrade plan |
| **2** | **`GEN-MOTOR-IND-R&D-1`** | One lamination/winding program — **generator upgrade + industrial motor** |
| **3** | **`LINE-SHAFT-MOTOR-DRIVE-1`** | Motor → shaft → belts · **same buildings as today** |
| **4** | **`EC-1-GRID-FEEDER-4`** | **Substantial** run to G2 MS · gauge from loss model |
| **5** | **`MACHINE-RELOC-G2-MS`** | Move tools · retire long belt runs where safe |

## Design anchors

- **WW-2 plan already allows mechanical-first:** turbine → reduction → **`BELT-TREE-1`** without waiting on electric *(clutch M before G)*.
- **Batteries bridge** gate changes — not continuous forge/mill duty.
- **Motor and generator R&D are one program:** same iron stack, winding, comm, brush lessons — different field connection.
- **First shop drive is belts on a line shaft** — matches campus grammar; direct motor-per-machine is later optimization.
- **Feeder-4 must be sized from measured loss**, not Feeder-2 copy-paste — **~44–80 m class** and **motor I** may force **heavier gauge or shorter route**.

## Measurement day checklist *(d5081+)*

1. **Prony / strap brake** on each live clutch path — record **N·m vs rpm** at working notch.
2. **`BLOCK-BENCH-LINE-SHAFT-1`** — draw during ×16 sprint class if safe.
3. **`MOTOR-2`** — R, stall torque, I @ fan load · compare to **`MOTOR-1`**.
4. **Feeder audits** — V_wheelhouse vs V_tap at **known I** (cell bench, fan ON) — patch loss table.
5. **Stake Feeder-4** — length, cleat route, **`PARK-MFG-1`** chase — estimate R before wire draw.
6. **Slate target:** **`MOTOR-IND-1` torque ≥ max machine row + margin** · **`GEN-WW-2` headroom** after **I²R(Feeder-4)**.

## Targets *(slated d5081)*

| ID | Spec |
|---|---|
| **`MOTOR-IND-1`** | **≥ ~130 N·m @ ~35–60 rpm** line shaft · **I_run ≤ ~0.42** on Feeder-4 |
| **`EC-1-GRID-FEEDER-4`** | **~51 m · 1.2 mm paired** · **R_est ~1.55** · chase @ G2 east jamb |
| **Budget torque** | Mill clutch **D** slip **~125 N·m** — motor + belts must clear with margin |

## Open questions

- Single **line shaft** location for motor drive vs motor at wheelhouse with long mechanical shaft.
- Whether **turbine mechanical** and **motor electric** run **concurrently** on light days *(upgrade plan says prove one loaded output first)*.
- **`FEEDER-4`** tap in **MS-3** stub vs wait for **C-4** trunk — stub tubes early, copper when motor exists.
