# Mr. Scrooge V1 Scoring System

type: system
status: active
tags: [scrooge, trading, scoring, v1]

trust:
  score: 90
  confidence: high
  evidence:
    - source: OANDA API audit of 511 V1 trades, 2026-04-09
      type: dataset
    - source: production deployment and log verification
      type: firsthand

## Summary
Three-layer opportunity scoring system (0-100 points) that ranks entry candidates. Recalibrated 2026-04-09 based on OANDA trade data. The scoring system decides which trade fires when multiple instruments qualify simultaneously.

## Architecture

Score is computed in `gates.py:_calculate_score()` (line 1792). Regime adjustment applied in `main.py` (line 1098) after scoring, before candidate ranking.

```
Layer 1: Validity pre-filter → hard reject (score = 0)
Layer 2: Base scoring → accumulate points
Layer 3: Contextual modifiers → adjust points
Layer 3b: OANDA truth modifiers → audit-calibrated adjustments
Regime: +10 NORMAL / -10 CAUTION (main.py, post-scoring)
```

## Layer 1: Validity Pre-Filter

Hard rejects — if any fail, score = 0 (no entry):

| Check | Condition | Rationale |
|-------|-----------|-----------|
| z_direction_mismatch | Short but z <= 0, or long but z >= 0 | Mean-reversion requires price extended away from mean |
| adr_ceiling | ADR > 1.3 and no gap context | Daily range already consumed — limited upside |
| low_extreme | abs(z) < 0.6 and touches < 10 | Insufficient mean-reversion extremity |

## Layer 2: Base Scoring

| Factor | Points | Details |
|--------|--------|---------|
| Zone tier 1/2/3/other | 30/20/12/6 | PDH/PDL = Tier 1, PHH/PHL = Tier 2 |
| ATR consumed 35-75% / 20-90% / >90% / other | 20/12/4/6 | Optimal range gets most points |
| OTR >= 2.0 / >= 1.5 / >= 1.2 | 15/10/5 | Overhead-to-range ratio |
| R:R (TP1) >= 2.0 / >= 1.5 / >= 1.0 | 15/10/5 | Uses TP1 (realistic target), not TP2 |
| john_wick + confidence | 15 + 5/3 | Was +10 pre-audit. Profitable both bots |
| power_of_towers + confidence | 5 + 5/3 | Was +10 pre-audit. Bleeds both bots |
| Standard pitchfork | 5 | |

## Layer 3: Contextual Modifiers

| Factor | Points | Details |
|--------|--------|---------|
| z-score edge >= 2.0 / >= 1.5 / >= 1.0 | 10/6/3 | Mean-reversion strength |
| BB position extreme >= 0.85 / >= 0.70 | 8/4 | Bollinger Band edge |
| Structure touches >= 10 / >= 6 | 8/4 | PDH/PDL touch count |
| Gap fade alignment | 6 | Price gapped against entry direction |

## Layer 3b: OANDA Truth Modifiers (added 2026-04-09)

Every point value is backed by OANDA trade data, not bot logs.

| Modifier | Points | OANDA Evidence |
|----------|--------|----------------|
| Ranging market (EMA slope near 0) | -20 | PF 0.33 both bots (225 V1 trades, 27 V2) |
| CT + power_of_towers | -15 | -$339 on 49 V1 trades |
| CT + john_wick | -5 | Near breakeven V1 |
| CT Tier 1 (PDH/PDL) | -10 | 45.7% WR, -$537 on 70 V1 trades |
| CT Tier 2 (PHH/PHL) | +5 | 66.7% WR, +$140 on 15 V1 trades |
| z-score alignment | +5 | r=+0.38 with P/L in V2 |

"CT" = counter-trend (shorting in an uptrend or buying in a downtrend). Trend determined by 50H EMA slope over 10 bars. Ranging = slope between +/-0.0005.

## Regime Scoring

Applied in `main.py` line 1098, after `_calculate_score()` returns, before candidate ranking.

| Regime State | Score Adjustment | OANDA Evidence |
|-------------|-----------------|----------------|
| NORMAL (score >= +2) | +10 | 77.8% WR, +$5,037 |
| CAUTION (score 0..+1) | -10 | 57.9% WR, -$5,719 |

Floor: if score drops below 1 after regime adjustment, it's clamped to 1. Score 0 means validity-rejected (Layer 1) and would be filtered from candidates.

## R:R Design Decision

- **Hard gate:** Uses TP2 (opposite box wall). Minimum R:R 1.60. Prevents entering with no room.
- **Scoring bonus:** Uses TP1 (box center). Buckets: >= 2.0 +15, >= 1.5 +10, >= 1.0 +5.
- **Why not TP1 for hard gate:** V2 OANDA data showed R:R < 1.5 (TP1) = 78.6% WR, +$1,441. A TP1 hard gate at 1.60 would reject the winners.

`rr_tp1` is stored on SignalResult and used only for scoring. `risk_reward_ratio` (TP2-based) is used for the hard gate.

## Candidate Ranking

After all instruments are scored in one 5-minute cycle:
1. Filter: `score > 0` (validity-rejected signals excluded)
2. Sort: descending by score
3. Fire: best-scored candidate enters (if `position_count < max_concurrent_positions`)

## Audit Data

Raw data used for calibration stored at:
- `data/audit/scrooge_v1_audit.csv` — 344 trades with OANDA P/L + bot decision factors
- `data/audit/oanda_v1_fills.json` — 1,077 ORDER_FILL transactions from OANDA API

## Key Takeaways

- Scoring has predictive power only with Layer 3b modifiers — without them, r ≈ 0 with P/L
- Ranging markets (no trend) are the #1 profit killer, not counter-trend
- john_wick signals consistently outperform power_of_towers across both bots
- Future scoring changes must be validated against OANDA trade data, not bot logs

## Related
- [[Mr. Scrooge V1]]
- [[Mr. Scrooge Architecture]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge V1 Changelog]]
