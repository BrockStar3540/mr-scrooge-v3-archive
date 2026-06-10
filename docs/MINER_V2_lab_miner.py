"""ML LAB v2 matrix-miner — UPDATED for current config (2026-06-10). PURE ANALYSIS, never
touches the live bot. Reads scored_7yr.parquet (net_ladder + alignv + 14 direction-aware
buckets), scoped to the live 4 pairs x 21 strats. Keys DIRECTION x ALIGN x AMP-bucket like
the live direction-keyed playbook. Scores on net_ladder (the green-exit ladder), not the old
SL10/TP12. Frames opportunities against the CURRENT gates (per-strategy floor + align_min=0 +
the +1.25 net EV floor + the htf-misalign gate), NOT the retired align_min=4.
Outputs: miner_map_v2.csv (full cells), miner_opportunities_v2.csv (+EV cells the config
excludes), miner_floorband_v2.csv (net-positive cells starved by the +1.25 EV floor)."""
import pandas as pd, numpy as np, os
SRC=os.environ.get("SRC","/Users/brock-mini-mac/scored_7yr.parquet")
OUT=os.environ.get("OUT","/Users/brock-mini-mac/miner_v2"); os.makedirs(OUT,exist_ok=True)
MINN=int(os.environ.get("MINN","40")); EV_FLOOR=1.25
# current live amp map: strategy -> (amp_factor, per-strategy align floor)
META={"BR2_vcb_short":("ADR",2),"BR3_inside_bar_short":("ADR",3),"CP1_coil_breakout_short":("ADR",1),
"CP2_squeeze_momentum_long":("ADR",2),"CP3_vol_coil_fade_long":("ADR",3),"CP3_vol_coil_fade_short":("ADR",2),
"MR2_bb_reversion_short":("ADR",2),"MR4_zscore_extreme_long":("ADR",2),"MR4_zscore_extreme_short":("ADR",2),
"MR5_williams_extreme_short":("ADR",2),"RG1_range_bound_scalp_long":("ADR",2),"RG1_range_bound_scalp_short":("ADR",2),
"TF2_pullback_EMA20_short":("RSI",0),"alpha_breakout_retest_v2":("RSI",2),"alpha_extended_fade_v2":("E50",1),
"alpha_pullback_v2":("RSI",2),"bravo_expansion_continuation":("RSI",2),"bravo_failed_momentum":("RSI",3),
"charlie_compression_breakout":("ADR",2),"delta_tag_and_go_v2":("ADR",2),"echo_box_fade_v2":("RSI",3)}
df=pd.read_parquet(SRC)
print("scored corpus: n=%d strategies=%d pairs=%s span ladder-EV=%+.3f"%(
  len(df),df["strategy"].nunique(),sorted(df["pair"].unique()),df["net_ladder"].mean()))
rows=[]
for strat,(amp,floor) in META.items():
    sub=df[df["strategy"]==strat]
    if not len(sub): continue
    for pair in sorted(df["pair"].unique()):
        for d in ("long","short"):
            sd=sub[(sub["pair"]==pair)&(sub["direction"]==d)]
            for al in range(5):
                sa=sd[sd["alignv"]==al]
                if len(sa)<MINN: continue
                ev=round(sa["net_ladder"].mean(),3)
                rows.append([pair,strat,d,al,"spine","",len(sa),ev,round(100*(sa["net_ladder"]>0).mean(),1),amp,floor,al>=floor])
                if amp in sa.columns:
                    for b,g in sa.groupby(amp):
                        if len(g)<MINN: continue
                        rows.append([pair,strat,d,al,"amp",str(b),len(g),round(g["net_ladder"].mean(),3),round(100*(g["net_ladder"]>0).mean(),1),amp,floor,al>=floor])
cells=pd.DataFrame(rows,columns=["pair","strategy","direction","align","tier","bucket","n","ev_net_ladder","wr","amp_factor","floor","in_playbook"])
cells.to_csv(f"{OUT}/miner_map_v2.csv",index=False)
sp=cells[cells["tier"]=="spine"]
# OPPORTUNITIES: strong +EV spine cells BELOW the per-strategy floor (config excludes them)
opp=sp[(sp["ev_net_ladder"]>=1.0)&(~sp["in_playbook"])&(sp["n"]>=60)].sort_values("ev_net_ladder",ascending=False)
opp.to_csv(f"{OUT}/miner_opportunities_v2.csv",index=False)
# FLOOR-BAND: in-playbook cells net-positive but under the +1.25 live EV floor (starved by the floor)
band=sp[(sp["ev_net_ladder"]>0)&(sp["ev_net_ladder"]<EV_FLOOR)&(sp["in_playbook"])&(sp["n"]>=60)].sort_values("ev_net_ladder",ascending=False)
band.to_csv(f"{OUT}/miner_floorband_v2.csv",index=False)
print("\nMINER MAP: %d cells (%d spine / %d amp) -> %s/"%(len(cells),len(sp),(cells["tier"]=="amp").sum(),OUT))
print("\n=== OPPORTUNITIES — +EV (>=1.0p net_ladder) cells BELOW the per-strategy floor (the bot can't reach them) ===")
print("count: %d  | total trade-vol: %d"%(len(opp),opp["n"].sum()))
print(opp.head(12)[["pair","strategy","direction","align","n","ev_net_ladder","wr","floor"]].to_string(index=False))
print("\n=== FLOOR-BAND — net-positive cells starved by the +1.25 EV floor (lower-floor candidates) ===")
print("count: %d  | total vol: %d  | mean EV %+.2fp"%(len(band),band["n"].sum(),band["ev_net_ladder"].mean() if len(band) else 0))
print(band.head(8)[["pair","strategy","direction","align","n","ev_net_ladder"]].to_string(index=False))
