# RETCON — Y5 spring sow + D341 harvest (Day 1687 audit)

**Filed:** Day 1687 · **Cal-Y5 D355**  
**Cause:** Agent continuity error — `SPRING-SOW-Y5` was planned and implied (d1400 bed read, d1655–d1684 harvest prep, `YELLOW-GO-READ-1680`) but never hero-logged; Days 1685–1686 incorrectly filed **HARVEST-BLOCK-HOLD** and empty beds.

**Player intent:** Frost-gate spring sow always happens; D341 harvest prep is for grain/pulse, not dye-only.

---

## Canonical fixes applied

| Item | Correction |
|------|------------|
| **SPRING-SOW-Y5** | **✓ hero @ Day 1400** (Cal-Y5 D68 · frost gate day 2 · post-WOAD d1399) |
| **Bed map @ sow** | **Bed B S emmer · B N lentil · B center flax · Bed A S chickpea · Bed A N mulch · madder W + WOAD Bed D untouched** |
| **Days 1685–1686** | **EMMER-Y5 + P-18-Y5 + P-17-Y5 harvest** (mirrors Y4 d1309–1310 grammar) |
| **Day 1686 madder** | **Moved → Day 1687** (dye harvest after grain block) |
| **Agent rule** | **`.cursor/rules/farm-calendar-non-negotiable.mdc`** — block play past sow/harvest windows without hero log |

---

## SPRING-SOW-Y5 @ Day 1400 (seed draws)

| Bed | Crop | Seed draw |
|-----|------|-----------|
| **Bed B south** | Emmer elite | **EMMER-ELITE-Y4 ~82 g · ~23 g reserve** |
| **Bed B north** | Lentil P-17 | **P-17-ELITE-Y3 ~38 g · ~14 g reserve** |
| **Bed B center** | Flax P-07 | **P-07 elite ~14 g** |
| **Bed A south** | Chickpea P-18 | **P-18-ELITE-Y4 ~44 g · ~10 g reserve** |
| **Bed A north** | Mulch only | — |
| **Bed D margin** | WOAD (prior) | **sown d1399 — hands off** |

**Doctrine:** Scare-only from d1401+ on rows until FARM-READ GREEN; expedition absences do **not** cancel standing crop.

---

## Y5 harvest @ Days 1685–1686 (yields)

| Crop | Day | Bulk | Elite save |
|------|-----|------|------------|
| **Emmer Bed B S+N** | **1685** | **~2.02 kg @ horreum A EMMER-BULK-Y5** | **~102 g EMMER-ELITE-Y5 @ SEED-VAULT** |
| **Chickpea Bed A** | **1686** | **~252 g @ pulse bay P-18-Y5** | **~51 g P-18-ELITE-Y5** |
| **Lentil Bed B north** | **1686** | **~238 g @ pulse bay P-17-Y5** | **~49 g P-17-ELITE-Y5** |
| **Flax Bed B center** | **standing** | **pull ~Cal-Y5 D360+ class (~d1692+)** | **seed @ harvest pull** |

---

*This file is the audit trail. Journal days 1400 · 1685 · 1686 · 1687 are the live canon.*
