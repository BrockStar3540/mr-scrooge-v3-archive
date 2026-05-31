# EUR_AUD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,385**  (W=2,160 / L=1,225)  -  WR: **63.8%**

## Session distribution

- asia: n=1337  W=836/L=501  WR=62.5%
- ny_close: n=429  W=285/L=144  WR=66.4%
- london: n=372  W=239/L=133  WR=64.2%
- ny_mid: n=358  W=232/L=126  WR=64.8%
- london_open: n=273  W=166/L=107  WR=60.8%
- ny_open: n=270  W=175/L=95  WR=64.8%
- asia_late: n=201  W=135/L=66  WR=67.2%
- off_hours: n=145  W=92/L=53  WR=63.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W02.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W03.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W05.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W07.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W08.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W09.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=219  W=187/L=32  WR=85.4%
- Refine: exclude T4=T4a drops 31/32 losers (97%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude T4=T4a drops 22/23 losers (96%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude T4=T4a drops 22/23 losers (96%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=155  W=132/L=23  WR=85.2%
- Refine: exclude T4=T4a drops 22/23 losers (96%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W13.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude T1=T1c drops 10/13 losers (77%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W14.  `H20=H20a AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude RSI=RSI3 drops 11/13 losers (85%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W15.  `T4=T4c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude T1=T1c drops 9/12 losers (75%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W16.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude T1=T1c drops 9/12 losers (75%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W17.  `H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI3 drops 10/13 losers (77%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W18.  `T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI3 drops 10/13 losers (77%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI3 drops 10/13 losers (77%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W20.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude RSI=RSI3 drops 10/12 losers (83%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W21.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude RSI=RSI3 drops 10/12 losers (83%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W22.  `H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude RSI=RSI3 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W23.  `T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude RSI=RSI3 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W24.  `H20=H20a AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude RSI=RSI3 drops 10/11 losers (91%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

### W25.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=87  W=76/L=11  WR=87.4%
- Refine: exclude RSI=RSI3 drops 9/11 losers (82%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is T4=T4a (34/101 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is T4=T4a (34/101 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is T4=T4a (34/101 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=151  W=59/L=92  WR=39.1%
- Sharpen: sharpest is T4=T4a (33/92 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=151  W=59/L=92  WR=39.1%
- Sharpen: sharpest is T4=T4a (33/92 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=151  W=59/L=92  WR=39.1%
- Sharpen: sharpest is T4=T4a (33/92 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP3`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is RSI=RSI3 (51/64 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; middle of band  •  ONLY when RSI 40-50 lower neutral

### L08.  `H20=H20a AND T1=T1a AND BBP=BBP3 AND direction_exec=short`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is RSI=RSI3 (51/64 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; middle of band  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H20=H20a (51/64 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L10.  `T1=T1a AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H20=H20a (51/64 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: SHORT**  •  1h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (37/54 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L12.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (37/54 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: LONG**  •  4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L13.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (37/54 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L14.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (37/54 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L15.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (37/54 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20a AND H60=H60a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is T1=T1a (51/53 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L17.  `T1=T1a AND T4=T4a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_open (13/50 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L18.  `H20=H20a AND T1=T1a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is H60=H60a (51/51 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L19.  `H60=H60e AND T4=T4a AND ZS=ZS2`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (34/50 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L20.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (34/50 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L21.  `H60=H60e AND T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (34/50 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L22.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (34/50 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L23.  `H60=H60e AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (34/50 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L24.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (34/50 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L25.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (34/50 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(52/47) | H20a(48/53) |
| H60 | — | — |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
