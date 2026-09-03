# Tech Tree Speedrun — Journal

Interactive thought experiment: one immortal human, 10,000 BC Levant, handheld assistant, goal is to trace the full human technology tree to cloning and space.

## How to read this repo

**Play path (routine next-day):** [now.md](now.md) · last day · [player-calendar.md](player-calendar.md) · grep [inventory.md](inventory.md).

| Path | Purpose |
|------|---------|
| [now.md](now.md) | **Live snapshot** — date, farm, char, next three |
| [purpose.md](purpose.md) | Rules of the simulation and your role |
| [rules.md](rules.md) | Canon — respawn, inventory, resource & skill gates |
| [player-calendar.md](player-calendar.md) | Recurring season windows |
| [inventory.md](inventory.md) | Live stock counts · lookup: [fixtures](inventory/fixtures.md) · [bridges](inventory/bridges-and-trail.md) · [tools](inventory/tools-lab.md) |
| [tech-tree.md](tech-tree.md) | Milestone checklist |
| [map.md](map.md) | HOME geography · campus · local trails |
| [route-a-road.md](route-a-road.md) | Long routes · TQ/BQ · leg registry |
| [resource-map.md](resource-map.md) | Plants, materials, fauna by location |
| [inventory/bridges-and-trail.md](inventory/bridges-and-trail.md) | Live crossings · trail kit |
| [skills.md](skills.md) | Skills ledger — Start (IRL) + Now |
| [journal/days/](journal/days/) | Day files · week `= ceil(day/7)` |
| [journal/weeks/](journal/weeks/) | Weekly rollups |
| [journal/index.md](journal/index.md) | Human timeline hub — do not load on play turns |
| [journal/summaries/](journal/summaries/) | Centadials / milladial |
| [obsolete/](obsolete/) | Archived plans · schedule · ladder · GPS notes |
| [sun-calendar.md](sun-calendar.md) | SUN-CAL-1 marks — lookup, not daily |
| [advancements.md](advancements.md) | Capability list — lookup |
| [movie/](movie/) | Feature-film concept |

## Week numbering

**One week = seven days.** Week *N* covers days **(N−1)×7 + 1** through **N×7**.

When advancing the journal, set **Meta → Week** and folder `journal/days/year-00Y/week-NNN/` from the formula. Append one row to [journal/index.md](journal/index.md) **Recent days** and the matching [part file](journal/index/) — do not read the full index.

## Journal entry format

Keep days short. One fact once. See `.cursor/rules/day-journal-slim.mdc`.

- **Meta** — day, Cal-Y date, place, weather
- **Events** — one paragraph or one table, not both
- **Consumption** — draws with amounts
- **Skills** — hero craft / new-tier only
- **Next** — 2–3 lines

Do not restate Events in Discoveries, Tech, Assistant, and a footer.

## Pacing

- **Day-by-day** when something new happens (crafting, danger, breakthrough).
- **Fast travel** — multi-day walks or repetitive grind get one summary paragraph inside a single day file, or a dedicated `journal/skips/skip-NNN.md` if you prefer a paper trail without 37 empty files.
- **Summaries** — ask for a week/year rollup when you want navigation, not during routine play.

## Assistant duties

The DM **checks gates before PASS** — see [rules.md — Resource & skill gates](rules.md#resource--skill-gates-assistant-duty) and [Build decomposition](rules.md#build-decomposition-assistant-duty). No building or crafting without stock, tools, prerequisite tech, and skill tier unless the day logs **NO-GO** / **queued** and names what's missing. **Multi-day builds** need phases in the current week file or `now.md` and **logged draws** in inventory.md — make subcomponents before assembly. **Wear, rot, and mishaps** apply at Easy→Normal — see [rules.md — Difficulty & realism](rules.md#difficulty--realism-easy--normal).

**Schedule discipline:** Before a hero week or multi-day expedition, read [now.md](now.md) and [player-calendar.md](player-calendar.md). Warn if the plan crosses a hard window in the next 7–14 days (sow · harvest · madder · feast · ice). Name the tradeoff; player may override.

## Commands (tell the assistant)

- "Next day" — advance one day from last entry
- "Next N days" — batch with summary unless you say otherwise
- "Skip to [milestone]" — jump timeline with realistic time cost noted
- "Week summary" / "Year summary" — generate rollup files
- "Where am I on the tree?" — status against tech-tree.md
