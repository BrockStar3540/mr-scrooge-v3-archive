"""Strategy-first context fitting for raw-M5 v2 candidates.

This intentionally does NOT use regime/context as a precondition for deciding
whether a strategy exists. It tests the strategy at pair level first:

    trigger_type x pair x direction

After the pair-level baseline is measured, we inspect which context labels
explain the wins:

    session, session_quarter, M15 trend, H1 regime, BB/RSI/EMA/BBW/echo bins

That makes regimes explanatory outputs, not up-front filters. A broad
strategy/pair can be net-losing and still contain a valid micro-regime; the
important quantity is the lift from parent baseline to context slice.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE = Path("/home/ubuntu/mr-scrooge-v3/research/raw-m5-winner-factory-v2")
EVENTS = BASE / "raw_m5_v2_candidate_events.parquet"


PAIR_KEYS = ["trigger_type", "pair", "pair_family", "direction"]
CONTEXT_DIMS = [
    "session_bucket",
    "session_quarter",
    "m15_trend",
    "h1_regime",
    "bb_pos_bin",
    "rsi_bin",
    "ema20_dist_bin",
    "bbw_bin",
    "echo_ratio_bin",
]


def summarize(group: pd.DataFrame) -> pd.Series:
    n = len(group)
    pos = group.loc[group["realized_at_2R_net"] > 0, "realized_at_2R_net"].sum()
    neg = -group.loc[group["realized_at_2R_net"] < 0, "realized_at_2R_net"].sum()
    return pd.Series({
        "n": n,
        "win_rate": float((group["realized_at_2R_net"] > 0).mean()) if n else 0.0,
        "clean_2r_rate": float(group["clean_2r"].mean()) if n else 0.0,
        "gave_back_rate": float(group["gave_back_green"].mean()) if n else 0.0,
        "clean_stop_rate": float(group["clean_stop"].mean()) if n else 0.0,
        "mean_R_2r": float(group["realized_at_2R_net"].mean()) if n else 0.0,
        "median_mfe_r": float(group["mfe_r_net"].median()) if n else 0.0,
        "median_mae_r": float(group["mae_r"].median()) if n else 0.0,
        "profit_factor": float(pos / neg) if neg > 0 else (999.0 if pos > 0 else 0.0),
    })


def era_summary(df: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    rows = []
    for era, suffix in [("discovery", "disc"), ("holdout", "hold")]:
        x = df[df["era"] == era].copy()
        if x.empty:
            continue
        x["win"] = x["realized_at_2R_net"] > 0
        x["pos_R"] = x["realized_at_2R_net"].clip(lower=0)
        x["neg_R_abs"] = (-x["realized_at_2R_net"].clip(upper=0))
        g = x.groupby(keys, dropna=False)
        s = g.agg(
            n=("realized_at_2R_net", "size"),
            win_rate=("win", "mean"),
            clean_2r_rate=("clean_2r", "mean"),
            gave_back_rate=("gave_back_green", "mean"),
            clean_stop_rate=("clean_stop", "mean"),
            mean_R_2r=("realized_at_2R_net", "mean"),
            median_mfe_r=("mfe_r_net", "median"),
            median_mae_r=("mae_r", "median"),
            pos_R=("pos_R", "sum"),
            neg_R_abs=("neg_R_abs", "sum"),
        ).reset_index()
        s["profit_factor"] = s.apply(
            lambda r: (r["pos_R"] / r["neg_R_abs"]) if r["neg_R_abs"] > 0 else (999.0 if r["pos_R"] > 0 else 0.0),
            axis=1,
        )
        s = s.drop(columns=["pos_R", "neg_R_abs"])
        metric_cols = [c for c in s.columns if c not in keys]
        rows.append(s.rename(columns={c: f"{c}_{suffix}" for c in metric_cols}))
    if not rows:
        return pd.DataFrame(columns=keys)
    out = rows[0]
    for r in rows[1:]:
        out = out.merge(r, on=keys, how="outer")
    for suffix in ("disc", "hold"):
        for metric in (
            "n", "win_rate", "clean_2r_rate", "gave_back_rate",
            "clean_stop_rate", "mean_R_2r", "median_mfe_r",
            "median_mae_r", "profit_factor",
        ):
            col = f"{metric}_{suffix}"
            if col not in out.columns:
                out[col] = 0
    return out.fillna(0)


def era_summary_slow(df: pd.DataFrame, keys: list[str]) -> pd.DataFrame:
    rows = []
    for era, suffix in [("discovery", "disc"), ("holdout", "hold")]:
        x = df[df["era"] == era]
        if x.empty:
            continue
        s = x.groupby(keys, dropna=False).apply(summarize).reset_index()
        metric_cols = [c for c in s.columns if c not in keys]
        s = s.rename(columns={c: f"{c}_{suffix}" for c in metric_cols})
        rows.append(s)
    if not rows:
        return pd.DataFrame(columns=keys)
    out = rows[0]
    for r in rows[1:]:
        out = out.merge(r, on=keys, how="outer")
    for suffix in ("disc", "hold"):
        for metric in (
            "n", "win_rate", "clean_2r_rate", "gave_back_rate",
            "clean_stop_rate", "mean_R_2r", "median_mfe_r",
            "median_mae_r", "profit_factor",
        ):
            col = f"{metric}_{suffix}"
            if col not in out.columns:
                out[col] = 0
    return out.fillna(0)


def main() -> None:
    df = pd.read_parquet(EVENTS)
    for c in ("clean_2r", "gave_back_green", "clean_stop"):
        df[c] = df[c].astype(bool)

    pair = era_summary(df, PAIR_KEYS)
    pair_survivors = pair[
        (pair["n_disc"] >= 100)
        & (pair["n_hold"] >= 30)
        & (pair["mean_R_2r_disc"] > 0)
        & (pair["mean_R_2r_hold"] > 0)
    ].copy()
    pair_survivors = pair_survivors.sort_values(
        ["mean_R_2r_hold", "mean_R_2r_disc"], ascending=False
    )

    fit_rows = []
    context_specs = [(dim, [dim]) for dim in CONTEXT_DIMS]
    context_specs += [
        ("session_quarter+m15_trend+h1_regime", ["session_quarter", "m15_trend", "h1_regime"]),
        ("session_bucket+m15_trend+h1_regime", ["session_bucket", "m15_trend", "h1_regime"]),
        ("m15_trend+h1_regime", ["m15_trend", "h1_regime"]),
        ("session_quarter+h1_regime", ["session_quarter", "h1_regime"]),
        ("session_quarter+m15_trend", ["session_quarter", "m15_trend"]),
    ]
    parent_cols = PAIR_KEYS + [
        "n_disc", "n_hold", "mean_R_2r_disc", "mean_R_2r_hold",
    ]
    parent = pair[parent_cols].rename(columns={
        "n_disc": "parent_n_disc",
        "n_hold": "parent_n_hold",
        "mean_R_2r_disc": "parent_mean_R_2r_disc",
        "mean_R_2r_hold": "parent_mean_R_2r_hold",
    })
    for dim_name, dim_cols in context_specs:
        ctx = era_summary(df, PAIR_KEYS + dim_cols)
        if ctx.empty:
            continue
        ctx = ctx.merge(parent, on=PAIR_KEYS, how="left")
        ctx = ctx[
            (ctx["n_disc"] >= 20)
            & (ctx["n_hold"] >= 8)
            & (ctx["mean_R_2r_disc"] > 0)
            & (ctx["mean_R_2r_hold"] > 0)
        ].copy()
        if ctx.empty:
            continue
        ctx["context_dim"] = dim_name
        ctx["context_value"] = ctx[dim_cols].astype(str).agg("|".join, axis=1)
        ctx["lift_disc"] = ctx["mean_R_2r_disc"] - ctx["parent_mean_R_2r_disc"]
        ctx["lift_hold"] = ctx["mean_R_2r_hold"] - ctx["parent_mean_R_2r_hold"]
        ctx["parent_negative_disc"] = ctx["parent_mean_R_2r_disc"] <= 0
        ctx["parent_negative_hold"] = ctx["parent_mean_R_2r_hold"] <= 0
        keep = [
            "trigger_type", "pair", "pair_family", "direction",
            "context_dim", "context_value",
            "n_disc", "mean_R_2r_disc", "clean_2r_rate_disc", "gave_back_rate_disc",
            "n_hold", "mean_R_2r_hold", "clean_2r_rate_hold", "gave_back_rate_hold",
            "parent_n_disc", "parent_n_hold",
            "parent_mean_R_2r_disc", "parent_mean_R_2r_hold",
            "lift_disc", "lift_hold",
            "parent_negative_disc", "parent_negative_hold",
        ]
        fit_rows.append(ctx[keep])

    fits = pd.concat(fit_rows, ignore_index=True) if fit_rows else pd.DataFrame()
    if not fits.empty:
        fits = fits.sort_values(["mean_R_2r_hold", "lift_hold"], ascending=False)

    # Compact regime suggestions: not names, just repeated context descriptors.
    if not fits.empty:
        regime_candidates = (
            fits.groupby(["trigger_type", "direction", "context_dim", "context_value"], dropna=False)
            .agg(
                cells=("pair", "count"),
                pairs=("pair", lambda s: ", ".join(sorted(set(s))[:12])),
                mean_hold_R=("mean_R_2r_hold", "mean"),
                mean_disc_R=("mean_R_2r_disc", "mean"),
                median_lift_hold=("lift_hold", "median"),
            )
            .reset_index()
            .sort_values(["cells", "mean_hold_R"], ascending=False)
        )
    else:
        regime_candidates = pd.DataFrame()

    pair_out = BASE / "report_strategy_first_pair_baselines.csv"
    pair_survivor_out = BASE / "report_strategy_first_pair_survivors.csv"
    fit_out = BASE / "report_strategy_first_context_fit.csv"
    reg_out = BASE / "report_strategy_first_regime_candidates.csv"
    summary_out = BASE / "summary_strategy_first_context_fit.md"
    pair.to_csv(pair_out, index=False)
    pair_survivors.to_csv(pair_survivor_out, index=False)
    fits.to_csv(fit_out, index=False)
    regime_candidates.to_csv(reg_out, index=False)

    lines = []
    lines.append("# Strategy-First Context Fit\n")
    lines.append("This pass tests strategy edges first at `trigger_type x pair x direction`. Context labels are fitted after the parent baseline is measured, and a parent can be losing overall.\n")
    lines.append("## Coverage\n")
    lines.append(f"- Raw-M5 candidate events: {len(df):,}\n")
    lines.append(f"- Pair-level strategy cells tested: {len(pair):,}\n")
    lines.append(f"- Pair-level strategy survivors without context: {len(pair_survivors):,}\n")
    lines.append(f"- Post-hoc context-fit rows: {len(fits):,}\n")
    lines.append("\n## Broad Pair-Level Baseline\n")
    lines.append("At `trigger_type x pair x direction`, no strategy survives without context. That means the edge is conditional; regimes have to be discovered from the context slices, not imposed first.\n")
    lines.append("\n## Top Broad Pair Baselines\n")
    display_cols = [
        "trigger_type", "pair", "pair_family", "direction",
        "n_disc", "mean_R_2r_disc", "clean_2r_rate_disc",
        "n_hold", "mean_R_2r_hold", "clean_2r_rate_hold",
        "gave_back_rate_hold",
    ]
    lines.append(pair.sort_values(["mean_R_2r_hold", "mean_R_2r_disc"], ascending=False)[display_cols].head(30).to_markdown(index=False))
    lines.append("\n## Top Post-Hoc Context Fits\n")
    if fits.empty:
        lines.append("No context slices passed the post-hoc fit gate.\n")
    else:
        lines.append(fits.head(60).to_markdown(index=False))
    lines.append("\n## Repeated Context Candidates\n")
    if regime_candidates.empty:
        lines.append("No repeated context candidates found.\n")
    else:
        lines.append(regime_candidates.head(40).to_markdown(index=False))
    lines.append("\n## Interpretation\n")
    lines.append("- Do not start with regimes. Start with the strategy and pair.\n")
    lines.append("- The broad parent strategy can lose; a regime is promoted when a post-hoc context repeatedly turns that parent into a survivor.\n")
    lines.append("- The existing `h1_regime`, `m15_trend`, and session labels are candidate descriptors, not authority.\n")
    lines.append("- If repeated context descriptors are too crude, the next step is to define a new regime from the shared OHLCV conditions of those surviving strategy/pair cells.\n")
    summary_out.write_text("\n".join(lines))

    print(summary_out)
    print(pair_out)
    print(fit_out)
    print(reg_out)
    print(f"pair_survivors={len(pair_survivors)} fits={len(fits)}")


if __name__ == "__main__":
    main()
