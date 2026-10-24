# EC-1 campus expansion — load plan

**Filed:** d4560 · **Cal-Y14 D320 · ~3 Nov Y14**  
**Authority:** [electrical-code-1.md](../government/regulations/electrical-code-1.md) (EC-1) · live map in [infrastructure.md](../inventory/infrastructure.md)

**Intent:** Every campus load has a **named tap**, a **max draw on paper**, and a **fuse + knife** before the machine sees the bus — so shorts stay local, wheel sag is predictable, and blackouts are **storage-backed ride-through**, not surprises.

---

## What exists today

| Layer | ID | Role |
|---|---|---|
| **Source** | **`GEN-WW-2`** @ wheelhouse | Primary · **~9.0 GB oc · ~2.25 GB·I peak** @ forebay feed (d4555) |
| **Storage** | **`LEAD-ACID-BANK-Y13-1/2`** + **`SW-STORAGE-TIE-1/2`** | Overnight · bench peaks · **gen OFF → bus sags to bank** |
| **Trunk A** | **`EC-1-GRID-FEEDER-1`** | Chem porch · **`GRID-TAP-CHEM-1`** · **`SW-CHEM-FEEDER-1`** |
| **Trunk B** | **`EC-1-GRID-FEEDER-2`** | Craft wing · **`GRID-TAP-CRAFT-1`** · **`SW-CRAFT-FEEDER-1`** |
| **Branch** | **`EC-1-GRID-BRANCH-DESK-1`** | Desk lamp · **`SW-FEAST-LAMP-1`** · **~1.1 A dim class** |
| **Reference** | **`DANIELL-CELL-1`** · meters | **Not bus loads** — measure / flash only |

★ **There is no “outlet stock” yet** — each tap is **built to order** (fuse tail + knife + labelled max I).

---

## Building feeders *(canonical — count buildings, not cleat runs)*

★ **One named building → one building-entry feeder** (knife @ jamb + **`GRID-TAP-*` bus**). Extra trunks to the **same** building are **phase debt**, not a third “building wired.”

| Building | Map | Building feeder | State |
|---|---|---|---|
| **Officina** *(Turris + craft + storage + north work wing)* | [officina.md](../map/campus/officina.md) | **`EC-1-GRID-FEEDER-2`** · **`SW-CRAFT-FEEDER-1` only** | **✓ LIVE d4987** · north tap **bus-tied** · **`FEEDER-3` trunk retired** |
| **Fabrica** *(WW-YARD plus · hub · forge court)* | [fabrica.md](../map/campus/fabrica.md) | **`FEEDER-1` chem + `FEEDER-FABRICA-1` hub** | **✓ building buses LIVE d4987** · branches ⚑ |
| **Domus** | Residential terrace | **Margin branch on `FEEDER-2`** only | **⚑** dedicated feeder or formal tap-in when M2 chase exists |
| **Horreum** | @ Domus | **None** | Defer |

### Fabrica vs chem porch *(do not double-count)*

| Trunk | What it actually serves | Building? |
|---|---|---|
| **`EC-1-GRID-FEEDER-1`** | **Chem east leg / porch entry** · **`GRID-TAP-CHEM-1`** · **`MOTOR-1` · cells** | **East wing of Fabrica compound** — chemistry **is** powered today |
| **`EC-1-GRID-FEEDER-FABRICA-1`** | **`WW-HUB-TOWER-1` south entry** · **hub + south court + west millhouse class** | **Compound bus** — belt assist · forge fan · lights · future **`STORE-4`** margin |

> **Target:** **Chem stays on Feeder-1** until a consolidation hero ties **`GRID-TAP-CHEM-1`** to **`GRID-TAP-FABRICA-1`** through the hub *(one switch per leg, not two wheelhouse trunks forever)*. **Next install:** land **Fabrica-1** @ hub · commission **industrial branches** · add **chem lab room lights / bench taps** on existing chem bus.

### Officina — one feeder *(done d4987)*

**✓ `OFFICINA-FEEDER-CONSOLIDATE-4987`** — **`GRID-TAP-CRAFT-1` → `GRID-TAP-WING-N-1`** bus tie **~7.2 m 0.5 mm** · **`SW-CRAFT-FEEDER-1` sole entry** · **`FEEDER-3` trunk stripped → Fabrica-1**. Lab + north motor branches unchanged on north tap; **phase-1 storage lamps** · **`STORAGE-WING-1`** + **`STORE-4`** · **×1 each** · roster [electric-grid.md](../inventory/electric-grid.md).

