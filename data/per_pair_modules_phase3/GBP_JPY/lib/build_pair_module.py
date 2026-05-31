#!/usr/bin/env python3
"""build_pair_module.py — self-contained per-pair research module builder.

Usage:
    python3 build_pair_module.py PAIR [PAIR ...]
    python3 build_pair_module.py --all

For each pair:
  1. Filter trades_PAIR_*.csv from the spec_sweep
  2. Compute 14-bucket v3 serial per trade + W/L suffix
  3. Cluster into 20 regimes using the 7 regime factors (KMeans, seed=42)
  4. Tag regime_id, regime_session, regime_session_wl per trade
  5. Build per-regime manuals (refined WIN + LOSE rules + cross-cut)
  6. Emit master_rules.csv, regime_summary.csv, cross_regime_factors.csv

Resulting folder is fully self-contained:
    research/per_pair/<PAIR>/
        lib/factor_buckets.py        # local copy, no external imports needed
        lib/build_pair_module.py     # this script
        README.md
        trade_serials.csv
        regime_centroids.csv
        regime_session_grid.csv
        regime_session_wl_grid.csv
        manuals/R00_Manual.md ... R19_Manual.md
        manuals/master_rules.csv
        manuals/regime_summary.csv
        manuals/cross_regime_factors.csv
"""
from __future__ import annotations
import argparse
import shutil
import sys
import time
from itertools import combinations
from collections import Counter
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
RESEARCH_ROOT = Path("/Volumes/Alien Device/mr-scrooge-v3/research")
SWEEP_DIR = RESEARCH_ROOT / "replay_lab/results/spec_sweep_phase3_RICH_MERGED_20260531T145650Z"
PER_PAIR_ROOT = RESEARCH_ROOT / "per_pair_phase3"
FACTOR_BUCKETS_SRC = RESEARCH_ROOT / "factor_matrix" / "factor_buckets.py"

# ---------------------------------------------------------------------------
# Make factor_buckets importable locally
# ---------------------------------------------------------------------------
sys.path.insert(0, str(FACTOR_BUCKETS_SRC.parent))
from factor_buckets import FACTORS  # type: ignore

REGIME_FACTORS = ["BB", "A5", "A1", "E20", "E50", "ADR", "SPR"]
ALIGN_FACTORS = ["H20", "H60", "T1", "T4"]
POSITION_FACTORS = ["BBP", "RSI", "ZS"]
FREE_AXES = ["H20","H60","T1","T4","BBP","RSI","ZS","strategy_id","direction_exec","session_bucket"]

N_REGIMES = 20
MIN_RULE_N = 30
WIN_WR = 0.85
LOSE_WR = 0.40
SOFT_WIN_WR = 0.75
SOFT_WIN_N = 50
MIN_BUCKET_N_FOR_DRILL = 2

