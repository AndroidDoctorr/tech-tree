# Scenario rules

*Canon for the speedrun journal. Source: [purpose.md](purpose.md) + player clarifications.*

## Immortality & respawn

| Rule | Detail |
|------|--------|
| **Aging / disease** | No effect |
| **Injury / death** | Possible |
| **Hunger** | Felt; **does not starve** if unfed |
| **Respawn** | Last **sleep site** (hut bed, etc.) |
| **Corpse** | **Disappears** on respawn |

### Closed loopholes

| Idea | Verdict |
|------|---------|
| **Cliff-farm corpses** for bone tools / hide | **No** — no corpse pile to harvest |
| *(more TBD)* | Player flags; DM closes when raised |

### Intentionally open loopholes
| Idea | Verdict |
|------|---------|
| **Literal dead drops** for long journeys | **Yes** — items on person left at location of death (with fall damage etc, if applicable) |
| **Immortal embryos** for cloning | **Yes** — a clone of me is immortal, too. Gestation might be VERY slow and VERY awkward, and the first few will wake up for the first time with a nonzero death count, but technically valid |

## Emergency multiplayer *(last resort only)*

If the solo speedrun hits a **hard wall** with no clever in-world workaround (tech-tree node that realistically needs more people), the player may invoke:

- **Other "players"** exist — each started in a **different location** worldwide
- Discovery by **stumble** (not spawn at camp); some may have **already met**
- Use **only** when stuck — not for convenience or speed

Film concept explores this by default: see [movie/](movie/).

## World

- **Era:** ~10,000 BC, Orontes valley (near future Antioch)
- **Humans:** None except player *(see Emergency multiplayer below)*
- **Assistant:** Handheld device — voice Q&A, no physical crafting · see **Assistant device** below

## Play style

- Day-by-day journal unless player requests skip/summary
- Realism challenged; solo-feasibility flagged in [tech-tree.md](tech-tree.md)

## Resource & skill gates *(assistant duty)*

Before the player **builds, crafts, smelts, hauls, or field-tests** something new, the assistant **must check** (and say so if blocked):

| Check | Source |
|-------|--------|
| **Materials & stock** | [inventory.md](inventory.md) — grep the row · [now.md](now.md) for runway |
| **Prerequisite tech / tools** | [tech-tree.md](tech-tree.md) · [inventory/tools-lab.md](inventory/tools-lab.md) when the named tool matters |
| **Skill tier** | [skills.md](skills.md) — task vs **Now** rank; no fumbling a tier-4 job without practice |
| **Prior build steps** | Day files + week plans — e.g. footings before posts, crane test before loft lift |

**If the gate fails:** do **not** log a clean **PASS** for that action. Instead:

1. **Block** or **defer** the action in the day file (`queued`, `NO-GO`, `PARTIAL`).
2. **Name the gap** — missing kg, missing tool, missing skill, wrong sequence.
3. **Offer honest next steps** — haul, pit char, practice craft, skill day, etc.

The player may **choose** a different priority; the assistant should **push back** when a plan skips prerequisites (same tone as farm neglect / ore-hold doctrine). Do not retroactively grant stock or skills to make a requested day work — fix forward on a later day unless the player explicitly asks to retcon.

### Build decomposition *(assistant duty)*

Compound builds (belt runs, roof batches, forge kits, vent systems) **decompose into parts**. Before logging a finished **PASS**:

| Step | Rule |
|------|------|
| **1 · Bill of materials** | List every **draw** — kg oak, m² hide, m rope, g wax, tool wear — from [inventory.md](inventory.md) |
| **2 · Subcomponents** | If a part is not in stock, it needs its **own fab day** or phase (pulley batch, rope twist, hide tan) — not a hand-wave |
| **3 · Doctrine choice** | When multiple materials work (e.g. **rope-primary vs hide-primary** belt), **audit**, pick, **file** — cite precedent day if any |
| **4 · Phase ledger** | Multi-day heroes get phases in [schedule.md](schedule.md) with **Est. days**, **cumulative %**, and **draw column** |
| **5 · Day file** | Log **−consumption** in **Craft** or **Events** (e.g. `HIDE-TRIM −0.04 m² pulley washers`) |

