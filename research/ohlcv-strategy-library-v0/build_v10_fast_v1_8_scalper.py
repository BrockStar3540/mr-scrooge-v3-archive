"""Build routing_table_v10_fast_v1_8.parquet.

Per Brock 2026-05-21:
- 12 REGULAR + MODERATE cells from scalper_bank_cells_10sl_12tp_ratchet.csv
- Top-session-only derived from the 10/12/ratchet corpus
- No GHOSTS, no synthetic session fan-out
- Mapped to the existing v9 schema for live bot consumption
"""
import pandas as pd
import numpy as np
import pyarrow.parquet as pq
import datetime as dt

BANK_CSV = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_bank_cells_10sl_12tp_ratchet.csv"
CORPUS = "/home/ubuntu/mr-scrooge-v3/research/ohlcv-strategy-library-v0/scalper_corpus_10sl_12tp_ratchet.parquet"
OUT_PARQUET = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v10_fast_v1_8.parquet"
OUT_MD = "/home/ubuntu/mr-scrooge-v3/data/routing_table_v10_fast_v1_8_summary.md"

# Tier mapping for live bot's entry_filter min_tier=Seed-Pro
TIER_BY_FREQ = {"REGULAR": "Elite", "MODERATE": "Pro", "RARE": "Seed-Pro"}

bank = pd.read_csv(BANK_CSV)
deploy = bank[bank.freq_class.isin(["REGULAR","MODERATE"])].copy()
print(f"deployable cells (REGULAR+MODERATE): {len(deploy)}", flush=True)
print(deploy[["pair","regime","direction","family","rule","n_clean","wr_clean",
              "expected_pips_per_trade","fires_per_week","expected_pips_per_week",
              "freq_class"]].to_string(index=False), flush=True)

# Load corpus
print("\nloading corpus for session derivation...", flush=True)
need = ["technical_regime_53","pair","direction","family",
        "session_bucket","outcome_10sl_12tp_ratchet",
        "realized_pips_estimated","is_clean_10sl_12tp_ratchet",
        "ATR_ratio","BB_compress","ADX14","RSI14","price_pos","volume_ratio"]
corpus = pq.read_table(CORPUS, columns=need).to_pandas()
print(f"corpus rows: {len(corpus):,}", flush=True)

# Legacy 3-bucket -> live 7-bucket mapping (use most-common live-bot bucket per legacy)
LEGACY_TO_LIVE = {
    "asia":   "asia",
    "london": "london_open",
    "ny":     "ny_mid",   # ny mid is the highest-volume sub-bucket; cell would also fire in ny_open/ny_close if shave_rule permits, but we deploy on one
}

# Per-cell, parse rule, apply to corpus, group by session, pick top by expected_pips
import re
CLAUSE_RE = re.compile(r"(\w+)\s*([<>=]+)\s*([-\d.eE]+)")

def parse_rule(rule):
    if pd.isna(rule) or rule in ("", "(no filter)"):
        return []
    clauses = []
    for part in rule.split(" AND "):
        m = CLAUSE_RE.match(part.strip())
        if not m: continue
        clauses.append((m.group(1), m.group(2), float(m.group(3))))
    return clauses

def apply_clauses(df, clauses):
    if not clauses: return df
    m = pd.Series(True, index=df.index)
    for col, op, thr in clauses:
        col_actual = "close_pos" if col == "price_pos" else col
        if col_actual not in df.columns: continue
        s = pd.to_numeric(df[col_actual], errors="coerce")
        if op == "<=": m &= (s <= thr)
        elif op == ">=": m &= (s >= thr)
        elif op == "<":  m &= (s <  thr)
        elif op == ">":  m &= (s >  thr)
    return df[m]

