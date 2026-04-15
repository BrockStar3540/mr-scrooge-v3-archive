# Regime Supervisor — NOTES

## What this is

An **active entry blocker** (activated 2026-03-31). It observes market conditions,
scores them, and enforces entry suppression when conditions are hostile.

Previously passive (logged protests only). Activated after 3+ weeks of data showed
regime score reliably predicts trade outcomes:
- NORMAL regime: 77.8% WR, +,037 (V2 OANDA data, Apr 2026)
- CAUTION regime: 57.9% WR, -,719
- RESTRICTED: 50% WR, -,138

## How it enforces

In , after signal evaluation:
- **Score >= +1**: Entry allowed (signal proceeds to ranking)
- **Score < +1**:  — entry suppressed
- **Score <= -3**:  — entry suppressed
- **Hysteresis**: After BLOCKED (score <= -3), require score >= +2 to re-enter
- **RESTRICTED**: Allows entry but halves position size (50%)

Regime score also feeds the scoring system (2026-04-09 audit):
- NORMAL: +10 pts to signal score
- CAUTION/RESTRICTED: -10 pts to signal score

## The four signals

### 1. box_acceptance (-1 to -2)
Price closing and holding outside PDH/PDL.
2+ consecutive closes outside = market accepting a new range = bad for fading.

### 2. rejection_decay (-1 to -2, or +2 if clean)
Quality of recent wall touches.
Clean rejection = touched wall, closed well away.
Weak = touched, lingered near it.
Failed = accepted through it.

### 3. expansion_pressure (-1 to -2)
ATR expanding directionally without mean reversion.

### 4. qualified_failures (-1 to -3) — most important
Our own gated setups hitting SL recently.
The market is directly telling us our framework isn't being honored.

## Score thresholds

| Score  | State      | Action                                      |
|--------|------------|---------------------------------------------|
| >= +2  | NORMAL     | Full trading, +10 scoring bonus             |
| 0..+1  | CAUTION    | Entry allowed if score >= +1, -10 scoring   |
| -1..-2 | RESTRICTED | Size halved, -10 scoring                    |
| <= -3  | BLOCKED    | Halt new entries entirely                    |

## Data files

-  — one JSON per event (name is historical; file logs both observations and active blocks)
-  and  filled in when trade closes

## History

- 2026-03-22: Created as passive observer
- 2026-03-31: Activated as entry blocker (score >= +1 required)
- 2026-04-09: Integrated into scoring system (+10 NORMAL, -10 CAUTION)
