# USD_JPY — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,091**  (W=2,525 / L=1,566)  -  WR: **61.7%**

## Session distribution

- ny_mid: n=1271  W=779/L=492  WR=61.3%
- asia: n=993  W=626/L=367  WR=63.0%
- london_open: n=701  W=450/L=251  WR=64.2%
- ny_open: n=545  W=323/L=222  WR=59.3%
- ny_close: n=386  W=236/L=150  WR=61.1%
- london: n=109  W=58/L=51  WR=53.2%
- asia_late: n=57  W=36/L=21  WR=63.2%
- off_hours: n=29  W=17/L=12  WR=58.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=164  W=143/L=21  WR=87.2%
- Refine: exclude T4=T4a drops 20/21 losers (95%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend WITH trade

### W02.  `H20=H20e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=152  W=131/L=21  WR=86.2%
- Refine: exclude BBP=BBP5 drops 21/21 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W03.  `T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=130  W=121/L=9  WR=93.1%
- Refine: exclude ZS=ZS2 drops 6/9 losers (67%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W04.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=119  W=107/L=12  WR=89.9%
- Refine: exclude BBP=BBP5 drops 12/12 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W05.  `T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=117  W=109/L=8  WR=93.2%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W06.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=117  W=109/L=8  WR=93.2%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W07.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=97  W=97/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W08.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=106  W=101/L=5  WR=95.3%
- Refine: exclude session_bucket=london drops 5/5 losers (100%)
- **Final: n=97  W=97/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W09.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP4 drops 13/14 losers (93%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W10.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP4 drops 13/14 losers (93%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W11.  `T4=T4c AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP4 drops 13/14 losers (93%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W12.  `H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W13.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W14.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=93  W=85/L=8  WR=91.4%
- Refine: exclude ZS=ZS2 drops 6/8 losers (75%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W15.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=88  W=81/L=7  WR=92.0%
- Refine: exclude BBP=BBP0 drops 7/7 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W16.  `H20=H20e AND T1=T1c AND RSI=RSI3`
- Raw: n=86  W=83/L=3  WR=96.5%
- Refine: exclude session_bucket=london_open drops 3/3 losers (100%)
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W17.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=86  W=83/L=3  WR=96.5%
- Refine: exclude session_bucket=london_open drops 3/3 losers (100%)
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W18.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=86  W=83/L=3  WR=96.5%
- Refine: exclude session_bucket=london_open drops 3/3 losers (100%)
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W19.  `H60=H60a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W20.  `ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W21.  `H60=H60a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=84  W=78/L=6  WR=92.9%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W22.  `T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 strongly against

### W23.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=81  W=81/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought

### W24.  `T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=81  W=77/L=4  WR=95.1%
- Refine: exclude H20=H20c drops 4/4 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W25.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=80  W=79/L=1  WR=98.8%
- Refine: no further refinement
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4a AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is H60=H60e (71/87 of losers there)
- **Sharp: n=95  W=24/L=71  WR=25.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L02.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: sharpest is H60=H60e (71/87 of losers there)
- **Sharp: n=95  W=24/L=71  WR=25.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 strongly against

### L03.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=135  W=50/L=85  WR=37.0%
- Sharpen: sharpest is T4=T4a (48/85 of losers there)
- **Sharp: n=50  W=2/L=48  WR=4.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (78/81 of losers there)
- **Sharp: n=104  W=26/L=78  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (78/81 of losers there)
- **Sharp: n=104  W=26/L=78  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20a AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (78/81 of losers there)
- **Sharp: n=104  W=26/L=78  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is H60=H60e (78/84 of losers there)
- **Sharp: n=104  W=26/L=78  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L08.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is H60=H60e (78/84 of losers there)
- **Sharp: n=104  W=26/L=78  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L09.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is H60=H60e (78/84 of losers there)
- **Sharp: n=104  W=26/L=78  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L10.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=123  W=46/L=77  WR=37.4%
- Sharpen: sharpest is H60=H60e (71/77 of losers there)
- **Sharp: n=95  W=24/L=71  WR=25.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L11.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=123  W=46/L=77  WR=37.4%
- Sharpen: sharpest is H60=H60e (71/77 of losers there)
- **Sharp: n=95  W=24/L=71  WR=25.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L12.  `T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=119  W=40/L=79  WR=33.6%
- Sharpen: sharpest is direction_exec=long (46/79 of losers there)
- **Sharp: n=46  W=0/L=46  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when long

### L13.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (29/70 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L14.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is session_bucket=asia (29/70 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L15.  `H20=H20a AND H60=H60e AND RSI=RSI5`
- Raw: n=104  W=26/L=78  WR=25.0%
- Sharpen: sharpest is BBP=BBP6 (30/78 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when deep above upper band

### L16.  `H20=H20a AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=104  W=26/L=78  WR=25.0%
- Sharpen: sharpest is BBP=BBP6 (30/78 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L17.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=104  W=26/L=78  WR=25.0%
- Sharpen: sharpest is BBP=BBP6 (30/78 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when deep above upper band

### L18.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=102  W=22/L=80  WR=21.6%
- Sharpen: sharpest is H20=H20a (59/80 of losers there)
- **Sharp: n=63  W=4/L=59  WR=6.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L19.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=95  W=24/L=71  WR=25.3%
- Sharpen: sharpest is BBP=BBP6 (30/71 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when deep above upper band

### L20.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=95  W=24/L=71  WR=25.3%
- Sharpen: sharpest is BBP=BBP6 (30/71 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when deep above upper band

### L21.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=95  W=24/L=71  WR=25.3%
- Sharpen: sharpest is BBP=BBP6 (30/71 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L22.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=95  W=24/L=71  WR=25.3%
- Sharpen: sharpest is BBP=BBP6 (30/71 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when deep above upper band

### L23.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is RSI=RSI3 (48/59 of losers there)
- **Sharp: n=64  W=16/L=48  WR=25.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L24.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=91  W=25/L=66  WR=27.5%
- Sharpen: sharpest is H60=H60e (34/66 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L25.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is ZS=ZS5 (29/55 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(36/30) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
