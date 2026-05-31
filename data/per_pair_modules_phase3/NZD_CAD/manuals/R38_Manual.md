# NZD_CAD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,404**  (W=906 / L=498)  -  WR: **64.5%**

## Session distribution

- asia: n=525  W=346/L=179  WR=65.9%
- london_open: n=195  W=116/L=79  WR=59.5%
- ny_mid: n=181  W=114/L=67  WR=63.0%
- london: n=147  W=104/L=43  WR=70.7%
- ny_close: n=147  W=95/L=52  WR=64.6%
- ny_open: n=102  W=54/L=48  WR=52.9%
- off_hours: n=62  W=44/L=18  WR=71.0%
- asia_late: n=45  W=33/L=12  WR=73.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude BBP=BBP3 drops 6/11 losers (55%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W02.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude ZS=ZS3 drops 7/9 losers (78%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W03.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude BBP=BBP3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_close  •  AVOID when middle of band

### W04.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude BBP=BBP3 drops 6/7 losers (86%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when middle of band

### W05.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude BBP=BBP3 drops 6/8 losers (75%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when middle of band

### W06.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude BBP=BBP3 drops 6/7 losers (86%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when middle of band

### W07.  `H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude ZS=ZS4 drops 6/7 losers (86%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W08.  `H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=49  W=44/L=5  WR=89.8%
- Refine: exclude H20=H20a drops 4/5 losers (80%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 2/4 losers (50%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when just touched lower band

### W11.  `H60=H60a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when 4h trend WITH trade

### W12.  `H60=H60a AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend WITH trade

### W13.  `H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=42  W=38/L=4  WR=90.5%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20a AND H60=H60e AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=42  W=36/L=6  WR=85.7%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; middle of band; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND H60=H60c AND RSI=RSI3`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; RSI 40-50 lower neutral  •  AVOID when upper third

### W19.  `H60=H60c AND T4=T4c AND RSI=RSI3`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W20.  `H60=H60c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  HTF60 neutral; RSI 40-50 lower neutral  •  AVOID when upper third

### W21.  `H20=H20e AND H60=H60c AND T4=T4c AND RSI=RSI3`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W22.  `H20=H20e AND H60=H60c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 neutral; RSI 40-50 lower neutral  •  AVOID when upper third

### W23.  `H60=H60c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP4 drops 2/3 losers (67%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W24.  `T1=T1a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude BBP=BBP2 drops 3/5 losers (60%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; session=off_hours  •  AVOID when lower third

### W25.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=40  W=38/L=2  WR=95.0%
- Refine: exclude BBP=BBP1 drops 2/2 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is RSI=RSI2 (22/37 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=58  W=20/L=38  WR=34.5%
- Sharpen: sharpest is BBP=BBP0 (13/38 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when deep below lower band

### L03.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: sharpest is BBP=BBP0 (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when deep below lower band

### L04.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is BBP=BBP0 (13/35 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when deep below lower band

### L05.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is BBP=BBP0 (13/35 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when deep below lower band

### L06.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is ZS=ZS0 (10/33 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L07.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=48  W=14/L=34  WR=29.2%
- Sharpen: sharpest is BBP=BBP0 (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_close  •  ONLY when deep below lower band

### L08.  `T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=47  W=14/L=33  WR=29.8%
- Sharpen: sharpest is H60=H60e (18/33 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L09.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is H20=H20b (11/31 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 slightly aligned

### L10.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is H20=H20b (11/31 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 slightly aligned

### L11.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is H20=H20b (11/27 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 slightly aligned

### L12.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=44  W=12/L=32  WR=27.3%
- Sharpen: sharpest is BBP=BBP0 (13/32 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when deep below lower band

### L13.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=44  W=12/L=32  WR=27.3%
- Sharpen: sharpest is H60=H60e (18/32 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L14.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is ZS=ZS0 (10/27 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L15.  `H20=H20c AND H60=H60e AND session_bucket=asia`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is T1=T1a (11/26 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=asia  •  ONLY when 1h trend WITH trade

### L16.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=40  W=10/L=30  WR=25.0%
- Sharpen: sharpest is H60=H60e (18/30 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L17.  `H20=H20e AND H60=H60a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=40  W=14/L=26  WR=35.0%
- Sharpen: sharpest is ZS=ZS0 (6/26 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

### L18.  `H20=H20c AND T1=T1c AND ZS=ZS2`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (12/23 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L19.  `H20=H20c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (12/23 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L20.  `H20=H20a AND H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is T1=T1a (16/23 of losers there)
- **Sharp: n=23  W=7/L=16  WR=30.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third; session=asia  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20c AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (12/23 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L22.  `H20=H20c AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (12/23 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L23.  `H20=H20c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=38  W=15/L=23  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (12/23 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; lower third; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L24.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=37  W=13/L=24  WR=35.1%
- Sharpen: sharpest is T4=T4a (24/24 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20e AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=37  W=14/L=23  WR=37.8%
- Sharpen: sharpest is ZS=ZS0 (6/23 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when zscore <-3 extreme

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(45/40) | H60e(36/44) |
| T1 | T1a(54/47) | T1c(46/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/46) | long(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
