# AUD_CAD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,906**  (W=1,171 / L=735)  -  WR: **61.4%**

## Session distribution

- asia: n=560  W=350/L=210  WR=62.5%
- london_open: n=469  W=287/L=182  WR=61.2%
- ny_close: n=234  W=139/L=95  WR=59.4%
- ny_mid: n=194  W=112/L=82  WR=57.7%
- london: n=138  W=83/L=55  WR=60.1%
- ny_open: n=132  W=84/L=48  WR=63.6%
- off_hours: n=95  W=57/L=38  WR=60.0%
- asia_late: n=84  W=59/L=25  WR=70.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W03.  `H20=H20a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W04.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=asia drops 11/11 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W05.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W06.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W07.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W08.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W09.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W10.  `H60=H60a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W11.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W12.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W13.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W14.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude H60=H60e drops 5/8 losers (62%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W15.  `H20=H20a AND H60=H60e AND RSI=RSI2`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS1 drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W16.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS1 drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W17.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS1 drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W18.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI2`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS1 drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `H20=H20a AND H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS1 drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude ZS=ZS1 drops 8/8 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W22.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude T1=T1a drops 6/8 losers (75%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W23.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude H20=H20c drops 2/6 losers (33%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 neutral

### W24.  `H60=H60a AND T4=T4c AND session_bucket=asia_late`
- Raw: n=53  W=51/L=2  WR=96.2%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=53  W=51/L=2  WR=96.2%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is H20=H20e (40/68 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L02.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is H20=H20e (40/68 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L03.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is H20=H20e (40/68 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is H20=H20e (40/68 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L05.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (19/57 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=london_open

### L06.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (19/57 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=london_open

### L07.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (19/57 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=london_open

### L08.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (27/55 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L09.  `H60=H60a AND T4=T4c AND RSI=RSI2`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is H20=H20e (32/51 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is H20=H20e (32/51 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L11.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is H20=H20e (32/51 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L12.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is H20=H20e (32/51 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L13.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is H20=H20e (32/51 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is H20=H20e (32/51 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L15.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is BBP=BBP2 (19/49 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when lower third

### L16.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is H60=H60a (37/49 of losers there)
- **Sharp: n=46  W=9/L=37  WR=19.6%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is BBP=BBP2 (19/49 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  ONLY when lower third

### L18.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is BBP=BBP2 (19/49 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when lower third

### L19.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is BBP=BBP2 (19/49 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when lower third

### L20.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is BBP=BBP2 (19/49 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when lower third

### L21.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS2`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (17/48 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L22.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is session_bucket=london_open (17/48 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L23.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is session_bucket=london_open (18/46 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when session=london_open

### L24.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=72  W=27/L=45  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (37/45 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L25.  `H60=H60e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=72  W=27/L=45  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (37/45 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/34) | H20e(36/44) |
| H60 | H60a(52/47) | H60e(48/53) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/47) | short(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
