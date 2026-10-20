# `STEEL-STANDARDS-SPRINT-Y13-1`

**Filed:** d3897 · **Cal-Y13 D25** · **~14 Jan**
**Gate:** magnet steel first · then structural · then spring · before motor standard hero
**Related:** [heat-register-y12.md](../government/regulations/heat-register-y12.md) · [manufacturing-code-2.md](../government/regulations/manufacturing-code-2.md) · **`GEN-WW-2`** · motor arc

---

## Intent

Register **homogeneous steel heats** under **MFGC-2** — not case-hardened wrought iron — and certify **repeatable alloy families** with charge sheets, coupons, and assay linkage.

> ★ **`CS-BAR-Y12-1/2` are pack-carburized wrought iron.** *They do not count as steel stock. The next step is a registered melt.*

> ★ **Magnet steel first.** *Stronger permanent magnets raise the motor ceiling immediately — field bootstrap, pole bias, or a return to PM-field machines with less sag than **`MAG-BOOT-EM`** class.*

---

## What is already paid for

| Asset | State |
|---|---|
| **`MFGC-2-CI` rhythm** | **`HEAT-Y12-001`–`004` PASS** · ~3.5 % C repeat |
| **`FMN-STD-Y12-1` triplicate** | **`HEAT-Y12-006`–`008` PASS** · **`FMN-BUTTON-Y12-1/2/3`** |
| **Combustion C assay** | **`COMBUSTION-C-TRAIN-Y12-1` live** |
| **`TC-PROBE-1` + ladder** | Muffle / furnace witness |
| **`FURNACE-2` + `MUFFLE-1`** | Empty heat PASS · atmosphere manifold defer |
| **Feedstock** | **`H-11-HEMATITE` ~4.47 kg** · **`M-22-MAGNETITE-1` ~18.0 kg** · **`M31-A` dressed ~54 kg @ bay** |
| **Magnet baseline** | **`MAG-BOOT-EM` ×8** · **`MAG-BOOT-SPARE` ×4** · **d1906 hot-quench grammar** |

---

## Alloy families *(target IDs)*

| ID | Role | C band *(target)* | Other | First use |
|---|---|---|---|---|
| **`ST-MAG-1`** | **Magnet steel** · permanent pole / bootstrap rod | **~0.8–1.2 %** | **Mn from `FMN-STD-*`** · magnetite feed bias | **Stronger **`MAG-BOOT-*`** successor · motor field** |
| **`ST-STR-1`** | **Structural** · frames · shafts · brackets | **~0.15–0.35 %** | **FMN deox** · homogeneous bar | **Motor frame · campus steel** |
| **`ST-SPR-1`** | **Spring** · brush · leaf · retainer | **~0.55–0.75 %** | **Oil quench + draw temper ladder** | **Commutator brush spring · wagon leaf class** |

---

## Build sequence *(priority order)*

### Phase A — grammar *(1–2 heroes)*

1. **`MFGC-2-ST-SLATE`** — ✓ **d3897** · alloy table · assay extensions
2. **`STEEL-HEAT-GATE-Y13-1`** — charge sheet template · steel ≠ CI char ratio · **`HEAT-Y13-009`** exploratory
3. **Extend assay** — ✓ **`ASSAY-Y13-001` ~1.0 % C PASS d3901** · ⚑ **Mn spot defer** until wet chemistry queue names it

### Phase B — magnet steel *(immediate)*

4. **`ST-MAG-HEAT-1`** — ✓ **d3898 · `HEAT-Y13-009` · `ST-MAG-BUTTON-Y13-1` ~74 g PASS exploratory**
5. **`ST-MAG-FORGE-1`** — ✓ **d3900 · `MAG-STEEL-Y13-ROD-1` ~72 g · ~44 mm lift vs ~36 mm `MAG-BOOT-EM` baseline**
6. **`ST-MAG-CERT-1`** — ✓ **d3903 · `MAG-STEEL-Y13-ROD-1/2/3` triplicate · `ST-MAG-1` production class**

### Phase C — structural + spring

7. **`ST-STR-HEAT-1`** — ✓ **d3906 · `HEAT-Y13-012` · `ST-STR-BUTTON-Y13-1` ~76 g PASS exploratory**
7b. **`ST-STR-FORGE-1`** — ✓ **d3911 · `ST-STR-BAR-Y13-1` ~71 g · `ASSAY-Y13-002` ~0.24 % C PASS · first `ST-STR-1` cert**
8. **`ST-SPR-HEAT-1`** — ✓ **d3913 · `HEAT-Y13-013` · `ST-SPR-BUTTON-Y13-1` ~77 g PASS exploratory**
8b. **`ST-SPR-FORGE-1`** — ✓ **d3914 · `ST-SPR-STRIP-Y13-1` ~70 g · `ASSAY-Y13-003` ~0.64 % C PASS · snap PASS**

### Phase D — code migration

9. **`MFGC-2-ST` table** — live **`ST-*`** rows replace WI placeholders for certified stock
10. **`MFGC-1 ST column`** — migrate when **`ST-STR-1`** cert exists

---

## Charge doctrine *(steel vs CI)*

| | **CI (`MFGC-2-CI`)** | **Steel (`MFGC-2-ST`)** |
|---|---|---|
| **Goal** | **~3.5 % C** grey iron | **Target C band** · solid steel button/bar |
| **Char** | **Heavy reducing pack** | **Less char · faster decarb risk — watch** |
| **Addition** | None | **`FMN-STD-*` pinch** · optional **`M-22` bias for MAG** |
| **Coupon** | Grey fracture · speckle | **Bright grain · spark vs CI** · magnet stick for **`ST-MAG`** |
| **Assay** | Combustion C **mandatory** | Combustion C **mandatory** before **PASS production** |

---

## Motor link

| Step | Depends on |
|---|---|
| **Stronger PM field** | **`ST-MAG-1` cert** |
| **Motor frame / shaft** | **`ST-STR-1` cert** |
| **Brush gear** | **`ST-SPR-1` cert** |
| **Motor standard hero** | **Above + `EC-1` grid tap live** ✓ |

---

## Ethanol / barrel note

**`BARREL-5-FERMENT` ✓ LIVE d3896** · empty · first load defer. A **second barrel (`BARREL-6`)** is optional scale — queue after steel/motor arc unless harvest surplus forces earlier.

---

## Window

| Milestone | Target |
|---|---|
| **Slate filed** | **d3897** |
| **First steel heat `HEAT-Y13-009`** | **✓ d3898 PASS exploratory** |
| **`ST-MAG-1` cert** | **Before motor build hero** |
| **Full trio certified** | **Before spring sow prep crowds bench** *(soft gate)* |
