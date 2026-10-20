# Retcon · `BLOCK-Y10` mix ratio — ledger vs Roman mass *(player audit d5075)*

**Filed:** d5075 · **forward rule effective immediately**

## What went wrong

The **1 : 2 : 5 measuring-box grammar** was treated in day files as **~8.6 kg quicklime + ~3.4 kg pozz + ~12.8 kg sand** per **×8 blocks**, with **gravel as a small add-on** (~8.5 kg) after [BLOCK-AGGREGATE-DEBT-Y13](BLOCK-AGGREGATE-DEBT-Y13.md).

That pattern matches **labeling the “5” leg as sand only** and **under-filling the box** relative to mould demand — not a full **lime : pozzolan : aggregate (sand + gravel)** mass balance for **390 × 190 × 190 mm** dry-tamped units (~**15 kg** each).

**Lime was closer to honest** when **dry `QUICKLIME-1` + putty** are counted (~**20–25 kg** binder class per ×16). **Pozzolan and aggregate were massively under-debited.**

## Canonical mass — research-aligned *(player d5075)*

**Per ×16 blocks** *(one full dual-mould sprint day at press cadence)*:

| Leg | Mass | Notes |
|---|---:|---|
| **Lime binder** | **~30 kg** | **Dry quicklime class** + slake water *(~1.3× hydrated mass in trough)* |
| **`POZZ-TUFF-1`** | **~45 kg** | Koruhöyük / M-27 class |
| **`SAND-FILTER-1`** | **~70 kg** | Fine leg of aggregate |
| **`GRAVEL-1`** | **~100 kg** | Coarse leg · **~40% sand / 60% gravel** of the “5” leg is a workable split |
| **Total premix** | **~245 kg** | ~**15.3 kg** input per block |

**Per ×8:** halve the row. **Per ×18:** multiply ×16 row by **18/16**.

**Roman pad reference** *(player)* — **~1 m²** at working thickness: **~24 kg lime · 45 kg pozz · 30 kg sand · 110 kg gravel** — same binder/pozz order of magnitude; pad sand/gravel split differs from block **70/100** split but **total aggregate ~170 kg** is in family with block **×16** aggregate **170 kg**.

### Measuring box *(calibrated)*

| | |
|---|---|
| **`BLOCK-MEASURER-1`** | **~20 L per “part”** · **1 : 2 : 5 = 7 parts** |
| **One full dump** | Fills **~×4 blocks** (dual nest A/B · two premix cycles per ×8) |
| **×16 day** | **×4 full 1:2:5 dumps** (matches premix A–D grammar) |

## Old vs new — per ×16

| Leg | Old ledger *(d5065)* | Canonical | Shortfall |
|---|---:|---:|---:|
| **Lime** | **~20.4 kg** *(17.2 QL + 3.2 putty)* | **~30 kg** | **~9.6 kg** |
| **Pozz** | **~6.8 kg** | **~45 kg** | **~38.2 kg** |
| **Sand** | **~25.2 kg** | **~70 kg** | **~44.8 kg** |
| **Gravel** | **~17 kg** | **~100 kg** | **~83 kg** |

## Blocks cast at old rates *(vibratory press era)*

| Day | Blocks |
|---|---:|
| **d4931** | ×8 |
| **d4941** | ×16 |
| **d5065** | ×16 |
| **d5068** | ×18 |
| **Total** | **×58** |

### Cumulative shortfall if all ×58 owed at canonical per-block delta

| Leg | ~Debt |
|---|---:|
| **Lime** | **~35 kg** |
| **Pozz** | **~138 kg** |
| **Sand** | **~162 kg** |
| **Gravel** | **~301 kg** |

**Last two batches only** *(d5065 + d5068 · ×34)*: **~81 kg pozz · ~95 kg sand · ~176 kg gravel · ~18 kg lime**.

## Policy

| | |
|---|---|
| **Forward** | **All `BLOCK-Y10` / press sprints** use **canonical mass** in Consumption · **no skimping** · patch inventory once per day. |
| **Backward** | **Do not rewrite** d4931–5068 day files. |
| **QC** | Blocks already submerged **stand** — lean mix units in pit · acceptable unless break test says otherwise. |

## Paydown *(logged d5075)*

| Scope | Treatment |
|---|---|
| **d5065 + d5068** *(×34)* | **✓ `BLOCK-MIX-DEBT-PAYDOWN-5075`** — pozz/sand/gravel + lime *(crock + char/CaCO₃ kiln class)* debited from inventory |
| **d4931 + d4941** *(×24)* | **Forgiven** — player: balances earlier under-haul era · **no debit** |

## Inventory @ paydown

| Row | After d5075 |
|---|---|
| **`POZZ-TUFF-1`** | **~5.6 kg** |
| **`SAND-FILTER-1`** | **~37.6 kg** |
| **`GRAVEL-1`** | **~20 kg** |
| **`QUICKLIME-1`** | **×0** |
| **`CHAR-LANE`** | **~17.0 kg** |
| **`CACO3-P7`** | **~82.6 kg** |
