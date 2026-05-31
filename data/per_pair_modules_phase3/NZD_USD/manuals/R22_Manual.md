# NZD_USD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,796**  (W=1,131 / L=665)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=567  W=354/L=213  WR=62.4%
- asia: n=439  W=289/L=150  WR=65.8%
- london_open: n=313  W=197/L=116  WR=62.9%
- ny_open: n=198  W=120/L=78  WR=60.6%
- ny_close: n=119  W=69/L=50  WR=58.0%
- asia_late: n=84  W=57/L=27  WR=67.9%
- london: n=72  W=42/L=30  WR=58.3%
- off_hours: n=4  W=3/L=1  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W02.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W03.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W04.  `T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude H20=H20e drops 7/10 losers (70%)
- **Final: n=88  W=85/L=3  WR=96.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W05.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude H20=H20e drops 7/10 losers (70%)
- **Final: n=88  W=85/L=3  WR=96.6%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W06.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude H20=H20e drops 7/10 losers (70%)
- **Final: n=88  W=85/L=3  WR=96.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W07.  `H20=H20a AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 4/13 losers (31%)
- **Final: n=85  W=76/L=9  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W08.  `H20=H20a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=88  W=83/L=5  WR=94.3%
- Refine: exclude H60=H60e drops 5/5 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 strongly against

### W09.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude T1=T1c drops 5/11 losers (45%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W10.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20e drops 6/9 losers (67%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W11.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20e drops 6/9 losers (67%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W12.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=80  W=75/L=5  WR=93.8%
- Refine: exclude H60=H60e drops 5/5 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 strongly against

### W13.  `T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20b drops 6/12 losers (50%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=asia  •  AVOID when HTF20 slightly aligned

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W15.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W16.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=76  W=73/L=3  WR=96.1%
- Refine: exclude H60=H60e drops 3/3 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 strongly against

### W17.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=76  W=73/L=3  WR=96.1%
- Refine: exclude H60=H60e drops 3/3 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 strongly against

### W18.  `H20=H20a AND H60=H60e AND session_bucket=london_open`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude BBP=BBP5 drops 2/11 losers (18%)
- **Final: n=74  W=65/L=9  WR=87.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  AVOID when just touched upper band

### W19.  `T1=T1a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude RSI=RSI3 drops 5/11 losers (45%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W20.  `ZS=ZS2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude RSI=RSI3 drops 5/11 losers (45%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W21.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude RSI=RSI3 drops 5/11 losers (45%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W22.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude RSI=RSI3 drops 5/11 losers (45%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W23.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude RSI=RSI3 drops 5/11 losers (45%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W24.  `H20=H20a AND H60=H60a AND BBP=BBP1`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/8 losers (75%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band  •  AVOID when RSI 40-50 lower neutral

### W25.  `H20=H20a AND H60=H60a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/8 losers (75%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND RSI=RSI2`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is BBP=BBP1 (26/83 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L02.  `H20=H20e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is BBP=BBP1 (26/83 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when just touched lower band

### L03.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is BBP=BBP1 (26/83 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L04.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (23/82 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L05.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=128  W=48/L=80  WR=37.5%
- Sharpen: sharpest is H60=H60a (41/80 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when HTF60 aligned WITH trade

### L06.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is ZS=ZS1 (30/84 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=123  W=48/L=75  WR=39.0%
- Sharpen: sharpest is H60=H60a (36/75 of losers there)
- **Sharp: n=47  W=11/L=36  WR=23.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when HTF60 aligned WITH trade

### L08.  `H20=H20e AND T1=T1a AND ZS=ZS2`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is H60=H60a (38/73 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L09.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is H60=H60a (38/73 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is T4=T4a (49/68 of losers there)
- **Sharp: n=71  W=22/L=49  WR=31.0%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L11.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is T4=T4a (49/68 of losers there)
- **Sharp: n=71  W=22/L=49  WR=31.0%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L12.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is H60=H60a (33/68 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L13.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is BBP=BBP0 (38/67 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L14.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=100  W=32/L=68  WR=32.0%
- Sharpen: sharpest is ZS=ZS1 (26/68 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=100  W=32/L=68  WR=32.0%
- Sharpen: sharpest is ZS=ZS1 (26/68 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=100  W=32/L=68  WR=32.0%
- Sharpen: sharpest is ZS=ZS1 (26/68 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=93  W=35/L=58  WR=37.6%
- Sharpen: sharpest is BBP=BBP0 (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L18.  `H20=H20e AND T4=T4a AND ZS=ZS2`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is T1=T1a (49/56 of losers there)
- **Sharp: n=71  W=22/L=49  WR=31.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L19.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is T1=T1a (49/56 of losers there)
- **Sharp: n=71  W=22/L=49  WR=31.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is BBP=BBP0 (38/55 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L21.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=82  W=27/L=55  WR=32.9%
- Sharpen: sharpest is session_bucket=ny_mid (16/55 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when session=ny_mid

### L22.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=82  W=27/L=55  WR=32.9%
- Sharpen: sharpest is session_bucket=ny_mid (16/55 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  ONLY when session=ny_mid

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is H20=H20e (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 strongly against

### L24.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is H20=H20e (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 strongly against

### L25.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=81  W=23/L=58  WR=28.4%
- Sharpen: sharpest is H20=H20e (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/41) | H20e(42/52) |
| H60 | H60e(41/36) | H60a(37/43) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | ZS1(24/29) |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
