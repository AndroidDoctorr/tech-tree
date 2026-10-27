# Food

Edible stock. Its own file because nearly every row carries a date, which is the opposite of [resources.md](resources.md) where nearly none do.

`| ID | Item | Qty | Where | Made | Last |`

**`Made` is close to mandatory here.** Blank means genuinely indefinite — salt. `?` means the date was lost in the v1 format and should be set at the next audit. Keep windows live once in [processing.md](../government/procedures/processing.md) and [food-menu.md](../government/procedures/food-menu.md), never on the row.

No expiry column. Date plus rule gives the answer on read, and a better keep window is then one edit instead of forty.

★ **Consolidated d5327** — interchangeable batches merged to **one row + total qty**; per-year IDs retired (journal holds press/distill/harvest history).

## Grain and meal

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`PARCH-EMMER-FOOD-1`** | Emmer, parched · quick-cook · **Y15–Y16 merge** | **~2.57 kg** | Horreum quick-cook peg | d4950 | d5337 mash |
| **`EMMER-BULK-Y16`** | Emmer, bulk · Y16 harvest dry | **~0.30 kg** | Horreum A main bay | d5315 | d5405 sow |
| **`BARLEY-BULK-Y16`** | Barley, bulk · Y16 trial | **~73 g** | Horreum A barley bay | d5314 | d5406 expand |
| **`EMMER-BULK-TAIL-Y10-14`** | Emmer, bulk · graded · **Y10–Y14 bay tails** *(sow backup)* | **~1.96 kg** | Horreum A main + incoming bays | Y10–Y14 harvests | d5405 sow |
| **`BARLEY-BULK-TAIL-Y10-14`** | Barley, bulk · trial · **Y10–Y14 tails** *(sow backup)* | **~1.44 kg** | Horreum A barley bay | Y10–Y14 trials | d5040 sow backup |
| `BARREL-4-GRAIN` | Cracked grain, working · v1 tap | **~0.51 kg** | `BARREL-4`, v1 | d4589 | d5325 sprint |
| `STARTER-Y6-1` | Sourdough starter, emmer · **daily feed** | — | Culina warm peg | d2041 | live |

`STARTER-Y6-1` is the only row in the inventory that dies if ignored for a week. Feeding it is a [daily.md](../checklists/daily.md) concern, not a stock concern.

## Pulse

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`STEW-Y16-JAR-5325`** | Pulse + emmer stew jar · Y16 sprint | **~0.72 kg** | Cool cellar step | d5325 | d5337 feast hold |
| **`P-17-LENTIL-FOOD-1`** | Lentil · dry food · **Y15–Y16 merge** | **~367 g** | Horreum A pulse bay north | d4950 | d5327 consolidate |
| **`P-18-CHICKPEA-FOOD-1`** | Chickpea · dry food · **Y15–Y16 merge** | **~460 g** | Horreum A pulse bay south | d4951 | d5327 consolidate |

All Y7–Y9 pulse bays went to the ground at `SOW-Y10-D2` on d3212 and are empty. The bays persist as locations; the rows do not. `FAVA-SEED-Y10` remains standing in [crops.md](crops.md) and is not food stock until dry threshing separates the seed bank first.

## Nuts

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `PISTACHIO-1` | Pistachio kernels · roast tray class | **~11.36 kg** | Horreum A nut tray | Y10–Y16 | d5253 roast Y16 |
| `ACORN-SHELL-ON` | Acorn, bulk shell-on | **~27.75 kg** | **`NUT-SHELF-EXT-1` west lip** | **Y16 lap 2 d5281** | d5320 tail |
| **`ACORN-ROAST-FOOD-1`** | Acorn roast · leached · **Y15–Y16 merge** | **~1.91 kg** | Nut tray | d5253 | d5327 consolidate |

Roast acorn wants 1–3 months of dry before it settles. Leaching is `ACORN-LEACH` in [processing.md](../government/procedures/processing.md); the troughs are [infrastructure.md](infrastructure.md).

## Honey

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`HONEY-STRAINED-Y13-1`** | Strained honey · pale-bar crush-strain | **~1.24 kg** | **`GLASS-BOTTLE-11` @ culina shelf** | d4726 + d4796 retcon | d5456 band tail |

*Co-harvested with **`WAX-CUT-SURPLUS`** on strong hives — not brood comb. See [apiary-routine.md](../government/procedures/apiary-routine.md).*

