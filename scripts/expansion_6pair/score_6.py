"""Score the extended (2019-2026) sig_corpus: compute ladder + SL/TP net per trade from the 7yr M5,
under BOTH fixed spread (comparable to prior gate) AND vol-scaled spread (realistic crisis — flag 3).
Reuses the validated ladder/SLTP sims. Output: scored parquet for regime_gate.py.
Usage: python3 score_extended.py <extended_sig_corpus.csv.gz> <out_scored.parquet>
vol-scaled spread = base*1.25 * clip(ATR14_at_entry / ATR14_baseline, 1, 10); calm->~fixed, 2020->wide."""
import sys, glob, warnings, numpy as np, pandas as pd
warnings.filterwarnings("ignore")
CORPUS=sys.argv[1]; OUT=sys.argv[2]
CACHE="/Volumes/Alien Device/mr-scrooge-v3/research/replay_lab/cache"
SPREAD={"AUD_USD":1.5,"EUR_USD":1.2,"GBP_USD":1.6,"USD_CAD":1.8,"USD_JPY":1.0,"USD_CHF":1.5,"NZD_USD":1.8,"EUR_JPY":1.5,"AUD_JPY":1.5,"EUR_GBP":1.5}; SMULT=1.25   # MATCHES prior gate (continuity w/ +3.09p), NOT the generator's internal pnl spread
P1=48; P2MAX=288; SL0=-10.0; SL_LOCK=6.0; TP1=12.0; TP2=20.0; TP3=30.0; W1,W2,W3=0.5,0.25,0.25
HARVEST_MIN=7.0; P2_LIMIT=7.5; H=48; SL=-10.0; TP=12.0; VS_CAP=10.0
def sim_ladder(fav,adv,clo,n):
    rem=1.0; sl=SL0; t1=t2=t3=False; rz=0.0
    for b in range(min(P1,n)):
        a,f=adv[b],fav[b]
        if a<=sl: return rz+rem*sl
        if (not t1) and f>=TP1: rz+=W1*TP1; rem-=W1; t1=True; sl=SL_LOCK
        if (not t2) and f>=TP2: rz+=W2*TP2; rem-=W2; t2=True
        if (not t3) and f>=TP3: rz+=W3*TP3; rem-=W3; t3=True
        if rem<=1e-9: return rz
    cb=min(P1-1,n-1); mark=clo[cb]
    if mark>=HARVEST_MIN: return rz+rem*(mark+0.5)
    for b in range(P1,min(P2MAX,n)):
        a,f=adv[b],fav[b]
        if a<=sl: return rz+rem*sl
        if f>=P2_LIMIT: return rz+rem*P2_LIMIT
    cb=min(P2MAX-1,n-1); return rz+rem*clo[cb]
def sim_sltp(fav,adv,clo,n):
    for b in range(min(H,n)):
        if adv[b]<=SL: return SL
        if fav[b]>=TP: return TP
    cb=min(H-1,n-1); return clo[cb]
def atr14(H_,L_,C_):
    pc=np.roll(C_,1); pc[0]=C_[0]
    tr=np.maximum(H_-L_, np.maximum(np.abs(H_-pc), np.abs(L_-pc)))
    return pd.Series(tr).rolling(14,min_periods=1).mean().values
df=pd.read_csv(CORPUS)
df["et"]=pd.to_datetime(df["entry_time"],utc=True).dt.tz_localize(None).values.astype("datetime64[ns]").astype("int64")
al=(df.H20.isin(["H20a","H20b"]).astype(int)+df.H60.isin(["H60a","H60b"]).astype(int)+df.T1.eq("T1a").astype(int)+df.T4.eq("T4a").astype(int))
df["alignv"]=al
for c in ("net_ladder","net_ladder_vs","net_sltp"): df[c]=np.nan
def load(p):
    f=glob.glob(f"{CACHE}/{p}_M5_20190701_*.parquet")[0]; d=pd.read_parquet(f).sort_index()
    return (d.index.values.astype("datetime64[ns]").astype("int64"),d["Open"].values,d["High"].values,d["Low"].values,d["Close"].values)
for pair,g in df.groupby("pair"):
    t,O,Hh,L,C=load(pair); pip=0.01 if "JPY" in pair else 0.0001
    base=SPREAD.get(pair,2.0)*SMULT
    atr=atr14(Hh,L,C); atr_base=np.nanmedian(atr)   # full-series baseline
    idx=np.searchsorted(t,g["et"].values,side="left"); gi=g.index.values; lng=(g["direction"].values=="long"); last=len(t)-1
    for k in range(len(gi)):
        ii=idx[k]
        if ii>=last: continue
        e=O[ii]; n=min(P2MAX,last-ii)
        if n<2: continue
        s=slice(ii,ii+n)
        if lng[k]: favR=(Hh[s]-e)/pip; advR=(L[s]-e)/pip; cloR=(C[s]-e)/pip
        else: favR=(e-L[s])/pip; advR=(e-Hh[s])/pip; cloR=(e-C[s])/pip
        mult=min(max(atr[ii]/atr_base if atr_base>0 else 1.0,1.0),VS_CAP); spv=base*mult
        df.at[gi[k],"net_ladder"]=sim_ladder(favR-base,advR-base,cloR-base,n)
        df.at[gi[k],"net_ladder_vs"]=sim_ladder(favR-spv,advR-spv,cloR-spv,n)
        df.at[gi[k],"net_sltp"]=sim_sltp(favR-base,advR-base,cloR-base,n)
df=df.dropna(subset=["net_ladder"]).reset_index(drop=True)
df["win"]=(df.net_sltp>0).astype(int)
df.to_parquet(OUT)
yr=pd.to_datetime(df["et"]).dt.year
print("scored n=%d -> %s"%(len(df),OUT))
print("fixed vs vol-scaled ladder EV by year (divergence = spread-sensitive year):")
print(df.assign(year=yr).groupby("year").agg(n=("net_ladder","size"),fixed=("net_ladder","mean"),volscaled=("net_ladder_vs","mean")).round(3).to_string())
