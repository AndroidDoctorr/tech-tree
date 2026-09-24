# Hazards & deterministic rolls

*Live hazard state + tables. Roll math: [sim/roll.py](sim/roll.py). Canon difficulty: [rules.md — Hazard rolls](rules.md#hazard-rolls-deterministic).*

**Do not** improvise PASS/MISS on a catalog hazard — run the roll and log the line.

---

## Volatility *(live knob)*

| Setting | Mult | Feel |
|---------|------|------|
| **low** | **0.65×** | Fewer hits · maintenance still matters |
| **normal** | **1.00×** | Default · matches [rules.md](player-introduction.md) mishap band |
| **high** | **1.35×** | More near-misses · still no death-spiral |

**Current:** **normal**

Change only when the player names it. Patch this row + [now.md](now.md) **Hazard** line same pass.

---

## Roll grammar

| Piece | Value |
|-------|-------|
| **Space** | `0 … 999_999_999` (**DENOM = 1e9**) |
| **Hit** | `roll < effective_threshold` |
| **Seed** | `SHA256(campaign_seed \| day \| hazard_id \| index)` |
| **Campaign seed** | `tech-tree-orontes-y1` *(fixed — retcon days, not seed)* |
| **Volatility** | `effective = min(DENOM-1, base × volatility_mult × modifier)` |

**Why billion, not percent:** a **1%** floor is wrong for disaster-class events.  
**1 / 500_000_000** daily ⇒ threshold **`2`** (0.0000002%).  
Write rates as **`threshold`** integer, **`1/N`**, or **`Xppm`** — see [sim/roll.py](sim/roll.py).

### Day-file log line *(required on HIT or tier-1 near-miss)*

```text
HAZARD · d3094 · GOAT-RUT-BREED · roll 412_883_221 · thr 620_000_000 · MISS
```

On **HIT**, add outcome id + state patch pointer.

### Agent command

```bash
python sim/roll.py check --day 3094 --hazard GOAT-RUT-BREED --threshold 62000000 --volatility normal
python sim/roll.py batch --day 3094 --volatility normal WEATHER-RAIN:45000000 CART-WHEEL-MISHAP:12000000:1.4
```

---

## Immunity & targets

| Target | Aging | Disease | Injury | Poison |
|--------|-------|---------|--------|--------|
| **Player** | **immune** | **immune** | **yes** | **yes** |
| **Goats · donkeys · bees · game** | **yes** | **yes** | **yes** | n/a |

Player **illness** hazards are **blocked** — do not roll them. Animal illness and age bands **do** roll.

### ☠ ★★★ IMMUNITY IS A BLIND SPOT, NOT ONLY A SHIELD *(d3302)*

> ☠ ★★★ **EVERY HAZARD THE PLAYER IS IMMUNE TO IS A HAZARD HE CANNOT FEEL — and therefore one he will build into every structure he puts up, forever, without noticing.** *The warning was never a separate system from the injury: a mortal's headache, nausea and bad night ARE the detector, and he does not get them.*

★★ **This is the one class of problem where he is strictly WORSE off than an ordinary person**, *and it is invisible to him by construction.*

| Reading | |
|---|---|
| ☠ **Slow, cumulative, symptom-signalled hazards** | ★★★ **He will not notice.** *Carbon monoxide, lead, chronic fume, bad water, mould* — **no roll fires, and no narrative cue arrives, so the campus quietly accumulates them** |
| ✓ **The correct move** | ★★★ **He must BUILD AN INSTRUMENT for anything he is immune to.** *Soot as the CO meter · the smoke-spot tile · mass balance on fume · weighed desiccant* — **an external, comparable reading standing in for a sense he does not have** |
| ⚠ **For the agent** | ★ **Do not roll the player's harm.** ★★★ **Do roll, and do narrate, the EVIDENCE** — *a sooting throat, a grey tile, a shortfall in a mass balance.* **The hazard is real and only the injury is blocked** |

☠ **"Lead gives no warning of any kind" *(d3297)* was filed as a fact about lead.** ★★★ **It is a fact about him.**

---

## Live state *(patch when counters move)*

| Key | Now @ d3094 | Notes |
|-----|-------------|-------|
| **rut_tension** | **20** | Per-rut FARM-CARE scare: threshold = `tension × 1_000_000` (20M ⇒ **2.0%**/scare) |
| **last_breed_day** | **3131** | **Kidded d3191 · ×1 buckling · clean · doe freshened** |
| **pens_separated** | **no** | If **yes** → skip **GOAT-RUT-BREED** |
| **doe_bred_this_rut** | **yes** | Set **yes** on HIT · resets next Cal-Y |
| **COVERED-WAGON-1 wear** | **26** | 0–100 · iron rims d1877 · tune **d2917** |
| **Norima wear** | **21** | Haul d3480 20→21 · overhaul d3442 → 15 · doctrine d3463 |
| **mishap_pool** | **1** | **+1 qualifying exped d3415 · pop only if pool ≥ 8** |
| **last_hazard_audit** | **d3118** | **MISHAP-POOL-DOCTRINE-Y9 · pool retired for routine days** |

### Mishap pool doctrine *(player @ d3118)*

| Rule | Value |
|------|-------|
| **Philosophy** | Hazards = **real triggers** (weather, wear, rut, forge, loaded trail) — **not** D&D crit-fail or forced “something happens” |
| **Pool tick** | **+1** only after **genuine risk** heroes: loaded expedition miles, novel/rushed build, forge under stress, trail/climb miles-out, first-run dangerous gear |
| **No tick** | Farm scare · porch salt · retort · small haul · proven press · madder dig · clay to pile 1 · kiln fire on known grammar |
| **POP roll** | Only when pool **≥ 8** after a **qualifying** hero · base thr **35M** (~3.5% on pop day) — still deterministic, still rare at source |
| **Targeted mishaps** | e.g. drop amphora = roll only if player names rush/carry hero at height or trail — not automatic on oil press close |
| **Wear on routine** | **Yes** — old hammer / worn tongs / high cart wear during **routine** work uses **wear-modified** catalog rows (e.g. **FORGE-TONGS-SLIP**, **CART-WHEEL-MISHAP**) — failure rises with condition, not with a fake “drama counter” |

---

### Rut tension ticks *(agent duty @ year boundary or rut open)*

| Event | Δ tension |
|-------|-----------|
| Cal-Y opens · shared pen · no kid last freshen | **+12** |
| Full rut band (Sep–Dec) closes · still unbred | **+8** |
| **GOAT-RUT-BREED** HIT | reset **→ 20** · set `doe_bred_this_rut` |
| Player separates pens | freeze · no rut rolls |
| Planned breed flag (player names) | **+20** instant once |

Cap **rut_tension** at **95**.

---

## Trigger matrix

| When | Read | Roll if |
|------|------|---------|
| **Day open** | [player-calendar.md](checklists/calendar.md) month | **WEATHER-*** seasonal row |
| **FARM-CARE / scare** | Farm + Animals | **GOAT-RUT-BREED** *(Sep–Dec · shared pen)* · **GOAT-ILLNESS-PASS** *(quarterly index 0)* |
| **Team pull / loaded roll** | Cart/wagon row | **CART-WHEEL-MISHAP** · **WAGON-HUB-BIND** |
| **Forge hero** | Tool condition | **FORGE-SCALD** · **FORGE-TONGS-SLIP** |
| **Trail / climb / loft hero** | — | **PLAYER-FALL-INJURY** · **PLAYER-POISON-MISID** |
| **Forage / shellfish hero** | — | **PLAYER-FOOD-POISON** |
| **Genuine risk hero close** | See **Mishap pool doctrine** | **MISHAP-POOL-POP** only if pool **≥ 8** after a qualifying hero |
| **Passive daily** | — | **QUAKE-DAILY** *(index 0 only)* |

**Do not** tick **mishap_pool** on routine home-campus days (farm scare, porch scrape, retort, small haul, press when frame is proven, madder dig, clay haul to pile 1). Roll **targeted** catalog hazards only when the trigger row fires — not a forced “something happens” counter.

Skip rolls on explicit player **no-touch** expedition miles unless trigger is **weather** or **passive daily**.

---

## Catalog

Base **`threshold`** before volatility × modifier. **Outcome** on HIT only.

### Weather *(day open · month from [calendar.md](checklists/calendar.md))*

★ **Resolve the calendar month first.** `sim/roll.py` has no month logic — the agent picks thresholds from the table below. **Do not use one flat rate year-round.**

| Calendar month | Rain rolls | Light threshold | Heavy threshold | ≈ @ normal |
|---|---|---|---|---|
| **Apr–Sep** | **SKIP** | — | — | Dry season · no rain row |
| **Oct, Mar** | Light only | **67_000_000** | — | ~1 in 15 / day |
| **Nov–Feb** | Light + heavy | **111_000_000** | **20_000_000** | ~1 in 9 light · ~1 in 50 heavy |
| **All year** | **WEATHER-STORM-SEVERE** | **500_000** | — | ~1 in 2,000 |

| ID | Outcome |
|----|---------|
| **WEATHER-RAIN-LIGHT** | Rain · work AMBER · char pit OK · **`ROOF-R&D-PANEL-1` post-rain read** when queued |
| **WEATHER-RAIN-HEAVY** | Soak · rett smell · trail RED loaded · panel read if queued |
| **WEATHER-STORM-SEVERE** | Hail/wind · roof/lash read · apiary |
| **QUAKE-FELT** | **Flavour only** · one line · no consequence |
| **QUAKE-DAMAGING** | **22_000** · ~1 in 125 yr · cracked masonry · kiln/brick/vault read |

> **QUAKE-DAILY is RETIRED** *(d3235)*. Passive daily is **`QUAKE-DAMAGING` only** at day open.

**Annual sanity (wet peak Nov–Feb, ~120 d):** light ~1 in 9 → **~13 rain days** in the band · heavy ~1 in 50 → **~2–3 soak days**. Dry season rolls **zero** rain rows.

*Dec @ d3512:* roll **WEATHER-RAIN-LIGHT** `111_000_000` + **WEATHER-RAIN-HEAVY** `20_000_000` + **QUAKE-DAMAGING** `22_000`.

### Animals *(farm · haul)*

| ID | Base threshold | Modifier | Outcome |
|----|----------------|----------|---------|
| **GOAT-RUT-BREED** | **`rut_tension × 1_000_000`** | 1.0 | Bred · log breed day · kid due **Feb band** · [player-calendar.md](checklists/calendar.md) |
| **GOAT-ILLNESS-PASS** | 3_000_000 | ×1 if age>6 Cal-Y | Off feed · scours · isolate · **may die** |
| **DONKEY-COLIC-PASS** | 2_000_000 | ×1.5 heavy grain day | Colic · rest band · vet hero defer |

### Wear *(load × modifier)*

**Modifier** = `(wear / 50) × load_mult × terrain_mult`

| Load | load_mult |
|------|-----------|
| empty / hand roll | 0.6 |
| ~50 kg | 1.0 |
| ~90 kg | 1.6 |

| Terrain | terrain_mult |
|---------|--------------|
| yard / campus | 0.7 |
| trail graded | 1.0 |
| ford / rut / bar | 1.5 |

| ID | Base threshold | Tier outcomes *(by roll index 1 on HIT)* |
|----|----------------|---------------------------------------------|
| **CART-WHEEL-MISHAP** | **8_000_000** *(was 12M)* | wobble trim · bind PARTIAL · rim slip hero |
| **WAGON-HUB-BIND** | **5_000_000** *(was 8M)* | grease defer · collar refresh · hub seize |

### Wagon wear ledger *(Norima · `WAGON-V2-CHASSIS-1`)*

**Scale:** **0–100** maintenance-debt index for hazard `(wear / 50) × load × terrain` — **not** rim mm or “percent life.”

**What it tracks:** deferred maintenance across **hubs · tyres · bed wear strips · lash · cover · hitch** — grease drying, collar creep, rim wobble, thin strips, stretched lash. **+1** ≈ one loaded haul’s worth of that debt.

| Band | Read |
|------|------|
| **0–15** | Fresh / just rebuilt |
| **16–30** | Normal season — routine tune on schedule |
| **31–45** | Due tune — bind ghost · wobble · thin strips flagged |
| **46–60** | Parts wearing — tune buys less; plan overhaul |
| **61+** | Failure band — mishap rolls get mean |

| Event | Δ wear |
|-------|--------|
| **Loaded haul hero** — margin · trail · exped · multi-lap stone/wood/lime **with meaningful load** | **+1** |
| **Heavy manifest** — four-lap wood · ~90 kg north run *(same day as haul)* | **+1** *(stacks with haul tick)* |
| **Campus yard roll · garage apron · empty bed · hand loop tune test** | **0** |
| **Farm-scare inline hub grease** *(minutes, not a tune hero)* | **0** |
| **Routine tune** — **`WAGON-V2-TUNE-*`**: grease · lash · trim · cover roll · empty cert | **−6** *(adjustment — does not replace metal)* |
| **Overhaul close** — **`WAGON-V2-OVERHAUL-*` D1–D3**: strip · forge replacements · cert on D3 | **set wear → 15** *(post-rebuild baseline — not a delta)* |
| **Partial grease pass** *(minutes, not a tune hero)* | **0** |

> **Prior routine tunes at −4 stand in the journal through d3462; apply −6 from d3463 onward.** **`WAGON-V2-OVERHAUL-Y10` baseline in [retcon](../journal/retcons/WAGON-V2-OVERHAUL-WEAR-Y10.md).**

### Forge *(hero-day)*

| ID | Base threshold | Outcome |
|----|----------------|---------|
| **FORGE-SCALD-NEARMISS** | **4_000_000** *(was 25M)* | Burn · PPE save vs injury — **~15 %/yr at ~40 forge days** |
| **FORGE-TONGS-SLIP** | **5_000_000** *(was 15M)* | Drop workpiece · jaw spring · retire tongs |

### Player *(injury / poison only)*

| ID | Base threshold | Outcome |
|----|----------------|---------|
| **PLAYER-FALL-INJURY** | **1_500_000** *(was 6M)* | Sprain · cut · bone · respawn rules — **~1 in 22 yr at ~30 trail heroes/yr** |
| **PLAYER-POISON-MISID** | **200_000** *(was 800k)* | Wrong plant/fungus · purge hero — **he consults the device on everything** |
| **PLAYER-FOOD-POISON** | **800_000** *(was 4M)* | Bad shellfish/batch · debilitated day |

### Pool *(hero-day backlog)*

| ID | Base threshold | Gate |
|----|----------------|------|
| **MISHAP-POOL-POP** | 35_000_000 | Only when **mishap_pool ≥ 8** · pick nearest active track · on HIT reset pool **→ 0** |

---

## Worked example — goat rut @ d3094 scare

1. Sep–Dec band · shared pen · `doe_bred_this_rut = no` → **GO**.
2. `rut_tension = 68` → threshold **68_000_000**.
3. `python sim/roll.py check --day 3094 --hazard GOAT-RUT-BREED --threshold 68000000`
4. Log line in day file · on HIT patch **Animals** row + tension reset.

---

## Audit tail *(last 5 · optional)*

| Day | Hazard | Roll | Thr | Verdict |
|-----|--------|------|-----|---------|
| — | — | — | — | — |

Append rows when hazards fire; trim to 5.