# ---------------------------------------------------------------------------
# Plain-English bucket decoder
# ---------------------------------------------------------------------------
DECODE = {
    "BB0":"very narrow bands","BB1":"narrow bands","BB2":"normal bands","BB3":"wide bands",
    "BBP0":"deep below lower band","BBP1":"just touched lower band","BBP2":"lower third",
    "BBP3":"middle of band","BBP4":"upper third","BBP5":"just touched upper band","BBP6":"deep above upper band",
    "A5_0":"5m ATR <33% stop","A5_1":"5m ATR 33-80%","A5_2":"5m ATR 80-120%","A5_3":"5m ATR >120%",
    "A1_0":"1h ATR <2x stop","A1_1":"1h ATR 2-4x","A1_2":"1h ATR 4-8x","A1_3":"1h ATR >8x",
    "RSI0":"RSI<20 extreme oversold","RSI1":"RSI 20-30 oversold","RSI2":"RSI 30-40 weak",
    "RSI3":"RSI 40-50 lower neutral","RSI4":"RSI 50-60 upper neutral","RSI5":"RSI 60-70 strong",
    "RSI6":"RSI 70-80 overbought","RSI7":"RSI>80 extreme overbought",
    "E20a":"EMA20 up >0.5x","E20b":"EMA20 up 0.15-0.5x","E20c":"EMA20 flat","E20d":"EMA20 down 0.15-0.5x","E20e":"EMA20 down >0.5x",
    "E50a":"EMA50 up >0.5x","E50b":"EMA50 up 0.15-0.5x","E50c":"EMA50 flat","E50d":"EMA50 down 0.15-0.5x","E50e":"EMA50 down >0.5x",
    "ZS0":"zscore <-3 extreme","ZS1":"zscore -3 to -2 deep oversold","ZS2":"zscore -2 to -1 oversold",
    "ZS3":"zscore -1 to +1 neutral","ZS4":"zscore +1 to +2 overbought","ZS5":"zscore +2 to +3 deep overbought","ZS6":"zscore >+3 extreme",
    "SPR0":"tightest spread","SPR1":"normal spread","SPR2":"moderate spread","SPR3":"wide spread",
    "ADR0":"ADR <30%","ADR1":"30-60%","ADR2":"30-60%","ADR3":"60-90%","ADR4":"90-110%","ADR5":">110% overshoot",
    "H20a":"HTF20 aligned WITH trade","H20b":"HTF20 slightly aligned","H20c":"HTF20 neutral",
    "H20d":"HTF20 mildly against","H20e":"HTF20 strongly against",
    "H60a":"HTF60 aligned WITH trade","H60b":"HTF60 slightly aligned","H60c":"HTF60 neutral",
    "H60d":"HTF60 mildly against","H60e":"HTF60 strongly against",
    "T1a":"1h trend WITH trade","T1b":"1h trend flat","T1c":"1h trend AGAINST trade",
    "T4a":"4h trend WITH trade","T4b":"4h trend flat","T4c":"4h trend AGAINST trade",
}
def english(b): return DECODE.get(b, b)


# ---------------------------------------------------------------------------
# Stage 1 — load + bucket
# ---------------------------------------------------------------------------
def load_pair_trades(pair: str) -> pd.DataFrame:
    files = sorted(SWEEP_DIR.glob(f"trades_{pair}_*.csv"))
    if not files:
        return pd.DataFrame()
    frames = []
    for fp in files:
        try:
            frames.append(pd.read_csv(fp))
        except Exception:
            pass
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True)
    if "session_bucket" not in df.columns:
        df["session_bucket"] = "NA"
    df["session_bucket"] = df["session_bucket"].fillna("NA").astype(str)
    if "win" in df.columns:
        df["win"] = df["win"].astype(bool)
    return df


def bucket_row(row_dict, direction, pip_size):
    ctx = {"stop_pips": 7.0, "pip_size": pip_size, "rv_baseline": 0.002, "direction": direction}
    out = {}
    for f in FACTORS:
        try:
            out[f.code] = f.bucket_for(row_dict, ctx)
        except Exception:
            out[f.code] = f"{f.code}x"
    return out


def stamp_serials_and_buckets(df: pd.DataFrame, pair: str) -> pd.DataFrame:
    pip = 0.01 if any(j in pair for j in ("JPY", "MXN")) else 0.0001
    records = df.to_dict("records")
    bucket_cols = {f.code: [] for f in FACTORS}
    serials = []
    for r in records:
        direction = str(r.get("direction_exec") or "").lower()
        b = bucket_row(r, direction, pip)
        for f in FACTORS:
            bucket_cols[f.code].append(b[f.code])
        serial = (
            f"{pair}|{r.get('strategy_id','')}|{direction}|"
            f"{r.get('session_bucket','')}|" + "|".join(b[f.code] for f in FACTORS)
        )
        serials.append(serial)
    n = len(df)
    wins_arr = df["win"].astype(bool).values
    serials_wl = [s + ("|W" if w else "|L") for s, w in zip(serials, wins_arr)]
    out = pd.DataFrame({
        "trade_id": range(1, n + 1),
        "strategy_id": df["strategy_id"].values,
        "direction_exec": df["direction_exec"].values,
        "session_bucket": df["session_bucket"].values,
        "entry_time": df.get("entry_time", pd.Series([""]*n)).values,
        "exit_time": df.get("exit_time", pd.Series([""]*n)).values,
        "pnl_pips": df.get("pnl_pips", pd.Series([0.0]*n)).values,
        "win": wins_arr,
        "mfe_pips": df.get("mfe_pips", pd.Series([0.0]*n)).values,
        "mae_pips": df.get("mae_pips", pd.Series([0.0]*n)).values,
        "duration": df.get("duration", pd.Series([0]*n)).values,
        "serial_14": serials_wl,
    })
    for f in FACTORS:
        out[f.code] = bucket_cols[f.code]
    return out


