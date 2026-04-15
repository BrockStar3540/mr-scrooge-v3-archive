# Audit Findings — 2026-04-09

## Methodology

Two independent OANDA API audits cross-referenced actual trade outcomes with bot logs.
- V1: 511 closed trades (Feb 23 - Apr 9), live account
- V2: 58 closed trades (Mar 22 - Apr 9), practice account
- Candle data from OANDA (H1) used for trend classification (50-period EMA slope)
- Entry-context.jsonl cross-referenced for scoring data (V2: 37 matched trades)

Source of truth: OANDA API (not bot logs). Bot P/L calculation was found to be wrong for non-USD-quote pairs.

## Key Findings

### 1. Scoring has zero predictive power
Higher signal scores correlate with WORSE outcomes.
- Score 60-70: 80% WR, +$2,724 (V2)
- Score 70-80: 60% WR, -$6,138 (V2)
- Score 80-90: 25% WR, +$93 (V2)

### 2. Ranging markets are the #1 profit killer
| Trend | V1 Trades | V1 PF | V2 Trades | V2 PF |
|-------|-----------|-------|-----------|-------|
| With-trend | 46 | 1.91 | 2 | — |
| Counter-trend | 240 | 1.03 | 29 | 0.97 |
| Ranging | 225 | 0.35 | 27 | 0.33 |

Counter-trend is NOT the problem (nearly breakeven). Ranging is catastrophic.

### 3. CT + power_of_towers at Tier 1 is the worst combo
- V1: CT+PoT = -$339 on 49 trades. CT Tier 1 = -$537.
- CT Tier 2 = profitable both bots (66-100% WR)

### 4. john_wick outperforms power_of_towers
- V2: john_wick +$1,267 (14 trades, 64% WR)
- V2: power_of_towers -$4,086 (22 trades, 59% WR — wins small, losses huge)

### 5. NORMAL regime is the edge
- NORMAL: 77.8% WR, +$5,037
- CAUTION: 57.9% WR, -$5,719

### 6. Sub-30-minute trades are catastrophic
- V1: 28.3% WR, -$662
- V2: 26.3% WR, -$15,871
- 2-8 hour trades: 60-64% WR, profitable

### 7. R:R against TP1 is the strongest predictor
- Pearson r = 0.68 with P/L (V1)
- TP2 hit rate: 6.6% — R:R against TP2 is fantasy

## Scoring Calibration Applied

| Factor | Points | Evidence |
|--------|--------|----------|
| Ranging penalty | -20 | PF 0.33 both bots |
| CT + power_of_towers | -15 | -$339 V1 (49 trades) |
| CT + john_wick | -5 | Near breakeven V1 |
| CT Tier 1 | -10 | Worst CT category both bots |
| CT Tier 2 | +5 | 66-100% WR both bots |
| john_wick signal | +15 | Profitable both bots |
| power_of_towers signal | +5 | Bleeds both bots |
| NORMAL regime | +10 | 77.8% WR, +$5,037 |
| CAUTION regime | -10 | Bleeds -$5,719 |
| z-score alignment | +5 | r=+0.38 V2 |
| R:R uses TP1 for scoring | (formula) | r=0.68 strongest predictor |

## Bugs Fixed

1. P/L calculation in quote currency (not USD) for non-USD-quote pairs — 17 of 21 instruments affected
2. Overhead cost in quote currency — same root cause
3. OANDA 404 fallback — closed trades now recovered via transactions API
4. TP2 clamped to 3x ATR — prevents absurd targets from stale box data
5. Duplicate log handler — propagate=False on child loggers
6. Log rotation — RotatingFileHandler (10MB, 5 backups)

## Data Files

- /tmp/scrooge_v1_trades.json — 511 V1 trades from OANDA
- /tmp/scrooge_v2_trades.json — 58 V2 trades from OANDA
- /tmp/v1_enriched_trades.json — V1 trades with trend classification
- /tmp/v2_enriched_trades.json — V2 trades with trend + entry-context
- Permanent copies in data/audit/ for both bots
