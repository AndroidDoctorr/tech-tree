# Food

Edible stock. Its own file because nearly every row carries a date, which is the opposite of [resources.md](resources.md) where nearly none do.

`| ID | Item | Qty | Where | Made | Last |`

**`Made` is close to mandatory here.** Blank means genuinely indefinite — salt. `?` means the date was lost in the v1 format and should be set at the next audit. Keep windows live once in [processing.md](../government/procedures/processing.md) and [food-menu.md](../government/procedures/food-menu.md), never on the row.

No expiry column. Date plus rule gives the answer on read, and a better keep window is then one edit instead of forty.

## Grain and meal

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `BARLEY-BULK-Y10` | Barley, bulk · Y10 trial harvest | ~0.48 kg | Horreum A barley bay | d3491 | d3491 |
| `EMMER-BULK-Y10` | Emmer, bulk · Y10 harvest | ~2.56 kg | Horreum A, `EMMER-BULK-Y10` incoming bay | d3485 | d3488 |
| `EMMER-BULK-Y9` | Emmer, bulk · ⚠ **germ ~half** — a thin eating year | ~0.85 kg | Horreum A, `EMMER-BULK-Y9` bay | Y9 | d3214 |
| `PARCHED-MU-12` | Parched emmer · green · Y10 refresh | ~0.38 kg | `P-μ-12` | d3489 | d3508 |
| `BARREL-4-GRAIN` | Cracked grain, working · Y10 top-up | ~0.46 kg | `BARREL-4`, v1 | d3488 | d3504 |
| `STARTER-Y6-1` | Sourdough starter, emmer · **daily feed** | — | Culina warm peg | d2041 | live |

`STARTER-Y6-1` is the only row in the inventory that dies if ignored for a week. Feeding it is a [daily.md](../checklists/daily.md) concern, not a stock concern.

## Pulse

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FAVA-GREEN-Y10-FINAL` | Fava, tender shelled · **eat / short brine** | ~0.50 kg | Cool shelf | d3325 | d3325 |
| `FAVA-DRYING-Y10-FOOD` | Fava, mature food beans · drying, not seed | ~0.25 kg wet-sort | Drying rack | d3325 | d3325 |
| `HUMMUS-Y10-1` | Hummus · chickpea · oil · garlic | ~170 g | Cool cellar step crock | d3492 | d3509 |
| `P-18-CHICKPEA-Y10` | Chickpea · Y10 harvest | ~48 g | Horreum A pulse bay | d3491 | d3492 |
| `P-17-LENTIL-Y10` | Lentil · Y10 harvest | ~126 g | Horreum A pulse bay | d3486 | d3498 |
| `P-17-LENTIL-Y6` | Lentil | ~91 g | Horreum A pulse bay `P-17-Y6` | Y6 | d2892 |
| `P-17-LENTIL-Y5` | Lentil | ~178 g | Pulse bay | Y5 | — |
| `P-18-CHICKPEA-Y5` | Chickpea | ~164 g | Pulse bay, post-expand | Y5 | — |

All Y7–Y9 pulse bays went to the ground at `SOW-Y10-D2` on d3212 and are empty. The bays persist as locations; the rows do not. `FAVA-SEED-Y10` remains standing in [crops.md](crops.md) and is not food stock until dry threshing separates the seed bank first.

## Nuts

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `PISTACHIO-1` | Pistachio kernels | ~3.64 kg | Horreum A nut tray | Y10 | d3508 |
| `ACORN-ROAST-Y9` | Acorn, shelled and roast · Y9 batches ×3 | ~1.86 kg | Nut tray | Y9 | [retcon](../journal/retcons/ACORN-GATHER-Y9.md) |
| `ACORN-ROAST-Y10-1` | Acorn roast · **`ACORN-LEACH-Y10-1` batch** | ~575 g | Nut tray | d3423 | d3508 |
| `ACORN-ROAST-Y10-2` | Acorn roast · **`ACORN-LEACH-Y10-2` batch** | ~610 g | Nut tray | d3465 | d3465 |
| `ACORN-ROAST-Y10-3` | Acorn roast · **`ACORN-LEACH-Y10-3` batch** | ~605 g | Nut tray | d3471 | d3471 |
| `ACORN-ROAST-Y10-4` | Acorn roast · **`ACORN-LEACH-Y10-4` batch** | ~600 g | Nut tray | d3478 | d3478 |
| `ACORN-SHELL-ON` | Acorn, bulk shell-on | ~1.15 kg | v1 mat · `WOOD-CRATE-4` | Y10 | d3469 |

Roast acorn wants 1–3 months of dry before it settles. Leaching is `ACORN-LEACH` in [processing.md](../government/procedures/processing.md); the troughs are [infrastructure.md](infrastructure.md).

## Fruit

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FIG-LEATHER-1` | Fig leather, rolled | ~720 g | Horreum east rack peg | ? | d3508 |
| `FIG-LEATHER-TRAY-Y10-1` | Fig leather, tray drying | ~0.65 kg wet | Sun rack / horreum porch | d3368 | d3380 |
| `FIG-FRESH-Y10-1` | Fig, fresh hold · Bed D first pass | ~1.25 kg | Cool step | d3368 | d3368 |
| `FIG-FRESH-Y10-2` | Fig, fresh · Bed D second pass | ~0.55 kg | Cool step | d3375 | d3375 |
| `FIG-FRESH-Y10-4` | Fig, fresh · Bed D strip | ~0.4 kg | Cool step | d3389 | d3389 |
| `GRAPE-FRESH-Y10-1` | Grape, fresh · P-03 partial strip | ~0.93 kg | Cool step | d3375 | d3508 |
| `GRAPE-FRESH-1` | Grape, fresh hold | ~1.15 kg | Cool step | Y9 | d3145 |

