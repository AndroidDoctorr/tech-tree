# Resource sites

Where things come from. **Sites and distances only — no stock counts.** What you have is [inventory](../../inventory/index.md); this file is where to go get more.

**Route, legs, `TQ` and crossing times are [trails-and-bridges.md](trails-and-bridges.md).** This file says *what and where*; that file says *how to get there and how long*. ★ **Plan every trip from both.**

## ★★★ How to use this file

**Player says "let's get X."** Find X in the lookup below → read its **site ID**, **trip class** and **leg** → open [trails-and-bridges.md](trails-and-bridges.md) for the day count and the crossings → check the **season** and the **confidence** → then gate it against [inventory](../../inventory/index.md) and [conditional.md](../../checklists/conditional.md).

### Trip classes

| Class | Range | Cost |
|---|---|---|
| **CAMPUS** | < 1 km | Minutes. Part of another day |
| **LOCAL** | 1–6 km | ⧗ **Half a day** on foot, out and back |
| ★ **DAY** | 6–20 km | ⧗ **One day**, out and back, wagon optional |
| **OVERNIGHT** | 20–70 km | ⧗ **1 day out, 1 back**, plus working days at the far end |
| **EXPEDITION** | 70 km+ | ⧗ **2+ days each way.** Needs trip prep, rations, waystations |

### Confidence — ★★★ read this before betting a trip on a row

☠ **The d3286 failure was a resource row believed at a confidence it had not earned.** *A nickel laterite at Kisecik was doctrine for thirteen days and a 117 km expedition was planned around it. There is no nickel there.*

| Grade | Means |
|---|---|
| ✓ **HELD** | **Worked, hauled from, or standing in inventory.** The Player has personally taken material from it |
| ◐ **SEEN** | **Eyes on the outcrop, not yet worked.** Location is real; yield and grade are not measured |
| ○ **INFERRED** | **The rock type or setting says it should be there.** ⚠ **Nothing has been seen.** ☠ **Do not plan an expedition on an `○` row — walk to it first** |
| ✗ **DISPROVED** | Checked and absent. Kept so the hypothesis is not re-formed |

**Intent** reads: Eat · Seed · Breed · Material · Dye · Chem · Watch.

---

## ★★★ LOOKUP — substance to site

**One line per thing you might want. Everything else in this file is detail behind these rows.**

### Metals and ores

| Want | Go to | Site | Dist | Class | Conf |
|---|---|---|---|---|---|
| **Copper** | Kisecik — malachite, azurite, chalcopyrite | `KISECIK-DISTRICT-1` | ~16 km | ★ **DAY** | ✓ |
| **Iron** | Kisecik gossan — limonite, hematite, siderite, magnetite | `KISECIK-DISTRICT-1` | ~16 km | ★ **DAY** | ✓ |
| **Lead** | Kisecik — galena at `ZN-PB-MARK-1A/1B` | `M-15` | ~16 km | ★ **DAY** | ✓ |
| ★★★ **Silver** | **Kisecik galena → cupellation** *(sparse but proven)* | `M-15` | ~16 km | ★ **DAY** | ✓ |
| | **Bolkardağ** — the real horizon, argentiferous lead | `M-16` | ~350 km+ | **EXPEDITION** | ○ |
| **Gold** | Kisecik — vein gold in arsenopyrite · placer in the Miocene gravels | `KISECIK-DISTRICT-1` | ~16 km | ★ **DAY** | ✓ |
| **Zinc** | Kisecik sphalerite. ⚠ **No process — needs a sealed retort and condenser** | `M-15` | ~16 km | ★ **DAY** | ✓ |
| ☠ **Mercury** | Kisecik cinnabar. ⚠ **Float only, source unlocated** | `KISECIK-DISTRICT-1` | ~16 km | ◐ | ◐ |
| **Chromium** | Kisecik, pods in the deep serpentinite. ⚠ **No process** | `KISECIK-DISTRICT-1` | ~16 km | ★ **DAY** | ◐ |
| | **Islahiye** — the documented podiform district | `M-24` | ~100 km N | **EXPEDITION** | ○ |
| **Nickel** | ☠ **NOT Kisecik.** Amanos, near Islahiye | `M-24` | ~100 km N | **EXPEDITION** | ○ |
| **Tin** | Kozan north gate — cassiterite | `M-25` | ~220 km | **EXPEDITION** | ✓ |
| ☠ **Arsenic** | ⚠ **Not a target — a HAZARD.** Arsenopyrite at Kisecik, and **the gold is inside it** | `KISECIK-DISTRICT-1` | ~16 km | — | ✓ |

