# Food

Edible stock. Its own file because nearly every row carries a date, which is the opposite of [resources.md](resources.md) where nearly none do.

`| ID | Item | Qty | Where | Made | Last |`

**`Made` is close to mandatory here.** Blank means genuinely indefinite — salt. `?` means the date was lost in the v1 format and should be set at the next audit. Keep windows live once in [processing.md](../government/procedures/processing.md) and [food-menu.md](../government/procedures/food-menu.md), never on the row.

No expiry column. Date plus rule gives the answer on read, and a better keep window is then one edit instead of forty.

## Grain and meal

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`PARCH-EMMER-Y16-1`** | Emmer, parched · quick-cook stash | **~1.02 kg** | Horreum quick-cook peg | d5315 | d5315 parch |
| **`PARCH-EMMER-Y15-1`** | Emmer, parched · quick-cook stash | **~1.18 kg** | Horreum quick-cook peg | d4950 | d4972 mash |
| **`EMMER-BULK-Y16`** | Emmer, bulk · Y16 harvest dry | **~2.82 kg** | Horreum A main bay | d5315 | d5315 store |
| **`BARLEY-BULK-Y16`** | Barley, bulk · Y16 trial | **~0.88 kg** | Horreum A barley bay | d5314 | d5316 tag |
| **`EMMER-BULK-TAIL-Y10-14`** | Emmer, bulk · graded · **Y10–Y14 bay tails** | **~2.16 kg** | Horreum A main + incoming bays | Y10–Y14 harvests | d5040 sow backup |
| **`BARLEY-BULK-TAIL-Y10-14`** | Barley, bulk · trial · **Y10–Y14 tails** | **~1.44 kg** | Horreum A barley bay | Y10–Y14 trials | d5040 sow backup |
| **`PARCHED-EMMER-TAIL-Y13-14`** | Parched emmer · sprint refresh tails | **~0.88 kg** | Horreum snack jar `P-μ-12` | d4221 / d4589 | d4608 |
| `PARCHED-WILD-GRAIN-Y12-1` | Parched wild mix · **`P-05` einkorn + `P-06` barley** · Y12–Y14 food laps | **~1.99 kg** | Horreum snack jar | d3685 | d4595 |
| `BARREL-4-GRAIN` | Cracked grain, working · v1 tap | **~0.58 kg** | `BARREL-4`, v1 | d4589 | d4956 stew |
| `STARTER-Y6-1` | Sourdough starter, emmer · **daily feed** | — | Culina warm peg | d2041 | live |

`STARTER-Y6-1` is the only row in the inventory that dies if ignored for a week. Feeding it is a [daily.md](../checklists/daily.md) concern, not a stock concern.

