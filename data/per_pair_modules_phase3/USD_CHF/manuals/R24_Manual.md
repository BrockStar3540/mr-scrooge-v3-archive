# USD_CHF — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,585**  (W=1,641 / L=944)  -  WR: **63.5%**

## Session distribution

- london_open: n=652  W=395/L=257  WR=60.6%
- ny_mid: n=632  W=389/L=243  WR=61.6%
- ny_open: n=325  W=194/L=131  WR=59.7%
- ny_close: n=304  W=206/L=98  WR=67.8%
- london: n=303  W=210/L=93  WR=69.3%
- asia: n=266  W=171/L=95  WR=64.3%
- asia_late: n=74  W=55/L=19  WR=74.3%
- off_hours: n=29  W=21/L=8  WR=72.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=183  W=160/L=23  WR=87.4%
- Refine: exclude RSI=RSI7 drops 10/23 losers (43%)
- **Final: n=171  W=158/L=13  WR=92.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  AVOID when RSI>80 extreme overbought

### W02.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=172  W=153/L=19  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/19 losers (95%)
- **Final: n=77  W=76/L=1  WR=98.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W03.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=172  W=153/L=19  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/19 losers (95%)
- **Final: n=77  W=76/L=1  WR=98.7%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W04.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=172  W=153/L=19  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/19 losers (95%)
- **Final: n=77  W=76/L=1  WR=98.7%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W05.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=172  W=153/L=19  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/19 losers (95%)
- **Final: n=77  W=76/L=1  WR=98.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/18 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W07.  `H20=H20a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/18 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/18 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W09.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/18 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W10.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/18 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude ZS=ZS4 drops 18/18 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W12.  `T1=T1c AND T4=T4c AND session_bucket=london`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude RSI=RSI7 drops 10/19 losers (53%)
- **Final: n=131  W=122/L=9  WR=93.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  AVOID when RSI>80 extreme overbought

### W13.  `T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude RSI=RSI7 drops 10/19 losers (53%)
- **Final: n=131  W=122/L=9  WR=93.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london  •  AVOID when RSI>80 extreme overbought

### W14.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=143  W=124/L=19  WR=86.7%
- Refine: exclude RSI=RSI7 drops 10/19 losers (53%)
- **Final: n=131  W=122/L=9  WR=93.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  AVOID when RSI>80 extreme overbought

### W15.  `H20=H20a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude ZS=ZS4 drops 17/17 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W16.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W17.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W18.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W19.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W20.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W21.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W22.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W23.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W24.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W25.  `T1=T1c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude RSI=RSI7 drops 10/14 losers (71%)
- **Final: n=100  W=96/L=4  WR=96.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london  •  AVOID when RSI>80 extreme overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is BBP=BBP4 (39/67 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when upper third

### L02.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=108  W=43/L=65  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=43/L=65  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; session=london_open

### L03.  `H20=H20e AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=108  W=43/L=65  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=108  W=43/L=65  WR=39.8%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; session=london_open

### L04.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20c (15/65 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=london_open  •  ONLY when HTF20 neutral

### L05.  `H60=H60a AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20c (15/65 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; session=london_open  •  ONLY when HTF20 neutral

### L06.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=104  W=41/L=63  WR=39.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=london_open

### L07.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is H20=H20c (15/60 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF20 neutral

### L08.  `H60=H60a AND ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is H20=H20c (15/60 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF20 neutral

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is H60=H60a (22/53 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20a AND T1=T1a AND session_bucket=london`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (32/44 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london  •  ONLY when RSI 70-80 overbought

### L11.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (32/44 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  ONLY when RSI 70-80 overbought

### L12.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (32/44 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london  •  ONLY when RSI 70-80 overbought

### L13.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (32/44 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london  •  ONLY when RSI 70-80 overbought

### L14.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (32/44 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  ONLY when RSI 70-80 overbought

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is H60=H60a (13/44 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is H60=H60a (13/44 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=64  W=15/L=49  WR=23.4%
- Sharpen: sharpest is RSI=RSI5 (22/49 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L18.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=20/L=44  WR=31.2%
- Sharpen: sharpest is H20=H20a (31/44 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L19.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (39/39 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_open  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=61  W=20/L=41  WR=32.8%
- Sharpen: sharpest is T4=T4c (40/41 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=61  W=20/L=41  WR=32.8%
- Sharpen: sharpest is T4=T4c (40/41 of losers there)
- **Sharp: n=51  W=11/L=40  WR=21.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (18/38 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (18/38 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (18/38 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=22/L=37  WR=37.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought; session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(55/39) | H20e(37/53) |
| H60 | H60e(39/31) | H60a(32/38) |
| T1 | T1a(54/42) | T1c(46/58) |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/42) | short(46/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
