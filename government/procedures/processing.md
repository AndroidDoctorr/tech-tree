# Processing procedures

Converting a harvested material into something that stores or works. Collection is [harvest.md](harvest.md); dishes and rations are [food-menu.md](food-menu.md); comb and honey are [bees.md](bees.md).

Same ID prefix as the harvest: `ACORN-GATHER` then `ACORN-SHELL` then `ACORN-LEACH` then `ACORN-ROAST`. New instances take an underscore — `ACORN-ROAST_Y10-1`. Historic instances predate the convention (`ACORN-ROAST-Y8-5`); leave them as filed.

## Cross-cutting doctrine

These four explain most of the failures below. Read them before inventing a new process.

| Rule | Applies to | Learned |
|---|---|---|
| **Hurry seals the surface and strands the middle.** Any process that works from the outside in will, if rushed, set a hard skin over a raw interior — and it will look finished | jerky, tanning, lime, concrete, plaster, carburising | d3250, d3254 |
| **Doneness is a measured number, not a look.** Weigh it, count it, or test it against a threshold | jerky weight loss, rett snap, hive scale, rope lay | d3250, d3253, d3263 |
| **Crystallise by cooling, not by boiling dry.** Boiling to dryness throws everything down together, wanted and unwanted | nitre, salt, any recrystallisation | d3222 |
| **A by-product stream is not a stock.** Whey, rinse water and liquor go off; use them the day they are made | ricotta, leach water | d3254 |

## Index

| ID | Input | Output |
|---|---|---|
| `ACORN-SHELL` · `ACORN-LEACH` · `ACORN-ROAST` | acorn | roast kernels |
| `CHARCOAL-BURN` | cordwood | charcoal |
| `CHEESE-ACID` · `CHEESE-RENNET` · `RICOTTA` | milk, whey | cheese |
| `CLAY-PREP` | raw clay | brick / tile / glass body |
| `FIBRE-BREAK` · `FIBRE-SCUTCH` · `FIBRE-HECKLE` | retted stalk | line and tow |
| `FIG-LEATHER` | fig | leather rolls |
| `FLAX-RETT` · `HEMP-RETT` | stalk | retted stalk |
| `GRAIN-THRESH` · `GRAIN-WINNOW` · `GRAIN-PARCH` | sheaf | clean and parched grain |
| `GRAPE-MUST` · `GRAPE-FERMENT` · `VINEGAR-MOTHER` | grape | must, vinegar |
| `LIME-BURN` · `PLASTER-CALCINE` · `POZZ-PREP` | limestone, gypsum | quicklime, plaster, cement |
| `MADDER-PREP` · `MADDER-BATH` | madder root | red dye |
| `NITRE-BOIL` | bed earth | saltpetre |
| `OLIVE-BRINE` · `OLIVE-PRESS` · `OIL-DECANT` | olive | table olives, oil |
| `ORE-ROAST` · `ORE-LEACH` | ore | oxide, liquor |
| `PISTACHIO-DRY` · `PISTACHIO-SHELL` | hull-on nuts | kernels |
| `RENNET-PREP` | dried cardoon heads | rennet liquor |
| `SALT-EVAP` | brackish water | salt |
| `TALLOW-RENDER` · `JERKY-DRY` · `PEMMICAN-MAKE` · `MEAT-SMOKE` | carcass | stored food |
| `TAN-BARK` | hide | leather |
| `WAX-RENDER` | comb | wax cakes |
| `WOAD-EXTRACT` · `WOAD-VAT` | woad leaf | indigo pigment, blue dye |

## Acorn

### `ACORN-SHELL`

Stone tap, cap split, float cull, reject worm and stain to the ditch lip. Batches run ~660–670 g kernels.

### `ACORN-LEACH`

`ACORN-LEACH-TROUGH-1/2` at the pool margin. Tannin is water-soluble; the whole job is getting water to it and taking the water away.

**Two levers decide how long this takes, and both have been left on the table.**

- **Break the kernel first.** Tannin leaves from the surface inward, so a whole kernel leaches from its skin and a coarse-crushed one leaches from everywhere at once. Crushing to grit or meal turns a week into a day or two. Crack them before the first soak, not after the last.
- **Use the ditch, not a still trough.** Running water carries tannin away continuously; a still soak reaches equilibrium and then stops working until it is changed. A porous sack pegged in the flow does the whole job unattended and does it faster than serial soaks ever will. The still troughs remain the fallback for a batch that cannot be watched.

Standing method where the ditch is unavailable: **cold water, ~24 h per soak**, drain, rinse, refill. Four soaks for crushed meal; whole kernels take substantially longer.

