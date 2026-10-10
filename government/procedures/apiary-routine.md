# Apiary routine — obligatory calendar

**Mechanism and doctrine:** [bees.md](bees.md). **When bands open:** [calendar.md](../../checklists/calendar.md). **State-fired work:** [triggers.md](../../checklists/triggers.md). **Intervals:** [periodic.md](../../checklists/periodic.md) · [daily.md](../../checklists/daily.md).

> ★★ **Wax is not harvested. It is manufactured inside the hive at ~8 honey : 1 wax, then released only when you cut surplus pale comb.** Scraping cappings was the skep poverty trap; top bars let you take the **rich fraction**. You cannot breed or scrape your way past **forage, population, and swarm loss.**

---

## Realistic output — five colonies, this valley

| Era | Order of magnitude | Why |
|---|---|---|
| **Skep / cappings only** | **~0.1 kg/yr** | Fixed comb · oldest darkest fraction · colony not expendable |
| **One-time skep renders (d3265/d3274)** | **~1 kg banked** | Closed the emergency · not repeatable |
| **Top-bar steady state (your grammar)** | **~0.3–0.8 kg/yr clean wax** | **2–4** pale-bar cuts when stores are **surplus**, rendered in **1–2** pot days |
| **Strong year + forage fixed + no swarms** | **~1 kg/yr** | Upper bound for **this campus** without a sixth hive |

Reference renders: **~90 g comb → ~62 g wax** · **~140 g → ~96 g** (d3600 · d4342) — **~65–70%** on pale honey comb.

**Genetics / import:** lowers the **~13% brood tax** → faster buildup → **more comb only if nectar exists**. Autumn sealed-colony import (Y14 plan @ d4342) is **long-term population health**, not a wax spike.

**Selective breeding:** slow; queen replacement is **reactive** (poor mating, supersedure), not a production programme.

---

## What actually raises wax (beyond scrapes)

| Lever | Effect | Effort |
|---|---|---|
| ★★★ **July–Aug forage** (`vitex` · borage · designated herbs in bloom) | **More bees survive the dearth** → more wax budget next spring | Plant/layer once · walk in summer |
| ★★ **Swarm steering** (space **before** charged cups) | **Keeps wax factories in boxes** | Mid-day opens in spring · trigger-fired |
| ★★ **Flow-end honey-bar cuts** (pale outer only · **2–3 strong hives**) | **Direct wax** without brood theft | 1–2 hero afternoons per flow |
| ★ **Scale curve + heft** | Know **when** to cut and **when** to feed | **Same hour daily** Mar–Oct |
| ★ **Autumn genetic import** | Buildup rate over years | One exped |
| ⚠ **Sixth hive** | **Divides same nectar** unless forage improved | **Not recommended** |

**Not a lever:** more renders with no comb queue · dark brood comb · robbing weak colonies · storing empty comb in a box.

---

## Obligatory calendar

Player directive @ d4342: **autumn sealed-colony genetic import** — **no spring `BAIT-BOX` swarm chase** unless explicitly named.

### Daily — **1 Mar – 31 Oct** *(active season)*

| ID | Procedure | Rule |
|---|---|---|
| **`HIVE-SCALE-READ`** | Weigh **`HIVE-3`** @ **fixed hour** | Log weight or “flat/climb/drop” in day file when apiary touched; **mandatory read even on non-apiary days** ([daily.md](../../checklists/daily.md)) |

### Weekly — **year-round**

| ID | Procedure | Rule |
|---|---|---|
| **`APIARY-DOORSTEP`** | **All five top-bar boxes · lid on** — pollen · traffic · fighting · drones · fanning · undertaker rate | **Bundled with any campus day** if not done in the last **7 d** ([periodic.md](../../checklists/periodic.md)) |

### Spring band — **21 Mar – 20 Apr**

