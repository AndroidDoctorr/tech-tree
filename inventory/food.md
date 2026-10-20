# Food

Edible stock. Its own file because nearly every row carries a date, which is the opposite of [resources.md](resources.md) where nearly none do.

`| ID | Item | Qty | Where | Made | Last |`

**`Made` is close to mandatory here.** Blank means genuinely indefinite — salt. `?` means the date was lost in the v1 format and should be set at the next audit. Keep windows live once in [processing.md](../government/procedures/processing.md) and [food-menu.md](../government/procedures/food-menu.md), never on the row.

No expiry column. Date plus rule gives the answer on read, and a better keep window is then one edit instead of forty.

## Grain and meal

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`EMMER-BULK-Y15`** | Emmer, bulk · Y15 harvest · graded | **×0** *(sown d5040)* | — | d4949 | d5040 sow |
| **`PARCH-EMMER-Y15-1`** | Emmer, parched · quick-cook stash | **~1.18 kg** | Horreum quick-cook peg | d4950 | d4972 mash |
| **`BARLEY-BULK-Y15`** | Barley, bulk · Y15 expanded trial · graded | **×0** *(sown d5040)* | — | d4949 | d5040 sow |
| **`EMMER-BULK-Y14`** | Emmer, bulk · Y14 harvest · graded | **~0.28 kg** | Horreum A main bay | d4584 | d5040 sow backup |
| **`EMMER-BULK-Y13`** | Emmer, bulk · Y13 harvest · graded | **~0.19 kg** | Horreum A main bay | d4217 | d4595 |
| **`BARLEY-BULK-Y14`** | Barley, bulk · Y14 trial · graded | **~0.21 kg** | Horreum A barley bay | d4584 | d5040 sow backup |
| **`BARLEY-BULK-Y13`** | Barley, bulk · Y13 trial · graded | **~0.24 kg** | Horreum A barley bay | d4217 | d4595 |
| **`P-17-LENTIL-Y13`** | Lentil · Y13 harvest · graded | **~143 g** | Horreum A pulse bay | d4217 | d4221 |
| **`P-18-CHICKPEA-Y13`** | Chickpea · Y13 harvest · graded | **~201 g** | Horreum A pulse bay | d4218 | d4221 |
| **`PARCHED-MU-13-Y13-1`** | Parched emmer · Y13 sprint refresh | **~0.52 kg** | Horreum snack jar `P-μ-12` | d4221 | d4221 |
| **`PARCHED-MU-14-Y14-1`** | Parched emmer · Y14 sprint refresh | **~0.36 kg** | Horreum snack jar `P-μ-12` | d4589 | d4608 |
| **`STEW-Y13-JAR-4221`** | Pulse + emmer stew jar | **×0** | — | d4221 | d4958 spoilage |
| **`STEW-Y14-JAR-4589`** | Pulse + emmer stew jar · Y14 sprint | **×0** | — | d4589 | d4958 spoilage |
| **`BARLEY-BULK-Y12`** | Barley, bulk · Y12 trial harvest | **~0.51 kg** | Horreum A barley bay | d3849 | d3849 |
| `BARLEY-BULK-Y10` | Barley, bulk · Y10 trial harvest | ~0.48 kg | Horreum A barley bay | d3491 | d3491 |
| **`EMMER-BULK-Y12`** | Emmer, bulk · Y12 harvest | **~0.58 kg** | Horreum A `EMMER-BULK-Y12` incoming bay | d3849 | d4257 |
| `EMMER-BULK-Y10` | Emmer, bulk · Y10 harvest | ~1.11 kg | Horreum A, `EMMER-BULK-Y10` incoming bay | d3485 | d3576 |
| `EMMER-BULK-Y9` | Emmer, bulk · Y9 tail | **×0** | — | Y9 | d4958 spoilage |
| **`PARCHED-MU-12-Y12-1`** | Parched emmer · Y12 refresh | **×0 · spent Y13 sprint** | — | d3854 | d4221 |
| `PARCHED-MU-12` | Parched emmer · green · Y10 refresh | **×0 → `PEMMICAN-Y12-1` + M31 pack** | — | d3489 | d3591 |
| `PARCHED-WILD-GRAIN-Y12-1` | Parched wild mix · **`P-05` einkorn + `P-06` barley** · Y12–Y14 food laps | **~1.99 kg** | Horreum snack jar | d3685 | d4595 |
| **`GRAIN-WILD-FOOD-Y15-1`** | Wild einkorn + barley · clean · Y15 food lap · **spent @ ferment** | **×0** | — | d4778 | d4779 ferment |
| `BARREL-4-GRAIN` | Cracked grain, working · v1 tap | **~0.58 kg** | `BARREL-4`, v1 | d4589 | d4956 stew |
| `STARTER-Y6-1` | Sourdough starter, emmer · **daily feed** | — | Culina warm peg | d2041 | live |