## Meat and fish

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `DEER-SMOKE-Y10-1` | Smoked deer | ~10.6 kg | Horreum A smoke shelf | d3253 | d3253 |
| `FISH-SMOKE-1` | Smoked fish | ~1.57 kg | Smoke rack, pool | ? | d3508 |
| `GOOSE-SMOKE-Y10-1` | Smoked goose · Y10 Yule hunt remainder | **~0.95 kg** | Horreum A smoke shelf | d3509 | d3509 |
| `GOOSE-SMOKE-1` | Smoked goose · Y9 tail | ~0.79 kg | Horreum A smoke shelf | ? | d3146 |
| `GOOSE-GIBLET-JAR` | Goose giblets, jarred | ~280 g | — | ? | d2426 |
| `STEW-Y10-JAR` | Stew jar, Y10 · lentil–emmer | ~0.80 kg | Cool cellar step | d3489 | d3508 |
| `STEW-Y9-JAR` | Stew jar, Y9 | ~0.80 kg | Cool cellar step | Y9 | d3145 |
| `STEW-Y8-JAR` | Stew jar, Y8 · tail | ~0.06 kg | Cool cellar step | Y8 | d2903 |
| `RED-STAG-Y10-1` | Red stag carcass · hide to tan queue · sinew · bone | ~95 kg | Racks and larder | d3269 | d3269 |

★ `DEER-SMOKE-Y10-1` is the largest single food row on the campus and the reason Y10 protein is not a worry.

⚠ **`RED-STAG-Y10-1` rendered only ~1.4 kg of tallow** — a fraction of an autumn deer. It was a velvet stag and spring-lean. **Autumn deer are the fat deer**, which is why pemmican is an autumn job and not a spring one: a pack is measured in fat, protein and starch, not in kilograms. See [food-menu.md](../government/procedures/food-menu.md).

