# Magnet peak — practical ceiling @ CY15 tech *(issued d5568)*

**Status:** **ACTIVE** · **Phase 0 ✓ d5578** · **Phase 1 next**  
**Player intent:** Turn **all** dials toward the **best repeatable poles** this campus can certify — not Nd/Co physics, but a **stable production class** for **`GEN-AC-1`**, **`MOTOR-4`**, and successor motors/alternators. **Quantity at two tiers:** bootstrap for field bank · **`ST-MAG-1`** for machines that care.

**Links:** [gen-ac-1-cy15.md](gen-ac-1-cy15.md) · [electric-grid.md](../inventory/electric-grid.md) · heat register **`HEAT-Y15-009`–`011`** · **`EM-COIL-3`** · **`FURNACE-2`**

**Parallel tracks (not sequential):** **`MAG-QUENCH-CELL-1`** ↔ **`EC-1` / `GEN-AC-1` headroom** — more stable **I** during quench is the same infrastructure push as alternators/motors; log both on the grid plan and the magnet plan.

---

## Target bands *(solo lift · standard pin · room temp)*

| Tier | Process | Lift class | Use |
|---|---|---:|---|
| **A — bootstrap** | **`M-22` roast → forge rod → N-quench + `EM-COIL-3`** | **~37–39 mm** *(hard cap ~40)* | Volume · culina · keeper stock · **`GEN-AC-1` hybrid trim** |
| **B — cert (`ST-MAG-1`)** | **`H-11` + roasted `M-22` + `FMN` melt → draw → quench + field** | **~44–48 mm** *(practical peak **~46–47**)* | Motor fields · alternator pole caps · **`MOTOR-4` class** |
| **C — aspirational (same alloy)** | Tier B + **grid-fed quench cell** + charge SPC | **~48–50 mm** sporadic | **Not production** until **3-of-3** triplicate |

> **Practical peak** = **Tier B at triplicate closure** with **σ ≤ ~1 mm** within a heat lot — not one lucky rod.

---

## What moves the needle most *(order)*

| Rank | Dial | Why | First move |
|---:|---|---|---|
| **1** | **Quench align field** | Bootstrap and **`ST-MAG-1`** share the same bottleneck: **domains lock to whatever B you apply in the first seconds.** Today: **`EM-COIL-3`** bench · hand cadence. | **`MAG-QUENCH-CELL-1`**: grid feed **`EC-1`** through **`EM-COIL-3`** (or **`EM-COIL-4`** duplicate) · fixed pole shoes · rod fixture · **logged A/B vs hand** |
| **2** | **`ST-MAG-1` production** | **~5–8 mm** over bootstrap — alloy path already **proved** (`HEAT-Y15-009`–`011`). | **`ST-MAG-SPRINT-CY15-2`**: **×6 heats** · **×6 cert rods** · FMN chip from **`FMN-BUTTON`** master · charge sheet frozen |
| **3** | **Roast consistency (`M-22`)** | Bias charge quality for melt **and** bootstrap pea. | Finish **~6.4 kg raw** roast · crock **≥ ~8 kg** roasted before big sprint |
| **4** | **`H-11` dress / slag** | P/S kills coercivity on cert steel. | Crumb charge · magnet reject · **no green vitrified inclusion** in crucible |
| **5** | **Forge draw geometry** | Pole aspect ratio + surface decarb. | **`ST-MAG-FORGE`** SOP: length · square section · light grind before quench |
| **6** | **Thermal stability** | Machines demagnetize under heat / reverse mmf. | **Tier B only** on hot fields · bootstrap on **`GEN-AC-1`** hybrid + wound trim per [gen-ac-1-cy15.md](gen-ac-1-cy15.md) |
| **7** | **Volume @ grade** | Alternators need **×12–24** poles in a class, not one hero. | After Phase 0–2: **parallel** roast batches + **×6 rod weeks** |

**Deprioritize for peak strength:** heavy **temper** on magnet steel (softens) · more bootstrap without quench-cell upgrade (same chemistry ceiling) · **`M-22-UP`** lens (worked out).

**Later tiers (not CY15 peak):** Co steel · Ni–Co · rare earth — different plan.

---