- **Test by bite, every soak.** Typical arc is bitter, falling, borderline, PASS.
- **Borderline is not PASS.** A batch pulled at borderline goes back in, not to the roast.
- **Cold, not hot.** Hot leaching is faster but it gelatinises the starch, which ruins the meal for flour. Hot-leached acorn can be eaten whole and cannot be baked with.
- **Dry promptly after PASS.** Wet leached meal sours in a day.

**Failure — the stale leach.** A soak left unattended for days goes sour and puts a bitter edge back into kernels that were nearly clean. Dump, triple-rinse, and **restart from soak 1**. It does not resume. *(d2055)*

### `ACORN-ROAST`

Dry on `DRY-TRAY-1/2` at the porch after PASS, then roast. ~620 g per batch from ~660 g dried. Roast keeps 1–3 months dry on the nut tray; bulk shell-on keeps far longer in `WOOD-CRATE-4`, so shell only what the leach can take.

## Fibre

### `FLAX-RETT` · `HEMP-RETT`

`RETT-TROUGH-FLAX-1` north and `RETT-TROUGH-HEMP-1` south at ditch W — clay-pitch lined, drain plug, rinse branch.

- Load submerged. **~10–14 day class** to the pull window, hemp often longer.
- **Pull gate is a reading, not a date:** snap test ×3, smell, day count — run inline on the weekly farm pass, `RETT-READ` in [periodic.md](../../checklists/periodic.md).
- Snap PASS → pull that pass. A borderline thick butt is an AMBER go for breaking.
- Wet bundle → **W-1 north rafter** dry queue. Pool rinse, bars reset, load the next bundle when the pool clears.
- **Over-rett is the one failure with no recovery** — the fibre itself rots. The snap and smell are the guards, which is why this is a state trigger and not an interval.
- A long dry spell can strand a bundle mid-process; `DRY-LEVELS` in [triggers.md](../../checklists/triggers.md) catches it.

### `FIBRE-BREAK` · `FIBRE-SCUTCH` · `FIBRE-HECKLE`

Break mat at W-1 / storage wing north, iron heckle, straw to mulch. Roughly ~6.8 kg wet → ~5.0 kg dry stalk → ~1 kg line plus ~35 g tow.

Yarn consistency, not rope technique, is the limit on rope strength — uneven hand-spun yarn breaks low. Tune the wheel before a big fibre lap, not after.

## Grain

### `GRAIN-THRESH` · `GRAIN-WINNOW`

Thresh at `THRESH-ZONE-1`, winnow into a light west wind at the winnow lane over `WINNOW-SHEET-1`. Elite last, on clean cloth.

### `GRAIN-PARCH`

The shelf-life sprint. Parched emmer to `P-μ-12`; working grain cracked by hand into `BARREL-4` and topped up from the bulk bays. Horreum A holds bulk by year and tag.

## Olive

### `OLIVE-BRINE`

Table-class fruit only, never press grade. Crock at the v1 porch, salt water topped up, weighted down. **6–18 month band.** One crock per year, tagged.

### `OLIVE-PRESS` · `OIL-DECANT`

- **Crush with the stones in.** The pit fragments open the flesh and give the mat something to drain through; pitted olives press to a paste that holds its oil.
- Cold press at `OLIVE-PRESS-1`, mash basket ~3–4 kg per load, multiple loads. Pomace to the compost margin.
- Yield runs ~1.7 L crude from ~11.8 kg fruit, ~2.2 L from ~15.6 kg.
- **What comes off the press is mostly water.** An olive is roughly half vegetation water and a fifth oil, so the run is a bitter dark liquor with oil floating on it. Let it stand and **draw the oil off the top** — the water beneath is amurca and it is the thing that spoils stored oil. Separating it is not optional tidying, it is the difference between oil that keeps a year and oil that goes foul by spring.
- Amurca is worth keeping separately: it is a usable weedkiller, a leather dressing and a wood preservative.
- Crude then sits at the `AMPHORA-6` foot through the **1–10 Dec settle band** to drop its fines. Draw the clear off to glass and `P-ξ-5`; leave the sediment sealed at the amphora foot.
- **Do not draw early**, and do not store oil on its own lees — settling twice is why the clear stock keeps.
- Keep it **cool and dark and full**. Heat, light and headroom air are what turn good oil rancid, in that order.

## Nuts

### `PISTACHIO-DRY` · `PISTACHIO-SHELL`

Dry hull-on ~10–14 days at the porch mat. Shell gate is a firm hull snap. Thumb shell to the horreum nut tray. ~4 kg hull-on gives ~1.9 kg kernels.

## Dye

### `WOAD-EXTRACT` · `WOAD-VAT`

