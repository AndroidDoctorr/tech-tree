# `EC-1-WIND` — distributed farm windmills *(issued d5521)*

**Status:** **CONCEPT / DESIGN** · **no field unit commissioned**  
**Player intent:** Small **farm-class** wind machines (wood pole · wood blades · tail vane) — **not** Dutch tower mills · aesthetic reference **Great Lakes / northern Indiana aeromotor** scale, **much smaller** and **lower tech**. **One unit per building** (or per ridge line) for **passive** loads: **lights · trickle storage · small fans** · **heaters only after** resistance elements exist. **Hydro (`WW-2`)** stays primary for **machines · cells · process heat · garage class**. Optional **dual buses** with **isolated tie** for failover — **never** hot-parallel two gens.

**Links:** [ec-1-campus-expansion.md](ec-1-campus-expansion.md) · [electric-grid.md](../inventory/electric-grid.md) · [electrical-code-1.md](../government/regulations/electrical-code-1.md) · [gen-ac-1-cy15.md](gen-ac-1-cy15.md) · [ww-2-power-upgrade.md](ww-2-power-upgrade.md) · hazards **WEATHER-STORM-SEVERE** · **`WIND-SECURE`** ([triggers.md](../checklists/triggers.md))

---

## Why this is not a fantasy bypass

| Fact | Implication |
|---|---|
| Campus **hydro** is **~0.4–1 kW mechanical** class @ wheel · **~3 W electrical** today on **`GEN-WW-3-M`** | Wind does **not** replace the wheel for **forge · cells · lathe** — it **offloads** always-on **lighting** and **bank float** |
| **Lime / char** bottleneck is **thermal mass**, not **lamp watts** | Wind helps **quality of life + bench hours** · **`ELEC-PROCESS-HEAT-1`** still lands on **`GEN-AC-1` + hydro** |
| **Orontes valley** wind is **patchy**: summer **thermal / gap** breeze · **winter / front** blows · **calm nights** common | Design for **trickle + storage**, not **continuous machine duty** |
| EC-1 rule: **☠ parallel sources forbidden** without isolation | Architecture must be **one energizing source per bus segment** · **diode OR knife tie** |

> **Wind is a distributed battery charger for the quiet loads, not a second wheelhouse.**

---

## Machine class — **`WIND-1` farm aeromotor** *(target spec)*

| Parameter | Pilot class | Notes |
|---|---:|---|
| **Rotor** | **~2.0–2.8 m** diameter · **2–3** wooden blades | **Not** megawatt scale · **~1–3 m** hub height on **timber pole** or **short hinged tower** |
| **Blades** | Oak / ash · laminated blank · **pitch fixed** pilot · **varnish + balance** | **`CORD-LIFE-READ` grammar** on guy lines · **annual blade walk** |
| **Yaw** | **Tail vane** · slip-ring or **brush trolley** for DC | **Furling** or **tilt** required before storm season |
| **Speed** | **~60–120 rpm** rotor · **belt step-up** to gen | Reuse **`GEN-WW-1-BELT-TRAIN`** doctrine — **crowned pulleys · idler** |
| **Generator** | **Small shunt dynamo** or **PMG** @ **~400–800 rpm** | **Fraction of `GEN-WW-3-M` scale** · **separate** from wheelhouse machine |
| **Sustained electrical** *(honest)* | **~5–40 W** per unit in **good** campus breeze · **~0** in calm | **14 feast lamps** dim class **~10–15 W total** if all on — **one good turbine + bank** can **float domus** on a windy evening |
| **Peak gust** | **Mechanical overspeed** before **electrical** | **Governor · brake · furl** — see storm table |

**Name pattern:** **`WIND-1-{BUILDING}`** e.g. **`WIND-1-DOMUS`** · **`WIND-1-OFFICINA-N`**.

---

## Scale — pick height from rotor, not ego

