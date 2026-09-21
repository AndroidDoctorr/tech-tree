# Periodic checklist

Everything that repeats on an interval longer than a day and shorter than a year. Seasonal date bands live in [calendar.md](calendar.md); condition-fired checks live in [triggers.md](triggers.md).

Last-done dates are state and live in [now.md](../now.md), not here.

Prefer a state trigger to an interval wherever the state is readable. An interval drifts and gets missed; "when the weight falls" cannot fire early or late. Rows here are the ones with no cheap reading to fire on.

## ★★ Read the NEGLECT column first *(added d3281)*

> ☠ ★★★ **Half of this list does not wait for you. Missing a PAUSE row costs an afternoon; missing a REVERSE row costs the thing itself** — the nitre bed does not sit at whatever it had reached, it goes airless in the middle and the nitrate it already made is taken apart again.

| | |
|---|---|
| ★ **PAUSE** | The process stops and resumes where it left off. **Late is just late** |
| ☠ ★★★ **REVERSE** | The process runs the other way, or a window closes. **Late is LOST, and no amount of later gets it back** |

☠ **These looked identical on this page for years.** *"A miss costs the year" sat on the nitre row, in words I wrote myself, in the same column as "a fouled weir" — and it read as the same kind of sentence.*

## Every 2–3 days

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| `TAN-LADDER` | Step the tan liquor when the cut edge reads through. ☠ **And watch the LIQUOR, not only the edge** — it is alive and spoils on its own clock whether or not the hide is ready | ⚠ **Revised d3281: not "weeks, not the hide."** Seventeen warm days turned the liquor sour and scummed and cost grain on the face that sat proud | ☠ **REVERSE** |
| `CU-CELL-CHARGE` | Recharge `CU-CELL-1` liquor with ore. The cell is liquor-limited | Sponge on the cathode, and a day's plating | ★ PAUSE |
| `RETORT-DRY-READ` *(closed d3330)* | **✓ `RETORT-E`–`H` bone-dry d3330** | ☠ **A thin neck dries before the bulb, pulling the joint open before the kiln ever sees it** | ✓ **DONE** |

## Every ~4 days

| ID | Check | A miss costs | When live | Neglect |
|---|---|---|---|---|
| `BIRD-DEVICE-RESET` | Move the scarecrow, change its tunic, layer a second device. Birds habituate to any single device in ~4 days — they are fooled by uncertainty, not by shapes. [sowing.md](../government/procedures/sowing.md) | The sown seed. The seed is the target, not the crop | First ~3 weeks after any sow | ☠ **REVERSE** |

## Twice a week

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| `SNAIL-GATHER` | A-02 creek rocks. Bulk calories, brine keeps 2–4 months | Cheap calories in a year that needs them | ★ PAUSE |
| `CHEESE-TURN-MATURE` *(corrected d3320)* | **Turn every wheel with an established rind twice weekly.** ☠ **A fresh tacky wheel is not on this interval — it turns DAILY under `CHEESE-RIND-DRY`** | ☠ **An unturned wheel settles its moisture downward and ages WET at the bottom and DRY at the top** — *and by the time that shows it is months old and past fixing* | ☠ **REVERSE** |

## Weekly

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| `APIARY-DOORSTEP` | Every box, lid on: pollen in, traffic, fighting, drones, fanning. [bees.md](../government/procedures/bees.md) | A queenless or robbing colony, found a fortnight late | ☠ **REVERSE** |
| `FARM-CARE` | Fork loop Bed B→D. Goat pen scrape, trough and feeder read, browse top-up | Compounding — nothing here is urgent alone | ★ PAUSE |
| `RETT-READ` | Every live submerged bundle: snap test, smell, day count. Runs inside the `FARM-CARE` pass, not as a separate trip. See `RETT-PULL` in [triggers.md](triggers.md) | An over-retted bundle, which is unrecoverable | ☠ **REVERSE** |
| `PERENNIAL-EYES` | Read [calendar.md](calendar.md) for live fruit and nut bands, then look at the plants on the farm pass. Bed D figs, P-03 grape, goat browse | A whole year of one crop — this is how Y9 acorn was lost | ☠ **REVERSE** |
| `JERKY-TOPUP` | Rack whatever the weir is running over with | Nothing, on a good week. The bank is built out of small weeks | ★ PAUSE |
| `INVENTORY-RECONCILE` | Reconcile only the rows that moved this week | Divergence, which is silent and compounds | ☠ **REVERSE** |

