# AUD_JPY — R25 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,652**  (W=2,326 / L=1,326)  -  WR: **63.7%**

## Session distribution

- asia: n=1570  W=997/L=573  WR=63.5%
- london_open: n=588  W=390/L=198  WR=66.3%
- london: n=336  W=223/L=113  WR=66.4%
- ny_open: n=330  W=208/L=122  WR=63.0%
- ny_mid: n=291  W=169/L=122  WR=58.1%
- ny_close: n=246  W=153/L=93  WR=62.2%
- asia_late: n=161  W=98/L=63  WR=60.9%
- off_hours: n=130  W=88/L=42  WR=67.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when lower third

### W02.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when lower third

### W03.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when lower third

### W04.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when lower third

### W05.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude BBP=BBP2 drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when lower third

### W06.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude BBP=BBP2 drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_open  •  AVOID when lower third

### W07.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude BBP=BBP2 drops 5/7 losers (71%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when lower third

### W08.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W09.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W10.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W11.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W12.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W13.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W16.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W17.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W18.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W19.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W20.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W21.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W22.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W23.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP3 drops 3/8 losers (38%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_close  •  AVOID when middle of band

### W24.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP3 drops 3/8 losers (38%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  AVOID when middle of band

### W25.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude BBP=BBP3 drops 3/8 losers (38%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  AVOID when middle of band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is RSI=RSI3 (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L02.  `H20=H20a AND T1=T1c AND direction_exec=long`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is RSI=RSI3 (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L03.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is RSI=RSI3 (23/56 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L04.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (23/54 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L05.  `H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (23/54 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L06.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (23/54 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L07.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (23/54 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L08.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (23/54 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (23/54 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L10.  `H20=H20a AND T1=T1c AND RSI=RSI4`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP4 (16/53 of losers there)
- **Sharp: n=21  W=5/L=16  WR=23.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L11.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4a (21/51 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L12.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4a (21/51 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L13.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4a (21/51 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4a (21/51 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L15.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4a (21/51 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is T4=T4a (21/51 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=82  W=30/L=52  WR=36.6%
- Sharpen: sharpest is T4=T4a (23/52 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=79  W=23/L=56  WR=29.1%
- Sharpen: sharpest is H60=H60a (36/56 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L19.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is T4=T4a (21/50 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is T4=T4a (21/50 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L21.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is T4=T4a (21/50 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L22.  `H60=H60e AND T1=T1c AND session_bucket=asia_late`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20d (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia_late  •  ONLY when HTF20 mildly against

### L23.  `H60=H60e AND T4=T4c AND session_bucket=asia_late`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20d (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia_late  •  ONLY when HTF20 mildly against

### L24.  `H60=H60e AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20d (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=asia_late  •  ONLY when HTF20 mildly against

### L25.  `T1=T1c AND T4=T4c AND session_bucket=asia_late`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is H20=H20d (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia_late  •  ONLY when HTF20 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/47) | T1c(45/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
