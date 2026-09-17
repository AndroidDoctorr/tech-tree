# Periodic checklist

Everything that repeats on an interval longer than a day and shorter than a year. Seasonal date bands live in [calendar.md](calendar.md); condition-fired checks live in [triggers.md](triggers.md).

Last-done dates are state and live in [now.md](../now.md), not here.

Prefer a state trigger to an interval wherever the state is readable. An interval drifts and gets missed; "when the weight falls" cannot fire early or late. Rows here are the ones with no cheap reading to fire on.

## Every 2–3 days

| ID | Check | A miss costs |
|---|---|---|
| `TAN-LADDER` | Step the tan liquor when the cut edge reads through. Interval is a reminder — the actual trigger is the edge | Weeks, not the hide |
| `CU-CELL-CHARGE` | Recharge `CU-CELL-1` liquor with ore. The cell is liquor-limited | Sponge on the cathode, and a day's plating |

## Every ~4 days

| ID | Check | A miss costs | When live |
|---|---|---|---|
| `BIRD-DEVICE-RESET` | Move the scarecrow, change its tunic, layer a second device. Birds habituate to any single device in ~4 days — they are fooled by uncertainty, not by shapes. [sowing.md](../government/procedures/sowing.md) | The sown seed. The seed is the target, not the crop | First ~3 weeks after any sow |

## Twice a week

| ID | Check | A miss costs |
|---|---|---|
| `SNAIL-GATHER` | A-02 creek rocks. Bulk calories, brine keeps 2–4 months | Cheap calories in a year that needs them |

## Weekly

| ID | Check | A miss costs |
|---|---|---|
| `APIARY-DOORSTEP` | Every box, lid on: pollen in, traffic, fighting, drones, fanning. [bees.md](../government/procedures/bees.md) | A queenless or robbing colony, found a fortnight late |
| `FARM-CARE` | Fork loop Bed B→D. Goat pen scrape, trough and feeder read, browse top-up | Compounding — nothing here is urgent alone |
| `RETT-READ` | Every live submerged bundle: snap test, smell, day count. Runs inside the `FARM-CARE` pass, not as a separate trip. See `RETT-PULL` in [triggers.md](triggers.md) | An over-retted bundle, which is unrecoverable |
| `PERENNIAL-EYES` | Read [calendar.md](calendar.md) for live fruit and nut bands, then look at the plants on the farm pass. Bed D figs, P-03 grape, goat browse | A whole year of one crop — this is how Y9 acorn was lost |
| `JERKY-TOPUP` | Rack whatever the weir is running over with | Nothing, on a good week. The bank is built out of small weeks |
| `INVENTORY-RECONCILE` | Reconcile only the rows that moved this week | Divergence, which is silent and compounds |

## Monthly

| ID | Check | A miss costs |
|---|---|---|
| `STOCK-HOOF` | Donkey hoof pick and body read at `HOLDING-1`; goat hoof and body at `P-GOAT-1` | Lameness, which ends hauling for the season |
| `HOLDING-SCRAPE` | Scrape the holding pad | Foot problems and fly load |

## Every ~3 weeks

| ID | Check | A miss costs |
|---|---|---|
| `NITRE-TURN` | Fork `NITRE-BED-1` end over end at the `FARM-CARE` pass, then re-wet to the damp mark. Damp, never wet, and never trodden. A weakening ammonia smell is the good sign; no bloom in cold weather is expected, not a failure | The year. The bed is a slow biological process and a neglected one does not catch up |
| `BASALT-DATUM` | The three lapping blocks read against each other. Three-point support, and **turn each block** at every check — stone relaxes toward whatever it is lying on, and gravity always sags the same way. Seasoning is done when two successive checks agree, whether that is August or next spring | Lapping a stone that is still moving. It will be flat this week and wrong silently after, and everything built off it inherits the error |

## Seasonal

| ID | Check | A miss costs |
|---|---|---|
| `STORE-WALK` | Walk every store and **look up**. Of each thing ask: where does this land, and what is under it? [storage-code-1.md](../government/regulations/storage-code-1.md) | Contents, which is the biggest earthquake loss and needs no structural damage at all |

## Annual — spring, immediately after the high water

| ID | Check | A miss costs |
|---|---|---|
| `BRIDGE-AUDIT` | Plumb every footing, two minutes a crossing. Rot and scour are different clocks: age predicts rot, **water** predicts scour, and scour drops a sound bridge into a river with no warning because the hole is underwater and the structure above it looks perfect. [trail-longevity.md](../government/procedures/trail-longevity.md) | The crossing, with no warning |
| `BEAM-PROBE` | Spike-probe every buried beam end — sound wood resists, rot takes the point. Ignore the deck; a timber bridge rots where the beams sit in the bank, dark and damp with no airflow | The span |
| `REGISTER-AUDIT` | Re-read the crossing register itself, one row per crossing, and hunt for small disagreements between entries. The campus bridge sat in it twice under two names with two grades for seven years | A fact stored twice diverges, and then both copies look authoritative |
