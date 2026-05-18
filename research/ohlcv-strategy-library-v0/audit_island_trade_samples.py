"""Forensic audit of candidate islands before promotion to routing_table_v9.

Per Brock 2026-05-18: spot-check actual trade rows inside each island to catch
parser bugs, duplicate trades, era leakage, rule-replay mismatches, factor
nulls, and outcome anomalies — before any of these islands go live.

Risk-tiered sampling (NOT full universe):
  Tier 1 (mandatory): 100% WR islands at 10 <= n <= 30 across all V3 probes
                      + echo_box_fade_v2 Elite islands + small textbook nuclei
  Tier 2 (representative): stratified across families/regimes/directions
  Tier 3 (boundary):       random sample of false-friend siblings

Outputs:
  island_trade_audit_samples.csv  one row per sampled trade
  island_trade_audit_flags.csv    one row per island, with flag columns
  island_trade_audit_summary.md   human-readable rollup
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

log = logging.getLogger("audit_island_trades")

RAW_PARQUET = Path("/Users/brock-mini-mac/scrooge-research/routing-table-v2/ml_training_corpus.parquet")
# all_strategies_all_pairs_trades.parquet (14.97M) is textbook-only — has no
# probe replay rows. ml_training_corpus.parquet (15.27M, 65 strategies) is the
# canonical merged corpus with all 9 probes (481K probe rows).

V3_PROBES = {
    "alpha_pullback_v2", "alpha_breakout_retest_v2", "alpha_extended_fade_v2",
    "echo_box_fade_v2", "echo_failed_breakout_v2",
    "charlie_pullback_continuation_v2", "charlie_compression_breakout",
    "bravo_failed_momentum", "bravo_expansion_continuation",
    "delta_tag_and_go_v2",
}

# Rule grammar parser — same shape as gate/EntryFilter (clauses AND'd)
_RULE_RE = re.compile(r"^([\w_]+)\s*(<=|>=|<|>|==|=)\s*(.+?)\s*$")

FACTOR_COLS = ["ATR_ratio", "BB_compress", "ADX14", "RSI14", "close_pos", "volume_ratio", "bb_position"]

# Probe rules sometimes reference legacy names; alias them to the live columns.
FACTOR_ALIAS = {"price_pos": "close_pos"}

def _session_bucket_for_hour(h):
    if h is None: return None
    h = int(h)
    if   0 <= h < 4:   return "asia"
    elif 4 <= h < 6:   return "asia_late"
    elif 6 <= h < 9:   return "london_open"
    elif 9 <= h < 13:  return "ny_open"
    elif 13 <= h < 17: return "ny_mid"
    elif 17 <= h < 21: return "ny_close"
    else:              return "off_hours"


def parse_rule(rule: str) -> list[tuple[str, str, object]]:
    """Parse 'A>=1 AND B<=2 AND session_bucket==asia' into [(feat,op,val),...]"""
    if not isinstance(rule, str) or not rule.strip():
        return []
    out = []
    for raw in rule.split(" AND "):
        m = _RULE_RE.match(raw.strip())
        if not m:
            continue
        feat, op, val = m.group(1), m.group(2), m.group(3)
        op = "==" if op == "=" else op
        if feat in ("session_bucket",):
            v: object = val.strip("\"'")
        elif feat == "hour_utc":
            try:
                v = int(float(val))
            except ValueError:
                continue
        else:
            try:
                v = float(val)
            except ValueError:
                continue
        out.append((feat, op, v))
    return out


def eval_rule(row: pd.Series, clauses: list) -> tuple[bool, str]:
    """Return (matches, reason). reason names the first failing clause."""
    for feat, op, val in clauses:
        v = row.get(feat)
        if v is None or (isinstance(v, float) and np.isnan(v)):
            return False, f"null:{feat}"
        if isinstance(val, str):
            ok = (str(v) == val) if op == "==" else (str(v) != val)
        else:
            try:
                vf = float(v)
            except (TypeError, ValueError):
                return False, f"non_numeric:{feat}"
            if   op == "<=": ok = vf <= val
            elif op == ">=": ok = vf >= val
            elif op == "<":  ok = vf <  val
            elif op == ">":  ok = vf >  val
            elif op == "==": ok = vf == val
            else: ok = False
        if not ok:
            return False, f"failed:{feat}{op}{val}"
    return True, "match"


def apply_rule_to_df(df: pd.DataFrame, clauses: list) -> pd.Series:
    """Vectorized rule eval. Returns boolean Series."""
    if not clauses:
        return pd.Series(False, index=df.index)
    mask = pd.Series(True, index=df.index)
    for feat, op, val in clauses:
        # alias legacy feature names
        feat = FACTOR_ALIAS.get(feat, feat)
        if feat not in df.columns:
            return pd.Series(False, index=df.index)
        col = df[feat]
        if isinstance(val, str):
            mask &= (col.astype(str) == val) if op == "==" else (col.astype(str) != val)
        else:
            num = pd.to_numeric(col, errors="coerce")
            mask &= num.notna()
            if   op == "<=": mask &= (num <= val)
            elif op == ">=": mask &= (num >= val)
            elif op == "<":  mask &= (num <  val)
            elif op == ">":  mask &= (num >  val)
            elif op == "==": mask &= (num == val)
    return mask


# ---------------------------------------------------------------------------
# Island selection
# ---------------------------------------------------------------------------

def select_audit_islands(
    probe_winners: pd.DataFrame,
    textbook: pd.DataFrame,
    boundary: pd.DataFrame | None,
    seed: int = 42,
) -> pd.DataFrame:
    """Build the audit set per Brock 2026-05-18 tiering.

    Tier 1 (mandatory):
      - All echo_box_fade_v2 winners with wr==1.0 (the C01 Elite nucleus)
      - Top 30 pure probe islands by purity_gain * sqrt(n)
      - All textbook pure islands (small set)
      - 5 islands per other V3 probe strategy, top by purity_gain * sqrt(n)
    Tier 2 (representative):
      - 20 stratified across (root_strategy_id, technical_regime_53)
    Tier 3 (boundary):
      - 10 random false-friend siblings
    """
    rng = np.random.default_rng(seed)
    picks: list[pd.DataFrame] = []
    probe_winners = probe_winners.copy()
    probe_winners["purity_score"] = probe_winners["purity_gain"] * np.sqrt(probe_winners["n"])

    # ECHO_BOX_FADE_V2: the only C01 Elite probe — audit ALL perfect winners
    echo = probe_winners[(probe_winners.root_strategy_id == "echo_box_fade_v2") &
                         (probe_winners.wr >= 0.99) &
                         (probe_winners.n >= 10)]
    if len(echo) > 25:
        echo = echo.nlargest(25, "purity_score")
    echo = echo.assign(tier="T1_echo_elite")
    picks.append(echo)

    # Top 30 probe-pure overall
    pure = probe_winners[(probe_winners.wr >= 0.99) & (probe_winners.n >= 10) & (probe_winners.n <= 30)]
    pure = pure[pure.root_strategy_id != "echo_box_fade_v2"]
    pure = pure.nlargest(30, "purity_score").assign(tier="T1_probe_pure")
    picks.append(pure)

    # 5 per OTHER probe strategy
    for sid in V3_PROBES - {"echo_box_fade_v2"}:
        g = probe_winners[probe_winners.root_strategy_id == sid]
        if g.empty:
            continue
        top = g.nlargest(5, "purity_score").assign(tier=f"T1_probe_{sid[:18]}")
        picks.append(top)

    # All textbook pure
    text_pure = textbook[(textbook.wr >= 0.99) & (textbook.n >= 10) & (textbook.n <= 30)]
    picks.append(text_pure.assign(tier="T1_textbook_pure"))

    # Tier 2: stratified medium-sized
    mid = textbook[(textbook.wr >= 0.75) & (textbook.wr < 0.99) & (textbook.n >= 15)]
    if not mid.empty:
        mid = mid.sample(min(20, len(mid)), random_state=seed)
        picks.append(mid.assign(tier="T2_textbook_strong"))

    # Tier 3: boundary
    if boundary is not None and not boundary.empty:
        sample = boundary.sample(min(10, len(boundary)), random_state=seed)
        picks.append(sample.assign(tier="T3_boundary"))

    audit = pd.concat([p for p in picks if not p.empty], ignore_index=True)
    audit = audit.drop_duplicates(subset=["root_strategy_id", "pair", "direction",
                                          "technical_regime_53", "child_rule"])
    audit = audit.reset_index(drop=True)
    audit["island_id"] = ["ISL_%04d" % i for i in range(len(audit))]
    return audit


# ---------------------------------------------------------------------------
# Per-island audit
# ---------------------------------------------------------------------------

def audit_island(
    island: pd.Series, raw: pd.DataFrame, max_sample: int = 10,
) -> tuple[pd.DataFrame, dict]:
    """Audit one island. Returns (sample_rows_df, flags_dict)."""
    flags = {
        "island_id": island["island_id"],
        "tier": island["tier"],
        "root_strategy_id": island["root_strategy_id"],
        "pair": island["pair"],
        "direction": island["direction"],
        "technical_regime_53": island["technical_regime_53"],
        "rule": island["child_rule"],
        "claimed_n": int(island["n"]),
        "claimed_wins": int(island["wins"]),
        "claimed_losses": int(island["losses"]),
        "claimed_wr": float(island["wr"]),
        "flag_parent_membership_mismatch": False,
        "flag_rule_membership_mismatch": False,
        "flag_duplicate_trade_rows": False,
        "flag_era_leakage_suspect": False,
        "flag_time_feature_mismatch": False,
        "flag_factor_null_or_impossible": False,
        "flag_outcome_pattern_suspect": False,
        "flag_boundary_fragile": False,
        "flag_replay_count_mismatch": False,
        "audit_status": "clean",
        "notes": "",
    }
    notes: list[str] = []

    # Build parent slice
    parent_mask = ((raw["strategy_id"] == island["root_strategy_id"]) &
                   (raw["pair"] == island["pair"]) &
                   (raw["direction"] == island["direction"]) &
                   (raw["technical_regime_53"] == island["technical_regime_53"]))
    parent = raw[parent_mask]
    if len(parent) == 0:
        flags["flag_parent_membership_mismatch"] = True
        notes.append("no_parent_rows_in_raw")
        flags["audit_status"] = "suspect"
        flags["notes"] = "; ".join(notes)
        return pd.DataFrame(), flags

    clauses = parse_rule(island["child_rule"])
    if not clauses:
        notes.append("rule_unparseable")
        flags["audit_status"] = "suspect"
        flags["flag_rule_membership_mismatch"] = True
        flags["notes"] = "; ".join(notes)
        return pd.DataFrame(), flags

    island_mask = apply_rule_to_df(parent, clauses)
    island_rows = parent[island_mask]
    winners = island_rows[island_rows.is_win]
    losers = island_rows[~island_rows.is_win]
    rejected = parent[~island_mask & ~parent.is_win]

    # Replay count vs claimed
    n_actual = len(island_rows)
    w_actual = len(winners)
    if abs(n_actual - flags["claimed_n"]) > max(2, flags["claimed_n"] * 0.10):
        flags["flag_replay_count_mismatch"] = True
        notes.append(f"replay_n={n_actual}_claimed_n={flags['claimed_n']}")
    if abs(w_actual - flags["claimed_wins"]) > max(1, flags["claimed_wins"] * 0.10):
        flags["flag_replay_count_mismatch"] = True
        notes.append(f"replay_w={w_actual}_claimed_w={flags['claimed_wins']}")

    # Duplicate check on (entry_ts, pair, strategy_id, direction)
    if len(island_rows) > 0:
        dup_keys = ["entry_ts", "pair", "strategy_id", "direction"]
        dup_counts = island_rows.groupby(dup_keys).size()
        if (dup_counts > 1).any():
            flags["flag_duplicate_trade_rows"] = True
            notes.append(f"dup_groups={(dup_counts > 1).sum()}")

    # Era leakage check (only if the corpus carries era labels)
    if "era" in island_rows.columns and len(island_rows) > 0:
        era_vals = set(island_rows.era.dropna().unique())
        if era_vals and era_vals != {"discovery", "holdout"}:
            era_split = island_rows.era.value_counts(normalize=True).to_dict()
            notes.append(f"era_split={era_split}")

    # Factor null check on the sampled rows
    if len(island_rows) > 0:
        for fc in FACTOR_COLS:
            if fc in island_rows.columns:
                null_pct = island_rows[fc].isna().mean()
                if null_pct > 0.20:
                    flags["flag_factor_null_or_impossible"] = True
                    notes.append(f"{fc}_null={null_pct:.0%}")

    # Outcome pattern check. Corpus stores realized_R as a signed multiple
    # (-1.0 = stop, positive = win). mfe_R / mae_R are positive magnitudes
    # in the all_strategies dataset but absent from ml_training_corpus, so
    # check only if those columns are present.
    if len(winners) > 0:
        unique_r = winners.realized_R.nunique() if "realized_R" in winners.columns else 0
        if unique_r == 1 and len(winners) >= 5:
            r0 = winners.realized_R.iloc[0]
            # only flag if the constant is suspicious; many wins legitimately
            # exit at the same R-target (tp2 hit). Flag if r0 < 1.0 (would
            # suggest non-target exit) or r0 absurdly large.
            if r0 < 1.0 or r0 > 10.0:
                flags["flag_outcome_pattern_suspect"] = True
                notes.append(f"all_winners_same_R={r0}")
        if "mfe_R" in winners.columns and winners["mfe_R"].notna().any():
            # mfe should be >= |realized_R| for a winner (price moved at
            # least as far as the realized outcome). Sign convention is
            # positive magnitudes in the source data, so we compare absolute.
            try:
                mfe_too_small = (winners.mfe_R.abs() + 1e-6 < winners.realized_R.abs()).sum()
                if mfe_too_small > 0:
                    flags["flag_outcome_pattern_suspect"] = True
                    notes.append(f"mfe_below_realized_R count={mfe_too_small}")
            except Exception:
                pass

    # Boundary fragility: compare island factor distribution to immediate rejects
    # If a single factor swing of <2% of the threshold flips winner→loser, fragile.
    if len(winners) > 0 and len(rejected) > 0:
        rejected_sample = rejected.sample(min(50, len(rejected)), random_state=42)
        for feat, op, val in clauses:
            if isinstance(val, str) or feat not in winners.columns:
                continue
            try:
                wmean = winners[feat].mean()
                rmean = rejected_sample[feat].mean()
                if not (np.isnan(wmean) or np.isnan(rmean)):
                    span = max(abs(val) * 0.02, 1e-6)
                    if abs(wmean - rmean) < span:
                        flags["flag_boundary_fragile"] = True
                        notes.append(f"boundary_thin:{feat}")
                        break
            except Exception:
                continue

    # Build sample frame: up to max_sample winners + max_sample losers + 5 rejected
    sample_chunks = []
    if len(winners) > 0:
        s = winners.sample(min(max_sample, len(winners)), random_state=42).copy()
        s["sample_bucket"] = "winner"
        sample_chunks.append(s)
    if len(losers) > 0:
        s = losers.sample(min(max_sample, len(losers)), random_state=42).copy()
        s["sample_bucket"] = "loser"
        sample_chunks.append(s)
    if len(rejected) > 0:
        s = rejected.sample(min(5, len(rejected)), random_state=42).copy()
        s["sample_bucket"] = "rejected_boundary"
        sample_chunks.append(s)

    if sample_chunks:
        samples = pd.concat(sample_chunks, ignore_index=True)
        samples["island_id"] = island["island_id"]
        samples["tier"] = island["tier"]
        samples["rule"] = island["child_rule"]
    else:
        samples = pd.DataFrame()

    # Final audit status
    bad_flags = [k for k, v in flags.items() if k.startswith("flag_") and v]
    critical = {"flag_parent_membership_mismatch", "flag_rule_membership_mismatch",
                "flag_replay_count_mismatch", "flag_outcome_pattern_suspect"}
    if any(f in critical for f in bad_flags):
        flags["audit_status"] = "suspect"
    elif bad_flags:
        flags["audit_status"] = "needs_review"
    flags["notes"] = "; ".join(notes)
    return samples, flags


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--probe-winners", required=True)
    p.add_argument("--textbook", required=True)
    p.add_argument("--boundary", default=None,
                   help="Optional CSV of false-friend siblings for Tier 3")
    p.add_argument("--out-dir", required=True)
    p.add_argument("--max-sample", type=int, default=10)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    log.info("Loading candidate CSVs...")
    probe = pd.read_csv(args.probe_winners)
    text = pd.read_csv(args.textbook)
    boundary = pd.read_csv(args.boundary) if args.boundary else None
    log.info("  probe winners=%d, textbook=%d, boundary=%s",
             len(probe), len(text),
             len(boundary) if boundary is not None else "skipped")

    log.info("Selecting audit islands...")
    audit_set = select_audit_islands(probe, text, boundary, seed=args.seed)
    log.info("  selected %d islands across tiers: %s",
             len(audit_set),
             audit_set["tier"].value_counts().to_dict())

    log.info("Loading raw trades parquet (this is heavy)...")
    # ml_training_corpus.parquet doesn't carry mfe_R/mae_R/era/session_bucket/
    # exit_reason — those live in all_strategies. We compute session_bucket
    # from hour_utc inline below.
    available = set(pq.read_schema(RAW_PARQUET).names)
    desired = ["pair", "strategy_id", "direction", "technical_regime_53",
               "entry_ts", "is_win", "realized_R", "hour_utc"] + FACTOR_COLS
    # Optional columns: include only if present
    for opt in ("mfe_R", "mae_R", "exit_reason", "session_bucket", "era", "day_of_week"):
        if opt in available:
            desired.append(opt)
    needed = [c for c in desired if c in available]
    raw = pq.read_table(RAW_PARQUET, columns=needed).to_pandas()
    if "session_bucket" not in raw.columns and "hour_utc" in raw.columns:
        raw["session_bucket"] = raw["hour_utc"].map(_session_bucket_for_hour)
    log.info("  raw rows=%d  cols=%s", len(raw), list(raw.columns))

    all_samples: list[pd.DataFrame] = []
    all_flags: list[dict] = []
    for idx, island in audit_set.iterrows():
        if idx % 10 == 0:
            log.info("  auditing %d / %d (%s)", idx, len(audit_set), island["island_id"])
        s, f = audit_island(island, raw, max_sample=args.max_sample)
        if not s.empty:
            all_samples.append(s)
        all_flags.append(f)

    samples_df = pd.concat(all_samples, ignore_index=True) if all_samples else pd.DataFrame()
    flags_df = pd.DataFrame(all_flags)

    samples_path = out / "island_trade_audit_samples.csv"
    flags_path = out / "island_trade_audit_flags.csv"
    summary_path = out / "island_trade_audit_summary.md"

    samples_df.to_csv(samples_path, index=False)
    flags_df.to_csv(flags_path, index=False)

    # Summary
    md = ["# Island trade audit summary",
          "",
          f"**Generated**: {pd.Timestamp.now(tz='UTC').isoformat()}",
          f"**Audited islands**: {len(flags_df)}",
          f"**Sample rows emitted**: {len(samples_df)}",
          "",
          "## Audit status",
          ""]
    status_counts = flags_df["audit_status"].value_counts().to_dict()
    for s in ["clean", "needs_review", "suspect"]:
        md.append(f"- **{s}**: {status_counts.get(s, 0)}")
    md.append("")
    md.append("## Tier breakdown")
    md.append("")
    md.append("| Tier | Total | Clean | Needs review | Suspect |")
    md.append("|---|---:|---:|---:|---:|")
    for tier in sorted(flags_df.tier.unique()):
        g = flags_df[flags_df.tier == tier]
        md.append(f"| {tier} | {len(g)} | {(g.audit_status=='clean').sum()} | "
                  f"{(g.audit_status=='needs_review').sum()} | "
                  f"{(g.audit_status=='suspect').sum()} |")
    md.append("")
    md.append("## Flag prevalence")
    md.append("")
    flag_cols = [c for c in flags_df.columns if c.startswith("flag_")]
    for fc in flag_cols:
        md.append(f"- **{fc}**: {flags_df[fc].sum()} / {len(flags_df)}")
    md.append("")
    md.append("## Suspect islands (do NOT promote)")
    md.append("")
    suspect = flags_df[flags_df.audit_status == "suspect"]
    if suspect.empty:
        md.append("_None_")
    else:
        md.append("| island_id | strategy | pair | dir | regime | n | w | wr | notes |")
        md.append("|---|---|---|---|---|---:|---:|---:|---|")
        for _, r in suspect.iterrows():
            md.append(f"| {r.island_id} | {r.root_strategy_id} | {r.pair} | "
                      f"{r.direction} | {r.technical_regime_53} | {r.claimed_n} | "
                      f"{r.claimed_wins} | {r.claimed_wr:.3f} | {r.notes[:120]} |")
    md.append("")
    md.append("## Needs-review islands (manual eyeball)")
    md.append("")
    review = flags_df[flags_df.audit_status == "needs_review"]
    if review.empty:
        md.append("_None_")
    else:
        md.append("| island_id | strategy | pair | dir | regime | n | wr | flags |")
        md.append("|---|---|---|---|---|---:|---:|---|")
        for _, r in review.iterrows():
            on_flags = [c.replace("flag_", "") for c in flag_cols if r.get(c)]
            md.append(f"| {r.island_id} | {r.root_strategy_id} | {r.pair} | "
                      f"{r.direction} | {r.technical_regime_53} | {r.claimed_n} | "
                      f"{r.claimed_wr:.3f} | {', '.join(on_flags)} |")
    summary_path.write_text("\n".join(md))

    log.info("=== DONE ===")
    log.info("  samples -> %s", samples_path)
    log.info("  flags   -> %s", flags_path)
    log.info("  summary -> %s", summary_path)
    log.info("Status: %s", status_counts)


if __name__ == "__main__":
    main()
