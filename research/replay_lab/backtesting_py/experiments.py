"""Experiment runners.

Each function takes a ReplaySpec or list of specs, runs the backtest(s),
and returns a summary DataFrame + writes artifacts to results/<ts>/.
"""
from __future__ import annotations
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from backtesting import Backtest

from .models import ReplaySpec
from .data_adapter import load_symbol_replay_bundle
from .router_adapter import load_routing_table
from .strategy_wrappers import make_strategy_class, instantiate_live_strategy

log = logging.getLogger("replay_lab.experiments")

RESULTS_ROOT = Path("/home/ubuntu/mr-scrooge-v3/research/replay_lab/results")
RESULTS_ROOT.mkdir(parents=True, exist_ok=True)


def _results_dir() -> Path:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    d = RESULTS_ROOT / ts
    d.mkdir(parents=True, exist_ok=True)
    return d


def run_single_replay(spec: ReplaySpec, family: str = "canonical_lien_dbb") -> dict:
    """Run one ReplaySpec end-to-end."""
    log.info("run_single_replay: %s", spec.key())
    bundle = load_symbol_replay_bundle(
        spec.symbol, spec.date_from, spec.date_to, spec.spread_mode,
    )
    if bundle["M5"].empty:
        return {"error": "no_data", "spec": spec.__dict__}

    table = load_routing_table(spec.routing_table_path)
    strat_cls = make_strategy_class(family)
    strat_cls._spec = spec
    strat_cls._bundle = bundle
    strat_cls._routing_table = table
    strat_cls._strategy_module = instantiate_live_strategy(family)

    bt = Backtest(
        bundle["M5"][["Open","High","Low","Close","Volume"]],
        strat_cls,
        cash=spec.cash, margin=spec.margin,
        exclusive_orders=True,
    )
    stats = bt.run()
    return {
        "spec": spec.__dict__,
        "family": family,
        "stats": {k: (v.isoformat() if hasattr(v, "isoformat") else v)
                  for k, v in stats.to_dict().items() if k != "_trades"},
        "trades": stats._trades.to_dict(orient="records") if hasattr(stats, "_trades") else [],
    }


# ============================================================
# Experiment 1: direction comparison
# ============================================================
def run_direction_comparison(base_spec: ReplaySpec, family: str = "canonical_lien_dbb") -> pd.DataFrame:
    """Same symbol/strategy/window. Compare native vs reversed."""
    rd = _results_dir()
    rows = []
    for mode in ("native", "reversed"):
        spec = ReplaySpec(**{**base_spec.__dict__, "direction_mode": mode,
                              "label": f"{base_spec.label or base_spec.symbol}.{mode}"})
        try:
            r = run_single_replay(spec, family=family)
            if "error" in r:
                rows.append({"label": spec.label, "error": r["error"]})
                continue
            s = r["stats"]
            rows.append({
                "label": spec.label, "direction_mode": mode,
                "n_trades": s.get("# Trades", 0),
                "win_rate_pct": s.get("Win Rate [%]", 0),
                "return_pct": s.get("Return [%]", 0),
                "expectancy_pct": s.get("Expectancy [%]", 0),
                "sharpe": s.get("Sharpe Ratio", 0),
                "max_dd_pct": s.get("Max. Drawdown [%]", 0),
                "avg_trade_pct": s.get("Avg. Trade [%]", 0),
            })
            # Save trades CSV
            if r.get("trades"):
                pd.DataFrame(r["trades"]).to_csv(rd / f"trades_{mode}.csv", index=False)
        except Exception as e:
            rows.append({"label": spec.label, "error": str(e)})
            log.exception("direction comparison failed for %s", mode)
    df = pd.DataFrame(rows)
    df.to_csv(rd / "direction_comparison_summary.csv", index=False)
    (rd / "spec.json").write_text(json.dumps(base_spec.__dict__, default=str, indent=2))
    print(f"results -> {rd}")
    print(df.to_string(index=False))
    return df