The leaf does not contain indigo. It contains a colourless precursor, and every step below is about converting it without destroying it.

**Fresh leaf, same day.** The precursor degrades as the leaf wilts, so a pull that sits is a pull that lost most of its value. Drying is a **storage** route, not a shortcut — dried leaf has to be milled and then **couched**, left damp and turned for weeks to ferment, before it is worth anything. Where the leaf can be worked the day it is pulled, work it the day it is pulled.

**`WOAD-EXTRACT` — fresh leaf to pigment**

1. Steep shredded fresh leaf in **hot but not boiling** water — hand-hot to steaming, never a rolling boil. Boiling destroys the precursor outright.
2. Steep ~1 h, strain the leaf out and discard it. The liquor is yellow-green and looks wrong; it is correct.
3. Make it alkaline with kelp-ash lye.
4. **Aerate hard** — whisk, or pour it repeatedly between two vessels, until the liquor turns and a blue froth rises. This is the step that makes indigo, and it is pure mechanical work.
5. Let the pigment settle out, pour off the spent liquor, keep the blue sludge. Dried, it stores indefinitely.

**`WOAD-VAT` — pigment to cloth**

Indigo pigment is insoluble, so the vat has to **reduce** it back to a soluble form before it will touch fibre.

- `WOAD-VAT-1`: pigment, kelp-ash lye for alkalinity, **bran reduction** with emmer sweepings, kept warm. The surface going coppery-green with a blue sheen means the vat is ready. Skip the reduction and the vat simply will not dye.
- Dip ~8 s, then **oxidise on the line ~2 h**. It comes out of the pot yellow and turns blue in the air. Many short dips build a deeper, faster colour than one long one.
- Keep air out of the vat itself between dips — the reduction is what you are paying for, and stirring air in spends it.
- Woad **flower** is not woad **leaf**; the flower has nothing to do with this.

No mordant is needed. Indigo is a vat dye and fixes mechanically inside the fibre — the alum is for the madder, not for this.

### `MADDER-PREP` · `MADDER-BATH`

Wash, dry, store on the chem shelf. Alum mordant, then ~58 g crushed dry root simmered ~90 minutes gives the burgundy class. Overdyeing with woad gives the merlot recipe.

## Nitre and salt

### `NITRE-BOIL`

The bed is the slow half and lives in `NITRE-TURN`; this is the autumn conversion.

1. Leach the earth.
2. Filter through linen and sand.
3. **Wood-ash potash swap** — trades calcium for potassium. The calcium drops out as chalk and is filtered off.
4. Boil down. **Skim the salt while it is hot.**
5. **Crystallise the nitre as it cools.**
6. Recharge the bed.

**Why hot then cold, which is the whole trick.** Common salt is about as soluble in boiling water as in cold — so as the liquor concentrates, salt falls out *hot* and can be skimmed off the boil. Nitre is the opposite: far more soluble hot than cold. So it stays in solution through the boil and drops out only as the pot cools. **Salt comes out hot, nitre comes out cold**, and that gap is the entire separation.

**Failure — boiling to dryness.** It throws nitre and salt down together, undoing the separation, and scorches the batch. Stop short and let the cooling do the work. *(d3222)*

Re-dissolve and re-cool a poor batch to purify it further; each pass sheds more salt.

**Assay:** a glowing splint that relights in the fume means nitrate; a flare on glowing charcoal means nitre. The CAVE-3 floor earth assayed **negative** — bitter salt of the Epsom class, not nitre. A dry cave floor is not a nitre floor.

### `SALT-EVAP`

Flood ×6 trays at `EVAP-RACK-1` in a thin sheet, south lean. Scrape ~3–5 days later once a dry-close crust has formed. Flake-lift the trays, second scrape at the cellar trough. ~915 g per cycle. Pour the next batch as trays clear.

Pouring before a skin forms, or flooding without a dry wind band, wastes the cycle.

## Meat and dairy

### `JERKY-DRY`

- **Lean only** — trim all fat. Fat goes rancid; that is the spoilage route, not bacteria.
- Slice **with the grain**, thin and even. Salt first, which pulls water before any heat is applied.
- **Cold smoke** and screen against flies.
- **Doneness is the scale:** weigh wet, dry to ~⅔ of the weight lost, confirm no plateau, cut-check dry through.
- Store dry and cool in **cloth, not sealed** — sealing something still breathing grows mould.

**Failure — case hardening.** Too much heat dries the outside firm over a wet middle. It looks finished and fails the weight test. Lower the heat, raise the airflow. *(d3250)*

### `PEMMICAN-MAKE` · `TALLOW-RENDER` · `MEAT-SMOKE`

