# Officina north work wing — layout & services plan

**Filed:** d4808 · **Cal-Y13 D189** · ~5 × 6 m · [BC-2 Annex A](../government/regulations/building-code-2-annex-clean-wing.md)  
**Power:** [ec-1-campus-expansion.md](ec-1-campus-expansion.md) · **`EC-1-GRID-FEEDER-3`** **✓ LIVE d4809** *(branches ⚑)*  
**Map:** [officina.md](../map/campus/officina.md) § North work wing

---

## Design intent

**Clean bench / cells / optics class** — not forge air, not paint solvents. **Spills and acids are expected**; finishes must survive wipe-down and short neutralization. **Comfort = light + reachable stores + one motion per task**, not more floor area.

---

## Floor — tile, not oak *(player decision d4808)*

| Option | Verdict |
|---|---|
| **Oak plank** *(craft wing canon)* | ✗ **Wrong default here** — BC-2A-MOIST: **no wood counter in splash zone**; acid and electrolyte wick at joints and swell the board from underneath |
| **`TILE-TF` floor** *(flat kaolin · hub/turris grammar)* | ★ **Recommended** · sealed lime bed · **cross-fall to drain** · spills stay on the surface |
| **`TILE-TR` roof stock** | ✗ **Wrong SKU** — TR is **curved roof half-pipe**, not floor |

**Rough takeoff (~30 m² + ~12 % waste):**

| Surface | Tiles (30 cm class) | Notes |
|---|---|---|
| **Floor** | **~×115–125** | Turris used **×108** on **25 m²** — same pitch |
| **Bench splash ledge** *(optional)* | **~×12–18** | **600 mm deep strip** behind north bench only — not full countertop tile |
| **Work surfaces** | **See § Surfaces below** | Acid/electrolyte zones ≠ general writing bench |

**Stock @ d4818:** **×94 fired** + **×64 green** *(bands 2–3 drying)* · band **`4809` fired ×31** · **no more press** until greens fire + kaolin lap.

| Use | Tiles (30 cm class) |
|---|---|
| **Floor** ~30 m² + waste | **~×115–125** |
| **Short backsplash** *(1–2 rows @ north bench · ~5 m run)* | **~×17–34** |
| **Counters** | **Oak/stone top** — not in tile count |
| **All-in ceiling** | **~×132–159** |

**×159 pipeline** = **inside the high case** (125 + 34) · **~×0–27 spare** at low floor + one splash row — **not past budget if splash stays short**.

**Underlay:** gravel blind bed + lime sand per Annex A · **DPC already paid** · **floor-load GO d4819**.

---

## Drainage — two planes *(BC-2A + site)*

| Plane | Built | Job |
|---|---|---|
| **Subgrade** | **Blind drain @ footing toe** d4730–4732 · gravel **~1:60 → north cheek / daylight** | **Groundwater @ wall toe** — not the spill tray |
| **Finish floor** | **d4819** screed **~1:80 fall south** · **×38 tile** hub→south | **Wash & spills** need a **low point + outlet** |

★ **✓ `OFFICINA-N-FLOOR-DRAIN-1` LIVE d4823** — south low pocket · WI grate · green clay sleeve to blind drain *(fired pipe upgrade when R&D ready)*.

| Piece | Spec |
|---|---|
| **Low point** | **South center** · ~**300 mm** off south stem · lowest string on screed |
| **Sleeve** | **Clay tube through stem core** *(BC-2: sleeve now)* · **~1:40–1:80** fall to **blind drain** or **south apron daylight** |
| **Cover** | **Brass or WI grate** · removable · **RC-22** class or square pocket · flush with tile |
| **Tile** | **Leave ×4 opening** in next courses · **no closed basin** |

Precedent: **Turris `HUB-S-OIL-GRATE-1`** *(fall + grate, not a pipe maze)*. **Copper drain line not required** for this tier.

---

## Surfaces — acid, fire, “modern clean” *(player d4817)*

