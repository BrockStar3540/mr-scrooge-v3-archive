# GBP_AUD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,143**  (W=1,913 / L=1,230)  -  WR: **60.9%**

## Session distribution

- asia: n=687  W=403/L=284  WR=58.7%
- ny_mid: n=590  W=362/L=228  WR=61.4%
- london_open: n=511  W=325/L=186  WR=63.6%
- ny_open: n=480  W=294/L=186  WR=61.3%
- ny_close: n=318  W=200/L=118  WR=62.9%
- london: n=293  W=185/L=108  WR=63.1%
- asia_late: n=207  W=116/L=91  WR=56.0%
- off_hours: n=57  W=28/L=29  WR=49.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude RSI=RSI3 drops 14/15 losers (93%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W02.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude H20=H20b drops 5/12 losers (42%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W03.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude H20=H20b drops 5/12 losers (42%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W04.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude H20=H20b drops 5/12 losers (42%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: LONG**  •  upper third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60e AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude H20=H20b drops 5/12 losers (42%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W06.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W07.  `T4=T4c AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W08.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 5/10 losers (50%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 slightly aligned

### W09.  `T4=T4c AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 5/10 losers (50%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 slightly aligned

### W10.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 5/10 losers (50%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 slightly aligned

### W11.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 5/10 losers (50%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 5/10 losers (50%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 slightly aligned

### W13.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 5/10 losers (50%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 slightly aligned

### W14.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 5/10 losers (50%)
- **Final: n=87  W=82/L=5  WR=94.3%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 slightly aligned

### W15.  `H20=H20e AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W16.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W17.  `H20=H20b AND H60=H60a AND RSI=RSI3`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W18.  `H20=H20b AND T4=T4a AND RSI=RSI3`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W19.  `H20=H20b AND RSI=RSI3 AND direction_exec=short`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 40-50 lower neutral  •  AVOID when upper third

### W20.  `H20=H20b AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W21.  `H20=H20b AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W22.  `H20=H20b AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W23.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20b drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

### W24.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20b drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

### W25.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude H20=H20b drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=136  W=50/L=86  WR=36.8%
- Sharpen: sharpest is BBP=BBP4 (38/86 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when upper third

### L02.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=136  W=50/L=86  WR=36.8%
- Sharpen: sharpest is BBP=BBP4 (38/86 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when upper third

### L03.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=136  W=50/L=86  WR=36.8%
- Sharpen: sharpest is BBP=BBP4 (38/86 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when upper third

### L04.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=136  W=50/L=86  WR=36.8%
- Sharpen: sharpest is BBP=BBP4 (38/86 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when upper third

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=134  W=53/L=81  WR=39.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=134  W=53/L=81  WR=39.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia

### L07.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=134  W=53/L=81  WR=39.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia

### L08.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_short (13/68 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when strategy=TF2_pullback_EMA20_short

### L09.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=104  W=40/L=64  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; session=asia

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=104  W=40/L=64  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia

### L11.  `H20=H20e AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=104  W=40/L=64  WR=38.5%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=asia

### L12.  `H20=H20a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is BBP=BBP5 (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when just touched upper band

### L13.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is BBP=BBP5 (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  ONLY when just touched upper band

### L14.  `T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=102  W=31/L=71  WR=30.4%
- Sharpen: sharpest is H20=H20d (26/71 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=asia  •  ONLY when HTF20 mildly against

### L15.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=102  W=34/L=68  WR=33.3%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_short (13/68 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when strategy=TF2_pullback_EMA20_short

### L16.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=102  W=34/L=68  WR=33.3%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_short (13/68 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when strategy=TF2_pullback_EMA20_short

### L17.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=102  W=34/L=68  WR=33.3%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_short (13/68 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when strategy=TF2_pullback_EMA20_short

### L18.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=102  W=34/L=68  WR=33.3%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_short (13/68 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when strategy=TF2_pullback_EMA20_short

### L19.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=102  W=34/L=68  WR=33.3%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_short (13/68 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when strategy=TF2_pullback_EMA20_short

### L20.  `H60=H60a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (42/62 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia_late  •  ONLY when RSI 40-50 lower neutral

### L21.  `H60=H60e AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=96  W=35/L=61  WR=36.5%
- Sharpen: sharpest is session_bucket=london_open (14/61 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L22.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=96  W=35/L=61  WR=36.5%
- Sharpen: sharpest is session_bucket=london_open (14/61 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L23.  `H60=H60e AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=96  W=35/L=61  WR=36.5%
- Sharpen: sharpest is session_bucket=london_open (14/61 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L24.  `H60=H60a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is RSI=RSI3 (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late  •  ONLY when RSI 40-50 lower neutral

### L25.  `T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is RSI=RSI3 (42/58 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia_late  •  ONLY when RSI 40-50 lower neutral

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