- Dry lean **hard**, pound it, then work rendered fat back in **at the end**. Not before — the drying has to finish first.
- Render tallow **separately and never near the drying rack.**
- Autumn deer are the fat deer; pemmican is an autumn job. A spring kill goes to jerky and gets its fat later.
- Smoked haunch is a different product from jerky and is not made by slicing one thin.

### `CHEESE-ACID`

Current practice until rennet lands.

- Heat to just under a simmer. **Pull the pot off the fire before the acid goes in.**
- Vinegar in a thin thread, clean break, greenish whey, curd in flakes.
- Drain, linen, light press. ~225 g class.
- **Fresh only.** Acid shatters the protein network, so this cheese can never age.

**Failure:** acid added while boiling gives squeaky gravel instead of curd. *(d3219)*

### `RICOTTA`

**Same day as the cheese.** Re-cook the whey near boiling with a splash of vinegar and skim the flocs.

Acid whey gives a poor yield; sweet rennet whey gives far more, which is another reason the rennet band matters. Whey banked for later is sour and thin — the leftovers go to plaster retarder, the goats, or the soil.

### `RENNET-PREP`

Dried cardoon heads steeped in warm water. **Use the least that sets it.** Too much plant rennet, or too long an age, turns the cheese bitter. Fig latex works but is strong and easy to overshoot; nettle is weak and needs impractical volumes.

This is the unlock for cheese that keeps six months instead of a week.

### `TAN-BARK`

Flesh, de-hair, rinse. Then **weak oak-bark liquor first, laddered weak to strong over weeks.** Step a rung when the cut edge reads through — `TAN-LADDER` in [periodic.md](../../checklists/periodic.md).

**Failure — striking too fast.** Strong liquor on a raw hide sets tannin at the surface and case-hardens it: firm outside, raw and rotting inside. The tell is a hard line at the cut edge. Back off the liquor. Exactly the jerky failure in a different material. *(d3254)*

Belt leather is a specific cut: butt, back and rump, along the backbone, grain to the pulley, tallow-stuffed and **pre-stretched under load**. A belt that stretches in service goes slack and loses its wrap.

## Fruit

### `FIG-LEATHER`

Tray-dry until tack and leather-go — ~5–7 days on the Y9 trays, much longer in a poor drying year. Halves firm, no mould. Peel, roll tight, interleave with parchment. ~220 g from ~250 g gross. Roll only when it reads leather-go; rolling early moulds the batch.

### `GRAPE-MUST` · `GRAPE-FERMENT` · `VINEGAR-MOTHER`

Crush to must in `BARREL-4` / `AMPHORA-9`. Mature must forks to vinegar; keep the mother crock at ~200 ml plus mat and refresh it against the August must season. Wine is not a stable product here — the vinegar and posca path is.

Sweet ferments stay gated behind a honey surplus.

## Mineral and fuel

### `CHARCOAL-BURN`

Feed the retort from pile 5, ×3 full retort runs per cycle. **Retort beats the pit by ~15–17% yield.** ~22 kg wood per burn, ~35–58 kg charcoal per ×3 cycle.

### `LIME-BURN`

`KILN-A-LIME` staggered ×2 burns, pile 7 limestone → ~5–10 kg quicklime per run.

### `PLASTER-CALCINE`

Gypsum, and it behaves nothing like lime.

- Identify first: thumbnail-soft, poorly soluble, and **no fizz in vinegar**. The fizz test is what separates it from carbonate.
- Gentle roast until steaming stops. **The pan visibly boils while calcining — when the boiling stops, count 100 and pull it.**
- **Over-roast is dead plaster.** It will never set, and there is no recovery.
- Mixing: plaster **into** water until islands form. ~12 min working time neat, ~25 min whey-gauged. **Never re-temper.** Interior only.
- **Set is not dry.** Damp the wall first or the substrate steals the water and you get chalk.
- Lime takes months to carbonate; plaster takes minutes. Do not carry habits between them.

### `POZZ-PREP`

`POZZ-KIT` prep, ~2 mm spread, **7 day cure** at bridge and tributary sites.

### `CLAY-PREP`

Wash, sift, magnet, tile test. Double-press runway for brick and tile. **Levigate and slip the inner skin** for refractory work; **double-levigate and triple-skim** for glass.

### `ORE-ROAST` · `ORE-LEACH`

- **Roast carbonate ore on an open hearth first** — it drives off water and carbon dioxide cheaply and leaves black oxide. Skipping it spends expensive blast heat on decomposition.
- Sulfide check: charcoal and blowpipe, then wet it — rotten eggs means sulfate.
- Copper leach: **settle overnight and draw the clear.** Filtering fine slime through linen alone clogs it and costs a day.
