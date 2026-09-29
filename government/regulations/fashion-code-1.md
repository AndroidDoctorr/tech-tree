# Fashion Code 1 *(FC-1)*

**Filed:** Day 3657 · **Cal-Y12 D138** · **~19 May Y12**  
**Authority:** Player directive *(in-game and real-life uniform alignment)*  
**Related:** [storage-code-1.md](storage-code-1.md) SC-1.3 textiles · [manufacturing-code-1.md](manufacturing-code-1.md) · **`EMMER-STARCH-1`** · **`CL-LAB-COAT-2`** *(d1297)*

---

## Intent

**Clean, fresh clothes are operational infrastructure**, not vanity. FC-1 defines **what “enough” means in rotation**, how **faded-but-sound** garments get **dye refresh** without chasing museum-grade colour, how **worn-out** pieces exit to **rag or bedfill**, and how **laundry chemistry** may be experimented with **carefully**.

> **Preserving exact shade is secondary to hygiene, dryness, and honest wear life.** *Refresh colour when the cloth is still good — do not keep dead dye on dead fibre.*

---

## FC-1-UNIFORM — daily wear *(game and life)*

| Layer | Item class | Notes |
|---|---|---|
| **Torso** | **Psychedelic / tie-dye T** | Primary visual identity · resist + vibrant pools · home **`DYE-VIBRANT-STOCK`** grammar |
| **Legs** | **Jeans** | Heavy twill · **dark blue or black** target *(woad/indigo class — **`CL-WOAD-JEANS-*` slate)* |
| **Under** | **Boxers** | **`CL-BOXER-Y9-1`** line · drawstring class · **rotation depth ≥ socks** |
| **Feet** | **Socks** | Linen foot-wrap or knit class · **one clean pair / day** + wash pair · **`CL-SOCK-Y12-*`** |
| **Footwear** | **Casual or work shoes** | **`BOOT-5`** primary · **`BOOT-4`** backup · tread maintenance separate from FC-1 |
| **Eyes** | **Round brass “steampunk” spectacles** | **`SUNGLASS-YULE-1`** · tint recipe **`TINT-RECIPE-D-Y10`** · not forge **`OPT-1`** *(spark visor)* |

**Forge / kiln / acid heroes** swap to **`FORGE-PPE-1`**, **`CL-LAB-WEAR`**, masks, and heat gear — **not** the daily uniform.

---

## FC-1-PALETTE — piecemeal but coherent

| Category | Target | Rule |
|---|---|---|
| **Jeans · coats** | **Dark blue or black** | Woad/indigo/black overdye refresh · not pastel |
| **Belts · shoes · leather accessories** | **Dark brown** | Tallow/oil care · resole/tread on schedule |
| **Tie-dye / hippie layer** | **Full spectrum** | Intentional chaos · **does not** need to match denim |
| **Steampunk / late C18–early C19 cues** | Brass, round lenses, structured coat when worn | **`SUNGLASS-YULE-1`**, brass hardware, cut lines |
| **Carhartt-chic** | Durable work twill, visible repair, function first | Patches OK · **rot is not** |

★ **Style is piecemeal but legible to the wearer** — FC-1 does not require a single period costume.

---

## FC-1-ROTATION — minimum wardrobe doctrine

**Goal:** **Never run a single point of failure on body layers.** Counts are **targets**, not maximums — adjust when laundry rhythm slips.

| Category | Rotation target | Wear / storage |
|---|---|---|
| **Socks** | **≥4 pairs** *(one/day + wash cycle)* | Vestiarium peg + **`C-0`** wash pair |
| **Underwear (boxers)** | **≥4** | Same peg grammar |
| **Shirts / tie-dye T** | **≥3** | Alternate daily · line dry |
| **Pants (jeans)** | **≥2 dark** | One wear / one dry or refresh queue |
| **Coat** | **≥1 good + 1 backup or rag-boundary piece** | **Low daily wear** — mostly **stored dry** *(see FC-1-COAT)* |
| **Towels** | **Plenty** — **≥6 bath/hand class** for campus + wash lag | **`BEACH-TOWEL` / `CL-TOWEL-*`** precedent · stripe dye optional |

