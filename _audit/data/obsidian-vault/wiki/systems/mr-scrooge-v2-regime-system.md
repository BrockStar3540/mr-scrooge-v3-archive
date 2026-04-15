---
type: system
status: active
tags: [scrooge, trading, regime, v2]
trust:
  score: 90
  confidence: high
  reason: Production-deployed since 2026-03-31, OANDA data validates regime-state outcomes
---

## Summary

The V2 regime system is an adaptive market-state classifier that gates trade entries based on recent price behavior. It aggregates seven independent signals into a composite score, maps that score to a regime state (NORMAL, CAUTION, RESTRICTED, BLOCKED), and enforces trading restrictions accordingly. Active as an entry blocker since 2026-03-31; was a passive observer from 2026-03-22 to 2026-03-30. Integrated into the scoring system on 2026-04-09.

## Regime Signals

Four signals contribute to the composite regime score. Each evaluates a different dimension of market stress.

### box_acceptance (-1 to -2)

Measures consecutive closes outside the previous day's high (PDH) or previous day's low (PDL). When price accepts outside the prior range, the box framework's reversal thesis weakens.

- -1: initial acceptance (2+ closes outside)
- -2: extended acceptance (sustained breakout)

### rejection_decay (-1 to -2, or +2)

Evaluates the quality of wall touches (rejections). Strong rejections with wicks confirm the box; weak closes through the wall degrade confidence.

- +2: strong rejections (confirming box integrity)
- -1: weakening rejections
- -2: failed rejections (price closing through walls)

### expansion_pressure (-1 to -2)

Detects ATR expanding directionally, indicating trending conditions where reversal setups are likely to fail.

- -1: moderate expansion
- -2: strong directional expansion

### qualified_failures (-1 to -3)

Tracks the bot's own recent setups that hit their stop-loss. Repeated SL hits on qualified signals indicate the current regime is hostile to the strategy.

- -1: one recent failure
- -2: two recent failures
- -3: three or more recent failures

### breadth_negative / breadth_positive (-1 or +1)

Added 2026-04-12. Evaluates correlated pairs' regime state. If multiple correlated pairs also show negative regime scores, this confirms broad market weakness rather than pair-specific noise.

- -1 (breadth_negative): avg regime score of top 4 correlated peers <= -2.0
- +1 (breadth_positive): avg regime score of top 4 correlated peers >= +2.0
- Peer cap: _MAX_BREADTH_PEERS=4 (prevents trigger frequency explosion with large correlation map)
- Correlation map: 17 entries covering EUR/GBP/USD majors, AUD/NZD crosses, and JPY crosses (merged from V1+V2 on 2026-04-12)

### compression (+1)

Identifies ATR compression — when recent 5M volatility is below 80% of the baseline. Compression often precedes reversals, making the box framework's thesis stronger.

- +1: recent ATR < 0.8x baseline (favorable for mean-reversion entries)

### bb_context (+1 or -1)

Bollinger Band snap-back detection. When price re-enters Band A from an extreme, signals a potential reversal.

- +1 (bb_rejection_long/short): close re-entered Bollinger Band lower/upper boundary

## Score Thresholds and Regime States

| Regime | Composite Score | Trading Rules |
|---|---|---|
| **NORMAL** | >= +2 | Full trading, no restrictions |
| **CAUTION** | 0 to +1 | Requires signal score >= +1 to enter |
| **RESTRICTED** | -1 to -2 | Position size halved |
| **BLOCKED** | <= -3 | All entries suppressed |

### Hysteresis After BLOCKED

When the regime transitions out of BLOCKED, it does not immediately return to NORMAL. The composite score must reach >= +2 before NORMAL is restored. This prevents rapid cycling between BLOCKED and unrestricted trading.

## Enforcement in coordinator.py

Regime enforcement happens in `coordinator.py` at lines ~490-517.

- **Score gate:** Signal score must be >= +1 when regime is CAUTION
- **BLOCKED suppression:** When regime is BLOCKED, no entries are attempted regardless of signal quality
- **Size reduction:** When regime is RESTRICTED, position size is halved from the standard calculation

## Scoring Integration (Added 2026-04-09)

Regime state feeds back into the signal scoring system:

| Regime | Points Added to Signal Score |
|---|---|
| NORMAL | +10 |
| CAUTION | -10 |
| RESTRICTED | -10 |

This creates a dual effect: CAUTION/RESTRICTED both gate entries (via enforcement) and depress signal scores (via scoring), making it harder for marginal signals to pass in adverse conditions.

## OANDA Evidence

Data from OANDA closed trades, classified by regime state at entry time.

| Regime | Win Rate | P/L |
|---|---|---|
| NORMAL | 77.8% | +$5,037 |
| CAUTION | 57.9% | -$5,719 |
| RESTRICTED | 50.0% | -$2,138 |

The data validates the regime system's classification: NORMAL entries are strongly profitable, while CAUTION and RESTRICTED entries lose money in aggregate.

## Data Storage

- **`regime-protests.jsonl`**: Logs all regime observations and entry blocks. Each line is a JSON object with timestamp, regime state, composite score, individual signal values, and action taken (allowed/blocked).

## History

| Date | Event |
|---|---|
| 2026-03-22 | Created as passive observer (logged regime state but did not block entries) |
| 2026-03-31 | Activated as entry blocker |
| 2026-04-09 | Integrated into scoring system (+10/-10 regime adjustments) |

## Key Takeaways

- The regime system is an empirically validated entry filter --- NORMAL trades are profitable, CAUTION/RESTRICTED trades lose money
- Four independent signals (box acceptance, rejection decay, expansion pressure, qualified failures) capture different dimensions of market hostility
- BLOCKED state has hysteresis: requires >= +2 to return to NORMAL, preventing rapid cycling
- Regime affects entries in two ways: hard gates (enforcement) and soft pressure (scoring integration)
- All observations are logged to regime-protests.jsonl for future audit and calibration

## Related

- [[Mr. Scrooge V2]]
- [[Mr. Scrooge V2 Scoring System]]
- [[Mr. Scrooge Architecture]]
