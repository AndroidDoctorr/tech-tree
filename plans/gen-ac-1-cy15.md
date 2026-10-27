# `GEN-AC-1` — campus alternator capstone *(issued d5497)*

**Status:** **DESIGN OPEN** · fab **NOT STARTED**  
**Player intent:** **Leapfrog** `GEN-WW-3-M` — **do not strip the live dynamo** · recover **`GEN-WW-2`** + stock Cu for the AC machine · **lights stay DC** · **AC for motors + heavy distribution** once **`XFMR-1`** class exists.

**Supersedes as north star:** [gen-ww-3-scale-cy15.md](gen-ww-3-scale-cy15.md) kiln-first sprint *(kiln still valid on DC · capstone power = AC + scale)*.

**Links:** [electric-grid.md](../inventory/electric-grid.md) · [ww-2-crossflow-design-y15.md](ww-2-crossflow-design-y15.md) · [ec-1-campus-expansion.md](ec-1-campus-expansion.md) · [ec-1-wind-campus-cy15.md](ec-1-wind-campus-cy15.md) *(housekeeping DC · not alternator substitute)* · **`MOTOR-4` R&D** · [industrial-mech-drive-cy14.md](industrial-mech-drive-cy14.md)

---

## Doctrine

| Rule | |
|---|---|
| **`GEN-WW-3-M`** | **Stays LIVE** · DC lamps · cells · bench · rollback |
| **`GEN-WW-2`** | **Approved harvest** @ bench · wire + lam + yoke scrap → **`GEN-AC-1` bill** |
| **Bus** | **Dual:** `EC-1-DC-*` unchanged · **`EC-1-AC-TRUNK-1`** new |
| **Power goal** | **Hundreds of watts** electrical class *(sustained **~100–300 W** target · peak **~400–600 W** aspirational @ winter NORMAL)* |
| **Not the goal** | Cannibalize **M** · single-bus AC migration · pretend AC adds shaft kW |
| **`ELEC-PROCESS-HEAT-1`** | **Yes — sized for it.** **Row L** **~200–500 W peak · ~100–300 W sustained** matches **P2** process assist in [gen-ww-3-scale-cy15.md](gen-ww-3-scale-cy15.md). **`M`** = **P0** bench muffle only; **electric oven / lime assist** is the leapfrog point. |

---

## Shaft budget *(ballpark · d5493 summer)*

| Quantity | Value | Notes |
|---|---:|---|
| **ρgQH @ runner** | **~0.96 kW** hyd | **~17.6 L/s · ~6.34 m** |
| **Mech @ clutch M** | **~0.42 kW** | Shop when engaged |
| **Available @ clutch G** | **~0.96 kW** input · **~0.75–0.85 kW** at gen after train | One loaded clutch |
| **Today `GEN-WW-3-M` peak** | **~2.92 GB·I** *(~3 W)* | Conversion + machine size limited |
| **Winter uplift (est.)** | **+10–25% ρgQH** | **NORMAL** re-read queue |

> **Hundreds of watts electrical** is plausible **only** with **(a)** larger iron + copper **(b)** alternator efficiency **(c)** winter/wet season headroom — not by swapping commutator for AC alone at **M** scale.

---

## Machine class — **`GEN-AC-1` @ row L** *(issued default)*

| vs `GEN-WW-3-M` | **L alternator** |
|---|---|
| **Core lam** | **~1.9×** pole span · same stack grammar as scale study |
| **Field** | **Hybrid:** **`MAG-BOOT-EM` pole magnets** + **light wound correction coil** *(bootstrap / trim)* · **`MAG-STEEL-Y15-*` optional pole caps** |
| **Rotor** | **Salient or non-salient** · **no commutator** · **~272 rpm** class @ crossflow |
| **Output** | **Single-phase** first · **~40–120 V** open class *(design tune)* · **~50–60 Hz** effective @ 4-pole grammar |
| **Est. peak** | **~350–500 W** class @ winter · **~200–350 W** summer nadir |
| **Est. sustained** | **~60–40% of peak** for kiln/motor duty planning |

**XL (2× machine)** — only if **L + winter Q** miss sustained target.

---

## Ballpark materials *(audit d5497 · refine each fab gate)*

