# Powered-machine service

**Applies to:** `LATHE-V2` · `BORING-MILL-1` · `DRILL-PRESS-1` · `TABLE-SAW-1` · `BELT-TREE-1` and their reduction boxes.

> A lathe head is not sharpened. **Cutting edges are sharpened; the headstock is aligned, lubricated, adjusted, scraped, or rebushed.**

## Cadence

| Trigger | Work |
|---|---|
| Before every powered session | Belt isolated → hand-spin · oil cup / plain bush · cutting edge · guards · loose keys |
| Before precision work | Test bar or reference cylinder · spindle play · center alignment · feed backlash |
| Full service | **Annually or after ~40 powered hero-days**, whichever comes first |
| Immediate stop | Hot bearing · knock · belt walking off crown · chatter that survives a sharp tool · measurable taper |

Calendar time matters even when use is light: oak moves with humidity, leather belts stretch, lubricant dries, and bright iron rusts. Cutting-tool wear follows powered cutting time instead.

## What wears

| Part | Normal service | Replace when |
|---|---|---|
| Cutting bit / boring tip | Stone or grind rake and clearance · retemper if needed | Edge chips, case is ground through, or geometry cannot be restored |
| Bronze plain bush | Flush grit · oil · take up split/cap · scrape high spots | Scored or oval after adjustment; runs warm under ordinary load |
| Headstock / tailstock | Re-level · shim · align centers | Crack, bent spindle, or adjustment range spent |
| Ways / saddle / gib | Wipe abrasive dust · oil/tallow film · take up gib | Galling, hollow wear, or persistent rock |
| Leadscrew / nut | Clean · oil · measure backlash · adjust split nut | Backlash remains above the work limit after adjustment |
| Leather belt | Clean · dress lightly · re-tension · align crowns | Glazed through, cracked, delaminated, or splice pulls |
| Wooden gears / pulleys | Tooth/pin and hub-key read · wax/tallow trace | Split hub, loose pin seat, or tooth profile lost |
| Saw blade | Sharpen and restore equal set · check arbor and splitter | Cracked plate, lost temper, or missing teeth |

## Full service — `POWERED-MACHINE-SERVICE-*`

1. **Lock out water power:** gate branch, drop every quick-release, prove hand-spin only.
2. Clean before measuring; grit can imitate wear.
3. Record **before and after** values against the same test bar / reference.
4. Service the lathe and boring mill first; they make replacement parts for the rest.
5. No-load spin, then sacrificial cut. A free spin alone does not prove alignment under cutting load.
6. Patch the service register in [infrastructure.md](../../inventory/infrastructure.md).

## Campus limits

These are honest limits for the present wood-bed, plain-bearing machines—not modern machine-tool tolerances.

| Read | GREEN | Service / AMBER |
|---|---:|---:|
| Lathe spindle radial play | **≤~0.08 mm** | **>~0.12 mm** |
| Test-bar runout @ 50 mm | **≤~0.10 mm** | **>~0.15 mm** |
| Tailstock center offset | **≤~0.10 mm** | **>~0.15 mm** |
| Leadscrew backlash | **≤~0.35 mm** after take-up | **>~0.50 mm** |
| Boring-mill spindle play | **≤~0.08 mm** | **>~0.12 mm** |
| Belt slip at rated cut | **≤~5%** | **>~8%** |

Crossing AMBER does not mean scrap. Adjust, scrape, shim, sharpen, or rebush; replace the assembly only after those fail.
