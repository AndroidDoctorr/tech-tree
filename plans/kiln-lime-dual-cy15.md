# Kiln lime — dedicated / dual layout + electric assist *(CY15)*

**Status:** **ISSUED d5549** · **KL-1 + KL-2 civil CLOSED d5560** · **`KILN-B-LIME-1` LIVE d5570** · **KL-3 electric defer** · **KL-4 twin optional** · pad **d5551** · grates **d5552** · sketch **d5550** · player: **next project after Kozan tin** · **char primary · electric = soak + control**  
**Parent:** [g2-ms1-machine-shop-cy14.md](g2-ms1-machine-shop-cy14.md) lime ledger · [ec-1-campus-expansion.md](ec-1-campus-expansion.md) · [ww-2-power-upgrade.md](ww-2-power-upgrade.md)

## Problem

**Kiln A** + retort shares **one human** and **one char lane**. Phase 1 wing alone is **~1.8–2.9 t QL-class** *(footing + mortar + grout)*. Manual single-bed cadence cannot keep pace with summer civil **and** everything else — player defer is rational.

**Goal:** **≥2× effective lime throughput** without pretending char is gone yet.

---

## Options *(not mutually exclusive)*

| Track | Throughput | Capex | Notes |
|---|---|---|---|
| **A — `KILN-B-LIME-1` dedicated** | **~1.8–2.2×** if tended in parallel | New stack · grate · hood · **`CACO3` bay** | **Default** — mirror Kiln A grammar · **lime only** |
| **B — Double-kiln **`KILN-AB-TWIN-1`** | **~2×** one fire session | Shared draft chimney · twin grates · one tender still bottleneck | Fire **both beds** on same char load · unload staggered |
| **C — Electric assist** | **Soak stability + trim** | Elements · relay · **`THERMOCOUPLE-1`** tap | **Not** full replacement — **hold 900–1000 °C band** · reduce underburn |

> **Player read d5549:** pursue **A + C** first sketch; **B** if yard setback allows one chimney serving two mouths without fighting Kiln A retort smoke.

---

## Electric assist — scope *(realistic CY15)*

| Layer | Intent | Grid |
|---|---|---|
| **Sense** | **`THERMOCOUPLE-1`** @ bed + flue · **`CAP-THERM-1`** witness | **`Z-BENCH`** stub |
| **Act** | **CR wire / nichrome gutter** under grate **or** side arch **~200–400 W class** per bed | **`EC-1`** branch · **not** trunk |
| **Control** | **Manual setpoint + contactor** first · no PID fantasy until clock stable | **`SW-*` interlock** with char fire — **elements off when grate cold** |
| **Char** | **Still charges kiln** — electric **tops** last 15–20 % soak · catches **underburn returns** | **`CHAR-LANE`** unchanged |

**Winter bench heroes:** element jig · soak A/B compare · **`FORSTERITE-GROG`** reflector ring reuse *(d5331 grammar)*.

**Explicit non-goals:** all-electric lime @ campus bus · abandoning **`CACO3-P7`** haul.

---

## Site — candidate

| Constraint | Read |
|---|---|
| **Wind** | **Downwind of apiary · upwind of domus** — same as Kiln A class |
| **Ash / lime dust** | **Tie to `MATERIARUM` apron** · slake trough **≤ ~15 m** |
| **Fuel** | **Char lane + retort** — second kiln **doubles char draw** → retort stays **every other day** class |
| **Electric** | **Short trench from `EC-1-GRID`** to kiln yard — **feeder amp modest** |

---

## Phase map

| ID | Work | Gate |
|---|---|---|
| **KL-0** | **`KILN-LIME-SLATE`** · dims · draft · element watt budget | **d5549 filed** |
| **KL-1** | Footings + grate shell **`KILN-B-LIME-1`** | Dry season · **`LIME-PUTTY-1`** mortar strip *(ironic)* · **plan @ d5550** |
| **KL-2** | Hood · **`CACO3` charge door** · ash pit | Match Kiln A ergonomics |
| **KL-3** | **`KILN-B-ELECTRIC-ASSIST-1`** — elements · TC · interlock | **`GEN-AC-1`** or **`WW-2`** bench power OK |
| **KL-4** | **`KILN-AB-TWIN-1`** chimney share *(optional)* | Only if KL-1 soak logs **GO** |

---

## **`KL-1` — `KILN-B-LIME-1` sketch / budget** *(d5550)*

**Site:** **Kiln yard · ~8 m east of Kiln A mouth** · shared apron drain · **smoke plume clears apiary** on summer breeze read.

### Footprint

| Item | Dim / count | Notes |
|---|---|---|
| **Pad** | **~1.6 × 1.4 m** gravel blind **≥ ~120 mm** | Fall to existing kiln drain |
| **Stack shell** | **~1.2 × 1.0 m interior · wall ~200 mm** | Mirror Kiln A throat height **−~50 mm** *(lower draft · lime not forge)* |
| **Grate** | **~0.9 × 0.6 m** iron bar grid · **~25 mm** gap class | Forge draw **×6 bars** · hinge service door south |
| **Ash pit** | **~0.4 m³** below grate · clean-out west | Shared shovel path with Kiln A |
| **Setback** | **≥ ~2 m** to Kiln A stack | **KL-4 twin chimney** leaves **~1.2 m** collar gap if pursued |

### **`KL-1-MAT-BUDGET`** *(footings + shell only — hood = KL-2)*