## Pulse

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FAVA-FRESH-Y16-1` | Fava, fresh shelled · eat-now · **`FAVA-Y16`** | **~0.45 kg** | Kitchen cool step | d5134 pick | d5161 pick |
| `FAVA-BRINE-Y12-1` | Fava, short brine · tender tail | **~0.72 kg** | Crock #3 cool step | d3704 | d3704 |
| `FAVA-DRY-Y12-FOOD-1` | Fava, dry food · blanch + rack finish · **not seed bank** | **~3.18 kg** | Horreum A pulse bay | d3704 | d3704 |
| `FAVA-PARCHED-Y12-1` | Fava, parched · trail / snack | **~0.54 kg** | Horreum snack jar | d3704 | d3704 |
| **`P-17-LENTIL-Y13`** | Lentil · Y13 harvest | **~143 g** | Horreum A pulse bay | d4217 | d4221 |
| **`P-18-CHICKPEA-Y13`** | Chickpea · Y13 harvest | **~201 g** | Horreum A pulse bay | d4218 | d4221 |
| `P-18-CHICKPEA-Y10` | Chickpea · Y10 harvest | ~48 g | Horreum A pulse bay | d3491 | d3492 |
| **`P-18-CHICKPEA-Y12`** | Chickpea · Y12 harvest | **~201 g** | Horreum A pulse bay | d3851 | d3854 |
| **`P-17-LENTIL-Y16`** | Lentil · Y16 harvest | **~268 g** | Horreum A pulse bay | d5315 | d5316 rack |
| **`P-18-CHICKPEA-Y16`** | Chickpea · Y16 harvest | **~286 g** | Horreum A pulse bay | d5316 | d5316 porch |
| **`P-17-LENTIL-Y15`** | Lentil · Y15 harvest | **~194 g** | Horreum A pulse bay | d4950 | d4956 stew |
| **`P-18-CHICKPEA-Y15`** | Chickpea · Y15 harvest | **~229 g** | Horreum A pulse bay | d4951 | d4956 stew |
| **`STEW-Y15-JAR-4956`** | Pulse + emmer stew jar · Y15 sprint | **~0.70 kg** | Cool cellar step | d4956 | d4973 feast |
| **`P-17-LENTIL-Y14`** | Lentil · Y14 harvest | **~186 g** | Horreum A pulse bay | d4585 | d4589 |
| **`P-18-CHICKPEA-Y14`** | Chickpea · Y14 harvest | **~287 g** | Horreum A pulse bay | d4585 | d4586 |
| **`P-17-LENTIL-Y12`** | Lentil · Y12 harvest | **~153 g** | Horreum A pulse bay | d3850 | d3854 |
| `P-17-LENTIL-Y10` | Lentil · Y10 harvest | ~126 g | Horreum A pulse bay | d3486 | d3498 |
| `P-17-LENTIL-Y6` | Lentil | ~91 g | Horreum A pulse bay `P-17-Y6` | Y6 | d2892 |
| `P-17-LENTIL-Y5` | Lentil | ~178 g | Pulse bay | Y5 | — |
| `P-18-CHICKPEA-Y5` | Chickpea | ~164 g | Pulse bay, post-expand | Y5 | — |

All Y7–Y9 pulse bays went to the ground at `SOW-Y10-D2` on d3212 and are empty. The bays persist as locations; the rows do not. `FAVA-SEED-Y10` remains standing in [crops.md](crops.md) and is not food stock until dry threshing separates the seed bank first.

## Nuts

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `PISTACHIO-1` | Pistachio kernels · roast tray class | **~11.36 kg** | Horreum A nut tray | Y10–Y16 | d5253 roast Y16 |
| `ACORN-ROAST-Y9` | Acorn, shelled and roast · Y9 batches ×3 | **~0.66 kg** | Nut tray | Y9 | d3591 |
| `ACORN-ROAST-Y10-1` | Acorn roast · **`ACORN-LEACH-Y10-1` batch** | ~575 g | Nut tray | d3423 | d3508 |
| `ACORN-ROAST-Y10-2` | Acorn roast · **`ACORN-LEACH-Y10-2` batch** | ~610 g | Nut tray | d3465 | d3465 |
| `ACORN-ROAST-Y10-3` | Acorn roast · **`ACORN-LEACH-Y10-3` batch** | ~605 g | Nut tray | d3471 | d3471 |
| `ACORN-ROAST-Y10-4` | Acorn roast · **`ACORN-LEACH-Y10-4` batch** | ~600 g | Nut tray | d3478 | d3478 |
| **`ACORN-ROAST-Y12-1`** | Acorn roast · **`ACORN-LEACH-Y12-1` batch** | **~575 g** | Nut tray | d3787 | d3872 |
| **`ACORN-ROAST-Y13-1`** | Acorn roast · **`ACORN-LEACH-Y13-1` batch** | **~605 g** | Nut tray | d4236 | d4236 |
| **`ACORN-ROAST-Y13-2`** | Acorn roast · **`ACORN-LEACH-Y13-2` batch** | **~600 g** | Nut tray | d4236 | d4236 |
| **`ACORN-ROAST-Y16-1`** | Acorn roast · **`ACORN-LEACH-Y16-1` soak 1** | **~610 g** | Nut tray | d5282 | d5282 roast |
| **`ACORN-ROAST-Y16-2`** | Acorn roast · **`ACORN-LEACH-Y16-1` soak 2** | **~615 g** | Nut tray | d5306 | d5306 roast |
| `ACORN-SHELL-ON` | Acorn, bulk shell-on | **~26.5 kg** | **`NUT-SHELF-EXT-1` west lip** | **Y16 lap 2 d5281** | d5282 soak 2 |
| **`ACORN-ROAST-Y15-1`** | Acorn roast · Y15 tail batch | **~680 g** | Nut tray | d5253 | d5253 roast |

Roast acorn wants 1–3 months of dry before it settles. Leaching is `ACORN-LEACH` in [processing.md](../government/procedures/processing.md); the troughs are [infrastructure.md](infrastructure.md).

## Honey

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`HONEY-STRAINED-Y13-1`** | Strained honey · pale-bar crush-strain | **~0.95 kg** | **`GLASS-BOTTLE-11` @ culina shelf** | d4726 + d4796 retcon | d5092 wax cut |

*Co-harvested with **`WAX-CUT-SURPLUS`** on strong hives — not brood comb. See [apiary-routine.md](../government/procedures/apiary-routine.md).*

**`FIG-NEWTON` standard fill (going forward):** fig paste from fresh + leather as available · **`HONEY-STRAINED-Y13-1` ~3 g / unit** · emmer + oil dough — same bake grammar as **d4841**.

## Fruit

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`FIG-LEATHER-Y14-1`** | Fig leather tray · sun dry | **~2.15 kg gross wet** | **`W-1` / east rack** | d4469 | d4474 tray |
| **`FIG-FRESH-Y15-1`** | Fig fresh · Bed D Y15 pass + repeat | **~0.45 kg** | Cool step | d4839 | d4841 repeat |
| **`FIG-FRESH-Y15-2`** | Fig fresh · Bed D Y15 band tail | **~0.35 kg** | Cool step | d4875 | d4875 tail |
| **`FIG-LEATHER-Y15-1`** | Fig leather tray · sun dry | **~0.84 kg gross wet** | Horreum east rack | d4839 | d4964 feast tray |
| **`FIG-LEATHER-Y15-2`** | Fig leather tray · tail lap | **~0.12 kg gross wet** | Horreum east rack | d4875 | dry |
| **`FIG-NEWTON-Y15-1`** | Fig newton · emmer shell · **fig + honey fill** | **×12 · ~315 g net** | **`PORC-PLATE-2` @ cool step** | d4841 | d4972 plate |

## Meat and fish

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FISH-SMOKE-1` | Smoked fish | **~2.31 kg** | Smoke rack, pool | ? | d4973 feast |
| **`GOOSE-SMOKE-Y15-1`** | Smoked goose · Y15 Yule hunt remainder | **~0.98 kg** | Horreum A smoke shelf | d4973 | d4973 hunt |
| **`GOOSE-SMOKE-Y13-1`** | Smoked goose · Y13 Yule hunt remainder | **~0.85 kg** | Horreum A smoke shelf | d4240 | d4973 feast |
| **`GOOSE-SMOKE-Y14-1`** | Smoked goose · Y14 Yule hunt remainder | **~0.96 kg** | Horreum A smoke shelf | d4609 | d4609 |
| **`DEER-JERKY-Y12-1`** | Red deer jerky · scale-dried batch | **~4.8 kg** | Horreum snack jar | d3798 | d3798 |
| **`DEER-SMOKE-Y12-1`** | Red deer · cold-smoke Y12 | **~14.60 kg** | Horreum A smoke shelf | d3797 | d4973 feast |
| **`DEER-JERKY-Y15-1`** | Red deer jerky · spring block | **~7.1 kg** | Horreum snack jar | d5110 | d5110 |
| **`DEER-SMOKE-Y15-1`** | Red deer · cold-smoke Y15 | **~24.2 kg** | Horreum A smoke shelf | d5110 | d5110 |
| **`DEER-TALLOW-WET-Y15-1`** | Spring deer trim fat | **~0.75 kg** @ cool step | d5108 | d5178 harness dress |
| **`BOAR-ORGANS-Y15-1`** | Heart · liver · trim | **~0.4 kg** stew tail | d4911 | d4912 |
| **`BOAR-TALLOW-Y15-1`** | Wild boar tallow · rendered | **~1.82 kg** | Horreum cool step jar | d4912 | d4913 trace |
| **`BOAR-JERKY-Y15-1`** | Wild boar jerky | **~4.7 kg** | Horreum snack jar | d4913 | d4913 |
| **`BOAR-SMOKE-Y15-1`** | Wild boar · cold-smoke | **~7.15 kg** | Horreum A smoke shelf | d4913 | d4964 belly carve |
| **`BOAR-BELLY-RASHERS-Y15-1`** | Boar-belly rashers · crisp · Yule menu | **~140 g** @ cool step | Cool step tail | d4972 | d4973 feast |
| **`HONEY-FRITTERS-Y15-1`** | Honey fritters · emmer batter · hot-hold | **×8 · ~140 g** tail | Domus ante | d4972 | d4973 feast |
| **`EMMER-YEAST-BREAD-Y15-4972`** | Feast loaf · starter | **~330 g** tail @ board | Culina board | d4972 | d4973 feast |
| **`YULE-FEAST-TRAY-Y15-1`** | Dry feast portion · domus ante | staged | Domus ante | d4964 | eat Yule |
| **`POSCA-BATCH-Y15-4964`** | Posca · vinegar batch | **~0.4 L** | Culina crock | d4964 | d4964 |
★ **Y12/Y15 smoke + jerky banks** are the live protein shelf after **d4958 spoilage pass**.