**Campus score @ d4987:** **3/3 building buses LIVE** — **Officina** single feeder · **Fabrica** chem + hub entries · **Domus** margin on Officina trunk. **Room fixtures** still ⚑ per Phase 2.

---

## Standard parts *(every new circuit)*

| Part | Spec | Job |
|---|---|---|
| **Trunk** | **0.9 mm** paired · cleated aerial · wax+rosin wrap | Wheelhouse → building entry |
| **Entry switch** | **`SW-*-FEEDER-*`** knife @ jamb | **Whole building off** for service |
| **Tap bus** | **`GRID-TAP-*`** brass posts · polarity tags | Split to branches |
| **Branch** | **0.5 mm** paired · **≤~3 m** to load class | Motor · lamp · loom assist |
| **Fuse tail** | **~0.3 mm × ~8 cm** @ tap or branch | **Sacrificial short** — blows before trunk cooks |
| **Load switch** | Knife @ fixture | **One load · default OPEN** when idle |
| **Ledger row** | **Name · max I · max GB·I · day commissioned** | Audit before adding the next tap |

**QC:** branch R from [EC-1-GAUGE](../government/regulations/electrical-code-1.md) table · **±5%** vs sample set.

---

## Protection doctrine *(surge · short · blackout)*

| Event | Campus response | Build rule |
|---|---|---|
| **Short at load** | **Fuse tail opens** · trunk switch may stay ON · repair branch only | **Never skip fuse tail** on a new circuit |
| **Overload / motor stall** | **Gen line sags** · belt may slip before wire smokes | **Name max I** · no second motor on one 0.5 mm branch |
| **Gen stops (water off)** | **Banks float bus** · **~1.5 GB class** at distant taps | **Heavy loads gen-only** · lights OK on bank minutes |
| **“Surge”** | ★ **No MOV era** — mitigation = **fuse + switch + one load per branch + storage** | **Do not hot-switch motors** |
| **Parallel sources** | ☠ **Forbidden** without isolation knife | One of: gen · bank · Daniell — not two gens |

**Blackout grammar:** **`SW-*-FEEDER` OFF** = building dark safe · **`SW-STORAGE-TIE` OFF** = bank isolated for service.

---

## Load ledger *(living — append on commission)*

| Load | Tap | Max I (named) | Max GB·I | Notes |
|---|---|---|---|---|
| **`MOTOR-1`** | **`GRID-TAP-CHEM-1`** | **~0.4 A class** | **~0.9** | Bench motor |
| **`CU-CELL` bank** | Chem parallel bus | **cell chemistry** | — | Not a “room” load |
| **`BULB-FEAST-LAMP-Y14-1`** | **`GRID-TAP-CRAFT-1` → desk** | **~1.1 A dim** | **~0.7** | Leave-on Yule |
| **`EC-1-TAP-BOX-STD-2`** | **`GRID-TAP-CRAFT-2`** south bay | **~0.35 I socket** | **~0.9** | LAMP-H / BENCH |
| **`EC-1-TAP-BOX-STD-1`** | **`GRID-TAP-DOMUS-1`** porticus | **~0.35 I socket** | **~0.25 dim** | **✓ `BULB-CULINA-LAMP-Y14-1` d4571** |
| **Loom / craft assist** | **`GRID-TAP-CRAFT-2`** lugs | **TBD @ commission** | — | Queued |
| **North wing bus** | **`GRID-TAP-WING-N-1`** @ **`EC-1-TAP-BOX-STD-3`** | **trunk LIVE d4809** | **~7.1 GB @ gen ON** | **⚑ branch commission** |
| **Garage shop** | **`GRID-TAP-GARAGE-1`** *(planned)* | **TBD** | **⚠ second trunk or 1.2 mm class** | See phase 4 |

**Headroom rule:** ★ **Sum of simultaneous max GB·I on one trunk ≤ ~70% of gen peak at that tap’s measured E** — rest is sag margin.

---

## Order of operations

### Phase 0 — **Now (paper + reads)** ✓ d4560

1. **Q @ race** on autumn nadir · file next to d4555.
2. **This plan** + ledger template.
3. **Wheelhouse slate:** trunk map · which switch kills what.

### Phase 1 — **Standardize taps (winter bites, no new buildings)**

