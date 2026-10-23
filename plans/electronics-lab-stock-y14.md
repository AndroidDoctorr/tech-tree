# Electronics lab — stocking plan *(side cadence)*

**Filed:** d4985 · **Cal-Y14 D1**  
**Authority:** [electrical-code-1.md](../government/regulations/electrical-code-1.md) · [tools.md](../inventory/tools.md) (`PARTS-PEG-BOARD-1` · `ELEC-COMPONENT-BOX-Y10-1`)  
**Sibling (campus power):** [ec-1-campus-expansion.md](ec-1-campus-expansion.md) — feeders · taps · room lights  
**Main arcs (do not block):** concrete/block runway · **`HYDRO-ELEC-1`** head/Q for fans and heating loads

★ **This is a background queue** — a few hours when wire is already hot, a half-day when a gauge runs thin, or a named “lab afternoon” between hauls. No sprint unless a storage fixture is explicitly opened.

---

## Intent

Keep the **chem / north bench electrical lane** able to **repair a branch**, **trim a standard**, or **swap a bulb** without opening a construction hero. Stock is **labeled lengths and counted parts**, not “somewhere in a drawer.”

---

## What exists today

| Asset | Role |
|---|---|
| **`PARTS-PEG-BOARD-1`** | BN / R / C / L working + spare slots @ chem bench east |
| **`ELEC-COMPONENT-BOX-Y10-1`** | 4-row tray (R · L · C · SW) · felt-lined |
| **`REF-SHELF-1`** | Masters only — not expendable bench stock |
| **`EC-1-WIRE-SAMPLE-SET-Y13-1`** | Gauge masters @ 14 °C — **do not draw from** |
| **Wire bank** | [resources.md](../inventory/resources.md) § Copper wire |
| **`FUSE-LINK-Y14-1`** | **×1** in chem peg pouch *(many spent on commission)* |

**Wire @ d4989:** **`WIRE-CU-GEN2-1` ~30.5 m comfort** · **`WIRE-CU-4` ~0.6 m tail** · lab spools per [resources.md](../inventory/resources.md).

---

## Runway targets *(order-of-magnitude · restock when below “min”)*

### Copper wire *(draw bench · malachite or `WIRE-CU-4` feed)*

| Gauge | Min | Comfort | Peg / location | Typical use |
|---|---|---|---|---|
| **0.9 mm** `WIRE-CU-GEN2-1` | **~15 m** | **~40 m** | Chem peg | Trunk reserve · gen-2 extensions |
| **0.65 mm** | **~6 m** | **~15 m** | Parts peg **`WIRE-*`** bay | Armature · motor branch class |
| **0.5 mm** | **~10 m** | **~25 m** | Parts peg **`LAB`** spool | EC-1 branch · lamp pairs |
| **0.3 mm** `CU-WIRE-Y10-3` + lab spool | **~15 m** | **~35 m** | Rack + peg | Fuses · standards · galvanometer |
| **1.6 mm** `WIRE-CU-4` | **~3 m** | **~12 m** | Chem porch | Draw feed only · **~10.6 m @ d4988** |

**Cadence:** **⟳** one **~½–1 h** draw pass when a row crosses **min**; **⚒** full day when **two or more** gauges are red or after a big EC commission.

### Fuses · switches · hardware

| Item | Min | Comfort | Notes |
|---|---|---|---|
| **`FUSE-LINK-Y14-1`** (0.3 mm × ~8 cm) | **×6** | **×12** | Pouch @ chem peg · **cut from 0.3 mm spool** |
| **`SW-KNIFE-BLANK-1`** | **×2** | **×4** | Forge from strip when named — queue with fuse batch |
| **Brass binding posts / clips** | spare pair | **×2 sets** | `ELEC-COMPONENT-BOX` row SW |
| **`NAIL-IRON` / tap screws** | campus tray | — | Cleat grammar only |

### Resistors · inductors · caps *(working + spare)*

| Class | Min | Comfort | Source |
|---|---|---|---|
| **R** 1 / 10 / 100 class | **1 working + 1 spare each** | **×2 spare tier @ d4991** | **`R-WORK-*` / `R-SPARE-*-1` / `R-SPARE-*-2`** |
| **L** air-core matched | **1 working + 1 spare** | duplicate former | **`L-WORK-1` / `L-SPARE-1`** |
| **C** waxed-paper pair | **2 matched** | **4+** | **`C-WORK-*` / `C-SPARE-*` / `C-BENCH-Y14-*`** · **×8 @ d4990** |
| **Tap wire** | **~25 cm** | **~1 m** | **`SW-TAP-WIRE-1`** |

**Cadence:** **⟳** trim afternoon when bridge/null work drifts — not tied to wire draw.

### Lamps · bulbs *(replacement, not production line)*

| Class | Min | Comfort | Notes |
|---|---|---|---|
| **Sealed feast / wing bulb** | **`BULB-LAMP-SPARE 10–17` ×8 loose** | **×2–3** | **Open kit queue ✓ d5271 · room hangs queue** |
| **Open / glass tail** | **`BULB-HW-OPEN-CY14-5`** · **`Y14-19` glass** · **~×1 reed** | — | Vac when named |
| **Glass-only shells** | **`Y14-18/19` ×2** | — | Next stem days |
| **Socket + pigtail assembly** | **`BULB-FEAST-SOCKET-Y14-9` ✓ d5268** | **×2** | **Unhung spares** |
| **Filament / reed practice** | study peg | — | Scrap pinch stems — not counted as spares |

