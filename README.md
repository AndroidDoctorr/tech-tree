# Tech Tree Speedrun — Journal

Interactive thought experiment: one immortal human, 10,000 BC Levant, handheld assistant, goal is to trace the full human technology tree to cloning and space.

## How to read this repo

| Path | Purpose |
|------|---------|
| [purpose.md](purpose.md) | Rules of the simulation and your role |
| [rules.md](rules.md) | Canon rules — respawn, inventory, **resource & skill gates** |
| [tech-tree.md](tech-tree.md) | Milestone checklist (eras and unlocks) |
| [inventory.md](inventory.md) | What you have on person and at base |
| [map.md](map.md) | Geography, sites, trails, resources |
| [resource-map.md](resource-map.md) | Resource catalog — plants, materials, fauna by location |
| [materials-roadmap.md](materials-roadmap.md) | Grout, lime, kiln/hypocaust brick budget |
| [sun-calendar.md](sun-calendar.md) | **Solar calendar** — SUN-CAL-1 dual track · YULE anchor · interpolation |
| [schedule.md](schedule.md) | **Deadlines & routines** — daily grind · weekly checks · farm windows · **multi-day build phase ledgers** · expeditions · feast countdown |
| [year-002-plan.md](year-002-plan.md) | **Cal-Y2 strategy archive** — pointer to [journal/years/year-002.md](journal/years/year-002.md) |
| [year-001-plan.md](year-001-plan.md) | Year 1 strategy *(archived @ Day 237)* |
| [journal/years/year-002.md](journal/years/year-002.md) | **Calendar Year 2** summary (Days 238–602) |
| [advancements.md](advancements.md) | Infrastructure, tools, capabilities, key stats |
| [skills.md](skills.md) | **Skills ledger** — Start (IRL) + Now · player = you · [RAG-MUD](purpose.md#rag-mud) |
| [ladder.md](ladder.md) | **Achievement ladder** — have vs need, all tracks, one glance |
| [journal/index.md](journal/index.md) | Master timeline — links to every day and summary |
| [journal/summaries/](journal/summaries/) | **Centadials** (every 100 days) · **milladial** (every 1000 days) |
| [journal/days/](journal/days/) | Day files by week (`week-NNN/day-NNN.md`) — see **Week numbering** below |
| [journal/weeks/](journal/weeks/) | Weekly rollups — see [journal/index.md](journal/index.md) |
| [journal/years/year-001.md](journal/years/year-001.md) | **Calendar Year 1** summary (Days 1–237) |
| [journal/years/year-002.md](journal/years/year-002.md) | **Calendar Year 2** summary (Days 238–602) |
| [journal/years/year-003.md](journal/years/year-003.md) | **Calendar Year 3** *(in progress · Day 603+)* |
| [movie/](movie/) | Feature-film concept — alien trial, ensemble players, story circle |

## Week numbering

**One week = seven days.** Week *N* covers days **(N−1)×7 + 1** through **N×7**.

| Week | Days | Notes |
|------|------|-------|
| *N* | *(N−1)×7+1 – N×7* | Formula — always derive from day number |
| **113** | **785–791** | STORE-4 shell *(closed)* |
| **114** | **792–798** | Fit-out · **STORAGE-REORG ✓ Day 797** *(open)* |

When advancing the journal, set each day file's **Meta → Week** and folder **`journal/days/year-00Y/week-NNN/`** from the formula — not from “days since last week summary.” After moving a day across a week boundary, update [journal/index.md](journal/index.md), the week rollup in [journal/weeks/](journal/weeks/), and close the prior week summary at day *N×7*.

## Journal entry format

Each day file uses the same sections so summaries are easy to compile:

- **Meta** — day number, in-world date (approximate), location, weather
- **Status** — body, hunger, sleep debt, injuries, inventory
- **Events** — what happened (narrative)
- **Craft / experiments** — what you tried to make
- **Skills** — skill checked vs [skills.md](skills.md) **Now** tier; PASS / PARTIAL / NO-GO *(required on hero craft/smelt days)*
- **Discoveries** — resources, terrain, fauna noted
- **Tech** — new capabilities or refinements (linked to tech-tree.md)
- **Assistant** — questions you asked the device, answers given
- **Next** — obvious priorities for tomorrow

## Pacing

- **Day-by-day** when something new happens (crafting, danger, breakthrough).
- **Fast travel** — multi-day walks or repetitive grind get one summary paragraph inside a single day file, or a dedicated `journal/skips/skip-NNN.md` if you prefer a paper trail without 37 empty files.
- **Summaries** — ask for a week/year rollup when you want navigation, not during routine play.

## Assistant duties

The DM **checks gates before PASS** — see [rules.md — Resource & skill gates](rules.md#resource--skill-gates-assistant-duty) and [Build decomposition](rules.md#build-decomposition-assistant-duty). No building or crafting without stock, tools, prerequisite tech, and skill tier unless the day logs **NO-GO** / **queued** and names what's missing. **Multi-day builds** need a **material ledger** in schedule.md and **logged draws** in inventory.md — make subcomponents before assembly. **Wear, rot, and mishaps** apply at Easy→Normal — see [rules.md — Difficulty & realism](rules.md#difficulty--realism-easy--normal).

**Schedule discipline:** Before a hero week or multi-day expedition, read [schedule.md](schedule.md) and **warn** if the plan crosses a **Hard** deadline in the next 7–14 days (harvest · madder · feast stock · queued farm window). Name the tradeoff; player may override.

## Commands (tell the assistant)

- "Next day" — advance one day from last entry
- "Next N days" — batch with summary unless you say otherwise
- "Skip to [milestone]" — jump timeline with realistic time cost noted
- "Week summary" / "Year summary" — generate rollup files
- "Where am I on the tree?" — status against tech-tree.md
