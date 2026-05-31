# EUR_GBP — R33 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,183**  (W=774 / L=409)  -  WR: **65.4%**

## Session distribution

- ny_mid: n=432  W=281/L=151  WR=65.0%
- london_open: n=280  W=195/L=85  WR=69.6%
- ny_open: n=146  W=89/L=57  WR=61.0%
- asia: n=102  W=63/L=39  WR=61.8%
- london: n=95  W=65/L=30  WR=68.4%
- ny_close: n=73  W=50/L=23  WR=68.5%
- asia_late: n=38  W=22/L=16  WR=57.9%
- off_hours: n=17  W=9/L=8  WR=52.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude BBP=BBP6 drops 5/14 losers (36%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when deep above upper band

### W02.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60e drops 9/11 losers (82%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 strongly against

### W03.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H60=H60b drops 8/10 losers (80%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W04.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H60=H60b drops 8/10 losers (80%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF60 slightly aligned

### W05.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W06.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=60  W=60/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third

### W07.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold

### W08.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=56  W=56/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold

### W09.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude H20=H20e drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W10.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude H20=H20d drops 3/8 losers (38%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 mildly against

### W11.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=52  W=48/L=4  WR=92.3%
- Refine: exclude BBP=BBP6 drops 2/4 losers (50%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when deep above upper band

### W12.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS3 drops 3/7 losers (43%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20b AND T4=T4a AND ZS=ZS2`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude direction_exec=short drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when short

### W14.  `H20=H20b AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude direction_exec=short drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when short

### W15.  `H60=H60d AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude T4=T4c drops 5/7 losers (71%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF60 mildly against; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W16.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when 1h trend WITH trade

### W17.  `H60=H60d AND T4=T4a AND RSI=RSI3`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W18.  `H20=H20b AND T4=T4a AND session_bucket=london_open`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude T1=T1a drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when lower third

### W20.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF60 strongly against

### W21.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude direction_exec=short drops 3/5 losers (60%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when short

### W22.  `H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W23.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude H20=H20e drops 5/5 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 strongly against

### W24.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=46  W=40/L=6  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 4/6 losers (67%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W25.  `H60=H60d AND RSI=RSI3 AND direction_exec=long`
- Raw: n=46  W=40/L=6  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is H20=H20d (22/40 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L02.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is ZS=ZS2 (10/39 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore -2 to -1 oversold

### L03.  `T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is H60=H60e (10/34 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third  •  ONLY when HTF60 strongly against

### L04.  `H20=H20d AND H60=H60a AND T4=T4c`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is T1=T1a (22/34 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when 1h trend WITH trade

### L05.  `H20=H20d AND T4=T4c AND direction_exec=short`
- Raw: n=52  W=14/L=38  WR=26.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=52  W=14/L=38  WR=26.9%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade

### L06.  `T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=47  W=15/L=32  WR=31.9%
- Sharpen: sharpest is T4=T4c (10/32 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L07.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=47  W=15/L=32  WR=31.9%
- Sharpen: sharpest is ZS=ZS1 (11/32 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=47  W=15/L=32  WR=31.9%
- Sharpen: sharpest is T4=T4c (10/32 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L09.  `T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is H60=H60a (13/28 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF60 aligned WITH trade

### L10.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=43  W=14/L=29  WR=32.6%
- Sharpen: sharpest is direction_exec=long (15/29 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when long

### L11.  `T4=T4c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP3 (18/25 of losers there)
- **Sharp: n=25  W=7/L=18  WR=28.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when middle of band

### L12.  `T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is H60=H60a (11/25 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L13.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is H60=H60a (11/25 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L14.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is direction_exec=short (20/23 of losers there)
- **Sharp: n=27  W=7/L=20  WR=25.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when short

### L15.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=36  W=14/L=22  WR=38.9%
- Sharpen: sharpest is H20=H20a (9/22 of losers there)
- **Sharp: n=11  W=2/L=9  WR=18.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is H20=H20d (11/21 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 mildly against

### L17.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=35  W=14/L=21  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (7/21 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L18.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=34  W=11/L=23  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (6/23 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L19.  `T4=T4c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=34  W=12/L=22  WR=35.3%
- Sharpen: sharpest is H20=H20d (12/22 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF20 mildly against

### L20.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=34  W=12/L=22  WR=35.3%
- Sharpen: sharpest is direction_exec=long (15/22 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when long

### L21.  `T1=T1c AND T4=T4c AND session_bucket=london`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is direction_exec=short (8/21 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  ONLY when short

### L22.  `T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=34  W=13/L=21  WR=38.2%
- Sharpen: sharpest is H60=H60e (7/21 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L23.  `H20=H20a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=33  W=9/L=24  WR=27.3%
- Sharpen: sharpest is H60=H60e (7/24 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third  •  ONLY when HTF60 strongly against

### L24.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=32  W=11/L=21  WR=34.4%
- Sharpen: sharpest is direction_exec=short (19/21 of losers there)
- **Sharp: n=24  W=5/L=19  WR=20.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when short

### L25.  `H20=H20d AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=32  W=11/L=21  WR=34.4%
- Sharpen: sharpest is T1=T1a (13/21 of losers there)
- **Sharp: n=18  W=5/L=13  WR=27.8%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/48) | short(43/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