## Monthly

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| `STOCK-HOOF` | Donkey hoof pick and body read at `HOLDING-1`; goat hoof and body at `P-GOAT-1` | Lameness, which ends hauling for the season | ☠ **REVERSE** |
| `HOLDING-SCRAPE` | Scrape the holding pad | Foot problems and fly load | ★ PAUSE |
| ☠ ★★★ `SMOKE-SPOT` | **A clean cool tile held in the gas of every enclosed fire for a slow count — hub, domus, forge.** ★★ **Date it and rack it beside last month's; the reading is the COMPARISON, not the tile.** *Barely marked on a good fire, black in seconds on a starved one* | ☠ ★★★ **The only warning I get.** *A starved fire makes soot and the colourless gas together, in proportion — and I have no headache, no nausea and no bad night to tell me* | ☠ **REVERSE** |
| ☠ `READ-BEFORE-SWEEP` | **No flue is swept until it is read: depth, texture, colour, and WHERE along the run.** ⚑ **Sweep date chalked on the flue, because the reading that matters is the RATE of return** | ☠ ★★★ **Sweeping without reading throws away the measurement and resets the experiment.** *Nine years of it* | ☠ **REVERSE** |

## Every ~3 weeks

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| `NITRE-TURN` | Fork `NITRE-BED-1` end over end at the `FARM-CARE` pass, then re-wet to the damp mark. Damp, never wet, and never trodden. A weakening ammonia smell is the good sign; no bloom in cold weather is expected, not a failure | The year. The bed is a slow biological process and a neglected one does not catch up | ☠ **REVERSE** |
| `BASALT-DATUM` | The three lapping blocks read against each other. Three-point support, and **turn each block** at every check — stone relaxes toward whatever it is lying on, and gravity always sags the same way. Seasoning is done when two successive checks agree, whether that is August or next spring | Lapping a stone that is still moving. It will be flat this week and wrong silently after, and everything built off it inherits the error | ☠ **REVERSE** |

## Quarterly

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| ☠ ★★★ `CORD-LIFE-READ` | **Every cordage bearing weight or a body — crane fall, cave fixed line, well rope, harness.** *Down, bent, flexed, opened at the lay; ends and bearing points first* | ☠ ★★★ **A fall, which is the ONE hazard I am not immune to** — *and both ropes found on the first walk were older than the rule that governs them* | ☠ **REVERSE** |
| ⚑ ★★★ `WORLD-FIRST-WALK` | **Walk a quarter of the property and name everything the eye lands on. For each: what list is this on · what is its clock · when was it last read.** ☠ **Anything with no answer is a finding, and the finding is the missing row** | ☠ ★★★ **A list can only catch what is already on it.** *Every failure of the d3295–d3303 fortnight was an item with no row anywhere* | ★ PAUSE |
| `DECAY-ROSTER-READ` | **Walk `DECAY-ROSTER-1` and refresh last-read dates** — *oil, tallow, varnish, glue, lime, charcoal, cordage, hide, wax, cell liquors* | ☠ **A stock is a quantity TIMES A RATE, and an unread stock has no number** | ★ PAUSE |
| ☠ ★★★ `RULE-AUDIT` *(added d3313)* | **Walk every filed rule against what was actually DONE.** ⚑ **Each survivor must carry a FIRST ACTION and a DATE, or it is struck** | ☠ ★★★ **Every rule filed in the glow of a discovery is dead; every rule filed while annoyed is alive.** *Understanding is the hard part and the part I enjoy, so a rule written at that moment FEELS finished.* ★★★ **A rule that does not land on a calendar band or a checklist is not filed — it is REMEMBERED** | ☠ **REVERSE** |

## Seasonal

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| `STORE-WALK` | Walk every store and **look up**. Of each thing ask: where does this land, and what is under it? [storage-code-1.md](../government/regulations/storage-code-1.md) | Contents, which is the biggest earthquake loss and needs no structural damage at all | ★ PAUSE |

## Annual — spring, immediately after the high water

| ID | Check | A miss costs | Neglect |
|---|---|---|---|
| `BRIDGE-AUDIT` | Plumb every footing, two minutes a crossing. Rot and scour are different clocks: age predicts rot, **water** predicts scour, and scour drops a sound bridge into a river with no warning because the hole is underwater and the structure above it looks perfect. [trail-longevity.md](../government/procedures/trail-longevity.md) | The crossing, with no warning | ☠ **REVERSE** |
| `BEAM-PROBE` | Spike-probe every buried beam end — sound wood resists, rot takes the point. Ignore the deck; a timber bridge rots where the beams sit in the bank, dark and damp with no airflow | The span | ☠ **REVERSE** |
| `REGISTER-AUDIT` | Re-read the crossing register itself, one row per crossing, and hunt for small disagreements between entries. The campus bridge sat in it twice under two names with two grades for seven years | A fact stored twice diverges, and then both copies look authoritative | ★ PAUSE |
