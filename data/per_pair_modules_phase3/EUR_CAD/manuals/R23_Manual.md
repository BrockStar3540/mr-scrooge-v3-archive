# EUR_CAD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,763**  (W=1,121 / L=642)  -  WR: **63.6%**

## Session distribution

- asia: n=934  W=599/L=335  WR=64.1%
- ny_close: n=456  W=301/L=155  WR=66.0%
- off_hours: n=165  W=97/L=68  WR=58.8%
- asia_late: n=58  W=33/L=25  WR=56.9%
- ny_open: n=52  W=31/L=21  WR=59.6%
- london_open: n=49  W=33/L=16  WR=67.3%
- london: n=30  W=18/L=12  WR=60.0%
- ny_mid: n=19  W=9/L=10  WR=47.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W02.  `T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20d drops 4/14 losers (29%)
- **Final: n=92  W=82/L=10  WR=89.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 mildly against

### W03.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude T1=T1b drops 5/13 losers (38%)
- **Final: n=86  W=78/L=8  WR=90.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend flat

### W04.  `T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude H20=H20e drops 9/11 losers (82%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W05.  `H60=H60b AND T1=T1c AND T4=T4c`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude direction_exec=short drops 13/13 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when short

### W06.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude H20=H20e drops 9/9 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W07.  `H60=H60b AND T1=T1c AND RSI=RSI4`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude direction_exec=short drops 11/11 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when short

### W08.  `H60=H60b AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude direction_exec=short drops 10/10 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when short

### W09.  `H60=H60b AND T1=T1c AND direction_exec=long`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20d AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H60=H60d drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 mildly against

### W11.  `H20=H20c AND T1=T1a AND BBP=BBP4`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude session_bucket=london drops 4/6 losers (67%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; upper third  •  AVOID when session=london

### W12.  `H60=H60e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude session_bucket=ny_open drops 4/7 losers (57%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band  •  AVOID when session=ny_open

### W13.  `ZS=ZS1 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude T1=T1c drops 5/6 losers (83%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: LONG**  •  zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W14.  `H20=H20c AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude session_bucket=london drops 4/6 losers (67%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=london

### W15.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude T4=T4c drops 6/7 losers (86%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20c AND H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when session=london

### W17.  `H20=H20c AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; upper third  •  AVOID when session=london

### W18.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W19.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W20.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W21.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T1=T1a drops 5/6 losers (83%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: LONG**  •  lower third; session=ny_close  •  AVOID when 1h trend WITH trade

### W22.  `H20=H20c AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude session_bucket=london drops 4/6 losers (67%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london

### W23.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude BBP=BBP6 drops 4/6 losers (67%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when deep above upper band

### W24.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude direction_exec=long drops 5/6 losers (83%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=asia  •  AVOID when long

### W25.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude direction_exec=long drops 7/7 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when long

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS4 (13/48 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L02.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=60  W=20/L=40  WR=33.3%
- Sharpen: sharpest is BBP=BBP4 (14/40 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L03.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is direction_exec=short (11/36 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when short

### L04.  `T4=T4a AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=57  W=16/L=41  WR=28.1%
- Sharpen: sharpest is H20=H20c (14/41 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when HTF20 neutral

### L05.  `H60=H60a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=55  W=18/L=37  WR=32.7%
- Sharpen: sharpest is H20=H20c (14/37 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=off_hours  •  ONLY when HTF20 neutral

### L06.  `H60=H60a AND T4=T4a AND session_bucket=off_hours`
- Raw: n=54  W=19/L=35  WR=35.2%
- Sharpen: sharpest is H20=H20c (14/35 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 neutral

### L07.  `H60=H60a AND T1=T1c AND session_bucket=off_hours`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is H20=H20c (14/36 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=off_hours  •  ONLY when HTF20 neutral

### L08.  `T1=T1c AND T4=T4a AND session_bucket=off_hours`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is direction_exec=short (32/33 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=off_hours  •  ONLY when short

### L09.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=49  W=14/L=35  WR=28.6%
- Sharpen: sharpest is H20=H20c (14/35 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=off_hours  •  ONLY when HTF20 neutral

### L10.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is H20=H20c (11/30 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=asia  •  ONLY when HTF20 neutral

### L11.  `H60=H60a AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=48  W=15/L=33  WR=31.2%
- Sharpen: sharpest is H20=H20c (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when HTF20 neutral

### L12.  `H20=H20e AND H60=H60a AND direction_exec=short`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_open (7/30 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when session=ny_open

### L13.  `T4=T4a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=47  W=14/L=33  WR=29.8%
- Sharpen: sharpest is H20=H20c (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=off_hours  •  ONLY when HTF20 neutral

### L14.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=47  W=14/L=33  WR=29.8%
- Sharpen: sharpest is H20=H20c (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 neutral

### L15.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=off_hours`
- Raw: n=46  W=13/L=33  WR=28.3%
- Sharpen: sharpest is H20=H20c (14/33 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 neutral

### L16.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=45  W=13/L=32  WR=28.9%
- Sharpen: sharpest is H20=H20c (14/32 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when HTF20 neutral

### L17.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=45  W=13/L=32  WR=28.9%
- Sharpen: sharpest is H20=H20c (14/32 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when HTF20 neutral

### L18.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is H20=H20e (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 strongly against

### L19.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=42  W=10/L=32  WR=23.8%
- Sharpen: sharpest is H20=H20c (14/32 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=off_hours  •  ONLY when HTF20 neutral

### L20.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is H20=H20c (14/30 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when HTF20 neutral

### L21.  `H20=H20b AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is RSI=RSI4 (15/26 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L22.  `H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=40  W=13/L=27  WR=32.5%
- Sharpen: sharpest is session_bucket=asia (18/27 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade  •  ONLY when session=asia

### L23.  `H20=H20c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is session_bucket=off_hours (12/24 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=off_hours

### L24.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is H20=H20b (6/24 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L25.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=38  W=9/L=29  WR=23.7%
- Sharpen: sharpest is H20=H20c (14/29 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=off_hours  •  ONLY when HTF20 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(35/26) | H20e(24/32) |
| H60 | — | H60a(37/43) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/47) | short(46/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