`STARTER-Y6-1` is the only row in the inventory that dies if ignored for a week. Feeding it is a [daily.md](../checklists/daily.md) concern, not a stock concern.

## Pulse

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FAVA-BRINE-Y12-1` | Fava, short brine · tender tail | **~0.72 kg** | Crock #3 cool step | d3704 | d3704 |
| `FAVA-DRY-Y12-FOOD-1` | Fava, dry food · blanch + rack finish · **not seed bank** | **~3.18 kg** | Horreum A pulse bay | d3704 | d3704 |
| `FAVA-PARCHED-Y12-1` | Fava, parched · trail / snack | **~0.54 kg** | Horreum snack jar | d3704 | d3704 |
| `HUMMUS-Y10-1` | Hummus · chickpea · oil · garlic | **×0** | — | d3492 | d4958 spoilage |
| `P-18-CHICKPEA-Y10` | Chickpea · Y10 harvest | ~48 g | Horreum A pulse bay | d3491 | d3492 |
| **`P-18-CHICKPEA-Y12`** | Chickpea · Y12 harvest | **~201 g** | Horreum A pulse bay | d3851 | d3854 |
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
| `PISTACHIO-1` | Pistachio kernels · roast tray class | **~9.54 kg** | Horreum A nut tray | Y10–Y15 | d4964 feast tray |
| **`PISTACHIO-HULL-Y13-1`** | Pistachio hull-on drying · **`P-01` primary Y13** | **✓ spent d4174** | — | d4135 | d4174 |
| **`PISTACHIO-HULL-Y14-1`** | Pistachio hull-on drying · **`P-01` primary Y14 d4499** | **✓ spent d4945** | — | d4499 | d4945 shell+roast |
| **`PISTACHIO-HULL-Y15-1`** | Pistachio hull-on drying · **`P-01` primary Y15 d4875** | **✓ spent d4947** | — | d4875 | d4947 shell+roast |
| `ACORN-ROAST-Y9` | Acorn, shelled and roast · Y9 batches ×3 | **~0.66 kg** | Nut tray | Y9 | d3591 |
| `ACORN-ROAST-Y10-1` | Acorn roast · **`ACORN-LEACH-Y10-1` batch** | ~575 g | Nut tray | d3423 | d3508 |
| `ACORN-ROAST-Y10-2` | Acorn roast · **`ACORN-LEACH-Y10-2` batch** | ~610 g | Nut tray | d3465 | d3465 |
| `ACORN-ROAST-Y10-3` | Acorn roast · **`ACORN-LEACH-Y10-3` batch** | ~605 g | Nut tray | d3471 | d3471 |
| `ACORN-ROAST-Y10-4` | Acorn roast · **`ACORN-LEACH-Y10-4` batch** | ~600 g | Nut tray | d3478 | d3478 |
| **`ACORN-ROAST-Y12-1`** | Acorn roast · **`ACORN-LEACH-Y12-1` batch** | **~575 g** | Nut tray | d3787 | d3872 |
| **`ACORN-ROAST-Y13-1`** | Acorn roast · **`ACORN-LEACH-Y13-1` batch** | **~605 g** | Nut tray | d4236 | d4236 |
| **`ACORN-ROAST-Y13-2`** | Acorn roast · **`ACORN-LEACH-Y13-2` batch** | **~600 g** | Nut tray | d4236 | d4236 |
| **`ACORN-DRY-Y13-1`** | Acorn leached · batch 1 PASS · **✓ roast d4236** | **×0** | — | d4226 | d4236 |
| **`ACORN-DRY-Y13-2`** | Acorn leached · batch 2 PASS · **✓ roast d4236** | **×0** | — | d4228 | d4236 |
| `ACORN-SHELL-ON` | Acorn, bulk shell-on | **~19.8 kg** | **`NUT-SHELF-EXT-1` west lip** | **Y15 lap 3 d4876** | d4877 shell |
| **`ACORN-LEACH-Y14-1`** | Acorn leach · Y14 batch 1 · **soak 4 ⧗ @ ditch W** | **~680 g in sack** | Ditch W flow | d4530 | flow PASS |
| **`ACORN-LEACH-Y15-1`** | Acorn leach · Y15 batch 1 · **✓ PULLED d5033** | **×0** | — | d4877 | d5033 |
| **`ACORN-DRY-Y15-1`** | Acorn, leached · dry before roast | **~710 g wet** | Porch dry tray | d5033 | dry read |

Roast acorn wants 1–3 months of dry before it settles. Leaching is `ACORN-LEACH` in [processing.md](../government/procedures/processing.md); the troughs are [infrastructure.md](infrastructure.md).

## Honey

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| **`HONEY-STRAINED-Y13-1`** | Strained honey · pale-bar crush-strain | **~0.56 kg** | **`GLASS-BOTTLE-11` @ culina shelf** | d4726 + d4796 retcon | d4972 fritters |

*Co-harvested with **`WAX-CUT-SURPLUS`** on strong hives — not brood comb. See [apiary-routine.md](../government/procedures/apiary-routine.md).*

**`FIG-NEWTON` standard fill (going forward):** fig paste from fresh + leather as available · **`HONEY-STRAINED-Y13-1` ~3 g / unit** · emmer + oil dough — same bake grammar as **d4841**.

## Fruit

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `FIG-LEATHER-1` | Fig leather, rolled | **×0** | — | ? | d4958 spoilage |
| `FIG-LEATHER-TRAY-Y10-1` | Fig leather, tray drying | **×0** | — | d3368 | d4958 spoilage |
| `FIG-FRESH-Y10-1` | Fig, fresh hold · Bed D first pass | **×0** | — | d3368 | d4958 spoilage |
| `FIG-FRESH-Y10-2` | Fig, fresh · Bed D second pass | **×0** | — | d3375 | d4958 spoilage |
| `FIG-FRESH-Y13-1` | Fig fresh · Bed D pick d4098 | **×0** | — | d4098 | d4958 spoilage |
| `FIG-LEATHER-Y13-1` | Fig leather tray · sun dry | **×0** | — | d4098 | d4958 spoilage |
| **`FIG-FRESH-Y14-1`** | Fig fresh · Bed D repeat | **×0** | — | d4469 | d4958 spoilage |
| **`FIG-LEATHER-Y14-1`** | Fig leather tray · sun dry | **~2.15 kg gross wet** | **`W-1` / east rack** | d4469 | d4474 tray |
| **`FIG-FRESH-Y15-1`** | Fig fresh · Bed D Y15 pass + repeat | **~0.45 kg** | Cool step | d4839 | d4841 repeat |
| **`FIG-FRESH-Y15-2`** | Fig fresh · Bed D Y15 band tail | **~0.35 kg** | Cool step | d4875 | d4875 tail |
| **`FIG-LEATHER-Y15-1`** | Fig leather tray · sun dry | **~0.84 kg gross wet** | Horreum east rack | d4839 | d4964 feast tray |
| **`FIG-LEATHER-Y15-2`** | Fig leather tray · tail lap | **~0.12 kg gross wet** | Horreum east rack | d4875 | dry |
| **`FIG-NEWTON-Y15-1`** | Fig newton · emmer shell · **fig + honey fill** | **×12 · ~315 g net** | **`PORC-PLATE-2` @ cool step** | d4841 | d4972 plate |
| `GRAPE-FRESH-Y13-1` | Grape, fresh · P-03 partial strip d4099 | **×0** | — | d4099 | d4958 spoilage |
| **`GRAPE-FRESH-Y14-1`** | Grape, fresh · P-03 partial strip d4488 | **×0** | — | d4488 | d4958 spoilage |
| `FIG-FRESH-Y12-1` | Fig fresh · Bed D pick d3745 | ×0 spent | — | d3745 | d3872 |
| `FIG-LEATHER-Y12-1` | Fig leather tray · sun dry | ×0 dry | Horreum east rack | d3745 | d3872 |
| `GRAPE-FRESH-Y10-1` | Grape, fresh · P-03 partial strip | ×0 spent | — | d3375 | d3579 |
| `GRAPE-FRESH-1` | Grape, fresh hold | ×0 spent | — | Y9 | d3872 |

## Meat and fish

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `DEER-SMOKE-Y10-1` | Smoked deer | **×0** | — | d3253 | d4958 spoilage |
| `FISH-SMOKE-1` | Smoked fish | **~2.31 kg** | Smoke rack, pool | ? | d4973 feast |
| `GOOSE-SMOKE-Y10-1` | Smoked goose · Y10 Yule hunt remainder | **×0** | — | d3509 | d4958 spoilage |
| **`GOOSE-SMOKE-Y15-1`** | Smoked goose · Y15 Yule hunt remainder | **~0.98 kg** | Horreum A smoke shelf | d4973 | d4973 hunt |
| **`GOOSE-SMOKE-Y13-1`** | Smoked goose · Y13 Yule hunt remainder | **~0.85 kg** | Horreum A smoke shelf | d4240 | d4973 feast |
| **`GOOSE-SMOKE-Y14-1`** | Smoked goose · Y14 Yule hunt remainder | **~0.96 kg** | Horreum A smoke shelf | d4609 | d4609 |
| `GOOSE-SMOKE-1` | Smoked goose · Y9 tail | **×0** | — | ? | d4958 spoilage |
| `GOOSE-GIBLET-JAR` | Goose giblets, jarred | **×0** | — | ? | d4958 spoilage |
| **`STEW-Y12-JAR-3854`** | Stew jar, Y12 · lentil–chickpea–emmer | **×0** | — | d3854 | d4958 spoilage |
| `STEW-Y10-JAR` | Stew jar, Y10 · lentil–emmer | **×0** | — | d3489 | d4958 spoilage |
| `STEW-Y9-JAR` | Stew jar, Y9 | **×0** | — | Y9 | d4958 spoilage |
| `STEW-Y8-JAR` | Stew jar, Y8 · tail | **×0** | — | Y8 | d4958 spoilage |
| `RED-STAG-Y10-1` | Red stag carcass · **bone sorted d4958** | **×0** | — | d3269 | d4958 → bone bank |
| **`DEER-FRESH-Y12-1`** | Red deer · eat-first cuts | **×0** | — | d3796 | d4958 reconcile |
| **`DEER-JERKY-Y12-1`** | Red deer jerky · scale-dried batch | **~4.8 kg** | Horreum snack jar | d3798 | d3798 |
| **`DEER-SMOKE-Y12-1`** | Red deer · cold-smoke Y12 | **~14.60 kg** | Horreum A smoke shelf | d3797 | d4973 feast |
| **`BOAR-CARCASS-Y15-1`** | Wild boar · field-dressed whole | **×0** | d4911 | d4912 butcher |
| **`BOAR-ORGANS-Y15-1`** | Heart · liver · trim | **~0.4 kg** stew tail | d4911 | d4912 |
| **`BOAR-FRESH-Y15-1`** | Wild boar · eat-first cuts | **~0.35 kg** tail | Ice-vault step | d4912 | d4913 spit |
| **`BOAR-FAT-WET-Y15-1`** | Trim fat · pre-render | **×0** | d4911 | d4912 render |
| **`BOAR-TALLOW-Y15-1`** | Wild boar tallow · rendered | **~1.82 kg** | Horreum cool step jar | d4912 | d4913 trace |
| **`BOAR-PRIMAL-SMOKE-Y15-1`** | Primals · salted · wet smoke queue | **×0** | d4912 | d4913 smoke |
| **`BOAR-JERKY-WET-Y15-1`** | Jerky strips · porch line | **×0** | d4912 | d4913 dry |
| **`BOAR-JERKY-Y15-1`** | Wild boar jerky | **~4.7 kg** | Horreum snack jar | d4913 | d4913 |
| **`BOAR-SMOKE-Y15-1`** | Wild boar · cold-smoke | **~7.15 kg** | Horreum A smoke shelf | d4913 | d4964 belly carve |
| **`BOAR-BELLY-RASHERS-Y15-1`** | Boar-belly rashers · crisp · Yule menu | **~140 g** @ cool step | Cool step tail | d4972 | d4973 feast |
| **`HONEY-FRITTERS-Y15-1`** | Honey fritters · emmer batter · hot-hold | **×8 · ~140 g** tail | Domus ante | d4972 | d4973 feast |
| **`EMMER-YEAST-BREAD-Y15-4972`** | Feast loaf · starter | **~330 g** tail @ board | Culina board | d4972 | d4973 feast |
| **`YULE-FEAST-TRAY-Y15-1`** | Dry feast portion · domus ante | staged | Domus ante | d4964 | eat Yule |
| **`POSCA-BATCH-Y15-4964`** | Posca · vinegar batch | **~0.4 L** | Culina crock | d4964 | d4964 |
| **`FRITTER-JAR-Y15-1`** | Fritter dry mix · emmer + salt | **×0 spent** | — | d4964 | d4972 fry |

★ **Y12/Y15 smoke + jerky banks** are the live protein shelf after **d4958 spoilage pass**.

⚠ **`RED-STAG-Y10-1` rendered only ~1.4 kg of tallow** — a fraction of an autumn deer. It was a velvet stag and spring-lean. **Autumn deer are the fat deer**, which is why pemmican is an autumn job and not a spring one: a pack is measured in fat, protein and starch, not in kilograms. See [food-menu.md](../government/procedures/food-menu.md).

## Dairy

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `CHEESE-AGED-Y10-1` | ★ **First rennet-set wheel** · salted · Yule wedges d3509 · d3873 · d4240 · d4609 | **~0.44 kg remain @ wheel** | **Cool dairy shelf, clean reed mat** | d3315 | d4973 feast |
| `CHEESE-Y10-10` | Cheese | **×0** | — | d3260 | d4958 spoilage |
| `CHEESE-Y10-9` | Cheese | **×0** | — | d3260 | d4958 spoilage |
| `RICOTTA-Y10-4` | Ricotta, off fresh whey | **×0** | — | d3260 | d4958 spoilage |
| `RICOTTA-Y10-3` | Ricotta, off fresh whey | **×0** | — | d3260 | d4958 spoilage |
| `RICOTTA-Y10-2` | Ricotta · thin — made on stale whey | **×0** | — | d3260 | d4958 spoilage |
| `CHEESE-Y10-8` | Cheese · clean set, clean break | **×0** | — | d3250 | d4958 spoilage |
| `CHEESE-Y10-7` | Cheese, pressed · acid-set | **×0** | — | d3244 | d4958 spoilage |
| `CHEESE-Y10-6` | Pressed curd · acid-set | **×0** | — | d3236 | d4958 spoilage |
| `GOAT-MILK-CROCK` | Goat milk | ~0.20 L | Ice vault niche | d3260 | d3260 |
| `WHEY-1` | Whey · ★ **working stock — do not bank it** | **~1.22 L** | Cool step | d3236 | d4806 plaster |

Ricotta off **fresh** whey runs half again the yield of ricotta off stale — the `RICOTTA-Y10-2` row is the control. The year's open cheese question is thistle heads in June, not the procedure, which runs without thought now.

★★ **Whey keeps souring after it leaves the curd, so run ricotta the same day as the cheese.** Acid whey gives a poor ricotta yield and sweet rennet whey gives far more, and the difference is measured in hours, not days. Old whey is not waste — it goes to the retarder jar, the goats, or the soil.

⚑ **`CHEESE-AGED-Y10-1`: turn DAILY until the rind is dry and firm, then return to `CAVE-3` and turn twice weekly. Wax only after the rind is established.** *The cave shelf tested too wet for the initial dry stage; its temperature remains excellent for later ageing.*

★ **Whey is a plaster retarder.** Gauging with whey roughly doubles working time, to about 25 minutes. That is the difference between a wall you can finish and one that goes off in the bucket.

## Cured and dried

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `JERKY-Y10` | Jerky · Y10 batch | **×0** | — | d3253 | d4958 spoilage |
| `EXPED-RATION-M31-Y12-RESERVE` | Returned dry scout ration · **spent Trip 1 d3690–3695** | **×0** | Wagon food chest | d3591 | d3695 |
| `GOAT-SMOKE-1` | Smoked goat | **×0** | — | ? | d4958 spoilage |
| `DEER-SMOKE-BATCH` | Smoked deer, earlier batch | **×0** | — | d3128 | d4958 spoilage |
| `TALLOW-KITCHEN` | Tallow, kitchen fat jar | **×0 → `PEMMICAN-Y12-1`** | Culina | | d3591 |
| `SOAP-Y10-1` | Soap bars · rosemary–thyme · **×4 culina · ×5 thermae · ×4 chem lab** | **×13 bars** | Service pegs *(retcon d4598)* | d3452 | d4598 |
| `DEER-TALLOW-Y10-1` | Deer tallow · rendered separate — candles and the wax-rosin pot | **~0.320 kg** | Lamp jar · culina | d3251 | d5034 hoe + lamp |
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
| `OIL-Y8-1` | Olive oil, clear | **×0** | — | d2749 | d4958 rancid |
| `OIL-Y7-1` | Olive oil, clear | **×0** | — | d2408 | d4958 rancid |
| `OIL-Y6-1` | Olive oil, clear | **×0** | — | d2043 | d4958 rancid |
| `OIL-SEDIMENT-Y10` | Olive oil sediment, sealed | ~125 ml | `AMPHORA-6` foot | d3490 | d3490 |
| `OIL-SEDIMENT-Y9` | Olive oil sediment, sealed | ~170 ml | `AMPHORA-6` foot | d3126 | d3126 |
| `OIL-SEDIMENT-Y8` | Olive oil sediment, sealed | ~165 ml | `AMPHORA-6` foot | d2760 | d2760 |

`Made` is the **press** date, not the decant — the clock starts when the fruit is crushed. Cool, dark and full is what keeps it; headroom air is what ruins it. Sediment stays sealed at the amphora foot and is never stored with the clear, which is why the clear keeps a year. See `OLIVE-PRESS` in [processing.md](../government/procedures/processing.md).

## Vinegar and ferment

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `GRAPE-VINEGAR-Y9-1` | Grape vinegar · Y9 fork · merged to `VINEGAR-Y6-1` | ~2.15 L rack | `AMPHORA-5` | d3475 | d3475 |
| `GRAPE-MUST-Y7-1` | Grape must, matured · vinegar-ready | **~1.24 L** | Horreum | Y7 | d4609 |
| `VINEGAR-Y6-1` | Vinegar · Y6/Y7/Y8/Y9 bands merged | ~2.75 L class | `AMPHORA-5` · `P-ξ-4` · crock | Y6 | d3508 |
| `VINEGAR-MOTHER-1` | Vinegar mother + mat | ~200 ml | Crock | live | d2704 |
| **`GRAIN-FERMENT-Y15-1`** | Grain mash ferment · **`GRAIN-WILD-FOOD-Y15-1` · wild lap** · **`BARREL-5`** | **✓ spent d4905 · `GRAIN-DISTILL-Y15-1` CLOSED** | d4779 | d4905 |
| **`GRAIN-FERMENT-Y15-2`** | Grain mash ferment · Y15 barley + emmer tail · **`BARREL-5`** | **✓ spent d4971 · `GRAIN-DISTILL-Y15-2` CLOSED** | — | d4959 | d4971 |
| **`GRAIN-FERMENT-Y14-1`** | Grain mash ferment · wild + tail emmer/barley · **`BARREL-5`** | **✓ spent d4625 · `GRAIN-DISTILL-Y14-1` CLOSED** | d4595 | d4625 |
| **`GRAIN-FERMENT-Y13-2`** | Grain mash ferment · emmer/barley · spirit lane | **✓ spent d4257 · `BARREL-5` in use Y14-1** | Horreum A margin | d4222 | d4257 |
| **`SPIRIT-GRAIN-Y13-1`** | Grain spirit · hearts cut · **~42 % class** · emmer/barley mash | **~0.83 L @ `P-LAB-SPIRIT-BOTTLE-1`** | Chem spirit peg | d3926 | d4624 dehyd |
| **`SPIRIT-GRAIN-Y15-1`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y15-1`** | **~1.20 L @ `P-LAB-SPIRIT-BOTTLE-Y15-1`** · peg **empty** | Chem spirit peg | d4905 | d4933 bottle |
| **`SPIRIT-GRAIN-Y15-2`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y15-2`** | **~1.76 L @ spirit peg** | Chem spirit peg | d4971 | d4973 Yule sip |
| **`SPIRIT-GRAIN-Y14-1`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y14-1`** | **~1.84 L @ `P-LAB-SPIRIT-BOTTLE-Y14-1`** · peg **empty** | Chem spirit peg | d4625 | d4936 bottle |
| **`SPIRIT-GRAIN-Y13-2`** | Grain spirit · hearts cut · **~42 % class** · **`GRAIN-FERMENT-Y13-2` batch** | **~2.95 L @ spirit peg** | Chem spirit peg | d4257 | d4257 |

