# GBP_AUD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **5,123**  (W=3,130 / L=1,993)  -  WR: **61.1%**

## Session distribution

- asia: n=1273  W=785/L=488  WR=61.7%
- london_open: n=1053  W=648/L=405  WR=61.5%
- ny_mid: n=962  W=579/L=383  WR=60.2%
- ny_close: n=560  W=340/L=220  WR=60.7%
- ny_open: n=519  W=313/L=206  WR=60.3%
- london: n=411  W=263/L=148  WR=64.0%
- off_hours: n=242  W=145/L=97  WR=59.9%
- asia_late: n=103  W=57/L=46  WR=55.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: exclude T4=T4c drops 12/25 losers (48%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W02.  `H20=H20a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: exclude T4=T4c drops 12/25 losers (48%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude T4=T4c drops 12/23 losers (52%)
- **Final: n=124  W=113/L=11  WR=91.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W04.  `T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 aligned WITH trade

### W05.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude BBP=BBP3 drops 10/17 losers (59%)
- **Final: n=104  W=97/L=7  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when middle of band

### W06.  `H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W07.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W08.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W09.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W10.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W11.  `H20=H20e AND T1=T1a AND BBP=BBP4`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude T4=T4a drops 5/5 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third  •  AVOID when 4h trend WITH trade

### W12.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude H20=H20b drops 4/9 losers (44%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when HTF20 slightly aligned

### W13.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude T4=T4a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W14.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude T4=T4a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W15.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude T4=T4a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude T4=T4a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W17.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude T4=T4a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude RSI=RSI2 drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=ny_open  •  AVOID when RSI 30-40 weak

### W19.  `H20=H20a AND T4=T4a AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 4/14 losers (29%)
- **Final: n=90  W=80/L=10  WR=88.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; middle of band; RSI 30-40 weak  •  AVOID when session=ny_open

### W20.  `T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60e AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude ZS=ZS3 drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W23.  `T1=T1c AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude ZS=ZS3 drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W24.  `RSI=RSI3 AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude ZS=ZS3 drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=off_hours  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude ZS=ZS3 drops 9/13 losers (69%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=off_hours  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=330  W=132/L=198  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=330  W=132/L=198  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak

### L02.  `T1=T1c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=195  W=77/L=118  WR=39.5%
- Sharpen: sharpest is T4=T4a (57/118 of losers there)
- **Sharp: n=68  W=11/L=57  WR=16.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L03.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=190  W=75/L=115  WR=39.5%
- Sharpen: sharpest is H20=H20d (21/115 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 mildly against

### L04.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=185  W=68/L=117  WR=36.8%
- Sharpen: sharpest is session_bucket=asia (32/117 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L05.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=175  W=62/L=113  WR=35.4%
- Sharpen: sharpest is BBP=BBP1 (83/113 of losers there)
- **Sharp: n=113  W=30/L=83  WR=26.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L06.  `H20=H20e AND T1=T1c AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=174  W=64/L=110  WR=36.8%
- Sharpen: sharpest is T4=T4a (54/110 of losers there)
- **Sharp: n=72  W=18/L=54  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched lower band; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L07.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is BBP=BBP1 (75/105 of losers there)
- **Sharp: n=105  W=30/L=75  WR=28.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L08.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is BBP=BBP1 (75/105 of losers there)
- **Sharp: n=105  W=30/L=75  WR=28.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L09.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is ZS=ZS1 (90/102 of losers there)
- **Sharp: n=130  W=40/L=90  WR=30.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is ZS=ZS1 (90/102 of losers there)
- **Sharp: n=130  W=40/L=90  WR=30.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=62/L=93  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=london_open

### L12.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=62/L=93  WR=40.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak; session=london_open

### L13.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=62/L=93  WR=40.0%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak; session=london_open

### L14.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=57/L=89  WR=39.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open

### L15.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=57/L=89  WR=39.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open

### L16.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=57/L=89  WR=39.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open

### L17.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=144  W=54/L=90  WR=37.5%
- Sharpen: sharpest is T1=T1a (90/90 of losers there)
- **Sharp: n=130  W=40/L=90  WR=30.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L18.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=144  W=54/L=90  WR=37.5%
- Sharpen: sharpest is T1=T1a (90/90 of losers there)
- **Sharp: n=130  W=40/L=90  WR=30.8%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L19.  `T1=T1c AND T4=T4a AND BBP=BBP1`
- Raw: n=143  W=48/L=95  WR=33.6%
- Sharpen: sharpest is session_bucket=asia (31/95 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched lower band  •  ONLY when session=asia

### L20.  `T1=T1c AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=143  W=48/L=95  WR=33.6%
- Sharpen: sharpest is session_bucket=asia (31/95 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L21.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is H20=H20d (34/87 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 mildly against

### L22.  `H60=H60e AND T4=T4c AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=142  W=52/L=90  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=52/L=90  WR=36.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band; RSI 30-40 weak

### L23.  `T4=T4c AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=142  W=52/L=90  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=52/L=90  WR=36.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; middle of band; RSI 30-40 weak

### L24.  `T1=T1c AND T4=T4c AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=141  W=54/L=87  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=141  W=54/L=87  WR=38.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; middle of band; RSI 30-40 weak

### L25.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=135  W=46/L=89  WR=34.1%
- Sharpen: sharpest is T4=T4c (62/89 of losers there)
- **Sharp: n=86  W=24/L=62  WR=27.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/35) | H20e(37/45) |
| H60 | H60a(53/46) | H60e(47/54) |
| T1 | T1a(55/45) | T1c(45/55) |
| T4 | T4c(53/48) | T4a(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