### Chemicals

| Want | Go to | Site | Dist | Class | Conf |
|---|---|---|---|---|---|
| ★★★ **Sulfuric acid** | `VITRIOL-HEAP-1` — weathering pyrite at the ore | `M-23` | ~16 km | ★ **DAY** | ⧗ **Liquor ~d3378** |
| **Sulfur** | Kisecik — pyrite is the bank; native sulfur is the old `M-14` mark | `M-14` · `KISECIK-DISTRICT-1` | ~16 km | ★ **DAY** | ✓ |
| **Alum** | Coast cliff, `COAST-SITE-1` | `M-11` | ~20 km W | **OVERNIGHT** | ✓ |
| **Nitrate** | Limestone, manure, bird cliff | `M-12` | Local · ⚠ cliff deferred | LOCAL | ✓ |
| **Salt** | `S-03` marsh margin · sea at ~20 km for volume | `SALT-1` | ~700 m | LOCAL | ✓ |
| **Iodine, soda ash** | Kelp, coast beach | `M-13` | ~20 km W | **OVERNIGHT** | ✓ |
| **Bitumen** | **Asi-margin seeps — the near one is generous** | `SEEP-REGISTER-1` | ~6 km | ★ **DAY** | ✓ |
| | Ghab stub — the real deposit core | `GHAB-STUB-1` | East string | **OVERNIGHT** | ◐ |

### Earth, stone and clay

| Want | Go to | Site | Dist | Class | Conf |
|---|---|---|---|---|---|
| **Limestone** | ★ **Everywhere.** Camp terrace pile 7 is the working face | `M-06` | 0 m | CAMPUS | ✓ |
| **Clay** *(pottery, kiln, mortar)* | T-1 cut face | `M-01` · `M-02` | 90–110 m | CAMPUS | ✓ |
| ★ **Kaolin** *(porcelain, refractory)* | **Tell Atchana, east string** | `SC-KAOLIN-01` | ~20 km E | ★ **DAY** *(good road)* | ✓ |
| | Koruhöyük tributary runoff | `M-26` | ~65 km N | **OVERNIGHT** | ○ |
| **Gypsum** *(plaster, selenite panes)* | Gorge wall below the cave line | `M-21` | ~300 m | CAMPUS | ✓ |
| ★★★ **Pozzolan** | ☠ **Ground kiln rejects — see the three-tier note below** | *(campus)* | 0 m | CAMPUS | ✓ |
| | Koruhöyük scoria and tuff — **the old haul source** | `M-27` | ~65 km N | **OVERNIGHT** | ✓ |
| | **Cappadocian tuff** — the premium natural pozzolan | `M-30` | Far N of Kozan | **EXPEDITION** | ○ |
| **Chert** *(knapping)* | T-4 terrace | `M-04` | 920 m | LOCAL | ✓ |
| **Quartz** *(optics, glass)* | Local terrace and T-1 gravel | `M-10` | 200 m | CAMPUS | ✓ |
| | **Nur Dağları / Belen pass** — high-purity vein quartz survey | `M-28` | ~15–25 km NE | ★ **DAY** | ○ |
| **Sand, grit, gravel** | T-1 river | `M-09` | 200 m | CAMPUS | ✓ |
| **Fluorite** | Akkaya, north of the Kozan gate | `M-29` | ~220 km+ | **EXPEDITION** | ○ |
| **Basalt** *(hard stone)* | Karasu graben flows | `M-27` | ~40 km N | **OVERNIGHT** | ◐ |

### Living things

