# NZD_CAD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,282**  (W=2,081 / L=1,201)  -  WR: **63.4%**

## Session distribution

- ny_mid: n=754  W=475/L=279  WR=63.0%
- asia: n=707  W=446/L=261  WR=63.1%
- london_open: n=513  W=316/L=197  WR=61.6%
- ny_open: n=397  W=258/L=139  WR=65.0%
- london: n=373  W=237/L=136  WR=63.5%
- ny_close: n=350  W=223/L=127  WR=63.7%
- asia_late: n=116  W=80/L=36  WR=69.0%
- off_hours: n=72  W=46/L=26  WR=63.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=193  W=165/L=28  WR=85.5%
- Refine: exclude T1=T1a drops 23/28 losers (82%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when 1h trend WITH trade

### W02.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=156  W=133/L=23  WR=85.3%
- Refine: no further refinement
- **Final: n=156  W=133/L=23  WR=85.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia

### W03.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=154  W=131/L=23  WR=85.1%
- Refine: no further refinement
- **Final: n=154  W=131/L=23  WR=85.1%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia

### W04.  `H20=H20a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=136  W=116/L=20  WR=85.3%
- Refine: exclude RSI=RSI5 drops 11/20 losers (55%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when RSI 60-70 strong

### W05.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude BBP=BBP2 drops 9/16 losers (56%)
- **Final: n=122  W=115/L=7  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when lower third

### W06.  `H20=H20e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude BBP=BBP2 drops 9/16 losers (56%)
- **Final: n=122  W=115/L=7  WR=94.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when lower third

### W07.  `H20=H20a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude RSI=RSI5 drops 11/18 losers (61%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W08.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude RSI=RSI5 drops 11/18 losers (61%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W09.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude H20=H20d drops 9/16 losers (56%)
- **Final: n=113  W=106/L=7  WR=93.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W10.  `H20=H20b AND H60=H60e AND RSI=RSI5`
- Raw: n=123  W=109/L=14  WR=88.6%
- Refine: exclude T4=T4a drops 14/14 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=119  W=108/L=11  WR=90.8%
- Refine: exclude BBP=BBP2 drops 9/11 losers (82%)
- **Final: n=110  W=108/L=2  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when lower third

### W12.  `T4=T4c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H20=H20a drops 5/17 losers (29%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W13.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H20=H20a drops 5/17 losers (29%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W14.  `H20=H20b AND H60=H60e AND session_bucket=asia`
- Raw: n=118  W=108/L=10  WR=91.5%
- Refine: exclude ZS=ZS4 drops 7/10 losers (70%)
- **Final: n=96  W=93/L=3  WR=96.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  AVOID when zscore +1 to +2 overbought

### W15.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude RSI=RSI5 drops 10/15 losers (67%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20b AND T4=T4c AND RSI=RSI5`
- Raw: n=106  W=98/L=8  WR=92.5%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=82  W=82/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20b AND T1=T1a AND RSI=RSI5`
- Raw: n=106  W=95/L=11  WR=89.6%
- Refine: exclude T4=T4a drops 11/11 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W18.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=106  W=94/L=12  WR=88.7%
- Refine: exclude H20=H20a drops 10/12 losers (83%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W20.  `H20=H20e AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H60=H60a drops 11/13 losers (85%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W21.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=97  W=88/L=9  WR=90.7%
- Refine: exclude ZS=ZS3 drops 2/9 losers (22%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20a AND T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude RSI=RSI5 drops 8/14 losers (57%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI 60-70 strong

### W23.  `H20=H20b AND T1=T1a AND session_bucket=asia`
- Raw: n=93  W=86/L=7  WR=92.5%
- Refine: exclude ZS=ZS4 drops 5/7 losers (71%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W24.  `H20=H20c AND T4=T4c AND RSI=RSI4`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude session_bucket=ny_mid drops 6/11 losers (55%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W25.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60a drops 8/11 losers (73%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=169  W=55/L=114  WR=32.5%
- Sharpen: sharpest is BBP=BBP4 (48/114 of losers there)
- **Sharp: n=57  W=9/L=48  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L02.  `T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=154  W=49/L=105  WR=31.8%
- Sharpen: sharpest is T1=T1a (49/105 of losers there)
- **Sharp: n=52  W=3/L=49  WR=5.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend WITH trade

### L03.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=149  W=56/L=93  WR=37.6%
- Sharpen: sharpest is direction_exec=long (42/93 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when long

### L04.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (71/82 of losers there)
- **Sharp: n=102  W=31/L=71  WR=30.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=130  W=46/L=84  WR=35.4%
- Sharpen: sharpest is BBP=BBP4 (48/84 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L06.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=127  W=42/L=85  WR=33.1%
- Sharpen: sharpest is T1=T1a (32/85 of losers there)
- **Sharp: n=34  W=2/L=32  WR=5.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend WITH trade

### L07.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=124  W=37/L=87  WR=29.8%
- Sharpen: sharpest is BBP=BBP4 (45/87 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L08.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=37/L=85  WR=30.3%
- Sharpen: sharpest is BBP=BBP4 (44/85 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L09.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=118  W=38/L=80  WR=32.2%
- Sharpen: sharpest is H20=H20e (45/80 of losers there)
- **Sharp: n=56  W=11/L=45  WR=19.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L10.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is direction_exec=long (20/71 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when long

### L11.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: sharpest is RSI=RSI5 (40/65 of losers there)
- **Sharp: n=56  W=16/L=40  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L12.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=105  W=35/L=70  WR=33.3%
- Sharpen: sharpest is direction_exec=long (29/70 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when long

### L13.  `H20=H20d AND H60=H60a AND session_bucket=asia`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=36/L=67  WR=35.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; session=asia

### L14.  `H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI4 (48/62 of losers there)
- **Sharp: n=57  W=9/L=48  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is BBP=BBP4 (36/71 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L16.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=98  W=34/L=64  WR=34.7%
- Sharpen: sharpest is ZS=ZS6 (24/64 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore >+3 extreme

### L17.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=97  W=34/L=63  WR=35.1%
- Sharpen: sharpest is ZS=ZS6 (20/63 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore >+3 extreme

### L18.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=96  W=28/L=68  WR=29.2%
- Sharpen: sharpest is BBP=BBP4 (36/68 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L19.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=96  W=37/L=59  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (33/59 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is direction_exec=long (54/58 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when long

### L21.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is T1=T1a (54/55 of losers there)
- **Sharp: n=74  W=20/L=54  WR=27.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L22.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=85  W=25/L=60  WR=29.4%
- Sharpen: sharpest is RSI=RSI4 (48/60 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L23.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is ZS=ZS4 (28/56 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L24.  `H20=H20e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is RSI=RSI4 (47/59 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is RSI=RSI4 (47/59 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(15/6), H20a(39/32) | H20e(32/41), H20d(7/14) |
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
