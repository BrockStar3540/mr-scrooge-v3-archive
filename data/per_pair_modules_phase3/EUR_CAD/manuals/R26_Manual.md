# EUR_CAD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,313**  (W=1,454 / L=859)  -  WR: **62.9%**

## Session distribution

- london_open: n=639  W=404/L=235  WR=63.2%
- ny_mid: n=441  W=274/L=167  WR=62.1%
- london: n=423  W=281/L=142  WR=66.4%
- ny_open: n=365  W=208/L=157  WR=57.0%
- asia: n=187  W=129/L=58  WR=69.0%
- asia_late: n=117  W=75/L=42  WR=64.1%
- ny_close: n=107  W=62/L=45  WR=57.9%
- off_hours: n=34  W=21/L=13  WR=61.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=ny_close drops 4/15 losers (27%)
- **Final: n=90  W=79/L=11  WR=87.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W02.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/12 losers (50%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W03.  `H60=H60d AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 8/10 losers (80%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60d AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude ZS=ZS3 drops 8/10 losers (80%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: LONG**  •  HTF60 mildly against; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W05.  `H60=H60a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=41  W=37/L=4  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when lower third

### W06.  `H60=H60a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=41  W=37/L=4  WR=90.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when lower third

### W07.  `H60=H60d AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude ZS=ZS3 drops 7/8 losers (88%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/8 losers (25%)
- **Final: n=59  W=53/L=6  WR=89.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when strategy=bravo_failed_momentum

### W09.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W10.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_mid

### W11.  `H60=H60e AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=59  W=56/L=3  WR=94.9%
- Refine: exclude T4=T4a drops 2/3 losers (67%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when 4h trend WITH trade

### W12.  `H60=H60e AND T4=T4c AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=57  W=56/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open

### W13.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/6 losers (33%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when strategy=bravo_failed_momentum

### W14.  `H60=H60a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude H20=H20c drops 4/8 losers (50%)
- **Final: n=45  W=41/L=4  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=london_open  •  AVOID when HTF20 neutral

### W15.  `H60=H60d AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude ZS=ZS3 drops 7/8 losers (88%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=53  W=50/L=3  WR=94.3%
- Refine: exclude T4=T4a drops 2/3 losers (67%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when 4h trend WITH trade

### W17.  `H60=H60e AND ZS=ZS1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=53  W=50/L=3  WR=94.3%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W18.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude session_bucket=asia_late drops 3/5 losers (60%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia_late

### W19.  `T4=T4c AND ZS=ZS1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=52  W=50/L=2  WR=96.2%
- Refine: exclude H20=H20c drops 2/2 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when HTF20 neutral

### W20.  `H20=H20a AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude session_bucket=ny_open drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W21.  `H60=H60a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=49  W=43/L=6  WR=87.8%
- Refine: exclude H20=H20c drops 4/6 losers (67%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 neutral

### W22.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=49  W=43/L=6  WR=87.8%
- Refine: exclude H20=H20c drops 4/6 losers (67%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 neutral

### W23.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=48  W=47/L=1  WR=97.9%
- Refine: no further refinement
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid

### W24.  `ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=47  W=47/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=ny_mid

### W25.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=47  W=47/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=107  W=34/L=73  WR=31.8%
- Sharpen: sharpest is T1=T1a (22/73 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L02.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=107  W=34/L=73  WR=31.8%
- Sharpen: sharpest is T1=T1a (22/73 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L03.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=105  W=38/L=67  WR=36.2%
- Sharpen: sharpest is ZS=ZS3 (12/67 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -1 to +1 neutral

### L04.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=105  W=38/L=67  WR=36.2%
- Sharpen: sharpest is ZS=ZS3 (12/67 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -1 to +1 neutral

### L05.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is direction_exec=long (40/59 of losers there)
- **Sharp: n=56  W=16/L=40  WR=28.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when long

### L06.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is direction_exec=long (36/51 of losers there)
- **Sharp: n=52  W=16/L=36  WR=30.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when long

### L07.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is direction_exec=long (36/51 of losers there)
- **Sharp: n=52  W=16/L=36  WR=30.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when long

### L08.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is H20=H20e (20/51 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L09.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (19/42 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H60=H60a (24/41 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L11.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is T1=T1c (27/41 of losers there)
- **Sharp: n=38  W=11/L=27  WR=28.9%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L12.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is session_bucket=london_open (23/40 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L13.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is H60=H60a (20/37 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L14.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (11/36 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `T4=T4a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is H60=H60a (26/35 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L16.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=56  W=16/L=40  WR=28.6%
- Sharpen: sharpest is H20=H20e (15/40 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when HTF20 strongly against

### L17.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is H20=H20d (15/37 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  ONLY when HTF20 mildly against

### L18.  `H20=H20a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is T4=T4c (17/35 of losers there)
- **Sharp: n=23  W=6/L=17  WR=26.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L19.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=55  W=19/L=36  WR=34.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L20.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is ZS=ZS4 (28/34 of losers there)
- **Sharp: n=40  W=12/L=28  WR=30.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L21.  `H20=H20d AND H60=H60b AND direction_exec=short`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (19/33 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 slightly aligned  •  ONLY when session=ny_mid

### L22.  `H20=H20b AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (16/33 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when upper third

### L23.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=54  W=15/L=39  WR=27.8%
- Sharpen: sharpest is H20=H20b (11/39 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when HTF20 slightly aligned

### L24.  `H60=H60b AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is H20=H20d (19/38 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; session=ny_mid  •  ONLY when HTF20 mildly against

### L25.  `H20=H20b AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_open (7/34 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(37/32) | — |
| T1 | T1a(54/45) | T1c(46/54) |
| T4 | T4c(54/48) | T4a(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/48) | long(45/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