**Red flags — stop and fix forward:**

- Stock appears mid-day with no prior haul, hunt, or fab
- Single named blob ("tannery offcut", "workshop spare") with **no inventory line**
- Continuous material longer than physics allows from counted stock (e.g. **142 m hide strip** from **~2 m²** scrap)
- Tool/material draw exceeds ledger (e.g. **54 g Cu** from **~12 g** peas)

**If blocked:** queue the missing phase (**GOAT-HUNT**, **ROPE-TWIST**, **PULLEY-BATCH**) before the assembly day.

### Skills in daily play

| Rule | Detail |
|------|--------|
| **Ledger** | [skills.md](skills.md) — **Start (IRL)** + **Now** tiers; player is not a blank slate |
| **Day files** | When a hero craft, smelt, or field-test runs, log a **Skills** block (or row in **Craft**) naming the skill checked, **Now** tier, and **PASS / PARTIAL / NO-GO** |
| **Tier gate** | Task above **Now** without practice → **PARTIAL** or **fail** with rework cost — not silent PASS |
| **Updates** | Bump **Now** in skills.md when a day logs first reliable PASS at a **new tier** of task |

## Difficulty & realism *(Easy → Normal)*

Target feel: **cautious, industrious solo** with assistant reference — good progress and survival are plausible, but **not** frictionless. The player brings real skills ([skills.md](skills.md)); the valley still pushes back.

