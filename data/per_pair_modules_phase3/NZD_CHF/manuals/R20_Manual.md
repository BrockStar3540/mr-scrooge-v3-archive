# NZD_CHF — R20 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **530**  (W=345 / L=185)  -  WR: **65.1%**

## Session distribution

- ny_mid: n=190  W=120/L=70  WR=63.2%
- ny_close: n=110  W=76/L=34  WR=69.1%
- asia: n=58  W=44/L=14  WR=75.9%
- off_hours: n=52  W=36/L=16  WR=69.2%
- ny_open: n=48  W=24/L=24  WR=50.0%
- london_open: n=35  W=24/L=11  WR=68.6%
- london: n=31  W=18/L=13  WR=58.1%
- asia_late: n=6  W=3/L=3  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=66  W=60/L=6  WR=90.9%
- Refine: exclude H20=H20e drops 4/6 losers (67%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W02.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude direction_exec=short drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when short

### W03.  `T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude RSI=RSI3 drops 8/8 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W04.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude session_bucket=london drops 3/5 losers (60%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  AVOID when session=london

### W05.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=50  W=46/L=4  WR=92.0%
- Refine: exclude session_bucket=london drops 3/4 losers (75%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=london

### W06.  `H20=H20e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude direction_exec=short drops 5/7 losers (71%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when short

### W07.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude H20=H20d drops 6/7 losers (86%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 mildly against

### W08.  `T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=44  W=40/L=4  WR=90.9%
- Refine: exclude T4=T4a drops 4/4 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 4h trend WITH trade

### W09.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude H20=H20e drops 4/5 losers (80%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W10.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude direction_exec=short drops 5/5 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when short

### W11.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=40  W=38/L=2  WR=95.0%
- Refine: exclude H60=H60b drops 2/2 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W12.  `H60=H60b AND T4=T4c AND direction_exec=long`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude session_bucket=asia_late drops 2/6 losers (33%)
- **Final: n=38  W=34/L=4  WR=89.5%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when session=asia_late

### W13.  `H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=38  W=36/L=2  WR=94.7%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=38  W=33/L=5  WR=86.8%
- Refine: exclude RSI=RSI3 drops 4/5 losers (80%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W15.  `T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=38  W=33/L=5  WR=86.8%
- Refine: exclude H60=H60a drops 3/5 losers (60%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W16.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=37  W=33/L=4  WR=89.2%
- Refine: exclude H60=H60b drops 2/4 losers (50%)
- **Final: n=33  W=31/L=2  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W17.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=37  W=33/L=4  WR=89.2%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

### W18.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude RSI=RSI4 drops 5/5 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W19.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=36  W=36/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid

### W20.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=36  W=36/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid

### W21.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=36  W=34/L=2  WR=94.4%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W22.  `H20=H20d AND H60=H60b AND T4=T4c`
- Raw: n=36  W=32/L=4  WR=88.9%
- Refine: exclude RSI=RSI4 drops 3/4 losers (75%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20d AND T4=T4c AND direction_exec=long`
- Raw: n=36  W=32/L=4  WR=88.9%
- Refine: exclude RSI=RSI4 drops 3/4 losers (75%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20d AND H60=H60b AND T4=T4c AND direction_exec=long`
- Raw: n=36  W=32/L=4  WR=88.9%
- Refine: exclude RSI=RSI4 drops 3/4 losers (75%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W25.  `H20=H20e AND H60=H60e AND BBP=BBP4`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is H60=H60a (20/32 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L02.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is H60=H60a (9/27 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when HTF60 aligned WITH trade

### L03.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_mid (22/28 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L04.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is T4=T4c (22/26 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L05.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is H20=H20b (8/26 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L06.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is direction_exec=short (20/27 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when short

### L07.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is H60=H60a (20/24 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L08.  `H20=H20a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is direction_exec=short (22/25 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when short

### L09.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=37  W=7/L=30  WR=18.9%
- Sharpen: sharpest is H20=H20b (14/30 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L10.  `T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=36  W=12/L=24  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (18/24 of losers there)
- **Sharp: n=23  W=5/L=18  WR=21.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L11.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is T1=T1c (11/23 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L12.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is H60=H60d (6/21 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF60 mildly against

### L13.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is H60=H60d (6/21 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 mildly against

### L14.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is H20=H20a (6/21 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L15.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is direction_exec=short (20/21 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when short

### L16.  `H20=H20a AND H60=H60a AND direction_exec=short`
- Raw: n=32  W=5/L=27  WR=15.6%
- Sharpen: sharpest is session_bucket=ny_mid (20/27 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  ONLY when session=ny_mid

### L17.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=31  W=7/L=24  WR=22.6%
- Sharpen: sharpest is H60=H60a (10/24 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  upper third; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is H60=H60a (15/18 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(32/26) | H20b(12/21) |
| H60 | H60e(31/20) | H60d(12/22) |
| T1 | — | — |
| T4 | T4c(53/44) | T4a(47/56) |
| BBP | BBP0(13/7) | — |
| RSI | — | RSI4(33/38) |
| ZS | ZS1(23/17) | — |
| strategy_id | — | — |
| direction_exec | long(61/44) | short(39/56) |
| session_bucket | asia(13/8) | ny_open(7/13) |

*Read: `bucket(winner%/loser%)`.*
