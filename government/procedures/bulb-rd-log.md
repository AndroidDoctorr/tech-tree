# Bulb R&D log

**Companion to** [bulb-characterization-ledger.md](bulb-characterization-ledger.md).

- **Ledger** = production lamps after seal · one **char sweep** row per service mount.
- **R&D log** = every **bench compare** or **filament variant** · prep chain · relative brightness · notes for the next build.

## When to file

| Event | Where |
|---|---|
| New sealed lamp · first energize | **Ledger** sweep + optional **R&D** row if filament prep changed |
| Side-by-side bench compare | **R&D log** table below |
| Filament stock change only | **R&D** row · ledger unchanged until sealed |

## Electrical block *(same as ledger)*

**GEN ON · bank ties OFF · fixed tap tag on every row.**

| Field | How |
|---|---|
| **Tap** | e.g. **`GRID-TAP-CRAFT-1` GEN-MID** |
| **I sweep** | **0.4 · 0.7 · 1.0 · 1.15 · 1.35 I** *(stop below fuse)* |
| **E @ tap (GB)** | **`RHEOSTAT-CLIP-1` + tap read** |
| **R_hot** | **E / I** |
| **P** | **E × I (GB·I)** |
| **R_cold** | Optional · lamp OFF **>5 min** · **~0.05 I** tickle |

## Luminance block *(relative — no lux meter)*

Absolute lumens are **not** on the bench yet. Use a **fixed geometry** every time:

| Fixture | Spec |
|---|---|
| **Card** | **`REF-WHITE-CARD-1`** @ **1.00 m** from bulb centre · normal to axis |
| **Room** | **Dark bay** · one **`TALLOW-CANDLE-REF-1`** @ same distance when calibrating |
| **Method A — grease spot** | **`GREASE-SPOT-PAD-1`**: oil on translucent paper · adjust lamp **I** until reflected spot **matches** filament glare on card · record **I_match** |
| **Method B — patch match** | Same **I** on all lamps under test · rank **patch brightness** on card **1–5** vs candle @ known **I_candle** |
| **`L_rel`** | **Patch score / standard lamp score** @ **same I and geometry** · **1.00 = reference lamp that day** |

★ **Compare filaments at matched P (GB·I), not only matched I** — when R differs, add a second column at **~7.5 GB·I class**.

## Filament prep block *(copy from day file)*

| Field | Example |
|---|---|
| **Stock ID** | **`CARBON-FILAMENT-FINE-Y14-1`** · **`REED-CARBON-FILAMENT-STOCK-Y14-1`** |
| **Source fibre** | Flax line tow · reed **`P-08`** ribbon |
| **Carbonize** | Muffle **~440 °C · ~55 min** · binder trace |
| **Draw** | Hand **~0.28–0.32 mm** |
| **Loop** | Hairpin **~52 mm** · centred |
| **Outgas** | **Y/N** · **I** · **~s to clear wisps** |
| **Vac** | Fall count · pump strokes · **hold candle s** *(McLeod when live)* |

## R&D compare log

| Day | Lamp | Filament prep | Tap | I_test | P (GB·I) | L_rel @ I | L_rel @ matched P | Notes |
|---|---|---|---|---|---|---|---|---|
| **d4582** | **`BULB-LAMP-POC-Y14-1`** | Standard flax carbon · d4452 class | CRAFT-1 MID | 1.15 | 7.21 | **1.00 ref** | **1.00** | Wide orange thread |
| **d4582** | **`BULB-LAMP-POC-Y14-2`** | Fine elite · outgas d4567 | CRAFT-1 MID | 1.15 | 7.50 | **1.25** | **1.20** | Tightest patch |
| **d4582** | **`BULB-LAMP-POC-Y14-3`** | Reed scout · outgas d4578 | CRAFT-1 MID | 1.15 | 7.48 | **0.90** | **0.93** | Broad ribbon · even wash |

## Brightness levers *(before tungsten / osmium)*

| Lever | Effect | Cost |
|---|---|---|
| **Finer draw + shorter loop** | Higher filament temperature at same P · **brighter thread** | Breakage · needs fine stock |
| **Pre-seal outgas** | Less flash at seal · **stable hot R** | Time · ✓ grammar live |
| **Harder vac** | Less gas conduction loss in envelope | Pump time · **McLeod** read |
| **Higher-T carbonize** | Denser char · less ash | Muffle band · R&D queue |
| **Matched P testing** | Fair compare · not fooling yourself with low R | Discipline |
| **Socket / lead I²R** | More power at filament · less in copper | Heavier leads · tap headroom |

## Not on the bench yet

| Idea | Verdict |
|---|---|
| **Fluorescent tube** | Needs **low-pressure gas discharge + phosphor + lead-in wires through glass** · UV pump is the hard part · **feasibility note only** — see **`BULB-FLUOR-SCOUT`** when chem/glass band opens |
| **Absolute photometry** | **Grease spot → relative** until a calibrated oil-lamp or candela standard is built |
