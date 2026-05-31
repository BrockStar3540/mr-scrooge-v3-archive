# GBP_USD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,482**  (W=1,567 / L=915)  -  WR: **63.1%**

## Session distribution

- asia: n=783  W=505/L=278  WR=64.5%
- ny_close: n=595  W=386/L=209  WR=64.9%
- london_open: n=380  W=231/L=149  WR=60.8%
- london: n=286  W=177/L=109  WR=61.9%
- ny_open: n=141  W=87/L=54  WR=61.7%
- ny_mid: n=137  W=83/L=54  WR=60.6%
- asia_late: n=127  W=77/L=50  WR=60.6%
- off_hours: n=33  W=21/L=12  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=286  W=247/L=39  WR=86.4%
- Refine: exclude ZS=ZS3 drops 15/39 losers (38%)
- **Final: n=239  W=215/L=24  WR=90.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W02.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=230  W=200/L=30  WR=87.0%
- Refine: exclude H60=H60e drops 16/30 losers (53%)
- **Final: n=170  W=156/L=14  WR=91.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 strongly against

### W03.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=227  W=203/L=24  WR=89.4%
- Refine: exclude ZS=ZS3 drops 12/24 losers (50%)
- **Final: n=196  W=184/L=12  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W04.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=216  W=185/L=31  WR=85.6%
- Refine: exclude H20=H20e drops 16/31 losers (52%)
- **Final: n=162  W=147/L=15  WR=90.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 strongly against