## Dairy

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CHEESE-AGED-Y10-1` | ★ **First rennet-set wheel** · salted · **first Yule wedge cut d3509** | **~1.65 kg remain @ wheel** | **Cool dairy shelf, clean reed mat** | d3315 | d3509 |
| `CHEESE-Y10-10` | Cheese | ~320 g | Dairy shelf | d3260 | d3260 |
| `CHEESE-Y10-9` | Cheese | ~250 g | Dairy shelf | d3260 | d3260 |
| `RICOTTA-Y10-4` | Ricotta, off fresh whey | ~190 g | Dairy shelf | d3260 | d3260 |
| `RICOTTA-Y10-3` | Ricotta, off fresh whey | ~150 g | Dairy shelf | d3260 | d3260 |
| `RICOTTA-Y10-2` | Ricotta · thin — made on stale whey | ~110 g | Dairy shelf | d3260 | d3260 |
| `CHEESE-Y10-8` | Cheese · clean set, clean break | ~230 g | Dairy shelf | d3250 | d3250 |
| `CHEESE-Y10-7` | Cheese, pressed · ⚠ **fresh, acid-set — eat within days** | ~250 g | Culina | d3244 | d3244 |
| `CHEESE-Y10-6` | Pressed curd · ⚠ **fresh, acid-set — eat within days** | ~225 g | Culina | d3236 | d3236 |
| `GOAT-MILK-CROCK` | Goat milk | ~0.20 L | Ice vault niche | d3260 | d3260 |
| `WHEY-1` | Whey · ★ **working stock — do not bank it** | ~1.5 L | Cool step | d3236 | d3236 |

Ricotta off **fresh** whey runs half again the yield of ricotta off stale — the `RICOTTA-Y10-2` row is the control. The year's open cheese question is thistle heads in June, not the procedure, which runs without thought now.

★★ **Whey keeps souring after it leaves the curd, so run ricotta the same day as the cheese.** Acid whey gives a poor ricotta yield and sweet rennet whey gives far more, and the difference is measured in hours, not days. Old whey is not waste — it goes to the retarder jar, the goats, or the soil.

⚑ **`CHEESE-AGED-Y10-1`: turn DAILY until the rind is dry and firm, then return to `CAVE-3` and turn twice weekly. Wax only after the rind is established.** *The cave shelf tested too wet for the initial dry stage; its temperature remains excellent for later ageing.*

★ **Whey is a plaster retarder.** Gauging with whey roughly doubles working time, to about 25 minutes. That is the difference between a wall you can finish and one that goes off in the bucket.

## Cured and dried

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `JERKY-Y10` | ★ Jerky · **dry, cool, in cloth, not sealed** | ~3.84 kg @ horreum · **~0.6 kg recovery pouch @ cave** | Horreum A / cave | d3253 | d3458 |
| `GOAT-SMOKE-1` | Smoked goat | ~0.60 kg | v1 cool shelf | ? | d3508 |
| `DEER-SMOKE-BATCH` | Smoked deer, earlier batch | ~6.1 kg | Horreum A | d3128 | d3128 |
| `TALLOW-KITCHEN` | Tallow, kitchen fat jar | ~0.26 kg | Culina | | d3537 |
| `SOAP-Y10-1` | Soap bars · rosemary–thyme · **GREEN · cure shelf** | ~0.47 kg green *(~22 bars)* | W-1 porch cure shelf | d3452 | d3539 |
| `DEER-TALLOW-Y10-1` | Deer tallow · rendered separate — candles and the wax-rosin pot | ~0.45 kg | Lamp jar · culina | d3251 | d3539 |

⚠ **Not sealed is deliberate.** Sealing jerky while it still breathes is how you find mould. `JERKY-Y10` was made **to a number** — weighed wet, dried to ~⅔ loss with no plateau, then cut and checked dry through rather than judged by feel.

☠ **Deer tallow is rendered well away from the drying rack and never stored near it.** Fat on drying meat is how a batch spoils.

## Oil

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `OIL-Y10-1` | Olive oil, clear · **cook live** | ~1.12 L | Glass bottles · working draw ~320 ml at `P-ξ-5` | d3479 | d3509 |
| `OIL-Y9-1` | Olive oil, clear · **cook live** | ~1.03 L | Glass bottles · working draw ~390 ml at `P-ξ-5` | d3117 | d3452 |
| `OIL-Y8-1` | Olive oil, clear · bulk settle | ~1.27 L | Glass bottles · `P-ξ-5` | d2749 | d3100 |
| `OIL-Y7-1` | Olive oil, clear | ~1.31 L | Glass bottles · `P-ξ-5` | d2408 | d3185 |
| `OIL-Y6-1` | Olive oil, clear | ~2.05 L | `GLASS-BOTTLE-4/5` · `P-ξ-5` | d2043 | d2043 |
| `OIL-SEDIMENT-Y10` | Olive oil sediment, sealed | ~125 ml | `AMPHORA-6` foot | d3490 | d3490 |
| `OIL-SEDIMENT-Y9` | Olive oil sediment, sealed | ~170 ml | `AMPHORA-6` foot | d3126 | d3126 |
| `OIL-SEDIMENT-Y8` | Olive oil sediment, sealed | ~165 ml | `AMPHORA-6` foot | d2760 | d2760 |

`Made` is the **press** date, not the decant — the clock starts when the fruit is crushed. Cool, dark and full is what keeps it; headroom air is what ruins it. Sediment stays sealed at the amphora foot and is never stored with the clear, which is why the clear keeps a year. See `OLIVE-PRESS` in [processing.md](../government/procedures/processing.md).

## Vinegar and ferment

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `GRAPE-VINEGAR-Y9-1` | Grape vinegar · Y9 fork · merged to `VINEGAR-Y6-1` | ~2.15 L rack | `AMPHORA-5` | d3475 | d3475 |
| `GRAPE-MUST-Y7-1` | Grape must, matured · vinegar-ready | ~1.48 L | Horreum | Y7 | d3509 |
| `VINEGAR-Y6-1` | Vinegar · Y6/Y7/Y8/Y9 bands merged | ~2.75 L class | `AMPHORA-5` · `P-ξ-4` · crock | Y6 | d3508 |
| `VINEGAR-MOTHER-1` | Vinegar mother + mat | ~200 ml | Crock | live | d2704 |

## Olives in brine

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `OLIVE-BRINE-Y10-1` | Olive, brined · 6–18 mo band | ~1.24 kg fruit | Crock #2, v1 porch | d3480 | d3508 |
| `OLIVE-BRINE-Y8-1` | Olive, brined · 6–18 mo band | ~1.9 kg fruit | Crock #2, v1 porch | d2747 | d2747 |
| `OLIVE-BRINE-Y7-1` | Olive, brined · 6–18 mo band | ~1.9 kg fruit | Crock #2, v1 porch | d2397 | d2397 |
| `OLIVE-BRINE-Y6-1` | Olive, brined · 6–18 mo band | ~910 g fruit | Crock #2, v1 porch | d2056 | d2056 |
| `OLIVE-BRINE-LEGACY` | Olive brine, P-02 legacy | ~2.0 kg | P-02 crock | ? | — |

The 6–18 month band is the one real keep window in this file. Y6 is well past it and should be read before it is relied on.

## Salt and spice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `SALT-1` | Salt | ~9.03 kg @ larder · **~1.0 kg @ `CAVE-RECOVERY-CRATE-1`** | Larder / cave | | d3474 |
| `SPICE-MU-10` | Spice | — | `P-μ-10`, horreum A margin | | — |
| `MINT-CROCK-1` | Mint | — | Crock | | d3175 |

Salt is the one indefinite row. **Y10 evap band OPEN** (6 Nov – 26 Nov) — cycle 1 harvested d3474 · trays empty · haul #15 when named.

## Ice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ICE-VAULT-STOCK` | Ice, hard class · ★ **full to cap, Y10 record** | ~130 kg | Ice vault | Y10 | d3193 |

Stock here, plant in [infrastructure.md](infrastructure.md) — `ICE-VAULT-NICHE-2` and `COLD-CELLAR-FAN-1`.

## Herbs

Dried herbs are food and belong here. Standing herbs are [crops.md](crops.md); herb seed is [seed-vault.md](seed-vault.md). Y9 herb stock went to the ground on d3219 — reserves only, listed in the vault.

## Pending port

v1 §Food · seed · ice is ported. Spent process instances — `ACORN-LEACH-Y6-1` through `Y8-6`, the Y5–Y8 stew tails, the Y6–Y9 bread bakes, trail packs — were **not** carried over. They are closed records and they live in the journal.
