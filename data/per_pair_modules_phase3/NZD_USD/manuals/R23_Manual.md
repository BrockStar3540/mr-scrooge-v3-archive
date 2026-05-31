# NZD_USD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,902**  (W=1,228 / L=674)  -  WR: **64.6%**

## Session distribution

- asia: n=566  W=366/L=200  WR=64.7%
- london_open: n=390  W=247/L=143  WR=63.3%
- ny_open: n=271  W=181/L=90  WR=66.8%
- ny_mid: n=250  W=158/L=92  WR=63.2%
- london: n=172  W=115/L=57  WR=66.9%
- ny_close: n=157  W=100/L=57  WR=63.7%
- asia_late: n=88  W=56/L=32  WR=63.6%
- off_hours: n=8  W=5/L=3  WR=62.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude T1=T1c drops 9/14 losers (64%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 1h trend AGAINST trade

### W02.  `H60=H60a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude H20=H20e drops 5/8 losers (62%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W03.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W04.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude session_bucket=asia drops 11/13 losers (85%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W05.  `H20=H20a AND H60=H60a AND ZS=ZS1`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude direction_exec=long drops 12/12 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when long

### W06.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP1 drops 9/12 losers (75%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=79  W=74/L=5  WR=93.7%
- Refine: exclude H60=H60b drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W08.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=79  W=74/L=5  WR=93.7%
- Refine: exclude H60=H60b drops 5/5 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W09.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude BBP=BBP1 drops 9/10 losers (90%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W10.  `H20=H20a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=75  W=70/L=5  WR=93.3%
- Refine: exclude H60=H60e drops 3/5 losers (60%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 strongly against

### W11.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; lower third  •  AVOID when session=london_open

### W12.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  AVOID when session=london_open

### W13.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W14.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=asia drops 9/10 losers (90%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=asia

### W15.  `H20=H20a AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=asia drops 9/10 losers (90%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=asia

### W16.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude H60=H60b drops 5/5 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W17.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 slightly aligned

### W18.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 slightly aligned

### W19.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 slightly aligned

### W20.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS2`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W21.  `H20=H20e AND H60=H60e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude session_bucket=london_open drops 4/7 losers (57%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W22.  `H60=H60a AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude RSI=RSI2 drops 7/7 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: exclude session_bucket=asia drops 3/4 losers (75%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W24.  `H20=H20a AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=61  W=57/L=4  WR=93.4%
- Refine: exclude session_bucket=asia drops 3/4 losers (75%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W25.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude session_bucket=asia_late drops 4/6 losers (67%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=115  W=45/L=70  WR=39.1%
- Sharpen: sharpest is ZS=ZS5 (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=70  W=22/L=48  WR=31.4%
- Sharpen: sharpest is BBP=BBP0 (28/48 of losers there)
- **Sharp: n=29  W=1/L=28  WR=3.4%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L03.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is BBP=BBP0 (27/42 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L04.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (14/41 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=london_open

### L05.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (14/41 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when session=london_open

### L06.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is BBP=BBP0 (23/41 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L07.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is RSI=RSI3 (30/38 of losers there)
- **Sharp: n=43  W=13/L=30  WR=30.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L08.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is session_bucket=london_open (14/42 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L09.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is BBP=BBP0 (25/40 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L10.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is RSI=RSI2 (20/38 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L11.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is RSI=RSI2 (20/37 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is RSI=RSI2 (20/36 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L13.  `H20=H20e AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=56  W=20/L=36  WR=35.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought

### L14.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=56  W=20/L=36  WR=35.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought

### L15.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is BBP=BBP2 (10/34 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L16.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=53  W=16/L=37  WR=30.2%
- Sharpen: sharpest is BBP=BBP0 (23/37 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L17.  `T4=T4a AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is direction_exec=long (15/36 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when long

### L18.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=53  W=19/L=34  WR=35.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L19.  `H20=H20a AND H60=H60a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=53  W=19/L=34  WR=35.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold

### L20.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=50  W=16/L=34  WR=32.0%
- Sharpen: sharpest is BBP=BBP0 (20/34 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L21.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is T1=T1c (15/31 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when 1h trend AGAINST trade

### L22.  `H60=H60e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=49  W=14/L=35  WR=28.6%
- Sharpen: sharpest is T1=T1a (18/35 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=london_open  •  ONLY when 1h trend WITH trade

### L23.  `H20=H20a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=49  W=15/L=34  WR=30.6%
- Sharpen: sharpest is BBP=BBP0 (15/34 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L24.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS2`
- Raw: n=49  W=17/L=32  WR=34.7%
- Sharpen: sharpest is session_bucket=ny_mid (5/32 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L25.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is BBP=BBP0 (17/31 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4c(54/47) | T4a(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
