# EUR_USD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,642**  (W=1,002 / L=640)  -  WR: **61.0%**

## Session distribution

- ny_close: n=444  W=270/L=174  WR=60.8%
- asia: n=425  W=262/L=163  WR=61.6%
- ny_mid: n=366  W=213/L=153  WR=58.2%
- london_open: n=177  W=115/L=62  WR=65.0%
- ny_open: n=140  W=84/L=56  WR=60.0%
- off_hours: n=37  W=23/L=14  WR=62.2%
- london: n=27  W=20/L=7  WR=74.1%
- asia_late: n=26  W=15/L=11  WR=57.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude H60=H60e drops 15/15 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 strongly against

### W02.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude H60=H60e drops 15/15 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 strongly against

### W03.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude H60=H60e drops 15/15 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 strongly against

### W04.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude BBP=BBP1 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when just touched lower band

### W05.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude BBP=BBP1 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when just touched lower band

### W06.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude BBP=BBP1 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when just touched lower band

### W07.  `H20=H20e AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude BBP=BBP1 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when just touched lower band

### W08.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W09.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when just touched lower band

### W10.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W11.  `H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when just touched lower band

### W12.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W13.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W14.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W15.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  AVOID when just touched lower band

### W16.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W17.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W18.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W19.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W20.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W21.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W22.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched lower band

### W23.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W24.  `H20=H20a AND T4=T4c AND direction_exec=short`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W25.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=113  W=40/L=73  WR=35.4%
- Sharpen: sharpest is RSI=RSI2 (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L02.  `H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=113  W=40/L=73  WR=35.4%
- Sharpen: sharpest is RSI=RSI2 (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_close  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=113  W=40/L=73  WR=35.4%
- Sharpen: sharpest is RSI=RSI2 (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L04.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is T1=T1c (36/73 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is T4=T4a (39/62 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is T4=T4a (39/62 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_close  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is T4=T4a (39/62 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is T4=T4a (39/62 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  ONLY when 4h trend WITH trade

### L09.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is T4=T4a (39/62 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when 4h trend WITH trade

### L10.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=98  W=27/L=71  WR=27.6%
- Sharpen: sharpest is H60=H60e (40/71 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 strongly against

### L11.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=98  W=27/L=71  WR=27.6%
- Sharpen: sharpest is H60=H60e (40/71 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 strongly against

### L12.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=98  W=27/L=71  WR=27.6%
- Sharpen: sharpest is H60=H60e (40/71 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 strongly against

### L13.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=89  W=27/L=62  WR=30.3%
- Sharpen: sharpest is T1=T1c (36/62 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=89  W=27/L=62  WR=30.3%
- Sharpen: sharpest is T1=T1c (36/62 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is T1=T1c (21/52 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L16.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=79  W=28/L=51  WR=35.4%
- Sharpen: sharpest is H20=H20e (39/51 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L17.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=79  W=28/L=51  WR=35.4%
- Sharpen: sharpest is H20=H20e (39/51 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=79  W=28/L=51  WR=35.4%
- Sharpen: sharpest is H20=H20e (39/51 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L19.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=72  W=26/L=46  WR=36.1%
- Sharpen: sharpest is H20=H20e (35/46 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L20.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP2 (30/45 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L21.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP2 (30/45 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when lower third

### L22.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP2 (30/45 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L23.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (36/44 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L24.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (36/44 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L25.  `H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (36/44 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(53/41) | H20e(42/54) |
| H60 | H60a(59/40) | H60e(41/59) |
| T1 | — | — |
| T4 | T4a(58/44) | T4c(42/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