| Line | Qty class | Source | Notes |
|---|---:|---|---|
| **`GRAVEL-1`** | **~180–220 kg** | `MATERIARUM` bay | Blind + pad lift |
| **`SAND-FILTER-1`** | **~40 kg** | Bay | Pad screed |
| **`LIME-PUTTY-1`** | **~6–8 kg** | Trough | Shell mortar + pad set *(not firing lime)* |
| **`POZZ-TUFF-1`** | **~25 kg** | Bay | Pad binding |
| **`BRICK-FIRED-B`** | **~×52–64** | Yard | **Brick-only shell** *(player d5553 — **no `BLOCK-Y10`**)* |
| **`BLOCK-Y10`** | **×0** | — | **Reserved `MS-1`** |
| **`FORSTERITE-GROG-1`** | **~2–4 kg** | Kiln yard | Fire-face liner ring *(expand production)* |
| **Wrought grate bars** | **×6** | Forge | **~1 forge afternoon** |
| **Iron strap / hinge** | **forge scrap class** | Forge | Door · grate lips |
| **`WOOD-OAK-P5`** | **~15 kg** | Pile 5 | Form stakes · door plug temp |

**Labour:** **~2 hero days** KL-1 civil · **~½ day** forge bars · **defer KL-3 trench** until shell cured.

### Build order *(KL-1 heroes)*

1. **Probe + pad compact** · DPC grit band  
2. **Footing ring** · **brick wythe only** · to grate shelf — **✓ d5553–5555**  
3. **Grog liner** · grate set · ash throat — **✓ d5555**  
4. **Cure band ~48 h** *(from d5555)* · **KL-2 hood** may start on **cured shell lip** *(d5559)* — **first fire** waits **shell + hood** mortar · **not** green **`GB`** stack  

**Electric stub:** **conduit sleeve @ south jamb** only in KL-1 — **wire after cure** (KL-3).

---

## Stock / labour *(order-of-magnitude)*

| Line | Class |
|---|---|
| **Firebrick / grog** | **`FORSTERITE-GROG`** + campus brick tail |
| **Iron** | Grate bars · door hinges · element frame |
| **Cu / wire** | Element tail · **`Z-BENCH`** |
| **Labour** | **~4–6 hero days** civil + **~2** electric hang |

---

## Capacity ladder *(d5570 player read)*

### What “double” means today

| Name | What it is | Throughput |
|---|---|---|
| **`KILN-B-LIME-1`** | **One** lime bed · **`KL-1` shell + `KL-2` hood** | **~1× Kiln A** per tended session *(first fire d5570 · 1 load gentle)* |
| **Yard “double”** | **`KILN-A-LIME-*` + `KILN-B-LIME-*` same day** | **~1.8–2.2×** if **both** get ×2 loads · **char −~19 kg** · **one human** — realistic **parallel** |
| **`KILN-C`** | **Metal / glass / tin** furnace · bellows · **~1120–1180 °C class** | **Different duty** — not interchangeable with lime calcine |

### **`KILN-B` + `KILN-C` + `KILN-A` same day?**

| Pair | Realistic? | Bottleneck |
|---|---|---|
| **A lime + B lime** | **Yes** — best use of “double kiln” | **Tender attention** · **char ~9–10 kg per bed ×2** · stagger unload |
| **B lime + C metal/glass** | **Sometimes** — **AM/PM split** | **C needs bellows watch** · **lime is soak + draft** · smoke/wind apiary rule |
| **A + B + C all hot** | **Rare hero** — not steady cadence | **Char lane** · **three ash paths** · **miss one door = ruin one batch** |

> **Verdict:** **A+B lime** = plan default · **+C** = **overlap on calendar**, not **three full fires one afternoon**.

### Triple / quad *(char-retort analogy)*

| Layout | Idea | CY15 realism |
|---|---|---|
| **`KILN-AB-TWIN-1` (KL-4)** | **Twin grates · one chimney · one char preheat** | **~2 mouths / 1 tend** · **not built** — needs KL-1 soak logs **GO** *(d5570 started)* |
| **Triple** | **A bed + B twin + retort** | **Char retort is ⧗** — lime is **⚒ watch** · triple **lime-only** = **yard redesign + shared plenum** |
| **Quad (4 mouths)** | **Retort-style manifold** | **Fuel yes · human no** as daily ops — **electric soak (KL-3)** is how you buy **capacity without ×4 grates** |

**Retort analogy limit:** char quad works because **unload is timed · tend is burst**. Lime **needs draft + soak judgment** per bed — **parallel mouths** scale **~√(tender hours)**, not ×4.

### Electrical assist (KL-3) — capacity effect

| Mode | What it does | Effective gain |
|---|---|---|
| **Trim soak** | **~200–400 W/bed** holds **900–1000 °C** last **15–20 %** · fewer underburn returns | **~+10–25 % CaO per char kg** *(plan est.)* |
| **Stagger** | Human loads stone **while** element holds previous bed | **~+0.5 load/day** same calendar |
| **Not** | Replace char | **Grid `EC-1`** cannot calcine **kg/h** class without **`GEN-AC-1`** scale |

**Queue after first B fire:** **`KILN-B-LIME` load 2** · **`KILN-A` + `KILN-B` paired day** · **`KL-3` stub wire** when **`GEN-AC-1` / quench cell** branch is live.

---

## Links

- Lime demand: [g2-ms1-machine-shop-cy14.md](g2-ms1-machine-shop-cy14.md) **lime ledger**
- Wind / deadmen grout: [ec-1-wind-campus-cy15.md](ec-1-wind-campus-cy15.md)
- Queue: [next-items.md](next-items.md) **`KILN-B-2`**
