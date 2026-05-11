# 1005. MASTER_THEORY realignment — fidelity to source transcripts

**Status:** Accepted
**Date:** 2026-03-11
**Version scope:** V1
**Backfilled:** 2026-05-11

## Context

By early March 2026, the bot was live and producing trades. A full audit against the source transcripts (Doug & Sylvia's Liquidity Sweep Reversal Framework) discovered that the **implementation had invented quantitative rules not in the transcripts**.

Daily notes from 2026-03-11 captured the assessment bluntly:
- ~55-65% rule fidelity to source theory
- ~30-40% numerical fidelity

The implementation had drifted from the doctrine — partly because the original doctrine doc itself contained interpretation that hadn't been verified back to transcripts.

## Decision

1. **Create `MASTER_THEORY.md`** — raw, unbiased quotes and rules from source transcripts only. No interpretation. Single source of truth for strategy decisions going forward.
2. **Delete `BOX_THEORY.md`** — was over-engineered interpretation.
3. **Realign code to MASTER_THEORY**, accepting that some V1 rules were inventions:
   - Sucker move: strict consecutive counting → flexible window (transcripts allow "messy" patterns: red-green-green-red-green)
   - Stop placement: mixed box-wall/candle-extreme → always signal candle extreme
   - Trigger prices: zone-anchored → always candle high/low (`h × 1.0001` / `l × 0.9999`)
   - **ATR gate (Gate 3): demoted to advisory** — transcripts have no ATR consumption requirement
   - **OTR gate (Gate 6): demoted to advisory** — transcripts have no overhead-to-range gate
   - Trend filter (Gate 2): tier-aware — Tier 1/2 zones override trend block
   - Time exit: 30-min hard → 4-hour backstop, only if price moved against trade
   - `max_hold_minutes`: 30 → 240
   - `max_reentries_per_setup`: 1 → 3
   - New 3-component hybrid trailing stop: `max(candle_trail, profit_lock_70%, peak − 1.5×ATR)`
   - `time_exit_cooldown_minutes`: 360 → 15

## Alternatives considered

- **Keep invented rules; transcripts are guidance not gospel** — rejected. The invented rules weren't validated to outperform the transcripts; they were just there. Burden of proof for departure was unmet.
- **Tighten code instead of loosen** — rejected. The audit found we were *over*-constraining the bot relative to source.
- **Soft realignment over multiple commits** — partially adopted, but Mar 11 was the bulk of it.

## Consequences

**Enabled:**
- Two of six gates became advisory — bot fires more often, more aligned with theory.
- Recovery of re-entry as a primary tool (1 → 3 per setup) — liquidity sweeps often re-trigger.
- Stop placement consistency (always signal candle extreme) eliminated an entire class of incoherent exits.

**Closed:**
- "Tightening invented rules for safety" as a design path. Future tightening must trace to MASTER_THEORY or to evidence.

**Costs:**
- ATR and OTR demotion meant some genuinely cost-inefficient trades could fire. Mitigated by `min_net_profit_pips = 7` floor.

## Lesson

**Documentation drift is a real bug class.** The implementation reflected what someone thought the theory said, not what the theory actually said. Codifying the source verbatim and writing code against it is the only defense.

## Cross-references

- `archive/DAILY_NOTES_2026-03-11.md` (Dropbox) — full change list
- `MASTER_THEORY.md` in `BrockStar3540/mr-scrooge` repo — the single source of truth
- ADR `1003-six-gate-signal-confirmation.md` — what gates 3 and 4 became
- `[[scrooge-bug-catalog]]` B-025 through B-032
