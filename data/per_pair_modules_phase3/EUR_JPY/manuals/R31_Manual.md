# EUR_JPY — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **6,078**  (W=3,721 / L=2,357)  -  WR: **61.2%**

## Session distribution

- asia: n=2320  W=1427/L=893  WR=61.5%
- ny_mid: n=1073  W=657/L=416  WR=61.2%
- london_open: n=1058  W=634/L=424  WR=59.9%
- ny_open: n=749  W=454/L=295  WR=60.6%
- ny_close: n=310  W=205/L=105  WR=66.1%
- london: n=298  W=180/L=118  WR=60.4%
- asia_late: n=233  W=142/L=91  WR=60.9%
- off_hours: n=37  W=22/L=15  WR=59.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=292  W=257/L=35  WR=88.0%
- Refine: exclude BBP=BBP5 drops 9/35 losers (26%)
- **Final: n=279  W=253/L=26  WR=90.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when just touched upper band

### W02.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=280  W=246/L=34  WR=87.9%
- Refine: exclude BBP=BBP5 drops 9/34 losers (26%)
- **Final: n=267  W=242/L=25  WR=90.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when just touched upper band

### W03.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=255  W=222/L=33  WR=87.1%
- Refine: exclude BBP=BBP5 drops 12/33 losers (36%)
- **Final: n=236  W=215/L=21  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when just touched upper band

### W04.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=251  W=214/L=37  WR=85.3%
- Refine: exclude BBP=BBP5 drops 12/37 losers (32%)
- **Final: n=232  W=207/L=25  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when just touched upper band

### W05.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=250  W=219/L=31  WR=87.6%
- Refine: exclude BBP=BBP5 drops 12/31 losers (39%)
- **Final: n=233  W=214/L=19  WR=91.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when just touched upper band

### W06.  `H20=H20e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=234  W=204/L=30  WR=87.2%
- Refine: exclude BBP=BBP2 drops 15/30 losers (50%)
- **Final: n=192  W=177/L=15  WR=92.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  AVOID when lower third

### W07.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=195  W=174/L=21  WR=89.2%
- Refine: exclude RSI=RSI3 drops 9/21 losers (43%)
- **Final: n=156  W=144/L=12  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; session=asia  •  AVOID when RSI 40-50 lower neutral

