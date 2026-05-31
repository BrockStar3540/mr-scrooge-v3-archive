# AUD_CHF — R25 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,432**  (W=1,564 / L=868)  -  WR: **64.3%**

## Session distribution

- ny_mid: n=731  W=463/L=268  WR=63.3%
- london_open: n=422  W=271/L=151  WR=64.2%
- ny_open: n=408  W=281/L=127  WR=68.9%
- asia: n=313  W=194/L=119  WR=62.0%
- ny_close: n=241  W=145/L=96  WR=60.2%
- london: n=174  W=113/L=61  WR=64.9%
- asia_late: n=96  W=67/L=29  WR=69.8%
- off_hours: n=47  W=30/L=17  WR=63.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=134  W=121/L=13  WR=90.3%
- Refine: exclude session_bucket=ny_close drops 7/13 losers (54%)
- **Final: n=115  W=109/L=6  WR=94.8%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W02.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=99  W=93/L=6  WR=93.9%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W03.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude session_bucket=ny_close drops 7/12 losers (58%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W04.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI2 drops 8/13 losers (62%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W05.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 4h trend WITH trade

### W06.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_open  •  AVOID when 4h trend WITH trade

### W07.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude T4=T4a drops 11/13 losers (85%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 4h trend WITH trade

### W08.  `T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude ZS=ZS0 drops 7/12 losers (58%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore <-3 extreme

### W09.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=83  W=79/L=4  WR=95.2%
- Refine: exclude RSI=RSI4 drops 2/4 losers (50%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W10.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=82  W=79/L=3  WR=96.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when lower third

### W11.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=82  W=79/L=3  WR=96.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when lower third

### W12.  `H20=H20e AND T1=T1c AND RSI=RSI3`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W13.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP1 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W14.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W15.  `H20=H20b AND H60=H60a AND RSI=RSI3`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W16.  `H20=H20b AND RSI=RSI3 AND direction_exec=long`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W17.  `H20=H20b AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude session_bucket=ny_mid drops 6/7 losers (86%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W18.  `T4=T4c AND BBP=BBP6 AND session_bucket=ny_open`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude H60=H60d drops 9/9 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; session=ny_open  •  AVOID when HTF60 mildly against

### W19.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude H60=H60d drops 9/9 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W20.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude RSI=RSI2 drops 9/9 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20b AND T4=T4a AND RSI=RSI3`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W22.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=57  W=56/L=1  WR=98.2%
- Refine: no further refinement
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral

### W23.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude BBP=BBP1 drops 4/6 losers (67%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W24.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W25.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=110  W=39/L=71  WR=35.5%
- Sharpen: sharpest is RSI=RSI3 (52/71 of losers there)
- **Sharp: n=62  W=10/L=52  WR=16.1%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L02.  `H60=H60e AND T1=T1a AND BBP=BBP0`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (40/59 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L03.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (40/59 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L04.  `H20=H20e AND T1=T1a AND BBP=BBP0`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (36/55 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L05.  `H20=H20e AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (36/55 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L06.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP0`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (35/54 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L07.  `T1=T1a AND T4=T4c AND BBP=BBP0`
- Raw: n=81  W=31/L=50  WR=38.3%
- Sharpen: sharpest is RSI=RSI3 (41/50 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L08.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=79  W=12/L=67  WR=15.2%
- Sharpen: sharpest is ZS=ZS0 (21/67 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore <-3 extreme

### L09.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is T4=T4a (45/46 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L10.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is T4=T4a (45/46 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L11.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is T4=T4a (45/46 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L12.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=66  W=12/L=54  WR=18.2%
- Sharpen: sharpest is H20=H20a (45/54 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L13.  `H20=H20e AND T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is T4=T4a (28/41 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L14.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is T4=T4a (45/46 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is T4=T4a (45/46 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=65  W=19/L=46  WR=29.2%
- Sharpen: sharpest is T4=T4a (45/46 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1a AND T4=T4c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is RSI=RSI3 (37/42 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L18.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is RSI=RSI3 (26/39 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L19.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is RSI=RSI4 (9/38 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L20.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is RSI=RSI4 (9/38 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when RSI 50-60 upper neutral

### L21.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=62  W=10/L=52  WR=16.1%
- Sharpen: sharpest is ZS=ZS0 (20/52 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore <-3 extreme

### L22.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=58  W=12/L=46  WR=20.7%
- Sharpen: sharpest is H20=H20a (13/46 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L23.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is T4=T4a (36/37 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L24.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is T4=T4a (36/37 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L25.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is T4=T4a (36/37 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(35/41) |
| H60 | H60e(47/41) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
