# Solar calendar — SUN-CAL-1

*Last updated: **Day 396** (~10,000 BC) · **Cal-Y2 D159***  
**Site:** **C-0** courtyard · **~12 m S of H-v2** · sight hole **~15 cm Ø** @ south wall  
**Built:** **SUN-CAL-1 v1 ✓ Day 195** · **SUN-CAL-YEAR ✓ Day 239**

---

## Dual tracks

| Track | What it measures | How you mark |
|-------|------------------|--------------|
| **Ground (SUN-MARK)** | Noon shadow **position** on the courtyard pad — seasonal **east–west drift** (figure-8 **horizontal** leg) | PM-R1 dot @ spear tip each clear noon |
| **Wall (SUN-SPECK)** | Noon sun **height** via sight hole onto north wall — seasonal **altitude** arc (figure-8 **vertical** leg) | Lime tick @ speck height each clear noon |
| **YULE band** | Fixed **anchor tick @ wall height 42** — feast eve reference · **not** a daily counter | Red double tick · stake **SUN-YULE-237** |

**Rule:** One pair of marks per day when sky is **clear @ noon** — journal logs **SUN-MARK-NNN** + **SUN-SPECK-NNN**.

---

## Figure-8 behavior (why winter feels “stuck”)

The sun’s apparent motion traces an **analemma** (figure-8). On this calendar:

- **Winter (tight curve):** Wall speck moves **slowly**; **YULE @ holds @ 42** for weeks — you are on the **pinched** part of the loop (Dec–Feb class).
- **Spring / autumn (steep legs):** Ground dots **advance ~+2/day** when logged; wall speck **~+2/day**; **YULE @** **accelerates** — days since feast eve climb faster on the wall index.
- **Summer (open curve):** Same **+2/day** discipline on ground/wall when marked daily; **YULE @** peaks before reversing toward next feast.

You do **not** need perfect daily marks — **interpolate** between anchors when you skip days (see below).

---

## Calendar years (player authority)

| Rule | Days |
|------|------|
| **Calendar Year 1** | **1–237** — closes **@ feast eve (Day 237)** |
| **Calendar Year 2+** | Begins **day after feast** — **Day 238 = Cal-Y2 D1** |
| **Dual date** | Journal **Day N** · **Cal-Y2 D(N−237)** for N ≥ 238 |
| **YULE / Christmas** | **Day 237** — **FEAST-237** · **WINTER-TREE-1** · **YULE-BENCH-1** benchmark |

---

## Anchor table (logged noon marks)

*Use for drift checks and interpolation. **YULE @** = secondary index on wall track (days-since-anchor class counter — **flat in deep winter**, **faster in spring**).*

| Day | Cal-Y2 | Season (approx.) | Ground | Wall | YULE @ | Notes |
|-----|--------|------------------|--------|------|--------|-------|
| **195** | — | Autumn | — | — | — | **SUN-CAL-1 v1 ✓** operational |
| **237** | — | **Solstice eve** | **46** (ring) | **42** (tick) | **anchor** | **FEAST-237** · Year 1 close |
| **239** | D2 | Early winter | — | — | — | **SUN-CAL-YEAR declared** |
| **301** | D64 | Late winter | 128 | 124 | 46 | Centadial 3 · **YULE @ leaves plateau** |
| **305** | D68 | Early spring | — | — | — | **SPRING-SOW-1** |
| **309** | D72 | Early spring | 136 | 132 | 54 | Frost gate · sow-2 |
| **322** | D85 | Spring | 149 | 145 | 67 | EXPED-B close |
| **337** | D100 | Early spring | 165 | 161 | 84 | **IRON-WELD-1** |
| **346** | D109 | Early spring | — | 179 | 102 | **ANVIL-FACE-1** |
| **364** | D127 | Early spring | 219 | 215 | 138 | **ROOF-W1 ✓** |
| **365** | D128 | Early spring | **221** | **217** | **139** | **FARM-WATCH-365** |
| **366** | D129 | Early spring | **223** | **219** | **140** | **IRON-BLOOM-6 ✓** |
| **367** | D130 | Early spring | **225** | **221** | **141** | **VAULT-CHAR · IRON-HAMMER-1 ✓** |
| **368** | D131 | Early spring | **227** | **223** | **142** | **EXPED-C gates GREEN** |

---

## Interpolation (missed days)

When you skip noon marks but know **Δ days** since last logged anchor:

### Ground & wall (primary tracks)

```
mark_new ≈ mark_last + (2 × Δdays)
```

Example: last log **Day 337** (ground **165**) → **Day 365** (Δ**28**) → **165 + 56 = 221** ✓

### YULE @ (secondary — seasonal rate)

| Phase | Approx. days | YULE @ behavior |
|-------|--------------|-----------------|
| **Plateau** | ~238–299 | **Hold @ 42** (winter pinched loop) |
| **Rising** | ~300–365 | **~+1.4 to +1.6 per day** between logged anchors |
| **Next plateau** | approach Day ~237+365 | Slows toward next feast eve |

Piecewise between anchors (linear segment):

| From Day | To Day | YULE @ start → end |
|----------|--------|---------------------|
| 301 | 309 | 46 → 54 |
| 309 | 322 | 54 → 67 |
| 322 | 337 | 67 → 84 |
| 337 | 364 | 84 → 138 |
| 364 | 365 | 138 → 139 |

### Season guess from marks only

| Ground class | Wall class | Season guess |
|--------------|------------|--------------|
| Rising from ~46 ring | Speck climbing from 42 | **Late winter → spring** |
| Mid **160–200** | Mid **156–196** | **Spring** |
| High **200+** | High **196+** | **Late spring → summer** (Year 2 not reached yet @ D365) |
| Ground drift slowing | Wall speck near summer max | **Summer** |
| Reverse toward 46 ring | Speck falling toward 42 band | **Autumn → winter** |

---

## Operational discipline

- **Clear noon only** — cloud day = no mark · do not guess
- **Trail:** portable spear + gnomon post @ C-0 center
- **Drift check:** ground and wall should stay **~4 marks apart** (wall ≈ ground − 4 at noon in current epoch — verify @ next anchor)
- **Sow windows:** **SPRING-SOW** keyed off **ground rising + YULE @ leaving 42**, not Roman month names
- **Feast eve:** always **Day 237 mod calendar year** — compare **YULE-BENCH-1** plate year-on-year

---

## Related

- [journal/years/year-001.md](journal/years/year-001.md) — Calendar Year 1 arc (Days 1–237)
- [journal/days/week-035/day-239.md](journal/days/week-035/day-239.md) — **SUN-CAL-YEAR** declaration
- [journal/days/week-034/day-237.md](journal/days/week-034/day-237.md) — **FEAST-237** · solstice eve
- [inventory.md](inventory.md) — C-0 site notes