| Knob | Setting |
|------|---------|
| **Baseline** | Above stone-age average success — **not** “Easy Mode auto-win” |
| **Ceiling** | Not Hard/Brutal — no death-spiral RNG, no gratuitous catastrophe |
| **Mishaps** | Expect **~1 meaningful complication** per **5–10 hero-days** on maintenance tracks (forge, farm, roof, haul); **more** when attempting a **new tier** or **heavy multi-heat** forge job |
| **Failure shape** | Cost **time · material · rework · defer** — rarely total loss of a finished build |
| **Volatility** | **normal** — see [hazards.md — Volatility](hazards.md#volatility-live-knob) · player may set **low / normal / high** |

### Hazard rolls *(deterministic)*

Random events use **seeded rolls**, not assistant judgment. Full catalog: **[hazards.md](hazards.md)** · tool: **[sim/roll.py](sim/roll.py)**.

| Rule | Detail |
|------|--------|
| **Space** | Billion-scale (`0 … 999_999_999`) — supports **sub-percent** rates (e.g. earthquake **~1 in 500M**/day) |
| **Hit** | `roll < threshold × volatility × modifier` |
| **When** | Triggers in [hazards.md — Trigger matrix](hazards.md#trigger-matrix) — farm scare, day-open weather, haul, forge hero, etc. |
| **Log** | Day file **`HAZARD · d#### · ID · roll · thr · HIT/MISS`** — on HIT, patch hazard state + inventory |
| **Player** | **No aging · no disease** — injury and poison hazards only |
| **Animals** | Age, illness, breeding — roll on trigger; surface on farm pass, not when player asks |
| **Calendar gates** | Sow, harvest, fig band, etc. stay **non-negotiable** — hazards change **cost/margin**, not whether crops exist |

**Assistant duty:** On a trigger, **run** `sim/roll.py check` (or batch), compare to [hazards.md](hazards.md) threshold, log result. **Do not** silent PASS for catalog hazards.

### Wear, decay & condition

Track **condition** on tools and deployed structures when use or season warrants it. Update [inventory.md](inventory.md) and day files — do not assume gear is forever **✓** after first PASS.

| Category | Examples | Typical trigger |
|----------|----------|-----------------|
| **Tool wear** | Copper tongs jaw spring · chisel edge roll · haft loosen · bowstring stretch | Heavy forge batches · metal-on-metal · moisture cycles |
| **Rot & pests** | Lash slack · reed door fray · green timber check · hide stiffen | Wet season · unchecked margins · stacked green wood |
| **Structural creep** | Pitch drip · shake lift · fence sag · loft board spring | Freeze-thaw · load without maintenance · skipped inspection |
| **Consumable depletion** | Char lane thin · nail tray low · lime crust · rope UV | Hero smelt/forge without pit refill · liberal nail doctrine |
| **Mishap types** | Slag inclusion · bloom split · dropped workpiece · scald near-miss · cart wheel bind | Wrong tool for job · tired split day · worn PPE/tongs |

**Cautious play mitigates** (PPE, gate checks, split heroes, maintenance days) but **does not eliminate** wear. **Industrious play** earns faster recovery — not immunity.

**Assistant duty:** When the player proposes a heavy forge job (hinges, anvil block, long nail batch), **check tool condition** and **anvil class** — defer or **PARTIAL** if copper tongs, thin anvil face, or low skill tier would make “clean PASS” dishonest.

## Inventory ([inventory.md](inventory.md))

| Rule | Detail |
|------|--------|
| **Source of truth** | **[inventory.md](inventory.md)** for live counts · **[now.md](now.md)** for the runway · fixtures / bridges / tools under `inventory/` |
| **When to update** | End of any day that moves stock — patch the inventory row and `now.md` in the same pass. Do not append a chronicle line. |
| **Estimates** | Mark `~` if not weighed/counted that day; **re-count** on next factory day, clay haul, or smelt marathon |
| **map.md** | Geography and pile **roles**; **quantities** live in inventory.md (map links there) |
| **Day file** | Log burns/consumption in the journal (e.g. `Store C: −5.5 kg`) so audits trace forward |

### Fuel — cooking & heating *(player @ d3178)*

| Rule | Detail |
|------|--------|
| **Scope** | **Hearth/culina cooks**, **hypocaust/indirect heat**, **forge-adjacent warmth** — log draws on hero days forward |
| **Char** | **CHAR lane / retort char** — draw on smelt, forge, and **named cook/hearth sprints**; routine stew may use **−trace class** on quiet days |
| **Wood** | **Pile 5 / green splits** — camp fuel, scare-day pickup, journey haul top-up; **not** infinite background heat |
| **Climate** | **Antioch winter << Indiana** — baseline heating load **low**; excess char bank (~years of surplus) covers **retro ambiguity** — do not back-audit every stew |
| **Forward** | Any day with **forge · kiln · hearth hero · feast prep · hypocaust burn** patches **inventory char/wood row** or day-file consumption |
| **Ledger** | Hero burns in **day file Consumption**; runway in **inventory.md** char lane + pile 5 |

### Assistant device *(player @ d3178)*

| Rule | Detail |
|------|--------|
| **Power** | **Finite** charge — absurdly long-lived alien/Star-Trek-class cell, **not** infinite @ ~10 yr runtime |
| **Low charge** | At **≤20%** the assistant **must** surface **exact** recharge/interface instructions the player can build toward |
| **Charge port** | **Contactless through skin** — magnetic/field-coupled · **no case cut** · mates to player-built dock when tech allows |
| **Data port** | **Same coupler** — data + power · requires **precisely controlled electronics** (not yet on-tree except trivial audio) |
| **Speaker** | **First plausible interface** — passive/active speaker from known copper/wire grammar · **no** silicon fab required for v0 |
| **Full I/O** | **Voltaic + measured circuits + stable clocks** before assistant drives arbitrary campus machines |
| **Play** | Assistant does **not** craft physically · player builds dock/speaker · assistant provides **specs @ low charge** |

### Farm fence longevity *(player @ d3178)*

| Rule | Detail |
|------|--------|
| **Horizon** | Replace **wattle/scare-only** margins with **stone · brick · or concrete** — **maintenance-minimum** doctrine |
| **Priority** | **Bed B/D corridor · pen adjacency · scare streamer posts** before cosmetic campus |
| **Timing** | **Post–Y10 harvest** masonry band honest — not before spring sow window |

---

*Add rows under "Closed loopholes" when the player proposes an exploit.*
