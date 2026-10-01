# Manufacturing Code 2 *(MFGC-2)*

**Opened:** Day 3742 · **Cal-Y12 D223** · **~12 Aug Y12**
**Scope:** alloy melts, heat identity, master-alloy references, assay linkage @ HOME campus
**Related:** [manufacturing-code-1.md](manufacturing-code-1.md) · [measurement-code-1.md](measurement-code-1.md) · [heat-register-y12.md](heat-register-y12.md)

> ★★ **The heat is the unit of record, not the bar.** Charge sheet in · poured coupon or stock out · assay against the coupon · heat ID stamped on retained metal.

---

## Intent

**MFGC-1** covers fasteners, pipe, and workshop mechanical stock. **MFGC-2** opens when homogeneous alloys and registered furnace melts need a **heat register**, **master-alloy table**, and **assay cross-reference** — the steel and master-alloy programme, not case-hardened bar stock.

☠ **`CS-BAR-Y12-*` are case-hardened wrought iron, not steel.** They do not receive MFGC-2 heat IDs until a true melt cert exists.

---

## MFGC-2-HEAT-ID — heat identity

| Field | Rule |
|---|---|
| **Grammar** | **`HEAT-Y12-{seq}`** — seq = **4-digit zero-padded** issue order from register *(000 reserved · 001 first full row)* |
| **Stamp** | Heat ID on **coupon**, **retained button**, or **stock tag** — same ID on charge sheet and assay row |
| **Furnace** | **`FURNACE-2` · `MUFFLE-1` · forge micro-melt** — name the vessel |
| **Pre-register** | Exploratory melts before d3742 may appear as **`HEAT-Y12-000-*`** annotation rows — not production heats |

---

## MFGC-2-CHARGE — charge sheet *(minimum fields)*

File one charge sheet per heat before pour (copy → [heat-register-y12.md](heat-register-y12.md)).

| # | Field |
|---|---|
| 1 | **Heat ID** |
| 2 | **Date / day** |
| 3 | **Furnace + atmosphere** *(oxidising · reducing crucible · charcoal pack · luted lid · bleed setting class)* |
| 4 | **Charge masses** — ore · flux · alloy addition · char · every row ID from inventory |
| 5 | **Temperature evidence** — cone witness · **`THERMOCOUPLE-1`** row when live · soak time class |
| 6 | **Pour target** — stock ID to create or replenish |
| 7 | **Coupon** — fracture · spark · combustion C · bridge drift — name the test |
| 8 | **Assay ID** — link to assay register row |
| 9 | **Verdict** | **PASS · HOLD · SCRAP** |

---

## MFGC-2-MAST — master-alloy table *(live references)*

| Master ID | Role | Campus stock | Notes |
|---|---|---|---|
| **`FMN-STD-Y12-1`** | Ferromanganese charge reference | ×3 staged d3615 | From **`M31-ASSAY-Y12-1`** composite |
| **`NI-STD-A/B/C`** | Nickel reduction standard | ~13 / ~9 / ~13 g remain d3734 | **`NI-REDUCTION-STD-Y12-1`** |
| **`CONSTANTAN-STD-Y12-1`** | Cu–Ni drift-minimum alloy | stub ~3.1 g + **`TC-CONST-LEG-1`** | Run D recipe on bridge label |
| **`CAST-IRON-BUTTON-Y12-1`** | Cast iron trial button | ~167 g | **`HEAT-Y12-000-1`** exploratory · **~3.6 % C** |
| **`CAST-IRON-BUTTON-Y12-2`** | Cast iron practice button | ~163 g | **`HEAT-Y12-001` PASS** |
| **`CAST-IRON-BUTTON-Y12-3`** | Cast iron practice button | ~165 g | **`HEAT-Y12-002` PASS** |
| **`CAST-IRON-BUTTON-Y12-4`** | Cast iron practice button | ~164 g *(chip)* | **`HEAT-Y12-003` PASS** |
| **`CAST-IRON-BUTTON-Y12-5`** | Cast iron practice button | ~163 g *(chip)* | **`HEAT-Y12-004` PASS** |

