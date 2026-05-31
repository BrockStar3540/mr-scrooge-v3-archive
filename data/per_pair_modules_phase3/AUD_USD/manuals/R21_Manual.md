# AUD_USD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,586**  (W=1,656 / L=930)  -  WR: **64.0%**

## Session distribution

- asia: n=734  W=485/L=249  WR=66.1%
- ny_open: n=424  W=274/L=150  WR=64.6%
- ny_mid: n=381  W=246/L=135  WR=64.6%
- london_open: n=349  W=220/L=129  WR=63.0%
- ny_close: n=284  W=182/L=102  WR=64.1%
- london: n=270  W=165/L=105  WR=61.1%
- asia_late: n=74  W=47/L=27  WR=63.5%
- off_hours: n=70  W=37/L=33  WR=52.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 5/15 losers (33%)
- **Final: n=95  W=85/L=10  WR=89.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W02.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude ZS=ZS5 drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W03.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude ZS=ZS5 drops 11/11 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W04.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W05.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP1 drops 6/10 losers (60%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W06.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP6 drops 10/10 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when deep above upper band

### W07.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI5 drops 8/10 losers (80%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W08.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude RSI=RSI5 drops 8/11 losers (73%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when RSI 60-70 strong

### W09.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude ZS=ZS6 drops 6/7 losers (86%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore >+3 extreme

### W10.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W11.  `T1=T1a AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when strategy=bravo_expansion_continuation

### W12.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W13.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W14.  `BBP=BBP6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI3 drops 4/9 losers (44%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: SHORT**  •  deep above upper band; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W15.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude BBP=BBP6 drops 8/9 losers (89%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when deep above upper band

### W16.  `H20=H20d AND T1=T1c AND RSI=RSI3`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=london_open drops 6/9 losers (67%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W17.  `H20=H20d AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude BBP=BBP6 drops 4/8 losers (50%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when deep above upper band

### W18.  `H60=H60e AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W19.  `H60=H60e AND ZS=ZS6 AND direction_exec=short`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W20.  `BBP=BBP6 AND ZS=ZS6 AND direction_exec=short`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W21.  `H60=H60e AND BBP=BBP6 AND ZS=ZS6 AND direction_exec=short`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; zscore >+3 extreme  •  AVOID when HTF20 neutral

### W22.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W23.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W24.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W25.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND ZS=ZS5`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (36/78 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L02.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=121  W=43/L=78  WR=35.5%
- Sharpen: sharpest is session_bucket=asia (27/78 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L03.  `H20=H20e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=121  W=43/L=78  WR=35.5%
- Sharpen: sharpest is session_bucket=asia (27/78 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L04.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is ZS=ZS5 (36/74 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is session_bucket=london (14/71 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L06.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is session_bucket=london (19/65 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L07.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is session_bucket=london (19/65 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=london

### L08.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is session_bucket=london (19/65 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london

### L09.  `H60=H60e AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is BBP=BBP6 (29/62 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L10.  `H20=H20e AND T4=T4a AND ZS=ZS5`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is H60=H60e (59/59 of losers there)
- **Sharp: n=90  W=31/L=59  WR=34.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L11.  `H20=H20e AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H60=H60e (57/57 of losers there)
- **Sharp: n=84  W=27/L=57  WR=32.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L12.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=90  W=31/L=59  WR=34.4%
- Sharpen: sharpest is BBP=BBP6 (28/59 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L13.  `H20=H20e AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=31/L=59  WR=34.4%
- Sharpen: sharpest is BBP=BBP6 (28/59 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L14.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is ZS=ZS6 (21/53 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore >+3 extreme

### L15.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is ZS=ZS4 (15/51 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L16.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is BBP=BBP2 (13/48 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when lower third

### L17.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is session_bucket=london (13/48 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L18.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is session_bucket=ny_open (11/49 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L19.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is session_bucket=ny_open (11/49 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L20.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is session_bucket=ny_open (11/49 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_open

### L21.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (31/45 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L22.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is session_bucket=london (13/47 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L23.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is session_bucket=london (13/47 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=london

### L24.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=71  W=23/L=48  WR=32.4%
- Sharpen: sharpest is ZS=ZS4 (15/48 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L25.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=71  W=23/L=48  WR=32.4%
- Sharpen: sharpest is ZS=ZS4 (15/48 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
