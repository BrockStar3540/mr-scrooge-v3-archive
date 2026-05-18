"""Current-time-slice war-room pass -- Brock 2026-05-18.

For the live market state the bot is in RIGHT NOW (e.g. Monday 1:35 PM ET):
identify the best-fit strategy/cell from existing data, and build the
narrowest honest table around it.

Pulls from:
  data/seed-telemetry.jsonl                live ledger
  data/routing_table_v9_observe.parquet    full observation surface
  data/routing_table_v10_fast_current_regime.parquet  current live surface
  research/.../strike-pass-2026-05-18/live_parent_strict_winners.csv
  research/.../probe_seed_family_children_winners.csv  broader probe bank

Outputs (war-room CSVs):
  current_slice_live_state.csv         top live tuples in last N min
  current_slice_ranked_candidates.csv  cells ranked best-fit for slice
  current_slice_fallback_ladder.csv    per pair: exact / sibling / fallback / no-trade
  current_slice_fast_candidates.csv    deployable narrow set
  current_slice_recommendation.md      answer to "what should fire here?"
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd


def session_for_hour(h):
    try: h = int(h)
    except: return None
    if h < 4: return "asia"
    if h < 6: return "asia_late"
    if h < 9: return "london_open"
    if h < 13: return "ny_open"
    if h < 17: return "ny_mid"
    if h < 21: return "ny_close"
    return "off_hours"


def load_ledger(p):
    rows = []
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try: rows.append(json.loads(line))
            except: pass
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--v9-observe", required=True)
    ap.add_argument("--v10-fast", required=True)
    ap.add_argument("--strike-strict", required=True,
                    help="strike-pass-B strict winners (boundary siblings)")
    ap.add_argument("--probe-winners", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--slice-window-min", type=int, default=60,
                    help="Define 'current slice' from last N minutes of ledger")
    ap.add_argument("--top-pairs", type=int, default=15)
    args = ap.parse_args()

    out = Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(minutes=args.slice_window_min)

    # 1. Freeze current slice from live ledger
    df = load_ledger(args.ledger)
    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    recent = df[df.ts >= cutoff]
    live_recent = recent[recent.gate == "entry_filter"]
    shadow_recent = recent[recent.gate == "entry_filter_shadow"]
    if live_recent.empty:
        print("No live ledger rows in current slice; aborting")
        return

    cur_hour = now.hour
    cur_session = session_for_hour(cur_hour)
    cur_regime = live_recent.regime53.value_counts().index[0]
    top_pairs = live_recent.symbol.value_counts().head(args.top_pairs).index.tolist()
    top_families = live_recent.candidate_strategy.value_counts().to_dict()
    top_directions = live_recent.direction.value_counts().to_dict()

    print(f"=== Current slice frozen ({args.slice_window_min}min window) ===")
    print(f"  UTC now: {now.isoformat()}  hour={cur_hour}  session={cur_session}")
    print(f"  dominant regime: {cur_regime} ({(live_recent.regime53==cur_regime).sum()}/{len(live_recent)})")
    print(f"  top pairs: {top_pairs[:10]}")
    print(f"  family mix: {top_families}")
    print(f"  direction mix: {top_directions}")
    print(f"  shadow shave-passes in window: {(shadow_recent.block_reason=='shave_rule_satisfied').sum()}")

    # Build state CSV
    state_rows = []
    for (sym, dirn), g in live_recent.groupby(["symbol","direction"]):
        if sym not in top_pairs: continue
        # Most common block reason for this tuple
        common_reason = g.block_reason.value_counts().head(1)
        state_rows.append({
            "regime53": cur_regime,
            "pair": sym,
            "direction": dirn,
            "session_bucket": cur_session,
            "hour_utc": cur_hour,
            "family": live_recent[live_recent.symbol==sym].candidate_strategy.value_counts().index[0],
            "live_count": len(g),
            "top_block_reason": common_reason.index[0] if len(common_reason) else None,
        })
    state_df = pd.DataFrame(state_rows).sort_values("live_count", ascending=False)
    state_df.to_csv(out / "current_slice_live_state.csv", index=False)

    # 2. Pull historical evidence for the slice
    v9 = pd.read_parquet(args.v9_observe)
    v10 = pd.read_parquet(args.v10_fast)
    strike = pd.read_csv(args.strike_strict)
    probe = pd.read_csv(args.probe_winners)

    def in_slice(regime, pair, session=None):
        return regime == cur_regime and pair in top_pairs

    # v10_fast cells -- already deployed (exact-match)
    v10_cells = v10.drop_duplicates(subset=["parent_regime","pair","strategy","direction","session_bucket"])
    v10_in_slice = v10_cells[
        v10_cells.parent_regime.eq(cur_regime) & v10_cells.pair.isin(top_pairs)
    ].copy()
    v10_in_slice["source"] = "live_validated_parent"
    v10_in_slice["session_match"] = (v10_in_slice.session_bucket == cur_session)

    # v9_observe -- existing routing surface (broader)
    v9_cells = v9.drop_duplicates(subset=["parent_regime","pair","strategy","direction","session_bucket"])
    v9_in_slice = v9_cells[
        v9_cells.parent_regime.eq(cur_regime) & v9_cells.pair.isin(top_pairs)
        & v9_cells.session_bucket.isin([cur_session, cur_session.replace("close","mid")
                                        if "close" in cur_session else cur_session])
    ].copy()
    v9_in_slice["source"] = "v9_observe_seed"
    v9_in_slice["session_match"] = (v9_in_slice.session_bucket == cur_session)

    # Strike-pass-B widened siblings -- per-parent strict winners
    strike_in_slice = strike[
        strike.regime53.eq(cur_regime) & strike.pair.isin(top_pairs)
    ].copy()
    strike_in_slice["source"] = "boundary_sibling"
    if "session_bucket" not in strike_in_slice.columns:
        strike_in_slice["session_bucket"] = cur_session
    strike_in_slice["session_match"] = (strike_in_slice.session_bucket == cur_session)

    # Probe seed-family children (broader siblings)
    probe_in_slice = probe[
        probe.technical_regime_53.eq(cur_regime) & probe.pair.isin(top_pairs)
    ].copy()
    probe_in_slice = probe_in_slice.rename(columns={
        "technical_regime_53":"regime53", "wins":"wins_unique",
        "n":"n_unique", "wr":"wr_unique", "root_strategy_id":"cell_strategy",
        "child_rule":"shave_rule",
    })
    # Apply 2x correction since probe rows are inflated
    probe_in_slice["n_unique"] = (probe_in_slice["n_unique"] // 2).astype(int)
    probe_in_slice["wins_unique"] = (probe_in_slice["wins_unique"] // 2).astype(int)
    probe_in_slice["wr_unique"] = np.where(
        probe_in_slice["n_unique"] > 0,
        probe_in_slice["wins_unique"] / probe_in_slice["n_unique"], 0.0,
    )
    probe_in_slice["source"] = "probe_seed_child"
    probe_in_slice["session_bucket"] = cur_session  # not session-specific in this CSV
    probe_in_slice["session_match"] = True

    # 3. Shadow shave-pass evidence for these cells
    sh_passed = shadow_recent[shadow_recent.block_reason == "shave_rule_satisfied"]
    sh_pass_counts = sh_passed.groupby(["regime53","symbol","cell_strategy","direction"]).size().to_dict()

    def normalize_cols(df, src):
        out_df = pd.DataFrame()
        if src in ("live_validated_parent","v9_observe_seed"):
            out_df["regime53"] = df["parent_regime"]
            out_df["pair"] = df["pair"]
            out_df["family"] = df.get("family")
            out_df["cell_strategy"] = df["strategy"]
            out_df["direction"] = df["direction"]
            out_df["session_bucket"] = df["session_bucket"]
            out_df["shave_rule"] = df.get("shave_rule")
            out_df["n_unique"] = df.get("n_unique", df.get("n", 0))
            out_df["wins_unique"] = df.get("wins_unique", df.get("wins", 0))
            out_df["wr_unique"] = df.get("wr_unique", df.get("wr", 0))
            out_df["wilson_lb"] = df.get("wilson_lb", 0)
        elif src == "boundary_sibling":
            for c in ["regime53","pair","family","cell_strategy","direction",
                      "session_bucket","child_rule","n_unique","wins_unique",
                      "wr_unique","wilson_lb"]:
                out_df[c if c != "child_rule" else "shave_rule"] = df.get(c, None)
        elif src == "probe_seed_child":
            for c in ["regime53","pair","cell_strategy","direction",
                      "session_bucket","shave_rule","n_unique","wins_unique",
                      "wr_unique"]:
                out_df[c] = df.get(c, None)
            out_df["family"] = df.get("cell_strategy").map(lambda s: {
                "alpha_pullback_v2":"dbb_trend","alpha_breakout_retest_v2":"direct",
                "alpha_extended_fade_v2":"reversal","echo_box_fade_v2":"reversal",
                "echo_failed_breakout_v2":"reversal","charlie_pullback_continuation_v2":"dbb_trend",
                "charlie_compression_breakout":"direct","bravo_failed_momentum":"reversal",
                "bravo_expansion_continuation":"dbb_trend","delta_tag_and_go_v2":"direct",
            }.get(s, "unknown"))
            out_df["wilson_lb"] = 0
        out_df["source"] = src
        return out_df

    combined = pd.concat([
        normalize_cols(v10_in_slice, "live_validated_parent"),
        normalize_cols(v9_in_slice, "v9_observe_seed"),
        normalize_cols(strike_in_slice, "boundary_sibling"),
        normalize_cols(probe_in_slice, "probe_seed_child"),
    ], ignore_index=True)

    # Look up live shadow-pass count
    def lookup_shadow(r):
        k = (r.regime53, r.pair, r.cell_strategy, r.direction)
        return int(sh_pass_counts.get(k, 0))
    combined["live_shadow_pass_count"] = combined.apply(lookup_shadow, axis=1)
    combined["session_match"] = (combined.session_bucket == cur_session)
    combined["pair_in_live"] = combined.pair.isin(top_pairs)

    # 4. Rank
    combined["wr_unique"] = pd.to_numeric(combined.wr_unique, errors="coerce").fillna(0)
    combined["n_unique"] = pd.to_numeric(combined.n_unique, errors="coerce").fillna(0).astype(int)
    combined["wilson_lb"] = pd.to_numeric(combined.wilson_lb, errors="coerce").fillna(0)
    src_rank = {"live_validated_parent": 1, "boundary_sibling": 2,
                "v9_observe_seed": 3, "probe_seed_child": 4}
    combined["src_rank"] = combined.source.map(src_rank).fillna(5).astype(int)

    combined["composite_score"] = (
        combined.live_shadow_pass_count * 5.0
        + combined.wilson_lb * 4.0
        + combined.wr_unique * 2.0
        + np.log1p(combined.n_unique) * 0.5
        + combined.session_match.astype(int) * 3.0
        + combined.pair_in_live.astype(int) * 1.0
        - combined.src_rank.astype(int) * 0.5
    )
    combined = combined.sort_values("composite_score", ascending=False)
    # dedup at deploy granularity, keep best
    combined_dd = combined.drop_duplicates(
        subset=["regime53","pair","cell_strategy","direction","session_bucket"], keep="first",
    )
    combined_dd["rank"] = range(1, len(combined_dd) + 1)
    combined_dd.to_csv(out / "current_slice_ranked_candidates.csv", index=False)

    # 5. Fallback ladder per pair
    ladder_rows = []
    for pair in top_pairs:
        for direction in ("long","short"):
            cell_set = combined_dd[(combined_dd.pair==pair) & (combined_dd.direction==direction)]
            if cell_set.empty:
                ladder_rows.append({"pair":pair, "direction":direction, "tier":"no_trade",
                                     "candidate":None, "source":None, "reason":"no_cell_in_slice"})
                continue
            # exact-match = live_validated_parent AND session_match AND in v10_fast already
            ex = cell_set[(cell_set.source=="live_validated_parent") & cell_set.session_match]
            if not ex.empty:
                r = ex.iloc[0]
                ladder_rows.append({"pair":pair, "direction":direction, "tier":"exact",
                                     "candidate":r.cell_strategy, "source":r.source,
                                     "session":r.session_bucket, "n":int(r.n_unique),
                                     "wr":round(r.wr_unique,3), "shadow_pass":int(r.live_shadow_pass_count),
                                     "reason":"live_validated, in v10_fast"})
                continue
            # widened sibling
            sb = cell_set[cell_set.source=="boundary_sibling"]
            if not sb.empty:
                r = sb.iloc[0]
                ladder_rows.append({"pair":pair, "direction":direction, "tier":"widened_sibling",
                                     "candidate":r.cell_strategy, "source":r.source,
                                     "session":r.session_bucket, "n":int(r.n_unique),
                                     "wr":round(r.wr_unique,3), "shadow_pass":int(r.live_shadow_pass_count),
                                     "reason":"boundary widened parent"})
                continue
            # alternate family in v9
            af = cell_set[cell_set.source=="v9_observe_seed"]
            if not af.empty:
                r = af.iloc[0]
                ladder_rows.append({"pair":pair, "direction":direction, "tier":"alt_family",
                                     "candidate":r.cell_strategy, "source":r.source,
                                     "session":r.session_bucket, "n":int(r.n_unique),
                                     "wr":round(r.wr_unique,3), "shadow_pass":int(r.live_shadow_pass_count),
                                     "reason":"v9_observe Seed in regime+pair"})
                continue
            ladder_rows.append({"pair":pair, "direction":direction, "tier":"no_trade",
                                 "candidate":None, "source":None, "reason":"no honest fit"})
    ladder = pd.DataFrame(ladder_rows)
    ladder.to_csv(out / "current_slice_fallback_ladder.csv", index=False)

    # 6. Fast candidate set: top entries from ladder where tier != no_trade
    fast = combined_dd[
        combined_dd.source.isin(["live_validated_parent","boundary_sibling"])
        & combined_dd.session_match
        & combined_dd.pair_in_live
    ].copy()
    fast.to_csv(out / "current_slice_fast_candidates.csv", index=False)

    # 7. Recommendation
    rec = [f"# Current-slice war-room — {now.isoformat()}"]
    rec.append("")
    rec.append(f"## Slice snapshot")
    rec.append(f"- UTC hour: {cur_hour} | session: **{cur_session}** | dominant regime: **{cur_regime}**")
    rec.append(f"- Top live pairs ({args.slice_window_min}min): {', '.join(top_pairs[:10])}")
    rec.append(f"- Family mix: {top_families}")
    rec.append(f"- Direction mix: {top_directions}")
    rec.append(f"- Shadow shave-passes in slice window: {(shadow_recent.block_reason=='shave_rule_satisfied').sum()}")
    rec.append("")
    rec.append(f"## Fast-candidate inventory")
    rec.append(f"- live_validated_parent in slice: {len(v10_in_slice)} (session_match={v10_in_slice.session_match.sum()})")
    rec.append(f"- boundary_sibling in slice:      {len(strike_in_slice)} (session_match={strike_in_slice.session_match.sum()})")
    rec.append(f"- v9_observe_seed in slice:       {len(v9_in_slice)}")
    rec.append(f"- probe_seed_child in slice:      {len(probe_in_slice)}")
    rec.append(f"- ranked candidates (dedup deploy): **{len(combined_dd)}**")
    rec.append(f"- fast candidates (in-session, in-pair, sibling+ parent): **{len(fast)}**")
    rec.append("")
    rec.append(f"## Top-10 candidates for current slice")
    rec.append("")
    rec.append("| rank | regime | pair | family | strategy | dir | session | source | n | wr | shadow_pass | score |")
    rec.append("|---:|---|---|---|---|---|---|---|---:|---:|---:|---:|")
    for _, r in combined_dd.head(10).iterrows():
        rec.append(f"| {int(r['rank'])} | {r.regime53} | {r.pair} | {r.family} | "
                   f"{r.cell_strategy} | {r.direction} | {r.session_bucket} | "
                   f"{r.source} | {int(r.n_unique)} | {r.wr_unique:.3f} | "
                   f"{int(r.live_shadow_pass_count)} | {r.composite_score:.2f} |")
    rec.append("")
    rec.append("## Fallback ladder by pair")
    rec.append("")
    rec.append("| pair | direction | tier | source | strategy | session | n | wr | reason |")
    rec.append("|---|---|---|---|---|---|---:|---:|---|")
    for _, r in ladder.iterrows():
        rec.append(f"| {r.pair} | {r.direction} | {r.tier} | {r.get('source','') or '-'} | "
                   f"{r.get('candidate','') or '-'} | {r.get('session','') or '-'} | "
                   f"{r.get('n','') or '-'} | {r.get('wr','') or '-'} | {r.reason} |")
    rec.append("")
    rec.append("## Direct answer: what should fire now?")
    rec.append("")
    if not fast.empty:
        top_fast = fast.head(5)
        rec.append(f"**{len(fast)} cells qualify** as honest fast candidates for this slice "
                   f"({cur_regime} / {cur_session} / top pairs). The top 5:")
        rec.append("")
        for _, r in top_fast.iterrows():
            rec.append(f"- `{r.regime53}|{r.pair}|{r.cell_strategy}|{r.direction}|{r.session_bucket}` "
                       f"({r.source}, n={int(r.n_unique)}, wr={r.wr_unique:.3f})")
    else:
        rec.append("**No cell currently in the live trade table OR among widened siblings "
                   "matches the current session.**")
        rec.append(f"All live-validated parents are for ny_open or ny_mid; current session is **{cur_session}**.")
        rec.append("")
        rec.append("Fix options:")
        rec.append("- Promote boundary siblings whose session_bucket clause was widened to include current session.")
        rec.append("- Mine new cells for the active session by re-running strike pass with current slice as target.")
        rec.append("- Accept no-trade for this session.")
    rec.append("")
    rec.append("## Recommendation")
    nowait = ladder[ladder.tier != "no_trade"]
    if not nowait.empty:
        rec.append(f"- **{len(nowait)} of {len(ladder)} pair×direction tuples have an honest fit.**")
        rec.append(f"- Tier breakdown: " + ", ".join(f"{t}={len(g)}" for t,g in nowait.groupby('tier')))
        rec.append("")
        rec.append("Build `v10_fast_v1.1` from `current_slice_fast_candidates.csv` and flip.")
        rec.append("This is a session-and-slice-aware narrow surface, not a universal table.")
    else:
        rec.append("No honest fit in the current slice. Two options:")
        rec.append("1. Mine slice-specific siblings: take live-validated parents, generate session siblings")
        rec.append("   targeted at the CURRENT session, replay against corpus, promote strict winners.")
        rec.append("2. Accept no-trade in this session, prepare for next active session.")

    (out / "current_slice_recommendation.md").write_text("\n".join(rec))

    print()
    print(f"-> {out / 'current_slice_live_state.csv'}")
    print(f"-> {out / 'current_slice_ranked_candidates.csv'}  ({len(combined_dd)} candidates)")
    print(f"-> {out / 'current_slice_fallback_ladder.csv'}    ({len(ladder)} ladder rows)")
    print(f"-> {out / 'current_slice_fast_candidates.csv'}    ({len(fast)} fast cells)")
    print(f"-> {out / 'current_slice_recommendation.md'}")


if __name__ == "__main__":
    main()