| Want | Go to | Site | Dist | Season | Conf |
|---|---|---|---|---|---|
| **Hemp** *(fibre and seed)* | **Ghab plain** | `P-22` | East string, far | **Fibre ~20 Jul–20 Aug · seed ~5 Sep–10 Oct** | ✓ |
| **Cork** | SW macchia | `P-20` | ~26 km W | **May–Aug**, 9-yr regrowth | ◐ |
| **Woad** *(blue)* | Plain limestone rise | `P-18` | ~2.8 km NW | Leaf summer · seed autumn | ✓ |
| **Madder** *(red)* | Dry calcareous bank | `P-19` | ~3.1 km WNW | **Root: autumn** | ✓ |
| **Donkeys** | `D-27` | `A-06` | ~19 km NE | — | ✓ |
| **Sheep, horses** | ⚠ **Not scouted.** Hills, 30–150 km | `A-07` · `A-08` | — | — | ○ |

---

## Plants

| ID | Name | Where | Season | Intent | Notes |
|---|---|---|---|---|---|
| `P-01` | Wild pistachio *(P. atlantica)* | 160 m · T-2 | Autumn hull | Eat · Seed | 4 trees, tagged `T-a/b/c`. Largest nuts go to the seed bank |
| `P-02` | Wild olive *(oleaster)* | 400 m · T-2 end | **Oct–Nov fruit** | Harvest · Seed | `P-02-SEL-1` in the vault. Nov pick and press band |
| `P-03` | Wild grape | 240 m · T-2 | Late summer | Eat · Seed · Leather | Trellis ✓ d192 · `P-03-SEL-1` |
| `P-04` | Wild emmer | Farm Bed A | Jun harvest | Sown · Breed | Domesticated onto the farm — the wild stand is the origin, not a supply |
| `P-05` | Einkorn | Farm Bed A | Jun | Sown · Breed | As above |
| `P-06` | Wild barley | Farm Bed A | Jun | Sown · Breed | As above |
| `P-07` | Flax *(Linum bienne)* | Farm Bed B | **Pull mid–late summer** | Sown · Cordage | Pull at grain-fill, not at ripeness |
| `P-08` | Reed *(Phragmites)* | 180 m · T-1 river | Year-round | Material | Cordage winner `C-1` |
| `P-09` | Oak | Camp and slopes | Acorns fall | Material · Eat | ⚠ **Leach the tannins before counting the calories.** Ash source. **Not wine cork** |
| `P-10` | Willow | 90–200 m · T-1 | Year-round | Material | Stakes, lashings `C-2` |
| `P-11` | "Fake rye" *(brome / wild barley)* | 200 m · plain | — | ✗ **Ignore** | Do not plant |
| `P-12` | **Wild fig** | **650 m** · T-3 / T-4 NW | **~Aug–Sep** | Eat · Seed · Breed | `FIG-C1`–`C4` at Bed D came from here. ★ **Cuttings root faster than seed**; seed is for variety |
| `P-13` | Wild mint *(Mentha)* | ~180 m · T-1 reed margin | Spring–autumn | Eat · Dry | |
| `P-14` | Wild garlic / leek *(Allium)* | ~200–350 m · T-2 ditch, farm shade | Spring–autumn | Eat · Seed | |
| `P-15` | Coriander *(Coriandrum)* | ~200 m · plain, farm edge | Spring–autumn | Eat · Seed | |
| `P-16` | Thyme, marjoram and other aromatics | ~350 m · T-2 olive shade | Spring–autumn | Eat · Dry | Modest pick only |
| `P-17` | Lentil *(Lens)* | ~450 m NW · plain margin | Spring sow | Breed | `P-17a` scouted and brought onto the farm |
| `P-18` | **Woad** *(Isatis)* | **~2.8 km NW** · plain limestone rise | **Leaf summer · seed autumn** | Dye · Breed | ~12 plants, ~4 m². The blue |
| `P-19` | **Wild madder** *(Rubia)* | **~3.1 km WNW** · dry calcareous bank | **Root: autumn** | Dye | ~6 m mat. The red |
| `P-20` | **Cork oak** *(Q. suber)* | **~26 km W** · SW macchia at `P-20-A` | **May–Aug** bark strip | Material · Breed | ~6 trees, scouted d852. ⚠ **9-year regeneration between strips** · not Orontes native |
| `P-21` | **Rosemary** | ~280 m · T-2 dry calcareous bank | Spring–autumn | Eat · Seed · Transplant | ~1.5 × 2 m mat, found d1691 |
| ★ `P-22` | **Wild hemp** *(Cannabis)* | **Ghab plain**, east string | ⚠ **Fibre ~20 Jul–20 Aug · seed ~5 Sep–10 Oct** | Cordage · Seed · Oil | ★★ **The fibre that beats flax for rope.** ⚠ **Seed band collides with the 27 Sep exped close — go early in the band or not at all** |
| ★ `P-23` | **Vitex** *(chaste tree)* | **Asi riverbank ~6 km**, and the wet margins generally | ★★★ **Flowers Jul–Sep — straight through the bee dearth** | Bee forage · Material | ✓ **Struck from cuttings d3284.** Semi-ripe wood, cut below a node. **The only thing here that blooms into the gap** |

