---
type: system
status: active
tags: [scrooge, trading, scoring, v2]
trust:
  score: 90
  confidence: high
  reason: Production-deployed, calibrated against OANDA closed-trade data (511 V1 + 58 V2 trades)
---

## Summary

Mr. Scrooge V2 uses a four-layer scoring system to rank trade signals before entry. Layers 1-3 are structural (validity, base points, context). Layer 4 was added 2026-04-09 after an OANDA audit revealed the original scoring inversely correlated with outcomes. The system lives in `signals/engine.py` (`_score()`) with regime injection in `coordinator.py`.

## Layer 1 --- Validity Pre-Filter

Rejects signals outright before scoring begins.

| Check | Condition | Result |
|---|---|---|
| Z-score direction mismatch | Short signal but z <= 0, or long signal but z >= 0 | **Reject** |
| ADR ceiling | ADR ratio > 1.3 without gap confirmation | **Reject** |
| Low extreme | \|z\| < 0.6 without structural override | **Reject** |

Signals that fail Layer 1 never reach scoring. They are logged to `decisions.log` with reason codes.

## Layer 2 --- Base Scoring

Core point accumulation from signal characteristics.

| Factor | Condition | Points |
|---|---|---|
| **Tier** | Tier 1 | +30 |
| | Tier 2 | +20 |
| | Tier 3 | +12 |
| | Tier 4+ | +6 |
| **ATR Consumed** | 35-75% | +20 |
| | 20-35% or 75-90% | +12 |
| | >90% | +4 |
| | <20% | +6 |
| **OTR Ratio** | >= 2.0 | +15 |
| | >= 1.5 | +10 |
| | >= 1.2 | +5 |
| **R:R (TP1-based)** | >= 2.0 | +15 |
| | >= 1.5 | +10 |
| | >= 1.0 | +5 |
| **Signal Type** | john_wick | +15 |
| | power_of_towers | +5 |
| | other | +5 |
| **Confidence** | HIGH | +5 |
| | MODERATE | +3 |

### R:R Design Decision

The hard gate uses TP2 (opposite box wall) with `min_rr` of 1.60. Scoring uses TP1. This split exists because V2 OANDA data showed:

- R:R < 1.5 (TP1): 78.6% win rate --- these are tight, high-probability setups
- R:R 1.5-2.0 (TP1): 0% win rate --- wider TP1 targets underperformed

A TP1 hard gate at 1.60 would have rejected the best-performing signals. TP2 sets the minimum reward ceiling; TP1 scoring rewards realistic take-profit quality.

## Layer 3 --- Contextual Adjustments

Bonus points from market structure context.

| Factor | Condition | Points |
|---|---|---|
| **Z-score magnitude** | \|z\| >= 2.0 | +10 |
| | \|z\| >= 1.5 | +6 |
| | \|z\| >= 1.0 | +3 |
| **Bollinger Band extreme** | >= 0.85 | +8 |
| | >= 0.70 | +4 |
| **Wall touches** | >= 10 | +8 |
| | >= 6 | +4 |
| **Gap alignment** | Gap aligned with signal direction | +6 |

## Layer 4 --- OANDA Truth (Calibrated 2026-04-09)

Adjustments derived from actual OANDA trade outcomes. These override structural assumptions with empirical reality.

| Factor | Condition | Points |
|---|---|---|
| **Ranging market** | Market classified as ranging | -20 |
| **Counter-trend + PoT** | Counter-trend with power_of_towers signal | -15 |
| **Counter-trend + JW** | Counter-trend with john_wick signal | -5 |
| **Counter-trend Tier 1** | Counter-trend, tier 1 | -10 |
| **Counter-trend Tier 2** | Counter-trend, tier 2 | +5 |
| **Z-alignment** | Long with z < -0.5, or short with z > 0.5 | +5 |

## Regime Scoring Integration

Injected in `coordinator.py` after `_score()` returns, before ranking.

| Regime | Points |
|---|---|
| NORMAL | +10 |
| CAUTION | -10 |
| RESTRICTED | -10 |

## Score Floor

Minimum score is 1 for any signal that has passed all gates (`all_gates_passed = True`). This prevents regime penalties from zeroing out otherwise valid signals. A score of 0 would silently suppress the signal; a score of 1 keeps it in the ranking (even if it loses to competitors).

## Code Locations

- **`signals/engine.py`** --- `_score()` method: Layers 1-4
- **`coordinator.py`** --- Regime injection after scoring, lines ~490-517

## OANDA Evidence Table

Data from two independent audits pulling closed trades via OANDA API.

| Factor | Sample | Result |
|---|---|---|
| Ranging market | 225 V1 + 27 V2 trades | PF 0.33 (both bots) |
| CT + PoT | 49 V1 trades | -$339 |
| CT Tier 1 | 70 V1 trades | -$537 |
| CT Tier 2 | V1 + V2 | V1: +$140, V2: +$5,820 |
| john_wick | V2 trades | +$1,267 |
| NORMAL regime | V2 trades | 77.8% WR, +$5,037 |

## Key Takeaways

- Layer 4 (OANDA truth) is the most impactful layer --- ranging at -20 is the single largest penalty and was the single largest source of losses
- R:R scoring uses TP1, not TP2. The hard gate uses TP2. Do not conflate them or change one thinking it is the other.
- john_wick signals earn 3x the points of power_of_towers (+15 vs +5) because PoT bled -$4,086 in V1 data while JW was consistently profitable
- Score floor of 1 exists deliberately --- removing it would cause regime penalties to silently kill valid signals
- Any future scoring changes require OANDA trade data validation, not bot log analysis (bot logs had wrong P/L for 17/21 pairs)

## Related

- [[Mr. Scrooge Architecture]]
- [[Mr. Scrooge V2]]
- [[Mr. Scrooge Known Defects]]
- [[Mr. Scrooge V2 Regime System]]
