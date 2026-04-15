# Mr. Scrooge V2 — Box Theory FX Engine (Practice Account)

## Overview

Mr. Scrooge V2 is a forex trading bot using box theory reversal strategy on OANDA.
It runs on a practice account for strategy validation before applying changes to V1 (live).

## Architecture

V2 is modular — each concern lives in its own package:

| Package | Purpose |
|---------|---------|
| coordinator.py | Main 5-min loop orchestrator + 3-sec fast execution thread |
| gates/ | 6-gate signal pipeline (zone, trend, ATR, sucker_move, pitchfork, OTR) |
| signals/ | Gate orchestrator, scoring system, extreme reversal engine |
| positions/ | Post-entry management (BE ratchet, hybrid trailing stop, green exit) |
| core/ | OANDA client, execution router, fee calculator |
| zones/ | Zone detection (PDH/PDL, magic lines, tiered zones) |
| box/ | Box state machine (ranging, broken, alternative box) |
| regime/ | Market regime supervisor (ACTIVE blocker since 2026-03-31) |
| sizing/ | Margin-based position sizing (80% utilization) |
| quality/ | Trade quality tracking (MFE/MAE, entry context) |
| harvester/ | Partial profit extraction at equity tiers |
| probes/ | Liquidity sweep pre-confirmation (disabled) |

## Scoring System (calibrated 2026-04-09 from OANDA trade data)

Layer 1: Validity pre-filter (hard rejects)
Layer 2: Base scoring (tier, ATR, OTR, R:R, signal type)
Layer 3: Contextual modifiers (z-score, BB position, touches, gap)
Layer 4: OANDA truth adjustments:
- Ranging market: -20 pts (PF 0.33 both bots)
- CT + power_of_towers: -15 pts
- CT + john_wick: -5 pts
- CT Tier 1: -10 pts (worst CT category)
- CT Tier 2: +5 pts (profitable CT category)
- z-score alignment: +5 pts
- Signal type: john_wick +15, power_of_towers +5
- Regime: NORMAL +10, CAUTION/RESTRICTED -10
- R:R scored against TP1 (realistic target), hard gate uses TP2

## SL/TP

Zone-anchored (NOT fixed pips):
- SL: Behind the pitchfork reversal candle + buffer
- TP1: Daily box center
- TP2: Opposite daily box wall (OANDA native TP), clamped to 3x daily ATR

The config values sl_pips/tp1_pips/tp2_pips are only used by the disabled probe system.

## Position Management

1. Break-even at 50% of way to TP1
2. Lock SL at TP1 when price passes TP1
3. Hybrid trailing stop: max(hourly candle trail, 80% profit lock, 1.5x ATR trail)
4. Hourly green exit: if profitable and stale, exit via limit order
5. SL limit system: proactive limit orders near stop (better fills than market stop)

## Operations

- Service: systemctl --user {start|stop|restart|status} mr-scrooge-v2.service
- Logs: logs/mrscroogev2.log (main), logs/decisions.log, logs/trades.log
- Status: data/status.json (updated every cycle)
- Config: config.py (frozen dataclass, env overrides via SCROOGE_ prefix)
- Account: OANDA practice (api-fxpractice.oanda.com)
