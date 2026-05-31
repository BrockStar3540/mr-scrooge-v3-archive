# USD_CHF — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,175**  (W=1,361 / L=814)  -  WR: **62.6%**

## Session distribution

- ny_mid: n=579  W=373/L=206  WR=64.4%
- asia: n=432  W=268/L=164  WR=62.0%
- ny_open: n=323  W=200/L=123  WR=61.9%
- london_open: n=293  W=170/L=123  WR=58.0%
- ny_close: n=221  W=141/L=80  WR=63.8%
- london: n=189  W=123/L=66  WR=65.1%
- asia_late: n=98  W=65/L=33  WR=66.3%
- off_hours: n=40  W=21/L=19  WR=52.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI1`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W02.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI1`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI1`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W05.  `H20=H20a AND H60=H60d AND T4=T4c`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude session_bucket=london_open drops 11/13 losers (85%)
- **Final: n=89  W=87/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when session=london_open

### W06.  `H60=H60a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T1=T1c drops 4/13 losers (31%)
- **Final: n=85  W=76/L=9  WR=89.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W07.  `H60=H60a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T1=T1c drops 4/13 losers (31%)
- **Final: n=85  W=76/L=9  WR=89.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W08.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude H60=H60e drops 8/10 losers (80%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W09.  `H60=H60a AND T1=T1a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W11.  `H20=H20b AND T1=T1a AND ZS=ZS1`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W12.  `H20=H20b AND T4=T4a AND ZS=ZS1`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=ny_open drops 8/9 losers (89%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W13.  `H60=H60b AND T1=T1a AND T4=T4c`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP3 drops 6/12 losers (50%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when middle of band

### W14.  `H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP3 drops 6/12 losers (50%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when middle of band

### W15.  `H20=H20e AND H60=H60b AND T1=T1a AND T4=T4c`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP3 drops 6/12 losers (50%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when middle of band

### W16.  `H20=H20e AND H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP3 drops 6/12 losers (50%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when middle of band

### W17.  `H60=H60b AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude BBP=BBP3 drops 6/12 losers (50%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when middle of band

### W18.  `H60=H60b AND T4=T4c AND RSI=RSI2`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude session_bucket=ny_open drops 7/9 losers (78%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=ny_open

### W19.  `H20=H20b AND ZS=ZS1 AND direction_exec=short`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W20.  `H20=H20b AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W21.  `H20=H20b AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W22.  `H20=H20b AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W23.  `H20=H20e AND H60=H60b AND T4=T4c AND RSI=RSI2`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude session_bucket=ny_open drops 7/8 losers (88%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=ny_open

### W24.  `H60=H60a AND T4=T4a AND BBP=BBP0`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=london_open

### W25.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude strategy_id=BR3_inside_bar_short drops 2/9 losers (22%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; RSI 20-30 oversold  •  AVOID when strategy=BR3_inside_bar_short

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=151  W=58/L=93  WR=38.4%
- Sharpen: sharpest is ZS=ZS1 (41/93 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is session_bucket=london (31/90 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=london

### L03.  `H20=H20e AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is session_bucket=london (31/90 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 20-30 oversold  •  ONLY when session=london

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (41/93 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (41/93 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (41/93 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (41/93 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is ZS=ZS1 (41/93 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is BBP=BBP0 (37/84 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L10.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is BBP=BBP0 (37/81 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L11.  `H60=H60e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is BBP=BBP0 (37/81 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L12.  `H20=H20a AND H60=H60d AND T4=T4a`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is RSI=RSI2 (38/75 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L13.  `H20=H20e AND H60=H60e AND RSI=RSI1`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is BBP=BBP0 (12/66 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  ONLY when deep below lower band

### L14.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is BBP=BBP0 (12/66 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L15.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is BBP=BBP0 (12/66 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when deep below lower band

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is BBP=BBP0 (12/66 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  ONLY when deep below lower band

### L17.  `H60=H60e AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=94  W=27/L=67  WR=28.7%
- Sharpen: sharpest is H20=H20a (29/67 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L18.  `T1=T1c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60e (25/52 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when HTF60 strongly against

### L19.  `T4=T4c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60e (25/52 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when HTF60 strongly against

### L20.  `BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60e (25/52 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: LONG**  •  deep below lower band; RSI 20-30 oversold  •  ONLY when HTF60 strongly against

### L21.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60e (25/52 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when HTF60 strongly against

### L22.  `T1=T1c AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60e (25/52 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when HTF60 strongly against

### L23.  `T4=T4c AND BBP=BBP0 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60e (25/52 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 20-30 oversold  •  ONLY when HTF60 strongly against

### L24.  `H20=H20d AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is ZS=ZS1 (31/53 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H20=H20d AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is ZS=ZS1 (31/53 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(35/29) | H20e(30/36) |
| H60 | H60a(39/27) | H60e(26/37) |
| T1 | T1a(54/44) | T1c(46/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/45) | long(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
