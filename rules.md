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
- **Assistant:** Handheld device — voice Q&A, no physical crafting

## Play style

- Day-by-day journal unless player requests skip/summary
- Realism challenged; solo-feasibility flagged in [tech-tree.md](tech-tree.md)

## Resource & skill gates *(assistant duty)*

Before the player **builds, crafts, smelts, hauls, or field-tests** something new, the assistant **must check** (and say so if blocked):

| Check | Source |
|-------|--------|
| **Materials & stock** | [inventory.md](inventory.md) — location, quantity, `~` estimates |
| **Prerequisite tech / tools** | [tech-tree.md](tech-tree.md), [advancements.md](advancements.md), [ladder.md](ladder.md) |
| **Skill tier** | [skills.md](skills.md) — task vs **Now** rank; no fumbling a tier-4 job without practice |
| **Prior build steps** | Day files + week plans — e.g. footings before posts, crane test before loft lift |

**If the gate fails:** do **not** log a clean **PASS** for that action. Instead:

1. **Block** or **defer** the action in the day file (`queued`, `NO-GO`, `PARTIAL`).
2. **Name the gap** — missing kg, missing tool, missing skill, wrong sequence.
3. **Offer honest next steps** — haul, pit char, practice craft, skill day, etc.

The player may **choose** a different priority; the assistant should **push back** when a plan skips prerequisites (same tone as farm neglect / ore-hold doctrine). Do not retroactively grant stock or skills to make a requested day work — fix forward on a later day unless the player explicitly asks to retcon.

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
| **Source of truth** | **[inventory.md](inventory.md)** — grouped by **location** (H-v2, hut v1, camp piles, W-1, farm, WW pad, on body), not just worn gear |
| **When to update** | End of **any day** that moves **charcoal, fired/green bricks, clay, ore, grain, lime**, or adds a **stored tool/pot** — update inventory in the same pass as the day file |
| **Estimates** | Mark `~` if not weighed/counted that day; **re-count** on next factory day, clay haul, or smelt marathon |
| **map.md** | Geography and pile **roles**; **quantities** live in inventory.md (map links there) |
| **Day file** | Log burns/consumption in the journal (e.g. `Store C: −5.5 kg`) so audits trace forward |

---

*Add rows under "Closed loopholes" when the player proposes an exploit.*
