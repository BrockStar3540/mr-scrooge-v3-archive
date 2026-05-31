# AUD_NZD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,212**  (W=1,411 / L=801)  -  WR: **63.8%**

## Session distribution

- asia: n=778  W=492/L=286  WR=63.2%
- ny_mid: n=444  W=287/L=157  WR=64.6%
- london_open: n=366  W=229/L=137  WR=62.6%
- ny_open: n=196  W=126/L=70  WR=64.3%
- ny_close: n=172  W=106/L=66  WR=61.6%
- london: n=153  W=105/L=48  WR=68.6%
- asia_late: n=89  W=57/L=32  WR=64.0%
- off_hours: n=14  W=9/L=5  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND ZS=ZS3`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude session_bucket=asia_late drops 8/28 losers (29%)
- **Final: n=187  W=167/L=20  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W02.  `T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude session_bucket=asia_late drops 8/28 losers (29%)
- **Final: n=187  W=167/L=20  WR=89.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W03.  `T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude session_bucket=asia_late drops 8/28 losers (29%)
- **Final: n=187  W=167/L=20  WR=89.3%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W04.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude session_bucket=asia_late drops 8/28 losers (29%)
- **Final: n=187  W=167/L=20  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W05.  `H60=H60a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude session_bucket=asia_late drops 8/28 losers (29%)
- **Final: n=187  W=167/L=20  WR=89.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W06.  `T1=T1a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=199  W=171/L=28  WR=85.9%
- Refine: exclude session_bucket=asia_late drops 8/28 losers (29%)
- **Final: n=187  W=167/L=20  WR=89.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W07.  `H20=H20a AND H60=H60a AND ZS=ZS3`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 8/26 losers (31%)
- **Final: n=183  W=165/L=18  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W08.  `H20=H20a AND T1=T1a AND ZS=ZS3`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 8/26 losers (31%)
- **Final: n=183  W=165/L=18  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W09.  `H20=H20a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 8/26 losers (31%)
- **Final: n=183  W=165/L=18  WR=90.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W10.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS3`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 8/26 losers (31%)
- **Final: n=183  W=165/L=18  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W11.  `H20=H20a AND H60=H60a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 8/26 losers (31%)
- **Final: n=183  W=165/L=18  WR=90.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W12.  `H20=H20a AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=195  W=169/L=26  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 8/26 losers (31%)
- **Final: n=183  W=165/L=18  WR=90.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W13.  `H20=H20a AND T4=T4a AND ZS=ZS3`
- Raw: n=193  W=169/L=24  WR=87.6%
- Refine: exclude session_bucket=asia_late drops 8/24 losers (33%)
- **Final: n=181  W=165/L=16  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W14.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS3`
- Raw: n=193  W=169/L=24  WR=87.6%
- Refine: exclude session_bucket=asia_late drops 8/24 losers (33%)
- **Final: n=181  W=165/L=16  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W15.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=193  W=169/L=24  WR=87.6%
- Refine: exclude session_bucket=asia_late drops 8/24 losers (33%)
- **Final: n=181  W=165/L=16  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W16.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=193  W=169/L=24  WR=87.6%
- Refine: exclude session_bucket=asia_late drops 8/24 losers (33%)
- **Final: n=181  W=165/L=16  WR=91.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia_late

### W17.  `T4=T4a AND RSI=RSI6 AND ZS=ZS3`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude BBP=BBP4 drops 13/19 losers (68%)
- **Final: n=98  W=92/L=6  WR=93.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; zscore -1 to +1 neutral  •  AVOID when upper third

### W18.  `H20=H20a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

### W19.  `H60=H60a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

### W20.  `T1=T1a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

### W21.  `T4=T4a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

### W22.  `RSI=RSI7 AND direction_exec=long AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: LONG**  •  RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

### W23.  `H20=H20a AND H60=H60a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

### W24.  `H20=H20a AND T1=T1a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

### W25.  `H20=H20a AND T4=T4a AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=140  W=129/L=11  WR=92.1%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=99  W=97/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought; session=asia  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND ZS=ZS3`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: sharpest is RSI=RSI6 (59/84 of losers there)
- **Sharp: n=88  W=29/L=59  WR=33.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L02.  `T1=T1c AND T4=T4c AND ZS=ZS3`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: sharpest is RSI=RSI6 (59/84 of losers there)
- **Sharp: n=88  W=29/L=59  WR=33.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L03.  `T4=T4c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: sharpest is RSI=RSI6 (59/84 of losers there)
- **Sharp: n=88  W=29/L=59  WR=33.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L04.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS3`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: sharpest is RSI=RSI6 (59/84 of losers there)
- **Sharp: n=88  W=29/L=59  WR=33.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L05.  `H60=H60e AND T4=T4c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: sharpest is RSI=RSI6 (59/84 of losers there)
- **Sharp: n=88  W=29/L=59  WR=33.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L06.  `T1=T1c AND T4=T4c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: sharpest is RSI=RSI6 (59/84 of losers there)
- **Sharp: n=88  W=29/L=59  WR=33.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L07.  `H20=H20e AND T4=T4c AND ZS=ZS3`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (58/82 of losers there)
- **Sharp: n=83  W=25/L=58  WR=30.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS3`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (58/82 of losers there)
- **Sharp: n=83  W=25/L=58  WR=30.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS3`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (58/82 of losers there)
- **Sharp: n=83  W=25/L=58  WR=30.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L10.  `H20=H20e AND T4=T4c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (58/82 of losers there)
- **Sharp: n=83  W=25/L=58  WR=30.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 70-80 overbought

### L11.  `H20=H20e AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI>80 extreme overbought; session=asia

### L12.  `H60=H60e AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI>80 extreme overbought; session=asia

### L13.  `T1=T1c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L14.  `T4=T4c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L15.  `RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: SHORT**  •  RSI>80 extreme overbought; session=asia

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI>80 extreme overbought; session=asia

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L19.  `H20=H20e AND RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI>80 extreme overbought; session=asia

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L21.  `H60=H60e AND T4=T4c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L22.  `H60=H60e AND RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI>80 extreme overbought; session=asia

### L23.  `T1=T1c AND T4=T4c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L24.  `T1=T1c AND RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI>80 extreme overbought; session=asia

### L25.  `T4=T4c AND RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=23/L=89  WR=20.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI>80 extreme overbought; session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(52/39) | H20e(42/55) |
| H60 | H60a(54/44) | H60e(46/56) |
| T1 | T1a(54/44) | T1c(46/56) |
| T4 | T4a(54/43) | T4c(46/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/44) | short(46/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