---

## Geology and minerals

| ID | Name | Where | Dist | Use | Conf | Notes |
|---|---|---|---|---|---|---|
| `M-01` | Grey-brown clay | T-1 | 90 m | Kiln · mortar · pots | ✓ | **Primary bank.** ~2 m cut face |
| `M-02` | Red seep clay | T-1 | 110 m | Mortar · hot face | ✓ | Heat-shock behaviour still being read |
| `M-03` | White clay | T-4 · site `S-01` | 780 m | Pottery | ✓ | Test tile d14 |
| `M-04` | Chert terrace | T-4 · site `S-02` | 920 m | Knapping | ✓ | ★ **Best source** |
| `M-05` | River gravel chert | T-1 | 200 m | Knapping | ✓ | Backup · lower yield |
| `M-06` | **Limestone** | Camp terrace, pile 7 | 0 m | Lime | ✓ | ★ **Unlimited.** The whole plain is limestone — this is the working face, not the deposit |
| `M-07` | Green copper stain | Camp pile 4 | 0 m | Ore clue | ✓ | ☠ **A pointer, not a source.** The copper is at `KISECIK-DISTRICT-1` |
| `M-08` | Aleppo pine resin | North, 150 m + climb | 150 m | Adhesive · pitch | ✓ | Amphora seal · hafting. True birch tar is still a horizon |
| `M-09` | River sand and grit | T-1 | 200 m | Grog · temper · concrete | ✓ | |
| `M-10` | **Quartz**, clear and white | Local terrace, T-1 gravel | 200 m | Optics · glass | ✓ | Local supply covers the R&D queue |
| `M-11` | **Alum** *(alunite class)* | Coast cliff, `COAST-SITE-1` | ~20 km W | Chem · mordant | ✓ | Collected d379. Stake refreshed |
| `M-12` | **Nitrate** *(efflorescence)* | Limestone · manure · bird cliff | Local | Chem · saltpetre | ✓ | Purified and mixed by d1609. ⚠ **Bird cliff deferred** |
| `M-13` | **Kelp / seaweed** | Beach | ~20 km W | Iodine · soda ash · wrap | ✓ | Burned to `KELP-ASH-1` |
| `M-14` | **Native sulfur** | Kisecik, Amanos toe | ~16 km | Chem · sulfur | ✓ | `KISECIK-SULFUR-ROAD` `K-R0`–`K-R3`. ☠ ★★★ **Held since d1651 and it never made a drop of acid** — *sulfur was never the bottleneck, the conversion was.* ★ **Pyrite at `M-23`, not this, is the acid feedstock** |
| `M-15` | **Galena and sphalerite** | Kisecik · `ZN-PB-MARK-1A/1B`, ~200 m NE of `M-14` | ~16 km | Lead · zinc · ★★★ **silver** | ✓ | Confirmed d1651 · **smelted and cupelled d3289.** ⚠ **Silver sparse** — ★★★ *the site's real worth is that the method was proved here.* ⚠ **Zinc boils at the temperature that reduces it** — sealed retort and condenser, caught from the top |
| `M-16` | **Bolkardağ** — argentiferous lead, and the region's iron, Cu-Pb-Zn and minor tin | Central Taurus, N of the Seyhan | ~350 km+ | Silver · lead | ○ | ☠ **Far lap, behind the Seyhan crossing.** ☠ ★★★ **REFRAMED d3289: a LEAD deposit silver is extracted FROM, not a silver deposit.** ★★ **Cupellation rehearsed at `M-15`, so this is now an errand rather than a gamble** · ★ **the district also carries iron and minor cassiterite — one trip, several prizes** |
| `M-17` | **Bitumen** *(fracture stain)* | Plain limestone bench, dry wash · `BITUMEN-SEEP-1` | ~3.2 km WNW | Waterproofing · mastic | ◐ | Found d2269. **No active flow at a dry read.** ★ Superseded for working volume by `SEEP-REGISTER-1` |
| `M-18` | **`CAVE-1`** — chamber and spring | Gorge slope across the tributary | ~250 m N | Cool store · shelter | ✓ | Good air on the lamp test. **Live seep and pool at the rear.** ⚠ **Too damp for seed** · ☠ **water untested — boil first** |
| `M-19` | **`CAVE-2`** | ~60 m upslope of `CAVE-1` | ~300 m | ✗ **None** | ✓ | Air PASS but **damp wall and floor — same seep horizon** |
| `M-20` | **`CAVE-3`** — dry chamber | Above the seep band, behind a rock shoulder | ~300 m | ★ **The seed ark** | ✓ | **Powder-dry floor, no bats, air PASS.** Fitted d3221 — see [off-campus-structures.md](off-campus-structures.md) |
| `M-21` | **Gypsum bed** | Gorge wall, below the cave line | ~300 m | **Plaster · selenite panes · desiccant** | ✓ | ★★ **A bed, not a pocket — supply is unconstrained.** Thumbnail-soft, no vinegar fizz, bars out in slabs. **Selenite gives clear cleavable sheets.** ⚠ Granular — not carving alabaster. **~48 kg d3224** · ⚠ **no return trip since** |
| ★★★ `KISECIK-DISTRICT-1` | **The Kisecik ophiolite district** | Across the Orontes | **~16 km** *(⚠ ~9 km if `SC-ORONTES-ISLAND-B` is bridged)* | ★★★ **Nine metals** | ✓ | **See the district block below** |
| ★★★ `M-23` | **`VITRIOL-HEAP-1`** — pyrite weathering bed | At the ore, Kisecik | ~16 km | ★★★ **SULFURIC ACID** | ✓ | Built d3288 — clay pan, stone bed, roofed sump, open heap. ⧗ **First liquor ~d3378.** **The heap stays at the ore; only the liquor travels** |
| `M-24` | **Islahiye / Amanos ophiolite** | N Amanos, Gaziantep side | ~100 km N | **Chromite** ✓ · **nickel** ○ | ○ | **Podiform chromite is the documented ore here**, near the harzburgite–cumulate boundary. ☠ **Nickel is the Player's inference, not a sighting** — see the nickel block below |
| `M-25` | **Cassiterite** | Kozan north gate and the slopes beyond | ~220 km | **Tin** | ✓ | **~2.4 kg concentrate hauled d1500.** ★ The wider Taurus tin district is real and was worked in antiquity — **placer cassiterite in the streams is the accessible form**, not the vein |
| `M-26` | **Koruhöyük kaolin** | Tributary runoff below the volcanic ground | ~65 km N | Porcelain · refractory | ○ | ★ **Same stop as the pozzolan.** ⚠ **Inferred from the setting — weathered feldspathic rock shedding white clay into the tributaries.** Not yet sampled |
| `M-27` | **Karasu volcanic field** — working face at **Koruhöyük** | Karasu graben, Kırıkhan north to the Belen ascent | ~40–65 km N | **Pozzolan · hard stone** | ✓ **at Koruhöyük** | ★★ **Young alkali olivine basalt along the rift faults — plainly visible from the road on the Kırıkhan→Belen climb.** ☠ ★★★ **The FLOWS ARE NOT POZZOLANIC — crystalline basalt is nearly inert. Only the glassy material reacts: scoria, cinder, ash and altered tuff off the cones.** *`POZZ-TUFF-1` came from here and it is a marginal pozzolan, which is half of why seven blocks emptied it* |
| `M-28` | **Nur Dağları / Belen pass quartz** | NE, same corridor as `L7` | ~15–25 km NE | High-purity optics · glass | ○ | `QUARTZ-SURVEY-NUR-BELEN-765`, a day survey. ★ **Combine with any Belen-bound lap — same road** |
| `M-29` | **Fluorite** | Akkaya, north of the Kozan gate | ~220 km+ | Flux · optics · ⚠ **HF if ever wanted** | ○ | Filed d2915 as **~1 day from the Kozan gate once the trail is mature** — ★ **rides on a `CAP-0` lap, never its own expedition** |
| `M-30` | **Cappadocian tuff** | Inland highland, far north of the Kozan gate | Multi-week | ★ **The premium natural pozzolan** | ○ | ⚠ **On the Cappadocian Road, NOT the coast** — do not go looking along the shore. ☠ **Almost certainly never worth the trip** — see the three-tier note below |
| `SC-KAOLIN-01` | **Kaolin bank** | Tell Atchana, east string near `AM-EAST-02` | ~20 km E | **Porcelain · refractory** | ✓ | Indexed d2523–d2525 · **~17.2 kg hauled d2561.** Not depleted. ★★ **On the best-graded road on the map — this is the cheapest 20 km anywhere** |
| `SEEP-REGISTER-1` | **Asi-margin bitumen seeps ×3** | Asi margin bench | **~6 km** | Waterproofing · asphalt | ✓ | Registered d3270. ★ **One of the three is properly generous** — a black weep out of a shaley bench, soft in the sun. **Far closer than the Ghab** |
| `GHAB-STUB-1` | **Ghab bitumen core** | East string, far | Multi-day | Asphalt at volume | ◐ | The real deposit. ⚠ **Only worth it for volume the Asi seeps cannot cover** |

