# NZD_JPY — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,300**  (W=1,457 / L=843)  -  WR: **63.3%**

## Session distribution

- asia: n=756  W=484/L=272  WR=64.0%
- ny_mid: n=575  W=369/L=206  WR=64.2%
- london_open: n=436  W=271/L=165  WR=62.2%
- london: n=141  W=88/L=53  WR=62.4%
- ny_close: n=131  W=88/L=43  WR=67.2%
- ny_open: n=113  W=69/L=44  WR=61.1%
- off_hours: n=106  W=63/L=43  WR=59.4%
- asia_late: n=42  W=25/L=17  WR=59.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude RSI=RSI3 drops 17/18 losers (94%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W02.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 4/13 losers (31%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W03.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W04.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude H60=H60e drops 10/12 losers (83%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W05.  `T4=T4a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude H60=H60a drops 11/11 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W06.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude H60=H60a drops 11/11 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W07.  `T4=T4a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude H60=H60a drops 11/11 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W08.  `T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; session=asia  •  AVOID when HTF60 strongly against

### W09.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 strongly against

### W10.  `H20=H20a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60e drops 5/10 losers (50%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 strongly against

### W11.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W12.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=75  W=68/L=7  WR=90.7%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS3 drops 7/8 losers (88%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H60=H60a drops 11/11 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF60 aligned WITH trade

### W15.  `H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude RSI=RSI3 drops 9/9 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W16.  `T1=T1a AND T4=T4a AND BBP=BBP1`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 40-50 lower neutral

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W18.  `H60=H60b AND T4=T4a AND direction_exec=short`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 5/9 losers (56%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_mid

### W19.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude BBP=BBP0 drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W20.  `T1=T1a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude BBP=BBP0 drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W21.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H60=H60d drops 5/10 losers (50%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W22.  `H60=H60a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude RSI=RSI3 drops 9/9 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60e AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude T4=T4a drops 7/9 losers (78%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  AVOID when 4h trend WITH trade

### W24.  `BBP=BBP1 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  just touched lower band; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

### W25.  `BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H20=H20d (14/51 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L02.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H20=H20d (14/51 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L03.  `H60=H60e AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H20=H20d (14/51 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=81  W=32/L=49  WR=39.5%
- Sharpen: sharpest is T1=T1c (28/49 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend AGAINST trade

### L05.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is H60=H60e (16/52 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is ZS=ZS1 (11/48 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is ZS=ZS1 (11/48 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H60=H60a (24/47 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is T1=T1a (26/43 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is ZS=ZS1 (15/42 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20d AND H60=H60e AND RSI=RSI4`
- Raw: n=66  W=21/L=45  WR=31.8%
- Sharpen: sharpest is T1=T1c (34/45 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20d AND RSI=RSI4 AND direction_exec=short`
- Raw: n=66  W=21/L=45  WR=31.8%
- Sharpen: sharpest is T1=T1c (34/45 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20d AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=66  W=21/L=45  WR=31.8%
- Sharpen: sharpest is T1=T1c (34/45 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is ZS=ZS1 (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=61  W=19/L=42  WR=31.1%
- Sharpen: sharpest is H60=H60e (16/42 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L17.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=asia (24/38 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L18.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=asia (24/38 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L19.  `H20=H20d AND T4=T4c AND RSI=RSI4`
- Raw: n=58  W=20/L=38  WR=34.5%
- Sharpen: sharpest is T1=T1c (31/38 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L20.  `BBP=BBP1 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is T1=T1c (17/34 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L21.  `BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is T1=T1c (17/34 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20d AND T1=T1c AND RSI=RSI4`
- Raw: n=55  W=13/L=42  WR=23.6%
- Sharpen: sharpest is T4=T4c (31/42 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is ZS=ZS1 (11/36 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: sharpest is T1=T1a (23/37 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is session_bucket=asia (20/34 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/34) | H20e(34/42), H20d(6/11) |
| H60 | H60a(44/39) | H60e(38/44) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
