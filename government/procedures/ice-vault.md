# Ice vault — stock reads and annual melt

**Stock ID:** `ICE-VAULT-STOCK` @ [food.md](../../inventory/food.md)  
**Plant:** `ICE-VAULT-NICHE-2` · `COLD-CELLAR-FAN-1` @ [infrastructure.md](../../inventory/infrastructure.md)

## Problem

Cap-bound mass (**~130 kg** practical) must **draw down over the civil year** (~**30–40 kg** melt + use). Daily melt logs are wrong tool — same doctrine as [ICE-VAULT-DRAW-Y12-Y13](../../journal/retcons/ICE-VAULT-DRAW-Y12-Y13.md) and [ICE-VAULT-DRAW-Y13-Y14](../../journal/retcons/ICE-VAULT-DRAW-Y13-Y14.md).

## Agent workflow — two reads per year

| When | Event | Action |
|---|---|---|
| **~Aug** (summer band) | **`ICE-VAULT-READ`** | Tray/lip read · run calculator **without** ice-break cull · patch `ICE-VAULT-STOCK` |
| **Pre-peak Feb** (before `ICE-HAUL`) | **`ICE-VAULT-READ` + ice-break** | Slush cull east tray · run calculator **with** cull · patch stock · haul gates use **headroom** |

Optional: log a **one-line** `ICE-VAULT-DRAW-CYnn` retcon row in journal/retcons when filing a full year composite (player request or band close).

**Do not** decrement ice on routine campus days.

## Calculator

```bash
python sim/ice_vault.py annual --start <kg>
python sim/ice_vault.py annual --start <kg> --hero-draw <kg>   # e.g. TC bath already logged
python sim/ice_vault.py annual --start <kg> --no-ice-break     # Aug mid-year read
```

### Model (fitted + napkin)

At **full pack** (`start ≈ 130 kg`), one civil year:

| Component | kg/yr | What it is |
|---|---:|---|
| **summer_edge_melt** | **~11.5** | Jun–Sep tray/lip slush — mostly **passive** heat leak through lid seams |
| **milk_niche_cheese** | **~8.5** | Milk crock in niche · cheese cool mass · cellar cold swaps |
| **cellar_turnover** | **~18.0** | Hard blocks sacrificed in repack — **use**, not physics |
| **ice-break cull** | **~1.8** | One-time Feb prep slush *(only when flag on)* |

**Scale:** each component × `min(1, start_kg / 130)` — a half-empty vault loses mass slower.

**Hero draws** (logged days only) **add** on top — e.g. `TC-PROBE` ice bath.

### Napkin check

Passive summer slice ≈ **30 W** average thermal leak × **~10⁶ s** summer ≈ **30 MJ** → **~90 kJ/kg** if spread over **~130 kg** → **~0.7 kg** pure melt per kg pack… **but** edge culls and air exchange dominate; the **~11.5 kg** line is the **fitted** tray/lip behaviour, not a naive U·A calculation. The **turnover** line is **operational**, not thermodynamics.

## Haul gates

Pre-peak read should show **headroom** from calculator output — peak laps fill toward **~130 kg**, not silently carry cap from prior February.
