# Mr. Scrooge Alternative Box Analysis

type: system
status: draft
tags: [trading, scrooge, box-theory, analysis, open-question]

trust:
  score: 50
  confidence: low
  evidence:
    - source: manual analysis 2026-04-12, insufficient trade data post-fix
      type: needs-validation

## Summary

The alternative box (session_cheat_code) fires when price breaches the prior-day box and rebuilds a new box from the current session's high/low range. This document tracks the open question of whether alternative-box trades have edge, and whether the mechanism aligns with the Master Theory.

## The Concern

The Master Theory (MASTER_THEORY.md) defines the box as prior-day high and prior-day low. When price breaks out of the box, the theory does not describe building a new box from session data. It describes:
1. Waiting for a pullback to the breakout level (old resistance becomes new support)
2. Waiting for a new day to form a new box

The alternative box is an engineering addition (acknowledged in MASTER_THEORY.md Section 24 as not derived from source transcripts). It manufactures structure where the original theory says none exists.

## Current State (as of 2026-04-12)

- Alternative box fires on 20 of 26 tracked pairs regularly — it is the dominant operating mode, not an edge case.
- Pre-fix trade data is unreliable (bugs in scoring, SL management, and slippage distort P&L).
- Post-fix data collection begins at the beta epoch (2026-04-13 02:41 UTC).
- Need 100+ trades on the fixed codebase before the alternative box can be evaluated.

## What to Track During Beta

1. **Flag alt-box trades**: Every entry where using_alternative=True should be tagged in entry-context.jsonl.
2. **Compare P&L**: Alt-box trades vs normal-box trades separately.
3. **Win rate**: Does alt-box win rate meet the 75% threshold needed for the harvester's R:R profile?
4. **Regime correlation**: Are alt-box trades more likely to be regime-blocked? If so, the regime may be correctly protecting against a weak setup.

## Possible Outcomes

| Verdict | Action |
|---------|--------|
| Alt-box trades profitable at 75%+ win rate | Keep. Treat as valid extension of the theory. |
| Alt-box trades marginal (60-75% win rate) | Tighten: require higher score threshold for alt-box entries (e.g. score >= 40 instead of 20). |
| Alt-box trades unprofitable (<60% win rate) | Remove. Revert to prior-day box only. When box is broken, sit out until next day. |

## Related

- [[Mr. Scrooge Architecture]]
- [[Mr. Scrooge V1 Changelog]]
- [[Mr. Scrooge V2 Changelog]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge Scoring Validation Plan]]
