# EUR_USD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,146**  (W=1,355 / L=791)  -  WR: **63.1%**

## Session distribution

- asia: n=1515  W=971/L=544  WR=64.1%
- ny_close: n=276  W=168/L=108  WR=60.9%
- asia_late: n=166  W=99/L=67  WR=59.6%
- off_hours: n=94  W=60/L=34  WR=63.8%
- london_open: n=57  W=36/L=21  WR=63.2%
- london: n=22  W=11/L=11  WR=50.0%
- ny_open: n=16  W=10/L=6  WR=62.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude ZS=ZS3 drops 7/16 losers (44%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W02.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W03.  `BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude ZS=ZS6 drops 10/12 losers (83%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  deep above upper band; session=asia  •  AVOID when zscore >+3 extreme

### W04.  `T4=T4c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude T1=T1a drops 12/13 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when 1h trend WITH trade

### W05.  `H20=H20a AND H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 4/14 losers (29%)
- **Final: n=86  W=76/L=10  WR=88.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; upper third  •  AVOID when session=ny_close

### W06.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude T1=T1a drops 11/13 losers (85%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude direction_exec=long drops 10/11 losers (91%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when long

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude T4=T4c drops 5/10 losers (50%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude T4=T4c drops 9/11 losers (82%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W10.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude H60=H60e drops 4/11 losers (36%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W11.  `T1=T1c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude T4=T4a drops 11/12 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude H60=H60d drops 6/11 losers (55%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 mildly against

### W13.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude T1=T1a drops 4/11 losers (36%)
- **Final: n=78  W=71/L=7  WR=91.0%**
- **Dir: SHORT**  •  deep above upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W14.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude T4=T4a drops 7/9 losers (78%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W15.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude T1=T1a drops 11/12 losers (92%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W16.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W17.  `H20=H20a AND H60=H60e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=ny_close drops 3/12 losers (25%)
- **Final: n=77  W=68/L=9  WR=88.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W18.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude T1=T1a drops 6/9 losers (67%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when 1h trend WITH trade

### W20.  `H20=H20e AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; session=asia  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20e AND BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; session=asia  •  AVOID when 4h trend WITH trade

### W22.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude T4=T4a drops 6/7 losers (86%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend WITH trade

### W23.  `T1=T1c AND BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude T4=T4a drops 6/7 losers (86%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when 4h trend WITH trade

### W24.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude T1=T1a drops 5/8 losers (62%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  AVOID when 1h trend WITH trade

### W25.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude T4=T4a drops 6/8 losers (75%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND RSI=RSI4`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: sharpest is T4=T4c (69/93 of losers there)
- **Sharp: n=101  W=32/L=69  WR=31.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L02.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: sharpest is direction_exec=long (38/90 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when long

### L03.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: sharpest is direction_exec=long (38/90 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when long

### L04.  `H20=H20e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=105  W=32/L=73  WR=30.5%
- Sharpen: sharpest is BBP=BBP4 (44/73 of losers there)
- **Sharp: n=55  W=11/L=44  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when upper third

### L05.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is T4=T4c (59/63 of losers there)
- **Sharp: n=84  W=25/L=59  WR=29.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when 4h trend AGAINST trade

### L06.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=101  W=32/L=69  WR=31.7%
- Sharpen: sharpest is BBP=BBP4 (35/69 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L07.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is direction_exec=long (23/62 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when long

### L08.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is ZS=ZS5 (14/56 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is T1=T1a (32/55 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is H60=H60e (41/56 of losers there)
- **Sharp: n=58  W=17/L=41  WR=29.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L11.  `H20=H20e AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is T4=T4c (41/54 of losers there)
- **Sharp: n=58  W=17/L=41  WR=29.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=82  W=29/L=53  WR=35.4%
- Sharpen: sharpest is T4=T4c (44/53 of losers there)
- **Sharp: n=61  W=17/L=44  WR=27.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=80  W=25/L=55  WR=31.2%
- Sharpen: sharpest is BBP=BBP4 (31/55 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when upper third

### L14.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is T4=T4a (25/48 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L15.  `T1=T1a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is T4=T4a (33/48 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is H60=H60a (21/47 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=77  W=26/L=51  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (37/51 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L18.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is BBP=BBP4 (19/52 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when upper third

### L19.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is BBP=BBP4 (30/52 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L20.  `H20=H20e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is T4=T4a (22/46 of losers there)
- **Sharp: n=29  W=7/L=22  WR=24.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L21.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is T4=T4c (35/46 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is T4=T4a (29/45 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is T4=T4c (32/42 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is T1=T1a (23/44 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is direction_exec=long (31/44 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when long

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(42/35) | H60b(5/11) |
| T1 | T1c(54/43) | T1a(46/56) |
| T4 | T4a(54/46) | T4c(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