**Target pilot:** **`WIND-1-DOMUS`** · **2.4 m** rotor · **hub ~4.5 m** above ground · **lowest blade tip ~3.3 m** (head-height safe on terrace edge with fence).

| Choice | Pilot | Why not bigger (yet) |
|---|---:|---|
| **Rotor diameter** | **2.4 m** | **Power ~∝ D²** but **gust load ~∝ D²** too — overspeed risk dominates before watts do |
| **Hub height** | **4.5 m** | **+1 m height ≈ +10–15% wind** in open fetch — **not worth** doubling structure load on first unit |
| **Blade count** | **3** | **2** is easier build · **3** runs smoother · pilot **3** if balance jig exists |
| **Mass budget** | **Rotor + tail < ~25 kg** | Wooden blades **absorb gust energy** — heavy rotor **stores** spin |

**Rule:** If you cannot **lay the whole head down in one person + donkey assist**, the pilot is too tall.

---

## Structure options *(wood-first)*

### Option 1 — **Hinged mast** *(recommended pilot)*

Single **oak mast** **~6–7 m** overall · **~0.18–0.22 m** butt · tapers to **~0.12 m** at head · **hinge @ ~0.6 m** on **oak shoe** in **stone pocket** · **gin pole** or **donkey pull** for raise/lay.

| Pro | Con |
|---|---|
| **`WIND-SECURE` = lay down** in **<1 h** | Mast sees **full bending** — needs **heartwood** + **guys when raised** |
| Blade service **at ground** | More **moving parts** at hinge · **pin + strap** must be **storm-rated** |

**Guys when raised:** **3×** hemp @ **~120°** · **anchor** = **buried log deadman** or **stone + lime grout** eye *(reuse BC-2 anchor grammar)*.

### Option 2 — **Fixed pole + guys only**

**Shorter mast ~5 m** · **4–5 guys** · **no hinge**. Storm = **furl + brake + optional blade sock** only.

| Pro | Con |
|---|---|
| **Simpler base** | **Cannot** lay down quickly · **trust furl** absolutely |

### Option 3 — **Trussed tower** *(second unit, not pilot)*

**4× corner posts** **~0.10 m** · **~1.2 m** square plan · **X-brace** oak + **peg** · **ladder bay** on lee side · **head beam** carries **yaw bearing**.

| Pro | Con |
|---|---|
| **Torsion stiff** · **climbable** · **guys optional** if **braced to ground** | **More timber + labour** · **still** need **lay-down** or **strong furl** for worst gusts |

**Hybrid (sensible campus grammar):** **trussed lower ~2.5 m** (stiff, anchored) + **single mast upper ~2 m** (carries head) + **2 guys** on upper mast only — **stiff base, lighter top**.

---

## Guys — hemp vs iron

| | **Hemp line** (`HEMP-LINE` / **`HEMP-THREAD` lash**) | **Wrought eye + hemp core** |
|---|---|---|
| **Campus fit** | **You have thread/line stock** · proven on carts, hive, lash | **Forge lugs** at mast + deadman |
| **Tension** | **Creep when wet** — **retension after rain** | Same if hemp carries load |
| **UV / rot** | **☠ Sun is the clock** — **tar/hemp dressing** @ **quarterly `CORD-LIFE-READ`** | **Bitumen band** on exposed runs |
| **Vibration** | **Good damping** — less **guy hum** than wire | — |
| **Defer** | **Bare copper guy wire** — **lightning + galling** · not era-appropriate anyway |

**Guy geometry (raised mast):**

- **3 guys** minimum · **~45–55°** from horizontal at mast head · **pretension** = **~15–25%** of design guy load *(tight enough to stop sway · not piano wire)*.
- **Turnbuckle substitute:** **lashing peg + toggle stick** — **documented length** each tune · no hidden iron screw era required.
- **Deadman:** **~1.2 m** buried oak **perpendicular** to guy · **≥~1 m** cover in firm soil · **lime grout cap** sheds water from eye.

