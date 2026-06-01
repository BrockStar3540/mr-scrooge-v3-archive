"""Out-of-sample validation of the matrix signatures.

For each matrix cell's mined rule (the `serial` with pinned factors), test whether
trades matching it on a HELD-OUT later time slice still beat the cell baseline, or
collapse (= overfit / survivorship). Report survival rate, how much the claimed
exp_optimized_pips over-promises OOS, and whether ALIGNMENT-factor rules
(H20/H60/T1/T4) hold better than non-alignment ones.

Caveat: which factors are pinned came from full-data mining (mild leak in factor
SELECTION); rule VALIDITY is tested on held-out time. Rules that fail this are
definitely overfit; rules that pass are promising (a full train-only re-mine would
confirm). Good enough to separate real signatures from fantasy.
"""
import pandas as pd, numpy as np

CODES = ["BB","BBP","A5","A1","RSI","E20","E50","ZS","SPR","ADR","H20","H60","T1","T4"]
ALIGN = {"H20","H60","T1","T4"}
SIG = "/tmp/sig_corpus_phase3.csv.gz"
MAT = "data/matrix_meal_lookup.csv"

sig = pd.read_csv(SIG)
sig["entry_time"] = pd.to_datetime(sig["entry_time"], utc=True, errors="coerce")
sig = sig.dropna(subset=["entry_time"]).sort_values("entry_time").reset_index(drop=True)
cut = sig["entry_time"].quantile(0.70)
sig["split"] = np.where(sig["entry_time"] <= cut, "train", "test")
print("trades=%d  train=%d test=%d  cut=%s" %
      (len(sig), (sig.split=="train").sum(), (sig.split=="test").sum(), cut))

# index cell -> sub-df
sig["k"] = sig[["pair","strategy","direction","session"]].astype(str).agg("|".join, axis=1)
cells = {k: g for k, g in sig.groupby("k")}

mat = pd.read_csv(MAT)
res = []
for _, m in mat.iterrows():
    k = "|".join(str(m[c]) for c in ["pair","strategy","direction","session"])
    g = cells.get(k)
    if g is None: continue
    serial = str(m.get("serial",""))
    parts = serial.split("|")
    if len(parts) < 4+len(CODES): continue
    pinned = {CODES[i]: parts[4+i] for i in range(len(CODES)) if parts[4+i] not in ("*","")}
    if not pinned: continue
    tr = g[g.split=="train"]; te = g[g.split=="test"]
    if len(tr) < 40 or len(te) < 20: continue
    def mask(df):
        mm = pd.Series(True, index=df.index)
        for c,v in pinned.items(): mm &= (df[c]==v)
        return df[mm]
    rtr, rte = mask(tr), mask(te)
    if len(rtr) < 30 or len(rte) < 10: continue
    res.append({
        "k": k, "n_pinned": len(pinned),
        "has_align": any(c in ALIGN for c in pinned),
        "claimed_opt": float(m.get("exp_optimized_pips", np.nan)),
        "base_test": te["pnl_pips"].mean(),
        "rule_train": rtr["pnl_pips"].mean(),
        "rule_test": rte["pnl_pips"].mean(),
        "rule_test_n": len(rte),
        "rule_test_wr": rte["win"].mean(),
    })

r = pd.DataFrame(res)
print("\nrules with enough train+test support: %d" % len(r))
r["holds"] = (r["rule_test"] > r["base_test"]) & (r["rule_test"] > 0)
print("HOLD OOS (test beats baseline AND >0): %d (%.0f%%)" % (r["holds"].sum(), 100*r["holds"].mean()))
print("\n-- over-promise: claimed optimized vs realized OOS --")
print("  mean claimed_opt = %+.2fp   mean rule_test (held-out) = %+.2fp   gap = %+.2fp"
      % (r["claimed_opt"].mean(), r["rule_test"].mean(), r["claimed_opt"].mean()-r["rule_test"].mean()))
print("  mean baseline_test = %+.2fp   => OOS lift of rule over baseline = %+.2fp"
      % (r["base_test"].mean(), (r["rule_test"]-r["base_test"]).mean()))
print("\n-- ALIGNMENT factors (H20/H60/T1/T4) vs not --")
for flag,lab in [(True,"rule USES alignment"),(False,"rule has NO alignment")]:
    s = r[r["has_align"]==flag]
    if len(s):
        print("  %-22s n=%4d  hold_rate=%.0f%%  mean_OOS_lift=%+.2fp  mean_test_wr=%.2f"
              % (lab, len(s), 100*s["holds"].mean(), (s["rule_test"]-s["base_test"]).mean(), s["rule_test_wr"].mean()))
r.to_csv("data/lab_training/oos_signature_validation.csv", index=False)
print("\nWROTE data/lab_training/oos_signature_validation.csv")