1. ✓ **`EC-1-TAP-BOX-STD-1`** + **`EC-1-TAP-BOX-JIG-Y14-1`** — reference @ **`REF-SHELF-CRAFT-1`** · **d4561**.
2. ✓ **`FUSE-LINK-Y14-1` ×12** @ chem peg pouch — **d4561**.
3. ✓ **Audit Feeder-1 / Feeder-2** — **d4565** · R **~2.35 / ~4.05** · domus margin cheek **PASS** · no re-wrap.
4. ✓ **`GRID-TAP-CRAFT-2`** @ south bay + **`EC-1-TAP-BOX-STD-2`** — **d4563** · ✓ **`GRID-TAP-DOMUS-1`** margin branch + **`EC-1-TAP-BOX-STD-1`** — **d4563** *(lighting only)*.

### Phase 2 — **Room lights (after tap std)**

1. **Socket std** = **`BULB-FEAST-SOCKET-Y14-1` geometry** · branch + **`SW-*`** each room.
2. **One branch per room** · dim carbon · **no room shares a 0.5 mm run with a motor**.
3. Order: **craft wing remainder** → **M2/domus when chase proven** → horreum margin last (dry only).

### Phase 2b — **`EC-1-GRID-FEEDER-FABRICA-1`** *(industrial compound · d4986+)*

1. **Route** wheelhouse post tree → **`WW-HUB-TOWER-1` south apron** · **~18 m paired class** · cleated · **not buried**.
2. **`SW-FABRICA-FEEDER-1`** @ hub · **`EC-1-TAP-BOX-STD-4`** *(or reuse std-2 jig)* · **`GRID-TAP-FABRICA-1`**.
3. **Branches (named before energize):** south-court **LAMP** · **`FORGE-D` fan assist** class · **`MILLHOUSE-2` bench** · **`STORE-4` dry margin** last.
4. ✓ **Chem lab:** **×2 room lamps · `SW-CHEM-LAB-LAMP-1`** on **`GRID-TAP-CHEM-1`** — **d5013–5019** · commission / reflectors defer.
5. **Wire budget:** **~36–40 m paired 0.9 mm** trunk + wrap — **restore `WIRE-CU-GEN2-1` comfort** before energize *(lab plan)*.

### Phase 3 — **North work wing civil + power**

1. **BC-2 shell** to jamb · **chase stub** in wall *(BC-2-SERVICES)*.
2. **`EC-1-GRID-FEEDER-3`** *(name TBD)* — **new trunk** wheelhouse → north jamb · **0.9 mm** · **separate entry switch**.
3. **`GRID-TAP-WING-N-1`** + **machine branches** sized from **named motor list** (lathe · mill · forge fan class).
4. ★ **Do not hang machines on Feeder-2** — craft tap is already lamp + assist class.

### Phase 4 — **`WAGON-GARAGE-2` / heavy shop**

1. **Civil + roof** before wire.
2. **`EC-1-GRID-FEEDER-4`** or **tap from Phase 3 bus at garage** if co-located — **heavier gauge or shorter run** (measure R first).
3. **Machine ledger** — crane · compressor class · **each gets fuse + switch + max I**.

### Phase 5 — **Campus-wide (long horizon)**

1. **AC / step-up** — [wishlist.md](wishlist.md) · **after** trunks exist · not before.
2. **“Outlet pool”** — mass-produced **`TAP-BOX`** + **`SW-KNIFE`** stock · **×0 today**.

---

## Dependencies *(hard gates)*

| Before | After |
|---|---|
| **Tap box standard** | More than **two** branches on one building |
| **Building jamb + chase** | **Feeder-3** install |
| **Feeder-3 LIVE** | North wing **motor** loads |
| **Garage slab / posts** | **Feeder-4** |
| **Harvest block closed** | Hero days for trunk pulls (optional overlap with stock haul only) |

---

## Next engineering reads

- **Spring `WW-2-Q` series** — resize gen expectation before Feeder-3 copper budget.
- **Forebay deeper hold** — more **E** at wheel · does not replace **wider wire** for garage.

*Revise ledger when a circuit commissions · patch [infrastructure.md](../inventory/infrastructure.md) once per install.*

---

## Fuses — yes, and you already make them

