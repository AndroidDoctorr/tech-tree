# Civil year anchor — Cal-Y13 @ d4620 *(player directive · d4623)*

**Filed:** Day 4623 · corrects inflated **`Cal-Y15`** display without renaming frozen stock IDs.

## Anchor

| Absolute day | Civil header | Prose |
|---|---|---|
| **d4256–d4619** | **Cal-Y12 D1–D365** | Late Dec **d4610–d4619** headers patched · **`CAL-Y12-CLOSE-4619`** |
| **d4620** | **Cal-Y13 D1** · ~1 Jan | **`CAL-Y13` opens** — canonical epoch for forward play |
| **d4621+** | **Cal-Y13 D2…** | `D = 1 + (d − 4620)` until next 31 Dec |

**Formula (d ≥ 4620):** `cal_year = 13 + floor((d − 4620) / 365)` · `cal_doy = 1 + ((d − 4620) % 365)`.

## Why not rename everything

Pre-d4620 headers and **`-Ynn-` / `-Y15-` tags** stay as **frozen lot labels**. Civil **`Cal-Y`** was ~**+2** vs elapsed time (Yule double-count + early drift). **Retagging inventory would collide or orphan logs** — not done.

## ID grammar — forward *(d4620+)*

| Era | Pattern | Example |
|---|---|---|
| **Legacy tag** | **`…-Y14-…` · `…-Y15-…`** | **`GRAIN-FERMENT-Y14-1`** · **`WAGON-V2-OVERHAUL-Y15-1`** · **`PAINTING-…-Y15-1`** |
| **New civil tag** | **`…-CY13-…`** | **`SPRING-SOW-CY13`** · **`BUILD-LOT-CY13-1`** |

**`CY13`** = civil year **13** at tagging time. **`Y14`** on an old row = **harvest/sprint tag 14**, not “today’s civil year.”

## Translation cheat sheet *(display only)*

| Misfiled display (pre-retcon) | Canonical civil |
|---|---|
| Cal-Y15 D1 @ d4620 | **Cal-Y13 D1** |
| Cal-Y15 D4 @ d4623 | **Cal-Y13 D4** |
| “~Jan Y15” prose | **~Jan Y13** |

## Year transition — only

**`Cal-Y(n+1) D1` @ 1 Jan** · **`CAL-Yn-CLOSE` @ 31 Dec**. **Never @ Yule.** **`SUN-YULE`** is observance only.
