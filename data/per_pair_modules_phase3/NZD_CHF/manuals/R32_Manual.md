# NZD_CHF — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **700**  (W=430 / L=270)  -  WR: **61.4%**

## Session distribution

- ny_mid: n=272  W=158/L=114  WR=58.1%
- london_open: n=103  W=67/L=36  WR=65.0%
- asia: n=82  W=61/L=21  WR=74.4%
- ny_close: n=73  W=42/L=31  WR=57.5%
- ny_open: n=67  W=37/L=30  WR=55.2%
- off_hours: n=61  W=37/L=24  WR=60.7%
- london: n=30  W=20/L=10  WR=66.7%
- asia_late: n=12  W=8/L=4  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude H60=H60d drops 4/7 losers (57%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF60 mildly against

### W02.  `H20=H20a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third  •  AVOID when HTF60 mildly against

### W03.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=45  W=41/L=4  WR=91.1%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W04.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=45  W=39/L=6  WR=86.7%
- Refine: exclude H60=H60d drops 4/6 losers (67%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W05.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=44  W=39/L=5  WR=88.6%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 strongly against

### W06.  `H60=H60b AND T1=T1c AND RSI=RSI3`
- Raw: n=43  W=38/L=5  WR=88.4%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W07.  `T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=43  W=37/L=6  WR=86.0%
- Refine: exclude H60=H60e drops 4/6 losers (67%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third  •  AVOID when HTF60 strongly against

### W08.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=42  W=36/L=6  WR=85.7%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF20 mildly against

### W09.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=42  W=36/L=6  WR=85.7%
- Refine: exclude H20=H20d drops 4/6 losers (67%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 mildly against

### W10.  `H20=H20a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=40  W=35/L=5  WR=87.5%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF60 mildly against

### W11.  `T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=40  W=35/L=5  WR=87.5%
- Refine: exclude H60=H60e drops 3/5 losers (60%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W12.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=40  W=35/L=5  WR=87.5%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF60 mildly against

### W13.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=40  W=35/L=5  WR=87.5%
- Refine: exclude H60=H60e drops 3/5 losers (60%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W14.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=38  W=33/L=5  WR=86.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 mildly against

### W15.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=37  W=33/L=4  WR=89.2%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/4 losers (50%)
- **Final: n=35  W=33/L=2  WR=94.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when strategy=bravo_failed_momentum

### W16.  `H60=H60d AND T4=T4a AND RSI=RSI4`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W17.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: exclude BBP=BBP0 drops 4/5 losers (80%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W18.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=34  W=32/L=2  WR=94.1%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=34  W=32/L=2  WR=94.1%
- Refine: no further refinement
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid

### W20.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=34  W=31/L=3  WR=91.2%
- Refine: exclude ZS=ZS1 drops 3/3 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=34  W=30/L=4  WR=88.2%
- Refine: exclude T1=T1a drops 3/4 losers (75%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  AVOID when 1h trend WITH trade

### W22.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=34  W=29/L=5  WR=85.3%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 mildly against

### W23.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=34  W=29/L=5  WR=85.3%
- Refine: exclude H60=H60e drops 3/5 losers (60%)
- **Final: n=24  W=22/L=2  WR=91.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W24.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=32  W=29/L=3  WR=90.6%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W25.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=32  W=29/L=3  WR=90.6%
- Refine: exclude H20=H20c drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=55  W=15/L=40  WR=27.3%
- Sharpen: sharpest is H20=H20a (18/40 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (19/33 of losers there)
- **Sharp: n=26  W=7/L=19  WR=26.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L03.  `H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (24/29 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L04.  `T1=T1c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is direction_exec=short (17/31 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when short

### L05.  `H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=39  W=13/L=26  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (19/26 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L06.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=38  W=9/L=29  WR=23.7%
- Sharpen: sharpest is T1=T1a (19/29 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend WITH trade

### L07.  `H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=37  W=9/L=28  WR=24.3%
- Sharpen: sharpest is RSI=RSI4 (24/28 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L08.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=37  W=13/L=24  WR=35.1%
- Sharpen: sharpest is H60=H60e (13/24 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L09.  `H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=36  W=13/L=23  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (20/23 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L10.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (15/21 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: LONG**  •  4h trend WITH trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L11.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=34  W=10/L=24  WR=29.4%
- Sharpen: sharpest is RSI=RSI4 (16/24 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L12.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is H20=H20b (5/21 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; upper third  •  ONLY when HTF20 slightly aligned

### L13.  `H20=H20a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (12/22 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L14.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is H60=H60d (9/21 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 mildly against

### L15.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=33  W=12/L=21  WR=36.4%
- Sharpen: sharpest is BBP=BBP1 (4/21 of losers there)
- **Sharp: n=4  W=0/L=4  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched lower band

### L16.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=33  W=13/L=20  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_mid (16/20 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when session=ny_mid

### L17.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=32  W=12/L=20  WR=37.5%
- Sharpen: sharpest is H20=H20b (5/20 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 slightly aligned

### L18.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is direction_exec=long (18/20 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when long

### L19.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_open (6/20 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_open

### L20.  `H60=H60b AND T4=T4c AND RSI=RSI4`
- Raw: n=30  W=9/L=21  WR=30.0%
- Sharpen: sharpest is session_bucket=ny_mid (8/21 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L21.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is BBP=BBP2 (13/20 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when lower third

### L22.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=30  W=10/L=20  WR=33.3%
- Sharpen: sharpest is H20=H20a (11/20 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=30  W=11/L=19  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_open (6/19 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L24.  `H20=H20a AND T1=T1a AND RSI=RSI4`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (13/18 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L25.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (6/18 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60c(19/12) | H60e(22/30) |
| T1 | T1c(51/45) | T1a(49/55) |
| T4 | T4c(58/49) | T4a(42/51) |
| BBP | — | BBP4(22/30) |
| RSI | — | — |
| ZS | — | ZS4(20/27) |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | asia(14/8) | ny_mid(37/42) |

*Read: `bucket(winner%/loser%)`.*
