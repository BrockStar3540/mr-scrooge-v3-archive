"""Yield report on the batch expansion -- Brock 2026-05-18 spec.

Sections:
  1. Yield by queue type (session_sibling / boundary_thin / live_gap)
  2. Direct-family breakdown
  3. Ranked top-25 candidate table
  4. Coverage impact (what strict+near would add over v9)
  5. Session-sibling focus
  6. Boundary-thin focus
  7. Decision recommendation
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import pandas as pd
import numpy as np


def fmt_pct(n: int, d: int) -> str:
    if d == 0:
        return "—"
    return f"{100*n/d:.1f}%"


def load_results(out_dir: Path) -> pd.DataFrame:
    """Combine the per-queue 'all' files into one DataFrame with queue column."""
    frames = []
    for q in ("live_gap", "boundary_thin", "session_sibling"):
        p = out_dir / f"expansion_all_{q}.csv"
        if p.exists() and p.stat().st_size > 0:
            try:
                df = pd.read_csv(p)
                if "queue" not in df.columns:
                    df["queue"] = q
                frames.append(df)
            except pd.errors.EmptyDataError:
                pass
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def section_1_yield_by_queue(results: pd.DataFrame) -> str:
    """Yield table by queue type."""
    lines = ["## 1. Yield by queue type", ""]
    if results.empty:
        lines.append("_No results._")
        return "\n".join(lines)
    rows = []
    for q in ("session_sibling", "boundary_thin", "live_gap"):
        g = results[results.queue == q]
        total = len(g)
        strict = int((g.outcome_tier == "strict_winner").sum())
        near = int((g.outcome_tier == "near_miss_candidate").sum())
        dead = int((g.outcome_tier == "dead").sum())
        productive = g[g.outcome_tier.isin(["strict_winner", "near_miss_candidate"])]
        avg_n = float(productive["n_unique"].mean()) if len(productive) else 0.0
        avg_wr = float(productive["wr_unique"].mean()) if len(productive) else 0.0
        avg_lb = float(productive["wilson_lb"].mean()) if len(productive) else 0.0
        hit_rate = (strict + near) / total if total else 0.0
        rows.append({
            "queue": q,
            "targets": total,
            "strict": strict,
            "near_miss": near,
            "dead": dead,
            "hit_rate": hit_rate,
            "avg_n_unique": avg_n,
            "avg_wr": avg_wr,
            "avg_wilson_lb": avg_lb,
        })
    lines.append("| queue | targets | strict | near_miss | dead | hit_rate | avg_n | avg_wr | avg_lb |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in rows:
        lines.append(
            f"| {r['queue']} | {r['targets']} | {r['strict']} | {r['near_miss']} | "
            f"{r['dead']} | {r['hit_rate']:.1%} | {r['avg_n_unique']:.1f} | "
            f"{r['avg_wr']:.3f} | {r['avg_wilson_lb']:.3f} |"
        )
    # winning queue
    productive_by_queue = {r["queue"]: r["strict"] + r["near_miss"] for r in rows}
    best = max(productive_by_queue, key=productive_by_queue.get)
    lines.append("")
    lines.append(f"**Most productive queue (by strict+near count)**: `{best}` "
                 f"({productive_by_queue[best]} productive cells)")
    return "\n".join(lines)


def section_2_direct_family(results: pd.DataFrame) -> str:
    lines = ["", "## 2. Direct-family breakdown", ""]
    if results.empty or "family" not in results.columns:
        lines.append("_No data._")
        return "\n".join(lines)
    direct = results[results.family == "direct"]
    if direct.empty:
        lines.append("_No `direct` family results in this batch._")
        return "\n".join(lines)
    strict = direct[direct.outcome_tier == "strict_winner"]
    near = direct[direct.outcome_tier == "near_miss_candidate"]
    dead = direct[direct.outcome_tier == "dead"]
    lines.append(f"- **strict winners**: {len(strict)}")
    lines.append(f"- **near misses**:   {len(near)}")
    lines.append(f"- **dead**:          {len(dead)}")
    productive = pd.concat([strict, near], ignore_index=True)
    if productive.empty:
        lines.append("")
        lines.append("_No productive direct cells in this batch._")
        return "\n".join(lines)
    lines.append("")
    lines.append("### Top pairs (productive only)")
    lines.append("")
    for pair, n in productive["pair"].value_counts().head(10).items():
        lines.append(f"- `{pair}`: {n}")
    lines.append("")
    lines.append("### Top regimes")
    lines.append("")
    for reg, n in productive["regime53"].value_counts().head(10).items():
        lines.append(f"- `{reg}`: {n}")
    lines.append("")
    lines.append("### Top sessions")
    lines.append("")
    for sess, n in productive["session_bucket"].value_counts().head(10).items():
        lines.append(f"- `{sess}`: {n}")
    if "cell_strategy" in productive.columns:
        strats = productive["cell_strategy"].dropna()
        if len(strats):
            lines.append("")
            lines.append("### Top cell strategies")
            lines.append("")
            for s, n in strats.value_counts().head(10).items():
                lines.append(f"- `{s}`: {n}")
    lines.append("")
    lines.append("### Productive direct cells by queue type")
    lines.append("")
    for q, n in productive["queue"].value_counts().items():
        lines.append(f"- `{q}`: {n}")
    return "\n".join(lines)


def section_3_top25(results: pd.DataFrame) -> str:
    lines = ["", "## 3. Ranked top-25 candidates", ""]
    if results.empty:
        lines.append("_No data._")
        return "\n".join(lines)
    productive = results[results.outcome_tier.isin(["strict_winner", "near_miss_candidate"])].copy()
    if productive.empty:
        lines.append("_No productive candidates._")
        return "\n".join(lines)
    # composite score
    productive["score"] = (
        productive["wilson_lb"] * 0.5
        + productive["wr_unique"] * 0.3
        + np.log1p(productive["n_unique"]) * 0.05
        + (productive["outcome_tier"] == "strict_winner").astype(float) * 0.15
    )
    # Optional family bonus: direct is starvation priority
    productive["family_priority"] = productive["family"].map(
        {"direct": 0.05, "reversal": 0.02, "dbb_trend": 0.0}
    ).fillna(0.0)
    productive["score"] += productive["family_priority"]
    productive = productive.sort_values("score", ascending=False).head(25)

    cols = ["regime53", "pair", "family", "cell_strategy", "direction",
            "session_bucket", "queue", "outcome_tier",
            "n_unique", "wr_unique", "wilson_lb", "source_strategy", "child_rule"]
    cols = [c for c in cols if c in productive.columns]

    header = "| rank | " + " | ".join(c for c in cols) + " |"
    sep = "|---|" + "|".join("---" for _ in cols) + "|"
    lines.append(header)
    lines.append(sep)
    for i, (_, r) in enumerate(productive.iterrows(), 1):
        cell_vals = []
        for c in cols:
            v = r.get(c)
            if isinstance(v, float):
                if c in ("wr_unique", "wilson_lb"):
                    cell_vals.append(f"{v:.3f}")
                elif c == "n_unique":
                    cell_vals.append(f"{int(v)}")
                else:
                    cell_vals.append(f"{v:.3f}")
            elif c == "child_rule" and isinstance(v, str):
                cell_vals.append(f"`{v[:60]}{'…' if len(v) > 60 else ''}`")
            else:
                cell_vals.append(str(v) if v is not None else "")
        lines.append("| " + str(i) + " | " + " | ".join(cell_vals) + " |")
    return "\n".join(lines)


def section_4_coverage(results: pd.DataFrame, v9_path: Path) -> str:
    lines = ["", "## 4. Coverage impact (strict + near vs v9_observe)", ""]
    productive = results[results.outcome_tier.isin(["strict_winner", "near_miss_candidate"])]
    if productive.empty:
        lines.append("_No productive candidates._")
        return "\n".join(lines)
    v9 = pd.read_parquet(v9_path)
    v9_seed_plus = v9[v9.tier.isin(["Seed", "Seed-Pro", "Pro", "Elite"])].drop_duplicates(
        subset=["parent_regime", "pair", "session_bucket", "direction", "family"]
    )

    def _coverage(by, label):
        new = productive.groupby(by).size().to_dict()
        existing = v9_seed_plus.groupby(by if by != "regime53" else "parent_regime").size().to_dict()
        rows = sorted(set(new.keys()) | set(existing.keys()))
        out = [f"### By {label}", ""]
        out.append(f"| {label} | v9 cells | new productive | delta |")
        out.append("|---|---:|---:|---:|")
        for k in rows:
            n = new.get(k, 0)
            e = existing.get(k, 0)
            out.append(f"| {k} | {e} | {n} | +{n} |")
        return "\n".join(out)

    lines.append(_coverage("family", "family"))
    lines.append("")
    lines.append(_coverage("pair", "pair"))
    lines.append("")
    lines.append(_coverage("regime53", "regime"))
    lines.append("")
    lines.append(_coverage("direction", "direction"))
    lines.append("")
    lines.append(_coverage("session_bucket", "session"))
    return "\n".join(lines)


def section_5_session_sibling_focus(results: pd.DataFrame) -> str:
    lines = ["", "## 5. Session-sibling focus", ""]
    ss = results[results.queue == "session_sibling"]
    if ss.empty:
        lines.append("_No session_sibling results._")
        return "\n".join(lines)
    strict = int((ss.outcome_tier == "strict_winner").sum())
    near = int((ss.outcome_tier == "near_miss_candidate").sum())
    lines.append(f"- targets: {len(ss)}")
    lines.append(f"- strict winners: {strict}")
    lines.append(f"- near misses: {near}")
    productive = ss[ss.outcome_tier.isin(["strict_winner", "near_miss_candidate"])].copy()
    if productive.empty:
        lines.append("_No productive session siblings._")
        return "\n".join(lines)
    # Parse the parent_session -> candidate_session transitions
    productive["transition"] = (
        productive["parent_rule"].fillna("").map(
            lambda s: (re.search(r"session_bucket==([\w_]+)", s) or [None, None])[1]
            if isinstance(s, str) else None
        ).astype(str)
        + " -> "
        + productive["session_bucket"].astype(str)
    )
    lines.append("")
    lines.append("### Productive transitions")
    lines.append("")
    lines.append("| transition | count | avg_wr | avg_lb |")
    lines.append("|---|---:|---:|---:|")
    for trans, g in productive.groupby("transition"):
        lines.append(f"| {trans} | {len(g)} | {g.wr_unique.mean():.3f} | {g.wilson_lb.mean():.3f} |")
    return "\n".join(lines)


def section_6_boundary_focus(results: pd.DataFrame) -> str:
    lines = ["", "## 6. Boundary-thin focus", ""]
    bt = results[results.queue == "boundary_thin"]
    if bt.empty:
        lines.append("_No boundary_thin results._")
        return "\n".join(lines)
    strict = int((bt.outcome_tier == "strict_winner").sum())
    near = int((bt.outcome_tier == "near_miss_candidate").sum())
    lines.append(f"- targets: {len(bt)}")
    lines.append(f"- strict winners: {strict}")
    lines.append(f"- near misses: {near}")
    productive = bt[bt.outcome_tier.isin(["strict_winner", "near_miss_candidate"])]
    if productive.empty:
        lines.append("_No productive boundary widenings._")
        return "\n".join(lines)
    # Which factor + which widen step produced the wins?
    def _factor_of_rule(rule):
        if not isinstance(rule, str): return None
        m = re.search(r"BB_compress|RSI14|ATR_ratio|ADX14|bb_position|volume_ratio", rule)
        return m.group(0) if m else None
    # The violated feature is what was widened; pull it from parent_rule context
    # Actually we recorded widen_pct on the row.
    lines.append("")
    if "widen_pct" in productive.columns:
        lines.append("### By widen_pct")
        lines.append("")
        lines.append("| widen_pct | count | avg_wr | avg_lb |")
        lines.append("|---|---:|---:|---:|")
        for wp, g in productive.groupby("widen_pct"):
            lines.append(f"| {wp} | {len(g)} | {g.wr_unique.mean():.3f} | {g.wilson_lb.mean():.3f} |")
    # Productive feature counts (from child_rule -- which feature is most-widened)
    productive = productive.copy()
    productive["main_factor"] = productive["child_rule"].map(_factor_of_rule)
    lines.append("")
    lines.append("### By widened factor (parsed from child_rule)")
    lines.append("")
    lines.append("| factor | count | avg_wr | avg_lb |")
    lines.append("|---|---:|---:|---:|")
    for f, g in productive.groupby("main_factor"):
        if f is None: continue
        lines.append(f"| {f} | {len(g)} | {g.wr_unique.mean():.3f} | {g.wilson_lb.mean():.3f} |")
    return "\n".join(lines)


def section_7_recommendation(results: pd.DataFrame) -> str:
    lines = ["", "## 7. Decision recommendation", ""]
    if results.empty:
        lines.append("_No data._")
        return "\n".join(lines)
    # Productive by queue
    productive = results[results.outcome_tier.isin(["strict_winner", "near_miss_candidate"])]
    by_q = productive["queue"].value_counts().to_dict()
    strict_total = int((results.outcome_tier == "strict_winner").sum())
    near_total = int((results.outcome_tier == "near_miss_candidate").sum())

    if by_q:
        scale = max(by_q, key=by_q.get)
        deprio = min(by_q, key=by_q.get) if len(by_q) > 1 else "—"
    else:
        scale = "none — all queues dead"
        deprio = "—"

    lines.append(f"- **Most productive queue → scale next**: `{scale}` ({by_q.get(scale, 0)} productive)")
    lines.append(f"- **Least productive queue → deprioritize**: `{deprio}` ({by_q.get(deprio, 0)} productive)")
    lines.append("")
    direct_strict = int(((results.family == "direct") & (results.outcome_tier == "strict_winner")).sum())
    direct_near = int(((results.family == "direct") & (results.outcome_tier == "near_miss_candidate")).sum())
    lines.append(f"- **Direct-family recovery**: {direct_strict} strict + {direct_near} near = "
                 f"{direct_strict + direct_near} new productive direct cells (v9 had 0 Pro+)")
    lines.append("")
    if strict_total >= 25:
        rec = "Build v10_trade from **strict winners only** — sample size already meaningful."
    elif strict_total + near_total >= 50:
        rec = ("Build v10_trade from **strict + top-N near misses** (e.g. top 25 by Wilson LB). "
               "OOS-validate the near misses before they ever enter HARD execution.")
    else:
        rec = ("Hold deployment. Both strict and near tiers are too thin. Continue the 4h cron "
               "to accumulate live telemetry; re-run batch synth after gen-2 mutation on the "
               "current strict winners.")
    lines.append(f"- **v10 build recommendation**: {rec}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--results-dir", required=True)
    p.add_argument("--v9-observe", required=True)
    p.add_argument("--out-md", required=True)
    args = p.parse_args()

    results = load_results(Path(args.results_dir))
    print(f"Loaded {len(results)} result rows from {args.results_dir}")
    if not results.empty:
        print(f"  by tier: {results.outcome_tier.value_counts().to_dict()}")
        print(f"  by queue: {results.queue.value_counts().to_dict()}")

    md = [
        "# Batch expansion yield report",
        "",
        f"Source: `{args.results_dir}`",
        f"v9_observe baseline: `{args.v9_observe}`",
        "",
    ]
    md.append(section_1_yield_by_queue(results))
    md.append(section_2_direct_family(results))
    md.append(section_3_top25(results))
    md.append(section_4_coverage(results, Path(args.v9_observe)))
    md.append(section_5_session_sibling_focus(results))
    md.append(section_6_boundary_focus(results))
    md.append(section_7_recommendation(results))

    Path(args.out_md).write_text("\n".join(md))
    print(f"\n-> {args.out_md}")


if __name__ == "__main__":
    main()
