# Trigger checklist

Checks that fire on a **condition**, never on a date. Scanned every day via `TRIGGER-SCAN` in [daily.md](daily.md) — cheap to scan, rare to fire.

A trigger lives where its condition is checked, not where its project lives. Weather does not care what the day was going to be about; the two reads missed in week 466 were both weather-fired and both sat in project documents.

Checks that fire on a *plan* rather than an observation — expedition prep, a forge day, a haul — live in [conditional.md](conditional.md).

## Weather triggers

Run against today's actual sky, before the day is planned.

| ID | Fires when | Do | A miss costs |
|---|---|---|---|
| `DRAIN-WALK` | Rain **starts** — while it is still running | Walk the CAVE-3 drainage: trench, drip lip, steps, where the water actually goes | Resolution. A dry walk reads the record — silt lines and tidemarks give the maximum — but never the flow |
| `SEEPAGE-READ` | Rain, and a cut face anywhere near the work | Read the seepage line on every terrace cut. A hillside carries water inside it, and a bench punches a hole in that plumbing, so the water comes out of the wall rather than falling on the bench | The line shows about one day a fortnight and is invisible the rest of the time. A drain cut without it goes to the wrong depth |
| `CRUST-READ` | Rain **ends**, +1–2 days | `GYPSUM-STRIP-TRIAL` crust read. A crust is a drying phenomenon; during the rain is too early | The one reading that only exists in that window |
| `WIND-SECURE` | Hard wind forecast or rising | Hive lids and roof weights, bird devices, drying racks | A lid off in the rain is a dead colony |
| `FROST-COVER` | Late frost warning | Vine, fig, any emerged bed | A year of fruit |
| `DRY-LEVELS` | Long dry spell | Rett pool level, tan pit level, beds | A rett bundle stranded dry mid-process |
| `HIVE-HEFT` | First properly fair day after a run of grey | Heft the hives. Grey days are days with no income | A colony starves a few days **before** the flow, with everything about to be fine |
| `APRON-FLOOD-READ` | **First flood that tops the bank** after any apron, riprap or bank armour is laid | Read `CAMPUS-BRIDGE-APRON-1`: has the launching collar moved, is the toe still keyed, is the mattress still under the stone | **An apron laid at low water has been proved against nothing.** The flood is the only test, and the reading is only there for a day or two afterwards |

## State triggers

Fire on a reading. Where one of these exists, it replaces any interval check for the same thing.

### Apiary — [bees.md](../government/procedures/bees.md)

| ID | Reading | Do |
|---|---|---|
| `HIVE-FEED` | Hive hefts light, or scale weight **falling** | Dearth. Feed thin honey-water with floats **and reduce the entrance** — a light colony is a robbing target |
| `SWARM-CHASE` | Sudden large weight drop on a fine day | They swarmed. Go and look |
| `FLOW-NOTE` | Scale weight **climbing** | The flow is on. Note the date — that date is a fact about the valley, not about the hive |
| `SWARM-SPLIT` | A queen cup with an **egg or jelly** in it | 8–9 day clock. Split into `SPARE-HIVE-1`, on the old stand |
| `SUPERSEDURE-LEAVE` | One or two queen cells on the comb **face** | Supersedure. Leave them — destroying them kills the colony |
| `SKEP-RENDER` | Last brood hatches in a driven skep | Render that day. Waiting buys nothing, the wax is already made, and wax moth runs on a temperature clock rather than a calendar. `SKEP-2` cost ~500 g to nine warm days |

### Food and materials

| ID | Reading | Do |
|---|---|---|
| `CHEESE-SET` | Milk crock ≥ ~2 L | Cheese — and ricotta the **same day**. Whey is a stream, not a stock; old whey is too acidic to throw ricotta. [food-menu.md](../government/procedures/food-menu.md) |
| `RETT-PULL` | A bundle snaps clean | Pull inline on that pass, not as a deferred hero. Overdue in the pool is the failure that cannot be undone |
| `JERKY-DIAGNOSE` | Weight stops falling before target | Sealed, not done. Lower the heat and raise the airflow — hurry seals the surface and strands the middle |
| `TAN-BACKOFF` | Cut edge shows a hard line | Struck too fast. Back off the liquor |
| `NITRE-FEED` | `URINE-CROCK-1` full *(pen rail, domus step)* | Pour over `NITRE-BED-1`, damp to the mark, never sodden |
| `ACORN-LEACH-RESET` | A soak left past its day, water sour, bitter edge back in clean kernels | Dump, triple-rinse, **restart from soak 1**. Leaching does not resume |

### Workshop

| ID | Reading | Do |
|---|---|---|
| `CU-CELL-DIAGNOSE` | Cathode comes down spongy | Current density too high for the bath: more area, more stirring, or richer liquor |
