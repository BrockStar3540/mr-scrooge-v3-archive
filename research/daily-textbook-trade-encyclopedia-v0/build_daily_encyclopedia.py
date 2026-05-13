"""Daily Textbook Trade Encyclopedia v0.

For each pair-day, select a first-pass textbook trade from raw-M5 event
candidates. If that trade loses, find the best same-day repaired winner and log
both the failed first-pass and the winning replacement. The purpose is regime
classification and microstrategy extraction, not pretending hindsight was known.

Inputs:
  research/raw-m5-winner-factory-v2/raw_m5_v2_candidate_events.parquet

Outputs:
  daily_textbook_trade_ledger.csv/parquet
  regime_training_snapshots.csv
  strategy_encyclopedia.csv
  summary.md
"""
from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import pandas as pd

SRC = Path("/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v2/raw_m5_v2_candidate_events.parquet")
OUT = Path("/home/ubuntu/mr-scrooge-v3/research/daily-textbook-trade-encyclopedia-v0")
OUT.mkdir(parents=True, exist_ok=True)

STRATEGY = {
    "T1_bb_lower_reclaim": ("lower_band_reclaim_snapback_long", "Mean-reversion reclaim after lower-band pressure"),
    "T2_bb_upper_reject": ("upper_band_rejection_snapback_short", "Mean-reversion rejection after upper-band pressure"),
    "T3_band_reentry_long": ("lower_rail_band_reentry_long", "Failed downside continuation; close back inside band"),
    "T4_band_reentry_short": ("upper_rail_band_reentry_short", "Failed upside continuation; close back inside band"),
    "T5_ema20_reclaim_long": ("ema20_reclaim_continuation_long", "Reclaim EMA20 after pullback"),
    "T6_ema20_reject_short": ("ema20_rejection_continuation_short", "Reject EMA20 after pullback"),
    "T7_pdh_proximity_reversal": ("pdh_rail_reversal_short", "Prior-day high rail reversal"),
    "T7_pdl_proximity_reversal": ("pdl_rail_reversal_long", "Prior-day low rail reversal"),
    "T8_pdh_failed_breakout": ("failed_pdh_breakout_short", "Failed breakout above prior-day high"),
    "T8_pdl_failed_breakdown": ("failed_pdl_breakdown_long", "Failed breakdown below prior-day low"),
    "T9_session_open_fade": ("session_open_impulse_fade", "Fade early session impulse after extension"),
    "T10_compression_expansion": ("compression_expansion_breakout", "Compression release / range expansion"),
}

TRIGGER_PRIORITY = {
    "T8_pdh_failed_breakout": 1,
    "T8_pdl_failed_breakdown": 1,
    "T7_pdh_proximity_reversal": 2,
    "T7_pdl_proximity_reversal": 2,
    "T3_band_reentry_long": 3,
    "T4_band_reentry_short": 3,
    "T1_bb_lower_reclaim": 4,
    "T2_bb_upper_reject": 4,
    "T9_session_open_fade": 5,
    "T10_compression_expansion": 6,
    "T5_ema20_reclaim_long": 7,
    "T6_ema20_reject_short": 7,
}

FACTOR_COLS = [
    "pair", "pair_family", "entry_ts", "direction", "trigger_type", "strategy_name",
    "session_bucket", "session_quarter", "m15_trend", "h1_regime", "entry_price",
    "spread_pips", "spread_cost_R", "stop_pips", "bb_position", "bb_pos_bin",
    "bbw_a_bps", "bbw_bin", "echo_range_ratio", "echo_ratio_bin",
]


def load_events() -> pd.DataFrame:
    cols = [
        "pair", "pair_family", "entry_ts", "direction", "trigger_type", "session_bucket", "session_quarter",
        "m15_trend", "h1_regime", "entry_price", "spread_pips", "spread_cost_R", "stop_pips",
        "bb_position", "bb_pos_bin", "rsi", "rsi_bin", "ema20_dist_bps", "ema20_dist_bin", "bbw_a_bps", "bbw_bin", "echo_range_ratio", "echo_ratio_bin",
        "realized_at_1R_net", "realized_at_1_5R_net", "realized_at_2R_net", "mfe_r_net", "mae_r",
        "exit_reason", "exit_bars", "gave_back_green", "clean_stop", "clean_2r", "era",
    ]
    df = pd.read_parquet(SRC, columns=cols)
    df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True)
    df["trade_date"] = df["entry_ts"].dt.date.astype(str)
    df = df[df["session_bucket"] != "rollover"].copy()
    df["strategy_name"] = df["trigger_type"].map(lambda t: STRATEGY.get(t, (t, ""))[0])
    df["strategy_description"] = df["trigger_type"].map(lambda t: STRATEGY.get(t, (t, ""))[1])
    df["trigger_priority"] = df["trigger_type"].map(TRIGGER_PRIORITY).fillna(99).astype(int)
    # Spread-aware eligibility. Keep USD_MXN possible but require cost not absurd in R terms.
    df["eligible_textbook"] = (
        (df["spread_cost_R"] <= 0.30)
        & (df["stop_pips"] >= 3.0)
        & (df["stop_pips"] <= 80.0)
    )
    df["is_winner_net"] = df["realized_at_2R_net"] > 0
    df["is_clean_winner_net"] = df["clean_2r"] & (df["realized_at_2R_net"] > 1.50)
    # First-pass score uses information available at entry only. It is intentionally simple.
    session_bonus = df["session_quarter"].str.endswith("q1").astype(int) * 0.15
    spread_penalty = df["spread_cost_R"].clip(0, 1.0)
    trigger_score = (10 - df["trigger_priority"]) / 10.0
    df["textbook_entry_score"] = trigger_score + session_bonus - spread_penalty
    return df