# ---------------------------------------------------------------------------
# Stage 2 — cluster into 20 regimes
# ---------------------------------------------------------------------------
def cluster_regimes(df: pd.DataFrame) -> pd.DataFrame:
    mask = pd.Series(True, index=df.index)
    for f in REGIME_FACTORS:
        mask &= df[f].notna() & ~df[f].str.endswith("x", na=False)
    clean = df[mask].copy()
    if len(clean) < N_REGIMES * 2:
        df["regime_id"] = "Rxx"
        return df
    X = pd.get_dummies(clean[REGIME_FACTORS], prefix=REGIME_FACTORS).astype(float)
    if X.shape[1] < 2:
        df["regime_id"] = "R00"
        return df
    km = KMeans(n_clusters=N_REGIMES, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    clean["regime_id"] = [f"R{l:02d}" for l in labels]
    df["regime_id"] = "Rxx"
    df.loc[clean.index, "regime_id"] = clean["regime_id"].values
    return df


def stamp_regime_session_wl(df: pd.DataFrame) -> pd.DataFrame:
    df["regime_session"] = df["regime_id"] + "|" + df["session_bucket"].astype(str)
    df["wl"] = df["win"].map({True: "W", False: "L"})
    df["regime_session_wl"] = df["regime_session"] + "|" + df["wl"]
    return df


def regime_centroids(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for r in sorted(df["regime_id"].unique()):
        sub = df[df["regime_id"] == r]
        modes = {f: (sub[f].mode().iloc[0] if not sub[f].mode().empty else "-") for f in REGIME_FACTORS}
        rows.append({"regime": r, "n_trades": len(sub),
                     "pct_of_total": len(sub) / len(df),
                     **modes,
                     "wr": float(sub["win"].mean()) if not sub.empty else 0.0,
                     "sum_pips": float(sub["pnl_pips"].sum())})
    return pd.DataFrame(rows).sort_values("n_trades", ascending=False)


def regime_session_grids(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    grid = (df.groupby(["regime_id", "session_bucket"])
              .agg(n=("win","count"), wins=("win","sum"),
                   sum_pips=("pnl_pips","sum"), exp_pips=("pnl_pips","mean"))
              .reset_index())
    grid["wr"] = grid["wins"] / grid["n"]

    wl_grid = (df.groupby(["regime_id","session_bucket","wl"])
                 .agg(n=("win","count"), sum_pips=("pnl_pips","sum"),
                      exp_pips=("pnl_pips","mean"),
                      mfe=("mfe_pips","mean"), mae=("mae_pips","mean"))
                 .reset_index())
    return grid, wl_grid


# ---------------------------------------------------------------------------
# Stage 3 — per-regime rule mining + refinement
# ---------------------------------------------------------------------------
def mine_rules(cell, k_list=(3, 4)):
    rules = []
    for k in k_list:
        for axes in combinations(FREE_AXES, k):
            grp = cell.groupby(list(axes))["win"].agg(["count","sum"]).reset_index()
            grp.columns = list(axes) + ["n","wins"]
            grp["wr"] = grp["wins"] / grp["n"]
            for _, r in grp[(grp["n"] >= MIN_RULE_N) & (grp["wr"] >= WIN_WR)].iterrows():
                rules.append({"k": k, "type":"WIN", "rule": {ax: r[ax] for ax in axes},
                              "n": int(r["n"]), "wins": int(r["wins"]),
                              "losses": int(r["n"]-r["wins"]), "wr": float(r["wr"])})
            for _, r in grp[(grp["n"] >= MIN_RULE_N) & (grp["wr"] <= LOSE_WR)].iterrows():
                rules.append({"k": k, "type":"LOSE", "rule": {ax: r[ax] for ax in axes},
                              "n": int(r["n"]), "wins": int(r["wins"]),
                              "losses": int(r["n"]-r["wins"]), "wr": float(r["wr"])})
    return rules


def soft_win_rules(cell, k_list=(3, 4)):
    rules = []
    for k in k_list:
        for axes in combinations(FREE_AXES, k):
            grp = cell.groupby(list(axes))["win"].agg(["count","sum"]).reset_index()
            grp.columns = list(axes) + ["n","wins"]
            grp["wr"] = grp["wins"] / grp["n"]
            for _, r in grp[(grp["n"] >= SOFT_WIN_N) & (grp["wr"] >= SOFT_WIN_WR)].iterrows():
                rules.append({"k": k, "type":"SOFT_WIN", "rule": {ax: r[ax] for ax in axes},
                              "n": int(r["n"]), "wins": int(r["wins"]),
                              "losses": int(r["n"]-r["wins"]), "wr": float(r["wr"])})
    return rules


def find_discriminator(sub, target_class):
    if target_class == "loser":
        target = sub[~sub["win"]]; other = sub[sub["win"]]
    else:
        target = sub[sub["win"]]; other = sub[~sub["win"]]
    if len(target) == 0: return None
    best = None
    for ax in FREE_AXES:
        if ax not in sub.columns: continue
        for b in target[ax].dropna().unique():
            tc = int((target[ax] == b).sum())
            oc = int((other[ax] == b).sum())
            tp = tc / max(len(target), 1)
            op = oc / max(len(other), 1)
            tilt = tp - op
            if tc >= MIN_BUCKET_N_FOR_DRILL and tilt >= 0.15:
                key = (tilt, tc)
                if best is None or key > best[0]:
                    best = (key, ax, b, tilt, tc, len(target))
    if best is None: return None
    _, ax, b, tilt, tc, tt = best
    return ax, b, tilt, tc, tt


def subset_of_rule(cell, rule_dict):
    mask = pd.Series(True, index=cell.index)
    for k, v in rule_dict.items():
        mask &= (cell[k] == v)
    return cell[mask]


def rule_text(rule_dict):
    return " AND ".join(f"{k}={v}" for k, v in rule_dict.items())


def plain_english_rule(rule_dict, refinement=None, op=None):
    direction = rule_dict.get("direction_exec", "?")
    pieces = []
    for k, v in rule_dict.items():
        if k == "direction_exec": continue
        if k == "strategy_id": pieces.append(f"strategy={v}")
        elif k == "session_bucket": pieces.append(f"session={v}")
        else: pieces.append(english(v))
    txt = "; ".join(pieces)
    line = f"**Dir: {direction.upper()}**  •  {txt}"
    if refinement:
        ax, b = refinement
        op_word = "AVOID when" if op == "exclude" else "ONLY when"
        if ax == "session_bucket": disp = f"session={b}"
        elif ax == "strategy_id": disp = f"strategy={b}"
        else: disp = english(b)
        line += f"  •  {op_word} {disp}"
    return line


# ---------------------------------------------------------------------------
# Stage 4 — emit per-regime manuals + master CSVs
# ---------------------------------------------------------------------------
def build_regime_manual(pair, regime, cell, master_rules_out, cross_w, cross_l, manuals_dir):
    n_cell = len(cell)
    n_w = int(cell["win"].sum())
    n_l = int((~cell["win"]).sum())
    wr_cell = cell["win"].mean()
    centroid = {f: cell[f].mode().iloc[0] if not cell[f].mode().empty else "-" for f in REGIME_FACTORS}

    out = []
    out.append(f"# {pair} — {regime} Manual\n")
    out.append(f"## Regime centroid (locked factors)\n")
    for f, v in centroid.items():
        out.append(f"- **{f} = {v}**  ({english(v)})")
    out.append("")
    out.append(f"## Baseline\n- Trades: **{n_cell:,}**  (W={n_w:,} / L={n_l:,})  -  WR: **{wr_cell:.1%}**\n")

    sess_counts = cell["session_bucket"].value_counts()
    out.append("## Session distribution\n")
    for s, c in sess_counts.items():
        sw = cell[(cell["session_bucket"] == s) & cell["win"]].shape[0]
        swr = sw / c if c else 0.0
        out.append(f"- {s}: n={c}  W={sw}/L={c-sw}  WR={swr:.1%}")
    out.append("")

    extreme = mine_rules(cell)
    wins = sorted([r for r in extreme if r["type"]=="WIN"], key=lambda r: (-r["n"], -r["wr"]))[:25]
    loses = sorted([r for r in extreme if r["type"]=="LOSE"], key=lambda r: (-r["n"], r["wr"]))[:25]
    softs = sorted(soft_win_rules(cell), key=lambda r: (-r["n"], -r["wr"]))[:15]

    out.append(f"## WIN rules (n>={MIN_RULE_N}, WR>={WIN_WR*100:.0f}%) — refined\n")
    if not wins: out.append("_None at this threshold._\n")
    for i, r in enumerate(wins, 1):
        rule = r["rule"]
        sub = subset_of_rule(cell, rule)
        disc = find_discriminator(sub, "loser")
        if disc:
            ax, b, tilt, tc, tt = disc
            refined = sub[sub[ax] != b]
            r_n = len(refined); r_w = int(refined["win"].sum())
            r_wr = r_w/r_n if r_n else 0.0
            note = f"exclude {ax}={b} drops {tc}/{tt} losers ({tc/tt:.0%})"
            plain = plain_english_rule(rule, (ax, b), "exclude")
        else:
            refined = sub; r_n, r_w, r_wr = r["n"], r["wins"], r["wr"]
            note = "no further refinement"; plain = plain_english_rule(rule)
        out.append(f"### W{i:02d}.  `{rule_text(rule)}`")
        out.append(f"- Raw: n={r['n']}  W={r['wins']}/L={r['losses']}  WR={r['wr']:.1%}")
        out.append(f"- Refine: {note}")
        out.append(f"- **Final: n={r_n}  W={r_w}/L={r_n-r_w}  WR={r_wr:.1%}**")
        out.append(f"- {plain}\n")
        master_rules_out.append({
            "pair": pair, "regime": regime, "rule_type":"WIN",
            "raw_rule": rule_text(rule),
            "raw_n": r["n"], "raw_w": r["wins"], "raw_l": r["losses"], "raw_wr": r["wr"],
            "refine_axis": disc[0] if disc else "",
            "refine_bucket": disc[1] if disc else "",
            "refine_op": "exclude" if disc else "",
            "refined_n": r_n, "refined_w": r_w, "refined_l": r_n - r_w,
            "refined_wr": r_wr, "plain_english": plain,
        })
        for ax in FREE_AXES:
            if ax in refined.columns:
                for v in refined[ax].dropna():
                    cross_w[ax][v] += 1

    if softs and len(wins) < 5:
        out.append(f"## Softer WIN rules (n>={SOFT_WIN_N}, WR>={SOFT_WIN_WR*100:.0f}%)\n")
        for r in softs:
            out.append(f"- n={r['n']}  W={r['wins']}/L={r['losses']}  WR={r['wr']:.1%}  IF `{rule_text(r['rule'])}`")
        out.append("")

    out.append(f"## LOSE rules (AVOID — n>={MIN_RULE_N}, WR<={LOSE_WR*100:.0f}%) — sharpened\n")
    if not loses: out.append("_None at this threshold._\n")
    for i, r in enumerate(loses, 1):
        rule = r["rule"]
        sub = subset_of_rule(cell, rule)
        disc = find_discriminator(sub, "loser")
        if disc:
            ax, b, tilt, tc, tt = disc
            refined = sub[sub[ax] == b]
            r_n = len(refined); r_w = int(refined["win"].sum())
            r_wr = r_w/r_n if r_n else 0.0
            note = f"sharpest is {ax}={b} ({tc}/{tt} of losers there)"
            plain = plain_english_rule(rule, (ax, b), "include")
        else:
            refined = sub; r_n, r_w, r_wr = r["n"], r["wins"], r["wr"]
            note = "no sharper sub-pattern"; plain = plain_english_rule(rule)
        out.append(f"### L{i:02d}.  `{rule_text(rule)}`")
        out.append(f"- Raw: n={r['n']}  W={r['wins']}/L={r['losses']}  WR={r['wr']:.1%}")
        out.append(f"- Sharpen: {note}")
        out.append(f"- **Sharp: n={r_n}  W={r_w}/L={r_n-r_w}  WR={r_wr:.1%}**")
        out.append(f"- {plain}\n")
        master_rules_out.append({
            "pair": pair, "regime": regime, "rule_type":"LOSE",
            "raw_rule": rule_text(rule),
            "raw_n": r["n"], "raw_w": r["wins"], "raw_l": r["losses"], "raw_wr": r["wr"],
            "refine_axis": disc[0] if disc else "",
            "refine_bucket": disc[1] if disc else "",
            "refine_op": "include" if disc else "",
            "refined_n": r_n, "refined_w": r_w, "refined_l": r_n - r_w,
            "refined_wr": r_wr, "plain_english": plain,
        })
        for ax in FREE_AXES:
            if ax in refined.columns:
                for v in refined[ax].dropna():
                    cross_l[ax][v] += 1

    # Per-regime cross-cut
    out.append("## Cross-cutting factor analysis (this regime)\n")
    out.append("| factor | winner-dominant | loser-dominant |")
    out.append("|---|---|---|")
    w_sub = cell[cell["win"]]; l_sub = cell[~cell["win"]]
    if not w_sub.empty and not l_sub.empty:
        for ax in ["H20","H60","T1","T4","BBP","RSI","ZS","strategy_id","direction_exec","session_bucket"]:
            if ax not in cell.columns: continue
            w_c = Counter(w_sub[ax].dropna()); l_c = Counter(l_sub[ax].dropna())
            w_t = sum(w_c.values()); l_t = sum(l_c.values())
            if w_t == 0 or l_t == 0: continue
            w_dom, l_dom = [], []
            for b in set(w_c) | set(l_c):
                wp = w_c.get(b,0)/w_t; lp = l_c.get(b,0)/l_t
                if wp - lp > 0.05: w_dom.append((b, wp, lp))
                elif lp - wp > 0.05: l_dom.append((b, wp, lp))
            w_dom.sort(key=lambda x: -(x[1]-x[2])); l_dom.sort(key=lambda x: -(x[2]-x[1]))
            ws = ", ".join(f"{b}({wp*100:.0f}/{lp*100:.0f})" for b,wp,lp in w_dom[:3]) or "—"
            ls = ", ".join(f"{b}({wp*100:.0f}/{lp*100:.0f})" for b,wp,lp in l_dom[:3]) or "—"
            out.append(f"| {ax} | {ws} | {ls} |")
    out.append("\n*Read: `bucket(winner%/loser%)`.*\n")

    (manuals_dir / f"{regime}_Manual.md").write_text("\n".join(out))
    return len(wins), len(loses), len(softs)


# ---------------------------------------------------------------------------
# Top-level driver per pair
# ---------------------------------------------------------------------------
def build_pair(pair: str, log_prefix: str = ""):
    pair_dir = PER_PAIR_ROOT / pair
    lib_dir = pair_dir / "lib"
    manuals_dir = pair_dir / "manuals"
    pair_dir.mkdir(parents=True, exist_ok=True)
    lib_dir.mkdir(parents=True, exist_ok=True)
    manuals_dir.mkdir(parents=True, exist_ok=True)

    # Copy factor_buckets.py + this script INTO the pair folder (self-contained)
    shutil.copy2(FACTOR_BUCKETS_SRC, lib_dir / "factor_buckets.py")
    shutil.copy2(Path(__file__), lib_dir / "build_pair_module.py")

    df = load_pair_trades(pair)
    if df.empty:
        print(f"{log_prefix}{pair}: no trades, skipping")
        return None

    t0 = time.time()
    df = stamp_serials_and_buckets(df, pair)
    df = cluster_regimes(df)
    df = stamp_regime_session_wl(df)

    df.to_csv(pair_dir / "trade_serials.csv", index=False)
    regime_centroids(df).to_csv(pair_dir / "regime_centroids.csv", index=False)
    rs_grid, rs_wl_grid = regime_session_grids(df)
    rs_grid.to_csv(pair_dir / "regime_session_grid.csv", index=False)
    rs_wl_grid.to_csv(pair_dir / "regime_session_wl_grid.csv", index=False)

    master_rules = []
    cross_w = {ax: Counter() for ax in FREE_AXES}
    cross_l = {ax: Counter() for ax in FREE_AXES}
    regimes = sorted(r for r in df["regime_id"].unique() if r != "Rxx")
    summary_rows = []
    for r in regimes:
        cell = df[df["regime_id"] == r]
        nw, nl, ns = build_regime_manual(pair, r, cell, master_rules, cross_w, cross_l, manuals_dir)
        summary_rows.append({
            "regime": r, "n_trades": len(cell),
            "n_winners": int(cell["win"].sum()),
            "n_losers": int((~cell["win"]).sum()),
            "wr": float(cell["win"].mean()),
            "n_win_rules": nw, "n_lose_rules": nl, "n_soft_win_rules": ns,
        })

    pd.DataFrame(master_rules).to_csv(manuals_dir / "master_rules.csv", index=False)
    pd.DataFrame(summary_rows).to_csv(manuals_dir / "regime_summary.csv", index=False)

    cross_rows = []
    for ax in FREE_AXES:
        wt = sum(cross_w[ax].values()); lt = sum(cross_l[ax].values())
        if wt == 0 or lt == 0: continue
        for b in set(cross_w[ax]) | set(cross_l[ax]):
            wp = cross_w[ax].get(b,0)/wt; lp = cross_l[ax].get(b,0)/lt
            cross_rows.append({"factor": ax, "bucket": b, "winner_share": wp,
                               "loser_share": lp, "tilt": wp - lp,
                               "winner_count": cross_w[ax].get(b,0),
                               "loser_count": cross_l[ax].get(b,0)})
    pd.DataFrame(cross_rows).sort_values("tilt", ascending=False).to_csv(
        manuals_dir / "cross_regime_factors.csv", index=False)

    readme = pair_dir / "README.md"
    readme.write_text(f"""# {pair} Trading Module

Self-contained per-pair research module built from 6 months of lab trades.

## Layout
- `trade_serials.csv` — every lab trade with its 14-bucket serial + regime + session + W/L
- `regime_centroids.csv` — the 20 KMeans regimes (defined by 7 regime factors)
- `regime_session_grid.csv` — performance per (regime, session) cell
- `regime_session_wl_grid.csv` — W/L breakdown per cell
- `manuals/R??_Manual.md` — readable per-regime manual with refined WIN + LOSE rules
- `manuals/master_rules.csv` — every refined rule, indexed by regime
- `manuals/regime_summary.csv` — headline stats per regime
- `manuals/cross_regime_factors.csv` — bucket prevalence W vs L

## Self-contained
- `lib/factor_buckets.py` — local copy, no external imports
- `lib/build_pair_module.py` — the builder script (this folder is reproducible)

To rebuild from source:
    python3 lib/build_pair_module.py {pair}

Built: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}
Trades: {len(df):,}  WR: {df['win'].mean():.1%}  Regimes: {len(regimes)}
Rules: {len(master_rules):,} refined
""")

    elapsed = time.time() - t0
    n_total = len(df); n_w = int(df["win"].sum())
    print(f"{log_prefix}{pair}: n={n_total:5d}  W={n_w:5d}  WR={df['win'].mean():.1%}  "
          f"regimes={len(regimes):2d}  rules={len(master_rules):4d}  ({elapsed:.1f}s)")
    return {"pair": pair, "n": n_total, "wr": df["win"].mean(),
            "regimes": len(regimes), "rules": len(master_rules)}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def all_pairs() -> list[str]:
    pairs = set()
    for fp in SWEEP_DIR.glob("trades_*.csv"):
        # filename format: trades_PAIR_STRATEGY_DIRECTION.csv
        parts = fp.stem.split("_")
        if len(parts) >= 3 and parts[0] == "trades":
            pair = f"{parts[1]}_{parts[2]}"
            pairs.add(pair)
    return sorted(pairs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pairs", nargs="*", help="pair codes e.g. EUR_USD GBP_USD")
    parser.add_argument("--all", action="store_true", help="process every pair found in sweep")
    args = parser.parse_args()

    if args.all:
        pairs = all_pairs()
    elif args.pairs:
        pairs = args.pairs
    else:
        parser.print_help()
        return

    print(f"Building modules for {len(pairs)} pair(s): {pairs}")
    print()
    t0 = time.time()
    results = []
    for i, p in enumerate(pairs, 1):
        prefix = f"[{i:2d}/{len(pairs)}] "
        try:
            r = build_pair(p, prefix)
            if r: results.append(r)
        except Exception as e:
            print(f"{prefix}{p}: FAILED — {type(e).__name__}: {e}")
    elapsed = time.time() - t0
    print()
    print(f"DONE — {len(results)}/{len(pairs)} pairs in {elapsed:.1f}s")
    print()
    print("=== Per-pair headline ===")
    for r in results:
        print(f"  {r['pair']:<8s}  n={r['n']:5d}  WR={r['wr']:.1%}  "
              f"regimes={r['regimes']:2d}  rules={r['rules']:4d}")


if __name__ == "__main__":
    main()
