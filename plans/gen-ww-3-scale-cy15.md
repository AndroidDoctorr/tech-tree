# `GEN-WW-3` — power program · kiln north star *(updated d5486)*

**Status:** **Phase 0 ✓ · kiln phase OPEN**  
**North star:** **`ELEC-PROCESS-HEAT-1`** — small electric muffle/kiln @ **forge/fabrica class** · cuts **wood · char · lime** hauls · **passive** duty so other work continues.  
**Not the goal right now:** new machine-shop volume · **`MOTOR-IND-1`** at G2 · campus lighting scale-up — those follow **kiln → faster masonry → MS shell**.

**Player path (explicit):** **power → kiln → faster construction → machine shop → machines on existing shaft/grid.**

**Links:** [electric-grid.md](../inventory/electric-grid.md) · [industrial-mech-drive-cy14.md](industrial-mech-drive-cy14.md) · [ww-2-crossflow-design-y15.md](ww-2-crossflow-design-y15.md) · [ww-2-power-upgrade.md](ww-2-power-upgrade.md) · **`MOTOR-4` / blower R&D** *(DC loads · not alternator)* · [culina-modernization-y14.md](culina-modernization-y14.md) Phase 5 *(oven = distant cousin; process muffle is earlier)*

> **`MOTOR-4` was never the alternator track** — it teaches **brush · torque · duty** on the **commutator dynamo** you run today. **Alternator = AC machine** (no commutation) · **defer** until stiff DC bus + trunks · see Track 4 below.

---

## Where you are *(measured · d5484–5486)*

| Layer | Read | SI class |
|---|---|---|
| **Crossflow hydraulic** | **~0.92 kW** @ **Q ~17.2 L/s · H ~6.32 m** | **~1 kW** in water at runner *(summer nadir · not winter max)* |
| **Belt tree (clutch M)** | **~0.40 kW** Prony class | **Mechanical shop already wins** — lathe/mill on **M** |
| **`GEN-WW-3-M` electrical** | **~9.58 GB open · ~8.14 R · ~1.51 I short · peak ~2.80 GB·I** | **~2.8 W** peak · **~4.6 V @ ~0.57 A** matched |
| **`GRID-TAP-G2-MS-1` @ 0.42 I** | **~5.50 GB** loaded | **Feeder-4 margin ✓** for **motor** class · **not** kiln class |
| **Undershot `WW-2`** | Bypass | Spare rollback |

★ **Big step up from `GEN-WW-2` + apron (~2.1 GB·I peak, ~0.41 kW shaft)** — but **electrical ceiling is still watts, not kilowatts.** Kiln is realistic as a **program**, not as **“flip switch tomorrow.”**

---

## Kiln power tiers *(targets for R&D — not yet measured)*

| Tier | Role | Electrical need *(order of magnitude)* | vs today |
|---|---|---:|---|
| **P0 — bench muffle** | Element grammar · soak curve · fuse discipline | **~5–30 W** sustained | **✓ in reach** @ wheelhouse tap · **`MOTOR-4` blower** proxy |
| **P1 — pilot process oven** | Dry/lime **assist** · small chamber · long preheat | **~50–150 W** sustained | **Marginal** — needs **stiffer gen + local tap** |
| **P2 — production assist** | Meaningful **char/lime** substitution | **~200–800 W** sustained | **Not yet** — **hydro + Cu + dedicated feeder** |
| **P3 — “heavy duty”** | Shop motors + kiln same season | **kW class** | **XL / alternator horizon** |

> **Process heat wants steady I at a useful V**, not peak **GB·I** for one second. The sprint is **stiffness + duty cycle + element R&D**, not another apron on the wheel.

---

## Sprint order *(sensible · parallel where noted)*

### Track 1 — **Water** *(raises ρgQH · no new copper)* · **start now**

| # | Work | Why | Gate |
|---:|---|---|---|
| 1 | **Winter / spring Q + H survey** *(gate wide vs summer nadir)* | You have **not seen max forebay** yet | One measure hero + chalk |
| 2 | **Invert smooth pass** *(Route A)* | Friction was budgeted **~0.12 m** — cheap head back | After flow stable |
| 3 | **Nozzle A/B tune · spill crest** | **Q ~17 vs 18 L/s design** · rpm already **~268** | d5486 baseline |
| 4 | **Trash screen / bypass policy** | Spill is lost **ρgQH** | Maintenance |

★ **Do not skip (1)** because summer reads falsely “maxed.” Crossflow already beat the wheel; **seasonal water** is the next free multiplier.

### Track 2 — **Mechanical** *(shop already good · protect turbine)* · **maintenance band**

| # | Work | Why |
|---:|---|
| 5 | **Belt dress · idler · clutch G drag** post cut-over | Every watt of drag is gen food |
| 6 | **`GS-2-FLYWHEEL-1` on ~10 rpm shaft** *(if not already)* | Kiln **preheat windows** — smooth gen load |
| 7 | **Clutch doctrine:** **M = machines · G = gen** — not both heavy |

Lathe/mill: **already on Track 2 winner** — focus electrical elsewhere.

### Track 3 — **Electrical stiffness** *(THE kiln gate)* · **main sprint with elements**

