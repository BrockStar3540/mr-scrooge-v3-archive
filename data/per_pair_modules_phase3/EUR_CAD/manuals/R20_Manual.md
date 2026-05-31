# EUR_CAD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,009**  (W=1,276 / L=733)  -  WR: **63.5%**

## Session distribution

- london_open: n=471  W=302/L=169  WR=64.1%
- ny_open: n=451  W=281/L=170  WR=62.3%
- ny_mid: n=305  W=188/L=117  WR=61.6%
- asia: n=246  W=157/L=89  WR=63.8%
- london: n=226  W=156/L=70  WR=69.0%
- ny_close: n=194  W=124/L=70  WR=63.9%
- asia_late: n=101  W=60/L=41  WR=59.4%
- off_hours: n=15  W=8/L=7  WR=53.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W02.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `H20=H20e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude RSI=RSI3 drops 5/14 losers (36%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: ?**  •  HTF20 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W05.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H60=H60b drops 8/14 losers (57%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF60 slightly aligned

### W06.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=93  W=87/L=6  WR=93.5%
- Refine: exclude BBP=BBP4 drops 3/6 losers (50%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W07.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when 4h trend WITH trade

### W08.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20e AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: LONG**  •  HTF20 strongly against; session=asia  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when 4h trend WITH trade

### W12.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T4=T4a drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude session_bucket=london drops 8/8 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london

### W14.  `T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H20=H20a drops 7/11 losers (64%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_open

### W16.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_open

### W17.  `H20=H20e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=asia  •  AVOID when HTF60 strongly against

### W18.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP4 drops 3/6 losers (50%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W19.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP4 drops 3/6 losers (50%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W20.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP4 drops 3/6 losers (50%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W21.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude session_bucket=london drops 8/8 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london

### W22.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W23.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W24.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when zscore -2 to -1 oversold

### W25.  `H60=H60a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude ZS=ZS2 drops 6/6 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI3 (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L02.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is RSI=RSI3 (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L03.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is H20=H20d (15/67 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 mildly against

### L04.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is H20=H20d (15/67 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 mildly against

### L05.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (25/59 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  lower third; session=ny_open  •  ONLY when RSI 30-40 weak

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is H20=H20d (15/57 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 mildly against

### L07.  `ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is RSI=RSI2 (25/55 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=ny_open  •  ONLY when RSI 30-40 weak

### L08.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is RSI=RSI2 (25/55 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold; session=ny_open  •  ONLY when RSI 30-40 weak

### L09.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=84  W=28/L=56  WR=33.3%
- Sharpen: sharpest is T1=T1a (21/56 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=84  W=28/L=56  WR=33.3%
- Sharpen: sharpest is T1=T1a (21/56 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L11.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (25/51 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=ny_open  •  ONLY when RSI 30-40 weak

### L12.  `T1=T1c AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (25/51 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  ONLY when RSI 30-40 weak

### L13.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is H20=H20d (13/51 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=ny_open  •  ONLY when HTF20 mildly against

### L14.  `T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is H20=H20e (31/50 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  ONLY when HTF20 strongly against

### L15.  `T4=T4c AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is H20=H20d (13/47 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  ONLY when HTF20 mildly against

### L16.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is H20=H20d (13/46 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_open  •  ONLY when HTF20 mildly against

### L17.  `H60=H60e AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is H20=H20d (13/46 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; session=ny_open  •  ONLY when HTF20 mildly against

### L18.  `T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is H20=H20a (30/45 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  ONLY when HTF20 aligned WITH trade

### L19.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is H20=H20d (13/44 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; session=ny_open  •  ONLY when HTF20 mildly against

### L20.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is H60=H60a (12/42 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L21.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=57  W=7/L=50  WR=12.3%
- Sharpen: sharpest is ZS=ZS2 (24/50 of losers there)
- **Sharp: n=25  W=1/L=24  WR=4.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L22.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is BBP=BBP2 (25/35 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L23.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is BBP=BBP2 (25/35 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L24.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is BBP=BBP2 (25/35 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when lower third

### L25.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is RSI=RSI2 (27/35 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(46/38) | H60e(40/47) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/46) | long(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
