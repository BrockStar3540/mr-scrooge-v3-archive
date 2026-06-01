"""Widened OOS validation: graded ALIGNMENT (H20/H60/T1/T4), huge-n simple rules.

Alignment codes (from factor_buckets):
  H20/H60: a/b = aligned, c = neutral, d/e = counter
  T1/T4  : a = aligned, c = counter
align_score = # of the 4 factors that are aligned (0..4).
Train = trades <= 70th pct entry_time; Test = held-out latest 30%.
"""
import pandas as pd, numpy as np

df = pd.read_csv("/tmp/sig_corpus_phase3.csv.gz")
df["entry_time"] = pd.to_datetime(df["entry_time"], utc=True, errors="coerce")
df = df.dropna(subset=["entry_time"]).sort_values("entry_time").reset_index(drop=True)
cut = df["entry_time"].quantile(0.70)
df["split"] = np.where(df["entry_time"] <= cut, "train", "test")
df["win"] = (df["pnl_pips"] > 0).astype(int)

al_H20 = df["H20"].isin(["H20a","H20b"])
al_H60 = df["H60"].isin(["H60a","H60b"])
al_T1  = df["T1"].eq("T1a")
al_T4  = df["T4"].eq("T4a")
df["align_score"] = (al_H20.astype(int)+al_H60.astype(int)+al_T1.astype(int)+al_T4.astype(int))
te = df[df.split=="test"]; tr = df[df.split=="train"]
print("trades=%d train=%d test=%d  cut=%s  overall test mean=%.2fp WR=%.1f%%"
      % (len(df), len(tr), len(te), cut.date(), te.pnl_pips.mean(), 100*te.win.mean()))

print("\n=== (A) mean_pip & WR by align_score (TRAIN vs HELD-OUT TEST) ===")
print("score |  train_n  tr_pip  tr_wr |  test_n  te_pip  te_wr")
for s in range(5):
    a=tr[tr.align_score==s]; b=te[te.align_score==s]
    if len(a) and len(b):
        print("  %d   | %8d %+6.2f  %4.1f%% | %7d %+6.2f  %4.1f%%"
              % (s, len(a), a.pnl_pips.mean(), 100*a.win.mean(), len(b), b.pnl_pips.mean(), 100*b.win.mean()))

print("\n=== (B) ENFORCEMENT trade-off: require align_score >= K (held-out) ===")
base_pip=te.pnl_pips.mean(); base_n=len(te)
print("threshold | kept_vol | te_pip   te_wr   pip_lift_vs_all")
for k in range(0,5):
    s=te[te.align_score>=k]
    if len(s):
        print("  >=%d      |  %4.1f%%   | %+6.2f  %4.1f%%   %+5.2f"
              % (k, 100*len(s)/base_n, s.pnl_pips.mean(), 100*s.win.mean(), s.pnl_pips.mean()-base_pip))

print("\n=== (C) per-cell consistency (held-out): aligned(score>=2) vs counter(score<=1) ===")
df["k"]=df[["pair","strategy","direction","session"]].astype(str).agg("|".join,axis=1)
te2=df[df.split=="test"]
better=0; total=0; lifts=[]
for k,g in te2.groupby("k"):
    hi=g[g.align_score>=2]; lo=g[g.align_score<=1]
    if len(hi)>=15 and len(lo)>=15:
        total+=1; d=hi.pnl_pips.mean()-lo.pnl_pips.mean(); lifts.append(d)
        if d>0: better+=1
print("  cells with enough hi+lo support: %d" % total)
if total: print("  aligned beats counter in %d (%.0f%%) of cells | median per-cell lift %+.2fp"
                % (better, 100*better/total, float(np.median(lifts))))

print("\n=== (D) direction split (held-out): aligned vs counter ===")
for d in ["long","short"]:
    g=te[te.direction==d]
    hi=g[g.align_score>=2]; lo=g[g.align_score<=1]
    if len(hi) and len(lo):
        print("  %-5s | aligned %+5.2fp WR%4.1f%% (n=%d)  vs  counter %+5.2fp WR%4.1f%% (n=%d)  lift %+5.2fp"
              % (d, hi.pnl_pips.mean(),100*hi.win.mean(),len(hi), lo.pnl_pips.mean(),100*lo.win.mean(),len(lo),
                 hi.pnl_pips.mean()-lo.pnl_pips.mean()))

print("\n=== (E) single-factor strength (held-out): aligned vs counter per factor ===")
defs={"H20":(["H20a","H20b"],["H20d","H20e"]),"H60":(["H60a","H60b"],["H60d","H60e"]),
      "T1":(["T1a"],["T1c"]),"T4":(["T4a"],["T4c"])}
for f,(al,co) in defs.items():
    a=te[te[f].isin(al)]; c=te[te[f].isin(co)]
    if len(a) and len(c):
        print("  %-4s aligned %+5.2fp WR%4.1f%% (n=%d) | counter %+5.2fp WR%4.1f%% (n=%d) | lift %+5.2fp"
              % (f, a.pnl_pips.mean(),100*a.win.mean(),len(a), c.pnl_pips.mean(),100*c.win.mean(),len(c),
                 a.pnl_pips.mean()-c.pnl_pips.mean()))
