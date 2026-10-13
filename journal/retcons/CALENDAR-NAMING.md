# Calendar naming — clocks, tags, IDs

**Authority:** [CAL-Y-EPOCH-Y13.md](CAL-Y-EPOCH-Y13.md) · [CAL-Y-JAN1-NOT-YULE-Y15.md](CAL-Y-JAN1-NOT-YULE-Y15.md)

**Tool:** `python3 sim/cal_year.py --day <d####>` *(d ≥ 4620)*

## Clocks

| Clock | Meaning | Use |
|---|---|---|
| **`d####`** | Absolute campaign day | **Primary** — hazards, inventory `Last`, audit |
| **`Cal-Yn` · `Dn`** | **Civil** year + day-of-year | Day headers · **roll only 31 Dec / 1 Jan** |
| **`year-0NN` folder** | `floor((d−1)/365)+1` | **Paths only** — anniversary buckets, not civil year |
| **`CYn` in new IDs** | Civil year at tag time *(d4620+)* | **`LOT-CY13-1`** — not the same as legacy **`Y14`** harvest tags |

## Civil epoch *(live)*

- **d4620 = Cal-Y13 D1** (~1 Jan Y13).
- **Before d4620:** headers in journal are **historical**; do not bulk-edit. **+2 display inflation** vs true civil is documented in [CAL-Y-EPOCH-Y13.md](CAL-Y-EPOCH-Y13.md).

## Frozen tag years — do not rename

**`-Ynn-` in an existing ID** = **label frozen when the lot opened** (harvest, sprint, mis-tagged civil). Examples:

- **`GRAIN-FERMENT-Y14-1`** — ferment lot tagged Y14
- **`WAGON-V2-OVERHAUL-Y15-1`** — overhaul tagged under old inflated counter; civil **CY13** era when logged
- **`THERMAE-FULL-Y14-3`** — towel sprint tag 14

Grep the **ID string**, not today’s **`Cal-Y`**.

## New IDs *(d4620+)*

Use **`CY13`** (civil year at open) for new stock, builds, and heroes:

- ✓ **`DISTILL-CY13-1`** · **`SPRING-SOW-CY13`**
- ✗ Do not mint new **`-Y15-`** civil tags

## Yule vs New Year

| Event | Rolls `Cal-Y`? |
|---|---|
| **~21 Dec `SUN-YULE`** | **No** — feast / hunt / solstice observance |
| **31 Dec `CAL-Yn-CLOSE`** | **Yes** |
| **1 Jan `Cal-Y(n+1) D1`** | **Yes** |

## Agent rule

1. **Header civil year:** `sim/cal_year.py` or anchor table — not folder `year-0NN`, not Yule.
2. **Never renumber** legacy **`-Ynn-`** inventory rows for civil correction.
3. **New tags:** **`CY` + civil year** per epoch above.
