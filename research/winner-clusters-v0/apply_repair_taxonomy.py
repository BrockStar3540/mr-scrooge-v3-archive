"""Apply repair taxonomy to trade-film ledger.

Per 2026-05-13 correction:
  Cell-level "earlier_ratchet" suggestion does NOT automatically make a loser
  salvageable. Box bugs, wrong-side entries, and broken geometry come FIRST.
  Only legit entries qualify for management-repair classification.

Two-stage annotation per row:

  Stage 1 — Entry legitimacy
    valid_entry_location   bool (entry_ts NOT in known box-bug window)
    box_boundary_context   str  (which box-bug window if any)
    entry_from_middle_flag bool (placeholder; needs box state at entry_ts)
    wrong_side_entry_flag  bool (placeholder; needs local price-action lookup)
    corrected_direction    str  (placeholder for future direction_repair work)
    corrected_entry_type   str  (placeholder)

  Stage 2 — Repair taxonomy
    repair_taxonomy        enum  one of:
      actual_winner           — realized_r > 0; already worked
      management_repair       — legit entry, went green, gave it back
      entry_timing_repair     — went green but bad timing; same direction OK
      direction_repair        — opposite direction was the legitimate winner
      box_geometry_repair     — entry made off broken box
      skip_required           — no honest entry available in the cell
      not_salvageable         — legit clean loss, no honest local save
      needs_review            — fallthrough / uncertain

  Plus, contingent on repair_taxonomy == 'management_repair':
    can_be_legitimately_saved  TRUE
    save_method                from cell_management_atlas recommendation
    management_hypothesis      free-text basis

Rules of assignment (order matters):
  1. If actual_realized_r > 0  → actual_winner
  2. If entry_ts in box-bug window for this pair → box_geometry_repair
  3. If audit_classification == 'good_entry_bad_management' → management_repair
     (audit already verified entry was legit AND management failed)
  4. If audit_classification == 'good_entry_clean_loser' → not_salvageable
     (audit verdict: clean entry, honest loss, no save available)
  5. If audit_classification == 'should_have_skipped':
       AND mfe_r > 0.3 (went green) → entry_timing_repair (placeholder; needs deeper work)
       AND mfe_r <= 0.3 (never went green) → direction_repair_or_skip
                                            (provisional — needs local opposite-direction lookup)
  6. Manual rows w/ actual_winner=False → not_salvageable
     (we don't have audit verdicts for manual theory trades)
  7. Else → needs_review

For management_repair rows, look up the (strategy, pair_family, session, direction)
cell in management_bug_atlas. If atlas recommendation is one of
{earlier_ratchet, tighter_be, quick_partial_or_lower_tp}, set:
  can_be_legitimately_saved = TRUE
  save_method = atlas recommendation
  management_hypothesis = atlas recommendation_basis
Otherwise mark TBD.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime, timezone

LEDGER = Path("/home/ubuntu/mr-scrooge-v3/research/trade-film-ledger/ledger.parquet")
MGMT_ATLAS = Path("/home/ubuntu/mr-scrooge-v3/research/management-bug-atlas-v0/cell_management_atlas.csv")

# Known box-bug contamination windows (from scrooge-bug-catalog B-068 to B-074)
# Each: (start_date_or_None, end_date_or_None, pairs_or_None, bug_id, description)
# entry_ts in [start, end] AND pair in pairs (or pairs=None means all) triggers the flag.
BOX_BUGS = [
    (None, "2026-03-09", {"EUR_USD","EUR_CAD","EUR_AUD","EUR_NZD","USD_CAD","GBP_CAD"},
     "B-068", "inverted boxes (stale 200-bar slice)"),
    ("2026-03-19", "2026-03-20", None, "B-069", "30m rolling box experiment"),
    ("2026-03-22", "2026-03-29", None, "B-072", "UTC midnight box-reset amnesia"),
    ("2026-03-31", "2026-04-09", {"USD_CHF","GBP_CAD"}, "B-073", "stale-box absurd TPs"),
    (None, "2026-04-13", None, "B-074", "regime vs alt-box mismatch (any alt-box trade)"),
]

PAIR_FAMILY = {
    "EUR_USD":"usd_base","GBP_USD":"usd_base","AUD_USD":"usd_base","NZD_USD":"usd_base",
    "USD_JPY":"usd_base","USD_CHF":"usd_base","USD_CAD":"usd_base","USD_MXN":"usd_base",
    "EUR_GBP":"eur_cross","EUR_AUD":"eur_cross","EUR_NZD":"eur_cross","EUR_CAD":"eur_cross",
    "EUR_CHF":"eur_cross","EUR_JPY":"eur_cross",
    "GBP_AUD":"gbp_cross","GBP_NZD":"gbp_cross","GBP_CAD":"gbp_cross","GBP_CHF":"gbp_cross","GBP_JPY":"gbp_cross",
    "AUD_NZD":"antipodean_cross","AUD_CAD":"antipodean_cross","AUD_CHF":"antipodean_cross",
    "AUD_JPY":"antipodean_cross","NZD_JPY":"antipodean_cross","CAD_JPY":"antipodean_cross","CHF_JPY":"antipodean_cross",
}


def session_of(ts):
    """Forex session from UTC hour."""
    if pd.isna(ts):
        return None
    h = ts.hour
    if 22 <= h or h < 6: return "asia"
    elif 6 <= h < 12: return "london"
    elif 12 <= h < 16: return "overlap"
    else: return "ny_pm"


def box_bug_context(entry_ts, pair):
    """Return list of bug_ids that apply to this entry_ts/pair, or empty list."""
    if pd.isna(entry_ts):
        return []
    hits = []
    for start, end, pairs, bug_id, desc in BOX_BUGS:
        if pairs is not None and pair not in pairs:
            continue
        d = entry_ts.date()
        s_ok = (start is None) or (d >= pd.Timestamp(start).date())
        e_ok = (end is None) or (d <= pd.Timestamp(end).date())
        if s_ok and e_ok:
            hits.append((bug_id, desc))
    return hits


def classify_repair(row):
    """Return (repair_taxonomy, valid_entry_location, box_boundary_context, notes)."""
    actual_r = row.get("actual_realized_r")
    src = str(row.get("source_label", ""))
    audit = str(row.get("audit_classification", "") or "")
    entry_ts = row.get("entry_ts")
    pair = row.get("pair")
    mfe_r = row.get("actual_mfe_r")

    bugs = box_bug_context(entry_ts, pair)
    valid_loc = (len(bugs) == 0)
    box_ctx = "; ".join(f"{b}:{d}" for b, d in bugs) if bugs else None

    # Rule 1: actual winner
    if pd.notna(actual_r) and actual_r > 0:
        return "actual_winner", valid_loc, box_ctx, "realized_r > 0"

    # Manual winner (no audit_classification, use actual_winner col)
    if src.startswith("manual") and bool(row.get("actual_winner", False)):
        return "actual_winner", valid_loc, box_ctx, "manual theory trade marked winner"

    # Rule 2: box bug overlay — entry on a broken box, regardless of audit verdict
    if not valid_loc:
        return "box_geometry_repair", valid_loc, box_ctx, f"entry in box-bug window: {box_ctx}"

    # Rule 3-4: trust the audit's clean classifications
    if audit == "good_entry_bad_management":
        return "management_repair", valid_loc, box_ctx, "audit: good entry, bad management"
    if audit == "good_entry_clean_loser":
        return "not_salvageable", valid_loc, box_ctx, "audit: clean entry, honest loss"
    if audit == "good_entry_clean_winner":
        return "actual_winner", valid_loc, box_ctx, "audit: clean winner"

    # Rule 5: should_have_skipped — split by whether trade went green
    if audit == "should_have_skipped":
        if pd.notna(mfe_r) and mfe_r > 0.3:
            return "entry_timing_repair", valid_loc, box_ctx, f"should-skip but went green to mfe={mfe_r:.2f}R; needs local-window lookup for valid entry"
        else:
            return "direction_repair_or_skip", valid_loc, box_ctx, "should-skip and never went green; opposite-direction lookup needed"

    # Manual losers without audit
    if src.startswith("manual") and not bool(row.get("actual_winner", False)):
        return "not_salvageable", valid_loc, box_ctx, "manual theory trade, no audit verdict"

    return "needs_review", valid_loc, box_ctx, f"audit={audit!r}"


# === Load ===
print(f"loading {LEDGER}")
df = pd.read_parquet(LEDGER)
print(f"  ledger: {len(df)} rows, {len(df.columns)} cols")
df["entry_ts"] = pd.to_datetime(df["entry_ts"], utc=True, errors="coerce")
df["session_derived"] = df["entry_ts"].apply(session_of)
print(f"  session derived for {df['session_derived'].notna().sum()} rows")
print(f"  session_bucket pre-fill nulls: {df['session_bucket'].isna().sum()}")
df.loc[df["session_bucket"].isna(), "session_bucket"] = df.loc[df["session_bucket"].isna(), "session_derived"]
print(f"  session_bucket post-fill nulls: {df['session_bucket'].isna().sum()}")

# === Apply taxonomy ===
print("\napplying repair taxonomy ...")
results = df.apply(classify_repair, axis=1, result_type="expand")
results.columns = ["repair_taxonomy", "valid_entry_location", "box_boundary_context", "_repair_notes"]
df["repair_taxonomy"] = results["repair_taxonomy"]
df["valid_entry_location"] = results["valid_entry_location"]
df["box_boundary_context"] = results["box_boundary_context"]
df["_repair_notes"] = results["_repair_notes"]

# Placeholders for future deeper work
for c in ["entry_from_middle_flag", "wrong_side_entry_flag",
          "corrected_direction", "corrected_entry_type",
          "management_hypothesis"]:
    if c not in df.columns:
        df[c] = None

# Reset can_be_legitimately_saved + save_method (we'll fill only management_repair rows)
df["can_be_legitimately_saved"] = None
df["save_method"] = None

# === Cross-reference management atlas for management_repair rows ===
mgmt = pd.read_csv(MGMT_ATLAS)
mgmt_key_cols = ["strategy", "pair_family", "session", "direction"]
# Build lookup: (strategy, pair_family, session, direction) -> (rec, basis)
mgmt_lookup = {}
for _, r in mgmt.iterrows():
    key = (r["strategy"], r["pair_family"], r["session"], r["direction"])
    mgmt_lookup[key] = (r["recommended_action"], r["recommendation_basis"])

# Resolve strategy/session for each ledger row
df["_strategy_for_lookup"] = df["bot_actual_strategy"].fillna(df["strategy_label"])
df["_session_for_lookup"] = df["session_bucket"].fillna(df["session_derived"])

n_saved = 0
n_repair_no_atlas = 0
for idx, r in df.iterrows():
    if r["repair_taxonomy"] != "management_repair":
        continue
    key = (r["_strategy_for_lookup"], r["pair_family"], r["_session_for_lookup"], r["direction"])
    if key in mgmt_lookup:
        rec, basis = mgmt_lookup[key]
        if rec in {"earlier_ratchet", "tighter_be", "quick_partial_or_lower_tp"}:
            df.at[idx, "can_be_legitimately_saved"] = True
            df.at[idx, "save_method"] = rec
            df.at[idx, "management_hypothesis"] = basis
            n_saved += 1
        elif rec == "skip_cell":
            # Atlas overrides audit — this cell should be skipped, not management-repaired
            df.at[idx, "repair_taxonomy"] = "skip_required"
            df.at[idx, "_repair_notes"] = f"audit said good_entry_bad_management but atlas says skip_cell: {basis}"
        else:
            df.at[idx, "can_be_legitimately_saved"] = None
            df.at[idx, "save_method"] = "TBD"
            df.at[idx, "management_hypothesis"] = f"atlas recommendation {rec}: {basis}"
            n_repair_no_atlas += 1
    else:
        n_repair_no_atlas += 1

# Drop scratch columns
df = df.drop(columns=["_strategy_for_lookup", "_session_for_lookup", "_repair_notes", "session_derived"], errors="ignore")

# === Save ===
df.to_parquet(LEDGER, index=False)
df.to_csv(LEDGER.with_suffix(".csv"), index=False)

print(f"\nrepair_taxonomy distribution:")
print(df["repair_taxonomy"].value_counts().to_string())
print(f"\nvalid_entry_location: {df['valid_entry_location'].sum()}/{len(df)} TRUE")
print(f"box_bug exposed: {df['box_boundary_context'].notna().sum()} rows")
print(f"\ncan_be_legitimately_saved = TRUE: {(df['can_be_legitimately_saved'] == True).sum()} rows")
print(f"save_method counts:")
print(df["save_method"].value_counts().to_string())

print(f"\nsaved {LEDGER}")
print(f"saved {LEDGER.with_suffix('.csv')}")
