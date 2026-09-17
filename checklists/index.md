# Checklists

Mandatory morning checks, run before any discretionary action. Can take precedence over the day's plan.

No histories or snapshots — checks only. Last-done dates and live watch items are state and belong in [now.md](../now.md). Modify these files only to add, amend, or retire a check.

Split by **what fires the check**, not by how often it happens:

| File | Fires on | Read |
|---|---|---|
| [daily.md](daily.md) | Nothing — unconditional | Every day |
| [periodic.md](periodic.md) | An elapsed interval, 2 days to a year | Every day, against last-done in now.md |
| [triggers.md](triggers.md) | An observation — weather, or a reading | Every day, against today's sky and readings |
| [calendar.md](calendar.md) | A date band | Every day |
| [conditional.md](conditional.md) | A planned activity — trip, forge day, sow day | When that activity is proposed |

## Design rules

- A check lives where its **condition** is checked, not where its project lives.
- Prefer a state trigger to an interval wherever the state is readable. `Every ten days` drifts and gets missed; `when the weight falls` cannot fire early or late.
- A good check is a cheap measurement plus a threshold.
- Every entry names what a **miss** costs. If a miss costs nothing, it is a preference, not a check.
- Checks say **when**. Procedures say **how** — see [government/procedures](../government/procedures/). Every check carries its procedure ID so the two can be joined by search.

## Procedure ID convention

`SUBJECT-ACTION` for the generic process, `SUBJECT-ACTION_INSTANCE` for one run of it.

- `ACORN-ROAST` — the procedure
- `ACORN-ROAST_Y8-5` — the fifth Y8 roast
- `ACORN-*` finds everything acorn across calendar, map, procedures and journal
- `ACORN-ROAST_Y8*` finds every Y8 roast
