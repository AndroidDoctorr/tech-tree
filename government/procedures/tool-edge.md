# Field and bench edge — condition and gates

**Live rows:** [inventory/tools.md](../../inventory/tools.md) → **Field edge — iron and steel** (+ forge peg tools as listed).

**Traffic light** on each edged tool (in `State`):

| Light | Meaning | Field / hero use |
|---|---|---|
| **GREEN** | Edge (and haft/socket) rated for rated load | **All gated work GO** |
| **AMBER** | Rolled lip · rounded point · loose socket · hammer face cupped | **Light campus only** — scare fork · weir read · bench scrape · **no hero dig · no fell · no harvest block** on that tool |
| **RED** | Chip · crack · bent tang · haft split | **Peg only** — repair or reforge before any use |
| **RETIRED** | Spent or unsafe | **Not drawn** — museum / scrap |

> ★ **AMBER is not “work slower.”** For gated heroes it is **NO-GO** until a **`FORGE-TOOL-SPRINT-*`** or targeted repair closes GREEN.

## Work gates *(minimum — agent checks before logging the hero)*

| Hero / work class | Tools that must be **GREEN** |
|---|---|
| **`HYDRO-ELEC-*` forebay / spoil dig** | **`IRON-SPADE-1`** · **`IRON-PICK-1`** |
| **`WOOD-HAUL-*` fell** | **`ST-AXE-1`** *(or named backup axe @ GREEN)* |
| **`HEMP-CUT` / `HARVEST-BLOCK` / sickle strip** | **`IRON-SICKLE-1`** |
| **`SLUICE-*` / raceway cut in cobble** | **`IRON-SPADE-1`** · **`IRON-PICK-1`** |
| **Masonry float / slab pour** | **`IRON-TROWEL-1`** · **`IRON-MORTAR-FLOAT-1`** if used |
| **Timber roof / adze battens** | **`IRON-ADZE-1`** |
| **Bed scratch / hoe till** | **`IRON-HOE-1`** |
| **Forge smelt / weld hero** | **`IRON-TONGS-1/2`** jaws · **`IRON-HAMMER-1`** face *(dress if AMBER — not a full hero block)* |

**Farm scare-only** does not require a dig-kit audit unless the day also names a **gated hero**.

## Wear accrual *(judgement + honesty)*

No hidden dice. After a **gated hero** closes, tick mentally against last service:

| Exposure | Typical push |
|---|---|
| **Full-day cobble/gravel dig** (spade + pick) | Spade **→ AMBER** after **~4–6** such days since **GREEN** · pick points **~6–8** |
| **Fell day / hard oak** | Axe **→ AMBER** after **~2–3** fell heroes without touch-up |
| **Harvest block** | Sickle **→ AMBER** if edge drags or tears stalks |
| **Wet socket / wade work** | Haft check — loose **→ AMBER** until wedge reset |

**Last full campus audit:** **`FORGE-TOOL-SPRINT-1880` d1880** — precedent for **`FORGE-TOOL-SPRINT-*`** grammar below.

Patch **`inventory/tools.md`** same pass when a light changes.

## `FORGE-TOOL-SPRINT-*` — restore day

**Hero:** ~½–1 day @ **`WW-1`** + **`GS-1`** (or forge + grindstone path used since d1880).

| Block | Work |
|---|---|
| **Gate** | **Not smelt · not pour · not exped** — edges + hafts only |
| **`TOOL-AUDIT-*` @ M2 peg rail** | Read every row in **Field edge** + hammer/tongs/chisels used this season |
| **Sprint** | Chert touch · grindstone lap · hammer face dress · haft wedge · tallow socket |
| **Close** | All drawn field kit **GREEN** or explicit **RED** + defer list |

**Consumption:** **`CHAR-LANE`** ~1–1.5 kg class · trace soap · optional **`DEER-TALLOW-Y12-1`** on sockets.

## Agent duty

1. **Before any gated hero** in the table above: grep **`inventory/tools.md`** for those IDs — if any required tool is **AMBER / RED**, **stop** and offer **`FORGE-TOOL-SPRINT-*`** (player override must be explicit).
2. **After a gated dig/fell/harvest hero** on **GREEN** tools: if the day file describes heavy cobble, note **“spade/pick service band”** in close when **~4+** dig heroes since last sprint.
3. **`now.md` header** may carry **`Dig kit GREEN`** / **`Axe GREEN`** when the player relies on that kit next — refresh on sprint close only.

## Related

- [wagon-wear.md](wagon-wear.md) — Norima **0–100** index (separate system)
- [campus-operations.md](campus-operations.md) — fuel · rett · metal path
- [rules.md](../../rules.md) — tool wear category · defer dishonest PASS
