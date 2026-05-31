# GBP_USD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,259**  (W=2,067 / L=1,192)  -  WR: **63.4%**

## Session distribution

- asia: n=1706  W=1115/L=591  WR=65.4%
- ny_close: n=604  W=373/L=231  WR=61.8%
- off_hours: n=250  W=171/L=79  WR=68.4%
- asia_late: n=197  W=112/L=85  WR=56.9%
- london: n=184  W=118/L=66  WR=64.1%
- london_open: n=180  W=102/L=78  WR=56.7%
- ny_open: n=80  W=43/L=37  WR=53.8%
- ny_mid: n=58  W=33/L=25  WR=56.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=138  W=122/L=16  WR=88.4%
- Refine: exclude H60=H60d drops 6/16 losers (38%)
- **Final: n=126  W=116/L=10  WR=92.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 mildly against

### W02.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=138  W=118/L=20  WR=85.5%
- Refine: exclude T1=T1c drops 16/20 losers (80%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when 1h trend AGAINST trade

### W03.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=132  W=113/L=19  WR=85.6%
- Refine: exclude T4=T4c drops 15/19 losers (79%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=132  W=113/L=19  WR=85.6%
- Refine: exclude T4=T4c drops 15/19 losers (79%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W05.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=127  W=117/L=10  WR=92.1%
- Refine: exclude strategy_id=BR5_opening_range_breakout_short drops 4/10 losers (40%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=BR5_opening_range_breakout_short

### W06.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude session_bucket=ny_close drops 9/15 losers (60%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W07.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude BBP=BBP0 drops 12/16 losers (75%)
- **Final: n=103  W=99/L=4  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W08.  `T4=T4a AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude H60=H60e drops 14/16 losers (88%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 strongly against

### W09.  `T1=T1c AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20e drops 6/10 losers (60%)
- **Final: n=100  W=96/L=4  WR=96.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W10.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude session_bucket=off_hours drops 7/11 losers (64%)
- **Final: n=101  W=97/L=4  WR=96.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when session=off_hours

### W11.  `H20=H20a AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=113  W=103/L=10  WR=91.2%
- Refine: exclude session_bucket=off_hours drops 7/10 losers (70%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=off_hours

### W12.  `H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=109  W=103/L=6  WR=94.5%
- Refine: exclude session_bucket=ny_close drops 3/6 losers (50%)
- **Final: n=93  W=90/L=3  WR=96.8%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W13.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude session_bucket=off_hours drops 7/11 losers (64%)
- **Final: n=93  W=89/L=4  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=off_hours

### W14.  `H60=H60b AND T4=T4a AND session_bucket=asia`
- Raw: n=101  W=95/L=6  WR=94.1%
- Refine: exclude T1=T1c drops 5/6 losers (83%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; session=asia  •  AVOID when 1h trend AGAINST trade

### W15.  `H60=H60b AND T4=T4a AND direction_exec=short`
- Raw: n=98  W=87/L=11  WR=88.8%
- Refine: exclude T1=T1c drops 7/11 losers (64%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20a AND T1=T1a AND BBP=BBP4`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude RSI=RSI3 drops 11/11 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W17.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=96  W=92/L=4  WR=95.8%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W18.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude ZS=ZS0 drops 3/9 losers (33%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when zscore <-3 extreme

### W19.  `H60=H60b AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=91  W=87/L=4  WR=95.6%
- Refine: exclude ZS=ZS2 drops 3/4 losers (75%)
- **Final: n=76  W=75/L=1  WR=98.7%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W20.  `H20=H20a AND H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude T1=T1c drops 9/10 losers (90%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when 1h trend AGAINST trade

### W21.  `H20=H20a AND T1=T1a AND ZS=ZS4`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude RSI=RSI3 drops 9/9 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude RSI=RSI3 drops 9/9 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W23.  `T1=T1c AND T4=T4a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H20=H20e drops 5/10 losers (50%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep below lower band; session=asia  •  AVOID when HTF20 strongly against

### W24.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude direction_exec=long drops 11/12 losers (92%)
- **Final: n=75  W=74/L=1  WR=98.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when long

### W25.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude T1=T1c drops 9/10 losers (90%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=163  W=60/L=103  WR=36.8%
- Sharpen: sharpest is T4=T4c (62/103 of losers there)
- **Sharp: n=88  W=26/L=62  WR=29.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L02.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=163  W=60/L=103  WR=36.8%
- Sharpen: sharpest is T4=T4c (62/103 of losers there)
- **Sharp: n=88  W=26/L=62  WR=29.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L03.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=127  W=46/L=81  WR=36.2%
- Sharpen: sharpest is T1=T1c (57/81 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when 1h trend AGAINST trade

### L04.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is session_bucket=asia (62/78 of losers there)
- **Sharp: n=85  W=23/L=62  WR=27.1%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when session=asia

### L05.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is H60=H60a (57/73 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF60 aligned WITH trade

### L06.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=118  W=43/L=75  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (57/75 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L07.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=118  W=43/L=75  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (57/75 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L08.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=112  W=41/L=71  WR=36.6%
- Sharpen: sharpest is session_bucket=asia (57/71 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L09.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: sharpest is BBP=BBP0 (44/70 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L10.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=108  W=42/L=66  WR=38.9%
- Sharpen: sharpest is H60=H60a (34/66 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L11.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4c (57/62 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4c (57/62 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=95  W=34/L=61  WR=35.8%
- Sharpen: sharpest is H20=H20e (28/61 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L14.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is RSI=RSI3 (42/55 of losers there)
- **Sharp: n=57  W=15/L=42  WR=26.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L15.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=85  W=23/L=62  WR=27.1%
- Sharpen: sharpest is T4=T4a (36/62 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L16.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (44/52 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L17.  `H20=H20e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is BBP=BBP0 (27/50 of losers there)
- **Sharp: n=37  W=10/L=27  WR=27.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L18.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=82  W=27/L=55  WR=32.9%
- Sharpen: sharpest is BBP=BBP0 (28/55 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L19.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is H20=H20e (45/52 of losers there)
- **Sharp: n=58  W=13/L=45  WR=22.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L20.  `H20=H20e AND H60=H60d AND RSI=RSI3`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T1=T1c (24/48 of losers there)
- **Sharp: n=33  W=9/L=24  WR=27.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L21.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is H20=H20e (40/47 of losers there)
- **Sharp: n=59  W=19/L=40  WR=32.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L22.  `H20=H20e AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is T4=T4c (39/48 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20e AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is T4=T4c (39/48 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20e AND H60=H60d AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (13/45 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; session=asia  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is H60=H60b (9/44 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/38) | H20e(37/44) |
| H60 | H60e(35/30) | H60a(31/36) |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | T4a(57/43) | T4c(43/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/46) | long(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