## Phased path

### Phase 0 — **Quench cell** *(highest ROI · start here)*

| Step | ID | Done when |
|---|---|---|
| 0.1 | **`MAG-QUENCH-GATE-CY15-5577`** slate | **✓ d5577** |
| 0.2 | **`MAG-QUENCH-CELL-1` fab** | **✓ LIVE d5578** |
| 0.3 | **`MAG-QUENCH-AB-CY15-5578`** | **✓ · Δ ~+1.7 mm mean** |
| 0.4 | **`MAG-QUENCH-SOP-CY15-5578`** | **✓ filed d5578** |

### Phase 1 — **`ST-MAG-1` lot production**

| Step | ID | Done when |
|---|---|---|
| 1.1 | **`ST-MAG-BATCH-GATE`** | **`CHAR-LANE` ≥ ~25 kg** · crucibles · **`FMN`** chip weighed |
| 1.2 | **`ST-MAG-HEAT-Y15-012`–`017`** | **✓ 6/6 d5580–5588** |
| 1.3 | **`ST-MAG-FORGE-Y15-LOT-1`** | **✓ `ROD-4`–`9` @ cell** |
| 1.4 | **`ST-MAG-CERT-Y15-2`** | **Next** |

**Deliverable:** **×6–12 `MAG-STEEL-Y15-*`** install-ready · **×2–4** spares @ tray.

### Phase 2 — **Feed pipeline**

| Step | ID | Done when |
|---|---|---|
| 2.1 | **`M-22-ROAST`** batches 2–3 | Raw **×0** · crock **~8–10 kg** roasted |
| 2.2 | **`MAG-BOOTSTRAP`** optional sprint | **×6–12** Tier A for **`GEN-AC-1`** pole bank *(hybrid field)* |
| 2.3 | **`M-22-TALUS-S1`** re-haul | When crock < **~4 kg** mid-sprint |

### Phase 3 — **Machine allocation**

| Machine | Field spec | Count |
|---|---|---|
| **`GEN-AC-1`** | **Hybrid:** Tier A pole magnets + wound correction · **Tier B optional pole caps** | **×12–16** A + **×4** B caps |
| **`MOTOR-4` / successors** | **Tier B** full stack | **×2–4** poles each |
| **Bench / culina** | Tier A | as needed |

---

## Stock gates *(live d5568)*

| Row | Read | Gate |
|---|---|---|
| **`MAG-BOOT-EM`** | **×20** tray + installs | **OK** for Tier A bank |
| **`MAG-STEEL-Y15`** | **×3** cert + **×2** in **`MOTOR-4`** | **Need lot** for scale |
| **`M-22` raw / roast** | **~6.4 kg / ~2.75 kg** | **Roast before Phase 1** |
| **`H-11-HEMATITE`** | **~88 kg** | **OK** |
| **`FMN-BUTTON`** | master chip | **Verify vial @ bench** before heat |
| **`CHAR-LANE`** | **~20.5 kg** post-d5567 | **≥ ~25 kg** before **`ST-MAG` ×6** week |
| **`EM-COIL-3`** | bench LIVE | **Upgrade → cell** |

---

## Success criteria *(“reasonable peak”)*

1. **Cert class closed:** **`ST-MAG-CERT-Y15-2`** with documented **`HEAT-Y15-*`** charge.
2. **Machine poles:** **≥ ×12** Tier B or hybrid-capable poles **without** scavenging **`MOTOR-1`/`MOTOR-4`**.
3. **Repeatability:** second **×6** lot within **±1 mm** of first lot mean.
4. **Bootstrap role:** Tier A explicitly **not** used where **`MOTOR-4`** stall torque matters.

---

## Immediate next heroes *(player queue)*

1. **`M-22-ROAST`** batches 2–3 *(raw **~6.4 kg** · crock thin)*  
2. **`ST-MAG-HEAT-Y15-012`** @ **`FURNACE-2`** · quench **@ cell**  
3. **`MAG-BOOTSTRAP`** sprint @ cell for **`GEN-AC-1`** bank  

*Plan owner:* magnet sprint · alternator/motor bank · revises on each **`ST-MAG`** or **`GEN-AC-1`** field log.
