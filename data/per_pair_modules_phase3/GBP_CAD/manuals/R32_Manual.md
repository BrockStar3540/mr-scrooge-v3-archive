# GBP_CAD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,585**  (W=2,082 / L=1,503)  -  WR: **58.1%**

## Session distribution

- ny_mid: n=1258  W=706/L=552  WR=56.1%
- london_open: n=569  W=337/L=232  WR=59.2%
- ny_open: n=551  W=317/L=234  WR=57.5%
- ny_close: n=479  W=301/L=178  WR=62.8%
- asia: n=270  W=166/L=104  WR=61.5%
- london: n=239  W=139/L=100  WR=58.2%
- asia_late: n=124  W=74/L=50  WR=59.7%
- off_hours: n=95  W=42/L=53  WR=44.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude ZS=ZS2 drops 15/18 losers (83%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W02.  `T4=T4a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude ZS=ZS2 drops 15/18 losers (83%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W03.  `H60=H60b AND T4=T4a AND RSI=RSI1`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude ZS=ZS2 drops 14/16 losers (88%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when zscore -2 to -1 oversold

### W04.  `H60=H60b AND T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude ZS=ZS2 drops 14/16 losers (88%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when zscore -2 to -1 oversold

### W05.  `H60=H60b AND T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude ZS=ZS2 drops 14/16 losers (88%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when zscore -2 to -1 oversold

### W06.  `H20=H20a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H60=H60c drops 9/10 losers (90%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 neutral

### W07.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W08.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H60=H60c drops 9/10 losers (90%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 neutral

### W09.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H60=H60c drops 9/10 losers (90%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when HTF60 neutral

### W10.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H60=H60c drops 9/10 losers (90%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 neutral

### W11.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60a drops 12/12 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W12.  `H20=H20a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI1 drops 3/7 losers (43%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=asia  •  AVOID when RSI 20-30 oversold

### W13.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude H60=H60c drops 9/10 losers (90%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 neutral

### W14.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude H60=H60c drops 9/10 losers (90%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 neutral

### W15.  `H20=H20a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H60=H60c drops 3/6 losers (50%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 neutral

### W16.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=72  W=66/L=6  WR=91.7%
- Refine: exclude H60=H60c drops 3/6 losers (50%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 neutral

### W17.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W18.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W19.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W20.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20b AND RSI=RSI0 AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP0 drops 3/5 losers (60%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI<20 extreme oversold; session=ny_mid  •  AVOID when deep below lower band

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI0`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP1 drops 4/5 losers (80%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI0`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP1 drops 4/5 losers (80%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W24.  `H60=H60a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP1 drops 4/5 losers (80%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W25.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI0`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP1 drops 4/5 losers (80%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=198  W=74/L=124  WR=37.4%
- Sharpen: sharpest is T1=T1a (59/124 of losers there)
- **Sharp: n=82  W=23/L=59  WR=28.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_mid  •  ONLY when 1h trend WITH trade

### L02.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=182  W=72/L=110  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=182  W=72/L=110  WR=39.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_mid

### L03.  `T4=T4c AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=142  W=52/L=90  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (33/90 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H60=H60d AND T1=T1c AND RSI=RSI1`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H20=H20e (26/86 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L05.  `H60=H60d AND RSI=RSI1 AND direction_exec=long`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H20=H20e (26/86 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L06.  `H60=H60d AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H20=H20e (26/86 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L07.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=138  W=49/L=89  WR=35.5%
- Sharpen: sharpest is direction_exec=short (89/89 of losers there)
- **Sharp: n=125  W=36/L=89  WR=28.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when short

### L08.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=137  W=48/L=89  WR=35.0%
- Sharpen: sharpest is T1=T1a (89/89 of losers there)
- **Sharp: n=125  W=36/L=89  WR=28.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L09.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=136  W=49/L=87  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=136  W=49/L=87  WR=36.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_mid

### L10.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=131  W=39/L=92  WR=29.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=131  W=39/L=92  WR=29.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral

### L11.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=125  W=36/L=89  WR=28.8%
- Sharpen: sharpest is BBP=BBP3 (21/89 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when middle of band

### L12.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=124  W=44/L=80  WR=35.5%
- Sharpen: sharpest is ZS=ZS1 (27/80 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=44/L=80  WR=35.5%
- Sharpen: sharpest is ZS=ZS1 (27/80 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H20=H20b AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is ZS=ZS1 (37/76 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H20=H20b AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is ZS=ZS1 (37/76 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (51/73 of losers there)
- **Sharp: n=67  W=16/L=51  WR=23.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when lower third

### L17.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (51/73 of losers there)
- **Sharp: n=67  W=16/L=51  WR=23.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when lower third

### L18.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (51/73 of losers there)
- **Sharp: n=67  W=16/L=51  WR=23.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when lower third

### L19.  `H60=H60d AND T4=T4c AND RSI=RSI1`
- Raw: n=114  W=38/L=76  WR=33.3%
- Sharpen: sharpest is H20=H20e (26/76 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L20.  `H60=H60d AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=114  W=38/L=76  WR=33.3%
- Sharpen: sharpest is H20=H20e (26/76 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L21.  `H60=H60d AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=114  W=38/L=76  WR=33.3%
- Sharpen: sharpest is H20=H20e (26/76 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 strongly against

### L22.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is BBP=BBP0 (15/66 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when deep below lower band

### L23.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=101  W=36/L=65  WR=35.6%
- Sharpen: sharpest is T1=T1a (56/65 of losers there)
- **Sharp: n=80  W=24/L=56  WR=30.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L24.  `H60=H60d AND T4=T4c AND BBP=BBP2`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is H20=H20e (20/63 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; lower third  •  ONLY when HTF20 strongly against

### L25.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=98  W=35/L=63  WR=35.7%
- Sharpen: sharpest is ZS=ZS1 (27/63 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/33) | H20e(33/39) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
