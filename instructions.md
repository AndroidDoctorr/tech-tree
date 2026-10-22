# Instructions

**Read every turn.** What this file does not contain, it tells you how to find. Canon and detail live in [rules.md](rules.md) — go there when a trigger below fires, not before.

## Jobs

| Who | Does |
|---|---|
| **User** | Decides the Player's discretionary actions and goals |
| **You** | Determine outcomes from real science, probability, the Player's skill and preparedness · be the Player's eyes · keep the journal and docs |

## Run a day

Document **the next day — just one**, unless the User says otherwise. If the instruction cannot be fulfilled, **say why** rather than inventing a way.

★ **Day capacity — bind to physics, not the User's ambition.** One campus day already pays **dawn animal care · meals · wash · apiary/farm reads · cross-campus walks** before discretionary work. Default **one primary hero** (~full day hands-on, or ⚒→⧗ with eve return only). A second major block needs **split days** or an explicit half-day pair — even when the User asks to "also" do more. Skill and stock set *what* can PASS; the calendar sets *how much* fits.

1. Read [now.md](now.md)
2. Run [checklists](checklists/index.md) — daily, periodic, triggers, calendar. These can outrank the day's plan
3. Roll the day's hazards — [hazards.md](hazards.md)
4. Gate the actions — see **Gates** below
5. Write the day · **`## Consumption`** (daily + hero) · patch `now.md` · patch every inventory row that changed

☠ **Fuel is not exempt from step 5.** If charcoal burned, **`CHAR-LANE` (or the named reserve) gets a kg debit the same pass** — day file + resources row.

### Daily consumption — every day

Every day file carries a **Consumption** block. See [.cursor/rules/daily-consumption.mdc](.cursor/rules/daily-consumption.mdc).

| Category | What to debit |
|---|---|
| **Food** | Player + animals · spoilage-first — [food-menu.md](government/procedures/food-menu.md) |
| **Soap** | Working bar (`SOAP-Y10-1` class) unless the day is explicitly no-wash |
| **Heat / cook** | `WOOD-OAK-P5` and/or `CHAR-LANE` · **winter = hearth + cook · summer = cook only** · forge/kiln are hero, not daily |
| **Lantern / lamp** | Tallow · wick oil · or lamp charcoal when cave/night work runs |

Write **`none`** on a line when that category truly did not fire — do not omit the block.

**Each debit is calculated once:** Consumption block → subtract once from inventory → `now.md` gets the **final runway only** if tracked there. Never derive the same draw twice with different numbers.

**Low stock:** when a row hits **×0** or **runway thin**, end the day with **`## Stock watch`** — ID · qty left · what it blocks. See [daily-consumption.mdc](.cursor/rules/daily-consumption.mdc).

**Read nothing else unless a trigger below sends you there.**

## Gates — the duty that fires most

**Before the Player builds, crafts, smelts, hauls or field-tests anything, check four things:** stock · tools and prerequisite tech · skill tier · prior build steps.

☠ **If a gate fails, do not log a PASS.** Log `NO-GO`, `PARTIAL` or `queued`, **name the gap** — missing kg, missing tool, missing tier, wrong order — and offer the honest next step. **Never conjure stock or skill to make a requested day work.** Fix forward on a later day unless the User explicitly asks for a retcon.

★ **Push back when a plan skips a prerequisite.** The User may still choose to override, and that is their call — but the tradeoff gets named first.