| Zone | Surface | Why |
|---|---|---|
| **North bench / cells** | **`TILE-TF` tray inset** or **stone/slate slab** · **drip edge to floor tile** · **no bare oak in splash radius** | Acid/electrolyte hits **glazed tile or stone**, not joints · wipe + neutralize on **floor tile** |
| **Centre table** | **Oak OK** · **no charging · no open acid** — meters/notebook only | Replaceable wood is fine **outside** the spill discipline |
| **Full tile counters** | **Optional** on north bench only · **not required on every bench** | Grout needs sealing/maintenance · **tile floor + tray/slab** covers most battery risk |
| **Fire** | **No open hearth · no brazier** *(BC-2A)* · **solder/ alcohol outside or future fume path** | Biggest fire win is **policy + separation**, not more tile |
| **Lead-acid / H₂** | **Charging only @ north bench** · **⚑ exhaust fan on `Z-MOTOR`** · **no flame in wing** | Annex gap until **fan commissioned** — treat as **must-have before heavy charging** |

**Adequate for electronics?** **Shell + gypsum + TF floor + feeder + earth + two lamps = right skeleton.** To be **campus-best clean/safe/bright**, still queue: **lamp branches LIVE** · **porcelain reflectors + brightest practical filaments** · **closed acid cabinet** · **spill kit** (neutralizer · rags · segregated waste) · **bench tray/slab** · **door curtain** · **optional slop sink** *(BC-3 tile splash — defer but plan sleeve)*.

---

## Room zones *(~5 m E–W × ~6 m N–S · hub door on north)*

```
        [ HUB N door ]
    W-window          E-window
         ┌──────────────────┐
         │  N bench (cells) │  ← Z-BENCH · tile tray · earth bond
         │  lamp #1 (ceiling)│
         ├────────┬─────────┤
         │ cabinet│  main   │  ← closed storage east cheek
         │  east  │  table  │  ← centre sightline W+E light
         │        │ lamp #2 │
         ├────────┴─────────┤
         │  mud throat S    │  ← coir + boot from hub ring
         └──────────────────┘
              (south toward hub ring path)
```

| Zone | Fixtures *(planned)* | Notes |
|---|---|---|
| **Entry / east jamb** | **`EC-1-TAP-BOX-STD-3`** · **`SW-WING-N-FEEDER-1`** · earth rod niche | **Whole wing OFF** for service |
| **North bench** | **`WORK-BENCH-N-1`** · cell tray · meter shelf · **tile inset tray** | **Z-BENCH** tubes land here · **no open flame** |
| **East cheek** | **`WING-N-CABINET-1`** closed · acid/glass upper | Same grammar as `CRAFT-CABINET-*` |
| **Centre / west** | **`WORK-TABLE-N-1`** ~900×600 class · scale + notebook | Copy `WORK-TABLE-ATELIER-1` height |
| **South** | **Boot mat + gravel drain strip** | Hub mud throat — **do not store fibre here** |

**Shelves:** **north bench rear** (heavy) · **east cabinet** (closed chems) · **west wall** under window (light tools) — **nothing over cell tray splash line**.

---

## Lighting — two fixtures

| ID | Mount | Branch | Bulb class |
|---|---|---|---|
| **`BULB-WING-N-LAMP-1`** | **North ceiling · porcelain wide reflector** | **`SW-WING-N-LIGHT-1`** · **LAMP-H** fuse | **Feast-class or brighter filament** · **not leave-on default** |
| **`BULB-WING-N-LAMP-2`** | **South/center · same reflector** | **`SW-WING-N-LIGHT-2`** · **LAMP-H** fuse | **Separate branch** — **one lamp per 0.5 mm run** |

★ **Porcelain / white enamel wide shade** — bounce light off gypsum without hot spot on bench. **Commission after feeder LIVE** · stub cords in **Z-LIGHT** tubes *(laid d4746)*.

---

## EC-1 — taps, wire, faults

**Doctrine:** [ec-1-campus-expansion.md](ec-1-campus-expansion.md) · **no GFCI product yet** — **fuse + knife + bonding + one load per branch**.

### Trunk *(in progress)*

| Item | Spec |
|---|---|
| **`EC-1-GRID-FEEDER-3`** | **Wheelhouse tee → campus path → north door east jamb** · **~48 m route surveyed d4808** · paired **0.9 mm bare** · oak cleats · **not buried** |
| **Entry** | **`SW-WING-N-FEEDER-1`** · default **OPEN** when wing idle |
| **Bus** | **`GRID-TAP-WING-N-1`** @ **`EC-1-TAP-BOX-STD-3`** |