| Class | What it is | Campus status |
|---|---|---|
| **Link fuse** | **0.3 mm × ~8 cm** wire tail | **Live grammar** @ taps · **Phase 1 stock bag** |
| **Cartridge fuse** | Brass tube + link + screw cap | **R&D** — same link inside **`FUSE-CART-Y14-*`** |
| **Plug fuse** | Link in **movable plug** body | **✓ `CP-G-PLUG-PROTOTYPE-Y14-1` d4564** · protects **cord + device** |

★ **Fuse rating is I (amps), not “13 A @ 230 V”.** Name **max I** and **which E band** the branch sees.

---

## GFCI / earth-leakage — not yet as a product

A **GFCI** needs **fast differential current sense** (+ vs − imbalance) and a **trip** — modern ones use a toroid + electronics. You can **approach** the problem in layers:

| Layer | What you can do now | GFCI equivalent |
|---|---|---|
| **Architecture** | **Frame − strap** · **no water-pipe return** · **one load per branch** | Prevents whole-campus faults |
| **Tap box** | **Fuse + knife** · **polarity tags** | Stops **hard shorts** · not **leak to frame** |
| **Bench R&D** | **Differential shunt + galvanometer** — “leakage bell” | **Detect** · human trips switch |
| **Product** | **Solenoid knife drop** on imbalance | **⚑ Phase 5+** · needs reliable **mA-class** sense |

☠ **Do not wait for GFCI to run lights** — use **bonding + fuses + switches** first.

---

## Voltage / current — invent **bus bands**, not 230 V

**Do not adopt 120/230 V RMS** — your source is a **load line** (**~9 GB oc**, sag under I). Domestic UK ratings assume **fixed E** and **ring mains**; your campus is **one generator + storage** with **real drop**.

### EC-1 bus bands *(nominal · measure at tap)*

| Band | E @ tap (gen ON) | Use |
|---|---|---|
| **GEN-HIGH** | **~6.5–9 GB** | Trunk alive · motors · cells · bright bench |
| **GEN-MID** | **~4–6.5 GB** | Normal loaded bus · **lamp dim** · **`BULB-FEAST`** class |
| **BANK-LOW** | **~1.2–2 GB** | Gen OFF · lights · logic · **not** **`MOTOR-1`** start |

**Current:** stay in **I** on the ledger. **Branch classes** (first pass):

| Class | Max I | Max GB·I @ GEN-MID | Typical load |
|---|---|---|---|
| **LAMP-L** | **≤0.3 I** | **~0.2** | Dim carbon · night bank |
| **LAMP-H** | **≤1.2 I** | **~0.8** | Feast lamp · prestige |
| **BENCH** | **≤0.5 I** | **~1.0** | Stirrer · small motor |
| **MACHINE** | **named** | **≤2.0** | **Own branch** · often **direct lugs** — **no plug** |

★ **Industrial default:** **`GRID-TAP` + knife + lugs** — plugs only where humans unplug things.

---

## Campus plug **CP-G** *(Type G–inspired · EC-1 native)*

Borrow **BS 1363 ideas**, not the **230 V / 13 A** numbers:

| UK idea | CP-G campus rule |
|---|---|
| **Earth pin longest** | **− frame strap engages first** · shutters open |
| **Fuse in plug** | **Link fuse in plug body** · sized to **cord + device max I** |
| **Shutters** | **Brass slider** until earth pin enters — **no live access** |
| **Polarized + / −** | **Keyed flat pins** · **cannot reverse** |
| **Bulky plug** | **Acceptable** — you are not fighting IKEA aesthetics |

**Not copied:** rectangular UK footprint · **ring mains** · **13 A on 230 V** · **AC**.

**Domus / craft:** **CP-G socket** on **0.5 mm branch** · **LAMP-H or BENCH** fuse class.  
**Shop / garage:** **CP-G optional** on portable lamps only · **mills · motors · cells = bolted tap box**.

**Tap box std (Phase 1)** = wall **shuttered CP-G socket(s)** + **branch fuse** + **ledger label** · optional **second set of lugs** for fixed machines.

---

## Reinventing the wheel *(on purpose)*

| If you imported… | Why it fights your grid |
|---|---|
| **NEMA 120 V** | Fixed E · wrong shape of **`GEN-WW-2` line** |
| **EU Schuko** | No mandatory fuse in plug · weak shutter story |
| **UK 13 A ring** | **Ring topology** assumes utility-scale AC |

**Your standard:** **GB · I · R · GB·I** + **CP-G** safety mechanics + **three tiers** — **link fuse · tap box · lug bus**.
