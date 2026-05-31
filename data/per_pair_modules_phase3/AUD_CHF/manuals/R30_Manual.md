# AUD_CHF — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,512**  (W=977 / L=535)  -  WR: **64.6%**

## Session distribution

- ny_mid: n=441  W=291/L=150  WR=66.0%
- asia: n=431  W=273/L=158  WR=63.3%
- london_open: n=166  W=108/L=58  WR=65.1%
- ny_open: n=150  W=102/L=48  WR=68.0%
- off_hours: n=106  W=66/L=40  WR=62.3%
- ny_close: n=88  W=55/L=33  WR=62.5%
- london: n=66  W=40/L=26  WR=60.6%
- asia_late: n=64  W=42/L=22  WR=65.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=97  W=87/L=10  WR=89.7%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W02.  `H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS3 drops 6/12 losers (50%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS3 drops 6/12 losers (50%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W04.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS3 drops 6/12 losers (50%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W05.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS3 drops 6/12 losers (50%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude BBP=BBP1 drops 8/11 losers (73%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when just touched lower band

### W07.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude BBP=BBP1 drops 8/11 losers (73%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when just touched lower band

### W08.  `H20=H20a AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude BBP=BBP1 drops 8/11 losers (73%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when just touched lower band

### W09.  `H20=H20a AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude BBP=BBP1 drops 8/11 losers (73%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when just touched lower band

### W10.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W12.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W13.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude ZS=ZS3 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP0 drops 6/9 losers (67%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W17.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP0 drops 6/9 losers (67%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W18.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP0 drops 6/9 losers (67%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W19.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP0 drops 6/9 losers (67%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W20.  `H20=H20a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=london

### W21.  `H60=H60a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=london

### W22.  `T1=T1c AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=london

### W23.  `BBP=BBP1 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: LONG**  •  just touched lower band; RSI 30-40 weak  •  AVOID when session=london

### W24.  `H20=H20a AND H60=H60a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=london

### W25.  `H20=H20a AND T1=T1c AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is H60=H60e (17/48 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L02.  `H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is H20=H20e (45/47 of losers there)
- **Sharp: n=64  W=19/L=45  WR=29.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=asia  •  ONLY when HTF20 strongly against

### L03.  `T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is H20=H20e (45/47 of losers there)
- **Sharp: n=64  W=19/L=45  WR=29.7%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=asia  •  ONLY when HTF20 strongly against

### L04.  `BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is H20=H20e (45/47 of losers there)
- **Sharp: n=64  W=19/L=45  WR=29.7%**
- **Dir: SHORT**  •  lower third; session=asia  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is H20=H20e (45/47 of losers there)
- **Sharp: n=64  W=19/L=45  WR=29.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; session=asia  •  ONLY when HTF20 strongly against

### L06.  `H60=H60e AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is H20=H20e (45/47 of losers there)
- **Sharp: n=64  W=19/L=45  WR=29.7%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; session=asia  •  ONLY when HTF20 strongly against

### L07.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=28/L=47  WR=37.3%
- Sharpen: sharpest is H20=H20e (45/47 of losers there)
- **Sharp: n=64  W=19/L=45  WR=29.7%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=asia  •  ONLY when HTF20 strongly against

### L08.  `H60=H60e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L09.  `T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L10.  `ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L13.  `H60=H60e AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L14.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L15.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L16.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (38/40 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L17.  `H20=H20e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=64  W=19/L=45  WR=29.7%
- Sharpen: sharpest is RSI=RSI1 (23/45 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L18.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=64  W=19/L=45  WR=29.7%
- Sharpen: sharpest is RSI=RSI1 (23/45 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L19.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=64  W=19/L=45  WR=29.7%
- Sharpen: sharpest is RSI=RSI1 (23/45 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L20.  `H20=H20e AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=64  W=19/L=45  WR=29.7%
- Sharpen: sharpest is RSI=RSI1 (23/45 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L21.  `T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H20=H20e (32/38 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L22.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H20=H20e (32/38 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L23.  `H20=H20e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=61  W=19/L=42  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (23/42 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L24.  `H20=H20e AND H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=61  W=19/L=42  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (23/42 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L25.  `H20=H20e AND T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=61  W=19/L=42  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (23/42 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(52/38) | H20e(38/51) |
| H60 | H60a(58/42) | H60e(42/57) |
| T1 | T1c(59/41) | T1a(41/59) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/42) | short(42/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
