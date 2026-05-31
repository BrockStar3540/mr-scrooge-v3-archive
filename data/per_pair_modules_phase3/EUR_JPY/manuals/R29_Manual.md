# EUR_JPY — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,496**  (W=1,502 / L=994)  -  WR: **60.2%**

## Session distribution

- asia: n=708  W=445/L=263  WR=62.9%
- london_open: n=540  W=309/L=231  WR=57.2%
- ny_close: n=432  W=259/L=173  WR=60.0%
- ny_mid: n=267  W=150/L=117  WR=56.2%
- london: n=247  W=153/L=94  WR=61.9%
- asia_late: n=109  W=64/L=45  WR=58.7%
- off_hours: n=107  W=67/L=40  WR=62.6%
- ny_open: n=86  W=55/L=31  WR=64.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude BBP=BBP2 drops 17/17 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when lower third

### W02.  `H20=H20e AND T1=T1a AND ZS=ZS1`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude RSI=RSI0 drops 6/13 losers (46%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI<20 extreme oversold

### W03.  `H20=H20e AND T4=T4a AND ZS=ZS1`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude RSI=RSI0 drops 6/13 losers (46%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI<20 extreme oversold

### W04.  `H20=H20e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude RSI=RSI0 drops 6/13 losers (46%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  AVOID when RSI<20 extreme oversold

### W05.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude RSI=RSI0 drops 6/13 losers (46%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI<20 extreme oversold

### W06.  `H20=H20e AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude RSI=RSI0 drops 6/13 losers (46%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI<20 extreme oversold

### W07.  `H20=H20e AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude RSI=RSI0 drops 6/13 losers (46%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI<20 extreme oversold

### W08.  `T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20d drops 12/14 losers (86%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W09.  `T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20d drops 12/14 losers (86%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W10.  `ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20d drops 12/14 losers (86%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20d drops 12/14 losers (86%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W12.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20d drops 12/14 losers (86%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W13.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20d drops 12/14 losers (86%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W14.  `H60=H60a AND RSI=RSI1 AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H20=H20d drops 10/10 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when HTF20 mildly against

### W15.  `H20=H20b AND T1=T1c AND session_bucket=asia`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W16.  `H20=H20b AND T4=T4c AND session_bucket=asia`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W17.  `H20=H20b AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; session=asia  •  AVOID when RSI 40-50 lower neutral

### W18.  `H20=H20b AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W19.  `H20=H20b AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20b AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W21.  `H20=H20a AND H60=H60e AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude ZS=ZS2 drops 8/9 losers (89%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=asia  •  AVOID when zscore -2 to -1 oversold

### W22.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude ZS=ZS2 drops 8/9 losers (89%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W23.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude ZS=ZS2 drops 8/9 losers (89%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W24.  `H20=H20a AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude ZS=ZS2 drops 8/9 losers (89%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=asia  •  AVOID when zscore -2 to -1 oversold

### W25.  `H20=H20e AND H60=H60d AND session_bucket=asia`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude ZS=ZS3 drops 5/8 losers (62%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; session=asia  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4c AND RSI=RSI1`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is session_bucket=asia (30/97 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L02.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is session_bucket=asia (30/97 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L03.  `H20=H20a AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is session_bucket=asia (30/97 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L04.  `H60=H60e AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=125  W=40/L=85  WR=32.0%
- Sharpen: sharpest is ZS=ZS1 (51/85 of losers there)
- **Sharp: n=57  W=6/L=51  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is H20=H20e (18/63 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L06.  `H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is H20=H20e (18/63 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L07.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is H20=H20e (18/63 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L08.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is H20=H20e (18/63 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L09.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is H20=H20e (18/63 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L10.  `T1=T1c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 20-30 oversold  •  ONLY when session=asia

### L11.  `T4=T4c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold  •  ONLY when session=asia

### L12.  `BBP=BBP1 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  just touched lower band; RSI 20-30 oversold  •  ONLY when session=asia

### L13.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND RSI=RSI1`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold  •  ONLY when session=asia

### L14.  `T1=T1c AND BBP=BBP1 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L15.  `T1=T1c AND BBP=BBP1 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band; RSI 20-30 oversold  •  ONLY when session=asia

### L16.  `T4=T4c AND BBP=BBP1 AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L17.  `T4=T4c AND BBP=BBP1 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band; RSI 20-30 oversold  •  ONLY when session=asia

### L18.  `BBP=BBP1 AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  just touched lower band; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L19.  `H20=H20a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=92  W=31/L=61  WR=33.7%
- Sharpen: sharpest is session_bucket=london_open (27/61 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L20.  `H60=H60b AND T1=T1c AND RSI=RSI2`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (18/56 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H60=H60b AND T4=T4c AND RSI=RSI2`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (18/56 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H60=H60b AND RSI=RSI2 AND direction_exec=long`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (18/56 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `H60=H60b AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (18/56 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H60=H60b AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (18/56 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H60=H60b AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (18/56 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(37/30) | H20a(29/36) |
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
