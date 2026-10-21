# Retcon · Lime kiln stoichiometry · CY14

**Filed:** d5141 player catch · **supersedes** per-load **~4.4 kg CaO from ~4.0 kg stone** in day files *(d4939–d5141 class)*.

## Real reaction

**CaCO₃ → CaO + CO₂** — the **~44%** of mass leaves as gas. Quicklime is **lighter** than limestone charged, never heavier.

| | |
|---|---|
| **Theoretical CaO / CaCO₃** | **~56%** by mass *(56/100)* |
| **~4.0 kg stone** *(good pile 7 class)* | **~2.2 kg CaO** per kiln load *(~90–95% calcination · fines/moisture in feed)* |
| **×2 loads / day** | **~8.0 kg stone → ~4.4–4.8 kg CaO** total *(matches [processing.md](../../government/procedures/processing.md) **~5–10 kg per ×2 run**)* |

**Char per load (~4.8 kg)** is **fuel** — unrelated to CaO mass balance.

## Ledger correction *(inventory truth from d5083 forward)*

| Event | Stone burned | Wrong CaO bank | **Correct CaO** |
|---|---|---|---|
| **d5083** ×2 loads | **8.0 kg** | **~8.8 kg** credited | **~4.4 kg** |
| **d5141** ×1 load | **4.0 kg** | **+4.4 kg** → 13.2 | **+~2.2 kg** → **~6.6 kg** |

Earlier kiln days before d5083 used the same bad multiplier; **no mass draw retcon** unless a hero names a specific pour that consumed the phantom lime. **`QUICKLIME-1` crock** resets to **~6.6 kg @ d5141 close**.

## Going forward

Every **`KILN-A-LIME`** load line: **`CACO3-P7` −~4.0 kg** → **~2.2 kg `QUICKLIME-1`** *(HIT +~0.1 · MISS −~0.1 class)*.
