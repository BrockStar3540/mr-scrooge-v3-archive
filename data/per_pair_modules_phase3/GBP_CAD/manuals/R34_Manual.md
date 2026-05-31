# GBP_CAD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,463**  (W=3,286 / L=2,177)  -  WR: **60.2%**

## Session distribution

- ny_mid: n=1427  W=852/L=575  WR=59.7%
- ny_open: n=1099  W=660/L=439  WR=60.1%
- ny_close: n=976  W=595/L=381  WR=61.0%
- london_open: n=698  W=428/L=270  WR=61.3%
- london: n=599  W=348/L=251  WR=58.1%
- asia: n=465  W=287/L=178  WR=61.7%
- off_hours: n=116  W=66/L=50  WR=56.9%
- asia_late: n=83  W=50/L=33  WR=60.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=156  W=134/L=22  WR=85.9%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=138  W=119/L=19  WR=86.2%
- Refine: exclude H20=H20a drops 14/19 losers (74%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W03.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude H20=H20a drops 13/18 losers (72%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W04.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H60=H60e drops 13/15 losers (87%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W05.  `T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude session_bucket=ny_open drops 7/16 losers (44%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when session=ny_open

### W06.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude session_bucket=ny_open drops 7/16 losers (44%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W07.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP4 drops 13/15 losers (87%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when upper third

### W08.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP4 drops 13/15 losers (87%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W09.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=97  W=88/L=9  WR=90.7%
- Refine: exclude H60=H60c drops 8/9 losers (89%)
- **Final: n=85  W=84/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 neutral

### W10.  `H20=H20a AND H60=H60c AND RSI=RSI3`
- Raw: n=96  W=88/L=8  WR=91.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20b AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude ZS=ZS2 drops 10/11 losers (91%)
- **Final: n=77  W=76/L=1  WR=98.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W12.  `H60=H60c AND T1=T1c AND ZS=ZS1`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W13.  `H60=H60c AND T4=T4a AND ZS=ZS1`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W14.  `H60=H60c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF60 neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W15.  `H60=H60c AND T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W16.  `H60=H60c AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W17.  `H60=H60c AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W18.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H60=H60c drops 4/14 losers (29%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 neutral

### W19.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 strongly against

### W20.  `H20=H20a AND H60=H60c AND T4=T4a AND RSI=RSI3`
- Raw: n=86  W=85/L=1  WR=98.8%
- Refine: no further refinement
- **Final: n=86  W=85/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 4h trend WITH trade; RSI 40-50 lower neutral

### W21.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W22.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude H20=H20e drops 9/11 losers (82%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W23.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H60=H60c drops 8/11 losers (73%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; session=london_open  •  AVOID when HTF60 neutral

### W24.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=ny_mid drops 9/9 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=ny_mid

### W25.  `T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20e drops 9/9 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=204  W=77/L=127  WR=37.7%
- Sharpen: sharpest is H20=H20a (38/127 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=188  W=56/L=132  WR=29.8%
- Sharpen: sharpest is H20=H20c (33/132 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L03.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=185  W=69/L=116  WR=37.3%
- Sharpen: sharpest is H60=H60e (70/116 of losers there)
- **Sharp: n=84  W=14/L=70  WR=16.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L04.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=177  W=62/L=115  WR=35.0%
- Sharpen: sharpest is T4=T4c (68/115 of losers there)
- **Sharp: n=82  W=14/L=68  WR=17.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20c AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=173  W=69/L=104  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (29/104 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=159  W=53/L=106  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (49/106 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L07.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=151  W=54/L=97  WR=35.8%
- Sharpen: sharpest is T1=T1c (41/97 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=151  W=60/L=91  WR=39.7%
- Sharpen: sharpest is RSI=RSI3 (31/91 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=145  W=51/L=94  WR=35.2%
- Sharpen: sharpest is session_bucket=ny_mid (49/94 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L10.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=145  W=51/L=94  WR=35.2%
- Sharpen: sharpest is session_bucket=ny_mid (49/94 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L11.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: sharpest is T4=T4c (52/94 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=140  W=53/L=87  WR=37.9%
- Sharpen: sharpest is T4=T4c (52/87 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L13.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=139  W=48/L=91  WR=34.5%
- Sharpen: sharpest is ZS=ZS4 (80/91 of losers there)
- **Sharp: n=113  W=33/L=80  WR=29.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L14.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=138  W=44/L=94  WR=31.9%
- Sharpen: sharpest is H60=H60e (57/94 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L15.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=137  W=51/L=86  WR=37.2%
- Sharpen: sharpest is T4=T4c (45/86 of losers there)
- **Sharp: n=63  W=18/L=45  WR=28.6%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L16.  `H60=H60e AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=135  W=49/L=86  WR=36.3%
- Sharpen: sharpest is T4=T4c (45/86 of losers there)
- **Sharp: n=63  W=18/L=45  WR=28.6%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L17.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is H60=H60e (41/81 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L18.  `H20=H20c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (37/77 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: LONG**  •  HTF20 neutral; upper third  •  ONLY when session=ny_open

### L19.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=127  W=47/L=80  WR=37.0%
- Sharpen: sharpest is H20=H20e (49/80 of losers there)
- **Sharp: n=55  W=6/L=49  WR=10.9%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF20 strongly against

### L20.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is T4=T4c (57/78 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is session_bucket=london (25/79 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L22.  `H20=H20c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=126  W=50/L=76  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=50/L=76  WR=39.7%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 40-50 lower neutral

### L23.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is ZS=ZS3 (25/75 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=ny_open  •  ONLY when zscore -1 to +1 neutral

### L24.  `T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=124  W=41/L=83  WR=33.1%
- Sharpen: sharpest is BBP=BBP5 (49/83 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when just touched upper band

### L25.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is H60=H60b (21/79 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(32/38) |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/47) | long(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
