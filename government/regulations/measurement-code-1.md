# Measurement Code 1 *(MC-1)*

**Filed:** Day 3558 · **Cal-Y12 D39** · **~8 Feb Y12**
**Scope:** every dimensional, mass, and temperature reference @ HOME campus and future stakes
**Related:** [manufacturing-code-1.md](manufacturing-code-1.md) · [electrical-code-1.md](electrical-code-1.md) · [storage-code-1.md](storage-code-1.md) SC-1.2

---

## Intent

Codify the **gen-3 metrology chain** already proven in **`METROLOGY-SPRINT-Y10`** — flatness, length, mass, and stated temperature — so manufactured parts cite **one government table**, not bench memory.

> ★★ **A standard is only a standard if its conditions are stated.** MC-1 is where those conditions live.

---

## MC-1-REF — reference environment

| Quantity | Campus standard | Notes |
|---|---|---|
| **Temperature** | **14 °C** | **`METROLOGY-CELLAR-1` @ `CAVE-1` upslope** · ~9 °C stable — references only |
| **Length certification** | **14 °C** | Steel and oak masters expand — state T on every cert line |
| **Mass substitution** | **14 °C** | **`MASS-REF-100-1` · `MASS-REF-1000-1`** @ `REF-SHELF-1` |
| **Humidity** | **Stated, not controlled** | Wood and paper drift — do not certify wood length as primary |

⚑ **Invar length masters · constantan resistance wire** — not campus stock · require **nickel / Fe-Ni alloy lane** · EC-1 §future refs.

---

## MC-1-CHAIN — dependency order

Build and maintain in this order. **Skipping a step orphans everything above it.**

| # | Artifact | Method | Live campus |
|---|---|---|---|
| 1 | **Flat** | Three-plate lap · A-B · B-C · C-A | **`BASALT-DATUM` triplet** |
| 2 | **Straightedge · square** | Off flat · flip test for square | Bench grammar |
| 3 | **Length** | **`CALIPER-1`** · **±0.1 mm class** gen-3 cert | **`REF-WORK-PEG-1`** |
| 4 | **Bore / cylinder** | **`REF-CYL-SET-1`** · **RC-06 · RC-10 · RC-12 · RC-22** | **`METROLOGY-CELLAR-1`** |
| 5 | **Mass** | Substitution nulling @ 14 °C | **`MASS-REF-*`** |
| 6 | **Time** | Pendulum class · small swing | ⧗ **`PENDULUM-1`** queued |
| 7 | **Frequency** | Monochord → tuning fork | ⧗ after time |
| 8 | **Electrical ratio** | See EC-1 | **`R-STD-1` · `SLIDE-WIRE-BRIDGE-1`** |

---

## MC-1-RC — reference cylinder (bore) series

**Nominal ID = cylinder label.** Used for bores, pipe IDs, and go/no-go checks.

| ID | Nominal ID (mm) | Cert class | Primary use |
|---|---|---|---|
| **RC-06** | **6.0** | gen-3 · d3503 | Small bore · BN shank · mill nose |
| **RC-10** | **10.0** | gen-3 · d3503 | **`BORING-MILL-1` trial bore** · pipe small |
| **RC-12** | **12.0** | gen-3 · d3503 | Medium bore · pipe branch |
| **RC-22** | **22.0** | gen-3 · d3503 | Large bore · pipe main class |

**Tolerance band (workshop):** **±0.05 mm** on ID check with **`CALIPER-1`** or plug gauge derived from RC master.

**Extension rule:** new RC sizes require **cellar archive entry + duplicate kitchen slate line** before production use.

---

## MC-1-LEN — length masters

| Class | Material | Rule |
|---|---|---|
| **Primary** | **Wrought steel bar** | BN length masters · **`BN-MASTER-06-S/M/L-1`** |
| **Bench** | **Oak strip** | Layout only — not cert primary |
| **Future** | **Invar** | Low expansion · hot/cold variance work · ⧗ nickel lane |

**Cert format:** *nominal · measured @ 14 °C · instrument · day*

---

## MC-1-NULL — measurement doctrine

| Rule | Application |
|---|---|
| **Null beats reading** | Substitution weighing · bridge balance · slide-wire ratio |
| **State conditions** | Temperature · instrument · which master |
| **One fact once** | Cert lives on the master row — day files cite ID only |
| **Dropped reference** | ☠ **Retire and re-cert** — a broken master is a lie that keeps working |

---

## MC-1-CARE

Per [storage-code-1.md](storage-code-1.md): references **off floor · sealed dry · fitted box · duplicate record off-campus.**

Annual read: flat triplet · caliper against RC-06 · mass null check.
