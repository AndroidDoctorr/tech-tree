# Inventory

What exists, how much, and where it lives. **State only — no clocks.** A thing that has to happen by a date is a checklist row; the inventory records the date and nothing more.

## Which file

The split is by **how the thing behaves in the ledger**, not by what it is made of.

| Ask | File | Shape |
|---|---|---|
| *How much have I got?* | [resources.md](resources.md) | Fungible, measured, consumed |
| *Where is it and is it sharp?* | [tools.md](tools.md) | Individuated, has a condition |
| *When was it last serviced?* | [infrastructure.md](infrastructure.md) | Installed, maintained, on the map |
| *Is it still good?* | [food.md](food.md) | Edible stock — nearly every row is dated |
| — | [vehicles.md](vehicles.md) · [animals.md](animals.md) · [crops.md](crops.md) · [seed-vault.md](seed-vault.md) · [museum.md](museum.md) | Specialised |

**The test.** Losing it makes you think *"I'm down to 20 metres"* → resource. *"Where is **the** ice pick?"* → tool. It is bolted down and has a service history → infrastructure.

Rope on the coil is a resource, measured in metres. The rope reeved into a winch is not a row at all — it is a line inside that winch's infrastructure entry. Same rope; the role decides, not the material.

Buildings are not inventory. They are [map](../map/index.md).

## Rules

**Rows are read alone.** These files get grepped for one row at a time and the row arrives without its header. So each file has exactly **one** table shape, the ID leads every row, and nothing means anything by virtue of which section it sits under.

**Location is one-way, item → place.** The item moves; the shelf does not. A two-way reference is two edits per move, and the first missed edit gives two sources of truth with no way to tell which is stale. Grep is the join — searching a storage ID returns its contents computed fresh, so it is never wrong because it is never stored.

The map describes the **space** — capacity, dry or damp, frost-free, lockable. Those don't change when a sack moves. A map entry may list which shelf IDs exist in it, and a dedicated space may say what it is *for*, but no map entry lists contents.

**Prep date, never expiry.** A made-on date is observed once and never revised. An expiry is a judgement about storage conditions and it goes stale. Put the date on the row and the keep-window rule in the procedure doc — edit one line there instead of forty rows here.

**A blank date cell is information.** It states *this does not go bad*. Most resource rows are blank, and that is what lets one table carry both fired brick and olive oil.

**`Last` is a bare day ref** — `d3190`. The journal holds the detail and every link resolves, so the row does not need to repeat it.

**Quality rides in the item name** — `Copper, 97%` · `Kaolin, washed`. Too few rows need it to earn a column.

**Retire spent rows.** This is the single biggest thing keeping v1 at 3197 lines: every batch that ever closed is still sitting there at `~0`. A row at zero whose year has closed gets **deleted** — the journal already holds it, and the bay it emptied still exists as a location. Keep a `×0` row only where the ID is drawn against by something live.

Closed process instances are never inventory. `ACORN-LEACH_Y8-5` is a journal event; only the acorn it produced is stock.

## Port status

★ **Complete.** All eight v1 sections ported d3275. Rows were routed by the test above rather than by which v1 section they sat in — the v1 sections were not class-clean, and several were outright mislabelled.

| v1 section | Lines | Outcome |
|---|---|---|
| Fuel · clay · stone | 11–142 | Split across resources, tools, infrastructure, vehicles, animals |
| Food · seed · ice | 143–308 | Split across food, seed-vault, resources, tools, infrastructure |
| Metals · ore · chem | 309–498 | Split across resources, tools, infrastructure, museum · **11 doctrine rows flagged** |
| Fiber · hide · rope | 499–541 | Resources, tools, food |
| Worn now | 542–548 | tools — *Worn and carried* |
| Animals | 549–587 | animals, food, resources |
| Farm (standing) | 588–3162 | ⚠ **~12 rows to crops. The other ~2550 were deleted — see below** |
| Yard kit | 3163–3197 | infrastructure, tools, vehicles |

### ⚠ The farm section was not a farm section

Under that heading sat **~2,550 rows of a day-by-day event log** going back past d2197 — every clay haul, green press, forge day and week-close, one row each, each ending in its day number.

They were **not ported**, because they are a verbatim duplicate of the journal. Spot-checking `HAUL-CLAY-2198`, `CHAR-RETORT-2198` and `GREEN-PRESS-2198` against [day-2198](../journal/days/year-007/week-314/day-2198.md) found all three logged there in far more detail than the inventory row carried. Same for d2199, d2431, d2434, d2551 and d2552.

> **This is what the retirement rule is for, at scale.** An append-only log inside a stock file grows without bound and is never read, and it made the v1 inventory 3197 lines when the actual stock is under 400.
