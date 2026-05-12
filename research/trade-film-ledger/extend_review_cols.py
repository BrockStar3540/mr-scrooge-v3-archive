"""Extend trade-film ledger with forensic-review columns.

Per locked direction 2026-05-12 (later that day):
  Winners reveal real structure; losers come in as contrast.

Adds these EMPTY columns (filled later by human/script review):
  - winner_cluster_id           — assigned during winner-synchrony discovery
  - raw_synchrony_notes         — free-text observation during clustering
  - pair_family                 — derived enum (will be filled by simple lookup)
  - session_bucket              — same as session for now; reserved for finer buckets
  - factor_signature            — JSON/text of factor pattern within the cluster
  - setup_geometry              — JSON/text of entry/stop/TP pattern
  - management_signature        — JSON/text of ratchet/exit behavior pattern
  - nearest_loser_contrast      — ledger_id of nearest loser; describes what was missing
  - candidate_micro_strategy    — micro-strategy id once registered
  - candidate_regime_split      — proposed split label ONLY when matrix proves a fork
  - ready_for_backtest          — bool gate: micro-strategy hardened, ready for corpus replay

pair_family IS auto-derived (simple deterministic lookup) — others stay null.
"""
import pandas as pd
from pathlib import Path

LEDGER_DIR = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger")
df = pd.read_parquet(LEDGER_DIR / "ledger.parquet")
print(f"loaded ledger: {len(df)} rows, {len(df.columns)} cols")

# Derive pair_family (rule: classify each pair into a family by macro-character)
PAIR_FAMILY = {
    # USD-base (USD is one side; majors and EUR-rate proxies)
    "EUR_USD": "usd_base", "GBP_USD": "usd_base", "AUD_USD": "usd_base",
    "NZD_USD": "usd_base", "USD_JPY": "usd_base", "USD_CHF": "usd_base",
    "USD_CAD": "usd_base", "USD_MXN": "usd_base",
    # EUR crosses
    "EUR_GBP": "eur_cross", "EUR_AUD": "eur_cross", "EUR_NZD": "eur_cross",
    "EUR_CAD": "eur_cross", "EUR_CHF": "eur_cross", "EUR_JPY": "eur_cross",
    # GBP crosses
    "GBP_AUD": "gbp_cross", "GBP_NZD": "gbp_cross", "GBP_CAD": "gbp_cross",
    "GBP_CHF": "gbp_cross", "GBP_JPY": "gbp_cross",
    # Antipodean crosses (commodity currencies crossed against each other)
    "AUD_NZD": "antipodean_cross", "AUD_CAD": "antipodean_cross",
    "AUD_CHF": "antipodean_cross", "AUD_JPY": "antipodean_cross",
    "NZD_JPY": "antipodean_cross", "CAD_JPY": "antipodean_cross",
    "CHF_JPY": "antipodean_cross",
}

NEW_COLS = [
    "winner_cluster_id",
    "raw_synchrony_notes",
    "pair_family",
    "session_bucket",
    "factor_signature",
    "setup_geometry",
    "management_signature",
    "nearest_loser_contrast",
    "candidate_micro_strategy",
    "candidate_regime_split",
    "ready_for_backtest",
]

for col in NEW_COLS:
    if col not in df.columns:
        df[col] = None

# Auto-fill pair_family (deterministic)
df["pair_family"] = df["pair"].map(PAIR_FAMILY).fillna("other")
# Auto-fill session_bucket = session for now (reserved field for later refinement)
df["session_bucket"] = df["session"]

# Coerce mixed-type str for parquet
for c in NEW_COLS:
    if c not in ("ready_for_backtest",):
        df[c] = df[c].astype("object")

df.to_parquet(LEDGER_DIR / "ledger.parquet", index=False)
df.to_csv(LEDGER_DIR / "ledger.csv", index=False)

print(f"\nextended ledger: {len(df)} rows, {len(df.columns)} cols")
print("\npair_family distribution:")
print(df["pair_family"].value_counts().to_string())
print("\nnew review columns (empty as intended):")
for c in NEW_COLS:
    nulls = df[c].isna().sum()
    print(f"  {c}: {nulls}/{len(df)} null")
