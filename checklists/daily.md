# Daily checklist

Runs every day before any discretionary work is planned. Unconditional — these fire regardless of what the day is "about".

Procedure IDs are searchable. Where a procedure doc owns the detail it is linked; `(no doc)` means the ID is reserved and the detail has not been written up yet.

## Open block — in this order

| ID | Check | A miss costs |
|---|---|---|
| `HAZARD-ROLL` | Read the weather, then roll the seasonal `WEATHER-*` and passive `QUAKE-DAILY` rows. [hazards.md](../hazards.md) | The audit trail |
| `TRIGGER-SCAN` | Run [triggers.md](triggers.md) against today's sky and today's readings — **before** planning the day, not after | A reading that only exists today |
| `CALENDAR-READ` | Open [calendar.md](calendar.md) and read the live band lines. Do not read from memory | A mandatory sow or harvest, silently |
| `PERIODIC-DUE` | Check [periodic.md](periodic.md) against the last-done dates in [now.md](../now.md) | Drift — the interval items are the ones that slip |

## Chores

| ID | Check | A miss costs |
|---|---|---|
| `MILK-GOAT` | Milk to crock. ~½ h *(blocked Feb–Apr until freshen)* | The doe |
| `STOCK-WATER` | Water and feed goats and donkeys; eyes on each animal while you do it | The animal — and the daily look is how illness gets caught early |
| `WEIR-FISH` | Clear the weir. Primary fresh protein | A day's protein, and a fouled weir |
| `HEARTH-BANK` | Bank the fire; check fuel on hand for tomorrow's work | An hour relighting, and any process that needed heat at dawn |
| `CONSUMPTION-DAILY` | Log **Daily** draws in the day file: **food · soap · heat/cook fuel · lamp** — [.cursor/rules/daily-consumption.mdc](../.cursor/rules/daily-consumption.mdc) | Silent calories and fuel — the larder drifts without audit |
| `STOCK-WATCH` | After patches: any row **×0** or **runway thin** → `## Stock watch` in day file | One calculation per debit — inventory is the ledger |

## Running processes

Only the ones live right now. Retire a row when its process closes.

| ID | Check | A miss costs |
|---|---|---|
| `CU-CELL-TEND` | `CU-CELL-1` — one look in the morning, one in the evening | A stalled or shorted cell running all night for nothing |
| `HIVE-SCALE-READ` | `HIVE-SCALE-1`, **at the same hour every day**. A hive weighs less at noon with its foragers out than at dusk | A point off the forage curve — and the curve is the whole point of the scale |

## Standing rule

Every sow and every harvest in [calendar.md](calendar.md) is mandatory. The only valid skip is an explicit player defer stated that turn; silence is never a defer. An unlogged item inside a live window is an agent failure, not a player choice — name outstanding items **before** a band closes.
