# EUR_AUD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,771**  (W=1,723 / L=1,048)  -  WR: **62.2%**

## Session distribution

- asia: n=1426  W=900/L=526  WR=63.1%
- ny_close: n=377  W=228/L=149  WR=60.5%
- london_open: n=337  W=214/L=123  WR=63.5%
- london: n=226  W=148/L=78  WR=65.5%
- ny_open: n=154  W=79/L=75  WR=51.3%
- off_hours: n=138  W=85/L=53  WR=61.6%
- asia_late: n=110  W=68/L=42  WR=61.8%
- ny_mid: n=3  W=1/L=2  WR=33.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=176  W=156/L=20  WR=88.6%
- Refine: exclude ZS=ZS2 drops 16/20 losers (80%)
- **Final: n=131  W=127/L=4  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W02.  `H20=H20a AND H60=H60a AND RSI=RSI3`
- Raw: n=142  W=136/L=6  WR=95.8%
- Refine: exclude session_bucket=asia_late drops 3/6 losers (50%)
- **Final: n=135  W=132/L=3  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W03.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=142  W=136/L=6  WR=95.8%
- Refine: exclude session_bucket=asia_late drops 3/6 losers (50%)
- **Final: n=135  W=132/L=3  WR=97.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W04.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=142  W=136/L=6  WR=95.8%
- Refine: exclude session_bucket=asia_late drops 3/6 losers (50%)
- **Final: n=135  W=132/L=3  WR=97.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W05.  `H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude RSI=RSI4 drops 10/18 losers (56%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W06.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude RSI=RSI4 drops 10/18 losers (56%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W07.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude RSI=RSI4 drops 10/18 losers (56%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=138  W=123/L=15  WR=89.1%
- Refine: exclude RSI=RSI4 drops 7/15 losers (47%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=136  W=121/L=15  WR=89.0%
- Refine: exclude RSI=RSI4 drops 7/15 losers (47%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W10.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=136  W=121/L=15  WR=89.0%
- Refine: exclude RSI=RSI4 drops 7/15 losers (47%)
- **Final: n=118  W=110/L=8  WR=93.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=133  W=120/L=13  WR=90.2%
- Refine: exclude ZS=ZS2 drops 12/13 losers (92%)
- **Final: n=99  W=98/L=1  WR=99.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W12.  `T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=133  W=120/L=13  WR=90.2%
- Refine: exclude ZS=ZS2 drops 12/13 losers (92%)
- **Final: n=99  W=98/L=1  WR=99.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W13.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=133  W=120/L=13  WR=90.2%
- Refine: exclude ZS=ZS2 drops 12/13 losers (92%)
- **Final: n=99  W=98/L=1  WR=99.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W14.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H20=H20a drops 16/18 losers (89%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=asia drops 14/17 losers (82%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W16.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=asia drops 14/17 losers (82%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W17.  `H20=H20a AND T1=T1c AND RSI=RSI3`
- Raw: n=108  W=105/L=3  WR=97.2%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W18.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude H20=H20a drops 15/16 losers (94%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W19.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=103  W=101/L=2  WR=98.1%
- Refine: exclude ZS=ZS2 drops 2/2 losers (100%)
- **Final: n=82  W=82/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W20.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=103  W=101/L=2  WR=98.1%
- Refine: exclude ZS=ZS2 drops 2/2 losers (100%)
- **Final: n=82  W=82/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W21.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4a drops 10/14 losers (71%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=96  W=91/L=5  WR=94.8%
- Refine: exclude BBP=BBP2 drops 5/5 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when lower third

### W23.  `T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude H20=H20e drops 8/13 losers (62%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 strongly against

### W24.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is RSI=RSI4 (53/83 of losers there)
- **Sharp: n=74  W=21/L=53  WR=28.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L02.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is T4=T4c (45/74 of losers there)
- **Sharp: n=59  W=14/L=45  WR=23.7%**
- **Dir: SHORT**  •  just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L03.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (55/72 of losers there)
- **Sharp: n=76  W=21/L=55  WR=27.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L04.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is H20=H20e (52/66 of losers there)
- **Sharp: n=62  W=10/L=52  WR=16.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L05.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is H20=H20e (52/66 of losers there)
- **Sharp: n=62  W=10/L=52  WR=16.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L06.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is H20=H20e (52/66 of losers there)
- **Sharp: n=62  W=10/L=52  WR=16.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L07.  `H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is RSI=RSI3 (32/68 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L08.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is RSI=RSI3 (32/68 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is RSI=RSI3 (32/68 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L10.  `H20=H20e AND H60=H60e AND RSI=RSI3`
- Raw: n=103  W=28/L=75  WR=27.2%
- Sharpen: sharpest is ZS=ZS1 (37/75 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=103  W=28/L=75  WR=27.2%
- Sharpen: sharpest is ZS=ZS1 (37/75 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=103  W=28/L=75  WR=27.2%
- Sharpen: sharpest is ZS=ZS1 (37/75 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=103  W=37/L=66  WR=35.9%
- Sharpen: sharpest is RSI=RSI4 (36/66 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L14.  `T1=T1a AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=103  W=37/L=66  WR=35.9%
- Sharpen: sharpest is RSI=RSI4 (36/66 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=99  W=30/L=69  WR=30.3%
- Sharpen: sharpest is RSI=RSI3 (32/69 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L16.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is RSI=RSI5 (21/60 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L17.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T1=T1a (59/60 of losers there)
- **Sharp: n=82  W=23/L=59  WR=28.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L18.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is T1=T1a (59/60 of losers there)
- **Sharp: n=82  W=23/L=59  WR=28.0%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L19.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=98  W=30/L=68  WR=30.6%
- Sharpen: sharpest is RSI=RSI3 (32/68 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L20.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=98  W=30/L=68  WR=30.6%
- Sharpen: sharpest is RSI=RSI3 (32/68 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L21.  `H60=H60e AND T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=96  W=37/L=59  WR=38.5%
- Sharpen: sharpest is H20=H20e (59/59 of losers there)
- **Sharp: n=82  W=23/L=59  WR=28.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L22.  `H20=H20e AND T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is H60=H60e (59/59 of losers there)
- **Sharp: n=82  W=23/L=59  WR=28.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is H60=H60e (45/56 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L24.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is H20=H20e (45/58 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L25.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=88  W=26/L=62  WR=29.5%
- Sharpen: sharpest is direction_exec=long (45/62 of losers there)
- **Sharp: n=58  W=13/L=45  WR=22.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  ONLY when long

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/43) | H20e(41/49) |
| H60 | H60a(50/43) | H60e(42/49) |
| T1 | T1c(56/45) | T1a(44/55) |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/47) | long(46/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