---

## ★★★ Pozzolan — three sources, and the nearest is the best

☠ **Three different documents named three different pozzolan sources.** *All three are real; they are tiers, not rivals.*

| Tier | Source | Cost | Quality |
|---|---|---|---|
| ★★★ **Make it** | **Ground underburnt brick and kiln seconds** | ✓ **Free, at home, and the stack refills itself every firing** | ★ **A true artificial pozzolan, and better than the tuff** |
| **Haul it** | **Koruhöyük scoria and tuff `M-27`** | ⧗ **Overnight, ~65 km** | ◐ **Marginal.** Rift basalt is mostly crystalline |
| **Forget it** | **Cappadocian tuff `M-30`** | ☠ **Weeks** | ★ Excellent — *and irrelevant at that distance* |

> ☠ ★★★ **THE FEEDSTOCK IS THE REJECT PILE, AND THE REJECTS ARE REJECTS FOR EXACTLY THE REASON THAT MAKES THEM WORK.** *Clay fired hard enough to be a good brick has vitrified into glass that will not react. Underburnt clay is a failure as a brick and a success as a pozzolan.* ★★ **Never haul what the kiln is already throwing away.**

⚠ **The `M-27` haul still has a reason to exist:** it is the same stop as the kaolin `M-26` and the staging point for Islahiye. **Go for the kaolin and bring tuff back; do not go for the tuff.**

