---
type: system
status: active
tags: [scrooge, trading, changelog, v2]
trust:
  score: 90
  confidence: high
  reason: Entries verified against git commits and OANDA audit data
---

## Summary

Dated record of significant changes to Mr. Scrooge V2. Each entry includes author, files changed, what was done, and why. For the changelog process (where to document, who is responsible, separation of concerns), see [[Mr. Scrooge Changelog Process]].

## Changelog

### 2026-04-12 — V1/V2 Convergence Fixes

**Author:** Claude Code
**Commit:** a5b000e
**Files:** coordinator.py, signals/engine.py, signals/extreme_reversal.py, zones/detector.py, regime/supervisor.py

**What:**
- Fixed session indicator frozen at boot value (added _update_sessions call to run loop)
- Merged correlation map — full 26-pair universe with MAX_BREADTH_PEERS=4 cap
- Enforced validity_detail schema on ALL signals (market_summary was always 0/0)
- Filtered box states to active instruments only (was showing all 26 pairs)
- Fixed V1 logger names leaking into V2 logs (zones/detector.py stub deleted, extreme_reversal.py renamed)
- Added OANDA 502 fallback — stale bar cache prevents pair skipping on API errors
- Aligned RR rejection message format with V1

**Why:** Dashboard comparison revealed 6 code-level divergences between V1 and V2. Root causes: dead code, missing method calls, incomplete schema population, stale correlation maps. Not market drift.

**Verification:** Per-pair regime scores match V1 within 1 point. Market summary shows valid/rejected counts and MEAN_REV setup distribution. Sessions update correctly at hour boundaries.

### 2026-04-09 --- OANDA Audit + Scoring Recalibration

**Author:** Claude (V2 auditor) + Claude (V1 auditor)

**Files:** `signals/engine.py`, `signals/models.py`, `gates/trend_gate/gate.py`, `coordinator.py`, `positions/manager.py`, `positions/models.py`, `core/oanda_client.py`, `config.py`, `main.py`

**What:** Scoring system recalibrated from OANDA trade data. Added Layer 4 (ranging -20, CT combos, tier adjustments, z-align +5). Signal reweighting (JW +15, PoT +5). Regime integration (+10/-10). R:R scoring against TP1. Score floor. Bug fixes: P/L currency conversion, overhead cost, OANDA 404 fallback, TP2 3x ATR clamp, log rotation.

**Why:** Two independent OANDA audits (511 V1 + 58 V2 trades) found scoring inversely correlated with outcomes. Ranging markets had a profit factor of 0.33. Bot logs were reporting wrong P/L for 17/21 currency pairs due to a quote-currency conversion bug.

**Verification:** V2 restarted, boot clean, no errors, scoring active (GBP_USD scored 44, worst combos floored to 1). V1 also restarted and verified.

## Key Takeaways

- This changelog records what changed and why, not how the system currently works (that belongs in the system docs)
- Each entry should reference the author, files touched, what was done, why, and how it was verified
- The 2026-04-09 entry represents the largest single change to V2's scoring logic since inception
- New entries should be prepended below the Changelog heading, with the most recent at top
- For the process governing what goes where, see [[Mr. Scrooge Changelog Process]]

## Related

- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V2 Scoring System]]
- [[Mr. Scrooge Changelog Process]]
