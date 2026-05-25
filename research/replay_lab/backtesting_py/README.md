# Mr Scrooge V3 — backtesting.py Replay Lab

Deterministic offline replay around the LIVE strategy modules. Use this
for strategy truth-testing, direction inversion tests, entry-geometry
experiments, management ablations, and regression checks. NOT a
replacement for the live engine — broker behavior, timeouts, and
portfolio throttles are out of scope.

## Quick start

```python
from research.replay_lab.backtesting_py.models import ReplaySpec
from research.replay_lab.backtesting_py.experiments import (
    run_single_replay, run_direction_comparison,
    run_entry_mode_comparison, run_management_ablation,
)

# Single replay: USD_JPY canonical_lien_dbb, last 14 days
spec = ReplaySpec(
    symbol="USD_JPY",
    date_from="2026-05-11T00:00:00Z",
    date_to="2026-05-25T00:00:00Z",
    entry_mode="signal",
    management_mode="tp1_be",
)
r = run_single_replay(spec, family="canonical_lien_dbb")
print(r["stats"])

# Direction comparison
df = run_direction_comparison(spec, family="canonical_lien_dbb")
```

## Architecture

| Module | Role |
|---|---|
| `models.py` | `ReplaySpec` + mode literals |
| `data_adapter.py` | OANDA OHLC fetcher (cached at `cache/`) |
| `context_factory.py` | Builds live-shaped `SymbolContext` per bar |
| `router_adapter.py` | Wraps live `RoutingTable`; emulates 3 routing modes |
| `management_adapter.py` | TP1 / BE / ratchet using `Trade.close()` + writable `Trade.sl` |
| `strategy_wrappers.py` | `backtesting.Strategy` subclasses that call live V3 modules |
| `experiments.py` | 3 canned experiments + `run_single_replay` |
| `regression_suite.py` | Fixed benchmark cases for commit-time regression |

## What this lab IS

- **Strategy-truth testing** — does the live code have edge on a window?
- **Direction inversion** — same signals/bars, native vs reversed
- **Entry geometry** — signal vs pullback_2/4/old_stop_zone
- **Management ablation** — none / tp1_only / tp1_be / tp1_be_ratchet
- **Routing-mode test** — exact_strategy_only vs +family vs +loose_override
- **Pre-deploy regression** — benchmark cases vs commit baseline

## What this lab IS NOT

- A live engine simulator (broker, timeouts, orphan recovery → live runtime)
- A multi-pair portfolio simulator (cross-currency throttles → live runtime)
- A spread-modeling truth (single fixed spread per pair, not time-varying)
- An intrabar simulator (decisions per completed bar, fills next-bar-open
  unless LIMIT triggers within bar range)

## Outputs

Results write to `research/replay_lab/results/<timestamp>/`:
- `*.csv` — per-experiment summary
- `trades_*.csv` — per-trade detail
- `spec.json` — replay configuration

## First milestone

Run on USD_JPY canonical_lien_dbb, last 7-14 days, 3 experiments:
1. Direction comparison (native vs reversed)
2. Entry mode comparison (signal / pullback_2 / pullback_4 / old_stop_zone)
3. Management ablation (none / tp1_only / tp1_be / tp1_be_ratchet)

Then expand to box_master_theory + textbook_scalper families.
