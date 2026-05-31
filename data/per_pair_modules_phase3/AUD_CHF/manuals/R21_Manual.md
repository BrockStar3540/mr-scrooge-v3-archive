# AUD_CHF — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,778**  (W=1,132 / L=646)  -  WR: **63.7%**

## Session distribution

- asia: n=477  W=312/L=165  WR=65.4%
- ny_mid: n=431  W=279/L=152  WR=64.7%
- london_open: n=291  W=188/L=103  WR=64.6%
- ny_close: n=268  W=163/L=105  WR=60.8%
- ny_open: n=226  W=135/L=91  WR=59.7%
- london: n=56  W=36/L=20  WR=64.3%
- off_hours: n=15  W=10/L=5  WR=66.7%
- asia_late: n=14  W=9/L=5  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4a AND RSI=RSI2`
- Raw: n=125  W=111/L=14  WR=88.8%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=off_hours

### W02.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI2`
- Raw: n=125  W=111/L=14  WR=88.8%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=off_hours

### W03.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=125  W=111/L=14  WR=88.8%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=off_hours

### W04.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=125  W=111/L=14  WR=88.8%
- Refine: exclude session_bucket=off_hours drops 5/14 losers (36%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=off_hours

### W05.  `H20=H20e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4c drops 11/13 losers (85%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4c drops 11/13 losers (85%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W07.  `T4=T4a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=88  W=82/L=6  WR=93.2%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W08.  `H20=H20e AND H60=H60e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude T4=T4c drops 11/13 losers (85%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20e AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude T4=T4c drops 11/13 losers (85%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W10.  `T4=T4a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W11.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=86  W=80/L=6  WR=93.0%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W12.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=off_hours

### W13.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W14.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP3 drops 5/9 losers (56%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when middle of band

### W15.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP3 drops 5/9 losers (56%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when middle of band

### W16.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP3 drops 5/9 losers (56%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when middle of band

### W17.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=off_hours

### W18.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=off_hours

### W19.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=74  W=68/L=6  WR=91.9%
- Refine: exclude H20=H20b drops 4/6 losers (67%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 slightly aligned

### W20.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: no further refinement
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia

### W21.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: no further refinement
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia

### W22.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: no further refinement
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia

### W23.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: no further refinement
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia

### W24.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude T4=T4c drops 8/10 losers (80%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W25.  `T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (18/57 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L02.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (18/57 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L03.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is session_bucket=london_open (18/57 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L04.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is BBP=BBP0 (28/58 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L05.  `H20=H20e AND T1=T1a AND BBP=BBP1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (11/48 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band  •  ONLY when session=ny_close

### L06.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (11/48 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; just touched lower band  •  ONLY when session=ny_close

### L07.  `H20=H20e AND T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (11/48 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L08.  `H20=H20e AND T1=T1a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (11/48 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band  •  ONLY when session=ny_close

### L09.  `H20=H20a AND T4=T4c AND RSI=RSI2`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is session_bucket=london_open (18/51 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L10.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is session_bucket=london_open (18/51 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L11.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is session_bucket=london_open (18/51 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L12.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is session_bucket=london_open (18/51 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L13.  `H20=H20a AND T4=T4c AND BBP=BBP2`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (18/48 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=london_open

### L14.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (18/48 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=london_open

### L15.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (18/48 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=london_open

### L16.  `H20=H20a AND T4=T4c AND ZS=ZS2`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (18/46 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L17.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (18/46 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L18.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (18/46 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L19.  `H20=H20a AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=london_open (18/46 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L20.  `H20=H20e AND T4=T4c AND BBP=BBP1`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_close (11/45 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=ny_close

### L21.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP1`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_close (11/45 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=ny_close

### L22.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_close (11/45 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_close (11/45 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=ny_close

### L24.  `H60=H60a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is T1=T1a (7/44 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when 1h trend WITH trade

### L25.  `ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is T1=T1a (7/44 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=asia  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(55/49) | T1a(45/51) |
| T4 | T4a(60/43) | T4c(40/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
