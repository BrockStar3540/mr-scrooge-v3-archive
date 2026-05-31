# NZD_CHF — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **285**  (W=187 / L=98)  -  WR: **65.6%**

## Session distribution

- asia: n=107  W=71/L=36  WR=66.4%
- ny_mid: n=99  W=61/L=38  WR=61.6%
- off_hours: n=43  W=28/L=15  WR=65.1%
- london_open: n=32  W=24/L=8  WR=75.0%
- london: n=3  W=3/L=0  WR=100.0%
- ny_open: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W02.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W03.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W04.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W05.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W06.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude H20=H20e drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W07.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=40  W=34/L=6  WR=85.0%
- Refine: exclude BBP=BBP0 drops 2/6 losers (33%)
- **Final: n=38  W=34/L=4  WR=89.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W08.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude BBP=BBP4 drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when upper third

### W09.  `H20=H20a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude BBP=BBP4 drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when upper third

### W10.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude BBP=BBP4 drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when upper third

### W11.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude BBP=BBP4 drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when upper third

### W12.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude BBP=BBP4 drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when upper third

### W13.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=37  W=32/L=5  WR=86.5%
- Refine: exclude BBP=BBP4 drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when upper third

### W14.  `H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold

### W15.  `H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold

### W16.  `H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third

### W18.  `T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold

### W19.  `T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought

### W20.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought

### W21.  `T1=T1a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third

### W22.  `T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold

### W23.  `T1=T1a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +1 to +2 overbought

### W24.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought

### W25.  `T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=34  W=34/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=34  W=11/L=23  WR=32.4%
- Sharpen: sharpest is RSI=RSI1 (7/23 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L02.  `H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is RSI=RSI1 (7/22 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L03.  `H60=H60a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is RSI=RSI1 (7/22 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L04.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is RSI=RSI1 (7/22 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L05.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is RSI=RSI1 (7/22 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L06.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is RSI=RSI1 (7/22 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 20-30 oversold

### L07.  `H60=H60a AND T1=T1a AND ZS=ZS2`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L08.  `H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L09.  `H60=H60a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L10.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L11.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L12.  `H60=H60a AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L13.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L14.  `H60=H60a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L15.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=31  W=11/L=20  WR=35.5%
- Sharpen: sharpest is RSI=RSI1 (7/20 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 20-30 oversold

### L16.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (8/18 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L17.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (8/18 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L18.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (8/18 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=30  W=12/L=18  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (8/18 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(57/27), H20d(17/6) | H20e(22/49), H20b(4/18) |
| H60 | H60e(50/39) | H60a(44/55) |
| T1 | T1c(59/43) | T1a(41/57) |
| T4 | T4c(59/42) | T4a(41/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | ZS1(21/15) | ZS3(9/14) |
| strategy_id | — | — |
| direction_exec | long(59/43) | short(41/57) |
| session_bucket | — | ny_mid(33/39) |

*Read: `bucket(winner%/loser%)`.*