### Branch ledger *(commission as built)*

| Branch | Switch | Fuse class | Max I *(named)* | Load |
|---|---|---|---|---|
| **LIGHT-N** | **`SW-WING-N-LIGHT-1`** | **LAMP-H** | **~1.15 I** | **`BULB-WING-N-LAMP-1`** |
| **LIGHT-S** | **`SW-WING-N-LIGHT-2`** | **LAMP-H** | **~1.15 I** | **`BULB-WING-N-LAMP-2`** |
| **BENCH** | **`SW-WING-N-BENCH-1`** | **BENCH** | **~0.35 I socket · lugs TBD** | **CP-G portable · cell clips · stirrer class** |
| **MOTOR** | **`SW-WING-N-MOTOR-1`** | **named @ fan** | **defer** | **Z-MOTOR tube · future exhaust** |

**Headroom:** sum simultaneous **GB·I ≤ ~70%** of gen peak at tap — **two LAMP-H + one BENCH** is the design ceiling on one trunk until **Q spring read** confirms E.

### Short / fault handling

| Event | Response |
|---|---|
| **Hard short at load** | **0.3 mm fuse tail opens** · fix branch · trunk may stay ON |
| **Overload / stall** | **Bus sags** · **do not stack motors** on one 0.5 mm branch |
| **Leak to frame** | **Earth rod + strap bond** · **human trips knife** · ⚑ differential bell R&D later |
| **Service** | **`SW-WING-N-FEEDER-1` OFF** → wing dark-safe · **`SW-STORAGE-TIE` OFF** only for bank work |

**Trunk ✓ d4809** — **~2.7 R · ~7.1 GB @ tap gen ON** · commission **light + BENCH branches** after parts exist *(see build order below)*.

### Wing lamps — build order *(one realistic hero per day · d4832 retcon)*

| # | Hero | Materials / precedent |
|---|---|---|
| 1 | **Queue + brass margin** | **✓ d4832** · **`BRASS-MARGIN-POUR`** → socket 3 stock |
| 2 | **`BULB-FEAST-SOCKET-Y14-3`** | **✓ d4835 · in `WING-N-LAMP-MOUNT-1`** |
| 3 | **`WING-N-PORC-REFLECTOR-1` green** | **✓ d4833 · fired d4843** |
| 4 | **Reflector 1 + 2 fire + glaze** | **✓ d4843 · `KILN-D` ×2 · white face** |
| 5 | **Reflector 1 mount** | **✓ d4844 · `WING-N-LAMP-MOUNT-1` + cleat 1** |
| 6 | **`WING-N-PORC-REFLECTOR-2` green** | **✓ d4834 · fired d4843** |
| 7 | **`BULB-FEAST-SOCKET-Y14-4`** | **✓ d4837 · in `WING-N-LAMP-MOUNT-2`** |
| 5b | **Reflector 2 mount** | **✓ d4844 · `WING-N-LAMP-MOUNT-2` + cleat 2** |
| 7b | **Wing filament refine + bulbs** | **✓ d4845–4846 · A/B sealed** |
| 8 | **`EC-1-GRID-BRANCH-WING-N-LIGHT-1`** | **✓ d4847 · `BULB-WING-N-LAMP-1` LIVE** |
| 9 | **`EC-1-GRID-BRANCH-WING-N-LIGHT-2`** | **✓ d4847 · `BULB-WING-N-LAMP-2` LIVE** |
| 10 | **Branch insulate** | **✓ d4847** |
| 11 | **Pendant mount + bulb** | **✓ d4847 hang + seat** |
| 12 | **Commission matrix** | **✓ d4847 T1–T5** |

---

## Build order *(after dry band)*

1. **Finish `FEEDER-3` trunk** · R read @ jamb · **commission bus**
2. **TF floor** on gravel bed · drain fall
3. **North bench + tile tray** · earth bond to rod — **✓ d4848 `WORK-BENCH-N-1` + BENCH branch**
4. **Cabinets + centre table** — **✓ d4850–4851 · `WING-N-CABINET-1` + `WORK-TABLE-N-1` · limewash queued**
5. **Lamp branches + reflector mounts**
6. **Move bench instruments** from chem porch overflow *(named days)*

---

*Layout filed d4808 · revise when furniture IDs commission.*
