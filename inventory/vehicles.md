# Vehicles

The most detailed entries in the inventory, and deliberately so — a vehicle is the only item that carries the player and a load away from the campus, so a thing you failed to check is a thing you find out about at distance.

Block shape, as [infrastructure.md](infrastructure.md). Fittings are listed under their vehicle rather than as their own rows: a yoke pad is only meaningful as part of the wagon it pads.

---

## `WAGON-V2-CHASSIS-1` — **Norima**
Map: `CART-YARD` south · Status: **default hauler · HOME** · Wear: **38** · Last out: **d3415 Ghab seed return**

The working wagon. Bulk dry aft. Ice kit stowed, wet rig staged.

**Wear 38 is a live number, not a note.** It feeds the `CART-WHEEL-MISHAP` and `WAGON-HUB-BIND` rolls as a modifier — see [hazards.md](../hazards.md). Patch it here when it changes, because the hazard table reads it from this row.

### Fittings

| ID | Fitting | State |
|---|---|---|
| `WAGON-V2-COVER-ARCH-1` | Cover arch — chassis · ribs · ridge · hoops · braces | ✓ **cover mounted · outer oilcloth d3408** |
| `WAGON-REAR-HITCH-1` | Pintle receiver at tail · latch · safety chain | Pod ghost PASS |
| `WAGON-LANTERN-HOOK-1` | Lantern hook, cover arch fore rib · portable lantern swap | Live |
| `WAGON-DASH-SHELF-1` | Dash shelf, driver bench rail · wick tin · wrench ghost | Live |
| `WAGON-SEAT-PAD-1` | Driver bench pad, deer leather, flax/hemp fill | Live |
| `WAGON-YOKE-PAD-1` | Team yoke pads ×2, deer leather, hemp/flax loft | Live |
| `WAGON-V2-RIP-TAIL-1` | Rip tail | ×0 spent → became a cover rib pair |

Cover cloth stock is a resource, not a fitting — `CLOTH-WAGON-COVER` in [resources.md](resources.md), ~2.08 kg on the `CART-YARD` south peg row.

### Open

✓ **`WAGON-GARAGE-1` @ `CART-YARD` south** — **stem d3375 · frame d3376–3378 · roof d3379.** Norima parks under cover; arch can stay closed.

> **Phased utility bay** @ south pad (not north passage). Block mix break PASS d3370.

---

## `COVERED-WAGON-1`
Map: `CART-YARD` south · Status: live, roadworthy · Last: d3093

The v1 wagon, **never named**. ★ **Museum / train lane — not to be cannibalised.** Kept roadworthy rather than retired, so it is a genuine second vehicle and not an exhibit.

`CART-IRON-RIM-1` — both wheels fully banded since d1877, wobble ~1 mm class.

---

## Carried kit

Stowed on a vehicle rather than at a bench, so it travels whether or not anyone remembers to pack it.

| ID | Item | Qty | Where |
|---|---|---|---|
| `TRAIL-MAINT-SLICE` | Trail maintenance stock | ~1.9 kg at wagon · ~2 kg at bench | Wagon |
| `EXPED-ROPE-WAGON` | Hemp rope | ~6 m | Wagon |
| `WAGON-V2-COVER-THATCH-TEMP-1` | Temporary thatch cover · M-08 removable | — | Cart yard peg — **pulled for the ice band** |
| `CART-POWDER-SAFE-1` | Powder safe | ☠ **×0 caps** — empty at cart and at HOME safe | Cart |
| `BRIDGE-SPARE-KIT` | Bridge spare kit | ×0 · caps ×6 at safe | Cart |

⚠ **Both powder stores read zero.** `BLAST-CAP` ×4 are in the HOME powder safe ([resources.md](resources.md)) but the cart safe is empty, so nothing is travelling. That is fine until a trip needs a blast and finds out at distance.

---

## `LELYA` — *placeholder*
Not built.

---

## Notes

Animals that pull are not vehicles. Donkeys are [animals.md](animals.md); the yoke and its pads are fittings above.
