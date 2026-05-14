"""Mine winner islands inside mixed textbook-regime cells.

Goal
----
Find small, high-purity winner clusters inside a broad mixed cell:

    strategy_id x pair x direction x technical_regime_53

This is deliberately different from a global decision tree. A useful island can
capture only 10 winners if it excludes almost all losers. Those islands become
micro-strategy candidates; the "regime" is the factor band that explains the
winner pocket.

Inputs are the OHLCV strategy-library trade logs, which already contain:
strategy, pair, direction, technical regime, session, entry factors, and
realized outcome.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd


BASE = Path("/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0")
OUT = BASE

GROUP_KEYS = ["strategy_id", "pair", "pair_family", "direction", "technical_regime_53"]
CONT_FACTORS = ["ATR_ratio", "ADX14", "BB_compress", "RSI14", "price_pos", "volume_ratio", "hour_utc"]
CAT_FACTORS = ["session_bucket"]

MIN_CELL_N = 200
MIN_CELL_WINS = 20
MIN_CELL_LOSSES = 50
MIN_ISLAND_WINS = 10
MAX_ISLAND_LOSSES_STRICT = 2
MIN_ISLAND_WR = 0.80
MAX_ISLAND_FRAC = 0.45


@dataclass
class Candidate:
    group: tuple
    factor: str
    rule: str
    lo: float | str
    hi: float | str
    selected: pd.Series
    parent_n: int
    parent_w: int
    parent_l: int


def load_logs() -> pd.DataFrame:
    cols = GROUP_KEYS + [
        "technical_regime_desc", "entry_ts", "era", "is_win", "realized_R",
        "clean_2r", "gave_back_green",
    ] + CONT_FACTORS + CAT_FACTORS
    parts = []
    for path in sorted(BASE.glob("trade_log_all_*.parquet")):
        df = pd.read_parquet(path, columns=[c for c in cols if c])
        parts.append(df)
    out = pd.concat(parts, ignore_index=True)
    out["is_win"] = out["is_win"].astype(bool)
    out["is_loss"] = ~out["is_win"]
    return out


def quantile_intervals(values: pd.Series, bins: int = 20) -> list[tuple[float, float]]:
    x = values.dropna().astype(float)
    if len(x) < 30:
        return []
    qs = np.linspace(0, 1, bins + 1)
    edges = np.unique(np.nanquantile(x, qs))
    if len(edges) < 3:
        return []
    intervals: list[tuple[float, float]] = []
    # One-sided tails and compact interior bands. Keep intervals coarse enough
    # that they describe a regime, not a single timestamp.
    for i in range(len(edges) - 1):
        for j in range(i + 1, len(edges)):
            lo, hi = float(edges[i]), float(edges[j])
            if hi <= lo:
                continue
            intervals.append((lo, hi))
    return intervals


def add_metrics(row: dict, sub: pd.DataFrame, mask: pd.Series) -> dict:
    selected = sub[mask]
    wins = int(selected["is_win"].sum())
    losses = int((~selected["is_win"]).sum())
    n = wins + losses
    parent_wr = row["parent_wins"] / row["parent_n"] if row["parent_n"] else 0.0
    wr = wins / n if n else 0.0
    disc = selected[selected["era"] == "discovery"]
    hold = selected[selected["era"] == "holdout"]
    row.update({
        "island_n": n,
        "island_wins": wins,
        "island_losses": losses,
        "island_wr": wr,
        "parent_wr": parent_wr,
        "wr_lift": wr - parent_wr,
        "mean_R": float(selected["realized_R"].mean()) if n else 0.0,
        "sum_R": float(selected["realized_R"].sum()) if n else 0.0,
        "clean_2r_rate": float(selected["clean_2r"].mean()) if n else 0.0,
        "gave_back_rate": float(selected["gave_back_green"].mean()) if n else 0.0,
        "disc_n": int(len(disc)),
        "disc_wins": int(disc["is_win"].sum()) if len(disc) else 0,
        "disc_losses": int((~disc["is_win"]).sum()) if len(disc) else 0,
        "disc_wr": float(disc["is_win"].mean()) if len(disc) else 0.0,
        "hold_n": int(len(hold)),
        "hold_wins": int(hold["is_win"].sum()) if len(hold) else 0,
        "hold_losses": int((~hold["is_win"]).sum()) if len(hold) else 0,
        "hold_wr": float(hold["is_win"].mean()) if len(hold) else 0.0,
    })
    return row


def maybe_record(
    rows: list[dict],
    sub: pd.DataFrame,
    mask: pd.Series,
    base_row: dict,
) -> None:
    n = int(mask.sum())
    if n == 0 or n > base_row["parent_n"] * MAX_ISLAND_FRAC:
        return
    wins = int(sub.loc[mask, "is_win"].sum())
    losses = n - wins
    if wins < MIN_ISLAND_WINS:
        return
    wr = wins / n
    if not (losses <= MAX_ISLAND_LOSSES_STRICT or wr >= MIN_ISLAND_WR):
        return
    rows.append(add_metrics(dict(base_row), sub, mask))


def mine_one_factor(sub: pd.DataFrame, group: tuple) -> list[dict]:
    parent_n = len(sub)
    parent_w = int(sub["is_win"].sum())
    parent_l = parent_n - parent_w
    base = {k: v for k, v in zip(GROUP_KEYS, group)}
    base.update({
        "technical_regime_desc": str(sub["technical_regime_desc"].iloc[0]),
        "parent_n": parent_n,
        "parent_wins": parent_w,
        "parent_losses": parent_l,
    })
    rows: list[dict] = []

    for factor in CONT_FACTORS:
        vals = sub[factor]
        if vals.notna().sum() < 50:
            continue
        for lo, hi in quantile_intervals(vals, bins=20):
            mask = vals.ge(lo) & vals.le(hi)
            row = dict(base)
            row.update({
                "rule_depth": 1,
                "factor_1": factor,
                "op_1": "between",
                "lo_1": lo,
                "hi_1": hi,
                "factor_2": "",
                "op_2": "",
                "lo_2": "",
                "hi_2": "",
            })
            maybe_record(rows, sub, mask.fillna(False), row)
    for factor in CAT_FACTORS:
        for val in sorted(sub[factor].dropna().unique()):
            mask = sub[factor].eq(val)
            row = dict(base)
            row.update({
                "rule_depth": 1,
                "factor_1": factor,
                "op_1": "==",
                "lo_1": str(val),
                "hi_1": str(val),
                "factor_2": "",
                "op_2": "",
                "lo_2": "",
                "hi_2": "",
            })
            maybe_record(rows, sub, mask, row)
    return rows


def refine_two_factor(sub: pd.DataFrame, islands: pd.DataFrame) -> list[dict]:
    rows: list[dict] = []
    if islands.empty:
        return rows
    # Refine only meaningful one-factor islands that still include losers.
    seed = islands[
        (islands["rule_depth"] == 1)
        & (islands["island_wins"] >= MIN_ISLAND_WINS)
        & (islands["island_losses"] > 0)
    ].copy()
    seed = seed.sort_values(["island_wr", "island_wins"], ascending=False).head(200)
    for _, s in seed.iterrows():
        m1 = apply_rule(sub, s["factor_1"], s["op_1"], s["lo_1"], s["hi_1"])
        subset = sub[m1].copy()
        if len(subset) < MIN_ISLAND_WINS + 1:
            continue
        for factor in CONT_FACTORS:
            if factor == s["factor_1"]:
                continue
            vals = subset[factor]
            if vals.notna().sum() < 20:
                continue
            for lo, hi in quantile_intervals(vals, bins=10):
                m2_local = vals.ge(lo) & vals.le(hi)
                full_mask = pd.Series(False, index=sub.index)
                full_mask.loc[subset.index] = m2_local.fillna(False)
                row = s.to_dict()
                row.update({
                    "rule_depth": 2,
                    "factor_2": factor,
                    "op_2": "between",
                    "lo_2": lo,
                    "hi_2": hi,
                })
                maybe_record(rows, sub, full_mask, row)
    return rows


def apply_rule(sub: pd.DataFrame, factor: str, op: str, lo, hi) -> pd.Series:
    if op == "==":
        return sub[factor].astype(str).eq(str(lo))
    lo_f = float(lo)
    hi_f = float(hi)
    return sub[factor].astype(float).ge(lo_f) & sub[factor].astype(float).le(hi_f)


def main() -> None:
    df = load_logs()
    mixed = []
    one_rows: list[dict] = []
    two_rows: list[dict] = []

    grouped = df.groupby(GROUP_KEYS, dropna=False, sort=False)
    for group, sub in grouped:
        n = len(sub)
        wins = int(sub["is_win"].sum())
        losses = n - wins
        if n < MIN_CELL_N or wins < MIN_CELL_WINS or losses < MIN_CELL_LOSSES:
            continue
        wr = wins / n
        if wr <= 0.02 or wr >= 0.80:
            continue
        mixed.append({
            **{k: v for k, v in zip(GROUP_KEYS, group)},
            "technical_regime_desc": str(sub["technical_regime_desc"].iloc[0]),
            "parent_n": n,
            "parent_wins": wins,
            "parent_losses": losses,
            "parent_wr": wr,
        })
        islands = mine_one_factor(sub, group)
        if islands:
            one_rows.extend(islands)
            two_rows.extend(refine_two_factor(sub, pd.DataFrame(islands)))

    mixed_df = pd.DataFrame(mixed)
    one_df = pd.DataFrame(one_rows)
    two_df = pd.DataFrame(two_rows)
    all_df = pd.concat([one_df, two_df], ignore_index=True) if not one_df.empty or not two_df.empty else pd.DataFrame()
    if not all_df.empty:
        all_df = all_df.sort_values(
            ["island_losses", "island_wr", "island_wins", "hold_wr"],
            ascending=[True, False, False, False],
        )

    mixed_df.to_csv(OUT / "winner_island_mixed_parent_cells.csv", index=False)
    one_df.to_csv(OUT / "winner_island_one_factor.csv", index=False)
    two_df.to_csv(OUT / "winner_island_two_factor_refined.csv", index=False)
    all_df.to_csv(OUT / "winner_island_candidates.csv", index=False)

    lines = []
    lines.append("# Winner Island Miner\n")
    lines.append("Mines high-purity winner pockets inside mixed `strategy x pair x direction x 53-regime` parent cells. A broad parent can lose; a valid island only needs to isolate a useful subset of winners without dragging many losers.\n")
    lines.append("## Coverage\n")
    lines.append(f"- Parent mixed cells tested: {len(mixed_df):,}\n")
    lines.append(f"- One-factor islands: {len(one_df):,}\n")
    lines.append(f"- Two-factor refined islands: {len(two_df):,}\n")
    lines.append(f"- Total candidate islands: {len(all_df):,}\n")
    if not all_df.empty:
        pure = all_df[(all_df["island_wins"] >= MIN_ISLAND_WINS) & (all_df["island_losses"] == 0)]
        near = all_df[(all_df["island_wins"] >= MIN_ISLAND_WINS) & (all_df["island_wr"] >= MIN_ISLAND_WR)]
        hold = all_df[(all_df["hold_n"] >= 5) & (all_df["hold_losses"] == 0) & (all_df["hold_wins"] >= 3)]
        lines.append(f"- Pure islands (>= {MIN_ISLAND_WINS} wins, 0 losses): {len(pure):,}\n")
        lines.append(f"- Near-pure islands (WR >= {MIN_ISLAND_WR:.0%}): {len(near):,}\n")
        lines.append(f"- Holdout-clean islands (hold wins >=3, hold losses 0): {len(hold):,}\n")
        show_cols = [
            "strategy_id", "pair", "direction", "technical_regime_53",
            "technical_regime_desc", "parent_n", "parent_wr",
            "rule_depth", "factor_1", "lo_1", "hi_1", "factor_2", "lo_2", "hi_2",
            "island_n", "island_wins", "island_losses", "island_wr",
            "disc_wins", "disc_losses", "hold_wins", "hold_losses", "hold_wr",
            "mean_R",
        ]
        lines.append("\n## Top Pure / Near-Pure Islands\n")
        lines.append(all_df[show_cols].head(60).to_markdown(index=False))
        lines.append("\n## Most Common First Factors\n")
        lines.append(all_df["factor_1"].value_counts().to_frame("islands").to_markdown())
    lines.append("\n## Interpretation\n")
    lines.append("- These are micro-strategy seeds, not deployable rules yet.\n")
    lines.append("- A seed is valuable if it captures a small winner island that the broad regime could not separate.\n")
    lines.append("- The next step is to replay top islands bar-by-bar and see whether their entry trigger + factor band has stable order-of-events performance.\n")
    (OUT / "summary_winner_island_miner.md").write_text("\n".join(lines))

    print(OUT / "summary_winner_island_miner.md")
    print(f"mixed={len(mixed_df)} one={len(one_df)} two={len(two_df)} all={len(all_df)}")


if __name__ == "__main__":
    main()
