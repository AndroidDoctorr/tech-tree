# BC-2 Annex A — clean / instrument wings

**Filed:** Day 4728 · **Cal-Y13 D109** · player directive before **Officina north work wing** (~5 × 6 m)
**Parent:** [building-code-2.md](building-code-2.md) · **procedure:** [construction.md](../procedures/construction.md)
**Electrical:** [electrical-code-1.md](electrical-code-1.md) **EC-1-GRID** · phase 4 **`EC-1-GRID-FEEDER-3`**
**Scope:** wings that hold **bench instruments, cells, optics, or low-dust craft** — not forge bays, not animal housing.

> ★ **This annex adds numbers and commissioning tiers BC-2 already implies.** It does not replace BC-2 seismic, DPC, or services doctrine. **Tier 1** below is enough for **one small wing (~≤40 m² floor, single storey, ≤3 m eaves)**. **Tier 2** (future large shells) reuses the same tables with **full batch breaks and mock-up load tests** — not required for the north work wing.

---

## BC-2A-FOOT — footing and subgrade

| Item | Tier 1 standard *(north wing)* | Notes |
|---|---|---|
| **Bearing proof** | **Reject topsoil, peat, loose fill.** Trench bottom: **thumb cannot push a clean probe deeper than ~25 mm in damp soil** without effort; if it can, **dig deeper or widen and recompact** | Poor-man penetrometer — log in day file |
| **Strip width** | **≥ 2.5 × structural wall thickness** · **≥ 500 mm** for 200 mm-class block/brick wythe | BC-2 said ~2–3×; this pins the floor |
| **Depth** | **≥ 400 mm below finished floor** · **≥ 200 mm below local frost heave class** *(campus: shallow, but not on topsoil)* | |
| **Subgrade prep** | **Scarify · dampen · compact in lifts ≤150 mm** with tamper or roller pass | Dry ground steals mix water — BC-2 |
| **Blind drain** | **Perimeter trench @ footing toe:** **≥ 100 mm coarse gravel**, **fall ≥ 1:80** to site drain or daylight · **never a closed basin** | Concrete is porous; water must have somewhere to go |
| **Footing pour segments** | **≤ ~2.5 m of wall length per session** or **≤ ~0.25 m³ mix** — whichever is less on a solo pour | Cold-joint grammar unchanged |
| **Capillary break** | **Continuous DPC** ([BC-2-DAMP](building-code-2.md#bc-2-damp--damp-proof-course)) **+ bitumen bed under socle** where `BITUMEN-ASI-1` is available | Hard gate before gypsum |
| **Season soak test** | **Optional defer** for Tier 1 if **spring pour test** ([BC-3](building-code-2.md#bc-3--site-and-layout)) **PASS** on the wing pad the same season | Full-year piezometer class → Tier 2 |

---

## BC-2A-ENV — envelope, cavity, glazing path

| Item | Tier 1 standard | Future *(not required this wing)* |
|---|---|---|
| **Structural vs finish** | **≥ 40 mm service cavity** between load-bearing wythe and gypsum line · chases and conduits live in the **cavity**, not in grouted cores | Full stud furring if cavity insufficient |
| **Vapour logic** | **Lime render outside · gypsum inside only** · **no gypsum below DPC** | |
| **Roof chamber** | **Ventilated void:** eave inlet + ridge outlet · **cross-section ≥ ~2 hand-spans** along the long axis | |
| **Glazing — single leaf** | **GP-Y8-class pane** in strap casement per BC-2 openings | Current north wing budget |
| **Glazing — paired leaf** | **Storm / inner leaf** on **second hinge set** or removable winter frame · **≥ 15 mm still air gap** · seal at sill/head with felt + pitch | **Not mandatory day one** — **route and jamb depth reserved** so inner leaf can be added without masonry surgery |
| **Floor moisture** | **Gravel + lime blind bed** · **cross-fall to drain** · **≥ 300 kg gravel** under plank during cure ([construction-mats.md](../../plans/construction-mats.md) §A) | Cork/hemp underlay optional Tier 2 |

---

## BC-2A-MOIST — moisture commissioning

| Gate | When | Pass |
|---|---|---|
| **DPC continuous** | Before any interior coat | Visual + probe at corners |
| **Roof on** | Before gypsum finish | No streaks on interior face after one rain |
| **Pad pour test** | Spring / before stake | Two buckets @ low point · clear **&lt; ~2 min** |
| **Interior RH read** | Before moving instruments in | **Hair hygrometer or salt-jar class** · log once · target **&lt; ~65 % RH** at **~20 °C** for bench work · if high, **delay gypsum** and run vent |
| **Wet trades** | Sink/slop in wing | **Tile or stone splash** · **no wood counter in splash zone** — BC-3 |

---

## BC-2A-SERV — utilities and grid *(with EC-1)*

BC-2 still says **route, not wire**. This annex names **what the north wing must leave.**

| Item | Standard |
|---|---|
| **Feeder** | **`EC-1-GRID-FEEDER-3`** from existing campus trunk · **`EC-1-TAP-BOX-STD`** @ east jamb · map entry before close-in |
| **Earth** | **Rod @ panel niche** · tail accessible · **bond to strap casement** where EC-1 requires |
| **Zones** *(conduit only)* | **Z-LIGHT** · **Z-BENCH** (cells, meters) · **Z-MOTOR** (exhaust fan ✓ d4860) — **separate clay tubes** · water sleeves **below** |
| **Draw-cord** | **Every empty tube** · tagged at box |
| **Load ledger** | One line per zone on [ec-1-campus-expansion.md](../../plans/ec-1-campus-expansion.md) when feeder lands — **amps are EC-1, routes are BC-2A** |
| **Combustion** | **No open hearth in Tier 1 clean wing** · **solder/alcohol outside or in fume path** · if a brazier is ever added, **BC-2 combustion-air** applies in full |

---

## BC-2A-STRUCT — roof and weight *(Tier 1 numbers)*

**Building:** ~**5 × 6 m** · single storey · **eaves ≤ ~3 m** · **TR roof** on triangulated oak.

| Check | Limit / rule |
|---|---|
| **Rafter span** | **≤ 3.0 m** clear on **≥ ~80 × ~120 mm** oak rafter class @ ~600 mm centres — **verify on a off-cut mock before cut list** |
| **Collar ties** | **≤ 1/3 span from plate** · **every rafter pair** on this span class |
| **Diaphragm** | **Continuous deck** before TR · **wind brace** at gable |
| **Dead load budget** | **Record on map:** TR + deck **≤ ~45 kg/m²** class target for this wing *(light frame first)* · **if stock tile exceeds budget, shake or lighter course on the diaphragm** — BC-2 light-finish rule |
| **Tie-down** | **Every heel to ring** · **strap + hooked bar** · log count in close |
| **Live load** | **Bench + two people + stores ≤ ~250 kg/m²** not required to prove by test on Tier 1 — **design for it in joist/plank choice** |

**Tier 2** *(garage-class, longer spans):* **sand-bag deflection mock** on a truss prototype · **rebar lap mock** already in BC-2 block QC.

---

## BC-2A-TEST — what to test on a small wing

| Test | Required Tier 1? | Method |
|---|---|---|
| **Block batch breaks** | **Yes** — 7 / 28 / 90 d from footing mix batch | BC-2 block QC |
| **Footing cube** | **Yes** — **×3 cubes** from first pour · crush at 28 d · **compare to prior campus pours** | Qualitative PASS/FAIL |
| **Rebar lap mock** | **Yes** if new lap detail | Existing **`REBAR-LAP-MOCK`** grammar |
| **Window leak** | **Yes** — hose or bucket pour on **installed casement** before interior gypsum | |
| **Roof truss load** | **Defer** on Tier 1 if span/table above satisfied | Tier 2 |
| **Full shear wall push** | **Defer** | Named experiment on mock frame only |

> ★ **Start assuming for shelters; stop assuming for instrument rooms.** Tier 1 is **one afternoon of mocks + the breaks you already cast** — not a materials lab.

---

## BC-2A-CLOSE — north wing checklist *(stake → weathertight)*

1. Footing trench · bearing proof · blind drain · segmented pour · DPC/bitumen
2. Stem block · grouted corners · **cavity set out**
3. Brick or block wythe · ring beam · **conduit + sleeves + cords**
4. Roof frame · deck · vent chamber · TR · tie-down count logged
5. Windows · leak test · optional inner-leaf hardware deferred
6. Oak floor on gravel bed · mudroom throat from hub
7. Scratch/float lime · gypsum finish only after roof + RH read
8. **`EC-1-GRID-FEEDER-3`** after jamb box set · map update

---

*Annex A filed d4728 · supplements BC-2 for clean/instrument wings only · does not amend seismic or retrofit tables.*