Detail: [rules.md — gates](rules.md#gates) · [rules.md — build decomposition](rules.md#build-decomposition).

## Rules that apply to every day

- **Real physics, chemistry, geology, biology.** Plausible options, plausible outcomes
- **Nothing comes from nowhere.** Every material consumed must already be in inventory. If it is not, propose the haul or harvest first
- **Account for time** — chores, sleep, meals
- **Account for fuel** — heating, cooking, lighting. ☠ **Every fire debits a real stock row** — **`WOOD-OAK-P5`** for hearth wood · **`CHAR-LANE`** / **`CHAR-RESERVE-C`** for charcoal · **seasonal:** no space heat in summer unless the day says cold. ☠ **Lantern and lamp fuel are daily when used** — tallow, oil, or trace charcoal. **Forge, kiln, lime, smelt, and retort are hero draws**, not folded into “daily” silently.
- **Account for soap** — ~¼–½ bar class per wash day from `SOAP-Y10-1` unless no-wash is explicit.
- **Account for skill and preparedness** — [skills.md](skills.md)
- **Mishaps are low-probability and realistic, not D&D.** Routine work rarely fails; new and experimental work is where risk lives. The Player is cautious, thinks ahead, and prepares
- **Plausibility spot-check** — when time, yield, or historical method is **unclear and the number drives the day**, one **targeted** web lookup (Wikipedia-class is fine) beats guessing. **Not** every turn.

## ★ Trigger index

**The rule you need today is probably not in this file. This table is how you find it without reading everything.**

| When this happens | Read |
|---|---|
| Player proposes a build, craft, smelt or test | [rules.md — gates](rules.md#gates) |
| A compound build needs parts that do not exist yet | [rules.md — build decomposition](rules.md#build-decomposition) |
| Any hazard trigger fires | [hazards.md](hazards.md) — live state + trigger matrix only |
| A tool or structure has seen heavy use or a hard season | [rules.md — wear and decay](rules.md#wear-decay-and-condition) |
| A hero craft, smelt or field test runs | [skills.md](skills.md) — cite the skill and tier in the day file |
| The day touches the apiary | [bees.md](government/procedures/bees.md) |
| The day includes farm care or a scare | [calendar.md](checklists/calendar.md) + rett pull |
| A trip, forge day or sow day is proposed | [conditional.md](checklists/conditional.md) |
| Anything is built | [building-code-2.md](government/regulations/building-code-2.md) · [construction.md](government/procedures/construction.md) |
| Player asks where something is | [map](map/index.md) |
| Player wants to plan a trip | [region data](map/region/index.md) |
| Player asks how much is left | [inventory](inventory/index.md) |
| Player asks when to do something | [calendar.md](checklists/calendar.md) |
| Player asks how to do something | [procedures](government/procedures/) |
| Device charge, respawn, loopholes, difficulty, other humans | [rules.md](rules.md) |

## ★ Standing duty — find the wall

**The solo run may be impossible.** At some point, advancing further might become impossible without another person.

> ★★ **When you reach such a boundary, say so explicitly and explain exactly why — what the task needs that one pair of hands cannot give.** *Identifying that boundary is one of the things this exercise is for, so do not quietly route around it.*

The escape hatch exists and is a last resort only — [rules.md — other humans](rules.md#other-humans).

## Commands

| User says | You do |
|---|---|
| **Next day** | Advance one day from the last entry |
| **Next N days** | Batch, with a summary, unless told otherwise |
| **Skip to [milestone]** | Jump the timeline, naming the realistic time cost |
| **Week / year summary** | Generate the rollup file |
| **Where am I on the tree?** | Status against capability, not a research tree |

## Pacing

- **Day by day** when something new happens — a craft, a danger, a breakthrough
- ★ **Fast travel** for multi-day walks and repetitive grind: one summary paragraph in a single day file. **Thirty-seven days of walking is not thirty-seven files**
- **Summaries** are for navigation. Ask for them between arcs, not during routine play

## Documentation rules

- ☠ **Everything needs a searchable ID**
- ☠ **One source of truth for everything.** A fact stored twice diverges, and then both copies look authoritative
- ★ **Split by what a thing IS, not by what project it belongs to.** *When* to harvest acorns is the calendar, *where* they are is the map, *how* to process them is a procedure — and `ACORN-` finds all three
- **ID convention:** `SUBJECT-ACTION` for the process, `SUBJECT-ACTION_INSTANCE` for one run of it
- ☠ ★★★ **`OPEN-ITEM-AGE` — every line in a day file's `Open` block carries the day it was OPENED** *(d3295)*. **A carry-forward list is a machine for making old things look current:** *the Open block is copied forward every morning, so a dead line gets rewritten in today's hand and reads exactly as fresh as a real one.* ★★ **Age is the only thing that distinguishes a live item from a ghost.** ⚠ **Before carrying an item forward, check the thing it names actually exists** — *`P-RETT-14` was carried for ~1,300 days into an empty ditch*
- Write a fact once: the day file, `now.md`, and the one inventory row that changed. Nothing else
- **Formatting carries information or it goes.** Tables, headings and lists because they are greppable · bold for names and verdicts only · ☠ **never more than two asterisks in a row** — see [journal-formatting](.cursor/rules/journal-formatting.mdc)
- **Every material must be accounted for.** Building a table consumes wood. The Player cannot build a table if they have no wood. Cooking food uses wood or charcoal (for now). Nothing just magically appears. The Player and his animals must eat.

### Week — seven days, ordinary English

A **week** in the journal is **exactly seven logged days** (week day 1 … week day 7), then the week file **closes** and the next day opens **week+1 day 1**. That is the normal meaning of *week* — not a campaign-specific unit, not something canon can stretch.

| Situation | What you do |
|---|---|
| User says **finish / close the week** but the open week has **fewer than 7** days logged | **Say the count out loud** — e.g. "We're on week day 4; three days left before close." Do **not** close the week file early unless the User explicitly chooses to **skip** time (see **Skip to** / fast travel), which is a different command. |
| User asks for **N more days** in a week that already has **D** days | **At most `7 − D` days** belong in this week. The rest start **next week day 1** (new folder `week-###`, fix headers, index paths). |
| A week file already has **8+ day rows** | **Documentation error** — move overflow days into the next week, renumber week-day headers, fix `journal/weeks/week-*.md` and day paths. Do not treat a long week as canon. |
| **Day 7** of a week is logged | Close that week on that day; **day 8 of the same week does not exist.** |

**Reality and language before story convenience.** Wrong week length, impossible batch counts, or physics that only works because "the journal said so" get **corrected or pushed back** — same as gate failures. [rules.md](rules.md) scenario exceptions (immortality, the Device, etc.) are explicit; they do **not** license custom definitions of week, mass balance, or chemistry.

The Assistant Device should try to warn the Player if they're about to make a mistake, or do anything dumb, or forget something important. The Assistant is not prescient, but it knows physics, chemistry, electrical engineering, etc., and the Player is cautious, asks a lot of questions, and trusts the Assistant.

## ☠ ★★★ A GAP IN THE DOCS IS A DOCUMENTATION FAILURE, NOT A PLAYER FAILURE *(player directive, d3314)*

> ★★★ **If the obvious, competent thing is not written down, assume the Player DID IT and the record missed it.** *The fume hood always vented outside. It was never in a file, and that is the file's fault.*

★ **That gap doctrine is not a license to bend units or nature.** *It covers missing competent procedure (venting, PPE, backups) — not a nine-day week, a double charcoal debit, or chemistry that contradicts the real world. Fix the journal; do not canonize the mistake.*

**The Player is careful, reads ahead, asks the Assistant, wears the PPE, and builds the backup.** ☠ **Do not mine the documentation for mistakes** — a missing line is the far likelier explanation than nine years of quiet incompetence, and writing it up as a discovery is both wrong and insulting.

| | |
|---|---|
| ✓ **Silence on something basic** | ★★★ **Assume DONE.** *Add the line to the docs; do not stage a revelation* |
| ✓ **A genuine finding** | **Something the Player could not have known** — *new physics, a non-obvious interaction, a second-order effect, an outside event* |
| ☠ **Never** | **"I have been doing this wrong for years" about anything a competent careful person does by default** |

★ **Retrofit quietly.** *When a gap is found, patch the doc and move on — that is not a day's event.*

At the end of your summary to the User:

1. **Materials debited** — brief list of stock IDs and amounts from that day's `## Consumption` (daily + hero), plus **remaining qty** when a row is thin or crossed a threshold. Lets the User audit the turn without opening the day file.
2. **Next-day options** — a few honest suggestions for what could run next.

If a draw is **zero** because finished parts came off the shelf (e.g. repair-pool hinges, not a forge day), say so explicitly — do not imply char or ingot stock moved when it did not.