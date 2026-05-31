# USD_CHF — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,960**  (W=1,252 / L=708)  -  WR: **63.9%**

## Session distribution

- asia: n=803  W=517/L=286  WR=64.4%
- ny_close: n=332  W=202/L=130  WR=60.8%
- london: n=262  W=172/L=90  WR=65.6%
- asia_late: n=172  W=110/L=62  WR=64.0%
- london_open: n=169  W=104/L=65  WR=61.5%
- off_hours: n=97  W=67/L=30  WR=69.1%
- ny_open: n=89  W=57/L=32  WR=64.0%
- ny_mid: n=36  W=23/L=13  WR=63.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude T1=T1a drops 13/18 losers (72%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend WITH trade

### W02.  `ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP1 drops 8/9 losers (89%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W03.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP1 drops 7/8 losers (88%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W04.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude BBP=BBP0 drops 6/9 losers (67%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  AVOID when deep below lower band

### W05.  `H60=H60e AND RSI=RSI3 AND session_bucket=asia_late`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude T1=T1a drops 7/9 losers (78%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia_late  •  AVOID when 1h trend WITH trade

### W06.  `H20=H20a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude direction_exec=short drops 9/9 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; session=asia  •  AVOID when short

### W07.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude BBP=BBP0 drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when deep below lower band

### W08.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude BBP=BBP0 drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when deep below lower band

### W09.  `H60=H60e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude session_bucket=london drops 5/7 losers (71%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band  •  AVOID when session=london

### W10.  `T1=T1a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude BBP=BBP1 drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W11.  `T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude direction_exec=short drops 6/7 losers (86%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when short

### W12.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude BBP=BBP0 drops 6/7 losers (86%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=asia_late  •  AVOID when deep below lower band

### W13.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=53  W=47/L=6  WR=88.7%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  AVOID when 1h trend AGAINST trade

### W14.  `H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS6 drops 3/7 losers (43%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend WITH trade  •  AVOID when zscore >+3 extreme

### W15.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude session_bucket=london drops 5/7 losers (71%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london

### W16.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude H20=H20e drops 4/6 losers (67%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W17.  `T4=T4c AND RSI=RSI3 AND ZS=ZS0`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude session_bucket=london drops 3/6 losers (50%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore <-3 extreme  •  AVOID when session=london

### W18.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude session_bucket=off_hours drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=off_hours

### W19.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS0`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude session_bucket=london drops 3/6 losers (50%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore <-3 extreme  •  AVOID when session=london

### W20.  `RSI=RSI4 AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=49  W=47/L=2  WR=95.9%
- Refine: exclude T4=T4c drops 2/2 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=off_hours  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20c AND T1=T1a AND direction_exec=long`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude H60=H60b drops 5/5 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W22.  `BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude T1=T1c drops 4/5 losers (80%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  upper third; session=london  •  AVOID when 1h trend AGAINST trade

### W23.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude BBP=BBP6 drops 2/5 losers (40%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when deep above upper band

### W24.  `T4=T4a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W25.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=48  W=47/L=1  WR=97.9%
- Refine: no further refinement
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold; session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=92  W=34/L=58  WR=37.0%
- Sharpen: sharpest is T4=T4c (31/58 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H60=H60a (31/51 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L03.  `H20=H20e AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=79  W=30/L=49  WR=38.0%
- Sharpen: sharpest is T1=T1c (36/49 of losers there)
- **Sharp: n=48  W=12/L=36  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L04.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is T1=T1a (23/40 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when 1h trend WITH trade

### L05.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is T4=T4c (24/42 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L06.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is T1=T1c (22/40 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  ONLY when 1h trend AGAINST trade

### L07.  `T1=T1c AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is H20=H20e (23/33 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 strongly against

### L08.  `H60=H60a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: sharpest is T4=T4c (10/35 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L09.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=50  W=15/L=35  WR=30.0%
- Sharpen: sharpest is H20=H20a (16/35 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L10.  `T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=47  W=17/L=30  WR=36.2%
- Sharpen: sharpest is H20=H20e (10/30 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london  •  ONLY when HTF20 strongly against

### L11.  `H20=H20e AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=46  W=14/L=32  WR=30.4%
- Sharpen: sharpest is RSI=RSI3 (26/32 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L12.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is T4=T4c (10/31 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=45  W=16/L=29  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (20/29 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L14.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is ZS=ZS2 (24/27 of losers there)
- **Sharp: n=35  W=11/L=24  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L15.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=44  W=10/L=34  WR=22.7%
- Sharpen: sharpest is T4=T4c (19/34 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L16.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS1`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is direction_exec=short (21/30 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when short

### L17.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=44  W=15/L=29  WR=34.1%
- Sharpen: sharpest is H60=H60a (18/29 of losers there)
- **Sharp: n=23  W=5/L=18  WR=21.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=44  W=17/L=27  WR=38.6%
- Sharpen: sharpest is T4=T4c (17/27 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: sharpest is T4=T4c (14/31 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20e AND H60=H60a AND ZS=ZS2`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (24/26 of losers there)
- **Sharp: n=35  W=11/L=24  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (24/26 of losers there)
- **Sharp: n=35  W=11/L=24  WR=31.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L22.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is ZS=ZS1 (12/29 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is direction_exec=short (20/28 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when short

### L24.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is T4=T4c (16/28 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L25.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is T4=T4a (15/26 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(44/38) | H60a(39/44) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/46) | short(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