# Build routing-table rows
now_iso = dt.datetime.now(dt.timezone.utc).isoformat()
rows = []
print("\nderiving top sessions...", flush=True)
for i, c in enumerate(deploy.itertuples(index=False), start=1):
    rg, pair, dirn, fam = c.regime, c.pair, c.direction, c.family
    sub = corpus[(corpus.technical_regime_53 == rg) & (corpus.pair == pair)
                 & (corpus.direction == dirn) & (corpus.family == fam)]
    clauses = parse_rule(c.rule)
    matched = apply_clauses(sub, clauses)
    if "session_bucket" not in matched.columns or len(matched) == 0:
        top_sess_legacy = "unknown"; sess_ev = 0.0; sess_n = 0
    else:
        # Per session: clean count + mean realized pips (only on clean events)
        clean = matched[matched.is_clean_10sl_12tp_ratchet]
        sess_stats = (
            clean.groupby("session_bucket")
            .agg(n_clean=("is_clean_10sl_12tp_ratchet","sum"),
                 ev_pips=("realized_pips_estimated","mean"))
        )
        # Require n_clean >= 20 AND positive ev_pips. Sort by ev_pips.
        elig = sess_stats[(sess_stats.n_clean >= 20) & (sess_stats.ev_pips > 0)]
        if len(elig) > 0:
            best = elig.sort_values("ev_pips", ascending=False).iloc[0]
            top_sess_legacy = best.name
            sess_ev = float(best["ev_pips"])
            sess_n = int(best["n_clean"])
        else:
            # Fall back to highest ev_pips regardless of n
            if len(sess_stats):
                best = sess_stats.sort_values("ev_pips", ascending=False).iloc[0]
                top_sess_legacy = best.name + "(fallback)"
                sess_ev = float(best["ev_pips"])
                sess_n = int(best["n_clean"])
            else:
                top_sess_legacy = "unknown"; sess_ev = 0.0; sess_n = 0
    # Map legacy bucket -> live 7-bucket
    top_sess_clean = top_sess_legacy.replace("(fallback)","")
    top_sess = LEGACY_TO_LIVE.get(top_sess_clean, top_sess_clean)
    # Drop cells where the deploy session has negative expectancy
    if sess_ev <= 0:
        print(f"     SKIP -- best session has non-positive ev ({sess_ev:+.2f})", flush=True)
        continue
    strat_id = f"scalper_v1_{fam}_{dirn}_{pair.lower()}_{rg.lower()}"
    tier = TIER_BY_FREQ.get(c.freq_class, "Seed-Pro")
    rows.append({
        "sub_regime": rg, "technical_regime_53": rg, "technical_regime_desc": "",
        "parent_regime": rg, "session_bucket": top_sess,
        "pair": pair, "strategy": strat_id, "family": fam, "direction": dirn,
        "r_target": 1.2, "score_boost": 0.0,
        "n": int(c.n_clean), "wins": int(c.wins_clean),
        "sum_R": 0.0, "mean_R": float(c.expected_pips_per_trade) / 10.0,
        "wr": float(c.wr_clean),
        "source": "scalper_bank_10sl_12tp_ratchet_2026-05-21",
        "last_updated": now_iso,
        "shave_rule": c.rule if c.rule != "(no filter)" else "",
        "loser_skip_rule": "",
        "winner_lift": float(c.expected_pips_per_trade - c.baseline_clean_ev_pips),
        "parent_n": 0, "parent_wr": float(c.baseline_clean_wr),
        "tier": tier,
        "n_unique": int(c.n_clean),
        "wilson_lb": float(c.wilson_lb),
        "source_bank": "scalper_bank_v1",
        "oos_status": "in_sample",
        "promotion_status": "candidate",
        "promote_source": "scalper_bank_v1_2026-05-21",
    })
    sess_info = f"sess={top_sess} ev={sess_ev:+.2f}pips n={sess_n}"
    print(f"  {i:>2}/{len(deploy)}  {rg}/{pair}/{dirn}/{fam}/{c.freq_class:<8}  {sess_info}", flush=True)

v18 = pd.DataFrame(rows)
v18.to_parquet(OUT_PARQUET, index=False)
print(f"\nwrote {OUT_PARQUET}  ({len(v18)} cells / {len(v18.drop_duplicates(['technical_regime_53','pair','direction','strategy']))} unique signatures)", flush=True)

# Summary
with open(OUT_MD,"w") as f:
    f.write("# v10_fast_v1.8 Routing Table Summary\n\n")
    f.write(f"Built {now_iso}\n\n")
    f.write(f"Source: scalper_bank_cells_10sl_12tp_ratchet.csv (REGULAR + MODERATE only)\n\n")
    f.write(f"**Total cells: {len(v18)}** (top-session-only, no synthetic fan-out)\n\n")
    f.write("## Cells\n\n")
    f.write("| # | pair | regime | dir | family | session | tier | rule | n | WR | E[pips]/trade | fires/wk |\n")
    f.write("|---:|---|---|---|---|---|---|---|---:|---:|---:|---:|\n")
    for idx, (_, r) in enumerate(deploy.iterrows(), start=1):
        # Find matching session from v18
        match = v18[(v18.pair==r.pair) & (v18.parent_regime==r.regime) & (v18.direction==r.direction) & (v18.family==r.family)]
        sess = match.iloc[0].session_bucket if len(match) else "?"
        tier = match.iloc[0].tier if len(match) else "?"
        f.write(f"| {idx} | {r.pair} | {r.regime} | {r.direction} | {r.family} | {sess} | {tier} | `{r.rule}` | {int(r.n_clean)} | {r.wr_clean:.3f} | {r.expected_pips_per_trade:+.2f} | {r.fires_per_week:.2f} |\n")
    f.write("\n## Execution truth\n\n")
    f.write("- SL = 10 pips (initial)\n- TP1 = 12 pips\n- Ratchet: +6→SL=-6, +8→SL=-3, +10→SL=BE\n")
print(f"wrote {OUT_MD}")
