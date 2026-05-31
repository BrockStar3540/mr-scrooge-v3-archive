# NZD_USD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,212**  (W=1,386 / L=826)  -  WR: **62.7%**

## Session distribution

- ny_mid: n=709  W=454/L=255  WR=64.0%
- asia: n=408  W=266/L=142  WR=65.2%
- ny_close: n=296  W=176/L=120  WR=59.5%
- ny_open: n=278  W=166/L=112  WR=59.7%
- london: n=260  W=164/L=96  WR=63.1%
- london_open: n=184  W=113/L=71  WR=61.4%
- off_hours: n=42  W=27/L=15  WR=64.3%
- asia_late: n=35  W=20/L=15  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=288  W=245/L=43  WR=85.1%
- Refine: exclude session_bucket=asia_late drops 9/43 losers (21%)
- **Final: n=279  W=245/L=34  WR=87.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third  •  AVOID when session=asia_late

### W02.  `H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=276  W=238/L=38  WR=86.2%
- Refine: exclude RSI=RSI3 drops 8/38 losers (21%)
- **Final: n=268  W=238/L=30  WR=88.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W03.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=276  W=238/L=38  WR=86.2%
- Refine: exclude RSI=RSI3 drops 8/38 losers (21%)
- **Final: n=268  W=238/L=30  WR=88.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W04.  `H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=251  W=216/L=35  WR=86.1%
- Refine: exclude session_bucket=asia_late drops 9/35 losers (26%)
- **Final: n=242  W=216/L=26  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=asia_late

### W05.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=245  W=211/L=34  WR=86.1%
- Refine: exclude session_bucket=asia_late drops 9/34 losers (26%)
- **Final: n=236  W=211/L=25  WR=89.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=asia_late

### W06.  `H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=237  W=207/L=30  WR=87.3%
- Refine: exclude H20=H20d drops 8/30 losers (27%)
- **Final: n=214  W=192/L=22  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W07.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=237  W=207/L=30  WR=87.3%
- Refine: exclude H20=H20d drops 8/30 losers (27%)
- **Final: n=214  W=192/L=22  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W08.  `H60=H60a AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=233  W=204/L=29  WR=87.6%
- Refine: exclude H20=H20d drops 8/29 losers (28%)
- **Final: n=210  W=189/L=21  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W09.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=229  W=204/L=25  WR=89.1%
- Refine: exclude session_bucket=asia_late drops 9/25 losers (36%)
- **Final: n=220  W=204/L=16  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W10.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=216  W=186/L=30  WR=86.1%
- Refine: exclude session_bucket=asia_late drops 9/30 losers (30%)
- **Final: n=207  W=186/L=21  WR=89.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=asia_late

### W11.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=213  W=183/L=30  WR=85.9%
- Refine: exclude H20=H20d drops 14/30 losers (47%)
- **Final: n=190  W=174/L=16  WR=91.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W12.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=213  W=183/L=30  WR=85.9%
- Refine: exclude H20=H20d drops 14/30 losers (47%)
- **Final: n=190  W=174/L=16  WR=91.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W13.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=213  W=183/L=30  WR=85.9%
- Refine: exclude H20=H20d drops 14/30 losers (47%)
- **Final: n=190  W=174/L=16  WR=91.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W14.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=208  W=188/L=20  WR=90.4%
- Refine: exclude session_bucket=asia_late drops 5/20 losers (25%)
- **Final: n=203  W=188/L=15  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W15.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=208  W=188/L=20  WR=90.4%
- Refine: exclude session_bucket=asia_late drops 5/20 losers (25%)
- **Final: n=203  W=188/L=15  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W16.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=206  W=181/L=25  WR=87.9%
- Refine: exclude RSI=RSI3 drops 6/25 losers (24%)
- **Final: n=200  W=181/L=19  WR=90.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W17.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=187  W=164/L=23  WR=87.7%
- Refine: exclude session_bucket=asia_late drops 9/23 losers (39%)
- **Final: n=178  W=164/L=14  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=asia_late

### W18.  `H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=184  W=167/L=17  WR=90.8%
- Refine: exclude ZS=ZS2 drops 9/17 losers (53%)
- **Final: n=167  W=159/L=8  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W19.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=175  W=157/L=18  WR=89.7%
- Refine: exclude session_bucket=asia_late drops 5/18 losers (28%)
- **Final: n=170  W=157/L=13  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W20.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=172  W=149/L=23  WR=86.6%
- Refine: exclude session_bucket=asia_late drops 9/23 losers (39%)
- **Final: n=163  W=149/L=14  WR=91.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W21.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude session_bucket=asia_late drops 5/18 losers (28%)
- **Final: n=158  W=145/L=13  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W22.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=160  W=146/L=14  WR=91.2%
- Refine: exclude H20=H20d drops 10/14 losers (71%)
- **Final: n=141  W=137/L=4  WR=97.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W23.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=160  W=146/L=14  WR=91.2%
- Refine: exclude H20=H20d drops 10/14 losers (71%)
- **Final: n=141  W=137/L=4  WR=97.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W24.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=157  W=144/L=13  WR=91.7%
- Refine: exclude H20=H20d drops 9/13 losers (69%)
- **Final: n=139  W=135/L=4  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