---

## ★★★ `KISECIK-DISTRICT-1` — the Kisecik district

> ☠ ⚠ **ID COLLISION, RESOLVED HERE.** *This district was filed as `M-22` on d3290. **`M-22` was already the NE magnetite pin at ~22 km**, with sub-marks `M-22-UP`, `M-22-TALUS-S1` and others, and about four hundred journal references going back to Y1.* ★★ **The nine-year-old pin keeps the number. The district gets its name.**

**Not a deposit. A district.** ★★ **An ophiolite is a slice of sea floor stood on its edge — mantle at the bottom, old vents at the top — and each level carries its own metals.** *One walk crosses the whole stack, which is why one walk crosses nine of them.*

★ **Local names:** the veins run in two groups, around **Kızıltepe** *(richer, more varied)* and **Deliklikaya** *(more gangue, less ore)*. The ground between Kisecik, **Gülderen** and **Sarıgöl** is the survey box.

| Level | Rock | Ores |
|---|---|---|
| **Deep** | **Serpentinite, dunite, harzburgite, olivine gabbro** — the barren ground, soaps under a wet thumb | **Chromite** in pods. ⚠ *No process for it yet* |
| **Middle** | **Metadiabase**, silicified and carbonatized, cut by quartz veins | ★★★ **The ore veins.** Gold, arsenopyrite, pyrite, chalcopyrite, sphalerite, galena · **cinnabar** ⚠ *minor, unlocated* · **hessite and electrum** in traces |
| **Upper** | Vent and vein tops | **Pyrite and chalcopyrite** under the rusty cap |
| **Surface** | Gossan, gravels, stream placers | **Limonite · hematite · siderite · magnetite · malachite · azurite · scorodite · placer gold** · ★ **and "copper vitriol" — blue crystals on the weathered faces** |