**Cadence:** **⚒→⧗** vac afternoon when **min = 0** installed spares; batch **×2** when Hg header is already hot.

---

## Storage vision *(build when named — not required for stocking)*

| Piece | Function | Status |
|---|---|---|
| **`WIRE-RACK-LAB-1`** *(planned)* | Horizontal pegs · paper tags **`0.3` / `0.5` / `0.65` / `0.9` / `COATED`** · coil hangs | **⚑** extend **`PARTS-PEG-BOARD-1`** north row first |
| **`ELEC-COMPONENT-BOX-Y10-2`** or **divider insert** | Second tray: **FUSE · BULB · SW · MISC** | **⚑** when fuse pouch overflows |
| **Labeled cells** | **`ELEC-PART-LABEL-KIT-Y14-1` ✓ d4993** | **⟳** maintain on any trim day |
| **`RESISTOR-COLOR-CHART-Y14-1`** | **✓ d4993** — table + diagram · **body bands ⚑** — see pigment ladder below | North wall |
| **`EM-LAWS-CHART-Y14-1`** | **✓ d4998** — Ohm · Kirchhoff · Maxwell **∇· / ∇×** · bench hooks | North wall |
| **`RC-LAB-NOTES-Y14-1`** | **✓ d4995** — τ vs **C-WORK** vs **~1.4× C** | Chem peg folder |
| **`L-CORE-NOTES-Y14-1`** | **✓ d4996** — air vs solid vs lam blanks | Same folder |
| **`L-WORK-IRON-SOLID-Y14-1` · `L-WORK-IRON-LAM-Y14-1`** | **✓ d4997 · 118 t · LC ring-down vs air** | Peg slot L |

### Pigment ladder *(chart queue — not all organic)*

| Swatch | Path | Gate |
|---|---|---|
| **Black / red / blue** | Soot · hematite · Prussian | **✓ on chart** |
| **White / gray** | Chalk or kaolin slip · soot dilute | **Mineral · ~next** |
| **Yellow-brown** | Campus ochre / iron earth wash | **Mineral · scout** |
| **Red-orange lake** | **`MADDER-ROOT-DRY` + alum** on paper | **Dye chem · queued** |
| **Green** | Terre verte class earth · or blue+yellow when both honest | **Mixed** |
| **Bright yellow / orange / violet** | Lead-tin yellow · orpiment class · coal-tar era | **Heavy inorganic / far organic** |
| **Chem east shelf map** | One-line chalk: *gauge → peg* | **⟳** update when wire moves |

★ **Do not mix masters and stock** — `REF-SHELF-1` and **`EC-1-WIRE-SAMPLE-SET`** stay isolated.

---

## Triggers *(agent / player — “lab is thin”)*

| Signal | Action |
|---|---|
| Any wire row **&lt; min** | Flag in day **Close** · suggest **draw pass** on next HOME bench day |
| **`FUSE-LINK` ≤ ×2** | Cut **×4** from 0.3 mm spool · **15 min** |
| **EC commission spent trunk** | Restore **`WIRE-CU-GEN2-1`** to **comfort** before next feeder extension |
| **Bulb installed count = live + 0 spare** | Queue **vac half-day** |
| **New gauge commissioned** | Add row to resources + peg map same day |

---

## Order of work *(cheap → expensive)*

1. **⟳ Labels + pouch fuse cut** — no forge.
2. **⟳ Draw one gauge** from existing **`WIRE-CU-4`** or **`WIRE-CU-GEN2-1`** tail.
3. **⚒ Malachite → rod → multi-gauge draw** — when feed coil **&lt; ~3 m**.
4. **⚒ Trim standard decade** — when metrology work is already open.
5. **⚒ Vac bulb ×2** — when spare band empty.
6. **⚒ `WIRE-RACK-LAB-1` / second box** — furniture hero · defer.

---

## Campus power *(related · separate queue)*

Count **buildings**, not wheelhouse trunks — see [ec-1-campus-expansion.md](ec-1-campus-expansion.md) § Building feeders.

| Building | Feeder | Notes |
|---|---|---|
| **Officina** *(one compound)* | **`FEEDER-2` only** · **`SW-CRAFT-FEEDER-1`** | **✓ d4987** · north bus-tied · **`FEEDER-3` trunk → Fabrica** |
| **Fabrica** | **`FEEDER-1` chem + `FEEDER-FABRICA-1` hub** | **✓ building buses d4987** · branches ⚑ |
| **Domus** | Margin on Feeder-2 | Culina lamp ✓ · rooms mostly dark |
| **Horreum · garage** | None | Defer / Phase 4 |

**Next EC work** (side, non-blocking): **land `FEEDER-FABRICA-1`** · chem lab lights on **`GRID-TAP-CHEM-1`** · Officina room lights · Domus chase.

---

## Log grammar

- **Wire credit:** patch **`inventory/resources.md`** § Copper wire · one row per **gauge + location**.
- **Fuse / trim:** patch **`FUSE-LINK`** count or note **×N cut @ d####** in day file only if qty unchanged on a working pouch.
- **Plan changes:** edit this file · bump **Filed** line · **do not** duplicate targets in `now.md`.

---

*Revise targets after first **`WIRE-RACK-LAB-1`** build or when **`EC-1`** room count jumps past ~6 branches.*
