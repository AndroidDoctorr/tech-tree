# Atelier → Officina (Day 4112)

**Authority:** Player — Latin naming consistency with **Domus** · **Fabrica** · campus grammar.  
**Effective:** Cal-Y13 D238 · d4112.

---

## What changed

| Live docs | Change |
|---|---|
| **[officina.md](../../map/campus/officina.md)** | Building map file *(was `atelier.md`)* |
| **Map · plans · inventory live rows** | Display name **Officina** where the *building* is meant |

**Closed day files are not rewritten.** Journal history still says **Atelier** wherever it was logged that way.

---

## How to read old text

| Old wording | Read as |
|---|---|
| **Atelier** *(building)* | **Officina** |
| **`M2` hub / east pad / craft wing @ mid-campus** | Same place — **Officina compound** |
| **`ATELIER-*` asset IDs** | **Unchanged** — e.g. `WORK-TABLE-ATELIER-1` · `ATELIER-WINDOW-W-1` · `ATELIER-RUG-1` |
| **`EC-1-GRID-FEEDER-2` "Atelier craft wing"** | Same feeder · same **`CRAFT-WING-1` east jamb** |
| **"W-1 north rafter" dry peg row** | Still the **Officina storage/craft dry queue** — legacy W-1 pad tag |

---

## Why not rename every ID

Inventory and day-file IDs are **audit trails**. Renaming `WORK-TABLE-ATELIER-1` would fork the ledger for no gain. The building name and the map file carry the live label; asset tags stay as filed.

---

## Related retcons

- [ATELIER-W1-PAD-1920.md](ATELIER-W1-PAD-1920.md) — W-1 pad → craft wing replacement *(still valid; "Atelier" there = this building)*