**Stock hint (pilot):** **~80–120 m** **`HEMP-THREAD-Y16-1`** class in **3× ~25 m** legs + **lash** — **not** the whole **583 m** spool on one machine if other craft still draws it.

---

## Timber & hardware bill *(pilot `WIND-1-DOMUS` — order-of-magnitude)*

| Part | Material | Qty class | Notes |
|---|---|---:|---|
| **Mast** | **Oak heart** · **`WOOD-OAK-P5`** | **1× ~6.5 m** effective | **Avoid sapwood shell** @ hinge |
| **Shoe + hinge pin** | Oak + **wrought pin** | **1 set** | Pin **greased leather** washer |
| **Head block** | Oak **`WIND-1-HEAD-1`** | **1** | **Yaw bore** · **tail boom** · **gen shelf** |
| **Blades ×3** | Oak lam blank | **3× ~1.1 m** each | **Leading edge** optional **thin copper strip** *(later)* |
| **Tail vane** | **Ply oak + linen skin** | **~0.8 m²** area | **Furl offset** built into **hinge stop** |
| **Deadmen ×3** | Oak + stone | **3** | Or **1 deadman + 2 building anchors** if geometry allows |
| **Nacelle hood** | **Framed oak + hemp felt + bitumen cap** | **1** | **Sheds rain** · **ventilated** — gen heat + condensation |
| **Slow shaft + pulleys** | Oak + **bronze bush** class | **1 train** | Mirror **`GEN-WW-1-BELT-TRAIN`** scale **down** |
| **Preservation** | **Char foot** · **BITUMEN-ASI** band · **linseed/tar** on blades | **trace** | **Ground line** = rot plane |

**Not wood:** **bronze or iron** for **main shaft** through head · **leather belt** · **slip rings / brush trolley** *(copper)*.

---

## Weather & exposure *(Orontes campus)*

| Hazard | What it does | Build response |
|---|---|---|
| **Summer sun** | **UV + dry** — hemp stiff · blade check **open** | **Tar dressing** on guys · **varnish** blades · **re-tension** guys |
| **Winter rain** | **Hemp swells** · **mast cap leaks** → **rot @ head** | **Felt cap** · **drip groove** on nacelle · **drain hole** in shoe pocket |
| **Front storms** | **Gust > sustained** · **direction shift** | **Furl first** · **`WIND-SECURE` lay-down** if **storm row HIT** |
| **Dust (dry season)** | **Bearing wear** · **brush dust** | **Leather bellows** or **simple hood** on gen · **monthly wipe** |
| **Lightning** | **Tallest point on terrace** | **Pilot:** **lower than trees on ridge** if possible · **no copper guys** · **field switch open** in thunder *(procedure)* |
| **Calm weeks** | **Zero output** | **Expected** — **bank** carries lights · **no “broken” diagnosis** |

**Exposure class:** Treat as **outdoor maritime-light** — same mental model as **apiary roof** and **cleated aerial feeders**: **drain paths, no pockets, inspect after weather**.

---

## Construction sequence *(when you implement — not now)*

1. **Footing / shoe / deadmen** — **dry season** · **lime grout** eyes · **no mast until cure**
2. **Mast + hinge on ground** — **fit head bore** · **balance empty**
3. **Head + yaw + tail** — **bench test spin** · **furl stop**
4. **Blades** — **static balance** · **mark lead/lag** · **mount**
5. **Raise once without gen** — **guy tune** · **spin in breeze**
6. **Gen + belt + brake** — **dump load wired** · **field switch**
7. **Wire to `GRID-TAP-DOMUS-WIND-1`** — **fuse · knife · bank**

---

## Storm survival *(design gate — not optional)*

Farm machines die in **overspeed**, not in average wind.