def choose_first_pass(g: pd.DataFrame) -> pd.Series | None:
    x = g[g["eligible_textbook"]].copy()
    if x.empty:
        return None
    # First-pass means no outcome sorting. Choose best textbook-looking setup from entry info, then earliest.
    return x.sort_values(["textbook_entry_score", "entry_ts"], ascending=[False, True]).iloc[0]


def choose_repair(g: pd.DataFrame, after_ts=None) -> pd.Series | None:
    x = g[g["eligible_textbook"] & g["is_winner_net"]].copy()
    if after_ts is not None:
        x_after = x[x["entry_ts"] >= after_ts]
        if len(x_after):
            x = x_after
    if x.empty:
        return None
    # Repaired winner: choose strongest clean/net winner, then simpler/earlier.
    x["repair_score"] = (
        x["realized_at_2R_net"].fillna(-9)
        + x["mfe_r_net"].clip(0, 5).fillna(0) * 0.05
        - x["spread_cost_R"].fillna(1) * 0.50
        - x["exit_bars"].fillna(300) * 0.001
    )
    return x.sort_values(["repair_score", "entry_ts"], ascending=[False, True]).iloc[0]


def row_from_trade(kind: str, base, first=None, repair=None) -> dict:
    src = repair if kind == "repaired_winner" else first
    assert src is not None
    first_won = bool(first["is_winner_net"]) if first is not None else False
    repair_needed = first is not None and not first_won
    row = {
        "ledger_id": None,
        "trade_date": src["trade_date"],
        "pair": src["pair"],
        "pair_family": src["pair_family"],
        "record_type": kind,
        "first_pass_won": first_won,
        "repair_needed": repair_needed,
        "repair_available": repair is not None,
        "repair_type": "none" if kind == "first_pass" else "same_day_winner_replacement",
        "entry_ts": src["entry_ts"].isoformat(),
        "direction": src["direction"],
        "trigger_type": src["trigger_type"],
        "strategy_name": src["strategy_name"],
        "strategy_description": src["strategy_description"],
        "session_bucket": src["session_bucket"],
        "session_quarter": src["session_quarter"],
        "m15_trend": src["m15_trend"],
        "h1_regime": src["h1_regime"],
        "entry_price": src["entry_price"],
        "spread_pips": src["spread_pips"],
        "spread_cost_R": src["spread_cost_R"],
        "stop_pips": src["stop_pips"],
        "bb_position": src["bb_position"],
        "bb_pos_bin": src["bb_pos_bin"],
        "rsi": src["rsi"],
        "rsi_bin": src["rsi_bin"],
        "ema20_dist_bps": src["ema20_dist_bps"],
        "ema20_dist_bin": src["ema20_dist_bin"],
        "bbw_a_bps": src["bbw_a_bps"],
        "bbw_bin": src["bbw_bin"],
        "echo_range_ratio": src["echo_range_ratio"],
        "echo_ratio_bin": src["echo_ratio_bin"],
        "realized_at_1R_net": src["realized_at_1R_net"],
        "realized_at_1_5R_net": src["realized_at_1_5R_net"],
        "realized_at_2R_net": src["realized_at_2R_net"],
        "mfe_r_net": src["mfe_r_net"],
        "mae_r": src["mae_r"],
        "exit_reason": src["exit_reason"],
        "exit_bars": src["exit_bars"],
        "gave_back_green": src["gave_back_green"],
        "clean_stop": src["clean_stop"],
        "clean_2r": src["clean_2r"],
        "era": src["era"],
        "textbook_entry_score": src["textbook_entry_score"],
    }
    if first is not None and kind == "repaired_winner":
        row.update({
            "original_entry_ts": first["entry_ts"].isoformat(),
            "original_strategy_name": first["strategy_name"],
            "original_direction": first["direction"],
            "original_realized_at_2R_net": first["realized_at_2R_net"],
        })
    else:
        row.update({"original_entry_ts": "", "original_strategy_name": "", "original_direction": "", "original_realized_at_2R_net": np.nan})
    return row