| ID | Procedure | Rule |
|---|---|---|
| **`APIARY-WATCH`** | **Mid-day** pass: doorstep **+** open **only** hives that doorstep flagged (congestion · cups · light heft) | **≥1 full watch in band** · **≥1 more** if **`HIVE-3`** or **`HIVE-6`** shows **waxed cups** |
| **`HIVE-SPACE-BAR`** | Empty waxed bar **into brood-nest edge** on **strong** hive when cups are **waxed dry** | **Before** jelly — not after ([bees.md](bees.md) swarm ladder) |
| **`WAX-RENDER`** | Only when **`COMB-TO-RENDER` ≥ ~80 g** pale comb queued | Spring band allows first cut; **not** “render because calendar” |

### Main flow — **~Apr – Jun** *(valley-specific; scale tells the date)*

| ID | Procedure | Rule |
|---|---|---|
| **`FLOW-NOTE`** | On **`HIVE-SCALE-READ` climb** | Note **start date** once per year ([triggers.md](../../checklists/triggers.md)) |
| **`WAX-CUT-SURPLUS`** | After climb **plateaus** ≥ **~7 d**: cut **≤1 pale outer honey bar** each from **up to 3** strongest hives (never **`HIVE-7`** unless heft clearly surplus) | Queue to **`COMB-TO-RENDER`** · same day or next **`WAX-RENDER`** |

### Summer dearth — **~Jul – Aug**

| ID | Procedure | Rule |
|---|---|---|
| **`HIVE-FEED`** | Scale **falling** or heft light on grey days | Feed + **reduce entrance** ([triggers.md](../../checklists/triggers.md)) |
| **`FORAGE-READ`** | On **`FARM-CARE`**: designated herbs · rosemary · **vitex/borage** plantings | **No extra trip** — eyes only |

### Autumn — **Sep – Nov** *(player plan)*

| ID | Procedure | Rule |
|---|---|---|
| **`GENETIC-IMPORT-AUTUMN`** | **Sealed top-bar colony** from far stock on a **named exped** | **Y14 essential** · not spring bait |

### Optional second wax pass — **late flow or mild autumn**

| ID | Procedure | Rule |
|---|---|---|
| **`WAX-CUT-SURPLUS`** | Same grammar as spring · **only if** post-cut heft still **solid** | **Max ~4 cuts/yr** across apiary |

### Annual — **once per spring band**

| ID | Procedure | Rule |
|---|---|---|
| **`INBREEDING-METER-REMAP`** | **`HIVE-6`**: one comb mapped at lay · re-map at seal **~9 d** | Baseline meter ([bees.md](bees.md)) · skip if import same year logged |

---

## Hero logging grammar

| Hero ID | When | Tags |
|---|---|---|
| **`APIARY-WATCH-Ynn-n`** | Full mid-day band pass | **⚒ ~½ h** |
| **`HIVE-SPACE-BAR-d####`** | Space bar on named hive | **⚒ ~¼ h** |
| **`WAX-CUT-d####`** | Pale bars cut · comb to queue | **⚒ ~¼ h** per hive opened |
| **`WAX-RENDER-d####`** | Pot on water · never dry | **⚒ ~½ h** |
| **`GENETIC-IMPORT-d####`** | Autumn exped colony move | **⚒ full day+** |

---

## Roster constraint — splits @ d3984

**`SPARE-HIVE-1` is a live colony**, not empty staging. On **`SWARM-CHASE`** / charged cup:

1. **`HIVE-SPACE-BAR`** first if cups still dry-waxed.
2. If jelly/egg: **artificial swarm** only with a **named plan** — second spare box · **boost `HIVE-7` with one sealed brood bar** · or **accept swarm risk**.
3. Do **not** auto-split into **`SPARE-HIVE-1`**.

---

## Agent / player checklist hook

On **`CALENDAR-READ`** in spring: confirm **apiary band** + **`APIARY-WATCH` count** before **20 Apr**.

On **`PERIODIC-DUE`**: if **`APIARY-DOORSTEP` > 7 d** → flag on next campus day.

On **`TRIGGER-SCAN`**: **`HIVE-FEED` · `SWARM-CHASE` · `FLOW-NOTE` · `WAX-CUT-SURPLUS` (plateau) · charged-cup split plan**.