| Layer | Mechanism | Procedure ID |
|---|---|---|
| **Furl** | Tail vane **offsets rotor** out of wind past **~12–15 m/s** equivalent | **`WIND-FURL-TEST`** after every service |
| **Brake** | **Wood shoe** or **strap** on **slow shaft** · **default ON** when climbing tower | **`WIND-BRAKE-ON`** before any blade work |
| **Tie-down** | **Hinged tower** → **lay down** · or **guy tension + blade sock** | **`WIND-SECURE`** on hard-wind forecast · [triggers.md](../checklists/triggers.md) |
| **Electrical** | **Field disconnect** · **dump load** on **local bank** or **resistor rack** | **`SW-WIND-FEEDER-*` OPEN** · **no open-circuit gen climb** |
| **Inspection** | After **every** **WEATHER-STORM-SEVERE** HIT or **felt** gust | **`WIND-POST-STORM-READ`** — bearing · guy · blade crack · tail hinge |

**Pilot rule:** **No unattended free-yaw** until **one full winter** of **`WIND-POST-STORM-READ`** logs **clean**.

---

## Grid architecture — recommended: **dual bus + isolated tie**

Three workable patterns; **B** matches player intent and EC-1 code.

### A — Single modular bus *(simplest on paper · hardest in ops)*

One **`EC-1-GRID-*`** · wind injects at **building taps** · **one** bank pool.  
**Risk:** **two sources** on one bus without **perfect** blocking → **motor drag / back-drive** · violates spirit of [ec-1-campus-expansion.md](ec-1-campus-expansion.md) parallel-source rule.

### B — **Dual bus + tie** *(recommended)*

| Bus | Source | Loads |
|---|---|---|
| **`EC-1-HYDRO-DC-*`** *(existing)* | **`GEN-WW-3-M`** → **`GEN-AC-1`** trunk later | **Motors · cells · bench · process heat · MS-1 machine floor** |
| **`EC-1-WIND-DC-*`** *(new)* | **`WIND-1-*`** per building · **local or ridge combiner** | **Room lamps · exhaust fans · trickle · future resistance heat** |

**Tie:** **`SW-BUS-TIE-1`** **knife** + **fuse** + **optional series diode** (gen-2 fab) · **default OPEN** · **manual failover only** — e.g. **hydro bank dead · wind bank carries domus lights** · **never** both closures closed without **procedure**.

### C — **Per-building island** *(most storm-safe · most copper)*

Each building: **`WIND-1` + `LEAD-ACID-BANK-Y*-WIND` + local lamp bus** · **no aerial trunk between buildings**.  
**Failover** = **carry lamp to charged building** or **temporary patch cord** — realistic early phase.

**Phasing:** start **C** at **`WIND-1-DOMUS` pilot** · evolve toward **B** when **`EC-1-WIND-TRUNK-1`** aerial is justified.

---

## Storage & “auto-shutoff” *(achievable now vs later)*

| Function | Near-term (DC era) | After `GEN-AC-1` / instruments |
|---|---|---|
| **Voltage stability** | **Lead-acid** **`BANK-*-WIND`** per building · **gen charges at fixed rpm band** | **Field buck · tap changer** on small machine |
| **Low-V disconnect** | **Hydrometer + manual** · **lamp dims → switch off** | **Voltmeter relay** · **`SW-WIND-LOW-V-1`** |
| **High-V / overspeed** | **Field knife OPEN** · **dump resistor** on **bank** | **Centrifugal governor** trips **field** |
| **Consistent lights** | **Bank float** · **dim carbon** already tolerant | Same · **do not** expect **wind-direct** lamps without buffer |

★ **“Auto-shutoff” = field off + fuse + tie open** before **smart grid**. That is still **realistic** and **documentable**.

---

## Siting on campus

| Site class | Pros | Cons |
|---|---|---|
| **Domus terrace / horreum ridge** | **Lights + people** · short wire | **Wake / turbulence** from buildings |
| **Officina north ridge** | **Clean fetch** · lab loads | **Longer** run to **`EC-1-WIND-TRUNK`** |
| **Fabrica hub tower** | **Already a post tree** | **Belt / machine noise** · **not** first pilot — **confusion with hydro feeders** |
| **Materiarum / MS-1 pad** *(later)* | **Future machine shop lights** | **Erect after** shell · **guy anchors** in **footing plan** |