def main():
    print("loading raw-M5 v2 candidate events...")
    df = load_events()
    print(f"events loaded: {len(df):,}; pairs={df['pair'].nunique()}; days={df['trade_date'].nunique()}")
    rows = []
    pair_days = 0
    for (pair, day), g in df.groupby(["pair", "trade_date"], sort=True):
        pair_days += 1
        first = choose_first_pass(g)
        if first is None:
            continue
        repair = None if bool(first["is_winner_net"]) else choose_repair(g, after_ts=first["entry_ts"])
        rows.append(row_from_trade("first_pass", None, first=first, repair=repair))
        if repair is not None:
            rows.append(row_from_trade("repaired_winner", None, first=first, repair=repair))
    ledger = pd.DataFrame(rows)
    ledger["ledger_id"] = [f"DTE-{i:07d}" for i in range(1, len(ledger) + 1)]
    ledger.to_csv(OUT / "daily_textbook_trade_ledger.csv", index=False)
    ledger.to_parquet(OUT / "daily_textbook_trade_ledger.parquet", index=False)

    # Regime training snapshots: one row per first-pass/repaired trade with entry-time factors.
    snapshots = ledger[["ledger_id", "record_type"] + [c for c in FACTOR_COLS if c in ledger.columns] + [
        "realized_at_2R_net", "mfe_r_net", "mae_r", "gave_back_green", "clean_stop", "clean_2r", "era",
    ]].copy()
    snapshots.to_csv(OUT / "regime_training_snapshots.csv", index=False)

    strat = []
    for trig, (name, desc) in STRATEGY.items():
        sub = ledger[(ledger["trigger_type"] == trig) & (ledger["record_type"] == "repaired_winner")]
        first = ledger[(ledger["trigger_type"] == trig) & (ledger["record_type"] == "first_pass")]
        strat.append({
            "trigger_type": trig,
            "strategy_name": name,
            "description": desc,
            "first_pass_count": len(first),
            "first_pass_win_rate": float((first["realized_at_2R_net"] > 0).mean()) if len(first) else 0.0,
            "repaired_winner_count": len(sub),
            "median_repaired_R": float(sub["realized_at_2R_net"].median()) if len(sub) else np.nan,
        })
    strat_df = pd.DataFrame(strat).sort_values("repaired_winner_count", ascending=False)
    strat_df.to_csv(OUT / "strategy_encyclopedia.csv", index=False)

    first = ledger[ledger.record_type == "first_pass"]
    repairs = ledger[ledger.record_type == "repaired_winner"]
    summary = []
    summary.append("# Daily Textbook Trade Encyclopedia v0")
    summary.append("")
    summary.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    summary.append(f"Source events: `{SRC}`")
    summary.append("")
    summary.append("## Frame")
    summary.append("")
    summary.append("For each pair-day, choose a first-pass textbook trade from raw-M5 event candidates using only entry-time quality. If that trade loses, find the same-day repaired winner and log the strategy/factor state. First-pass and repaired winner rows are kept separate so hindsight does not contaminate what was knowable at entry.")
    summary.append("")
    summary.append("## Counts")
    summary.append("")
    summary.append(f"- Pair-days scanned: {pair_days:,}")
    summary.append(f"- First-pass textbook trades: {len(first):,}")
    summary.append(f"- First-pass net winners: {(first["realized_at_2R_net"] > 0).sum():,} ({(first["realized_at_2R_net"] > 0).mean():.1%})")
    summary.append(f"- Repaired same-day winners found: {len(repairs):,}")
    summary.append(f"- Pair-days with no eligible first-pass trade: {pair_days - len(first):,}")
    summary.append("")
    summary.append("## Top Repaired Strategies")
    summary.append("")
    summary.append(strat_df.head(12).to_markdown(index=False, floatfmt=".3f"))
    summary.append("")
    summary.append("## Repaired Winners By Pair Family")
    summary.append("")
    pf = repairs.groupby(["pair_family", "strategy_name"]).size().reset_index(name="n").sort_values("n", ascending=False).head(30)
    summary.append(pf.to_markdown(index=False))
    summary.append("")
    summary.append("## Important Discipline")
    summary.append("")
    summary.append("A repaired winner is not claimed to be knowable by the first-pass rule. It is a supervised example for strategy discovery: here is the trade that would have won on that pair-day, and here are the factors/regime state at entry. The next step is to cluster repaired winners and write deterministic rules that can be tested without hindsight.")
    summary.append("")
    summary.append("## Next Step")
    summary.append("")
    summary.append("Cluster `repaired_winner` rows by strategy_name, pair_family, session_quarter, direction, M15/H1 context, and factor bins. Generate named microstrategy techniques from the clusters, then backtest those rules against all raw-M5 events.")
    (OUT / "summary.md").write_text("\n".join(summary) + "\n")

    print(f"first-pass trades: {len(first):,}; win rate={(first["realized_at_2R_net"] > 0).mean():.2%}; repaired={len(repairs):,}")
    print(strat_df.head(12).to_string(index=False))
    print(f"wrote {OUT}")

if __name__ == "__main__":
    main()
