# AUD_NZD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,277**  (W=815 / L=462)  -  WR: **63.8%**

## Session distribution

- asia: n=417  W=275/L=142  WR=65.9%
- ny_close: n=248  W=159/L=89  WR=64.1%
- london_open: n=177  W=119/L=58  WR=67.2%
- off_hours: n=112  W=74/L=38  WR=66.1%
- ny_mid: n=104  W=53/L=51  WR=51.0%
- ny_open: n=90  W=61/L=29  WR=67.8%
- london: n=72  W=44/L=28  WR=61.1%
- asia_late: n=57  W=30/L=27  WR=52.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude ZS=ZS5 drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W02.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude ZS=ZS5 drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W03.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude ZS=ZS5 drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W04.  `T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when 1h trend AGAINST trade

### W05.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W06.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20b AND T4=T4c AND session_bucket=asia`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude ZS=ZS4 drops 2/7 losers (29%)
- **Final: n=50  W=45/L=5  WR=90.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20b AND H60=H60a AND session_bucket=asia`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS4 drops 2/7 losers (29%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W09.  `H20=H20b AND direction_exec=long AND session_bucket=asia`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS4 drops 2/7 losers (29%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; session=asia  •  AVOID when zscore +1 to +2 overbought

### W10.  `H20=H20b AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS4 drops 2/7 losers (29%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20b AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS4 drops 2/7 losers (29%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W12.  `H20=H20b AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude ZS=ZS4 drops 2/7 losers (29%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W13.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude H20=H20b drops 3/7 losers (43%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 slightly aligned

### W14.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=47  W=44/L=3  WR=93.6%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when lower third

### W15.  `H20=H20e AND T4=T4c AND RSI=RSI2`
- Raw: n=47  W=43/L=4  WR=91.5%
- Refine: exclude ZS=ZS4 drops 2/4 losers (50%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore +1 to +2 overbought

### W16.  `H20=H20b AND T1=T1c AND session_bucket=asia`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude strategy_id=charlie_compression_breakout drops 2/5 losers (40%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  AVOID when strategy=charlie_compression_breakout

### W17.  `H20=H20b AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude strategy_id=charlie_compression_breakout drops 2/5 losers (40%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when strategy=charlie_compression_breakout

### W18.  `H20=H20b AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude strategy_id=charlie_compression_breakout drops 2/5 losers (40%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when strategy=charlie_compression_breakout

### W19.  `H20=H20b AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude strategy_id=charlie_compression_breakout drops 2/5 losers (40%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  AVOID when strategy=charlie_compression_breakout

### W20.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=42  W=36/L=6  WR=85.7%
- Refine: exclude H20=H20c drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 neutral

### W21.  `T4=T4c AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=41  W=37/L=4  WR=90.2%
- Refine: exclude H20=H20b drops 3/4 losers (75%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when HTF20 slightly aligned

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W23.  `H60=H60e AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude T1=T1c drops 3/5 losers (60%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; session=asia  •  AVOID when 1h trend AGAINST trade

### W24.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W25.  `BBP=BBP0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude T1=T1c drops 3/5 losers (60%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: SHORT**  •  deep below lower band; session=asia  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (33/39 of losers there)
- **Sharp: n=47  W=14/L=33  WR=29.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 30-40 weak

### L02.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (33/39 of losers there)
- **Sharp: n=47  W=14/L=33  WR=29.8%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (33/39 of losers there)
- **Sharp: n=47  W=14/L=33  WR=29.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 30-40 weak

### L04.  `T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is T1=T1c (14/39 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when 1h trend AGAINST trade

### L05.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (7/33 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L06.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (7/33 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when deep below lower band

### L07.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (7/33 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L08.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is BBP=BBP0 (7/33 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L09.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is BBP=BBP0 (7/32 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L10.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is BBP=BBP0 (7/32 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L11.  `T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is BBP=BBP0 (7/32 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L12.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is BBP=BBP0 (7/32 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L13.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is BBP=BBP0 (7/32 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L14.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is BBP=BBP0 (7/32 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L15.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=47  W=14/L=33  WR=29.8%
- Sharpen: sharpest is T1=T1c (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when 1h trend AGAINST trade

### L16.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=47  W=14/L=33  WR=29.8%
- Sharpen: sharpest is T1=T1c (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when 1h trend AGAINST trade

### L17.  `H20=H20d AND T4=T4a AND session_bucket=asia`
- Raw: n=41  W=15/L=26  WR=36.6%
- Sharpen: sharpest is RSI=RSI3 (16/26 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L18.  `H20=H20d AND H60=H60e AND session_bucket=asia`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (16/25 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; session=asia  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20d AND direction_exec=short AND session_bucket=asia`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (16/25 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: SHORT**  •  HTF20 mildly against; session=asia  •  ONLY when RSI 40-50 lower neutral

### L20.  `H20=H20d AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (16/25 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20d AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (16/25 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; session=asia  •  ONLY when RSI 40-50 lower neutral

### L22.  `H20=H20d AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is RSI=RSI3 (16/25 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L23.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=39  W=14/L=25  WR=35.9%
- Sharpen: sharpest is ZS=ZS3 (9/25 of losers there)
- **Sharp: n=11  W=2/L=9  WR=18.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L24.  `H60=H60e AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is BBP=BBP0 (7/24 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_mid  •  ONLY when deep below lower band

### L25.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=38  W=14/L=24  WR=36.8%
- Sharpen: sharpest is BBP=BBP0 (7/24 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_mid  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(53/47) | H60e(47/53) |
| T1 | — | — |
| T4 | T4c(55/46) | T4a(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/47) | short(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
