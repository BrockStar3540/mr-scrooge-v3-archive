# CHF_JPY — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,952**  (W=1,775 / L=1,177)  -  WR: **60.1%**

## Session distribution

- asia: n=739  W=439/L=300  WR=59.4%
- london_open: n=609  W=367/L=242  WR=60.3%
- london: n=379  W=237/L=142  WR=62.5%
- ny_mid: n=336  W=214/L=122  WR=63.7%
- ny_close: n=333  W=209/L=124  WR=62.8%
- ny_open: n=234  W=134/L=100  WR=57.3%
- asia_late: n=208  W=122/L=86  WR=58.7%
- off_hours: n=114  W=53/L=61  WR=46.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=156  W=138/L=18  WR=88.5%
- Refine: exclude H20=H20e drops 17/18 losers (94%)
- **Final: n=120  W=119/L=1  WR=99.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W02.  `H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude T4=T4a drops 18/18 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when 4h trend WITH trade

### W03.  `T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude T4=T4a drops 18/18 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when 4h trend WITH trade

### W04.  `RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude T4=T4a drops 18/18 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=asia  •  AVOID when 4h trend WITH trade

### W05.  `H60=H60e AND T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude T4=T4a drops 18/18 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60e AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude T4=T4a drops 18/18 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when 4h trend WITH trade

### W07.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude T4=T4a drops 18/18 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when 4h trend WITH trade

### W08.  `T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W09.  `T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W10.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W11.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W12.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H20=H20e drops 17/17 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 strongly against

### W13.  `H60=H60e AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude H20=H20a drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude H20=H20a drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W15.  `ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude H20=H20a drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60e AND T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude H20=H20a drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60e AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude H20=H20a drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W18.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude H20=H20a drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 aligned WITH trade

### W19.  `T1=T1a AND T4=T4c AND BBP=BBP1`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=london drops 10/12 losers (83%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=london

### W20.  `T1=T1a AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude session_bucket=london drops 10/12 losers (83%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W21.  `H20=H20e AND T1=T1a AND BBP=BBP1`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band  •  AVOID when session=london

### W22.  `H20=H20e AND T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W23.  `H20=H20c AND T4=T4c AND session_bucket=asia`
- Raw: n=96  W=96/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=96  W=96/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; session=asia

### W24.  `H20=H20c AND H60=H60e AND session_bucket=asia`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=asia  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20c AND T1=T1a AND session_bucket=asia`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=83  W=83/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=asia  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND ZS=ZS1`
- Raw: n=165  W=58/L=107  WR=35.2%
- Sharpen: sharpest is RSI=RSI2 (62/107 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L02.  `H20=H20a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=161  W=58/L=103  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (58/103 of losers there)
- **Sharp: n=78  W=20/L=58  WR=25.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L03.  `H20=H20a AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=161  W=58/L=103  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (58/103 of losers there)
- **Sharp: n=78  W=20/L=58  WR=25.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L04.  `H20=H20a AND H60=H60a AND ZS=ZS1`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is RSI=RSI2 (45/90 of losers there)
- **Sharp: n=65  W=20/L=45  WR=30.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L05.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS1`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is RSI=RSI2 (45/90 of losers there)
- **Sharp: n=65  W=20/L=45  WR=30.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L06.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is RSI=RSI2 (45/90 of losers there)
- **Sharp: n=65  W=20/L=45  WR=30.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L07.  `H20=H20a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is RSI=RSI2 (38/82 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L08.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is H60=H60a (37/78 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L09.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=125  W=28/L=97  WR=22.4%
- Sharpen: sharpest is H20=H20c (45/97 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF20 neutral

### L10.  `H20=H20a AND T4=T4c AND ZS=ZS1`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is session_bucket=asia_late (26/78 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia_late

### L11.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is session_bucket=asia_late (26/78 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia_late

### L12.  `H20=H20a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is session_bucket=asia_late (26/78 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia_late

### L13.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=107  W=34/L=73  WR=31.8%
- Sharpen: sharpest is BBP=BBP1 (38/73 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L14.  `T4=T4c AND RSI=RSI2 AND session_bucket=london`
- Raw: n=107  W=36/L=71  WR=33.6%
- Sharpen: sharpest is T1=T1c (42/71 of losers there)
- **Sharp: n=55  W=13/L=42  WR=23.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20e AND T4=T4a AND RSI=RSI3`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: sharpest is H60=H60a (37/65 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: sharpest is H60=H60a (37/65 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L17.  `H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=101  W=28/L=73  WR=27.7%
- Sharpen: sharpest is H20=H20e (37/73 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=100  W=31/L=69  WR=31.0%
- Sharpen: sharpest is T4=T4c (63/69 of losers there)
- **Sharp: n=76  W=13/L=63  WR=17.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia_late  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4a (28/62 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when 4h trend WITH trade

### L20.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4a (28/62 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when 4h trend WITH trade

### L21.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4a (28/62 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when 4h trend WITH trade

### L22.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4a (28/62 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when 4h trend WITH trade

### L23.  `H60=H60a AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4a (28/62 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when 4h trend WITH trade

### L24.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is T4=T4a (28/62 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when 4h trend WITH trade

### L25.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is H20=H20a (38/59 of losers there)
- **Sharp: n=45  W=7/L=38  WR=15.6%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold; session=london_open  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(37/43) |
| H60 | H60e(57/38) | H60a(40/59) |
| T1 | T1a(57/42) | T1c(43/58) |
| T4 | T4a(52/46) | T4c(48/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/42) | long(44/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
