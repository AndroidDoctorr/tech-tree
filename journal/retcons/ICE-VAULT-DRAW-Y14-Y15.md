# RETCON — Y14→Y15 ice vault annual draw

**Filed:** Day 5386 audit · **Cal-Y15 D37** *(player catch)*  
**Cause:** **`ICE-VAULT-STOCK` carried @ ~115 kg** from **d5021 close (~128.5 kg)** without **~Aug + Feb composite read** or **logged polymer hero draws**. Precedent [ICE-VAULT-DRAW-Y13-Y14](ICE-VAULT-DRAW-Y13-Y14.md) · [ice-vault.md](../../government/procedures/ice-vault.md).

---

## Anchor

| Event | Mass |
|---|---:|
| **Close d5021** | **~128.5 kg hard** | Y14 peak **CLOSED** |
| **Hero draws (logged)** | **−~13.5 kg** | **d5276–5285** polymer C₄ trap / brine tops |

| Day | Draw |
|---|---:|
| d5276 | **−~5.0 kg** | C₄ trap brine |
| d5277 | **−~2.0 kg** | Brine top |
| d5283 | **−~1.8 kg** | Brine top |
| d5284 | **−~2.2 kg** | Brine top |
| d5285 | **−~2.5 kg** | C₄ trap |

**No separate Aug Y15 `ICE-VAULT-READ` filed** — full civil-year passive slice rolled into **pre-peak d5384 composite** (same grammar as **d5004** since **d4657**).

## Calculator

`python sim/ice_vault.py annual --start 128.5 --hero-draw 13.5`

| Component | kg |
|---|---:|
| Summer edge melt | 11.4 |
| Milk niche + cheese | 8.4 |
| Cellar turnover | 17.8 |
| Ice-break slush cull (Feb prep) | 1.8 |
| Hero draws (logged) | 13.5 |
| **Total** | **52.9** |

| Post-read (pre-haul @ d5384)** | **~75.6 kg hard** |
| **Headroom to ~130 kg cap** | **~54.4 kg** |

**Patches:** [day-5384.md](../days/year-015/week-770/day-5384.md) **`ICE-VAULT-READ`** · [day-5386.md](../days/year-015/week-770/day-5386.md) **peak lap 1** yield · [food.md](../../inventory/food.md).

**Doctrine:** Two peak laps (~25 kg + ~14 kg class) expected to refill from this headroom — **lap 2 outstanding** after corrected lap 1.
