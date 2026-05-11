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

---

## Conversation evidence — 2026-03-11 session

Source: `/Users/brock-mini-mac/Dropbox/LLM Sessions/Claude Sessions/trading - Mr Scrooge/2026-03-11_d66ae964.md`

Context: this is the MASTER_THEORY realignment day. Claude audited the bots against
the raw transcripts and concluded a layer of invented quantitative gates was
filtering out valid setups. Brock pushed for a single source-of-truth document
extracted directly from the videos, then ordered a full audit of code against it.

**The framing — invented machinery, not from the source:**

> Claude: "The bots are over-engineered relative to the source. The backbone is
> right, but a layer of invented quantitative machinery sits on top of it that
> isn't in the transcripts — and that machinery is likely filtering out valid
> setups." *(early in audit, ~msg around line 2130)*

**Brock's principle — source of truth document, no interpretation:**

> Brock: "first, we need to take the theory, direct quotes and examples and put
> them in a comprehensive master theory document (without interpretation from us,
> just unbiased and raw) in each bot file. This way as we make modifactions we
> can always go back to the unbiased original strategy." *(line ~2171)*

**The specific verdict on ATR and OTR (audit table, line ~2139):**

> | ATR gate = hard 20% minimum | Invented threshold, may block early setups | Soften or remove as hard gate |
> | OTR ratio gate | Not in transcripts at all | Demote to warning only, not hard block |

**The reasoning for demotion, in Claude's own words:**

> Claude: "Now the ATR gate. The theory says use ATR to *set expectations*, not
> as a hard block. I'll demote it from a hard rejection to a warning that still
> allows trades through." *(line ~2531)*

**Audit verdict on each gate (line ~2336, ~2339):**

> | ATR gate (20% min, 60% valid, 80% strong) | Gate 3: hard block below 20% ATR consumed | Theory: use ATR to "set expectations" — no hard gate thresholds given | **OVER-ENGINEERED** |
> | OTR gate (overhead-to-range ratio) | Gate 6: blocks if overhead > 25% of half-box | Not in the transcripts at all | **ADDED** |

**Alternative considered and rejected:** outright removal. The chosen path was
demotion to advisory — keep the calculation and log it, but never block:

> Claude (post-patch summary, line ~2834): "ATR gate (Gate 3): Demoted from hard
> block to advisory — `atr_gate = True` always; still calculates `atr_pct` and
> `atr_strength` for logging … OTR gate (Gate 6): Demoted to advisory —
> `otr_gate = True` always; logs warning when category is 'skip' but never
> blocks"

**Key technical detail informing the decision:** the audit was anchored to
direct video transcript quotes. The transcripts described ATR as a way to "set
expectations" and never mentioned an OTR ratio at all, so any hard threshold was
by definition engineered, not strategy-faithful.

> Brock (closing the audit pass, line ~2648): "yeah, let's be absolutely
> thorough"
