# EUR_CHF — R35 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **701**  (W=460 / L=241)  -  WR: **65.6%**

## Session distribution

- london_open: n=187  W=116/L=71  WR=62.0%
- ny_open: n=161  W=114/L=47  WR=70.8%
- ny_mid: n=137  W=89/L=48  WR=65.0%
- london: n=87  W=56/L=31  WR=64.4%
- asia: n=48  W=32/L=16  WR=66.7%
- asia_late: n=42  W=28/L=14  WR=66.7%
- ny_close: n=39  W=25/L=14  WR=64.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude RSI=RSI2 drops 8/13 losers (62%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  AVOID when RSI 30-40 weak

### W02.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/13 losers (69%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/13 losers (69%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_mid drops 9/13 losers (69%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W05.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W06.  `T1=T1a AND T4=T4c AND RSI=RSI2`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W07.  `T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W08.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W09.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H20=H20c drops 4/7 losers (57%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 neutral

### W10.  `H20=H20a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W11.  `H20=H20a AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W12.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W13.  `T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI3 drops 9/10 losers (90%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W14.  `T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude RSI=RSI3 drops 9/10 losers (90%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W15.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude RSI=RSI3 drops 9/10 losers (90%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W16.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 3/10 losers (30%)
- **Final: n=65  W=58/L=7  WR=89.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W17.  `T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W19.  `T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W20.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W21.  `T1=T1a AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20a AND T4=T4c AND RSI=RSI2`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when 1h trend AGAINST trade

### W23.  `H20=H20b AND T1=T1c AND direction_exec=long`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  AVOID when session=london

### W24.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude H20=H20c drops 4/8 losers (50%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 neutral

### W25.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude H20=H20c drops 4/8 losers (50%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=57  W=16/L=41  WR=28.1%
- Sharpen: sharpest is H20=H20e (25/41 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=56  W=12/L=44  WR=21.4%
- Sharpen: sharpest is ZS=ZS2 (23/44 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L03.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=56  W=12/L=44  WR=21.4%
- Sharpen: sharpest is ZS=ZS2 (23/44 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L04.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=56  W=12/L=44  WR=21.4%
- Sharpen: sharpest is ZS=ZS2 (23/44 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L05.  `H20=H20e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (24/32 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; lower third  •  ONLY when RSI 30-40 weak

### L06.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (24/32 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L07.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=50  W=15/L=35  WR=30.0%
- Sharpen: sharpest is H20=H20e (20/35 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 strongly against

### L08.  `H20=H20e AND T1=T1c AND ZS=ZS2`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is RSI=RSI2 (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L09.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is RSI=RSI2 (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L10.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=48  W=12/L=36  WR=25.0%
- Sharpen: sharpest is H20=H20e (20/36 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  ONLY when HTF20 strongly against

### L11.  `H20=H20e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=45  W=15/L=30  WR=33.3%
- Sharpen: sharpest is RSI=RSI2 (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20e AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=45  W=15/L=30  WR=33.3%
- Sharpen: sharpest is RSI=RSI2 (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L13.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=45  W=15/L=30  WR=33.3%
- Sharpen: sharpest is RSI=RSI2 (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L14.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is H20=H20e (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L15.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is H20=H20e (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L16.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is H20=H20e (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L17.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is H20=H20e (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L18.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is H20=H20e (23/30 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L19.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=42  W=9/L=33  WR=21.4%
- Sharpen: sharpest is RSI=RSI2 (17/33 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 30-40 weak

### L20.  `H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=41  W=12/L=29  WR=29.3%
- Sharpen: sharpest is H20=H20e (13/29 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: LONG**  •  HTF60 strongly against; session=london_open  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=38  W=12/L=26  WR=31.6%
- Sharpen: sharpest is H20=H20a (8/26 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L22.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=38  W=12/L=26  WR=31.6%
- Sharpen: sharpest is H20=H20a (8/26 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1c AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is RSI=RSI2 (14/25 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=london_open  •  ONLY when RSI 30-40 weak

### L24.  `H20=H20e AND H60=H60e AND ZS=ZS2`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is RSI=RSI2 (16/23 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (11/23 of losers there)
- **Sharp: n=14  W=3/L=11  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(37/26), H20b(18/12) | H20e(26/37) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(54/45) | T4a(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | ny_open(25/20) | — |

*Read: `bucket(winner%/loser%)`.*