**`FIG-NEWTON` standard fill (going forward):** fig paste from fresh + leather as available · **`HONEY-STRAINED-Y13-1` ~3 g / unit** · emmer + oil dough — same bake grammar as **d4841**.

## Fruit

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`FIG-LEATHER-Y15-1`** | Fig leather tray · sun dry | **~0.78 kg gross wet** | Horreum east rack | d4839 | d5338 newton fill |
| **`FIG-NEWTON-Y14-1`** | Fig-honey emmer cakes · Yule bake | **×6 @ cool jar** | Horreum sweet peg | d5338 | d5338 feast |
| **`GOOSE-SMOKE-Y14-1`** | Yule greylag · cold-smoke remainder | **~1.02 kg** | Horreum A smoke shelf | d5338 hunt | d5338 rack |

## Meat and fish

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FISH-SMOKE-1` | Smoked fish | **~2.77 kg** | Smoke rack, pool | ? | d5337 feast warm |
| **`DEER-JERKY-FOOD-1`** | Red deer jerky · **Y12 + Y15 merge** | **~11.9 kg** | Horreum snack jar | d3798 | d5327 consolidate |
| **`DEER-SMOKE-FOOD-1`** | Red deer · cold-smoke · **Y12 + Y15 merge** | **~38.8 kg** | Horreum A smoke shelf A | d3797 | d5327 consolidate |
| **`BOAR-JERKY-Y15-1`** | Wild boar jerky | **~4.7 kg** | Horreum snack jar | d4913 | d4913 |
| **`BOAR-SMOKE-Y15-1`** | Wild boar · cold-smoke | **~6.95 kg** | Horreum A smoke shelf | d4913 | d5337 belly |
| **`BOAR-TALLOW-Y15-1`** | Wild boar tallow · rendered | **~1.785 kg** | Horreum cool step jar | d4912 | d5381 machines |

★ **Deer/boar smoke + jerky banks** live after **d4958** · **d5326** cull · **d5327** deer rows merged.

⚠ **`RED-STAG-Y10-1` rendered only ~1.4 kg of tallow** — a fraction of an autumn deer. It was a velvet stag and spring-lean. **Autumn deer are the fat deer**, which is why pemmican is an autumn job and not a spring one: a pack is measured in fat, protein and starch, not in kilograms. See [food-menu.md](../government/procedures/food-menu.md).

## Dairy

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CHEESE-AGED-Y10-1` | ★ **First rennet-set wheel** · salted · Yule wedges d3509 · d3873 · d4240 · d4609 | **~0.37 kg remain @ wheel** | **Cool dairy shelf, clean reed mat** | d3315 | d5337 wedge |
| `WHEY-1` | Whey · ★ **working stock — do not bank it** | **~0.38 L** | Cool step | d5326 | d5326 refresh |

Ricotta off **fresh** whey runs half again the yield of ricotta off stale — the `RICOTTA-Y10-2` row is the control. The year's open cheese question is thistle heads in June, not the procedure, which runs without thought now.

★★ **Whey keeps souring after it leaves the curd, so run ricotta the same day as the cheese.** Acid whey gives a poor ricotta yield and sweet rennet whey gives far more, and the difference is measured in hours, not days. Old whey is not waste — it goes to the retarder jar, the goats, or the soil.

⚑ **`CHEESE-AGED-Y10-1`: turn DAILY until the rind is dry and firm, then return to `CAVE-3` and turn twice weekly. Wax only after the rind is established.** *The cave shelf tested too wet for the initial dry stage; its temperature remains excellent for later ageing.*

★ **Whey is a plaster retarder.** Gauging with whey roughly doubles working time, to about 25 minutes. That is the difference between a wall you can finish and one that goes off in the bucket.

## Cured and dried

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `SOAP-Y10-1` | Soap bars · rosemary–thyme · sealed @ service pegs | **×2 full** · **×2 thin tails** on hooks · **×1 open @ culina** *(d5406)* | Service pegs | d3452 | d5406 farm |
| **`SOAP-Y15-1`** | Soap bars · rosemary–thyme · **titre-charged batch** | **×24 GREEN · ~1.85 kg** @ W-1 porch cure shelf | W-1 porch | d5404 | curing |
| **`SOAP-WORKING-CULINA-1`** | Open working bar @ culina hearth dish | **~0 g** *(exhausted d5404)* | Culina hearth | d3452 | d5404 wash |
| `DEER-TALLOW-Y10-1` | Deer tallow · rendered separate — candles and the wax-rosin pot | **~0.194 kg** | Lamp jar · culina | d3251 | d5381 lamp |
| **`DEER-TALLOW-Y12-1`** | Deer tallow · **`DEER-HUNT-Y12-3795`** · autumn render | **~4.12 kg** | Horreum cool step jar | d3795 | d5404 soap |

