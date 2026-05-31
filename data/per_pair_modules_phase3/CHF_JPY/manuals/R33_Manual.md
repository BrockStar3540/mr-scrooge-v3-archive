# CHF_JPY — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,771**  (W=2,114 / L=1,657)  -  WR: **56.1%**

## Session distribution

- ny_mid: n=1282  W=712/L=570  WR=55.5%
- asia: n=634  W=338/L=296  WR=53.3%
- london_open: n=580  W=303/L=277  WR=52.2%
- ny_close: n=514  W=314/L=200  WR=61.1%
- ny_open: n=337  W=195/L=142  WR=57.9%
- london: n=318  W=192/L=126  WR=60.4%
- asia_late: n=96  W=55/L=41  WR=57.3%
- off_hours: n=10  W=5/L=5  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude T4=T4c drops 9/10 losers (90%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W02.  `T1=T1a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude H20=H20c drops 5/8 losers (62%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W03.  `H60=H60e AND T1=T1a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude H20=H20c drops 5/8 losers (62%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W04.  `T1=T1a AND BBP=BBP5 AND session_bucket=ny_mid`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude H20=H20c drops 5/7 losers (71%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; session=ny_mid  •  AVOID when HTF20 neutral

### W05.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude H20=H20c drops 5/7 losers (71%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W06.  `H60=H60e AND T1=T1a AND BBP=BBP5`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude H20=H20b drops 4/5 losers (80%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band  •  AVOID when HTF20 slightly aligned

### W07.  `H60=H60e AND T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude H20=H20b drops 4/5 losers (80%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W08.  `T1=T1a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=71  W=68/L=3  WR=95.8%
- Refine: exclude H20=H20b drops 2/3 losers (67%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched upper band  •  AVOID when HTF20 slightly aligned

### W09.  `H60=H60e AND T1=T1a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=71  W=68/L=3  WR=95.8%
- Refine: exclude H20=H20b drops 2/3 losers (67%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band  •  AVOID when HTF20 slightly aligned

### W10.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=71  W=68/L=3  WR=95.8%
- Refine: exclude H20=H20b drops 2/3 losers (67%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W11.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W12.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: LONG**  •  lower third; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W13.  `H60=H60a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W15.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W16.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W17.  `H20=H20a AND T1=T1a AND BBP=BBP5`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band  •  AVOID when session=asia

### W18.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP5`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; just touched upper band  •  AVOID when session=asia

### W19.  `H20=H20a AND T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W20.  `H20=H20a AND T1=T1a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band  •  AVOID when session=asia

### W21.  `H20=H20b AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude BBP=BBP4 drops 4/9 losers (44%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when upper third

### W22.  `H20=H20b AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude BBP=BBP4 drops 4/9 losers (44%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when upper third

### W23.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude session_bucket=asia drops 2/9 losers (22%)
- **Final: n=63  W=56/L=7  WR=88.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W24.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W25.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20c AND T1=T1a AND RSI=RSI3`
- Raw: n=250  W=94/L=156  WR=37.6%
- Sharpen: sharpest is ZS=ZS1 (35/156 of losers there)
- **Sharp: n=36  W=1/L=35  WR=2.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=206  W=76/L=130  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (47/130 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L03.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=206  W=76/L=130  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (47/130 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L04.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=206  W=76/L=130  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (47/130 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L05.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=176  W=66/L=110  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_mid (43/110 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L06.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=176  W=66/L=110  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_mid (43/110 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L07.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=176  W=66/L=110  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_mid (43/110 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L08.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=176  W=66/L=110  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_mid (43/110 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L09.  `H20=H20c AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=145  W=53/L=92  WR=36.6%
- Sharpen: sharpest is H60=H60a (60/92 of losers there)
- **Sharp: n=75  W=15/L=60  WR=20.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20c AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=140  W=48/L=92  WR=34.3%
- Sharpen: sharpest is T1=T1a (60/92 of losers there)
- **Sharp: n=75  W=15/L=60  WR=20.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when 1h trend WITH trade

### L11.  `H20=H20c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=140  W=48/L=92  WR=34.3%
- Sharpen: sharpest is T1=T1a (60/92 of losers there)
- **Sharp: n=75  W=15/L=60  WR=20.0%**
- **Dir: LONG**  •  HTF20 neutral; session=ny_mid  •  ONLY when 1h trend WITH trade

### L12.  `H20=H20c AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=140  W=48/L=92  WR=34.3%
- Sharpen: sharpest is T1=T1a (60/92 of losers there)
- **Sharp: n=75  W=15/L=60  WR=20.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when 1h trend WITH trade

### L13.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=139  W=47/L=92  WR=33.8%
- Sharpen: sharpest is session_bucket=ny_mid (53/92 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L14.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=134  W=50/L=84  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (50/84 of losers there)
- **Sharp: n=50  W=0/L=50  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L15.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=131  W=41/L=90  WR=31.3%
- Sharpen: sharpest is session_bucket=london_open (62/90 of losers there)
- **Sharp: n=62  W=0/L=62  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L16.  `H20=H20c AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=131  W=50/L=81  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=131  W=50/L=81  WR=38.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; lower third; RSI 40-50 lower neutral

### L17.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=129  W=42/L=87  WR=32.6%
- Sharpen: sharpest is session_bucket=london_open (42/87 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L18.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=129  W=42/L=87  WR=32.6%
- Sharpen: sharpest is session_bucket=london_open (42/87 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

### L19.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=129  W=42/L=87  WR=32.6%
- Sharpen: sharpest is H20=H20c (35/87 of losers there)
- **Sharp: n=36  W=1/L=35  WR=2.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 neutral

### L20.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=129  W=42/L=87  WR=32.6%
- Sharpen: sharpest is session_bucket=london_open (42/87 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L21.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=129  W=42/L=87  WR=32.6%
- Sharpen: sharpest is session_bucket=london_open (42/87 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L22.  `H20=H20a AND H60=H60a AND ZS=ZS1`
- Raw: n=129  W=46/L=83  WR=35.7%
- Sharpen: sharpest is RSI=RSI2 (45/83 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=129  W=46/L=83  WR=35.7%
- Sharpen: sharpest is RSI=RSI2 (45/83 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L24.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=129  W=46/L=83  WR=35.7%
- Sharpen: sharpest is RSI=RSI2 (45/83 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L25.  `T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is BBP=BBP6 (28/77 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
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