Dehyd stock: **`ETHANOL-DEHYD-STOCK-1`** @ [resources.md — Alcohol · ethanol organics pathway](resources.md#alcohol--ethanol-organics-pathway).

## Olives in brine

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `OLIVE-BRINE-Y10-1` | Olive, brined · 6–18 mo band | **~1.18 kg fruit** | Crock #2, v1 porch | d3480 | d3872 |
| `OLIVE-BRINE-Y8-1` | Olive, brined · 6–18 mo band | **×0** | — | d2747 | d4958 spoilage |
| `OLIVE-BRINE-Y7-1` | Olive, brined · 6–18 mo band | **×0** | — | d2397 | d4958 spoilage |
| `OLIVE-BRINE-Y6-1` | Olive, brined · 6–18 mo band | **×0** | — | d2056 | d4958 spoilage |
| `OLIVE-BRINE-LEGACY` | Olive brine, P-02 legacy | **×0** | — | ? | d4958 spoilage |
| **`OLIVE-FRUIT-P-02-Y12-1`** | Olive fruit · P-02 laps 1–2 · **processed d3850** | **×0** | — | d3847 | d3850 |
| **`OLIVE-FRUIT-P-02-Y14-1`** | Olive fruit · P-02 lap 1 · **pressed d4580** | **×0** | — | d4576 | d4580 |
| **`OLIVE-FRUIT-P-02-Y15-1`** | Olive fruit · P-02 lap 1 · **pressed d4945** | **×0** | — | d4944 | d4945 |
| **`OIL-Y15-1`** | Olive oil, clear · Y15 lap 1 · **cook live** | **~0.53 L** @ glass rack · **~240 ml @ `P-ξ-5`** | d4945 | d4973 roast |
| **`OIL-SEDIMENT-Y15-1`** | Olive oil sediment, sealed | **~125 ml** | `AMPHORA-6` foot | d4953 | d4953 |
| **`OLIVE-FRUIT-P-02-Y15-2`** | Olive fruit · P-02 lap 2 · **pressed d4954** | **×0** | — | d4953 | d4954 |
| **`OIL-Y15-2`** | Olive oil, crude · Y15 lap 2 · settling | **~0.59 L** @ `AMPHORA-6` cool-step | d4954 | d4954 |
| **`OLIVE-BRINE-Y15-1`** | Olive, brined · snack jar · 6–18 mo band | **~0.39 kg fruit** | **`OLIVE-JAR-Y15-1` · v1 porch** | d4954 | d4964 feast tray |
| **`OIL-Y14-1`** | Olive oil, clear · Y14 laps 1–3 · **decant ✓ d4593** | **~1.03 L** @ glass rack · **~280 ml @ `P-ξ-5`** | d4580 | d4617 cover wipe |
| **`OIL-Y14-1-SEDIMENT`** | Olive oil, crude tail · spent decant | **×0** compost d4594 | d4593 | d4594 |
| **`OLIVE-BRINE-Y14-1`** | Olive, brined · snack jar · 6–18 mo band | **~1.29 kg fruit** | **`OLIVE-JAR-Y14-1` · v1 porch** | d4576 | d4592 |

The 6–18 month band is the one real keep window in this file. Y6 is well past it and should be read before it is relied on.

## Salt and spice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `SALT-1` | Salt | **~10.80 kg @ larder** · **~1.0 kg @ `CAVE-RECOVERY-CRATE-1`** | Larder / cave | | d4954 brine |
| **`BRINE-HOLD-Y13-1`** | Brackish hold · **`SALT-HAUL-Y13-1` d4200** | **×0 spent · poured d4201** | d4200 | d4201 |
| **`BRINE-HOLD-Y14-1`** | Brackish hold · **`SALT-HAUL-Y14-2` d4574** | **×0 spent · poured d4575** | d4574 | d4575 |
| `SPICE-MU-10` | Spice | — | `P-μ-10`, horreum A margin | | — |
| `MINT-CROCK-1` | Mint | — | Crock | | d3175 |

Salt is the one indefinite row. **`SALT-EVAP` band OPEN** (6 Nov – 26 Nov) · **cycle 2 harvest ✓ d4578 · optional pour #3**.

## Ice

| ID | Item | Qty | Where | Made | Last |
|---|---|---|---|---|---|
| `ICE-VAULT-STOCK` | Ice, hard class | **~128.5 kg** | Ice vault | CY14 peak · cap | d5021 stow |

Stock here, plant in [infrastructure.md](infrastructure.md) — `ICE-VAULT-NICHE-2` and `COLD-CELLAR-FAN-1`.

## Herbs

Dried herbs are food and belong here. Standing herbs are [crops.md](crops.md); herb seed is [seed-vault.md](seed-vault.md). Y9 herb stock went to the ground on d3219 — reserves only, listed in the vault.

## Pending port

v1 §Food · seed · ice is ported. Spent process instances — `ACORN-LEACH-Y6-1` through `Y8-6`, the Y5–Y8 stew tails, the Y6–Y9 bread bakes, trail packs — were **not** carried over. They are closed records and they live in the journal.
