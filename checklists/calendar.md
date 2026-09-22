# Season calendar

Checked every day, in game. This file says **when**; [government/procedures](../government/procedures/) says **how**; [map](../map/index.md) says **where**. Join them on the procedure ID.

Every sow and every harvest here is mandatory. The only valid skip is an explicit player defer stated that turn — silence is never a defer, and a defer is only reasonable when surplus already covers the next full year. Ask about optional items. Name outstanding items before a band closes; a band that closes with items unlogged gets a retcon.

## January
- **20 Jan** — Ice haul opens · `ICE-HAUL`
- **~18 Jan** — Annual holding walk and care-doc tick · `STOCK-CARE-AUDIT`

## February
- **Feb – Apr** — Goat kidding / freshen window · `GOAT-KID` *(milking blocked until freshen)*
- **8 Feb** — Ice max haul (peak) · `ICE-HAUL`
- **10 Feb** — Ice max haul (peak) · `ICE-HAUL`
- **14 Feb** — Ice haul tail · `ICE-HAUL`
- **24 Feb** — `SEED-RAG-TEST` — germination-test **every bank in the [seed-vault.md](../inventory/seed-vault.md) roster, by ID, and write the date in the `Tested` column.** ☠ ★★★ *Revised d3285. This row read "every bank" for years and three banks had never been tested once — **an "every" with no roster is not auditable, because you can test one, tick the row, and be honestly finished.** The row is done when no `Tested` cell reads `—`*
- **24 Feb** — `SEED-REGEN` — **sow out and replace any bank past its cycle: emmer ~3 yr · chickpea ~3 yr · lentil ~2 yr.** ★★ *A reserve is a stock times a rate and the rate falls — banks are regenerated, not stored*
- **26 Feb** — Spring sow opens · `SPRING-SOW` *(run `SOW-PREP` in [conditional.md](conditional.md) on every sow day)*
- **26 Feb – 16 Mar** — Parsley / fava seed scout lap · `SEED-SCOUT` *(beyond campus — acquire before sow close)*

## March
- **11 Mar** — Exped / cart trips open
- **16 Mar** — Spring sow closes · `SPRING-SOW` *(emmer · lentil · field flax · chickpea · hemp · fava · culina herbs)*
- ⚑ **Y11 spring sow** — `EMMER-Y5-RESCUE` *(sow the ~25% Y5 elite bank thick as its own block, harvest as seed, replace the bank. **25% is not dead, it is the last call** — the curve is a cliff at this age)*
- **Mar** — Mark the wild grain stands while they are green · `GRAIN-GATHER-WILD` *(P-04 · P-05-A/B · P-06-A/B/C — in June they are indistinguishable from everything around them).* ★★ **Marking exists to TIME THE FOOD GATHER** — *the `T-2` parent ghost already finds the stands* **(d3312)**
- **Sow day + 3 weeks** — Bird establishment window · `BIRD-WATCH` · `BIRD-DEVICE-RESET`
- **Mar – Apr** — Shoot thin · `GRAPE-SHOOT-THIN` *(the budbreak job)*
- **21 Mar** — Apiary expand / swarm / wax harvest opens · `HIVE-SPLIT` · `WAX-RENDER`
- **21 Mar – 20 Apr** — Campus herb seed **designation** · `HERB-SEED-DESIGNATE` *(choose and stake the plants — ripe seed is May–June. Woody herbs go to `HERB-LAYER`, mint to `MINT-DIVIDE`)*

## April
- **1 Apr** — Quartz / ore haul season · `ORE-HAUL`
- **20 Apr** — Apiary / swarm / wax harvest closes

## May
- **15 May – 30 Jun** — ✓ **Fava FOOD pod pick CLOSED d3325** · `FAVA-PICK` *(Bed A west)* · ⚑ **`FAVA-SEED-Y10` remains standing — harvest on black, dry, rattling pods under the state trigger, not this food band**

## June
- **21 Jun** — Summer solstice
- **Jun** — Herb seed cut · `HERB-SEED-CUT` *(coriander · allium · thyme · parsley)* · ⚠ ★★ **CORIANDER FIRST — it drops the day it dries.** *Cut a shade under-ripe onto a sheet and let it finish off the plant* · ⚠ **parsley is BIENNIAL — second-year plants only** **(d3312)**
- ★★★ **Jun — Wild grain: TWO GATHERS, NOT ONE** · `GRAIN-GATHER-WILD` *(P-04 emmer · P-05 einkorn · P-06 wild barley)* **(split d3312)**
  - ✓ **FOOD gather — EARLY, at first dry.** *Volume, any head. Selects for nothing, and that is fine*
  - ✓ ★★★ **SEED gather — DELIBERATELY LATE.** **Only heads STILL HOLDING, stripped by hand** — ★★★ *every head still full in late June is full because it CANNOT LET GO, so the late stand is pre-sorted for TOUGH RACHIS* — ☠ **the one trait that separates a wild grass from a crop, handed over free**
- **Jun – Aug** — Thistle / cardoon flower gather · `THISTLE-GATHER` *(this is rennet — gates aged cheese)* · ✓ **plot sited d3312, rough ground east, off all beds** · ⚠ **CUT EVERY HEAD AT FULL FLOWER** — ★★ *the harvest stage IS the containment: a head cut in flower never makes seed* **(d3237 rule)**
- **Jun – Jul** — Grape cluster thin · `GRAPE-CLUSTER-THIN` *(at fruit set, not at budbreak)*
- **26 Jun** — Wild flax pull opens · `FLAX-PULL-WILD` *(ditch W · T-1 lip · FLAX-PATCH-1 — not the Bed B field drill)*
- **26 Jun – 26 Jul** — Wild / patch flax pull window *(second fibre lap · combines with woad walks)*

