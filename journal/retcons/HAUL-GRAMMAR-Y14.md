# RETCON — Norima aggregate haul grammar · Y14

**Filed:** **d4303 audit** · **Cal-Y14 D63**  
**Cause:** After **wood** ([WOOD-CHAR-GRAMMAR-Y14](WOOD-CHAR-GRAMMAR-Y14.md)), audit found **sand · gravel · limestone** still on **cart-lap counts** scaled to Norima wheel count, not **wagon payload**. **`d4094` sand four-lap (~7.2 kg net)** · **`d4117` gravel three-lap (~10.2 kg)** · **`d4121` limestone one-lap (~14 kg)** — all under-credit a covered wagon with iron rims and a bulk bed.

**Player directive:** Procedures **forward** + **partial ledger credit** — last few heroes of each type corrected in their day files; **bonus** line for the rest of the winter haul stack. **Do not** re-audit every sand/gravel/lime day in Y12.

---

## Retired grammars *(do not use on Norima)*

| ID | Logged pattern | Typical net | Problem |
|---|---|---|---|
| **d4094** | Sand · four-lap · sack + sieve | **~7.2 kg** | Cart lap count on a wagon |
| **d4117 / d2631** | Gravel · three-lap · sacks | **~10 kg** | Hand-cart lap scale |
| **d4121** | Limestone · one-lap stub + knap | **~14 kg** | Single light load on a full-day hero |

**Still valid:** **`d3174` clay** bulk liner · **ice** · **ore @ face** · **weir glean**.

---

## Canonical forward grammar

See [harvest.md](../../government/procedures/harvest.md).

| Haul | Default Norima hero | Net target |
|---|---|---|
| **`SAND-HAUL`** | **2-load wet + yard sieve** | **~18–28 kg** |
| **`GRAVEL-HAUL`** | **2–3 laden trips** | **~45–70 kg** |
| **`HAUL-LIME`** | **Full day · knap + 2 loads** | **~40–55 kg** |
| **`CLAY-HAUL`** | **3-lap bulk liner** | **~35–45 kg** |

---

## Partial replay — last heroes corrected

| Day | Event | Logged | Canonical | Δ |
|---|---|---|---|---|
| **d4261** | `SAND-HAUL-4261` | **+~7.2 kg** | **+~16 kg** | **+~8.8** |
| **d4290** | `SAND-HAUL-4290` | **+~7.2 kg** | **+~16 kg** | **+~8.8** |
| **d4292** | `SAND-HAUL-4292` | **+~7.2 kg** | **+~16 kg** | **+~8.8** |
| **d4117** | `GRAVEL-HAUL-4117` | **+~10.2 kg** | **+~22 kg** | **+~11.8** |
| **d4122** | `GRAVEL-HAUL-4122` | **+~10.2 kg** | **+~22 kg** | **+~11.8** |
| **d4268** | `HAUL-LIME-4268` | **+~14.2 kg** | **+~28 kg** | **+~13.8** |
| **d4294** | `HAUL-LIME-4294` | **+~14.2 kg** | **+~28 kg** | **+~13.8** |

**Subtotal correction:** sand **+~26.4** · gravel **+~23.6** · limestone **+~27.6**

---

## Bonus *(unlogged winter stack — wagon bed fuller than lap grammar credited)*

| Stock | Bonus |
|---|---|
| **`SAND-FILTER-1`** | **+~10 kg** |
| **`GRAVEL-1`** | **+~18 kg** |
| **`CACO3-P7`** | **+~8 kg** |

---

## Ledger @ d4302 close

| Stock | Pre-retcon | Correction | Bonus | Post-retcon |
|---|---|---|---|---|
| **`SAND-FILTER-1`** | **~37.0 kg** | **+~26.4** | **+~10** | **~73.4 kg** |
| **`GRAVEL-1`** | **~20.4 kg** | **+~23.6** | **+~18** | **~62.0 kg** |
| **`CACO3-P7`** | **~19.0 kg** | **+~27.6** | **+~8** | **~54.6 kg** |

★ **Pour gravel still haul-gated** — but each future hero day is **~45–70 kg**, not **~10**.

---

*Procedure patch: [harvest.md](../../government/procedures/harvest.md). Char quad: [day-4302.md](../days/year-012/week-615/day-4302.md).*