| # | Work | Why | Depends |
|---:|---|---|---|
| 8 | **`ELEC-PROCESS-HEAT-1` element R&D** *(bench)* | Nichrome/class grammar · **`MOTOR-4` throat** = blower · **future knowledge** = not blind | **∥** all |
| 9 | **Muffle + brick box** *(small · forge-adjacent)* | “Just a box” — **fuse · interlock · gen-on policy** | P0 element |
| 10 | **`GEN-WW-3-M` armature program** — **more Cu · lower R** | **~8.14 R** sags V under **I** — kiln needs **amps** | Draw + rewind hero |
| 11 | **Row L evaluation** *(plan table)* | **~7.5 R · ~1.95 I_short · ~3.4 GB·I peak** — still **watts** but **stiffer** | After (10) or combined |
| 12 | **`EC-1-KILN-TAP-1`** — **short heavy paired** @ **Fabrica / forge** | **Feeder-4 @ 51 m** is for **MS** · kiln should be **local** first | Site pick |
| 13 | **Sustained load line** @ kiln tap | **Not** open-circuit brag — **30 min @ target I** | (10–12) |

### Track 4 — **Deferred · know the names**

| Topic | Verdict |
|---|---|
| **AC generation** | **Different machine** (alternator) or **motor-generator** — **not** a commutator tweak. **Down the line** after stiff **DC bus** and trunks. |
| **“Convert” DC→AC** | **Rotary converter / vibrator** — R&D arc · **not** before kiln P1. |
| **Commutator vs AC losses** | Commutator losses matter at **motors**; **resistive kiln runs on DC fine.** AC helps **long transmission**, not element physics. |
| **Transformers** | Need **AC**. Use case: **step up V · lower I** on **long** runs, **step down** at load. With **DC shunt gen**, first win is **thick short feed + lower R_arm**, not transformers. Revisit when **[ec-1-campus-expansion.md](ec-1-campus-expansion.md) Phase 5** AC is live. |
| **`GEN-WW-2` parallel / XL** | **Rollback spare exists** — only if **L + hydro** still miss **P2** |

---

## Bang-for-buck table *(updated)*

| ID | What | Peak **GB·I** | **Sustained I** class | Kiln relevance |
|---|---|---:|---|---|
| **Hydro tune** | Q · H · nozzle | — | **+ shaft kW** | Indirect · more **G** headroom |
| **`GEN-WW-3-M` today** | Built | **~2.8** | **~0.57 @ matched** | **P0 only** |
| **M + Cu rewind** | Same iron · fatter wire | **~3–3.5** est | **↑ I @ same wind** | **P1 path** |
| **Row L** | Heavier stack + field | **~3.4** est | **↑** | **P1–P2 bridge** |
| **Local kiln feeder** | 1.6–2 mm · **&lt;15 m** | — | **less I²R** | **Required for P1+** |
| **Elements + muffle** | R&D | — | sets **W target** | **Defines gen goal** |

---

## Sequence *(supersedes d5469 list)*

1. ✓ **Crossflow Route A + cut-over** — d5486  
2. ✓ **`GEN-WW-3-M` + Feeder-4 margin** — d5483–5485  
3. **∥ Water survey (winter) + invert/nozzle + belt maintenance**  
4. **∥ `ELEC-PROCESS-HEAT-1` P0 bench + muffle box**  
5. **Gen stiffness hero** (Cu rewind / **L** decision) + **kiln tap**  
6. **P1 pilot kiln** — scheduled preheat · **gen interlock** · prove lime/char **assist**  
7. **MS shell / G2** — **after** kiln proves **binder/runway** time savings  
8. **`MOTOR-IND-1`** · heavier feeders · **AC** — **after** DC kiln lane honest  

---

## Open measurements

- **Winter Q · H** on Route A *(max ρgQH)*  
- **Sustained I** @ **P0/P1** element without brush flash  
- **Element R(T)** curve · **`MOTOR-4` blower** curve @ kiln throat  
- **Kiln site:** **Fabrica south** vs **forge east** — shortest **heavy** feed  

---

## Legacy scale scenarios *(armature + field · d5469)*

| ID | Core vs `GEN-WW-2` | Field | Est **R** | Est **I_short** | Peak **GB·I** | **Cu class** | Verdict |
|---|---|---|---:|---:|---:|---:|---|
| **S** | **+15% lam** | Reuse shunt | **~7.8** | **~1.15** | **~2.3** | **~+0.6 kg** | Superseded by **M ✓** |
| **M** ★ | **~1.45× lam** | Dual shunt **0.5 mm** | **~8.2** | **~1.55** | **~2.85** | **~+1.6 kg** | **✓ built d5471–5483** |
| **L** | **~1.9× lam** | Heavy shunt | **~7.5** | **~1.95** | **~3.4** | **~+3.0 kg** | **Kiln P1–P2 candidate** |
| **XL** | 2× machine | Parallel | — | — | **~4+** | **2× M** | Only if **L + winter Q** fail **P2** |

**Loss budget reminder** *(Feeder-4 @ design I)*:

```text
V_gen(open) ≈ 9.6 GB          (GEN-WW-3-M · summer)
I_run       ≈ 0.42            (MOTOR-IND slate)
R_feed      ≈ 1.52 R          (measured d5485)
ΔV_feed     ≈ 0.64 GB
V_tap       ≈ 5.5 GB loaded   (motor margin ✓ · kiln wants local tap)
```