**Pilot:** **`WIND-1-DOMUS`** — **one pole** · **guyed** · **hinge base** for **`WIND-SECURE`** lay-down · **≤~15 m** paired **0.5 mm** to **`GRID-TAP-DOMUS-WIND-1`** *(new)* · **separate** from **`GRID-TAP-DOMUS-1`** hydro margin until **`SW-BUS-TIE-1`** commissioned.

---

## Build order *(multi-season)*

| Phase | ID | Deliverable |
|---|---|---|
| **0** | **`WIND-1-DESIGN-1`** | Blade template · hub · tail · **furl geometry** on paper · **storm lay-down** method |
| **1** | **`WIND-1-DOMUS-PILOT`** | **One** machine · **one** **`BANK-*-WIND`** · **3–5** lamps max on **wind bus only** · **wind logbook** (daily **rpm / breeze / charge A**) |
| **2** | **`WIND-1-OFFICINA` · `WIND-1-FABRICA-MARGIN`** | Copy **proven** hub · **ridge combiner** optional · **still no tie to hydro** |
| **3** | **`EC-1-WIND-TRUNK-1`** | Aerial **wind bus** building-to-building · **`SW-WIND-FEEDER-*`** @ each jamb |
| **4** | **`SW-BUS-TIE-1`** | **Failover procedure** filed · **drill** · **diode** if fab allows |
| **5** | **Resistance heat** | **Only after** **`ELEC-PROCESS-HEAT-1`** element + **wind bank** sized for **duty cycle** |

**Explicit defer:** **AC wind** · **grid-tied induction** · **synchronous campus** — **`GEN-AC-1`** is **hydro-first**; wind stays **DC** until a **small rectifier** or **unified AC sub-panel** is a **named R&D** row.

---

## Dependencies & collisions

| Gate | Blocks |
|---|---|
| **`GEN-AC-1` fab** | **Does not block** wind pilot — **different shop queue** |
| **Copper draw** | Wind **branches** compete with **`GEN-AC-1`** wire — **budget ~20–40 m 0.5 mm** per building |
| **`WW-2` outage windows** | **Good** wind-pilot time — **lights on wind bank** while race dry |
| **MS-1 footing** | **Anchor sleeves** for **future guy** if pole sits on pad edge — **plan now · pour later** |

---

## R&D questions *(kitchen slate)*

- [ ] **Pilot structure:** **hinged mast** vs **fixed + furl-only** — **lay-down time** vs **timber count**
- [ ] **Guys:** **3× hemp** vs **hybrid truss + 2 guys**
- [ ] **Furl vs hinged tower** — which is faster on **`WIND-SECURE`** days?
- [ ] **PMG** ( **`MAG-BOOT-EM`** + small core) vs **shunt dynamo** — **maintenance vs cut-in speed**
- [ ] **One bank per building** vs **central wind bank** on **`EC-1-WIND-TRUNK`**
- [ ] **Diode tie** — **Cu + selenium / thermionic** path or **manual-only** for years?
- [ ] **Blade count** — **2** (simple) vs **3** (smoother · harder balance)

---

## Relation to player goals

| Goal | Wind role |
|---|---|
| **Less “always haul wood for light”** | **Partial** — **lamps on bank** · **hydro wood** unchanged for **kiln** |
| **Campus “normal grid” feel** | **Yes** — **building feeder + bank + switch** grammar matches **EC-1** |
| **Realistic** | **Low watts · storm discipline · no parallel gens** |
| **Combine with hydro** | **Dual bus + open tie** · **hydro = muscle · wind = housekeeping electrons** |

*Revise when **`WIND-1-DOMUS-PILOT`** breaks ground · patch [electric-grid.md](../inventory/electric-grid.md) on first commission.*