**Lab coats** (**CL-LAB-COAT-2**, smocks): **≥2 in rotation @ chem door pegs** · change-at-door · **not** domus sleep wear.

When rotation drops **below target for any row**, **textile hero precedes cosmetic projects** unless a safety gate blocks work.

---

## FC-1-DYE — refresh policy

| Situation | Action |
|---|---|
| **Fade but fibre sound** | **Occasional dye refresh** — vat or overdye · **match FC-1-PALETTE** for jeans/coat · **vibrant re-pass** for tie-dye |
| **Stain / chemistry** | **`CL-LAB-WEAR`** isolation · **no cross-wash with domus rotation** until cleared |
| **Colour match obsession** | **Not required** — even refresh beats patchy preservation |

Log refresh days with **garment ID + vat + before/after read** in the journal; **do not duplicate full wardrobe state in `now.md`.**

---

## FC-1-END — exit from rotation

| Condition | Disposition |
|---|---|
| **Worn through · torn out · elastic dead** | **Rag stock** **`HIDE-SCRAP` / textile rag bins** |
| **Clean but structurally dead** | **Bedfill / stuffing / patch source** if not gross |
| **Gross contamination** *(bio, tar, unknown chem)* | **Burn or dedicated waste** — **not** bedfill |

★ **Anything that left rotation honestly becomes material**, not guilt.

---

## FC-1-LAUNDRY — wash chemistry *(experimental)*

**Baseline:** **`SOAP-Y10-1`** · ash-soap · hot water when available · **line dry**.

**Experiments — permitted with care:**

| Agent | Use | Guard |
|---|---|---|
| **Detergent class** | Grease + field soil on jeans/work shirts | **Record recipe in day file** · patch test on scrap |
| **Bleach** *(VERY careful)* | Whites · towel refresh · **not** default on indigo/tie-dye | **Dilute · short contact · ventilate · **never** mixed with acid bench same pass** |
| **Starch** | **Lab coat collar/lapel stand** · optional formal shirt | **`EMMER-STARCH-1`** precedent *(d1297)* — **collar/lapel only** on coat · body must still flex · **`SOAP` margin rinse if tacky** |

### Lab coat starch — **yes, done**

**`CL-LAB-COAT-2` close @ d1297:** **`EMMER-STARCH-1`** formal pass · emmer bran paste @ **collar stand and lapel faces** · porch line dry · stone press · **`SOAP-Y10-1` margin if tacky** · hung **chem-lab peg #2**. **Repeat on refresh when collar droops**, not every wash.

---

## FC-1-COAT — low wear, anti-rot

Coats are **event / weather**, not daily uniform.

| Rule | Why |
|---|---|
| **Dry before peg** | Mildew beats moths |
| **Brush · air · shade** | More important than frequent wash |
| **Oil/wax on shell only** when grammar calls | Not on lining |
| **Dye refresh rare** | Dark woad/black overdye when fade shows · structure first |

Stored **off floor · ventilated peg · not compressed under wet heap** per SC-1.

---

## FC-1-RECORD

| Rule | Application |
|---|---|
| **One fact once** | Garment state on **`inventory/tools.md`** or textile rows · day file owns hero |
| **FC-1 is policy** | **`now.md`** cites **rotation gaps**, not every sock |
| **Real-life mirror** | Player may update FC-1 when off-campus wardrobe doctrine shifts |

---

## FC-1-NEXT *(queued @ d3657)*

- ⚑ **Detergent / bleach trials** — **not yet formal std** · log as **`FC-1-LAUNDRY-TRIAL-*`**
- ⚑ **Towel count audit** — campus use vs rotation target
- ⚑ **Jeans / coat dye refresh** — when peg read shows fade · not urgent vs **`FURNACE-2`**