⚠ **Not sealed is deliberate.** Sealing jerky while it still breathes is how you find mould. `JERKY-Y10` was made **to a number** — weighed wet, dried to ~⅔ loss with no plateau, then cut and checked dry through rather than judged by feel.

☠ **Deer tallow is rendered well away from the drying rack and never stored near it.** Fat on drying meat is how a batch spoils.

## Oil

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`OIL-OLIVE-CLEAR-1`** | Olive oil, clear · cook live · **Y9–Y16 merge** | **~6.86 L @ glass rack** · **~1.18 L working @ `P-ξ-5`** | Horreum A oil rack | Y9 press | d5404 soap |
| **`OIL-OLIVE-SEDIMENT-1`** | Olive oil sediment, sealed · **foot + side cups merge** | **~1.22 L** | `AMPHORA-6` foot + side cups | Y8–Y16 press | d5327 consolidate |

`Made` is the **oldest press band in the merge** for the clear row — individual decant dates live in the journal. Cool, dark and full is what keeps it; headroom air is what ruins it. Sediment stays sealed and is never stored with the clear. See `OLIVE-PRESS` in [processing.md](../government/procedures/processing.md).

## Vinegar and ferment

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`VINEGAR-WORKING-1`** | Vinegar · **Y6–Y9 merge** · **~5.8 % acetic class d5042** | **~4.86 L class** | `AMPHORA-5` · `P-ξ-4` · crock | Y6 | d5404 titre |
| `VINEGAR-MOTHER-1` | Vinegar mother + mat | ~200 ml | Crock | live | d2704 |
| **`SPIRIT-GRAIN-POTABLE-1`** | Grain spirit · hearts · **~42 % class** · **Y13–Y17 merge** | **~8.45 L** | Chem spirit peg + labelled bottles | d3926 | d5411 dehyd |

Dehyd stock: **`ETHANOL-DEHYD-STOCK-1`** @ [resources.md — Alcohol · ethanol organics pathway](resources.md#alcohol--ethanol-organics-pathway).

**`GRAIN-FERMENT-Y17-1` ✓ CLOSED d5343** *(whiskey mash · journal)*. **`GRAIN-FERMENT-Y18-1` ⧗ day 0 d5511** — wild food mash @ **`BARREL-5-FERMENT`**. Closed batches → journal; potable hearts consolidated **d5327** + **d5343**.

## Olives in brine

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`OLIVE-BRINE-FOOD-1`** | Olive, brined · **Y14 + Y15 jars merge** | **~1.68 kg fruit** | **`OLIVE-JAR-Y14-1` + `OLIVE-JAR-Y15-1` · v1 porch** | d4576 | d5327 consolidate |

The 6–18 month band is the one real keep window in this file. Read oldest jar first after merge.

## Salt and spice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `SALT-1` | Salt | **~7.10 kg @ larder** · **~1.0 kg @ `CAVE-RECOVERY-CRATE-1`** | Larder / cave | | d5419 brine top |
| `SPICE-MU-10` | Spice | — | `P-μ-10`, horreum A margin | | — |
| `MINT-CROCK-1` | Mint | — | Crock | | d3175 |

Salt is the one indefinite row. **`SALT-EVAP` band OPEN** (6 Nov – 26 Nov) · **cycle 2 harvest ✓ d4578 · optional pour #3**.

## Ice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ICE-VAULT-STOCK` | Ice, hard class | **~77.2 kg** | Ice vault | CY15 peak closed | d5423 C₄ trap |

Stock here, plant in [infrastructure.md](infrastructure.md) — `ICE-VAULT-NICHE-2` and `COLD-CELLAR-FAN-1`.

## Herbs

Dried herbs are food and belong here. Standing herbs are [crops.md](crops.md); herb seed is [seed-vault.md](seed-vault.md). Y9 herb stock went to the ground on d3219 — reserves only, listed in the vault.

Spent batches and **d4958 / d5326** spoilage tails are **not** listed here — see [index.md](index.md) retirement rule and the journal.
