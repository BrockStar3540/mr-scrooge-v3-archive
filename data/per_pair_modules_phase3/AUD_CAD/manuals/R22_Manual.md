# AUD_CAD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,035**  (W=1,861 / L=1,174)  -  WR: **61.3%**

## Session distribution

- asia: n=783  W=469/L=314  WR=59.9%
- ny_mid: n=688  W=427/L=261  WR=62.1%
- ny_close: n=434  W=269/L=165  WR=62.0%
- ny_open: n=379  W=213/L=166  WR=56.2%
- london_open: n=371  W=237/L=134  WR=63.9%
- asia_late: n=195  W=127/L=68  WR=65.1%
- london: n=122  W=83/L=39  WR=68.0%
- off_hours: n=63  W=36/L=27  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=167  W=144/L=23  WR=86.2%
- Refine: exclude H20=H20b drops 6/23 losers (26%)
- **Final: n=149  W=132/L=17  WR=88.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W02.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude BBP=BBP6 drops 11/17 losers (65%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W03.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude BBP=BBP6 drops 11/17 losers (65%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W04.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude BBP=BBP6 drops 11/17 losers (65%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W05.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=112  W=100/L=12  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 11/12 losers (92%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W06.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=112  W=100/L=12  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 11/12 losers (92%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W07.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP6 drops 7/12 losers (58%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W08.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude ZS=ZS2 drops 5/8 losers (62%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W09.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude ZS=ZS2 drops 5/8 losers (62%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W10.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude ZS=ZS2 drops 5/8 losers (62%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  AVOID when zscore -2 to -1 oversold

### W11.  `H60=H60e AND T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W12.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W13.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude session_bucket=ny_mid drops 5/6 losers (83%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W14.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude session_bucket=ny_mid drops 5/5 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W15.  `H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W16.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W17.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W18.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W19.  `H60=H60a AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W20.  `T1=T1a AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W21.  `H20=H20b AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 3/8 losers (38%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; session=asia  •  AVOID when strategy=alpha_breakout_retest_v2

### W22.  `H20=H20b AND H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 3/8 losers (38%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when strategy=alpha_breakout_retest_v2

### W23.  `H20=H20b AND T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 3/8 losers (38%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; upper third; session=asia  •  AVOID when strategy=alpha_breakout_retest_v2

### W24.  `H20=H20b AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 3/8 losers (38%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third; session=asia  •  AVOID when strategy=alpha_breakout_retest_v2

### W25.  `H20=H20b AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 3/8 losers (38%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; upper third; session=asia  •  AVOID when strategy=alpha_breakout_retest_v2

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=253  W=101/L=152  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=253  W=101/L=152  WR=39.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong

### L02.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=253  W=101/L=152  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=253  W=101/L=152  WR=39.9%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong

### L03.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=253  W=101/L=152  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=253  W=101/L=152  WR=39.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong

### L04.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=247  W=97/L=150  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=247  W=97/L=150  WR=39.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 60-70 strong

### L05.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=247  W=97/L=150  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=247  W=97/L=150  WR=39.3%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 60-70 strong

### L06.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=225  W=90/L=135  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=90/L=135  WR=40.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought

### L07.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=225  W=90/L=135  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=90/L=135  WR=40.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought

### L08.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=225  W=90/L=135  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=90/L=135  WR=40.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought

### L09.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=225  W=90/L=135  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=90/L=135  WR=40.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought

### L10.  `BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=225  W=90/L=135  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=225  W=90/L=135  WR=40.0%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; zscore +1 to +2 overbought

### L11.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=220  W=86/L=134  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=220  W=86/L=134  WR=39.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought

### L12.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=220  W=86/L=134  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=220  W=86/L=134  WR=39.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought

### L13.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=192  W=76/L=116  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=192  W=76/L=116  WR=39.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong

### L14.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=192  W=76/L=116  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=192  W=76/L=116  WR=39.6%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 60-70 strong

### L15.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=186  W=72/L=114  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=186  W=72/L=114  WR=38.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong

### L16.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/100 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L17.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/100 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L18.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=164  W=65/L=99  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (23/99 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when session=asia

### L19.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=161  W=62/L=99  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_open (28/99 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L20.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=147  W=58/L=89  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (19/89 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=asia

### L21.  `H60=H60e AND T1=T1c AND RSI=RSI7`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (34/88 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when deep above upper band

### L22.  `H60=H60e AND T4=T4c AND RSI=RSI7`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (34/88 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when deep above upper band

### L23.  `H60=H60e AND RSI=RSI7 AND direction_exec=short`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (34/88 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI>80 extreme overbought  •  ONLY when deep above upper band

### L24.  `T1=T1c AND T4=T4c AND RSI=RSI7`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (34/88 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when deep above upper band

### L25.  `T1=T1c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (34/88 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(13/19) |
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
