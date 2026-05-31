# CHF_JPY — R30 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,197**  (W=2,605 / L=1,592)  -  WR: **62.1%**

## Session distribution

- asia: n=2030  W=1296/L=734  WR=63.8%
- ny_close: n=885  W=536/L=349  WR=60.6%
- off_hours: n=318  W=168/L=150  WR=52.8%
- asia_late: n=281  W=182/L=99  WR=64.8%
- ny_open: n=190  W=115/L=75  WR=60.5%
- london: n=165  W=108/L=57  WR=65.5%
- london_open: n=165  W=93/L=72  WR=56.4%
- ny_mid: n=163  W=107/L=56  WR=65.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60b AND T4=T4c AND direction_exec=long`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude ZS=ZS4 drops 10/19 losers (53%)
- **Final: n=106  W=97/L=9  WR=91.5%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when zscore +1 to +2 overbought

### W02.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI3 drops 9/17 losers (53%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W03.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude BBP=BBP4 drops 5/8 losers (62%)
- **Final: n=78  W=75/L=3  WR=96.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when upper third

### W04.  `H20=H20a AND H60=H60b AND session_bucket=asia`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; session=asia  •  AVOID when upper third

### W05.  `H60=H60b AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 40-50 lower neutral; session=asia  •  AVOID when upper third

### W06.  `H20=H20a AND H60=H60b AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; RSI 40-50 lower neutral; session=asia  •  AVOID when upper third

### W07.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude BBP=BBP4 drops 5/8 losers (62%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W08.  `H60=H60b AND T4=T4c AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W09.  `H60=H60b AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF60 slightly aligned; session=asia  •  AVOID when upper third

### W10.  `H20=H20a AND H60=H60b AND T4=T4c AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W11.  `H20=H20a AND H60=H60b AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; session=asia  •  AVOID when upper third

### W12.  `H60=H60b AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when upper third

### W13.  `H60=H60b AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W14.  `H60=H60b AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude BBP=BBP4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 40-50 lower neutral; session=asia  •  AVOID when upper third

### W15.  `H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude T1=T1a drops 6/9 losers (67%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_mid  •  AVOID when 1h trend WITH trade

### W16.  `H20=H20e AND T1=T1a AND BBP=BBP5`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched upper band  •  AVOID when HTF60 strongly against

### W17.  `H20=H20e AND T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W18.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W19.  `T1=T1a AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=82  W=77/L=5  WR=93.9%
- Refine: exclude H60=H60c drops 3/5 losers (60%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore >+3 extreme  •  AVOID when HTF60 neutral

### W20.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 aligned WITH trade

### W21.  `H20=H20a AND H60=H60b AND T1=T1a`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude ZS=ZS4 drops 5/10 losers (50%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W22.  `T1=T1a AND RSI=RSI4 AND ZS=ZS6`
- Raw: n=77  W=73/L=4  WR=94.8%
- Refine: exclude H60=H60c drops 3/4 losers (75%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore >+3 extreme  •  AVOID when HTF60 neutral

### W23.  `T1=T1a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS6`
- Raw: n=77  W=73/L=4  WR=94.8%
- Refine: exclude H60=H60c drops 3/4 losers (75%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore >+3 extreme  •  AVOID when HTF60 neutral

### W24.  `H60=H60b AND T1=T1a AND RSI=RSI3`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude ZS=ZS4 drops 5/10 losers (50%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

### W25.  `H20=H20a AND H60=H60b AND T1=T1a AND RSI=RSI3`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude ZS=ZS4 drops 5/10 losers (50%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore +1 to +2 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=164  W=63/L=101  WR=38.4%
- Sharpen: sharpest is session_bucket=asia (54/101 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L02.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=163  W=63/L=100  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (54/100 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L03.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is direction_exec=short (54/77 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when short

### L04.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=121  W=47/L=74  WR=38.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia

### L05.  `H20=H20c AND T4=T4c AND session_bucket=asia`
- Raw: n=96  W=32/L=64  WR=33.3%
- Sharpen: sharpest is T1=T1a (16/64 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend WITH trade

### L06.  `H20=H20a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=93  W=33/L=60  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_mid (9/60 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third  •  ONLY when session=ny_mid

### L07.  `H20=H20e AND BBP=BBP1 AND direction_exec=short`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is T1=T1c (17/57 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched lower band  •  ONLY when 1h trend AGAINST trade

### L08.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is T1=T1c (17/57 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L09.  `H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is ZS=ZS1 (11/56 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=88  W=21/L=67  WR=23.9%
- Sharpen: sharpest is RSI=RSI4 (54/67 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `H60=H60d AND T4=T4a AND RSI=RSI3`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H60=H60d AND RSI=RSI3 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `H60=H60d AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H20=H20a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=87  W=31/L=56  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=87  W=31/L=56  WR=35.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought

### L15.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=87  W=31/L=56  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=87  W=31/L=56  WR=35.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought

### L16.  `H20=H20e AND H60=H60d AND RSI=RSI3`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (11/53 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20e AND H60=H60d AND direction_exec=short`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (11/53 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H20=H20e AND H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (11/53 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T4=T4a AND RSI=RSI3 AND session_bucket=off_hours`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is BBP=BBP0 (12/56 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=off_hours  •  ONLY when deep below lower band

### L20.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=85  W=24/L=61  WR=28.2%
- Sharpen: sharpest is T4=T4a (25/61 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L21.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=85  W=24/L=61  WR=28.2%
- Sharpen: sharpest is T4=T4a (25/61 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L22.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=85  W=24/L=61  WR=28.2%
- Sharpen: sharpest is T4=T4a (25/61 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L23.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=85  W=24/L=61  WR=28.2%
- Sharpen: sharpest is T4=T4a (25/61 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L24.  `H20=H20a AND T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=85  W=28/L=57  WR=32.9%
- Sharpen: sharpest is ZS=ZS1 (42/57 of losers there)
- **Sharp: n=52  W=10/L=42  WR=19.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `T1=T1a AND T4=T4c AND session_bucket=off_hours`
- Raw: n=85  W=33/L=52  WR=38.8%
- Sharpen: sharpest is RSI=RSI4 (21/52 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=off_hours  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(56/44) | T4c(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
