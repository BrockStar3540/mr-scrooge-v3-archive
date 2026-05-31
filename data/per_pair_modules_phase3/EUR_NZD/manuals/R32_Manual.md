# EUR_NZD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,777**  (W=1,580 / L=1,197)  -  WR: **56.9%**

## Session distribution

- asia: n=927  W=544/L=383  WR=58.7%
- london_open: n=492  W=279/L=213  WR=56.7%
- ny_mid: n=406  W=210/L=196  WR=51.7%
- ny_close: n=288  W=170/L=118  WR=59.0%
- london: n=260  W=150/L=110  WR=57.7%
- ny_open: n=251  W=137/L=114  WR=54.6%
- asia_late: n=105  W=61/L=44  WR=58.1%
- off_hours: n=48  W=29/L=19  WR=60.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W02.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W03.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20d drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W04.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20d drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W05.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20d drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W06.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20d drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W07.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20d drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W08.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 13/13 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W09.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W10.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W11.  `H60=H60e AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W12.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W13.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W14.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W15.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=78  W=72/L=6  WR=92.3%
- Refine: exclude H20=H20d drops 6/6 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 mildly against

### W16.  `T4=T4c AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=78  W=72/L=6  WR=92.3%
- Refine: exclude H20=H20d drops 6/6 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 mildly against

### W17.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W18.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W19.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W20.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W22.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W23.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=71  W=68/L=3  WR=95.8%
- Refine: exclude BBP=BBP4 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W24.  `H20=H20c AND H60=H60a AND session_bucket=ny_close`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude RSI=RSI2 drops 7/7 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=ny_close  •  AVOID when RSI 30-40 weak

### W25.  `H20=H20c AND T1=T1a AND session_bucket=ny_close`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude RSI=RSI2 drops 7/7 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=ny_close  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=440  W=173/L=267  WR=39.3%
- Sharpen: sharpest is RSI=RSI2 (103/267 of losers there)
- **Sharp: n=142  W=39/L=103  WR=27.5%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L02.  `H60=H60e AND T1=T1c AND ZS=ZS2`
- Raw: n=348  W=134/L=214  WR=38.5%
- Sharpen: sharpest is T4=T4a (76/214 of losers there)
- **Sharp: n=95  W=19/L=76  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=348  W=134/L=214  WR=38.5%
- Sharpen: sharpest is T4=T4a (76/214 of losers there)
- **Sharp: n=95  W=19/L=76  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L04.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=343  W=134/L=209  WR=39.1%
- Sharpen: sharpest is H60=H60e (151/209 of losers there)
- **Sharp: n=216  W=65/L=151  WR=30.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L05.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=339  W=134/L=205  WR=39.5%
- Sharpen: sharpest is T4=T4a (76/205 of losers there)
- **Sharp: n=95  W=19/L=76  WR=20.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L06.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=275  W=102/L=173  WR=37.1%
- Sharpen: sharpest is ZS=ZS2 (103/173 of losers there)
- **Sharp: n=142  W=39/L=103  WR=27.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L07.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=226  W=75/L=151  WR=33.2%
- Sharpen: sharpest is RSI=RSI2 (87/151 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L08.  `H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=216  W=65/L=151  WR=30.1%
- Sharpen: sharpest is RSI=RSI2 (87/151 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L09.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=216  W=65/L=151  WR=30.1%
- Sharpen: sharpest is RSI=RSI2 (87/151 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=210  W=68/L=142  WR=32.4%
- Sharpen: sharpest is T4=T4a (87/142 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L11.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=210  W=68/L=142  WR=32.4%
- Sharpen: sharpest is T4=T4a (87/142 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L12.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=210  W=68/L=142  WR=32.4%
- Sharpen: sharpest is T4=T4a (87/142 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L13.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=183  W=58/L=125  WR=31.7%
- Sharpen: sharpest is H60=H60e (82/125 of losers there)
- **Sharp: n=103  W=21/L=82  WR=20.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when HTF60 strongly against

### L14.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=175  W=54/L=121  WR=30.9%
- Sharpen: sharpest is session_bucket=asia (57/121 of losers there)
- **Sharp: n=63  W=6/L=57  WR=9.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L15.  `T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=168  W=50/L=118  WR=29.8%
- Sharpen: sharpest is H60=H60e (87/118 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L16.  `T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=168  W=50/L=118  WR=29.8%
- Sharpen: sharpest is H60=H60e (87/118 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L17.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=168  W=50/L=118  WR=29.8%
- Sharpen: sharpest is H60=H60e (87/118 of losers there)
- **Sharp: n=103  W=16/L=87  WR=15.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=165  W=64/L=101  WR=38.8%
- Sharpen: sharpest is T1=T1c (92/101 of losers there)
- **Sharp: n=125  W=33/L=92  WR=26.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak  •  ONLY when 1h trend AGAINST trade

### L19.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=163  W=48/L=115  WR=29.4%
- Sharpen: sharpest is H60=H60e (76/115 of losers there)
- **Sharp: n=95  W=19/L=76  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L20.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=163  W=48/L=115  WR=29.4%
- Sharpen: sharpest is H60=H60e (76/115 of losers there)
- **Sharp: n=95  W=19/L=76  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L21.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=157  W=59/L=98  WR=37.6%
- Sharpen: sharpest is H60=H60e (82/98 of losers there)
- **Sharp: n=103  W=21/L=82  WR=20.4%**
- **Dir: LONG**  •  4h trend WITH trade; lower third  •  ONLY when HTF60 strongly against

### L22.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=155  W=61/L=94  WR=39.4%
- Sharpen: sharpest is T1=T1c (88/94 of losers there)
- **Sharp: n=118  W=30/L=88  WR=25.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L23.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=155  W=61/L=94  WR=39.4%
- Sharpen: sharpest is T1=T1c (88/94 of losers there)
- **Sharp: n=118  W=30/L=88  WR=25.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L24.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=151  W=44/L=107  WR=29.1%
- Sharpen: sharpest is T4=T4a (68/107 of losers there)
- **Sharp: n=89  W=21/L=68  WR=23.6%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L25.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=151  W=44/L=107  WR=29.1%
- Sharpen: sharpest is T4=T4a (68/107 of losers there)
- **Sharp: n=89  W=21/L=68  WR=23.6%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(21/16) | H20a(16/23) |
| H60 | — | — |
| T1 | T1a(57/43) | T1c(43/57) |
| T4 | T4c(54/46) | T4a(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/46) | long(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
