# Ethanol → butadiene R&D pathway · CY14

**Filed:** d5227 planning read · **live state:** [now.md](../now.md) · **inventory:** `ETHANOL-DEHYD-*` · `OLEFIN-TRAP-STOCK-Y14-1` · `C4-COUPLING-STOCK-Y14-1`

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

```
[feed: high ethanol] → [preheat / vaporizer]
    → [bed cartridge: dehyd | olefin | future aldehyde]
    → [sweep manifold: N₂ or AIR-PUMP stroke class]
    → [trap train: C₂ jar → C₄ jar → waste heel]
    → [assay ports: TC · bromine · maleic anhydride paper]
```

- **Modular cartridges** — swap bed, not rebuild the lane.
- **Stub flange** for future **Route B** aldehyde condenser leg (no commit until step 6).

## Ordered ladder (player + agent default)

| # | Step | Type | Gate |
|---|---|---|---|
| **1** | **Build `POLYMER-LANE-PILOT-1`** | ⚒ | Modular bed + trap train @ chem wing · gas-tight grammar |
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