### W25.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=157  W=144/L=13  WR=91.7%
- Refine: exclude H20=H20d drops 9/13 losers (69%)
- **Final: n=139  W=135/L=4  WR=97.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=200  W=76/L=124  WR=38.0%
- Sharpen: sharpest is T1=T1a (50/124 of losers there)
- **Sharp: n=61  W=11/L=50  WR=18.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when 1h trend WITH trade

### L02.  `H60=H60e AND T1=T1c AND BBP=BBP4`
- Raw: n=196  W=74/L=122  WR=37.8%
- Sharpen: sharpest is RSI=RSI5 (58/122 of losers there)
- **Sharp: n=72  W=14/L=58  WR=19.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when RSI 60-70 strong

### L03.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=190  W=74/L=116  WR=38.9%
- Sharpen: sharpest is RSI=RSI5 (54/116 of losers there)
- **Sharp: n=68  W=14/L=54  WR=20.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when RSI 60-70 strong

### L04.  `H60=H60e AND T1=T1c AND ZS=ZS4`
- Raw: n=184  W=66/L=118  WR=35.9%
- Sharpen: sharpest is RSI=RSI5 (57/118 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=184  W=66/L=118  WR=35.9%
- Sharpen: sharpest is RSI=RSI5 (57/118 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L06.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=179  W=66/L=113  WR=36.9%
- Sharpen: sharpest is RSI=RSI5 (53/113 of losers there)
- **Sharp: n=67  W=14/L=53  WR=20.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L07.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=178  W=60/L=118  WR=33.7%
- Sharpen: sharpest is session_bucket=london (46/118 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when session=london

### L08.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=175  W=58/L=117  WR=33.1%
- Sharpen: sharpest is session_bucket=london (46/117 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london

### L09.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=175  W=58/L=117  WR=33.1%
- Sharpen: sharpest is session_bucket=london (46/117 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london

### L10.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=175  W=62/L=113  WR=35.4%
- Sharpen: sharpest is H60=H60e (67/113 of losers there)
- **Sharp: n=74  W=7/L=67  WR=9.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L11.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=174  W=60/L=114  WR=34.5%
- Sharpen: sharpest is session_bucket=london (46/114 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong  •  ONLY when session=london

### L12.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=174  W=60/L=114  WR=34.5%
- Sharpen: sharpest is session_bucket=london (46/114 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when session=london

### L13.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=171  W=58/L=113  WR=33.9%
- Sharpen: sharpest is session_bucket=london (46/113 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london

### L14.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=171  W=58/L=113  WR=33.9%
- Sharpen: sharpest is session_bucket=london (46/113 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london

### L15.  `BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=171  W=58/L=113  WR=33.9%
- Sharpen: sharpest is session_bucket=london (46/113 of losers there)
- **Sharp: n=52  W=6/L=46  WR=11.5%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london

### L16.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=171  W=62/L=109  WR=36.3%
- Sharpen: sharpest is H60=H60e (63/109 of losers there)
- **Sharp: n=70  W=7/L=63  WR=10.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=171  W=62/L=109  WR=36.3%
- Sharpen: sharpest is H60=H60e (63/109 of losers there)
- **Sharp: n=70  W=7/L=63  WR=10.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=164  W=64/L=100  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (45/100 of losers there)
- **Sharp: n=48  W=3/L=45  WR=6.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L19.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is T4=T4c (39/96 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is T4=T4c (39/96 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=152  W=57/L=95  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (50/95 of losers there)
- **Sharp: n=53  W=3/L=50  WR=5.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20a AND H60=H60e AND RSI=RSI4`
- Raw: n=149  W=56/L=93  WR=37.6%
- Sharpen: sharpest is T1=T1a (50/93 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L23.  `H60=H60e AND T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=142  W=49/L=93  WR=34.5%
- Sharpen: sharpest is RSI=RSI5 (49/93 of losers there)
- **Sharp: n=52  W=3/L=49  WR=5.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L24.  `H60=H60e AND T4=T4c AND RSI=RSI4`
- Raw: n=139  W=54/L=85  WR=38.8%
- Sharpen: sharpest is BBP=BBP4 (42/85 of losers there)
- **Sharp: n=55  W=13/L=42  WR=23.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L25.  `H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=135  W=44/L=91  WR=32.6%
- Sharpen: sharpest is direction_exec=short (49/91 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when short

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(14/5) | H20d(6/13) |
| H60 | H60a(57/36) | H60e(35/55) |
| T1 | T1a(54/43) | T1c(46/57) |
| T4 | T4c(55/47) | T4a(45/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/41) | short(45/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
