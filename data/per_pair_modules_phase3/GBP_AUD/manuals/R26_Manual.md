# GBP_AUD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **4,857**  (W=2,791 / L=2,066)  -  WR: **57.5%**

## Session distribution

- asia: n=1370  W=793/L=577  WR=57.9%
- ny_open: n=726  W=422/L=304  WR=58.1%
- ny_mid: n=691  W=353/L=338  WR=51.1%
- london: n=610  W=369/L=241  WR=60.5%
- ny_close: n=604  W=363/L=241  WR=60.1%
- london_open: n=549  W=308/L=241  WR=56.1%
- asia_late: n=217  W=136/L=81  WR=62.7%
- off_hours: n=90  W=47/L=43  WR=52.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude H20=H20b drops 4/12 losers (33%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 slightly aligned

### W02.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W03.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W04.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W05.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=london_open drops 7/10 losers (70%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W06.  `H20=H20b AND T4=T4a AND session_bucket=ny_open`
- Raw: n=66  W=60/L=6  WR=90.9%
- Refine: exclude BBP=BBP1 drops 2/6 losers (33%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W07.  `H20=H20b AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=66  W=60/L=6  WR=90.9%
- Refine: exclude BBP=BBP1 drops 2/6 losers (33%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 40-50 lower neutral; session=ny_open  •  AVOID when just touched lower band

### W08.  `H20=H20b AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=66  W=60/L=6  WR=90.9%
- Refine: exclude BBP=BBP1 drops 2/6 losers (33%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when just touched lower band

### W09.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia_late drops 4/6 losers (67%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=asia_late

### W10.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 7/7 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W11.  `T1=T1a AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 7/7 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W12.  `H20=H20a AND T1=T1a AND strategy_id=TF2_pullback_EMA20_long`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude RSI=RSI4 drops 5/9 losers (56%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; strategy=TF2_pullback_EMA20_long  •  AVOID when RSI 50-60 upper neutral

### W13.  `H20=H20e AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W14.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W15.  `H20=H20a AND H60=H60a AND T1=T1a AND strategy_id=TF2_pullback_EMA20_long`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude RSI=RSI4 drops 4/8 losers (50%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; strategy=TF2_pullback_EMA20_long  •  AVOID when RSI 50-60 upper neutral

### W16.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude T1=T1c drops 4/8 losers (50%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when 1h trend AGAINST trade

### W17.  `H20=H20a AND T1=T1a AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude RSI=RSI4 drops 4/8 losers (50%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; strategy=TF2_pullback_EMA20_long  •  AVOID when RSI 50-60 upper neutral

### W18.  `H20=H20a AND RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude T1=T1c drops 4/8 losers (50%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W20.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W21.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W22.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W23.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W24.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W25.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=55  W=51/L=4  WR=92.7%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=229  W=83/L=146  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (56/146 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L02.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=229  W=83/L=146  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (56/146 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L03.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=229  W=83/L=146  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (56/146 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L04.  `H60=H60e AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=229  W=83/L=146  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (56/146 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L05.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=229  W=83/L=146  WR=36.2%
- Sharpen: sharpest is session_bucket=asia (56/146 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L06.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=219  W=83/L=136  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=83/L=136  WR=37.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid

### L07.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=219  W=83/L=136  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=83/L=136  WR=37.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid

### L08.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=219  W=83/L=136  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=83/L=136  WR=37.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid

### L09.  `H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=201  W=69/L=132  WR=34.3%
- Sharpen: sharpest is H20=H20e (98/132 of losers there)
- **Sharp: n=138  W=40/L=98  WR=29.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L10.  `T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=201  W=69/L=132  WR=34.3%
- Sharpen: sharpest is H20=H20e (98/132 of losers there)
- **Sharp: n=138  W=40/L=98  WR=29.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=201  W=69/L=132  WR=34.3%
- Sharpen: sharpest is H20=H20e (98/132 of losers there)
- **Sharp: n=138  W=40/L=98  WR=29.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=201  W=69/L=132  WR=34.3%
- Sharpen: sharpest is H20=H20e (98/132 of losers there)
- **Sharp: n=138  W=40/L=98  WR=29.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L13.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=201  W=69/L=132  WR=34.3%
- Sharpen: sharpest is H20=H20e (98/132 of losers there)
- **Sharp: n=138  W=40/L=98  WR=29.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L14.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=194  W=77/L=117  WR=39.7%
- Sharpen: sharpest is ZS=ZS4 (98/117 of losers there)
- **Sharp: n=138  W=40/L=98  WR=29.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L15.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=194  W=77/L=117  WR=39.7%
- Sharpen: sharpest is ZS=ZS4 (98/117 of losers there)
- **Sharp: n=138  W=40/L=98  WR=29.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L16.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=181  W=64/L=117  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=181  W=64/L=117  WR=35.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought

### L17.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=181  W=64/L=117  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=181  W=64/L=117  WR=35.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought

### L18.  `H20=H20a AND T4=T4c AND ZS=ZS2`
- Raw: n=175  W=69/L=106  WR=39.4%
- Sharpen: sharpest is T1=T1a (61/106 of losers there)
- **Sharp: n=89  W=28/L=61  WR=31.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L19.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=175  W=69/L=106  WR=39.4%
- Sharpen: sharpest is T1=T1a (61/106 of losers there)
- **Sharp: n=89  W=28/L=61  WR=31.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L20.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=172  W=60/L=112  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (45/112 of losers there)
- **Sharp: n=54  W=9/L=45  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L21.  `H20=H20e AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=172  W=60/L=112  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (45/112 of losers there)
- **Sharp: n=54  W=9/L=45  WR=16.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L22.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=161  W=58/L=103  WR=36.0%
- Sharpen: sharpest is H20=H20e (72/103 of losers there)
- **Sharp: n=101  W=29/L=72  WR=28.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=161  W=58/L=103  WR=36.0%
- Sharpen: sharpest is H20=H20e (72/103 of losers there)
- **Sharp: n=101  W=29/L=72  WR=28.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L24.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=160  W=53/L=107  WR=33.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=53/L=107  WR=33.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought

### L25.  `T1=T1c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=160  W=53/L=107  WR=33.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=53/L=107  WR=33.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
