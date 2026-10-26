# WW-2 crossflow turbine — design issue CY15

**Issued:** d5379 · **`WW-2-CROSSFLOW-SURVEY-5379`**  
**Parent:** [ww-2-power-upgrade.md](ww-2-power-upgrade.md) · [industrial-mech-drive-cy14.md](industrial-mech-drive-cy14.md)  
**Status:** **Design frozen for off-line fab** · civil install **summer nadir** · WW-2 **untouched** until cut-over

---

## Site datum *(winter read d5379)*

| Quantity | Read | Notes |
|---|---:|---|
| **Forebay surface → tailrace** | **7.14 m** | Confirms d5029 **~7.15 m** |
| **Forebay surface → WW-2 pad lip** | **7.06 m** | Staff + line level |
| **Open race Q @ gate NORMAL** | **~16.8 L/s** | Winter band · staff + timed bucket |
| **Open race water-surface drop @ wheel** | **~0.86 m** | Why undershot capture stays **~20% class** |
| **Tailrace datum** | **0.00** | South lip pin · all heads referenced here |

---

## Hydraulic route — **Route A** *(preferred · issued)*

Tap existing **`HYDRO-ELEC-1-RACE-FEED-1`** @ forebay south wing · **near-level contour** to new headbox · **short vertical chute** to tailrace — **not** a 180 m pressure penstock.

```text
FOREBAY (wing tap) ──138 m @ ~0.4% grade──► HEADBOX ──6.15 m chute──► TAILRACE
                      (~0.55 m fall)              (isolation gate + spill)
```

| Segment | Dimension | Material class |
|---|---|---|
| **Contour flume** | **138 m** run · **0.65 m** cut width · **0.28 m** normal depth | Dry block invert **×22** · oak cap boards **~18 kg** |
| **Headbox @ WW-2 north cheek** | **2.4 m** upstream of wheel axle CL | See below |
| **Terminal chute** | **6.15 m** vert · **ø380 mm** effective bore | Fired brick **×18** · oak guides |
| **Bypass** | Tie to **`SLUICE-2-RACEWAY-1`** spill board grammar | WW-2 wheel branch isolates for cut-over day |

### Head loss budget → runner

| Loss | m |
|---|---:|
| Screen / trash rack | **0.05** |
| Contour friction (138 m) | **0.12** |
| Headbox entry + turn | **0.04** |
| Nozzle velocity head | **0.08** |
| **Design H @ runner center** | **6.65 − 0.29 = 6.36 m** |
| **Nadir guard (@ 12 L/s)** | **≥ 6.20 m** |

---

## Headbox — **`WW-2-CROSSFLOW-HEADBOX-1`**

| | mm |
|---|---:|
| **Internal L × W × H** | **420 × 380 × 520** |
| **Nozzle sill → tailrace** | **6150** |
| **Spill crest → sill** | **+80** (flood pass) |
| **Isolation gate** | Iron pintle · **`SLUICE-2`** latch grammar |

**Frame:** oak **~14 kg** · iron strap **~2.2 kg** wrought · **`NAIL-IRON` ×12** class.

---

## Runner — **`WW-2-CROSSFLOW-RUNNER-1`** *(two-cell · off-line build)*

| Parameter | Value |
|---|---:|
| **Runner OD** | **274 mm** |
| **Axial width** | **228 mm** *(blade active **210 mm**)* |
| **Blades** | **×20** · backward curved **~22°** · chamber wrap **~180°** |
| **Shaft** | **ø32 mm** · bearing span **418 mm** CL–CL |
| **Bearings** | **×2** bronze shells **`BRONZE-BUSH-WW2-2`** · ID **32.2 mm** |
| **Design point** | **H ≈ 6.36 m** · **Q ≈ 18 L/s** · **~262 rpm** |
| **Hydraulic shaft power** | **~0.90–1.05 kW** class *(before reduction / gen)* |
| **Nadir point** | **Q ≈ 12 L/s** · cell-1 only · **~0.45 kW** class |

### Nozzle — two-cell

| Cell | Gap × width | When |
|---|---|---|
| **A** *(nadir)* | **24 mm × 105 mm** | Single cell |
| **B** *(boost)* | **+24 mm × 105 mm** | Linked for **≥ ~16 L/s** |

Slider iron **~1.1 kg** · oak ways **~2.4 kg**.

---

## Power train — bench-first

```text
RUNNER @ ~262 rpm ──25.7:1──► MECH SHAFT @ ~10.2 rpm ──clutch M──► BELT-TREE-1
                              │
                              └── clutch G ──► generator match (phase 5)
```

| Stage | Ratio | Notes |
|---|---:|---|
| **Primary belt** | **4.5 : 1** | Runner jackshaft |
| **Secondary chain** | **5.7 : 1** | To **`~10 rpm`** mechanical shaft |
| **`GS-2-FLYWHEEL-1`** | — | **Only** on reduced mechanical shaft · **never** on runner |

**Transition hardware planning mass:** **~4.8 kg** wrought/steel · **~0.55 kg** bronze *(clutches + jackshaft)* — **separate** from runner fab stock.

---

## Fab bill — off-line *(from `IRON-BLOOM-1`)*

| Component | Mass class | ID |
|---|---:|---|
| Shaft + keys | **~2.8 kg** | **`CROSSFLOW-SHAFT-1`** |
| End discs ×2 | **~3.2 kg** | **`CROSSFLOW-DISC-1/2`** |
| Blades ×20 | **~4.6 kg** | **`CROSSFLOW-BLADE-SET-1`** |
| Nozzle + gate hardware | **~1.4 kg** | **`CROSSFLOW-NOZZLE-2CELL-1`** |
| **Runner subtotal** | **~12.0 kg** | Leaves **~4 kg** bloom for fits / tooling |
| Jackshaft + clutches *(later)* | **~5.3 kg** | **`WW-2-TURBINE-TRANSITION-1`** |

**Bronze:** cast **×2** shells **~0.72 kg** finished — **assay + batch before shaft final grind**.

---

## Build order *(off-line)*

1. **`CROSSFLOW-LAYOUT-1`** @ WW yard — full-size blade template + shaft centers on slab. **✓ d5380**  
2. **`CROSSFLOW-SHAFT-1`** — forge + lathe journals · **leave +0.15 mm** for bronze fit. **✓ d5380**  
3. **`BRONZE-BUSH-WW2-2`** — cast · bore · scrape to shaft.  
4. **`CROSSFLOW-DISC-1/2`** + **`CROSSFLOW-BLADE-SET-1`** — batch blades · rivet to discs.  
5. **`CROSSFLOW-NOZZLE-2CELL-1`** — dry-fit to headbox mock (oak only).  
6. **`WW-2-CROSSFLOW-SPIN-1`** — belt from **`BLOCK-BENCH-LINE-SHAFT-1`** · no water.  
7. Civil **Route A** + headbox install — **summer nadir** hero arc.  
8. **`WW-2-CROSSFLOW-COMMISSION-1`** — water · mechanical mode · then **clutch G**.

**✓ Wet pilot d5475** *(partial feed · not step 7–8 complete):* wing tap + **~18 m** temp flume → **`CROSSFLOW-HEADBOX-MOCK-1`** @ north cheek · **cell A** · **Q ~13.4 L/s · H ~6.28 m · ~238 rpm · ~0.55 kW** class · **WW-2** still prime mover.

---

## Rejected on survey

| Option | Why |
|---|---|
| **180 m stave penstock** | Oak + hoop mass · not economical |
| **Wheel retrofit only** | Ceiling **~0.41 kW** — documented d5041 |
| **Runner on flywheel shaft** | Speed / energy grammar violation |
