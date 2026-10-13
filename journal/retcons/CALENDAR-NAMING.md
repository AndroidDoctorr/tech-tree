# Calendar naming — three clocks (player clarification · d4610)

**Filed:** Day 4610 · **Cal-Y15 D1** · post-Yule confusion review

## What went wrong in the UI

**`journal/days/year-0NN/` is not `Cal-Yn`.** Folder `year-010` holds absolute days **~3286–3650**. Folder `year-011` holds **~3651–4015**, etc.:

```text
journal folder year-0NN  =  floor((d − 1) / 365) + 1
```

**`Cal-Yn`** advances at **`SUN-CAL` close @ Yule** (~21 Dec class), usually **mid-week** inside a folder year. Example **week 502 / year-010**:

| d | Header | Normal? |
|---|---|---|
| 3508–3509 | **Cal-Y10** · Yule eve/feast | ✓ |
| 3510+ | **Cal-Y11** opens d3510 | ✓ same folder |

Browsing **`year-010` → `year-012` in the file tree** skips **`year-011`** and looks like “two calendar years in two weeks” — it is **two filesystem buckets**, not a missing `Cal-Y12`.

## Authoritative clocks

| Clock | Meaning | Use in IDs |
|---|---|---|
| **`d####`** | Absolute campaign day | **Primary** — audit, hazards, inventory `Last` |
| **`Cal-Yn` · `Dn`** | Sun-calendar year + day-of-year @ C-0 | Day headers · **`SUN-CAL-Yn-CLOSE`** · harvest tags **`…-Y14-…`** |
| **`year-0NN` folder** | Archive partition only | **Path only** — do not embed in new stock IDs |

## Correction without refactor

- **No rename of `year-0NN` folders** — paths are stable links.
- **No bulk ID renames** — `SPIRIT-GRAIN-Y13-1`, `THERMAE-FULL-Y14-1`, etc. stay **`Cal-Y` = sun year when tagged**.
- **Agent rule:** grep **`Cal-Y`** for “what year is it in-world”; grep **`d####`** for ledger; **ignore folder `year-0NN` for chronology**.

## Optional display (future)

Player may alias in prose: **“archive year 10”** vs **“calendar year 10”** — not required in filenames.
