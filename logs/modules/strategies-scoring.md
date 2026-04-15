# strategies/scoring — Dev Log

> Cross-cutting scoring system: aggregates gate results, signal types, regime, and market context into a single trade score.

---

## Historical Lessons (V1/V2)

### [2026-04-09] [BOTH] — CRITICAL: Scoring had ZERO predictive power (inverse correlation)
**Source:** AUDIT_FINDINGS_20260409.md, scoring-inversion postmortem
**Type:** bug
**Detail:** Higher signal scores correlated with WORSE outcomes. Score 60-70: 80% WR, +$2,724. Score 70-80: 60% WR, -$6,138. Score 80-90: 25% WR. Root causes: 1) blind to trend alignment, 2) R:R computed against TP2 (6.6% hit rate), 3) signal types weighted equally, 4) regime not integrated. Full recalibration applied.

### [2026-04-09] [BOTH] — Ranging markets are #1 profit killer, not counter-trend
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** discovery
**Detail:** Ranging: 225 V1 trades, PF 0.33 (catastrophic). Counter-trend: 240 trades, PF 1.03 (nearly breakeven). V3 must detect ranging via 50H EMA slope and penalize -20 pts.

### [2026-04-09] [BOTH] — Counter-trend Tier 1 worst, Tier 2 best
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** discovery
**Detail:** CT Tier 1 (PDH/PDL): 45.7% WR, -$537 (70 trades). CT Tier 2 (PHH/PHL): 66.7% WR, +$140. Scoring: CT Tier 1 -10 pts, CT Tier 2 +5 pts.

### [2026-04-09] [BOTH] — R:R against TP1 is strongest predictor (r=0.68)
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** discovery
**Detail:** Pearson r = 0.68 with P&L (V1). TP2 hit rate only 6.6%. Score using TP1 for bonus buckets. Hard gate keeps TP2 (1.60 min) to prevent chasing.

### [2026-04-09] [BOTH] — Z-score alignment bonus: +5 pts (r=0.38)
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** discovery
**Detail:** z-score alignment shows r=+0.38 correlation with P&L. Add +5 pts when price aligned to z-score direction.

### [2026-04-09] [BOTH] — Sub-30-minute trades are catastrophic
**Source:** AUDIT_FINDINGS_20260409.md
**Type:** warning
**Detail:** V1: 28.3% WR, -$662. V2: 26.3% WR, -$15,871. 2-8 hour trades: 60-64% WR, profitable. Do NOT chase quick exits. Minimum time_exit_cooldown 15 min.

### [2026-04-09] [BOTH] — Future scoring changes require OANDA trade data validation
**Source:** scoring-inversion postmortem
**Type:** rule
**Detail:** NEVER trust bot log P/L — it was wrong for 17/21 pairs due to quote-currency conversion bug. Always pull closed trades from broker API and compute P&L independently. Any new scoring factor must show statistical significance against realized P&L.

### [2026-04-10] [BOTH] — Score=1 entries with full sizing are catastrophic
**Source:** known-defects.md, Defect 15
**Type:** bug
**Detail:** Regime penalty pushed scores to floor (1) but bot still entered with full sizing. Score=1 USD/MXN lost -$40.41 V1 and -$940.54 V2. Fixed with minimum score >= 20 gate.

### [2026-04-13] [V2] — Counter-trend override has no memory
**Source:** known-defects.md, Defect 1
**Type:** bug
**Detail:** Tier 1/2 zones unconditionally pass against trend with zero memory of how many times same zone already failed. Trade 4 on 2026-04-07 was 3rd short at PDH in one day. Decay zone strength after repeated touches.

### [2026-04-13] [V2] — No daily same-zone entry cap in signal flow
**Source:** known-defects.md, Defect 3
**Type:** bug
**Detail:** Zone debounce is 20 min, TP cooldown 15 min. Normal fresh signal entries did NOT increment any cap. Bot could short same zone unlimited times per day. Add daily cap on fresh entries per pair+direction+zone.

### [2026-04-09] [BOTH] — R:R < 1.5 (TP1) has 78.6% WR — counter-intuitive
**Source:** v2-scoring-system.md
**Type:** discovery
**Detail:** V2 OANDA data: R:R < 1.5 (against TP1) had 78.6% WR. These are tight, high-probability setups. R:R 1.5-2.0 (TP1) had 0% WR. A TP1 hard gate at 1.60 would reject the best performers. Hard gate uses TP2 (not TP1), scoring uses TP1 (not TP2). Do not conflate.

### [2026-04-09] [BOTH] — Score floor of 1 exists deliberately (not a bug)
**Source:** v2-scoring-system.md
**Type:** rule
**Detail:** After regime penalty, if gate-passed signal drops below 1, clamped to 1 (not 0). Score 0 means validity-rejected (Layer 1) and would be silently filtered. Removing the floor causes regime penalties to kill valid signals without log trace.

### [2026-04-09] [BOTH] — Scoring validation requires quarterly re-audit
**Source:** scoring-validation-plan.md
**Type:** rule
**Detail:** Layer 4 weights (-20 ranging, -15 CT+PoT, etc.) calibrated from Feb-Apr 2026. Market conditions change. Re-audit quarterly against fresh broker trade data. The -10 CAUTION penalty may double-count. Check after 50-100 trades.
