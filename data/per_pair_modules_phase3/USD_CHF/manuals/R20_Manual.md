# USD_CHF — R20 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,499**  (W=962 / L=537)  -  WR: **64.2%**

## Session distribution

- asia: n=811  W=531/L=280  WR=65.5%
- ny_close: n=277  W=172/L=105  WR=62.1%
- asia_late: n=153  W=99/L=54  WR=64.7%
- off_hours: n=83  W=50/L=33  WR=60.2%
- london: n=68  W=45/L=23  WR=66.2%
- london_open: n=55  W=35/L=20  WR=63.6%
- ny_open: n=49  W=28/L=21  WR=57.1%
- ny_mid: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=218  W=187/L=31  WR=85.8%
- Refine: exclude H20=H20b drops 11/31 losers (35%)
- **Final: n=197  W=177/L=20  WR=89.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF20 slightly aligned

### W02.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=150  W=137/L=13  WR=91.3%
- Refine: no further refinement
- **Final: n=150  W=137/L=13  WR=91.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia

### W03.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H20=H20b drops 9/17 losers (53%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 slightly aligned

### W04.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=115  W=103/L=12  WR=89.6%
- Refine: exclude session_bucket=ny_open drops 3/12 losers (25%)
- **Final: n=112  W=103/L=9  WR=92.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W05.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=114  W=100/L=14  WR=87.7%
- Refine: exclude BBP=BBP3 drops 3/14 losers (21%)
- **Final: n=108  W=97/L=11  WR=89.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when middle of band

### W06.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=112  W=99/L=13  WR=88.4%
- Refine: exclude BBP=BBP3 drops 3/13 losers (23%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when middle of band

### W07.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=106  W=104/L=2  WR=98.1%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  AVOID when 4h trend WITH trade

### W08.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T4=T4c drops 7/15 losers (47%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20c AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude H60=H60e drops 7/9 losers (78%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF20 neutral; session=asia  •  AVOID when HTF60 strongly against

### W10.  `H20=H20c AND H60=H60a AND session_bucket=asia`
- Raw: n=96  W=93/L=3  WR=96.9%
- Refine: exclude RSI=RSI4 drops 2/3 losers (67%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude H20=H20a drops 8/10 losers (80%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W12.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude H60=H60b drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when HTF60 slightly aligned

### W13.  `H20=H20c AND T1=T1a AND direction_exec=long`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude H60=H60e drops 7/9 losers (78%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when HTF60 strongly against

### W14.  `H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude T1=T1c drops 10/11 losers (91%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude session_bucket=ny_open drops 3/12 losers (25%)
- **Final: n=84  W=75/L=9  WR=89.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_open

### W16.  `H20=H20e AND T1=T1c AND BBP=BBP4`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude RSI=RSI3 drops 8/12 losers (67%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W17.  `H20=H20c AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=82/L=2  WR=97.6%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20e AND T1=T1c AND ZS=ZS4`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude RSI=RSI3 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W19.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude RSI=RSI3 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W20.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude H20=H20b drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 slightly aligned

### W21.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude H60=H60b drops 3/8 losers (38%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 slightly aligned

### W22.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude BBP=BBP2 drops 4/10 losers (40%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when lower third

### W23.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

### W24.  `H20=H20c AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=78  W=76/L=2  WR=97.4%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20c AND T4=T4a AND direction_exec=long`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude H60=H60e drops 7/9 losers (78%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=219  W=84/L=135  WR=38.4%
- Sharpen: sharpest is direction_exec=short (69/135 of losers there)
- **Sharp: n=96  W=27/L=69  WR=28.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when short

### L02.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=156  W=50/L=106  WR=32.1%
- Sharpen: sharpest is H60=H60a (51/106 of losers there)
- **Sharp: n=66  W=15/L=51  WR=22.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L03.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=151  W=58/L=93  WR=38.4%
- Sharpen: sharpest is T4=T4c (69/93 of losers there)
- **Sharp: n=96  W=27/L=69  WR=28.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is ZS=ZS3 (13/63 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L05.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=103  W=34/L=69  WR=33.0%
- Sharpen: sharpest is H20=H20a (26/69 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L06.  `H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is T4=T4c (51/60 of losers there)
- **Sharp: n=66  W=15/L=51  WR=22.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when 4h trend AGAINST trade

### L07.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is ZS=ZS5 (22/59 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=96  W=27/L=69  WR=28.1%
- Sharpen: sharpest is ZS=ZS5 (24/69 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=96  W=33/L=63  WR=34.4%
- Sharpen: sharpest is H20=H20a (23/63 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L10.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=95  W=38/L=57  WR=40.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close

### L11.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is H20=H20a (35/57 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L12.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (42/60 of losers there)
- **Sharp: n=55  W=13/L=42  WR=23.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L13.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=24/L=63  WR=27.6%
- Sharpen: sharpest is ZS=ZS5 (20/63 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is RSI=RSI4 (42/59 of losers there)
- **Sharp: n=55  W=13/L=42  WR=23.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is BBP=BBP4 (35/54 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L16.  `H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=85  W=31/L=54  WR=36.5%
- Sharpen: sharpest is H20=H20c (29/54 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when HTF20 neutral

### L17.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (40/48 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L18.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (24/47 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L19.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=71  W=23/L=48  WR=32.4%
- Sharpen: sharpest is direction_exec=short (24/48 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when short

### L20.  `T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=71  W=24/L=47  WR=33.8%
- Sharpen: sharpest is H60=H60c (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 neutral

### L21.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is H20=H20a (27/44 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L22.  `H20=H20a AND T4=T4c AND BBP=BBP4`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is RSI=RSI4 (38/44 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L23.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is T1=T1c (24/47 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L24.  `H20=H20d AND T4=T4c AND RSI=RSI4`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is BBP=BBP6 (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L25.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: sharpest is H60=H60c (16/43 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(56/44) | T1a(43/55) |
| T4 | T4a(59/36) | T4c(41/64) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/44) | short(42/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
