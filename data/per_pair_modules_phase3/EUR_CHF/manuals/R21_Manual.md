# EUR_CHF — R21 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,301**  (W=865 / L=436)  -  WR: **66.5%**

## Session distribution

- asia: n=293  W=191/L=102  WR=65.2%
- ny_close: n=251  W=166/L=85  WR=66.1%
- london_open: n=214  W=142/L=72  WR=66.4%
- london: n=198  W=136/L=62  WR=68.7%
- ny_open: n=156  W=108/L=48  WR=69.2%
- ny_mid: n=92  W=62/L=30  WR=67.4%
- asia_late: n=55  W=37/L=18  WR=67.3%
- off_hours: n=42  W=23/L=19  WR=54.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=139  W=125/L=14  WR=89.9%
- Refine: exclude ZS=ZS4 drops 5/14 losers (36%)
- **Final: n=119  W=110/L=9  WR=92.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W02.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=134  W=120/L=14  WR=89.6%
- Refine: exclude ZS=ZS4 drops 5/14 losers (36%)
- **Final: n=114  W=105/L=9  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W03.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=129  W=114/L=15  WR=88.4%
- Refine: exclude session_bucket=asia drops 9/15 losers (60%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W04.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=102  W=91/L=11  WR=89.2%
- Refine: exclude session_bucket=asia drops 8/11 losers (73%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W05.  `H20=H20b AND T1=T1c AND direction_exec=long`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude RSI=RSI2 drops 9/13 losers (69%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W06.  `H20=H20d AND T1=T1c AND direction_exec=long`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade  •  AVOID when 4h trend WITH trade

### W07.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude T4=T4c drops 4/5 losers (80%)
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20b AND T1=T1c AND T4=T4a`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI2 drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W09.  `H20=H20b AND T4=T4a AND direction_exec=long`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI2 drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W10.  `H20=H20b AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI2 drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W11.  `H20=H20b AND H60=H60e AND RSI=RSI3`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude T1=T1a drops 4/8 losers (50%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W12.  `H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 7/11 losers (64%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W13.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 7/11 losers (64%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W14.  `H60=H60c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 7/11 losers (64%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W15.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=73  W=72/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open

### W16.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=73  W=72/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open

### W17.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=73  W=72/L=1  WR=98.6%
- Refine: no further refinement
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open

### W18.  `H60=H60c AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=ny_close drops 5/9 losers (56%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=ny_close

### W19.  `H60=H60c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=ny_close drops 5/9 losers (56%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when session=ny_close

### W20.  `T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude ZS=ZS1 drops 7/10 losers (70%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude ZS=ZS1 drops 7/10 losers (70%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london  •  AVOID when zscore -3 to -2 deep oversold

### W22.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude ZS=ZS1 drops 7/10 losers (70%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when zscore -3 to -2 deep oversold

### W23.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude session_bucket=london drops 5/9 losers (56%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when session=london

### W24.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H60=H60a drops 3/10 losers (30%)
- **Final: n=65  W=58/L=7  WR=89.2%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W25.  `H20=H20b AND T1=T1c AND RSI=RSI3`
- Raw: n=69  W=65/L=4  WR=94.2%
- Refine: exclude session_bucket=asia drops 4/4 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (16/66 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L02.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=92  W=33/L=59  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_close (16/59 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L03.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is session_bucket=ny_close (16/56 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L04.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is BBP=BBP0 (26/51 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L05.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is T4=T4c (39/43 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_close (16/44 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is BBP=BBP0 (19/41 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L08.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is BBP=BBP0 (19/41 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L09.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is T4=T4a (14/39 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (8/37 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L11.  `H20=H20b AND T1=T1a AND direction_exec=short`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is T4=T4a (24/35 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade  •  ONLY when 4h trend WITH trade

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_open (11/34 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L13.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is RSI=RSI3 (7/33 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L14.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is ZS=ZS1 (26/31 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is H20=H20e (7/31 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L16.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=48  W=9/L=39  WR=18.8%
- Sharpen: sharpest is RSI=RSI1 (13/39 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 20-30 oversold

### L17.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=48  W=9/L=39  WR=18.8%
- Sharpen: sharpest is RSI=RSI1 (13/39 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 20-30 oversold

### L18.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=48  W=9/L=39  WR=18.8%
- Sharpen: sharpest is RSI=RSI1 (13/39 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 20-30 oversold

### L19.  `H60=H60c AND T1=T1a AND RSI=RSI2`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is H20=H20e (9/32 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L20.  `H60=H60c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is H20=H20e (9/32 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L21.  `H60=H60c AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is H20=H20e (9/32 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is H20=H20e (7/31 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L23.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (9/30 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L24.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (7/30 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L25.  `H20=H20a AND T1=T1c AND ZS=ZS1`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is H60=H60b (11/29 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(36/43) |
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
