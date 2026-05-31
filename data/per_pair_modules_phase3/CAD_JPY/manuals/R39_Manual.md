# CAD_JPY — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,702**  (W=1,073 / L=629)  -  WR: **63.0%**

## Session distribution

- asia: n=791  W=497/L=294  WR=62.8%
- ny_mid: n=393  W=246/L=147  WR=62.6%
- london_open: n=203  W=133/L=70  WR=65.5%
- ny_close: n=118  W=81/L=37  WR=68.6%
- london: n=82  W=46/L=36  WR=56.1%
- ny_open: n=67  W=38/L=29  WR=56.7%
- asia_late: n=31  W=21/L=10  WR=67.7%
- off_hours: n=17  W=11/L=6  WR=64.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude BBP=BBP2 drops 9/10 losers (90%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W02.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude BBP=BBP2 drops 9/10 losers (90%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W03.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude session_bucket=ny_mid drops 6/10 losers (60%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W04.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 aligned WITH trade

### W05.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H60=H60b drops 5/12 losers (42%)
- **Final: n=78  W=71/L=7  WR=91.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 slightly aligned

### W06.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60d drops 7/7 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 mildly against

### W07.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude BBP=BBP0 drops 11/11 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W08.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude BBP=BBP0 drops 11/11 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W09.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude BBP=BBP0 drops 11/11 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W10.  `H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=72  W=69/L=3  WR=95.8%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when upper third

### W11.  `H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=69/L=3  WR=95.8%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_close  •  AVOID when upper third

### W12.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=69/L=3  WR=95.8%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  AVOID when upper third

### W13.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=72  W=69/L=3  WR=95.8%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when upper third

### W14.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H60=H60b drops 5/9 losers (56%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 slightly aligned

### W15.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

### W16.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W17.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W19.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude H60=H60d drops 7/7 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; session=asia  •  AVOID when HTF60 mildly against

### W20.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude H60=H60b drops 7/7 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 slightly aligned

### W21.  `T1=T1a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude ZS=ZS1 drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W22.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W23.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W24.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

### W25.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is T4=T4c (14/52 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L02.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=84  W=30/L=54  WR=35.7%
- Sharpen: sharpest is ZS=ZS1 (26/54 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=84  W=30/L=54  WR=35.7%
- Sharpen: sharpest is ZS=ZS1 (26/54 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=30/L=54  WR=35.7%
- Sharpen: sharpest is ZS=ZS1 (26/54 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is ZS=ZS0 (12/52 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when zscore <-3 extreme

### L06.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is ZS=ZS0 (12/52 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore <-3 extreme

### L07.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is ZS=ZS0 (12/52 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia  •  ONLY when zscore <-3 extreme

### L08.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is ZS=ZS0 (12/52 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore <-3 extreme

### L09.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is ZS=ZS0 (12/52 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when zscore <-3 extreme

### L10.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is ZS=ZS0 (12/52 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore <-3 extreme

### L11.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=79  W=28/L=51  WR=35.4%
- Sharpen: sharpest is session_bucket=asia (28/51 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=asia

### L12.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is H60=H60a (32/49 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L13.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is session_bucket=asia (26/47 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L14.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is session_bucket=asia (26/47 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L15.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is H20=H20a (39/44 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L16.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H60=H60a (39/46 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 aligned WITH trade

### L17.  `BBP=BBP0 AND direction_exec=long AND session_bucket=asia`
- Raw: n=69  W=26/L=43  WR=37.7%
- Sharpen: sharpest is ZS=ZS0 (19/43 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  deep below lower band; session=asia  •  ONLY when zscore <-3 extreme

### L18.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (33/42 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=asia

### L19.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (33/42 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=asia

### L20.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (33/42 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: LONG**  •  deep below lower band; RSI 30-40 weak  •  ONLY when session=asia

### L21.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (33/42 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=asia

### L22.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (33/42 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=asia

### L23.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (33/42 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=asia

### L24.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=68  W=19/L=49  WR=27.9%
- Sharpen: sharpest is session_bucket=asia (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L25.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=68  W=19/L=49  WR=27.9%
- Sharpen: sharpest is session_bucket=asia (25/49 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60a(45/51) |
| T1 | T1a(56/44) | T1c(43/56) |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/47) | long(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
