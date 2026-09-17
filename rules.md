# Scenario rules

**Canon.** Not a daily read — come here when a trigger in [instructions.md](instructions.md) sends you.

## Immortality and respawn

| Rule | Detail |
|---|---|
| **Aging · disease** | No effect. ☠ **Never roll either** |
| **Injury · death** | Both possible |
| **Hunger** | Felt, and it hurts — **but the Player does not starve** |
| **Respawn** | At the **last sleep site** |
| **Corpse** | **Disappears** on respawn |

### Closed loopholes

| Idea | Verdict |
|---|---|
| **Cliff-farm corpses** for bone and hide | ✗ **No** — nothing is left to harvest |

*Add a row when the Player proposes an exploit and it gets closed.*

### Open loopholes — deliberately allowed

| Idea | Verdict |
|---|---|
| **Dead drops** on long journeys | ✓ Items carried are left where the Player died, with fall damage if it applies |
| **Immortal embryos** for cloning | ✓ A clone is immortal too. Gestation may be very slow and very awkward, and the first few wake up with a nonzero death count — **technically valid** |

## World

- **Era:** ~10,000 BCE, Orontes valley near the future Antioch
- **Humans:** none but the Player
- **Assistant:** a handheld device — voice Q&A, no physical crafting

### Other humans

Other "players" exist, each started somewhere else in the world, and some may already have met. Discovery happens by **stumbling into them**, never by spawning at camp.

