# USD_JPY — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **7,414**  (W=4,625 / L=2,789)  -  WR: **62.4%**

## Session distribution

- asia: n=2734  W=1715/L=1019  WR=62.7%
- ny_close: n=1396  W=890/L=506  WR=63.8%
- ny_open: n=789  W=482/L=307  WR=61.1%
- london_open: n=780  W=472/L=308  WR=60.5%
- ny_mid: n=602  W=374/L=228  WR=62.1%
- london: n=527  W=344/L=183  WR=65.3%
- asia_late: n=359  W=214/L=145  WR=59.6%
- off_hours: n=227  W=134/L=93  WR=59.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=207  W=179/L=28  WR=86.5%
- Refine: exclude H60=H60e drops 28/28 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_close  •  AVOID when HTF60 strongly against

### W02.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=207  W=179/L=28  WR=86.5%
- Refine: exclude H60=H60e drops 28/28 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_close  •  AVOID when HTF60 strongly against

### W03.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=191  W=165/L=26  WR=86.4%
- Refine: exclude H60=H60e drops 26/26 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W04.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=191  W=165/L=26  WR=86.4%
- Refine: exclude H60=H60e drops 26/26 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W05.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude H60=H60b drops 5/12 losers (42%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF60 slightly aligned

### W06.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude H60=H60b drops 5/13 losers (38%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF60 slightly aligned

### W07.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude H60=H60b drops 5/13 losers (38%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF60 slightly aligned

### W08.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=ny_close`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude H20=H20e drops 8/8 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF20 strongly against

### W09.  `H20=H20a AND direction_exec=short AND session_bucket=london`
- Raw: n=75  W=72/L=3  WR=96.0%
- Refine: exclude T1=T1a drops 3/3 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london  •  AVOID when 1h trend WITH trade

### W10.  `H20=H20e AND H60=H60d AND BBP=BBP4`
- Raw: n=74  W=69/L=5  WR=93.2%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; upper third  •  AVOID when zscore -1 to +1 neutral

### W11.  `H60=H60d AND T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude H20=H20b drops 7/8 losers (88%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60d AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude H20=H20b drops 7/8 losers (88%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF60 mildly against; upper third; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W13.  `H20=H20e AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude T1=T1a drops 3/9 losers (33%)
- **Final: n=58  W=52/L=6  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 70-80 overbought; session=ny_close  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20e AND H60=H60d AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=70  W=65/L=5  WR=92.9%
- Refine: exclude T1=T1a drops 4/5 losers (80%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; upper third; RSI 60-70 strong  •  AVOID when 1h trend WITH trade

### W15.  `H60=H60d AND T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude H20=H20b drops 7/8 losers (88%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W16.  `H60=H60d AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude H20=H20b drops 7/8 losers (88%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W17.  `H20=H20e AND H60=H60d AND ZS=ZS4`
- Raw: n=67  W=65/L=2  WR=97.0%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20e AND H60=H60d AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=67  W=65/L=2  WR=97.0%
- Refine: exclude T4=T4a drops 2/2 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20a AND T1=T1c AND session_bucket=london`
- Raw: n=66  W=66/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london

### W20.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=66  W=66/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london

### W21.  `H20=H20d AND H60=H60a AND RSI=RSI5`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP5 drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W22.  `H20=H20d AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP5 drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W23.  `H20=H20d AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP5 drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W24.  `H20=H20b AND T4=T4a AND session_bucket=london_open`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude BBP=BBP5 drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W25.  `H20=H20b AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude BBP=BBP5 drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=164  W=65/L=99  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=65/L=99  WR=39.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_close

### L02.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=164  W=65/L=99  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=65/L=99  WR=39.6%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_close

### L03.  `H20=H20d AND T1=T1c AND T4=T4c`
- Raw: n=157  W=54/L=103  WR=34.4%
- Sharpen: sharpest is RSI=RSI4 (25/103 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L04.  `H20=H20d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=157  W=54/L=103  WR=34.4%
- Sharpen: sharpest is RSI=RSI4 (25/103 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L05.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=152  W=60/L=92  WR=39.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close

### L06.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=152  W=60/L=92  WR=39.5%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close

### L07.  `ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is BBP=BBP5 (59/82 of losers there)
- **Sharp: n=76  W=17/L=59  WR=22.4%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=london_open  •  ONLY when just touched upper band

### L08.  `H20=H20d AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is session_bucket=asia_late (17/78 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L09.  `H20=H20d AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is session_bucket=asia_late (17/78 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L10.  `H20=H20d AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=125  W=47/L=78  WR=37.6%
- Sharpen: sharpest is session_bucket=asia_late (17/78 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L11.  `H20=H20d AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=125  W=47/L=78  WR=37.6%
- Sharpen: sharpest is session_bucket=asia_late (17/78 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L12.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is H60=H60e (64/74 of losers there)
- **Sharp: n=89  W=25/L=64  WR=28.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when HTF60 strongly against

### L13.  `H20=H20b AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=120  W=47/L=73  WR=39.2%
- Sharpen: sharpest is T4=T4a (44/73 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 60-70 strong; session=asia  •  ONLY when 4h trend WITH trade

### L14.  `T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is H60=H60e (47/68 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band  •  ONLY when HTF60 strongly against

### L15.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=108  W=36/L=72  WR=33.3%
- Sharpen: sharpest is T4=T4a (51/72 of losers there)
- **Sharp: n=69  W=18/L=51  WR=26.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=108  W=38/L=70  WR=35.2%
- Sharpen: sharpest is H60=H60e (47/70 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=106  W=38/L=68  WR=35.8%
- Sharpen: sharpest is H60=H60e (47/68 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is direction_exec=short (64/67 of losers there)
- **Sharp: n=89  W=25/L=64  WR=28.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when short

### L19.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (13/59 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when deep above upper band

### L20.  `H20=H20b AND H60=H60e AND T1=T1c`
- Raw: n=95  W=25/L=70  WR=26.3%
- Sharpen: sharpest is ZS=ZS5 (38/70 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=94  W=28/L=66  WR=29.8%
- Sharpen: sharpest is H60=H60e (22/66 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L22.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=94  W=28/L=66  WR=29.8%
- Sharpen: sharpest is H60=H60e (22/66 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L23.  `H20=H20d AND T1=T1c AND ZS=ZS5`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (22/57 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L24.  `H20=H20d AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (22/57 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L25.  `H20=H20b AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is BBP=BBP6 (24/56 of losers there)
- **Sharp: n=27  W=3/L=24  WR=11.1%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(41/34) | H20a(33/38) |
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
