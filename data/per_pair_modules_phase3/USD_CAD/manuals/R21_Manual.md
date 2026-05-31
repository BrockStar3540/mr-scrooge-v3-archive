# USD_CAD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,623**  (W=1,047 / L=576)  -  WR: **64.5%**

## Session distribution

- ny_mid: n=376  W=247/L=129  WR=65.7%
- london_open: n=278  W=178/L=100  WR=64.0%
- asia: n=258  W=168/L=90  WR=65.1%
- ny_close: n=257  W=166/L=91  WR=64.6%
- ny_open: n=253  W=158/L=95  WR=62.5%
- london: n=152  W=99/L=53  WR=65.1%
- off_hours: n=46  W=29/L=17  WR=63.0%
- asia_late: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=181  W=159/L=22  WR=87.8%
- Refine: exclude T1=T1a drops 14/22 losers (64%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: LONG**  •  4h trend WITH trade; lower third  •  AVOID when 1h trend WITH trade

### W02.  `T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=173  W=157/L=16  WR=90.8%
- Refine: exclude session_bucket=ny_mid drops 11/16 losers (69%)
- **Final: n=106  W=101/L=5  WR=95.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=172  W=152/L=20  WR=88.4%
- Refine: exclude H60=H60a drops 19/20 losers (95%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W04.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=167  W=146/L=21  WR=87.4%
- Refine: exclude T1=T1a drops 14/21 losers (67%)
- **Final: n=123  W=116/L=7  WR=94.3%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W05.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=167  W=146/L=21  WR=87.4%
- Refine: exclude T1=T1a drops 14/21 losers (67%)
- **Final: n=123  W=116/L=7  WR=94.3%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W06.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=155  W=139/L=16  WR=89.7%
- Refine: exclude ZS=ZS1 drops 10/16 losers (62%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=155  W=139/L=16  WR=89.7%
- Refine: exclude ZS=ZS1 drops 10/16 losers (62%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W08.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=154  W=144/L=10  WR=93.5%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=80  W=78/L=2  WR=97.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 strongly against

### W09.  `H20=H20a AND T4=T4a AND BBP=BBP2`
- Raw: n=145  W=127/L=18  WR=87.6%
- Refine: exclude session_bucket=asia drops 9/18 losers (50%)
- **Final: n=119  W=110/L=9  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=asia

### W10.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=140  W=132/L=8  WR=94.3%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W11.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=140  W=132/L=8  WR=94.3%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W12.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=135  W=127/L=8  WR=94.1%
- Refine: exclude H20=H20e drops 8/8 losers (100%)
- **Final: n=75  W=75/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND T4=T4a AND ZS=ZS2`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude session_bucket=asia drops 9/17 losers (53%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W14.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude session_bucket=asia drops 9/17 losers (53%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=asia

### W15.  `H20=H20a AND T4=T4a AND RSI=RSI2`
- Raw: n=126  W=117/L=9  WR=92.9%
- Refine: exclude session_bucket=ny_mid drops 8/9 losers (89%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W16.  `H60=H60b AND T1=T1c AND T4=T4a`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude H20=H20b drops 9/11 losers (82%)
- **Final: n=94  W=92/L=2  WR=97.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF20 slightly aligned

### W17.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=123  W=116/L=7  WR=94.3%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=69  W=69/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W18.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude ZS=ZS1 drops 10/15 losers (67%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude ZS=ZS1 drops 10/15 losers (67%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude ZS=ZS1 drops 10/15 losers (67%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=119  W=108/L=11  WR=90.8%
- Refine: exclude RSI=RSI3 drops 10/11 losers (91%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W22.  `H20=H20a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude H60=H60a drops 15/16 losers (94%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W23.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=117  W=109/L=8  WR=93.2%
- Refine: exclude session_bucket=ny_open drops 3/8 losers (38%)
- **Final: n=102  W=97/L=5  WR=95.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when session=ny_open

### W24.  `H20=H20e AND H60=H60b AND direction_exec=long`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=asia drops 13/15 losers (87%)
- **Final: n=86  W=84/L=2  WR=97.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned  •  AVOID when session=asia

### W25.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=110  W=101/L=9  WR=91.8%
- Refine: exclude session_bucket=ny_mid drops 8/9 losers (89%)
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=211  W=78/L=133  WR=37.0%
- Sharpen: sharpest is T1=T1a (57/133 of losers there)
- **Sharp: n=66  W=9/L=57  WR=13.6%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L02.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=168  W=67/L=101  WR=39.9%
- Sharpen: sharpest is T1=T1c (92/101 of losers there)
- **Sharp: n=124  W=32/L=92  WR=25.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L03.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=152  W=54/L=98  WR=35.5%
- Sharpen: sharpest is direction_exec=long (92/98 of losers there)
- **Sharp: n=124  W=32/L=92  WR=25.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when long

### L04.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=124  W=32/L=92  WR=25.8%
- Sharpen: sharpest is BBP=BBP1 (19/92 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when just touched lower band

### L05.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=123  W=32/L=91  WR=26.0%
- Sharpen: sharpest is BBP=BBP2 (37/91 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L06.  `H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is RSI=RSI2 (27/75 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L07.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=114  W=32/L=82  WR=28.1%
- Sharpen: sharpest is BBP=BBP2 (37/82 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=114  W=32/L=82  WR=28.1%
- Sharpen: sharpest is BBP=BBP2 (37/82 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L09.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is RSI=RSI2 (27/66 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L10.  `H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is H20=H20e (27/65 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is H20=H20e (27/65 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L12.  `T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=96  W=25/L=71  WR=26.0%
- Sharpen: sharpest is T1=T1a (57/71 of losers there)
- **Sharp: n=68  W=11/L=57  WR=16.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third  •  ONLY when 1h trend WITH trade

### L13.  `H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=96  W=32/L=64  WR=33.3%
- Sharpen: sharpest is BBP=BBP2 (27/64 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L14.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=96  W=32/L=64  WR=33.3%
- Sharpen: sharpest is BBP=BBP2 (27/64 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=96  W=32/L=64  WR=33.3%
- Sharpen: sharpest is BBP=BBP2 (27/64 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L16.  `H20=H20e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is T4=T4c (52/58 of losers there)
- **Sharp: n=72  W=20/L=52  WR=27.8%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L17.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=90  W=32/L=58  WR=35.6%
- Sharpen: sharpest is BBP=BBP1 (15/58 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when just touched lower band

### L18.  `H60=H60e AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is RSI=RSI2 (23/56 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L19.  `T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=86  W=22/L=64  WR=25.6%
- Sharpen: sharpest is T1=T1a (51/64 of losers there)
- **Sharp: n=59  W=8/L=51  WR=13.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L20.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=86  W=22/L=64  WR=25.6%
- Sharpen: sharpest is T1=T1a (51/64 of losers there)
- **Sharp: n=59  W=8/L=51  WR=13.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L21.  `H60=H60d AND T1=T1a AND T4=T4c`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is BBP=BBP2 (18/54 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when lower third

### L22.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=84  W=21/L=63  WR=25.0%
- Sharpen: sharpest is RSI=RSI2 (27/63 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20e AND T4=T4c AND ZS=ZS1`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is direction_exec=long (52/52 of losers there)
- **Sharp: n=72  W=20/L=52  WR=27.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when long

### L24.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is RSI=RSI2 (23/50 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20e AND T4=T4c AND RSI=RSI2`
- Raw: n=80  W=17/L=63  WR=21.2%
- Sharpen: sharpest is session_bucket=ny_open (22/63 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(41/33) | — |
| H60 | H60b(19/10) | H60e(30/38), H60d(10/16) |
| T1 | — | — |
| T4 | T4a(62/38) | T4c(38/62) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
