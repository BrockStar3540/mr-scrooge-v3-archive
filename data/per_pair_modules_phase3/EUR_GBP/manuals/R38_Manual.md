# EUR_GBP — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **965**  (W=617 / L=348)  -  WR: **63.9%**

## Session distribution

- ny_mid: n=502  W=322/L=180  WR=64.1%
- london_open: n=228  W=147/L=81  WR=64.5%
- london: n=116  W=73/L=43  WR=62.9%
- ny_open: n=62  W=42/L=20  WR=67.7%
- ny_close: n=25  W=15/L=10  WR=60.0%
- off_hours: n=18  W=12/L=6  WR=66.7%
- asia: n=14  W=6/L=8  WR=42.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=196  W=167/L=29  WR=85.2%
- Refine: exclude H20=H20a drops 24/29 losers (83%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=148  W=128/L=20  WR=86.5%
- Refine: exclude H20=H20e drops 11/20 losers (55%)
- **Final: n=137  W=128/L=9  WR=93.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 strongly against

### W03.  `T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=117  W=108/L=9  WR=92.3%
- Refine: exclude T4=T4a drops 6/9 losers (67%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 4h trend WITH trade

### W04.  `T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude H60=H60e drops 8/16 losers (50%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when HTF60 strongly against

### W05.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude H60=H60e drops 6/13 losers (46%)
- **Final: n=103  W=96/L=7  WR=93.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when HTF60 strongly against

### W06.  `T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=106  W=94/L=12  WR=88.7%
- Refine: exclude session_bucket=london drops 9/12 losers (75%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W07.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=106  W=94/L=12  WR=88.7%
- Refine: exclude session_bucket=london drops 9/12 losers (75%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W08.  `T1=T1a AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude H60=H60e drops 6/13 losers (46%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W09.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=87/L=8  WR=91.6%
- Refine: exclude T4=T4a drops 5/8 losers (62%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 4h trend WITH trade

### W10.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude BBP=BBP1 drops 6/9 losers (67%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when just touched lower band

### W11.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude ZS=ZS0 drops 4/13 losers (31%)
- **Final: n=85  W=76/L=9  WR=89.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore <-3 extreme

### W12.  `H20=H20a AND H60=H60d AND direction_exec=short`
- Raw: n=87  W=87/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=87  W=87/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against

### W13.  `H20=H20b AND T1=T1a AND direction_exec=short`
- Raw: n=87  W=81/L=6  WR=93.1%
- Refine: exclude T4=T4a drops 5/6 losers (83%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20e AND H60=H60a AND T4=T4a`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP4 drops 8/12 losers (67%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W15.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude H60=H60e drops 8/11 losers (73%)
- **Final: n=77  W=74/L=3  WR=96.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W16.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude H60=H60b drops 6/6 losers (100%)
- **Final: n=78  W=78/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W17.  `H20=H20e AND H60=H60a AND direction_exec=long`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP4 drops 6/10 losers (60%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  AVOID when upper third

### W18.  `H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP4 drops 6/10 losers (60%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W19.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP4 drops 6/10 losers (60%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W20.  `H20=H20a AND H60=H60d AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; session=ny_mid  •  AVOID when RSI 20-30 oversold

### W21.  `H20=H20b AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W22.  `H20=H20d AND H60=H60e AND T1=T1a`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=off_hours drops 6/10 losers (60%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=off_hours

### W23.  `H20=H20d AND T1=T1a AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=off_hours drops 6/10 losers (60%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade  •  AVOID when session=off_hours

### W24.  `H20=H20d AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=off_hours drops 6/10 losers (60%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=off_hours

### W25.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=77  W=74/L=3  WR=96.1%
- Refine: exclude strategy_id=CP1_coil_breakout_short drops 2/3 losers (67%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when strategy=CP1_coil_breakout_short

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=151  W=55/L=96  WR=36.4%
- Sharpen: sharpest is H60=H60d (32/96 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 mildly against

### L02.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is RSI=RSI3 (37/73 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L03.  `T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=103  W=33/L=70  WR=32.0%
- Sharpen: sharpest is session_bucket=ny_mid (52/70 of losers there)
- **Sharp: n=68  W=16/L=52  WR=23.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L04.  `T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is T4=T4a (26/54 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L05.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=88  W=31/L=57  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (31/57 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L06.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=86  W=29/L=57  WR=33.7%
- Sharpen: sharpest is RSI=RSI2 (31/57 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L07.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is RSI=RSI2 (31/51 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L08.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is RSI=RSI2 (31/51 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L09.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (31/51 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L10.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is H60=H60b (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 slightly aligned

### L11.  `T1=T1c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=76  W=16/L=60  WR=21.1%
- Sharpen: sharpest is H60=H60e (31/60 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF60 strongly against

### L12.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is T1=T1c (30/46 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L13.  `T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=70  W=20/L=50  WR=28.6%
- Sharpen: sharpest is session_bucket=ny_mid (37/50 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L14.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=70  W=20/L=50  WR=28.6%
- Sharpen: sharpest is session_bucket=ny_mid (37/50 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L15.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=68  W=16/L=52  WR=23.5%
- Sharpen: sharpest is T4=T4a (37/52 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is H20=H20d (24/41 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 mildly against

### L17.  `H20=H20d AND T1=T1c AND direction_exec=long`
- Raw: n=65  W=15/L=50  WR=23.1%
- Sharpen: sharpest is session_bucket=ny_mid (39/50 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L18.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is ZS=ZS5 (16/42 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=62  W=19/L=43  WR=30.6%
- Sharpen: sharpest is T4=T4a (32/43 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when 4h trend WITH trade

### L20.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=62  W=19/L=43  WR=30.6%
- Sharpen: sharpest is H20=H20d (29/43 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 mildly against

### L21.  `H20=H20b AND H60=H60a AND T1=T1c`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is RSI=RSI4 (24/41 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L22.  `H20=H20b AND T1=T1c AND direction_exec=short`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is RSI=RSI4 (24/41 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L23.  `H20=H20b AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is RSI=RSI4 (24/41 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L24.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=57  W=15/L=42  WR=26.3%
- Sharpen: sharpest is session_bucket=ny_mid (31/42 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L25.  `H20=H20e AND H60=H60b AND session_bucket=ny_mid`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is direction_exec=long (33/36 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; session=ny_mid  •  ONLY when long

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(40/26), H60d(19/13) | H60e(23/37), H60b(13/19) |
| T1 | T1a(64/38) | T1c(36/62) |
| T4 | T4c(52/43) | T4a(48/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(59/41) | long(41/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
