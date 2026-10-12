# Bulb characterization ledger

**Procedure:** Every sealed lamp that ships or mounts for service gets **one row** here after **`BULB-CHAR-SWEEP-*`** on the bench. Copy the sweep table from the day file; do not re-measure from memory.

**R&D compares · filament prep · relative brightness:** [bulb-rd-log.md](bulb-rd-log.md) — **`BULB-RD-COMPARE-*`** after **d4582**.

## How to measure *(EC-1 · gen ON · bank ties OFF for stable E)*

| Step | Tool | Note |
|---|---|---|
| **E @ tap** | **`RHEOSTAT-CLIP-1` + tap tags** | Read **GB** at the **same tap** that feeds the lamp |
| **I** | **Series clip @ branch** | **Dim sweep:** **~0.4 · 0.7 · 1.0 · 1.1 · 1.3 I** *(stop below fuse class)* |
| **R (hot)** | **E / I** @ each sweep point | Filament **hot** — expect **R_hot > R_cold** |
| **P (heat)** | **E × I** · **GB·I** | *Dissipated in the envelope + lead losses* |
| **Operating point** | **Named dim** | Feast grammar · room grammar · or bench max |

★ **Cold R optional:** lamp **OFF** **>5 min** · **one** clip read @ **~0.05 I** tickle — log **R_cold** only when comparing filaments.

## R&D queue *(not blocking production)*

| ID | Intent |
|---|---|
| **`BULB-FILAMENT-ALT-1`** | Second filament stock in a new envelope · **`CARBON-FILAMENT-FINE-Y14-1`** vs standard stock |
| **`BULB-CARBONIZE-HIGH-T`** | Muffle **higher band** carbonization · less ash · finer grain |
| **`BULB-PRESEAL-OUTGAS`** | Heat glass · **I through loop** before tip-off · **✓ grammar d4567** |
| **`BULB-FILAMENT-REED-1`** | **✓ `BULB-LAMP-POC-Y14-3` d4579** · **`BULB-PROD-Y14-5` spare hardware** · **`P-08-FILAMENT-A` winter cut Jan–Mar** |
| **`MCLEOD-GAUGE-1`** | Vacuum quality read · **Hg manometer grammar** · not dial gauge fantasy |

---

## Production log

| Lamp ID | Filament | Seal day | E band @ tap | I_op | R_hot @ op | P @ op (GB·I) | Glow note | Char day |
|---|---|---|---|---|---|---|---|---|
| **`BULB-LAMP-POC-Y14-1`** | **`BULB-PROD-Y14-2`** · carbon loop · standard draw | d4479 | **GEN-MID** ~6.55 GB @ desk | **~1.10 I** dim | **~5.95 GB/I** | **~7.2 GB·I** | Orange thread · prestige not room | **d4565** |
| **`BULB-LAMP-POC-Y14-2`** | **`BULB-PROD-Y14-3`** · **`CARBON-FILAMENT-FINE-Y14-1`** · outgas d4567 | d4567 | **GEN-MID** ~6.52 GB @ bench | **~1.15 I** | **~5.67 GB/I** | **~7.5 GB·I** | Tighter thread · **~22 s @ ~1.4 I** | **d4567** |
| **`BULB-LAMP-POC-Y14-3`** | **`BULB-PROD-Y14-4`** · **`REED-CARBON-FILAMENT-STOCK-Y14-1`** · outgas d4578 | d4579 | **GEN-MID** ~6.50 GB @ bench | **~1.15 I** | **~5.65 GB/I** | **~7.5 GB·I** | Steady ribbon · **~19 s @ ~1.35 I** · scout | **d4579** |

### **`BULB-LAMP-POC-Y14-1` — sweep d4565** *(desk · `GRID-TAP-CRAFT-1` · gen ON)*

| I | E @ tap (GB) | R_hot (GB/I) | P (GB·I) |
|---|---|---|---|
| 0.42 | 6.72 | 16.0 | 2.82 |
| 0.68 | 6.68 | 9.82 | 4.54 |
| 0.95 | 6.61 | 6.96 | 6.28 |
| 1.10 | 6.55 | 5.95 | 7.21 |
| 1.28 | 6.46 | 5.05 | 8.27 |

**R_cold** *(tickle ~0.05 I):* **~42 GB/I class** — not comparable to hot op without correction.

### **`BULB-LAMP-POC-Y14-2` — sweep d4567** *(vac header · bench clip)*

| I | E (GB) | R_hot (GB/I) | P (GB·I) |
|---|---|---|---|
| 0.40 | 6.70 | 16.8 | 2.68 |
| 0.72 | 6.65 | 9.24 | 4.79 |
| 1.00 | 6.58 | 6.58 | 6.58 |
| 1.15 | 6.52 | 5.67 | 7.50 |
| 1.40 | 6.44 | 4.60 | 9.02 |

### **`BULB-LAMP-POC-Y14-3` — sweep d4579** *(reed · vac bench clip)*

| I | E (GB) | R_hot (GB/I) | P (GB·I) |
|---|---|---|---|
| 0.38 | 6.68 | 17.6 | 2.54 |
| 0.70 | 6.62 | 9.46 | 4.63 |
| 0.95 | 6.56 | 6.91 | 6.23 |
| 1.15 | 6.50 | 5.65 | 7.48 |
| 1.35 | 6.43 | 4.76 | 8.68 |