☠ **Last resort only.** Invoke this if and only if the solo run hits a hard wall with no in-world workaround — never for convenience or speed, and never before the wall has been named and explained per the standing duty in [instructions.md](instructions.md#-standing-duty--find-the-wall).

## Gates

**Before the Player builds, crafts, smelts, hauls or field-tests something new:**

| Check | Source |
|---|---|
| **Materials and stock** | [inventory](inventory/index.md) — grep the row · [now.md](now.md) for runway |
| **Prerequisite tech and tools** | [tools.md](inventory/tools.md) · [infrastructure.md](inventory/infrastructure.md) |
| **Skill tier** | [skills.md](skills.md) — task versus **Now** rank |
| **Prior build steps** | Day files — footings before posts, crane test before loft lift |

**If a gate fails:**

1. **Block or defer** in the day file — `queued`, `NO-GO`, `PARTIAL`
2. **Name the gap** — missing kg, missing tool, missing tier, wrong sequence
3. **Offer the honest next step** — haul, char burn, practice craft, skill day

☠ **Do not retroactively grant stock or skill to make a requested day work.** Fix forward on a later day, unless the User explicitly asks for a retcon.

## Build decomposition

Compound builds — belt runs, roof batches, forge kits, vent systems — **decompose into parts.** Before logging a finished PASS:

| Step | Rule |
|---|---|
| **1 · Bill of materials** | Every draw, named: kg oak, m² hide, m rope, g wax, tool wear |
| **2 · Subcomponents** | A part not in stock needs **its own fab day**, not a hand-wave |
| **3 · Doctrine choice** | Where several materials would work, audit, pick, file, and cite the precedent day |
| **4 · Phase ledger** | Multi-day heroes get phases with estimated days, cumulative percentage, and a draw column |
| **5 · Day file** | Log the consumption as a negative draw |

### ☠ Red flags — stop and fix forward

- Stock appears mid-day with no prior haul, hunt or fab
- A single named blob — *"tannery offcut"*, *"workshop spare"* — with no inventory line
- ★ **More continuous material than physics allows from counted stock** — *142 m of hide strip does not come out of 2 m² of scrap*
- A draw that exceeds the ledger — *54 g of copper from 12 g of ore*

## Skills in daily play

| Rule | Detail |
|---|---|
| **Ledger** | [skills.md](skills.md) — **Start (IRL)** plus **Now**. ★ *The Player is not a blank slate* |
| **Day files** | A hero craft, smelt or field test logs the skill checked, the **Now** tier, and PASS / PARTIAL / NO-GO |
| **Tier gate** | A task above **Now** without practice gives **PARTIAL or failure with rework cost** — never a silent PASS |
| **Updates** | Bump **Now** when a day logs the first reliable PASS at a new tier |

## Difficulty — Easy to Normal

**Target feel: a cautious, industrious solo with a reference device.** Good progress and survival are plausible; the valley still pushes back.

| Knob | Setting |
|---|---|
| **Baseline** | Above stone-age average — **not auto-win** |
| **Ceiling** | Not brutal. **No death spirals, no gratuitous catastrophe** |
| **Mishaps** | Roughly **one meaningful complication per 5–10 hero-days** on maintenance tracks · more when attempting a new tier |
| **Failure shape** | Costs **time, material, rework, delay** — ★ **rarely the total loss of a finished build** |
| **Volatility** | **normal** by default · Player may set low / normal / high — [hazards.md](hazards.md#volatility) |

## Hazard rolls

Random events use **seeded deterministic rolls**, never assistant judgment. Catalog: [hazards.md](hazards.md) · tool: `sim/roll.py`.

| Rule | Detail |
|---|---|
| **Space** | Billion-scale, so sub-percent rates are expressible |
| **Hit** | `roll < threshold × volatility × modifier` |
| **When** | The trigger matrix in [hazards.md](hazards.md) |
| **Log** | `HAZARD · d#### · ID · roll · thr · HIT/MISS` — on a hit, patch hazard state and inventory |
| **Player** | ☠ **No aging, no disease.** Injury and poison only |
| **Animals** | Age, illness and breeding roll on trigger — surface them on the farm pass, not when the Player asks |
| **Calendar gates** | ☠ **Sow and harvest stay non-negotiable.** A hazard changes the cost or the margin, never whether the crop exists |

★ **Annualize before setting any recurring threshold.** A daily rate that looks small almost never is — full procedure in [hazards.md](hazards.md).

## Wear, decay and condition

Track condition on tools and deployed structures when use or season warrants. ☠ **Gear is not forever ✓ after its first PASS.**

| Category | Examples | Trigger |
|---|---|---|
| **Tool wear** | Jaw spring · edge roll · haft loosen · string stretch | Heavy batches · metal on metal · moisture cycles |
| **Rot and pests** | Lash slack · fray · timber check · hide stiffen | Wet season · unchecked margins |
| **Structural creep** | Pitch drip · tile lift · fence sag · board spring | Freeze-thaw · load without maintenance |
| **Depletion** | Char lane thin · nail tray low · lime crust | Hero burns without refill |

★ **Cautious play mitigates wear; it does not eliminate it. Industrious play earns faster recovery, not immunity.**

**Duty:** when the Player proposes a heavy forge job, check tool condition and anvil class first. **Defer or PARTIAL if a clean PASS would be dishonest.**

## Inventory

| Rule | Detail |
|---|---|
| **Source of truth** | [inventory](inventory/index.md) for counts · [now.md](now.md) for runway |
| **When to update** | End of any day that moves stock. Patch the row and `now.md` in the same pass — ☠ **do not append a chronicle line** |
| **Estimates** | Mark `~` when not weighed that day · re-count on the next factory or smelt day |
| **Map versus inventory** | The map holds **places**; quantities live in inventory |

## Fuel

| Rule | Detail |
|---|---|
| **Scope** | Hearth cooks, indirect heat, forge-adjacent warmth — log draws on hero days |
| **Char** | Draw on smelt, forge and named cook sprints · routine stew may draw a trace |
| **Wood** | Camp fuel and journey top-up — ⚠ **not infinite background heat** |
| **Climate** | ★ **Antioch winters are mild.** Baseline heating load is low, and the char surplus covers retro ambiguity — **do not back-audit every stew** |

## Assistant device

| Rule | Detail |
|---|---|
| **Power** | **Finite.** An absurdly long-lived cell, on the order of a decade — **not infinite** |
| **Low charge** | ☠ **At 20% or below, surface exact recharge and interface instructions the Player can build toward** |
| **Charge port** | Contactless through skin, magnetic or field-coupled · no case cut · mates to a Player-built dock when the tech allows |
| **Data port** | The same coupler · needs precisely controlled electronics |
| **Speaker** | ★ **The first plausible interface** — buildable from known copper and wire grammar, no silicon required |
| **Full I/O** | Needs voltaic sources, measured circuits and stable clocks before the device can drive campus machines |
| **Play** | ☠ **The device never crafts anything physically.** The Player builds; the device specifies |
