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

### [2026-04-15] [V1+V2] — V3 Hybrid Scorer replaces old 3-layer scoring system
**Source:** Raw OANDA candle analysis, docs/SCORING_V3_LIVE.md
**Type:** correction
**Detail:** Old scoring had +0.5 pt separation between W and L (useless). V3 Hybrid Scorer achieves +80.3 pt separation. Out-of-sample validated at 100% WR on 20-trade test set. Key changes: OTR scoring REMOVED (17% WR at low OTR), RR reduced from 0-15 to 0-3 pts, ATR consumed reduced from 0-20 to 0-4 pts. New factors added: box age (±13), entry hour (±13), volume ratio (±9), SMA20 distance (±8), EMA50 proximity (-10), EMA20 proximity (-7). Pair layer adds ±9 to ±14 for combined factor clusters.

## V3.1.1 Recalibration (2026-04-16)

### Score Scale Change
V3.1.1 operates on a **lower score scale** than original V3.0. Do not compare
live scores to the V3.0 documentation (SCORING_V3_LIVE.md is now marked legacy).

### What Changed

**RSI neutral: hard block → soft penalty (-5 pts)**
- Backtest: 6/29 winners (21%) were hard-blocked by RSI 45-55
- Including a $17.48 USD_CHF winner
- Now scored like any other factor — the scorer decides, not a blind gate

**Session floors lowered by 6 (all sessions, both families)**
- Default: 30/32/30/34/40 (was 36/38/36/40/46)
- Trend:   28/30/28/32/38 (was 34/36/34/38/44)
- Loser max base score on calibration data: +3
- New floors still 27+ pts above highest loser

**EMA20 < 15% penalty: -6 → -3**
- Was biggest single drag on blocked winners (-42 total across 7/18 rejected)
- Factor diagnosis: hurts winners without clearly separating from losers

**Box age 18-24h penalty: -7 → -4**
- Combined with e20, these two factors suppressed more winners than any other class

### Family-Aware Scoring (V3.1)
Scorer now receives the candidate and branches on strategy_family:

**Trend overlays** (applied when strategy_family = "trend"):
- Structure break confirmed: +6
- DBB_PULLBACK with depth ≤55%: +4
- DBB_BREAKOUT: +4
- Directional candles ≥4: +2
- Hour 16-19 UTC softening: +2
- Box age 18-24h softening: +3
- Exhausted chase (z≥1.5 + ema20<15): -5

**Reversal path: unchanged.** No family overlays applied.

**Separate trend session thresholds** (lower than default):
Trend family uses floors 2 pts lower than default at each session.

### Backtest Results (50-trade calibration dataset)
| Config | Winners Passed | Losers Passed | P&L |
|--------|---------------|---------------|-----|
| V3.0 original | 4 | 0 | $80.81 |
| V3.1 (decompressed) | 5 | 0 | $85.28 |
| V3.1.1 (recalibrated) | 9 | 0 | $144.14 |

### Calibration Warning
Thresholds calibrated on 50-trade executed-trade dataset (survivor-biased).
Full calibration requires candidate-level replay dataset. Current thresholds
are a live hypothesis under forward validation.

### Scorer Audit Payload
Every log line now includes raw box-derived inputs after "||":
```
base=21 final=29 ... | hr=-7 age=+9 ... || px=1.21585 ema20=1.21566 ema50=1.21365 box=0.00122 age=1.7h
```
Enables full score verification: e20d = |px - ema20| / box * 100.
