# USD_CHF — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,897**  (W=1,876 / L=1,021)  -  WR: **64.8%**

## Session distribution

- ny_mid: n=734  W=488/L=246  WR=66.5%
- ny_open: n=515  W=320/L=195  WR=62.1%
- london_open: n=502  W=316/L=186  WR=62.9%
- ny_close: n=435  W=280/L=155  WR=64.4%
- london: n=334  W=218/L=116  WR=65.3%
- asia: n=282  W=192/L=90  WR=68.1%
- off_hours: n=51  W=32/L=19  WR=62.7%
- asia_late: n=44  W=30/L=14  WR=68.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=179  W=154/L=25  WR=86.0%
- Refine: exclude session_bucket=ny_mid drops 16/25 losers (64%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W02.  `T4=T4a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=179  W=154/L=25  WR=86.0%
- Refine: exclude session_bucket=ny_mid drops 16/25 losers (64%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W03.  `T1=T1a AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude H60=H60e drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W04.  `BBP=BBP3 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude H60=H60e drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: LONG**  •  middle of band; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W05.  `T1=T1a AND BBP=BBP3 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude H60=H60e drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W06.  `T1=T1a AND BBP=BBP3 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude H60=H60e drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: LONG**  •  1h trend WITH trade; middle of band; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W07.  `BBP=BBP3 AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude H60=H60e drops 11/20 losers (55%)
- **Final: n=103  W=94/L=9  WR=91.3%**
- **Dir: LONG**  •  middle of band; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W08.  `T4=T4a AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=144  W=123/L=21  WR=85.4%
- Refine: exclude H60=H60e drops 9/21 losers (43%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W09.  `T4=T4a AND BBP=BBP3 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=144  W=123/L=21  WR=85.4%
- Refine: exclude H60=H60e drops 9/21 losers (43%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  4h trend WITH trade; middle of band; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W10.  `H20=H20d AND H60=H60a AND RSI=RSI4`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude ZS=ZS3 drops 13/18 losers (72%)
- **Final: n=117  W=112/L=5  WR=95.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1a AND T4=T4a AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=135  W=118/L=17  WR=87.4%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W12.  `T4=T4a AND BBP=BBP3 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=135  W=118/L=17  WR=87.4%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: LONG**  •  4h trend WITH trade; middle of band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W13.  `H60=H60a AND T1=T1a AND BBP=BBP3`
- Raw: n=129  W=113/L=16  WR=87.6%
- Refine: exclude session_bucket=ny_mid drops 8/16 losers (50%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band  •  AVOID when session=ny_mid

### W14.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=129  W=113/L=16  WR=87.6%
- Refine: exclude session_bucket=ny_mid drops 8/16 losers (50%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W15.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=122  W=105/L=17  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 8/17 losers (47%)
- **Final: n=98  W=89/L=9  WR=90.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W16.  `H60=H60a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H20=H20d drops 6/17 losers (35%)
- **Final: n=107  W=96/L=11  WR=89.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; middle of band  •  AVOID when HTF20 mildly against

### W17.  `H60=H60a AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H20=H20d drops 6/17 losers (35%)
- **Final: n=107  W=96/L=11  WR=89.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when HTF20 mildly against

### W18.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP3`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 8/15 losers (53%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; middle of band  •  AVOID when session=ny_mid

### W19.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 8/15 losers (53%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band  •  AVOID when session=ny_mid

### W20.  `H60=H60a AND T4=T4a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H20=H20d drops 6/17 losers (35%)
- **Final: n=105  W=94/L=11  WR=89.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; middle of band  •  AVOID when HTF20 mildly against

### W21.  `BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=112  W=105/L=7  WR=93.8%
- Refine: exclude H60=H60e drops 4/7 losers (57%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: SHORT**  •  upper third; session=london_open  •  AVOID when HTF60 strongly against

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 8/16 losers (50%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W23.  `H60=H60a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 8/16 losers (50%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W24.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude BBP=BBP4 drops 5/16 losers (31%)
- **Final: n=91  W=80/L=11  WR=87.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when upper third

### W25.  `ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=105  W=99/L=6  WR=94.3%
- Refine: exclude H60=H60e drops 4/6 losers (67%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=166  W=60/L=106  WR=36.1%
- Sharpen: sharpest is ZS=ZS5 (58/106 of losers there)
- **Sharp: n=73  W=15/L=58  WR=20.5%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is ZS=ZS5 (49/101 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=156  W=61/L=95  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=156  W=61/L=95  WR=39.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral

### L04.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=148  W=59/L=89  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (49/89 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=139  W=50/L=89  WR=36.0%
- Sharpen: sharpest is RSI=RSI5 (50/89 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L06.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=139  W=50/L=89  WR=36.0%
- Sharpen: sharpest is RSI=RSI5 (50/89 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: LONG**  •  deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L07.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=139  W=50/L=89  WR=36.0%
- Sharpen: sharpest is RSI=RSI5 (50/89 of losers there)
- **Sharp: n=65  W=15/L=50  WR=23.1%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L08.  `H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: sharpest is BBP=BBP6 (26/81 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L09.  `H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is BBP=BBP6 (26/80 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L10.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is BBP=BBP6 (26/80 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L11.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=118  W=44/L=74  WR=37.3%
- Sharpen: sharpest is BBP=BBP6 (23/74 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L12.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=116  W=43/L=73  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (23/73 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is RSI=RSI5 (41/75 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L14.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is RSI=RSI5 (41/75 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=107  W=38/L=69  WR=35.5%
- Sharpen: sharpest is BBP=BBP5 (19/69 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=london_open  •  ONLY when just touched upper band

### L16.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (33/61 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L17.  `H20=H20e AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (33/61 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L18.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is ZS=ZS5 (33/60 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is ZS=ZS4 (22/62 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L20.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is H20=H20e (27/60 of losers there)
- **Sharp: n=38  W=11/L=27  WR=28.9%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L21.  `ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is H20=H20e (27/60 of losers there)
- **Sharp: n=38  W=11/L=27  WR=28.9%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L22.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is H20=H20e (27/60 of losers there)
- **Sharp: n=38  W=11/L=27  WR=28.9%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 strongly against

### L23.  `T1=T1c AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (15/57 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 60-70 strong  •  ONLY when session=ny_close

### L24.  `BBP=BBP3 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (15/57 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: SHORT**  •  middle of band; RSI 60-70 strong  •  ONLY when session=ny_close

### L25.  `T1=T1c AND BBP=BBP3 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (15/57 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(42/37) | H60e(37/44) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | ZS5(28/34) |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
