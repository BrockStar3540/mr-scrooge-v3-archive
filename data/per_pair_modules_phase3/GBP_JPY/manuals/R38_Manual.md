# GBP_JPY — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **7,519**  (W=4,084 / L=3,435)  -  WR: **54.3%**

## Session distribution

- asia: n=1940  W=1066/L=874  WR=54.9%
- ny_mid: n=1732  W=923/L=809  WR=53.3%
- london_open: n=1114  W=598/L=516  WR=53.7%
- london: n=906  W=483/L=423  WR=53.3%
- ny_open: n=834  W=447/L=387  WR=53.6%
- ny_close: n=783  W=468/L=315  WR=59.8%
- asia_late: n=174  W=84/L=90  WR=48.3%
- off_hours: n=36  W=15/L=21  WR=41.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60b AND T4=T4a AND BBP=BBP4`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude ZS=ZS4 drops 10/12 losers (83%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; upper third  •  AVOID when zscore +1 to +2 overbought

### W02.  `H20=H20e AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: no further refinement
- **Final: n=80  W=69/L=11  WR=86.2%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; session=asia

### W03.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: no further refinement
- **Final: n=80  W=69/L=11  WR=86.2%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold; session=asia

### W04.  `H60=H60b AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF60 slightly aligned; upper third; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W05.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: no further refinement
- **Final: n=77  W=66/L=11  WR=85.7%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak; session=asia

### W06.  `H60=H60b AND T4=T4a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W07.  `H60=H60a AND ZS=ZS1 AND session_bucket=london`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude RSI=RSI2 drops 4/4 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when RSI 30-40 weak

### W08.  `H60=H60a AND T1=T1c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude RSI=RSI2 drops 4/4 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when RSI 30-40 weak

### W09.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND session_bucket=london`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude RSI=RSI2 drops 4/4 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when RSI 30-40 weak

### W10.  `H60=H60a AND ZS=ZS1 AND direction_exec=long AND session_bucket=london`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude RSI=RSI2 drops 4/4 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when RSI 30-40 weak

### W11.  `H20=H20e AND H60=H60a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: no further refinement
- **Final: n=64  W=56/L=8  WR=87.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; just touched lower band; session=asia

### W12.  `H20=H20e AND T1=T1c AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: no further refinement
- **Final: n=64  W=56/L=8  WR=87.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched lower band; session=asia

### W13.  `H20=H20e AND BBP=BBP1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: no further refinement
- **Final: n=64  W=56/L=8  WR=87.5%**
- **Dir: LONG**  •  HTF20 strongly against; just touched lower band; session=asia

### W14.  `H60=H60b AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude ZS=ZS4 drops 7/9 losers (78%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20a AND BBP=BBP0 AND RSI=RSI1`
- Raw: n=61  W=61/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 20-30 oversold

### W16.  `T4=T4a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20e drops 9/9 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W17.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND session_bucket=london`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI2 drops 4/4 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=london  •  AVOID when RSI 30-40 weak

### W18.  `H60=H60b AND T1=T1c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude ZS=ZS4 drops 5/7 losers (71%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W19.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W20.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: no further refinement
- **Final: n=56  W=48/L=8  WR=85.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; session=asia

### W21.  `H20=H20d AND T1=T1c AND T4=T4a`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude BBP=BBP1 drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when just touched lower band

### W22.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/4 losers (75%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when strategy=bravo_expansion_continuation

### W23.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/4 losers (75%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when strategy=bravo_expansion_continuation

### W24.  `H20=H20e AND RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/4 losers (75%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when strategy=bravo_expansion_continuation

### W25.  `H20=H20a AND T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=48  W=43/L=5  WR=89.6%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND RSI=RSI1`
- Raw: n=370  W=144/L=226  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=370  W=144/L=226  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 20-30 oversold

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI1`
- Raw: n=370  W=144/L=226  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=370  W=144/L=226  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold

### L03.  `H20=H20e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=370  W=144/L=226  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=370  W=144/L=226  WR=38.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold

### L04.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=370  W=144/L=226  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=370  W=144/L=226  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold

### L05.  `H20=H20e AND H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=370  W=144/L=226  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=370  W=144/L=226  WR=38.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 20-30 oversold

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=370  W=144/L=226  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=370  W=144/L=226  WR=38.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold

### L07.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=369  W=144/L=225  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=369  W=144/L=225  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold

### L08.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=369  W=144/L=225  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=369  W=144/L=225  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=369  W=144/L=225  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=369  W=144/L=225  WR=39.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold

### L10.  `H60=H60a AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=305  W=122/L=183  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=305  W=122/L=183  WR=40.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia

### L11.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=273  W=108/L=165  WR=39.6%
- Sharpen: sharpest is H20=H20e (54/165 of losers there)
- **Sharp: n=73  W=19/L=54  WR=26.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=273  W=109/L=164  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=273  W=109/L=164  WR=39.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid

### L13.  `RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=273  W=109/L=164  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=273  W=109/L=164  WR=39.9%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=ny_mid

### L14.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=273  W=109/L=164  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=273  W=109/L=164  WR=39.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid

### L15.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=272  W=107/L=165  WR=39.3%
- Sharpen: sharpest is H20=H20e (55/165 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L16.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=272  W=107/L=165  WR=39.3%
- Sharpen: sharpest is H20=H20e (55/165 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L17.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=272  W=107/L=165  WR=39.3%
- Sharpen: sharpest is H20=H20e (55/165 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=271  W=107/L=164  WR=39.5%
- Sharpen: sharpest is H20=H20e (54/164 of losers there)
- **Sharp: n=73  W=19/L=54  WR=26.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L19.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=271  W=107/L=164  WR=39.5%
- Sharpen: sharpest is H20=H20e (54/164 of losers there)
- **Sharp: n=73  W=19/L=54  WR=26.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L20.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=263  W=105/L=158  WR=39.9%
- Sharpen: sharpest is H20=H20e (55/158 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L21.  `H60=H60a AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=263  W=105/L=158  WR=39.9%
- Sharpen: sharpest is H20=H20e (55/158 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L22.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=254  W=95/L=159  WR=37.4%
- Sharpen: sharpest is H20=H20b (35/159 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

### L23.  `T1=T1c AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=249  W=97/L=152  WR=39.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_mid

### L24.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=249  W=97/L=152  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=249  W=97/L=152  WR=39.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_mid

### L25.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=247  W=95/L=152  WR=38.5%
- Sharpen: sharpest is H20=H20b (35/152 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

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
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
