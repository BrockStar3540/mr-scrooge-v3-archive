# EUR_CAD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,672**  (W=1,688 / L=984)  -  WR: **63.2%**

## Session distribution

- ny_mid: n=1048  W=665/L=383  WR=63.5%
- ny_open: n=586  W=357/L=229  WR=60.9%
- london_open: n=530  W=350/L=180  WR=66.0%
- london: n=265  W=167/L=98  WR=63.0%
- ny_close: n=111  W=70/L=41  WR=63.1%
- asia: n=83  W=51/L=32  WR=61.4%
- asia_late: n=49  W=28/L=21  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=173  W=148/L=25  WR=85.5%
- Refine: exclude H20=H20b drops 14/25 losers (56%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 slightly aligned

### W02.  `T1=T1c AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=170  W=145/L=25  WR=85.3%
- Refine: exclude H20=H20b drops 14/25 losers (56%)
- **Final: n=105  W=94/L=11  WR=89.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W03.  `H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=167  W=143/L=24  WR=85.6%
- Refine: exclude H20=H20b drops 14/24 losers (58%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W04.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=167  W=143/L=24  WR=85.6%
- Refine: exclude H20=H20b drops 14/24 losers (58%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=167  W=143/L=24  WR=85.6%
- Refine: exclude H20=H20b drops 14/24 losers (58%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W06.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=158  W=139/L=19  WR=88.0%
- Refine: exclude H60=H60e drops 19/19 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W07.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=147  W=126/L=21  WR=85.7%
- Refine: exclude H20=H20b drops 14/21 losers (67%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W08.  `H20=H20b AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude ZS=ZS3 drops 13/18 losers (72%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W09.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=129  W=112/L=17  WR=86.8%
- Refine: exclude H60=H60e drops 17/17 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W10.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude T4=T4c drops 10/16 losers (62%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W11.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude T4=T4c drops 10/16 losers (62%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W12.  `H60=H60d AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude RSI=RSI2 drops 7/17 losers (41%)
- **Final: n=109  W=99/L=10  WR=90.8%**
- **Dir: ?**  •  HTF60 mildly against; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 30-40 weak

### W13.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude RSI=RSI3 drops 15/17 losers (88%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W14.  `T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude T4=T4a drops 11/11 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W15.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: no further refinement
- **Final: n=102  W=88/L=14  WR=86.3%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong

### W16.  `BBP=BBP1 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=101  W=90/L=11  WR=89.1%
- Refine: exclude H20=H20e drops 10/11 losers (91%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W17.  `BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=101  W=90/L=11  WR=89.1%
- Refine: exclude H20=H20e drops 10/11 losers (91%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W18.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude H20=H20a drops 2/13 losers (15%)
- **Final: n=99  W=88/L=11  WR=88.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W19.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude H20=H20a drops 2/13 losers (15%)
- **Final: n=99  W=88/L=11  WR=88.9%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60d AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20e drops 13/14 losers (93%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF60 mildly against; lower third; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W21.  `H60=H60d AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF60 mildly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W22.  `H60=H60d AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF60 mildly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W23.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude H60=H60e drops 9/12 losers (75%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 strongly against

### W24.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude ZS=ZS3 drops 5/9 losers (56%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is H20=H20d (28/70 of losers there)
- **Sharp: n=34  W=6/L=28  WR=17.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L02.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (34/63 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L03.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=104  W=32/L=72  WR=30.8%
- Sharpen: sharpest is H20=H20e (24/72 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L04.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=101  W=36/L=65  WR=35.6%
- Sharpen: sharpest is H20=H20e (36/65 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L05.  `H60=H60b AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (46/59 of losers there)
- **Sharp: n=69  W=23/L=46  WR=33.3%**
- **Dir: ?**  •  HTF60 slightly aligned; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L06.  `H20=H20d AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is RSI=RSI3 (29/59 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L07.  `H20=H20d AND T4=T4c AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (36/54 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (19/53 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L09.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (19/53 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (19/53 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L11.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=87  W=31/L=56  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (38/56 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L12.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=87  W=31/L=56  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (38/56 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20d AND H60=H60a AND T4=T4c`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is BBP=BBP2 (16/52 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when lower third

### L14.  `H20=H20d AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is BBP=BBP2 (16/52 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when lower third

### L15.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=83  W=26/L=57  WR=31.3%
- Sharpen: sharpest is T4=T4c (29/57 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L16.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T4=T4c (39/48 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L17.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T4=T4c (39/48 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L18.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T4=T4c (39/48 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60b AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is T1=T1c (33/47 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  HTF60 slightly aligned; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L20.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=75  W=27/L=48  WR=36.0%
- Sharpen: sharpest is H20=H20d (20/48 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L21.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (39/46 of losers there)
- **Sharp: n=53  W=14/L=39  WR=26.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L22.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H20=H20d (20/48 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L23.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=73  W=25/L=48  WR=34.2%
- Sharpen: sharpest is H20=H20d (20/48 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L24.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H60=H60c (19/46 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 neutral

### L25.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (18/42 of losers there)
- **Sharp: n=23  W=5/L=18  WR=21.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(26/17) | H20e(17/26) |
| H60 | H60a(39/33) | H60e(31/39) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
