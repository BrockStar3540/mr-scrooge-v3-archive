# NZD_CAD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,533**  (W=995 / L=538)  -  WR: **64.9%**

## Session distribution

- asia: n=667  W=450/L=217  WR=67.5%
- ny_close: n=305  W=189/L=116  WR=62.0%
- london: n=196  W=121/L=75  WR=61.7%
- london_open: n=101  W=60/L=41  WR=59.4%
- ny_open: n=83  W=57/L=26  WR=68.7%
- asia_late: n=77  W=55/L=22  WR=71.4%
- off_hours: n=72  W=42/L=30  WR=58.3%
- ny_mid: n=32  W=21/L=11  WR=65.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=112  W=105/L=7  WR=93.8%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=asia  •  AVOID when RSI 40-50 lower neutral

### W02.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=97  W=88/L=9  WR=90.7%
- Refine: exclude H20=H20b drops 5/9 losers (56%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 slightly aligned

### W03.  `ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude H60=H60e drops 6/13 losers (46%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W04.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude H60=H60e drops 6/13 losers (46%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W05.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude T4=T4a drops 7/14 losers (50%)
- **Final: n=67  W=60/L=7  WR=89.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60a AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=92  W=87/L=5  WR=94.6%
- Refine: exclude RSI=RSI3 drops 3/5 losers (60%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; session=asia  •  AVOID when RSI 40-50 lower neutral

### W07.  `H60=H60a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=92  W=86/L=6  WR=93.5%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W08.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=92  W=86/L=6  WR=93.5%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H60=H60e drops 9/12 losers (75%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W10.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20b drops 5/7 losers (71%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when HTF20 slightly aligned

### W11.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude T4=T4c drops 8/10 losers (80%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when 4h trend AGAINST trade

### W12.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=87  W=81/L=6  WR=93.1%
- Refine: exclude RSI=RSI3 drops 4/6 losers (67%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; session=asia  •  AVOID when RSI 40-50 lower neutral

### W13.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H60=H60e drops 6/13 losers (46%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W14.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude H60=H60d drops 3/8 losers (38%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 mildly against

### W15.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude H20=H20b drops 5/7 losers (71%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 slightly aligned

### W16.  `H60=H60a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H20=H20e drops 6/11 losers (55%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 30-40 weak  •  AVOID when HTF20 strongly against

### W17.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W18.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude session_bucket=ny_close drops 7/11 losers (64%)
- **Final: n=44  W=40/L=4  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_close

### W19.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude session_bucket=ny_open drops 5/7 losers (71%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_open

### W20.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude session_bucket=ny_open drops 5/7 losers (71%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_open

### W21.  `H20=H20e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H60=H60e drops 4/10 losers (40%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=asia  •  AVOID when HTF60 strongly against

### W22.  `H60=H60a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 slightly aligned

### W24.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude H20=H20b drops 5/6 losers (83%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 slightly aligned

### W25.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP0 drops 4/9 losers (44%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=73  W=21/L=52  WR=28.8%
- Sharpen: sharpest is BBP=BBP1 (20/52 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when just touched lower band

### L02.  `H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is ZS=ZS3 (13/44 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF60 strongly against; upper third  •  ONLY when zscore -1 to +1 neutral

### L03.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=71  W=22/L=49  WR=31.0%
- Sharpen: sharpest is BBP=BBP1 (22/49 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when just touched lower band

### L04.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is ZS=ZS3 (13/43 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when zscore -1 to +1 neutral

### L05.  `H20=H20a AND T1=T1a AND RSI=RSI3`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is H60=H60c (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L06.  `H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is T1=T1a (41/45 of losers there)
- **Sharp: n=57  W=16/L=41  WR=28.1%**
- **Dir: SHORT**  •  HTF60 strongly against; session=asia  •  ONLY when 1h trend WITH trade

### L07.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is H60=H60c (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L08.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is H60=H60c (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L09.  `H20=H20d AND T1=T1c AND direction_exec=long`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is T4=T4c (31/40 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L10.  `H60=H60e AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is ZS=ZS3 (12/41 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 30-40 weak  •  ONLY when zscore -1 to +1 neutral

### L11.  `H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is BBP=BBP1 (17/39 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when just touched lower band

### L12.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is BBP=BBP1 (28/37 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L13.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is H20=H20e (15/39 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when HTF20 strongly against

### L14.  `H20=H20d AND H60=H60e AND direction_exec=long`
- Raw: n=57  W=15/L=42  WR=26.3%
- Sharpen: sharpest is T4=T4c (31/42 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=57  W=16/L=41  WR=28.1%
- Sharpen: sharpest is BBP=BBP1 (12/41 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when just touched lower band

### L16.  `H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=55  W=14/L=41  WR=25.5%
- Sharpen: sharpest is RSI=RSI1 (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L17.  `H20=H20d AND H60=H60e AND T1=T1c`
- Raw: n=54  W=15/L=39  WR=27.8%
- Sharpen: sharpest is T4=T4c (31/39 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20d AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=54  W=15/L=39  WR=27.8%
- Sharpen: sharpest is T4=T4c (31/39 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (10/32 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=asia

### L20.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=51  W=15/L=36  WR=29.4%
- Sharpen: sharpest is BBP=BBP1 (20/36 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when just touched lower band

### L21.  `H60=H60e AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=50  W=14/L=36  WR=28.0%
- Sharpen: sharpest is T1=T1a (20/36 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; session=asia  •  ONLY when 1h trend WITH trade

### L22.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=50  W=14/L=36  WR=28.0%
- Sharpen: sharpest is T1=T1a (20/36 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 1h trend WITH trade

### L23.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=50  W=17/L=33  WR=34.0%
- Sharpen: sharpest is BBP=BBP1 (25/33 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L24.  `H60=H60e AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is T1=T1a (22/32 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L25.  `H60=H60e AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is T1=T1a (22/32 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(10/16) |
| H60 | H60a(54/34) | H60e(34/52) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