> ☠ ★★★ **THE FOUR IRON ORES ARE THE SULFIDES, ROTTED.** *Rain and air on pyrite make rust and acid and carry the rest away, so the iron cap is a gravestone standing exactly over the body.* ★★★ **Virtue and defect as a signpost: the weathering that destroyed the top of the ore is the flag that marks it.** ⚠ **Fresh ore begins about a body's length below the cap.**

> ★★★ **THE BLUE CRYSTALS PROVE THE HEAP BEFORE IT IS BUILT.** *Copper vitriol on a weathered face is sulfide plus air plus water, having already made its own sulfate without being asked.* **`VITRIOL-HEAP-1` is not an experiment — it is that reaction, fenced in and given a sump.**

> ★★★ **`SERPENTINE-FLORA-READ` — the barren IS the outcrop.** *Ultramafic rock weathers to soil heavy in magnesium and chromium and short of calcium, so almost nothing grows on it.* **A flora that refuses to match its neighbours is a map of the bedrock, in colour, all year, from a hundred metres** — ⚑ **walk the other barren patches; this is a survey method, not one find.**

### ☠ ⚠ Hazards — all four are real and none of them announce themselves

| | |
|---|---|
| ☠ ★★★ **ARSENIC** | **Arsenopyrite is a main ore mineral here and the GOLD IS INSIDE IT.** ⚠ **Roasting arsenopyrite gives arsenic trioxide — a serious poison, and it travels as a fume and a dust.** ☠ **It also means the vitriol liquor will carry arsenic: the heap is not just acid.** *Scorodite on the weathered faces is the tell* |
| ☠ **LEAD** | Galena. **A quiet poison, no warning, and it accumulates.** Cupellation **fumes** it |
| ☠ **MERCURY** | Cinnabar, minor and unlocated. ⚠ **Find it deliberately or not at all** |
| ⚠ **ACID DRAINAGE** | Contained by design at `M-23` — **because the drainage is the product** |

☠ ★★★ **AND THE STANDING WARNING FROM d3286: this district was CATALOGUED — `M-14` sulfur, `M-15` sulfides, a road built and named — while a 117 km expedition was planned for sulfur.** *The prizes were not hidden. They were indexed.* ★★★ **Check the near site before optimising the far one.**

---

## ☠ `NICKEL-TARGET-1` — and what the d3286 miss actually taught

> **Do not look for pentlandite.** It is the wrong target for an ophiolite. The ore is the **red-brown dirt on top of weathered serpentinite**, found by **vegetation, not rock** — and **garnierite**, apple-green and waxy, in the fractures.

☠ ★★★ **NOT AT KISECIK.** *The d3273 laterite hypothesis was walked out on d3286 and there is none there; the ultramafic ore in that ophiolite is **chromite**.* See [KISECIK-MINERALOGY-3286](../../journal/retcons/KISECIK-MINERALOGY-3286.md).