### W05.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=215  W=185/L=30  WR=86.0%
- Refine: exclude ZS=ZS3 drops 15/30 losers (50%)
- **Final: n=170  W=155/L=15  WR=91.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=201  W=173/L=28  WR=86.1%
- Refine: exclude RSI=RSI4 drops 10/28 losers (36%)
- **Final: n=191  W=173/L=18  WR=90.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W07.  `H20=H20a AND H60=H60a AND direction_exec=short`
- Raw: n=195  W=176/L=19  WR=90.3%
- Refine: exclude ZS=ZS3 drops 12/19 losers (63%)
- **Final: n=165  W=158/L=7  WR=95.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=179  W=163/L=16  WR=91.1%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=139  W=131/L=8  WR=94.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=177  W=163/L=14  WR=92.1%
- Refine: exclude ZS=ZS3 drops 11/14 losers (79%)
- **Final: n=150  W=147/L=3  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=174  W=157/L=17  WR=90.2%
- Refine: exclude ZS=ZS3 drops 7/17 losers (41%)
- **Final: n=137  W=127/L=10  WR=92.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=170  W=146/L=24  WR=85.9%
- Refine: exclude ZS=ZS3 drops 12/24 losers (50%)
- **Final: n=140  W=128/L=12  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=163  W=140/L=23  WR=85.9%
- Refine: exclude H20=H20e drops 20/23 losers (87%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=157  W=144/L=13  WR=91.7%
- Refine: exclude direction_exec=long drops 8/13 losers (62%)
- **Final: n=129  W=124/L=5  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when long

### W14.  `H60=H60a AND T1=T1a AND ZS=ZS2`
- Raw: n=153  W=133/L=20  WR=86.9%
- Refine: exclude H20=H20e drops 18/20 losers (90%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W15.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=153  W=133/L=20  WR=86.9%
- Refine: exclude H20=H20e drops 18/20 losers (90%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W16.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=151  W=132/L=19  WR=87.4%
- Refine: exclude ZS=ZS3 drops 12/19 losers (63%)
- **Final: n=121  W=114/L=7  WR=94.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=148  W=134/L=14  WR=90.5%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=123  W=116/L=7  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W18.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=148  W=129/L=19  WR=87.2%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 6/19 losers (32%)
- **Final: n=135  W=122/L=13  WR=90.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=charlie_pullback_continuation_v2

### W19.  `H20=H20a AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=147  W=137/L=10  WR=93.2%
- Refine: exclude ZS=ZS3 drops 6/10 losers (60%)
- **Final: n=130  W=126/L=4  WR=96.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W20.  `H60=H60a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=144  W=123/L=21  WR=85.4%
- Refine: exclude H20=H20e drops 20/21 losers (95%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W21.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=144  W=123/L=21  WR=85.4%
- Refine: exclude H20=H20e drops 20/21 losers (95%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W22.  `H20=H20a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=140  W=121/L=19  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 10/19 losers (53%)
- **Final: n=105  W=96/L=9  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W23.  `H20=H20a AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=140  W=121/L=19  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 10/19 losers (53%)
- **Final: n=105  W=96/L=9  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W24.  `H60=H60a AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude H20=H20e drops 18/19 losers (95%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W25.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=132  W=120/L=12  WR=90.9%
- Refine: exclude ZS=ZS3 drops 7/12 losers (58%)
- **Final: n=107  W=102/L=5  WR=95.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=174  W=51/L=123  WR=29.3%
- Sharpen: sharpest is direction_exec=long (96/123 of losers there)
- **Sharp: n=124  W=28/L=96  WR=22.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when long

### L02.  `H20=H20e AND H60=H60e AND direction_exec=long`
- Raw: n=147  W=44/L=103  WR=29.9%
- Sharpen: sharpest is T1=T1c (96/103 of losers there)
- **Sharp: n=124  W=28/L=96  WR=22.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when 1h trend AGAINST trade

### L03.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=146  W=55/L=91  WR=37.7%
- Sharpen: sharpest is H60=H60e (41/91 of losers there)
- **Sharp: n=52  W=11/L=41  WR=21.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 strongly against

### L04.  `H20=H20e AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=142  W=53/L=89  WR=37.3%
- Sharpen: sharpest is H60=H60e (36/89 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 strongly against

### L05.  `H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=137  W=50/L=87  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_close (49/87 of losers there)
- **Sharp: n=59  W=10/L=49  WR=16.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when session=ny_close

### L06.  `H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=131  W=46/L=85  WR=35.1%
- Sharpen: sharpest is session_bucket=ny_close (39/85 of losers there)
- **Sharp: n=41  W=2/L=39  WR=4.9%**
- **Dir: LONG**  •  HTF60 strongly against; lower third  •  ONLY when session=ny_close

### L07.  `H60=H60e AND T1=T1c AND ZS=ZS2`
- Raw: n=131  W=48/L=83  WR=36.6%
- Sharpen: sharpest is session_bucket=ny_close (47/83 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L08.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=131  W=48/L=83  WR=36.6%
- Sharpen: sharpest is direction_exec=long (66/83 of losers there)
- **Sharp: n=91  W=25/L=66  WR=27.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when long

### L09.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=131  W=48/L=83  WR=36.6%
- Sharpen: sharpest is session_bucket=ny_close (47/83 of losers there)
- **Sharp: n=57  W=10/L=47  WR=17.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L10.  `H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=130  W=50/L=80  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_close (44/80 of losers there)
- **Sharp: n=60  W=16/L=44  WR=26.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_close

### L11.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=130  W=52/L=78  WR=40.0%
- Sharpen: sharpest is H60=H60e (51/78 of losers there)
- **Sharp: n=64  W=13/L=51  WR=20.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 strongly against

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=124  W=28/L=96  WR=22.6%
- Sharpen: sharpest is T4=T4c (74/96 of losers there)
- **Sharp: n=88  W=14/L=74  WR=15.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L13.  `H60=H60e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=124  W=44/L=80  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_close (38/80 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L14.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=124  W=44/L=80  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_close (38/80 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L15.  `H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=123  W=48/L=75  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (42/75 of losers there)
- **Sharp: n=58  W=16/L=42  WR=27.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L16.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=123  W=48/L=75  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_close (42/75 of losers there)
- **Sharp: n=58  W=16/L=42  WR=27.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L17.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=119  W=42/L=77  WR=35.3%
- Sharpen: sharpest is session_bucket=ny_close (39/77 of losers there)
- **Sharp: n=41  W=2/L=39  WR=4.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when session=ny_close

### L18.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=116  W=32/L=84  WR=27.6%
- Sharpen: sharpest is direction_exec=long (74/84 of losers there)
- **Sharp: n=88  W=14/L=74  WR=15.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when long

### L19.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=114  W=40/L=74  WR=35.1%
- Sharpen: sharpest is session_bucket=ny_close (38/74 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_close

### L20.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=113  W=40/L=73  WR=35.4%
- Sharpen: sharpest is T1=T1c (66/73 of losers there)
- **Sharp: n=91  W=25/L=66  WR=27.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L21.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=111  W=30/L=81  WR=27.0%
- Sharpen: sharpest is T1=T1c (74/81 of losers there)
- **Sharp: n=88  W=14/L=74  WR=15.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=109  W=41/L=68  WR=37.6%
- Sharpen: sharpest is H60=H60e (36/68 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: LONG**  •  HTF20 strongly against; lower third  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is H60=H60e (40/67 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 strongly against

### L24.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (44/68 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_close

### L25.  `H20=H20e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is H60=H60e (35/65 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/40) | H20e(41/50) |
| H60 | H60a(37/27) | H60e(28/38) |
| T1 | T1a(58/40) | T1c(42/60) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/45) | long(48/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
