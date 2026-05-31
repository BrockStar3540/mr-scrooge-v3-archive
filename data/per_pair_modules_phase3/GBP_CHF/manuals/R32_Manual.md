# GBP_CHF — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,232**  (W=1,405 / L=827)  -  WR: **62.9%**

## Session distribution

- asia: n=1197  W=758/L=439  WR=63.3%
- ny_close: n=487  W=302/L=185  WR=62.0%
- asia_late: n=297  W=194/L=103  WR=65.3%
- off_hours: n=155  W=91/L=64  WR=58.7%
- london_open: n=68  W=41/L=27  WR=60.3%
- ny_mid: n=22  W=16/L=6  WR=72.7%
- london: n=6  W=3/L=3  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=144  W=125/L=19  WR=86.8%
- Refine: exclude T1=T1a drops 14/19 losers (74%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia_late  •  AVOID when 1h trend WITH trade

### W02.  `T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=136  W=117/L=19  WR=86.0%
- Refine: exclude T1=T1c drops 16/19 losers (84%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W03.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude BBP=BBP0 drops 4/15 losers (27%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_close  •  AVOID when deep below lower band

### W04.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=106  W=97/L=9  WR=91.5%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W05.  `T1=T1c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=102  W=95/L=7  WR=93.1%
- Refine: exclude T4=T4a drops 6/7 losers (86%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia_late  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=95  W=84/L=11  WR=88.4%
- Refine: exclude H20=H20d drops 6/11 losers (55%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W07.  `H20=H20c AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude session_bucket=asia drops 6/9 losers (67%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W08.  `T1=T1c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=90  W=85/L=5  WR=94.4%
- Refine: exclude H20=H20d drops 3/5 losers (60%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia_late  •  AVOID when HTF20 mildly against

### W09.  `H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude H20=H20b drops 9/11 losers (82%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third  •  AVOID when HTF20 slightly aligned

### W10.  `H60=H60e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude H20=H20b drops 9/11 losers (82%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W11.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude H20=H20b drops 9/11 losers (82%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W12.  `T4=T4c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude T1=T1a drops 10/11 losers (91%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia_late  •  AVOID when 1h trend WITH trade

### W13.  `H20=H20c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude T1=T1a drops 7/11 losers (64%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: LONG**  •  HTF20 neutral; upper third; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude T1=T1a drops 7/11 losers (64%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: LONG**  •  HTF20 neutral; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W15.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude T4=T4c drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W16.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP0 drops 4/9 losers (44%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when deep below lower band

### W17.  `H20=H20c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude T1=T1a drops 5/10 losers (50%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade; upper third  •  AVOID when 1h trend WITH trade

### W18.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude session_bucket=asia drops 6/10 losers (60%)
- **Final: n=42  W=38/L=4  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when session=asia

### W19.  `H20=H20e AND H60=H60e AND RSI=RSI3`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude T1=T1c drops 6/10 losers (60%)
- **Final: n=44  W=40/L=4  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude H60=H60a drops 9/9 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W21.  `H60=H60a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=68  W=64/L=4  WR=94.1%
- Refine: exclude H20=H20d drops 3/4 losers (75%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia_late  •  AVOID when HTF20 mildly against

### W22.  `H20=H20c AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude T1=T1a drops 5/10 losers (50%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W23.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=67  W=64/L=3  WR=95.5%
- Refine: exclude H20=H20d drops 3/3 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia_late  •  AVOID when HTF20 mildly against

### W24.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude T1=T1a drops 6/7 losers (86%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W25.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude T1=T1a drops 6/7 losers (86%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia_late  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=119  W=43/L=76  WR=36.1%
- Sharpen: sharpest is T1=T1c (30/76 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L02.  `H20=H20a AND T4=T4a AND ZS=ZS4`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T1=T1a (34/63 of losers there)
- **Sharp: n=49  W=15/L=34  WR=30.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L03.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T1=T1a (34/63 of losers there)
- **Sharp: n=49  W=15/L=34  WR=30.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L04.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is H20=H20a (19/62 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L05.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=92  W=31/L=61  WR=33.7%
- Sharpen: sharpest is BBP=BBP4 (25/61 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia_late  •  ONLY when upper third

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=79  W=26/L=53  WR=32.9%
- Sharpen: sharpest is session_bucket=asia_late (30/53 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L07.  `T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is T4=T4c (30/52 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L08.  `H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is T1=T1c (20/47 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L09.  `ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is T1=T1a (20/47 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=asia  •  ONLY when 1h trend WITH trade

### L10.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=72  W=27/L=45  WR=37.5%
- Sharpen: sharpest is session_bucket=asia_late (19/45 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; upper third  •  ONLY when session=asia_late

### L11.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=69  W=26/L=43  WR=37.7%
- Sharpen: sharpest is session_bucket=asia_late (18/43 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=asia_late

### L12.  `T1=T1a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=18/L=49  WR=26.9%
- Sharpen: sharpest is BBP=BBP4 (25/49 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia_late  •  ONLY when upper third

### L13.  `T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=26/L=41  WR=38.8%
- Sharpen: sharpest is T1=T1a (36/41 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia_late  •  ONLY when 1h trend WITH trade

### L14.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is T1=T1a (15/40 of losers there)
- **Sharp: n=20  W=5/L=15  WR=25.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L15.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is H20=H20a (16/45 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L16.  `H20=H20c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is T4=T4c (27/41 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: LONG**  •  HTF20 neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is ZS=ZS4 (34/40 of losers there)
- **Sharp: n=49  W=15/L=34  WR=30.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L18.  `H20=H20c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is T1=T1a (26/39 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: SHORT**  •  HTF20 neutral; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L19.  `H20=H20c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is T1=T1a (26/38 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L20.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=61  W=19/L=42  WR=31.1%
- Sharpen: sharpest is T4=T4c (29/42 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is BBP=BBP1 (6/37 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when just touched lower band

### L22.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is session_bucket=asia_late (25/41 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L23.  `H20=H20c AND T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is RSI=RSI4 (26/37 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20c AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=57  W=14/L=43  WR=24.6%
- Sharpen: sharpest is session_bucket=asia_late (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L25.  `H20=H20c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is direction_exec=long (27/35 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; session=ny_close  •  ONLY when long

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
| direction_exec | long(54/49) | short(46/51) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
