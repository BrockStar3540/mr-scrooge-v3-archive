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


# ============================================================
# Multi-pair runner — backtesting.py is single-asset; we loop + aggregate
# ============================================================
LIVE_PAIRS = [
    "EUR_USD", "GBP_USD", "USD_JPY", "USD_CHF", "USD_CAD",
    "AUD_USD", "NZD_USD",
    "EUR_JPY", "GBP_JPY", "CHF_JPY", "AUD_JPY", "CAD_JPY", "NZD_JPY",
    "EUR_GBP", "EUR_CHF", "EUR_AUD", "EUR_CAD", "EUR_NZD",
    "GBP_AUD", "GBP_CAD", "GBP_CHF", "GBP_NZD",
    "AUD_CAD", "AUD_NZD", "AUD_CHF",
    "NZD_CAD", "NZD_CHF",
]

LIVE_FAMILIES = [
    "canonical_lien_dbb",
    "box_master_theory",
    "canonical_darvas",
    "probes",
]


def run_pair_sweep(
    base_spec: ReplaySpec,
    pairs: list[str] | None = None,
    families: list[str] | None = None,
) -> pd.DataFrame:
    """For each (pair, family), run a single replay and aggregate to one summary.

    Returns a DataFrame with one row per (pair, family) cell.
    """
    rd = _results_dir()
    pairs = pairs or LIVE_PAIRS
    families = families or LIVE_FAMILIES
    rows = []
    for pair in pairs:
        for family in families:
            spec = ReplaySpec(**{**base_spec.__dict__,
                                  "symbol": pair,
                                  "label": f"{pair}.{family}"})
            try:
                r = run_single_replay(spec, family=family)
                if "error" in r:
                    rows.append({"pair": pair, "family": family,
                                 "error": r["error"]})
                    continue
                st = r["stats"]
                rows.append({
                    "pair": pair, "family": family,
                    "n_trades": st.get("# Trades", 0),
                    "wr": st.get("Win Rate [%]", 0),
                    "return_pct": st.get("Return [%]", 0),
                    "expectancy_pct": st.get("Expectancy [%]", 0),
                    "max_dd_pct": st.get("Max. Drawdown [%]", 0),
                    "avg_trade_pct": st.get("Avg. Trade [%]", 0),
                    "sharpe": st.get("Sharpe Ratio", 0),
                })
                if r.get("trades"):
                    pd.DataFrame(r["trades"]).to_csv(
                        rd / f"trades_{pair}_{family}.csv", index=False
                    )
            except Exception as e:
                log.exception("pair=%s family=%s failed", pair, family)
                rows.append({"pair": pair, "family": family, "error": str(e)})
    df = pd.DataFrame(rows)
    df.to_csv(rd / "pair_sweep_summary.csv", index=False)
    # Aggregate per family across pairs
    g = df.dropna(subset=["n_trades"]).groupby("family").agg(
        pairs=("pair","nunique"),
        total_trades=("n_trades","sum"),
        avg_wr=("wr","mean"),
        avg_return=("return_pct","mean"),
        avg_expectancy=("expectancy_pct","mean"),
    ).reset_index()
    g.to_csv(rd / "family_rollup.csv", index=False)
    print(f"\nresults -> {rd}")
    print("\n=== Per family rollup ===")
    print(g.to_string(index=False))
    return df


def run_cell_sweep(
    base_spec: ReplaySpec,
    routing_table_path: str | None = None,
    max_cells: int | None = None,
) -> pd.DataFrame:
    """Walk every (pair, session, regime, strategy) cell in the routing table
    and run a focused replay per cell. Slow but exhaustive."""
    from .router_adapter import load_routing_table
    table = load_routing_table(routing_table_path)
    raw = table.raw_table if hasattr(table, "raw_table") else None
    if raw is None:
        # Direct parquet read fallback
        path = routing_table_path or "data/routing_table_v10_fast_v1_13_full_mirror.parquet"
        if not Path(path).is_absolute():
            path = "/home/ubuntu/mr-scrooge-v3/" + path
        raw = pd.read_parquet(path)
    cells = raw[["pair","session_bucket","technical_regime_53","strategy","family","direction"]].drop_duplicates()
    if max_cells:
        cells = cells.head(max_cells)
    print(f"sweeping {len(cells)} cells...")
    rd = _results_dir()
    rows = []
    for _, c in cells.iterrows():
        spec = ReplaySpec(**{**base_spec.__dict__,
                              "symbol": c["pair"],
                              "label": f"{c['pair']}.{c['strategy']}.{c['session_bucket']}.{c['technical_regime_53']}"})
        try:
            r = run_single_replay(spec, family=c["family"])
            if "error" in r:
                rows.append({**c.to_dict(), "error": r["error"]}); continue
            st = r["stats"]
            rows.append({
                "pair": c["pair"], "session": c["session_bucket"],
                "regime": c["technical_regime_53"], "strategy": c["strategy"],
                "family": c["family"], "direction": c["direction"],
                "n_trades": st.get("# Trades", 0),
                "wr": st.get("Win Rate [%]", 0),
                "return_pct": st.get("Return [%]", 0),
                "expectancy_pct": st.get("Expectancy [%]", 0),
            })
        except Exception as e:
            rows.append({**c.to_dict(), "error": str(e)})
    df = pd.DataFrame(rows)
    df.to_csv(rd / "cell_sweep_summary.csv", index=False)
    print(f"results -> {rd}")
    return df