# ============================================================
# Experiment 2: entry mode comparison
# ============================================================
def run_entry_mode_comparison(base_spec: ReplaySpec, family: str = "canonical_lien_dbb") -> pd.DataFrame:
    rd = _results_dir()
    rows = []
    for mode in ("signal", "pullback_2", "pullback_4", "old_stop_zone"):
        spec = ReplaySpec(**{**base_spec.__dict__, "entry_mode": mode,
                              "label": f"{base_spec.label or base_spec.symbol}.{mode}"})
        try:
            r = run_single_replay(spec, family=family)
            if "error" in r:
                rows.append({"entry_mode": mode, "error": r["error"]})
                continue
            s = r["stats"]
            rows.append({
                "entry_mode": mode,
                "n_trades": s.get("# Trades", 0),
                "win_rate_pct": s.get("Win Rate [%]", 0),
                "return_pct": s.get("Return [%]", 0),
                "expectancy_pct": s.get("Expectancy [%]", 0),
                "avg_trade_pct": s.get("Avg. Trade [%]", 0),
            })
            if r.get("trades"):
                pd.DataFrame(r["trades"]).to_csv(rd / f"trades_entry_{mode}.csv", index=False)
        except Exception as e:
            rows.append({"entry_mode": mode, "error": str(e)})
    df = pd.DataFrame(rows)
    df.to_csv(rd / "entry_mode_summary.csv", index=False)
    print(f"results -> {rd}")
    print(df.to_string(index=False))
    return df


# ============================================================
# Experiment 3: management ablation
# ============================================================
def run_management_ablation(base_spec: ReplaySpec, family: str = "canonical_lien_dbb") -> pd.DataFrame:
    rd = _results_dir()
    rows = []
    for mode in ("none", "tp1_only", "tp1_be", "tp1_be_ratchet"):
        spec = ReplaySpec(**{**base_spec.__dict__, "management_mode": mode,
                              "label": f"{base_spec.label or base_spec.symbol}.mgmt_{mode}"})
        try:
            r = run_single_replay(spec, family=family)
            if "error" in r:
                rows.append({"management_mode": mode, "error": r["error"]})
                continue
            s = r["stats"]
            rows.append({
                "management_mode": mode,
                "n_trades": s.get("# Trades", 0),
                "win_rate_pct": s.get("Win Rate [%]", 0),
                "return_pct": s.get("Return [%]", 0),
                "expectancy_pct": s.get("Expectancy [%]", 0),
                "avg_trade_pct": s.get("Avg. Trade [%]", 0),
            })
            if r.get("trades"):
                pd.DataFrame(r["trades"]).to_csv(rd / f"trades_mgmt_{mode}.csv", index=False)
        except Exception as e:
            rows.append({"management_mode": mode, "error": str(e)})
    df = pd.DataFrame(rows)
    df.to_csv(rd / "management_ablation_summary.csv", index=False)
    print(f"results -> {rd}")
    print(df.to_string(index=False))
    return df


# ============================================================
# Regression suite
# ============================================================
def benchmark_cases() -> list[ReplaySpec]:
    """Fixed benchmark cases that catch silent code drift."""
    from datetime import datetime, timezone, timedelta
    end = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    start = (datetime.now(timezone.utc) - timedelta(days=14)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return [
        ReplaySpec(symbol="USD_JPY", date_from=start, date_to=end,
                   strategy_name="DBB3_sell_zone_sustained_short",
                   label="benchmark_usdjpy_dbb3_short"),
        ReplaySpec(symbol="USD_JPY", date_from=start, date_to=end,
                   strategy_name="DBB3_buy_zone_sustained_long",
                   label="benchmark_usdjpy_dbb3_long"),
        ReplaySpec(symbol="NZD_JPY", date_from=start, date_to=end,
                   strategy_name="DBB1_sell_zone_short",
                   label="benchmark_nzdjpy_dbb1_short"),
        ReplaySpec(symbol="GBP_JPY", date_from=start, date_to=end,
                   strategy_name="DBB3_buy_zone_sustained_long",
                   label="benchmark_gbpjpy_dbb3_long"),
    ]