| **`MAG-STEEL-Y13-ROD-1/2/3`** | Magnet steel pole rod set · **`ST-MAG-1` certified triplicate** | **~71–72 g each** | **`HEAT-Y13-009`–`011` · ~1.0 % C on 009 · lift ~43–44 mm d3903** |
| **`FMN-BUTTON-Y12-1`** | Ferromanganese master · **`FMN-STD-A`** | **~65 g** *(chip drawn d3898)* | **`HEAT-Y12-006`** |

⚑ **Ferronickel · ferrochrome · `ST-STR-1` · `ST-SPR-1`** — add rows when melts certify.

---

## MFGC-2-ASSAY — assay register

Assay events that **close or reopen** a heat verdict get a row in [heat-register-y12.md](heat-register-y12.md) **Assay log** section.

| Assay ID grammar | **`ASSAY-Y12-{seq}`** |
| Method column | combustion C · fracture · spark · cupellation · bridge null · wet chemistry |
| Link | **Heat ID** + **coupon mass** + **verdict** |

★ **Pyrometry calibration rows** *(ice · boil · Sn · Zn)* live under **`THERMOCOUPLE-1`** until a heat uses them — then cross-ref heat ID in the assay log.

---

## MFGC-2-STOCK — stamped stock rule

| Rule | Application |
|---|---|
| **One heat → one primary pour ID** | Split pours share heat ID · note split in register |
| **Remelt** | New heat ID · parent heat noted in charge sheet |
| **Expendable crucible melts** | Heat ID on **coupon/button only** if stock is not inventory-grade |

---

---

## MFGC-2-CI — cast iron rhythm *(opened d3802)*

**Vessel:** **`FURNACE-2`** · half-plugs **LIVE** · hot blast **bleed ~½** · reducing **crucible only** *(plan d3586)*.

| Step | Rule |
|---|---|
| **1 · Gate** | Stack draw · duct joints · **`SMOKE-SPOT`** · **`FORGE-PPE-1`** before lit |
| **2 · Grate** | **`CHAR-LANE` ~2.8–3.2 kg** even bed · ash pit weep |
| **3 · Crucible** | **`H-11-HEMATITE` ~1.05 kg** crumbs + char pack **~1.0–1.1 kg** · lid · sand lute · expendable **`P-LAB-CRUC-2`** |
| **4 · Soak** | Hot blast on · vent via cracked half-plugs · **~50–55 min** class to even pool |
| **5 · Bank** | Fire out · freeze in place · eve chill |
| **6 · Coupon** | Grey fracture · speckle class · spark vs **`CAST-IRON-BUTTON-Y12-1`** reference |
| **7 · Register** | New **`HEAT-Y12-{seq}`** · charge sheet fields per **MFGC-2-CHARGE** · combustion C before **PASS** production |

**Exploratory:** **`HEAT-Y12-000-1`** · **`CAST-IRON-BUTTON-Y12-1`** ~3.6 % C (**`ASSAY-Y12-002`**).

**Practice / production row 1:** **`HEAT-Y12-001`** · **`CAST-IRON-BUTTON-Y12-2`** · **PASS** (**`ASSAY-Y12-003`** ~3.5 % C).

**Row 2:** **`HEAT-Y12-002`** · **`CAST-IRON-BUTTON-Y12-3`** · **PASS** (**`ASSAY-Y12-004`**).

**Row 3:** **`HEAT-Y12-003`** · **`CAST-IRON-BUTTON-Y12-4`** · **PASS** (**`ASSAY-Y12-005`**).

**Row 4:** **`HEAT-Y12-004`** · **`CAST-IRON-BUTTON-Y12-5`** · **PASS** (**`ASSAY-Y12-006`**).

> ★ **`MFGC-2-CI` cast-iron rhythm certified d3812** — **`001`–`003` fracture + ~3.5 % C repeat.**

---

## Split from MFGC-1

| MFGC-1 keeps | MFGC-2 owns |
|---|---|
| **PT-*** pipe · **BN-*** fasteners · WI hoop placeholders | Heats · master alloys · assay linkage · **`ST`** homogeneous steel when certified |

Update [manufacturing-code-1.md](manufacturing-code-1.md) **MFGC-1-FUTURE** when **ST** column migrates here.