| Line | Est. need | On hand / source | Gap |
|---|---:|---|---|
| **Cu wire (armature + field)** | **~4.5–6.0 kg** drawn | **`GEN-WW-2` harvest ~2.85 kg** *(d5508)* · tray **~510 g** · scrap **~445 g** | **~1.0–2.5 kg** electrowin/draw |
| **Si lam / iron core** | **~18–22 kg** finished stack | **`GEN-AC-1-LAM-SEED-1` ~9.1 kg** · bloom forge · **`H-11-HEMATITE`** | **~9–13 kg** lam stack @ **1.9×** seed |
| **`MAG-BOOT-EM` rods** | **×14–18 live** | **×14 @ tray · ×4 spare** *(d5504)* | **optional ×2–4** top-up |
| **Magnet steel / pole caps** | **~0.35–0.50 kg** | **`MAG-STEEL-Y15-ROD-3` spare** | **Hands off `MOTOR-4` stack** |
| **`M-22-MAGNETITE-1` feed** | **~4–8 kg** roasted charge class | **~5.0 kg @ pile 4** *(d5500 haul)* | **Roast + bootstrap sprint** |
| **Wrought / shaft / bearings** | **~6–8 kg** | **`IRON-BLOOM-1`** · **`WW-2-TURBINE-TRANSITION-1` grammar** | **Machine days** |
| **Insulation** | paper · wax · linen | flax shive · wax render | **Routine** |
| **`XFMR-1` pilot** | **~2–4 kg** lam offcuts · **~1.2 kg** Cu | same Cu program | **∥ after AC bench spin** |

**`GEN-WW-2` harvest list** *(approved · not `GEN-WW-3-M`)*:

- Armature + field **Cu** → draw stock  
- **Lam stack** → **`GEN-AC-1-CORE-1`** after measure  
- **Yoke / pole paths** → reuse or forge shoes  
- **Commutator + brush gear** → **museum / scrap** *(not AC)*

---

## Build order *(multi-week)*

1. **✓ Design issue** — d5497  
2. **✓ `GEN-WW-2-HARVEST-1`** — d5508 · **~2.85 kg Cu · ~9.1 kg lam seed**  
3. **`GEN-AC-1-CORE-1`** — lam stack @ L scale · **sheet issued d5509** · **~8.2 kg** `H-11` add to seed  
4. **`GEN-AC-1-FIELD-1` / `GEN-AC-1-ROTOR-1`** — bench spin  
5. **`GEN-AC-1-BENCH-SPIN-1`** — open V · Hz · scope class  
6. **`XFMR-1-BENCH-1`** — step-down to **lamp-safe** trial voltage  
7. **`EC-1-AC-TRUNK-1`** — wheelhouse → **one** motor building *(Fabrica / wing N)*  
8. **Clutch / schedule** — **G** to **`GEN-AC-1`** · **DC dynamo** on bench or second clutch hero  
9. **`ELEC-PROCESS-HEAT-1`** — revisit on **AC tap** after sustained load line  

---

## Resource collection sprint *(player: nothing else more important)*

| Priority | ID | Until |
|---|---|---|
| 1 | **Cu** | **`CU-CELL` runs** + malachite draw · **`GEN-WW-2` harvest** |
| 2 | **Iron / lam** | **Bloom + stack** · **`H-11`** roast path |
| 3 | **`MAG-BOOT-EM` bootstrap** | **`M-22` roast + hot-quench rod runs** · target **×6–10** new rods before **`GEN-AC-1-FIELD-1`** |
| 4 | **Excitation steel** | **`MAG-STEEL-Y15-ROD-3`** pole caps *(optional)* |
| 5 | **Char / fuel** | Kiln + forge + magnet quench runway |

**Defer hero:** new masonry MS shell · expeditions not named · **row L DC rewind** on **M**.

---

## Open design choices *(kitchen slate)*

- [ ] **4-pole vs 2-pole** @ **~272 rpm** → **~54 Hz vs ~27 Hz**  
- [ ] **Excitation:** fixed **`MAG-STEEL`** vs **field coil + slip rings**  
- [ ] **Clutch G:** swap **`GEN-WW-3-M` → `GEN-AC-1`** or **add `clutch H`**  
- [ ] **First AC load:** **`MOTOR-IND-1`** vs **wing N motor tap** vs **kiln P1**  

---

## Measurements to file before fab

- **`GEN-WW-2` strip audit** — kg Cu · kg lam · runout  
- **Winter NORMAL Q+H** — scale **`GEN-AC-1` target sustained W**  
- **`MOTOR-4` load curve`** — AC motor compatibility check  