⚠ **`RED-STAG-Y10-1` rendered only ~1.4 kg of tallow** — a fraction of an autumn deer. It was a velvet stag and spring-lean. **Autumn deer are the fat deer**, which is why pemmican is an autumn job and not a spring one: a pack is measured in fat, protein and starch, not in kilograms. See [food-menu.md](../government/procedures/food-menu.md).

## Dairy

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CHEESE-AGED-Y10-1` | ★ **First rennet-set wheel** · salted · Yule wedges d3509 · d3873 · d4240 · d4609 | **~0.44 kg remain @ wheel** | **Cool dairy shelf, clean reed mat** | d3315 | d4973 feast |
| `GOAT-MILK-CROCK` | Goat milk | ~0.20 L | Ice vault niche | d3260 | d3260 |
| `WHEY-1` | Whey · ★ **working stock — do not bank it** | **~1.22 L** | Cool step | d3236 | d4806 plaster |

Ricotta off **fresh** whey runs half again the yield of ricotta off stale — the `RICOTTA-Y10-2` row is the control. The year's open cheese question is thistle heads in June, not the procedure, which runs without thought now.

★★ **Whey keeps souring after it leaves the curd, so run ricotta the same day as the cheese.** Acid whey gives a poor ricotta yield and sweet rennet whey gives far more, and the difference is measured in hours, not days. Old whey is not waste — it goes to the retarder jar, the goats, or the soil.

⚑ **`CHEESE-AGED-Y10-1`: turn DAILY until the rind is dry and firm, then return to `CAVE-3` and turn twice weekly. Wax only after the rind is established.** *The cave shelf tested too wet for the initial dry stage; its temperature remains excellent for later ageing.*

★ **Whey is a plaster retarder.** Gauging with whey roughly doubles working time, to about 25 minutes. That is the difference between a wall you can finish and one that goes off in the bucket.

## Cured and dried

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `SOAP-Y10-1` | Soap bars · rosemary–thyme · **×4 culina · ×5 thermae · ×4 chem lab** | **×13 bars** | Service pegs *(retcon d4598)* | d3452 | d4598 |
| `DEER-TALLOW-Y10-1` | Deer tallow · rendered separate — candles and the wax-rosin pot | **~0.302 kg** | Lamp jar · culina | d3251 | d5257 lamp |
| **`DEER-TALLOW-Y12-1`** | Deer tallow · **`DEER-HUNT-Y12-3795`** · autumn render | **~5.62 kg** | Horreum cool step jar | d3795 | d5030 apron |

⚠ **Not sealed is deliberate.** Sealing jerky while it still breathes is how you find mould. `JERKY-Y10` was made **to a number** — weighed wet, dried to ~⅔ loss with no plateau, then cut and checked dry through rather than judged by feel.

☠ **Deer tallow is rendered well away from the drying rack and never stored near it.** Fat on drying meat is how a batch spoils.

## Oil

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`OIL-Y13-1`** | Olive oil, clear · **cook live** | **~1.045 L** | Glass bottles · working draw ~240 ml @ `P-ξ-5` | d4218 | d4740 hinge wipe |
| **`OIL-SEDIMENT-Y13-1`** | Olive oil sediment, sealed | **~145 ml** | `AMPHORA-6` foot | d4222 | d4222 |
| **`OIL-Y12-1`** | Olive oil, clear · **cook live** | **~920 ml** | Glass bottles · working draw ~280 ml @ `P-ξ-5` | d3850 | d3914 |
| **`OIL-SEDIMENT-Y12-1`** | Olive oil sediment, sealed | **~150 ml** | `AMPHORA-6` foot | d3854 | d3854 |
| `OIL-Y10-1` | Olive oil, clear · **cook live** | ~1.12 L | Glass bottles · working draw ~320 ml at `P-ξ-5` | d3479 | d3509 |
| `OIL-Y9-1` | Olive oil, clear · **cook live** | ~1.03 L | Glass bottles · working draw ~390 ml at `P-ξ-5` | d3117 | d3452 |
| `OIL-SEDIMENT-Y10` | Olive oil sediment, sealed | ~125 ml | `AMPHORA-6` foot | d3490 | d3490 |
| `OIL-SEDIMENT-Y9` | Olive oil sediment, sealed | ~170 ml | `AMPHORA-6` foot | d3126 | d3126 |
| `OIL-SEDIMENT-Y8` | Olive oil sediment, sealed | ~165 ml | `AMPHORA-6` foot | d2760 | d2760 |

`Made` is the **press** date, not the decant — the clock starts when the fruit is crushed. Cool, dark and full is what keeps it; headroom air is what ruins it. Sediment stays sealed at the amphora foot and is never stored with the clear, which is why the clear keeps a year. See `OLIVE-PRESS` in [processing.md](../government/procedures/processing.md).

## Vinegar and ferment

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `GRAPE-VINEGAR-Y9-1` | Grape vinegar · Y9 fork · merged to `VINEGAR-Y6-1` | ~2.15 L rack | `AMPHORA-5` | d3475 | d3475 |
| `GRAPE-MUST-Y7-1` | Grape must, matured · vinegar-ready | **~1.24 L** | Horreum | Y7 | d4609 |
| `VINEGAR-Y6-1` | Vinegar · Y6/Y7/Y8/Y9 bands merged · **~5.8 % acetic class d5042** | **~2.72 L class** | `AMPHORA-5` · `P-ξ-4` · crock | Y6 | d5042 assay |
| `VINEGAR-MOTHER-1` | Vinegar mother + mat | ~200 ml | Crock | live | d2704 |
| **`SPIRIT-GRAIN-Y16-1`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y16-1`** | **~0.30 L @ spirit peg** | Chem spirit peg | d5193 | d5223 dehyd |
| **`SPIRIT-GRAIN-Y13-1`** | Grain spirit · hearts cut · **~42 % class** · emmer/barley mash | **~0.83 L @ `P-LAB-SPIRIT-BOTTLE-1`** | Chem spirit peg | d3926 | d4624 dehyd |
| **`SPIRIT-GRAIN-Y15-1`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y15-1`** | **~0.85 L @ `P-LAB-SPIRIT-BOTTLE-Y15-1`** | Chem spirit peg | d4905 | d5116 dehyd |
| **`SPIRIT-GRAIN-Y15-2`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y15-2`** | **~1.06 L @ spirit peg** | Chem spirit peg | d4971 | d5090 dehyd |
| **`SPIRIT-GRAIN-Y14-1`** | Grain spirit · hearts cut · **~42 % v/v @ 14 °C SG d5042** · **`GRAIN-FERMENT-Y14-1`** | **~1.83 L @ `P-LAB-SPIRIT-BOTTLE-Y14-1`** · peg **empty** | Chem spirit peg | d4625 | d5042 assay |
| **`SPIRIT-GRAIN-Y13-2`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y13-2` batch** | **~2.95 L @ spirit peg** | Chem spirit peg | d4257 | d4257 |

Dehyd stock: **`ETHANOL-DEHYD-STOCK-1`** @ [resources.md — Alcohol · ethanol organics pathway](resources.md#alcohol--ethanol-organics-pathway).

Closed mash batches **`GRAIN-FERMENT-Y13-2` … `Y16-1`** → journal + matching **`SPIRIT-GRAIN-*`** rows above.

## Olives in brine

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `OLIVE-BRINE-Y10-1` | Olive, brined · 6–18 mo band | **~1.18 kg fruit** | Crock #2, v1 porch | d3480 | d3872 |
| **`OIL-Y15-1`** | Olive oil, clear · Y15 lap 1 · **cook live** | **~0.53 L** @ glass rack · **~240 ml @ `P-ξ-5`** | d4945 | d4973 roast |
| **`OIL-SEDIMENT-Y15-1`** | Olive oil sediment, sealed | **~125 ml** | `AMPHORA-6` foot | d4953 | d4953 |
| **`OIL-Y15-2`** | Olive oil, crude · Y15 lap 2 · settling | **~0.59 L** @ glass settle jar · cool lip | d4954 | d5308 rack |
| **`OIL-Y16-1`** | Olive oil, crude · Y16 laps 1–3 crush | **~1.75 L** @ `AMPHORA-6` cool-step | d5308 | d5308 press |
| **`OLIVE-BRINE-Y15-1`** | Olive, brined · snack jar · 6–18 mo band | **~0.39 kg fruit** | **`OLIVE-JAR-Y15-1` · v1 porch** | d4954 | d4964 feast tray |
| **`OIL-Y14-1`** | Olive oil, clear · Y14 laps 1–3 · **decant ✓ d4593** | **~1.03 L** @ glass rack · **~280 ml @ `P-ξ-5`** | d4580 | d4617 cover wipe |
| **`OLIVE-BRINE-Y14-1`** | Olive, brined · snack jar · 6–18 mo band | **~1.29 kg fruit** | **`OLIVE-JAR-Y14-1` · v1 porch** | d4576 | d4592 |

The 6–18 month band is the one real keep window in this file. Y6 is well past it and should be read before it is relied on.

## Salt and spice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `SALT-1` | Salt | **~8.05 kg @ larder** · **~1.0 kg @ `CAVE-RECOVERY-CRATE-1`** | Larder / cave | | d5284 brine top |
| `SPICE-MU-10` | Spice | — | `P-μ-10`, horreum A margin | | — |
| `MINT-CROCK-1` | Mint | — | Crock | | d3175 |

Salt is the one indefinite row. **`SALT-EVAP` band OPEN** (6 Nov – 26 Nov) · **cycle 2 harvest ✓ d4578 · optional pour #3**.

## Ice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ICE-VAULT-STOCK` | Ice, hard class | **~115.0 kg** | Ice vault | CY14 peak · cap | d5285 coupling |

Stock here, plant in [infrastructure.md](infrastructure.md) — `ICE-VAULT-NICHE-2` and `COLD-CELLAR-FAN-1`.

## Herbs

Dried herbs are food and belong here. Standing herbs are [crops.md](crops.md); herb seed is [seed-vault.md](seed-vault.md). Y9 herb stock went to the ground on d3219 — reserves only, listed in the vault.

Spent batches and **d4958** spoilage tails are **not** listed here — see [index.md](index.md) retirement rule and the journal.
