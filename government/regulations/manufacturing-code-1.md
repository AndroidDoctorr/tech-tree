# Manufacturing Code 1 *(MFGC-1)*

**Filed:** Day 3558 · **Cal-Y12 D39** · **~8 Feb Y12**
**Scope:** fasteners, pipe, and workshop-produced mechanical stock @ HOME campus
**Related:** [measurement-code-1.md](measurement-code-1.md) · [electrical-code-1.md](electrical-code-1.md) · [campus-operations.md](../procedures/campus-operations.md)

> ⚑ **Split policy:** pipe fittings · bevel gears · sheet stock may become **MFGC-2+** when tables outgrow one file. Until then, **one code, named sections.**

---

## Intent

Unify **`TORR-FASTENER-STANDARD-1`** and the new **pipe series** under one manufacturing law — nominal sizes, materials, test-before-production, and which machine owns which dimension.

---

## MFGC-1-MAT — material classes

| Class | Symbol | Use | Pressure note |
|---|---|---|---|
| **Wrought iron** | **WI** | Bloom · forge · first pipe trials | Lower hoop yield — **conservative P column** |
| **Steel** | **ST** | ⧗ branch open · barrel · pressure pipe | Target for rated pipe + musket bore |
| **Brass / bronze** | **BR / BZ** | Bushings · nuts · low-load fittings | Not pressure primary |
| **Copper** | **CU** | Wire · rolled seam tube · conductor | ★ **Conductor economics** — not default drain pipe |

---

## MFGC-1-FAST — fasteners *(live)*

**Authority:** **`TORR-FASTENER-STANDARD-1`** @ kitchen slate + **`METROLOGY-CELLAR-1`** copy.

| Family | ID grammar | Pitch / form | Machine |
|---|---|---|---|
| **Bolt / nut** | **BN-06** | **~1.0 mm · 60° · RC-06** | **`LATHE-V2`** power thread · hand die backup |
| **Wood screw** | **WS-COARSE-*** | Coarse taper · pilot chart | **`WS-HAND-CHASE-1`** · lathe turn |
| **Stud** | **BN-STUD-06-*** | Double-ended BN | Forge + lathe |
| **Grub** | **BN-GRUB-06-*** | Cup point · set screw | Lathe + case tip |

**Length grades (BN-06):** **S ~14 mm · M ~24 mm · L ~36 mm** — masters on **`BN-TRAY-Y12-1`**.

**Batch rule:** copy from **gen-3 certified pair** — do not re-invent pitch per batch.

---

## MFGC-1-PIPE — pipe series *(defined · not mass-production yet)*

### Nominal grammar

**`PT-{RC}-{wall}`** — **P**ipe **T**ubular · **RC** nominal ID · **wall** letter.

| ID | Nominal ID (mm) | OD (mm) | Wall t (mm) | Metal area (mm²) | Flow area (mm²) |
|---|---|---|---|---|---|
| **PT-06-A** | 6.0 | 10.0 | 2.0 | 50.3 | 28.3 |
| **PT-10-A** | 10.0 | 14.0 | 2.0 | 75.4 | 78.5 |
| **PT-12-A** | 12.0 | 18.0 | 3.0 | 141.4 | 113.1 |
| **PT-22-A** | 22.0 | 30.0 | 4.0 | 276.5 | 380.1 |

Formulas: **t = (OD−ID)/2** · **A_flow = π·ID²/4** · **A_metal = π·(OD²−ID²)/4**

**ID** is authority — keyed to [MC-1-RC](measurement-code-1.md#mc-1-rc).

### Machine ownership

| Dimension | Machine | Clutch |
|---|---|---|
| **OD true** | **`LATHE-V2`** | **B · reduced ~58 rpm** |
| **ID true** | **`BORING-MILL-1`** | **D · reduced ~36 rpm** |
| **Length / facing** | Lathe | A or B per finish |
| **Stroke limit** | **~180 mm / setup** | Re-chuck or mandrel for longer |

### Fittings *(defined · second ops)*

| Fitting | Class | Method |
|---|---|---|
| **Elbow** | **PF-EL-*** | Forged sweep · mill bore through bend · lathe OD |
| **Tee** | **PF-TEE-*** | Thick-wall boss · mill cross-bore · lathe seat face |
| **Coupling** | **PF-CPL-*** | Lathe socket/counterbore · mill true bore · thread optional |

⚑ **PF-*** tables filed when first fitting hero names a size.

### Pressure — hoop stress (working)

**Thin-wall hoop:** **σ_hoop ≈ P·ID / (2t)** (gauge pressure, circular cylinder).

**Safe working P (provisional · WI):** use **σ_allow = 25 MPa class** for wrought iron until steel certs exist.

| ID | t (mm) | P_max WI (MPa) | P_max WI (bar) |
|---|---|---|---|
| **PT-06-A** | 2.0 | 0.75 | ~7.5 |
| **PT-10-A** | 2.0 | 0.50 | ~5.0 |
| **PT-12-A** | 3.0 | 0.75 | ~7.5 |
| **PT-22-A** | 4.0 | 0.69 | ~6.9 |

☠ **These are code placeholders for calculation — not proof-tested ratings.** Steel column **ST** will supersede WI when **`STEEL-*`** branch certifies yield.

**Steam / rifle / high P:** ☠ **Not WI table scope** — steel + hone + proof hero.

---

## MFGC-1-PIPE-TEST — test-before-production *(mandatory)*

No production pipe run until **all three** pass on **scrap or sacrificial blank**:

| # | Test | Pass |
|---|---|---|
| 1 | **Geometry** | ID plug **`RC-*`** GO · OD mic **`CALIPER-1`** · wall = (OD−ID)/2 within **±0.1 mm** |
| 2 | **Straightness** | Roll on **`BASALT-DATUM`** flat · light gap ≤ class |
| 3 | **Pressure** | Water column / blind cap to **50% of table P_max** · hold · no weep · no slip |

Log: **`PIPE-TEST-{ID}-{day}`** one line in day file · master not required for scrap.

⚑ **First production PT-*** hero names which **PT-** row is under test.

---

## MFGC-1-GEAR — power train *(reference)*

Torque reduction boxes **`LATHE-TORQUE-GB-1` · `MILL-TORQUE-GB-1`** — see journal **`TORQUE-GEARBOX-SLATE-Y12-1`**.

| Rule | Application |
|---|---|
| **Gears slow · belt fast** | Mortise + lantern · belt to spindle |
| **One clutch live** | **`BELT-TREE-1` A–D** |
| **Wood teeth** | Hornbeam · never oak on cog |

---

## MFGC-1-FUTURE — split candidates

| Topic | When to split |
|---|---|
| **Bevel gears · sheet roller** | First production table exceeds ~1 screen |
| **Musket / barrel** | **`STEEL-*` + rifling** — separate ordnance section or MFGC-2 |
| **Potentiometers · switches** | EC-1 component section or MFGC-3 |