### W08.  `T4=T4c AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=187  W=164/L=23  WR=87.7%
- Refine: exclude T1=T1c drops 17/23 losers (74%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; session=asia  •  AVOID when 1h trend AGAINST trade

### W09.  `T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude RSI=RSI3 drops 21/24 losers (88%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band  •  AVOID when RSI 40-50 lower neutral

### W10.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude RSI=RSI3 drops 21/24 losers (88%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W11.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=158  W=140/L=18  WR=88.6%
- Refine: exclude T1=T1c drops 13/18 losers (72%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend AGAINST trade

### W12.  `T4=T4c AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=158  W=138/L=20  WR=87.3%
- Refine: exclude T1=T1c drops 15/20 losers (75%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend AGAINST trade

### W13.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=156  W=136/L=20  WR=87.2%
- Refine: exclude H60=H60e drops 14/20 losers (70%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 strongly against

### W14.  `H20=H20e AND H60=H60a AND RSI=RSI4`
- Raw: n=150  W=131/L=19  WR=87.3%
- Refine: exclude BBP=BBP2 drops 9/19 losers (47%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when lower third

### W15.  `T1=T1a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=150  W=128/L=22  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 7/22 losers (32%)
- **Final: n=129  W=114/L=15  WR=88.4%**
- **Dir: LONG**  •  1h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W16.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=145  W=127/L=18  WR=87.6%
- Refine: exclude BBP=BBP2 drops 12/18 losers (67%)
- **Final: n=121  W=115/L=6  WR=95.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when lower third

### W17.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=143  W=127/L=16  WR=88.8%
- Refine: exclude BBP=BBP2 drops 9/16 losers (56%)
- **Final: n=121  W=114/L=7  WR=94.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when lower third

### W18.  `H20=H20e AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=143  W=127/L=16  WR=88.8%
- Refine: exclude BBP=BBP2 drops 9/16 losers (56%)
- **Final: n=121  W=114/L=7  WR=94.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when lower third

### W19.  `T1=T1a AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=136  W=120/L=16  WR=88.2%
- Refine: exclude H60=H60e drops 11/16 losers (69%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 strongly against

### W20.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=131  W=116/L=15  WR=88.5%
- Refine: exclude BBP=BBP2 drops 7/15 losers (47%)
- **Final: n=103  W=95/L=8  WR=92.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when lower third

### W21.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=131  W=116/L=15  WR=88.5%
- Refine: exclude ZS=ZS3 drops 8/15 losers (53%)
- **Final: n=98  W=91/L=7  WR=92.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W22.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude H20=H20e drops 12/19 losers (63%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W23.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=ny_mid drops 8/18 losers (44%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W24.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 7/15 losers (47%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W25.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude ZS=ZS3 drops 10/16 losers (62%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=345  W=138/L=207  WR=40.0%
- Sharpen: sharpest is T4=T4a (112/207 of losers there)
- **Sharp: n=162  W=50/L=112  WR=30.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=302  W=111/L=191  WR=36.8%
- Sharpen: sharpest is T4=T4a (105/191 of losers there)
- **Sharp: n=148  W=43/L=105  WR=29.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=269  W=105/L=164  WR=39.0%
- Sharpen: sharpest is T1=T1c (101/164 of losers there)
- **Sharp: n=144  W=43/L=101  WR=29.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L04.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=254  W=89/L=165  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=254  W=89/L=165  WR=35.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia

### L05.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=233  W=78/L=155  WR=33.5%
- Sharpen: sharpest is ZS=ZS4 (71/155 of losers there)
- **Sharp: n=93  W=22/L=71  WR=23.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +1 to +2 overbought

### L06.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=209  W=77/L=132  WR=36.8%
- Sharpen: sharpest is session_bucket=asia (71/132 of losers there)
- **Sharp: n=96  W=25/L=71  WR=26.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L07.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=209  W=79/L=130  WR=37.8%
- Sharpen: sharpest is RSI=RSI4 (85/130 of losers there)
- **Sharp: n=118  W=33/L=85  WR=28.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L08.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=203  W=67/L=136  WR=33.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=203  W=67/L=136  WR=33.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia

### L09.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=203  W=68/L=135  WR=33.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=203  W=68/L=135  WR=33.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia

### L10.  `T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=194  W=60/L=134  WR=30.9%
- Sharpen: sharpest is RSI=RSI2 (71/134 of losers there)
- **Sharp: n=90  W=19/L=71  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 30-40 weak

### L11.  `H60=H60e AND T1=T1c AND ZS=ZS3`
- Raw: n=189  W=73/L=116  WR=38.6%
- Sharpen: sharpest is session_bucket=london_open (32/116 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L12.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (71/109 of losers there)
- **Sharp: n=93  W=22/L=71  WR=23.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=asia

### L13.  `H60=H60e AND T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=172  W=67/L=105  WR=39.0%
- Sharpen: sharpest is session_bucket=london_open (25/105 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L14.  `H20=H20a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=163  W=43/L=120  WR=26.4%
- Sharpen: sharpest is ZS=ZS4 (45/120 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L15.  `T1=T1c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=160  W=61/L=99  WR=38.1%
- Sharpen: sharpest is H20=H20e (56/99 of losers there)
- **Sharp: n=78  W=22/L=56  WR=28.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L16.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (71/93 of losers there)
- **Sharp: n=90  W=19/L=71  WR=21.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `T1=T1c AND T4=T4a AND BBP=BBP1`
- Raw: n=154  W=60/L=94  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (69/94 of losers there)
- **Sharp: n=87  W=18/L=69  WR=20.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched lower band  •  ONLY when session=asia

### L18.  `T1=T1c AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=154  W=60/L=94  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (69/94 of losers there)
- **Sharp: n=87  W=18/L=69  WR=20.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L19.  `H60=H60a AND T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=153  W=53/L=100  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (63/100 of losers there)
- **Sharp: n=77  W=14/L=63  WR=18.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 30-40 weak

### L20.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=153  W=53/L=100  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (63/100 of losers there)
- **Sharp: n=77  W=14/L=63  WR=18.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 30-40 weak

### L21.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=152  W=52/L=100  WR=34.2%
- Sharpen: sharpest is RSI=RSI4 (83/100 of losers there)
- **Sharp: n=117  W=34/L=83  WR=29.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L22.  `T4=T4a AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=150  W=55/L=95  WR=36.7%
- Sharpen: sharpest is H20=H20e (70/95 of losers there)
- **Sharp: n=98  W=28/L=70  WR=28.6%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; session=asia  •  ONLY when HTF20 strongly against

### L23.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is H20=H20e (74/87 of losers there)
- **Sharp: n=110  W=36/L=74  WR=32.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L24.  `T1=T1c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (28/88 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; middle of band  •  ONLY when session=london_open

### L25.  `H20=H20e AND T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is session_bucket=asia (47/88 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(45/39) | H60e(39/44) |
| T1 | T1a(55/46) | T1c(45/54) |
| T4 | T4c(54/46) | T4a(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/46) | short(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
