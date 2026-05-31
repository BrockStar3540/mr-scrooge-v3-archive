# GBP_CHF — R25 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,603**  (W=1,630 / L=973)  -  WR: **62.6%**

## Session distribution

- london_open: n=675  W=439/L=236  WR=65.0%
- ny_open: n=448  W=285/L=163  WR=63.6%
- ny_mid: n=439  W=280/L=159  WR=63.8%
- asia: n=335  W=209/L=126  WR=62.4%
- london: n=256  W=162/L=94  WR=63.3%
- ny_close: n=206  W=122/L=84  WR=59.2%
- off_hours: n=205  W=114/L=91  WR=55.6%
- asia_late: n=39  W=19/L=20  WR=48.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=146  W=127/L=19  WR=87.0%
- Refine: exclude H20=H20e drops 14/19 losers (74%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 strongly against

### W02.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude H20=H20b drops 6/19 losers (32%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W03.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude session_bucket=off_hours drops 11/15 losers (73%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when session=off_hours

### W04.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude session_bucket=off_hours drops 7/13 losers (54%)
- **Final: n=101  W=95/L=6  WR=94.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W05.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=103  W=92/L=11  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W06.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H60=H60a drops 5/11 losers (45%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W07.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=96  W=86/L=10  WR=89.6%
- Refine: exclude T1=T1c drops 7/10 losers (70%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W08.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude session_bucket=off_hours drops 10/12 losers (83%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  AVOID when session=off_hours

### W09.  `H20=H20e AND H60=H60a AND BBP=BBP2`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude session_bucket=off_hours drops 4/9 losers (44%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  AVOID when session=off_hours

### W10.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude session_bucket=off_hours drops 4/9 losers (44%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  AVOID when session=off_hours

### W11.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude session_bucket=ny_mid drops 9/10 losers (90%)
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W12.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude session_bucket=off_hours drops 4/13 losers (31%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W13.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude ZS=ZS4 drops 7/10 losers (70%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude session_bucket=off_hours drops 4/7 losers (57%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=off_hours

### W15.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude session_bucket=off_hours drops 10/12 losers (83%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W16.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude T4=T4c drops 9/12 losers (75%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20e AND H60=H60a AND ZS=ZS2`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude session_bucket=off_hours drops 4/7 losers (57%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W18.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude session_bucket=off_hours drops 4/7 losers (57%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W19.  `H20=H20e AND H60=H60a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=79  W=72/L=7  WR=91.1%
- Refine: exclude session_bucket=off_hours drops 4/7 losers (57%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W20.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude RSI=RSI3 drops 7/10 losers (70%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W21.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W22.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI4 drops 6/11 losers (55%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W23.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude H20=H20e drops 9/9 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 strongly against

### W24.  `H20=H20a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude BBP=BBP1 drops 7/10 losers (70%)
- **Final: n=36  W=33/L=3  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W25.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude BBP=BBP6 drops 3/6 losers (50%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when deep above upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=116  W=38/L=78  WR=32.8%
- Sharpen: sharpest is BBP=BBP0 (20/78 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when deep below lower band

### L02.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=105  W=36/L=69  WR=34.3%
- Sharpen: sharpest is direction_exec=long (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when long

### L03.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is ZS=ZS0 (26/59 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L04.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is H20=H20a (24/55 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L05.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is ZS=ZS5 (20/57 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=86  W=27/L=59  WR=31.4%
- Sharpen: sharpest is H20=H20e (30/59 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 strongly against

### L07.  `H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is ZS=ZS0 (22/58 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L08.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is BBP=BBP2 (22/51 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_open  •  ONLY when lower third

### L09.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=80  W=22/L=58  WR=27.5%
- Sharpen: sharpest is H20=H20e (26/58 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L10.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is H20=H20a (23/48 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=79  W=26/L=53  WR=32.9%
- Sharpen: sharpest is ZS=ZS0 (22/53 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L12.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=78  W=20/L=58  WR=25.6%
- Sharpen: sharpest is session_bucket=london_open (21/58 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L13.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=77  W=24/L=53  WR=31.2%
- Sharpen: sharpest is ZS=ZS0 (19/53 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore <-3 extreme

### L14.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=76  W=23/L=53  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_close (10/53 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L15.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H20=H20e (30/49 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 strongly against

### L16.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is T4=T4c (20/44 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L17.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is BBP=BBP2 (13/42 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  ONLY when lower third

### L18.  `T1=T1a AND T4=T4c AND BBP=BBP0`
- Raw: n=67  W=18/L=49  WR=26.9%
- Sharpen: sharpest is H20=H20d (10/49 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 mildly against

### L19.  `H20=H20c AND T1=T1c AND ZS=ZS5`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is session_bucket=london_open (9/45 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L20.  `T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H20=H20a (22/43 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60e AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is T4=T4c (18/41 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L22.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is H60=H60e (33/40 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=65  W=21/L=44  WR=32.3%
- Sharpen: sharpest is T1=T1a (34/44 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: SHORT**  •  HTF20 strongly against; deep below lower band  •  ONLY when 1h trend WITH trade

### L24.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=64  W=20/L=44  WR=31.2%
- Sharpen: sharpest is H20=H20a (23/44 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L25.  `H20=H20c AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is session_bucket=ny_open (19/42 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(54/48) | T4c(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/47) | long(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