> ☠ ★★★ **THE INDICATOR IS RIGHT AND IT IS NOT SUFFICIENT.** *Kisecik passed the vegetation test perfectly and carries no nickel whatsoever.* ★★★ **The barren tells you the rock is ULTRAMAFIC, which is a precondition, not a deposit.** ★ **Look for the green in the fractures. If the green is absent, the nickel is absent.**

**Where now:** `M-24`, **the Amanos near Islahiye, ~100 km N.** ⚠ ○ **INFERRED, not seen** — *what is documented up there is podiform **chromite**, which confirms the right rock and says nothing about a laterite cap.*

| Corridor stage | Distance | State |
|---|---|---|
| HOME → **Kırıkhan** | ~53 km | ✓ **Maintained road**, `L0`–`L6` |
| Kırıkhan → **Koruhöyük** | ~12 km | ⚠ **Mostly trail** · ★ **the pozzolan `M-27` and the kaolin `M-26` are both here** |
| Koruhöyük → **Islahiye** | ~30–35 km | ○ **Unscouted** |

> ★ **Nickel, chromite, pozzolan and kaolin are ONE northern trip up a corridor already half-owned.** ⧗ **Y11, not urgent** — *constantan and invar are conveniences; acid was the ceiling, and acid is now 16 km away.*

★ **And reduce it in contact with the copper or the iron** — constantan and invar are alloys, so the metal never has to exist on its own.

---

## Salt

`SALT-1` operational since d187. First food-grade salt came from the `S-03` brackish margin through the porch evaporation tray.

| Option | Where | Verdict |
|---|---|---|
| **A — marsh / plain** | `S-03` ~700 m NW · Amuq | ★ **Live.** ~2.8 L brackish per haul |
| **B — saline seep** | Marked WNW ~1.1 km | Backup if `S-03` thins. Follow mineral taste and white stain on limestone |
| **C — sea** | ~20 km W coast | Real volume, but an overnight. Tidal flat evaporation or wash salt |
| **D — saltbush** | Local, at the goat trap | ✗ **Bait, not cure salt.** Not NaCl |
| **E — murex / brackish farm** | Near camp | Horizon |

☠ **Not salt:** fresh river water · red seep clay `M-02` · the lime pile.

---

## Fauna

| ID | Species | Where | Reliable? | Notes |
|---|---|---|---|---|
| `A-01` | Fish | 200 m · TRIB-1 weir | **Daily** | 4–8 small per day. ⚠ Not the Orontes |
| `A-02` | Snails | 90–200 m · TRIB-1 rocks | **Daily** | Bulk calories · collected ~2×/week |
| `A-03` | Wild goat | 850 m · gorge | **Live trap** since d79 | Pause the drive when there is kid sign |
| `A-04` | Night heron | 200 m · weir | Competitor | Reset the stakes |
| `A-05` | Fox · partridge | Local | No | Background |
| `A-06` | **Donkey** *(wild ass)* | `D-27` ~19 km NE | Herd ×4 sighted | The source of the working team |
| `A-07` | **Sheep** *(wild)* | Hills, 30–100+ km | ○ **Not scouted** | Horizon |
| `A-08` | **Horse** *(wild Equus)* | ○ **Not marked** · estimated ~80–150 km N/NE | ○ **Not scouted** | `HORSE-SCOUT-1` filed d723 and still open |

---

## ★ Historical notes kept on purpose

### The `CAVE-3` floor was not nitre

The chamber floor earth looked like a nitre deposit and was worked as one. It is **gypsum plus an epsom-class bitter salt** *(d3222–d3223)*.

**No quarry was cut, because the whole chamber is the ark** — and following the mistake to its source found `M-21`, which is worth far more than the nitre would have been.

### ★ Navigation

★★ **This country is easy to move through without a road.** *Distinct ridgelines, the two rivers, the Amanos wall on the west and the lake in the middle — getting lost takes effort.* ⚠ **The exception is deep in the mountains**, where the landmarks stop being visible from inside the valleys. **Route-finding cost is near zero on the plain and real above the treeline.**