## July
- **9 Jul** — Woad leaf pull opens · `WOAD-PULL`
- **~20 Jul – 20 Aug** — Wild hemp fibre band · `HEMP-CUT` *(local / campus-margin stands · **Bed A cut is Aug** — **Ghab fibre is a wagon haul on the east string when the trail is open**, not a foot scout; **Y6 foot was pre-trail + bad ford season** · **d2943 proved Norima to `GHAB-STUB-1`**)*
- **26 Jul** — Wild flax pull closes

## August
- **1 Aug** — Wild grape pick opens · `GRAPE-PICK` *(P-03 · T-2 trellis · partial strip OK through Oct)*
- **1 Aug – 15 Sep** — Bed D fig pick · `FIG-PICK` *(FIG-C1–C4 · FARM-CARE eyes · not missable)*
- **1 Aug – 15 Sep** — Wild fig P-12 optional · `FIG-PICK` *(~650 m NW · not required if Bed D picked)*
- **1 Aug – 15 Sep** — Goat browse trim inline · `BROWSE-TRIM` *(at the fig and grape heroes — not a solo trip)*
- **15 Aug – 30 Sep** — Bed A north hemp cut · `HEMP-CUT` *(fibre-first, before seed hard)*
- **18 Aug** — Woad leaf pull closes

## September
- **1 Sep – 15 Oct** — Pistachio kernel harvest · `PISTACHIO-PICK` *(P-01, wild only, T-2 ~160 m · primary — do not skip)*
- **~5 Sep – 10 Oct** — Ghab wild hemp **seed** run · `HEMP-SEED-STRIP` *(seed, not fibre — this is the genetics import. Exped closes 27 Sep, so go early in the band)*
- **7 Sep** — Donkey hunt opens · `DONKEY-HUNT` *(wild recruit at D-27 — not holding care)*
- **Sep – Dec** — Goat rut band · `GOAT-RUT` *(separate pens if no planned breeding · rut read at FARM-CARE)*
- **15 Sep – 30 Nov** — Acorn gather window · `ACORN-GATHER` *(P-09 terrace. Calendar hero, not opportunistic — this band collides with grain harvest every year and that is how Y9 was lost. Flag it on every farm pass in band)*
- **15 Sep – 31 Oct** — Nitre bed leach band · `NITRE-LEACH` *(NITRE-BED-1 at north lee · recharge the bed after)*
- **27 Sep** — Exped / cart trips close

## October
- **12 Oct** — Donkey hunt closes
- **15 Oct** — Wild grape pick closes · `GRAPE-PICK` *(before hard frost)*

## November
- **1 Nov – 28 Feb** — Grape winter prune band · `GRAPE-PRUNE` *(P-03 at T-2 · highest yield and quality lever · do not skip)*
- **Nov – Mar** — Donkey winter care band · `STOCK-WINTER` *(rug at holding · trace-rest rotation)*
- **6 Nov** — Salt evap opens · `SALT-EVAP`
- **16 Nov** — Olive pick and madder root dig open · `OLIVE-PICK` · `MADDER-DIG`
- **20 Nov** — Olive oil press window opens · `OLIVE-PRESS`
- **~20 Nov – 1 Dec** — Pistachio ground-recovery tail only · `PISTACHIO-PICK` *(if primary was missed — a modest sweep, not a full pick)*
- **~20 Nov – 15 Dec** — Farm-deadline buffer *(keep Sep–Oct wild pistachio clear of the emmer / oil / salt crunch)*
- **26 Nov** — Salt evap closes
- **27 Nov** — Emmer harvest · `EMMER-HARVEST`
- **28 Nov** — Pulse harvest · `PULSE-HARVEST`
- **29 Nov** — Food prep day *(shelf-life sprint)*
- **~28 Nov – 15 Dec** — Field flax pull · `FLAX-PULL-FIELD` *(Bed B centre / campus P-07 drill · after grain and pulse · second annual fibre lap)*

## December
- **1 Dec – 10 Dec** — Olive oil decant / settle · `OIL-DECANT`
- **~1 Dec** — Acorn last tail lap · `ACORN-GATHER` *(windfall only, then hands off until next fall)*
- **10 Dec** — Olive oil press window closes *(before the feast band)*
- **16 Dec** — Olive pick and madder root dig close *(last table-olive stray lap for brine)*
- **20 Dec** — Feast eve −1
- **21 Dec** — Yule / Feast · animal treat
- **22 Dec** — Year opens

## Year-round

Low-effort, high-calorie. Cadence rows live in [periodic.md](periodic.md) and [daily.md](daily.md); listed here so the annual picture is complete.

| Cadence | What | ID |
|---|---|---|
| Daily | Weir fish — primary fresh protein | `WEIR-FISH` |
| 2×/week | Snail collect (A-02 creek rocks) — brine keeps 2–4 months | `SNAIL-GATHER` |
| Weekly | Smoke / jerky top-up when the weir runs over | `JERKY-TOPUP` |
| As needed | Grape vinegar mother refresh | `VINEGAR-MOTHER` |

## Known collision points

Where windows get lost. Each of these has cost a harvest at least once.

| Band | Collides with | Guard |
|---|---|---|
| 15 Sep – 30 Nov acorn | Grain and pulse harvest | Lost in Y9, retcon filed. Flag on every farm pass in band |
| ~5 Sep – 10 Oct Ghab hemp seed | Exped closes 27 Sep | Go early in the band or not at all |
| 26 Feb – 16 Mar spring sow | Long build arcs | Herbs are sown last and are the item most likely to be dropped |
| 1 Nov – 28 Feb grape prune | Winter build and ice haul | Do not skip |
| 1 Sep – 15 Oct pistachio | Emmer, oil and salt crunch | The Nov tail is recovery, not a plan |
