# CAD_JPY — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,458**  (W=808 / L=650)  -  WR: **55.4%**

## Session distribution

- ny_close: n=350  W=197/L=153  WR=56.3%
- ny_mid: n=335  W=191/L=144  WR=57.0%
- ny_open: n=247  W=150/L=97  WR=60.7%
- london: n=218  W=92/L=126  WR=42.2%
- london_open: n=215  W=128/L=87  WR=59.5%
- asia: n=70  W=37/L=33  WR=52.9%
- off_hours: n=17  W=9/L=8  WR=52.9%
- asia_late: n=6  W=4/L=2  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI2`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H60=H60b drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when HTF60 slightly aligned

### W02.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 slightly aligned

### W03.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 slightly aligned

### W04.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 slightly aligned

### W05.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W06.  `H20=H20e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=london_open  •  AVOID when lower third

### W07.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when lower third

### W08.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude T4=T4a drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude T4=T4a drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude T4=T4a drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude T4=T4a drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude T4=T4a drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude T4=T4a drops 5/8 losers (62%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when lower third

### W15.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  AVOID when lower third

### W16.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W17.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when lower third

### W18.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when lower third

### W19.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W20.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=london_open  •  AVOID when lower third

### W21.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W22.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W23.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when lower third

### W24.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when lower third

### W25.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=293  W=117/L=176  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (76/176 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L02.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=293  W=117/L=176  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (76/176 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L03.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=293  W=117/L=176  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (76/176 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L04.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=293  W=117/L=176  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (76/176 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L05.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=293  W=117/L=176  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (76/176 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L06.  `H20=H20a AND T1=T1c AND BBP=BBP2`
- Raw: n=185  W=70/L=115  WR=37.8%
- Sharpen: sharpest is RSI=RSI0 (76/115 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L07.  `H20=H20a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is RSI=RSI0 (76/109 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third  •  ONLY when RSI<20 extreme oversold

### L08.  `H20=H20a AND H60=H60a AND BBP=BBP2`
- Raw: n=176  W=67/L=109  WR=38.1%
- Sharpen: sharpest is RSI=RSI0 (76/109 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  ONLY when RSI<20 extreme oversold

### L09.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=176  W=67/L=109  WR=38.1%
- Sharpen: sharpest is RSI=RSI0 (76/109 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L10.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=176  W=67/L=109  WR=38.1%
- Sharpen: sharpest is RSI=RSI0 (76/109 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  ONLY when RSI<20 extreme oversold

### L11.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=176  W=67/L=109  WR=38.1%
- Sharpen: sharpest is RSI=RSI0 (76/109 of losers there)
- **Sharp: n=97  W=21/L=76  WR=21.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when RSI<20 extreme oversold

### L12.  `H20=H20a AND T1=T1c AND ZS=ZS2`
- Raw: n=175  W=65/L=110  WR=37.1%
- Sharpen: sharpest is RSI=RSI0 (73/110 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI<20 extreme oversold

### L13.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=175  W=65/L=110  WR=37.1%
- Sharpen: sharpest is RSI=RSI0 (73/110 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI<20 extreme oversold

### L14.  `H20=H20a AND H60=H60a AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L15.  `H20=H20a AND T1=T1c AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L16.  `H20=H20a AND T4=T4c AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L17.  `H20=H20a AND RSI=RSI0 AND direction_exec=long`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L18.  `H60=H60a AND T1=T1c AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L19.  `H60=H60a AND T4=T4c AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L20.  `H60=H60a AND RSI=RSI0 AND direction_exec=long`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L21.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L22.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L23.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L24.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

### L25.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI0`
- Raw: n=171  W=50/L=121  WR=29.2%
- Sharpen: sharpest is ZS=ZS2 (73/121 of losers there)
- **Sharp: n=92  W=19/L=73  WR=20.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when zscore -2 to -1 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(32/23) | H20a(24/35) |
| H60 | H60e(56/40) | H60a(42/58) |
| T1 | T1a(58/39) | T1c(42/61) |
| T4 | T4a(57/43) | T4c(43/57) |
| BBP | — | — |
| RSI | — | RSI0(21/28) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(57/41) | long(43/59) |
| session_bucket | — | london(11/19) |

*Read: `bucket(winner%/loser%)`.*
