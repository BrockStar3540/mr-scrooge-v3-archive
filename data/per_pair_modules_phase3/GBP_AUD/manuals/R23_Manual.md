# GBP_AUD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **7,433**  (W=4,044 / L=3,389)  -  WR: **54.4%**

## Session distribution

- ny_mid: n=1956  W=1035/L=921  WR=52.9%
- asia: n=1828  W=1009/L=819  WR=55.2%
- ny_close: n=1299  W=744/L=555  WR=57.3%
- ny_open: n=868  W=451/L=417  WR=52.0%
- london_open: n=511  W=298/L=213  WR=58.3%
- london: n=418  W=207/L=211  WR=49.5%
- off_hours: n=344  W=189/L=155  WR=54.9%
- asia_late: n=209  W=111/L=98  WR=53.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=142  W=128/L=14  WR=90.1%
- Refine: exclude ZS=ZS3 drops 10/14 losers (71%)
- **Final: n=108  W=104/L=4  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W02.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=125  W=115/L=10  WR=92.0%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W03.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=125  W=115/L=10  WR=92.0%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W04.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=108  W=104/L=4  WR=96.3%
- Refine: exclude session_bucket=london drops 3/4 losers (75%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london

### W05.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=98  W=95/L=3  WR=96.9%
- Refine: exclude session_bucket=london drops 2/3 losers (67%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london

### W06.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=98  W=95/L=3  WR=96.9%
- Refine: exclude session_bucket=london drops 2/3 losers (67%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london

### W07.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude H60=H60e drops 4/7 losers (57%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W08.  `H20=H20a AND H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP6 drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  AVOID when deep above upper band

### W09.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP6 drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when deep above upper band

### W10.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP6 drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when deep above upper band

### W11.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP6 drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when deep above upper band

### W12.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude BBP=BBP3 drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when middle of band

### W13.  `T4=T4c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude RSI=RSI6 drops 7/7 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when RSI 70-80 overbought

### W14.  `H20=H20e AND H60=H60a AND session_bucket=asia`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude T4=T4a drops 3/7 losers (43%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend WITH trade

### W15.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude T4=T4a drops 3/7 losers (43%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude T4=T4a drops 3/7 losers (43%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude T4=T4a drops 3/7 losers (43%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude T4=T4a drops 3/7 losers (43%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS1 drops 6/9 losers (67%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS1 drops 6/9 losers (67%)
- **Final: n=66  W=63/L=3  WR=95.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude ZS=ZS3 drops 4/4 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude ZS=ZS3 drops 4/4 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude ZS=ZS3 drops 4/4 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=319  W=114/L=205  WR=35.7%
- Sharpen: sharpest is BBP=BBP5 (63/205 of losers there)
- **Sharp: n=63  W=0/L=63  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L02.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=317  W=113/L=204  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=317  W=113/L=204  WR=35.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open

### L03.  `H20=H20a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=317  W=113/L=204  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=317  W=113/L=204  WR=35.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_open

### L04.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=317  W=113/L=204  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=317  W=113/L=204  WR=35.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open

### L05.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=315  W=107/L=208  WR=34.0%
- Sharpen: sharpest is BBP=BBP5 (56/208 of losers there)
- **Sharp: n=63  W=7/L=56  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L06.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=315  W=107/L=208  WR=34.0%
- Sharpen: sharpest is BBP=BBP5 (56/208 of losers there)
- **Sharp: n=63  W=7/L=56  WR=11.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L07.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=315  W=107/L=208  WR=34.0%
- Sharpen: sharpest is BBP=BBP5 (56/208 of losers there)
- **Sharp: n=63  W=7/L=56  WR=11.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L08.  `H20=H20a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=290  W=101/L=189  WR=34.8%
- Sharpen: sharpest is BBP=BBP5 (51/189 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when just touched upper band

### L09.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=290  W=101/L=189  WR=34.8%
- Sharpen: sharpest is BBP=BBP5 (51/189 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when just touched upper band

### L10.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=290  W=101/L=189  WR=34.8%
- Sharpen: sharpest is BBP=BBP5 (51/189 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when just touched upper band

### L11.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=288  W=95/L=193  WR=33.0%
- Sharpen: sharpest is BBP=BBP5 (56/193 of losers there)
- **Sharp: n=56  W=0/L=56  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L12.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=288  W=95/L=193  WR=33.0%
- Sharpen: sharpest is BBP=BBP5 (56/193 of losers there)
- **Sharp: n=56  W=0/L=56  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L13.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=267  W=85/L=182  WR=31.8%
- Sharpen: sharpest is T4=T4c (77/182 of losers there)
- **Sharp: n=96  W=19/L=77  WR=19.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=266  W=84/L=182  WR=31.6%
- Sharpen: sharpest is BBP=BBP5 (51/182 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L15.  `H20=H20a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=266  W=84/L=182  WR=31.6%
- Sharpen: sharpest is BBP=BBP5 (51/182 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L16.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=257  W=95/L=162  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=257  W=95/L=162  WR=37.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=ny_mid

### L17.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=257  W=95/L=162  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=257  W=95/L=162  WR=37.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_mid

### L18.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=257  W=95/L=162  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=257  W=95/L=162  WR=37.0%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_mid

### L19.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=253  W=98/L=155  WR=38.7%
- Sharpen: sharpest is RSI=RSI6 (72/155 of losers there)
- **Sharp: n=89  W=17/L=72  WR=19.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L20.  `T1=T1c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=253  W=98/L=155  WR=38.7%
- Sharpen: sharpest is RSI=RSI6 (72/155 of losers there)
- **Sharp: n=89  W=17/L=72  WR=19.1%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L21.  `ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=253  W=98/L=155  WR=38.7%
- Sharpen: sharpest is RSI=RSI6 (72/155 of losers there)
- **Sharp: n=89  W=17/L=72  WR=19.1%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L22.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=253  W=98/L=155  WR=38.7%
- Sharpen: sharpest is RSI=RSI6 (72/155 of losers there)
- **Sharp: n=89  W=17/L=72  WR=19.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L23.  `H60=H60a AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=253  W=98/L=155  WR=38.7%
- Sharpen: sharpest is RSI=RSI6 (72/155 of losers there)
- **Sharp: n=89  W=17/L=72  WR=19.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L24.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=253  W=98/L=155  WR=38.7%
- Sharpen: sharpest is RSI=RSI6 (72/155 of losers there)
- **Sharp: n=89  W=17/L=72  WR=19.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L25.  `T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=244  W=87/L=157  WR=35.7%
- Sharpen: sharpest is RSI=RSI6 (72/157 of losers there)
- **Sharp: n=89  W=17/L=72  WR=19.1%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
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
