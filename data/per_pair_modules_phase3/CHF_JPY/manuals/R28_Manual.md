# CHF_JPY — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,040**  (W=1,885 / L=1,155)  -  WR: **62.0%**

## Session distribution

- asia: n=1371  W=863/L=508  WR=62.9%
- ny_close: n=848  W=531/L=317  WR=62.6%
- london_open: n=238  W=141/L=97  WR=59.2%
- asia_late: n=171  W=108/L=63  WR=63.2%
- london: n=164  W=105/L=59  WR=64.0%
- off_hours: n=137  W=64/L=73  WR=46.7%
- ny_open: n=63  W=44/L=19  WR=69.8%
- ny_mid: n=48  W=29/L=19  WR=60.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude ZS=ZS1 drops 14/14 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W02.  `T4=T4c AND BBP=BBP0 AND session_bucket=ny_close`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W03.  `H20=H20a AND H60=H60a AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W04.  `H20=H20a AND T1=T1c AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W05.  `H20=H20a AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W06.  `H20=H20a AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W07.  `H60=H60a AND T1=T1c AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W08.  `H60=H60a AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W09.  `H60=H60a AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W10.  `T1=T1c AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W11.  `T1=T1c AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W12.  `BBP=BBP0 AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W13.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W14.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W15.  `H20=H20a AND H60=H60a AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W16.  `H20=H20a AND T1=T1c AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W17.  `H20=H20a AND T1=T1c AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W18.  `H20=H20a AND BBP=BBP0 AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W19.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W20.  `H60=H60a AND T1=T1c AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=ny_close

### W21.  `H60=H60a AND BBP=BBP0 AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W22.  `T1=T1c AND BBP=BBP0 AND ZS=ZS0 AND direction_exec=long`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=ny_close

### W23.  `T4=T4c AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude RSI=RSI3 drops 9/9 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore <-3 extreme  •  AVOID when RSI 40-50 lower neutral

### W24.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude ZS=ZS1 drops 9/9 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W25.  `H20=H20a AND T1=T1c AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude ZS=ZS1 drops 9/9 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; session=asia  •  AVOID when zscore -3 to -2 deep oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=135  W=47/L=88  WR=34.8%
- Sharpen: sharpest is ZS=ZS0 (29/88 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L02.  `H60=H60e AND T1=T1a AND BBP=BBP0`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: sharpest is T4=T4a (75/84 of losers there)
- **Sharp: n=110  W=35/L=75  WR=31.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: sharpest is T4=T4a (75/84 of losers there)
- **Sharp: n=110  W=35/L=75  WR=31.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend WITH trade

### L04.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is ZS=ZS0 (29/81 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L05.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=128  W=47/L=81  WR=36.7%
- Sharpen: sharpest is ZS=ZS0 (29/81 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L06.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is ZS=ZS0 (34/78 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L07.  `H60=H60e AND T4=T4a AND BBP=BBP0`
- Raw: n=110  W=35/L=75  WR=31.8%
- Sharpen: sharpest is ZS=ZS0 (29/75 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L08.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=110  W=35/L=75  WR=31.8%
- Sharpen: sharpest is ZS=ZS0 (29/75 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L09.  `H60=H60e AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=110  W=35/L=75  WR=31.8%
- Sharpen: sharpest is ZS=ZS0 (29/75 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L10.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=109  W=39/L=70  WR=35.8%
- Sharpen: sharpest is ZS=ZS0 (29/70 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L11.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=109  W=39/L=70  WR=35.8%
- Sharpen: sharpest is ZS=ZS0 (29/70 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L12.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=104  W=39/L=65  WR=37.5%
- Sharpen: sharpest is T4=T4a (65/65 of losers there)
- **Sharp: n=92  W=27/L=65  WR=29.3%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=104  W=39/L=65  WR=37.5%
- Sharpen: sharpest is T4=T4a (65/65 of losers there)
- **Sharp: n=92  W=27/L=65  WR=29.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=104  W=39/L=65  WR=37.5%
- Sharpen: sharpest is T4=T4a (65/65 of losers there)
- **Sharp: n=92  W=27/L=65  WR=29.3%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L15.  `H60=H60e AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=92  W=27/L=65  WR=29.3%
- Sharpen: sharpest is ZS=ZS0 (29/65 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L16.  `H20=H20e AND T4=T4a AND BBP=BBP0`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is ZS=ZS0 (29/55 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L17.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP0`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is ZS=ZS0 (29/55 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L18.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is ZS=ZS0 (29/55 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L19.  `H20=H20e AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is ZS=ZS0 (29/55 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L20.  `H20=H20e AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is RSI=RSI3 (10/49 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20e AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=75  W=24/L=51  WR=32.0%
- Sharpen: sharpest is ZS=ZS0 (29/51 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L22.  `H60=H60a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is H20=H20a (26/45 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is H20=H20a (26/45 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L24.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is H20=H20a (26/45 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L25.  `H60=H60e AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is ZS=ZS0 (26/45 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; session=asia  •  ONLY when zscore <-3 extreme

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
