# EUR_AUD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,708**  (W=2,316 / L=1,392)  -  WR: **62.5%**

## Session distribution

- asia: n=1488  W=918/L=570  WR=61.7%
- ny_close: n=785  W=501/L=284  WR=63.8%
- london_open: n=337  W=217/L=120  WR=64.4%
- london: n=277  W=175/L=102  WR=63.2%
- off_hours: n=260  W=151/L=109  WR=58.1%
- asia_late: n=190  W=126/L=64  WR=66.3%
- ny_mid: n=188  W=115/L=73  WR=61.2%
- ny_open: n=183  W=113/L=70  WR=61.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W02.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W03.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=72/L=8  WR=90.0%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W05.  `H60=H60d AND T1=T1c AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when middle of band

### W06.  `H60=H60d AND T4=T4c AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; session=asia  •  AVOID when middle of band

### W07.  `H60=H60d AND direction_exec=long AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 mildly against; session=asia  •  AVOID when middle of band

### W08.  `H60=H60d AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when middle of band

### W09.  `H60=H60d AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when middle of band

### W10.  `H60=H60d AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade; session=asia  •  AVOID when middle of band

### W11.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W12.  `H20=H20a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF60 strongly against

### W13.  `H20=H20a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude H60=H60e drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 strongly against

### W14.  `H60=H60d AND T1=T1c AND RSI=RSI2`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60d AND T4=T4c AND RSI=RSI2`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60d AND RSI=RSI2 AND direction_exec=long`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W17.  `H60=H60d AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W18.  `H60=H60d AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W19.  `H60=H60d AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W20.  `H60=H60d AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 mildly against; RSI 30-40 weak; session=asia  •  AVOID when middle of band

### W21.  `H60=H60d AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when middle of band

### W22.  `H60=H60d AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when middle of band

### W23.  `H60=H60d AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude BBP=BBP3 drops 4/6 losers (67%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 30-40 weak; session=asia  •  AVOID when middle of band

### W24.  `T1=T1a AND RSI=RSI2 AND ZS=ZS5`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W25.  `T4=T4a AND RSI=RSI2 AND ZS=ZS5`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore +2 to +3 deep overbought  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is RSI=RSI2 (39/76 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L02.  `H60=H60a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is RSI=RSI2 (39/76 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is RSI=RSI2 (39/76 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L04.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is RSI=RSI2 (41/73 of losers there)
- **Sharp: n=45  W=4/L=41  WR=8.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L05.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is RSI=RSI2 (40/73 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L06.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is RSI=RSI2 (37/70 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L07.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is RSI=RSI2 (37/70 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L08.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is RSI=RSI2 (37/70 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L09.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is RSI=RSI2 (34/67 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L10.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is RSI=RSI2 (34/67 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L11.  `H20=H20a AND H60=H60a AND BBP=BBP0`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is RSI=RSI2 (37/64 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is RSI=RSI2 (37/64 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L13.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is RSI=RSI2 (37/64 of losers there)
- **Sharp: n=39  W=2/L=37  WR=5.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L14.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP0`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is RSI=RSI2 (34/61 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L15.  `H20=H20a AND T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=88  W=29/L=59  WR=33.0%
- Sharpen: sharpest is RSI=RSI2 (35/59 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=88  W=29/L=59  WR=33.0%
- Sharpen: sharpest is RSI=RSI2 (35/59 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L17.  `H20=H20a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is RSI=RSI2 (32/56 of losers there)
- **Sharp: n=34  W=2/L=32  WR=5.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20a AND H60=H60a AND session_bucket=off_hours`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (17/49 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=off_hours`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (17/49 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=off_hours`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is ZS=ZS1 (17/49 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=off_hours  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (26/50 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L22.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=78  W=22/L=56  WR=28.2%
- Sharpen: sharpest is ZS=ZS1 (12/56 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `T1=T1a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is H60=H60a (42/49 of losers there)
- **Sharp: n=59  W=17/L=42  WR=28.8%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; session=asia  •  ONLY when HTF60 aligned WITH trade

### L24.  `T4=T4a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is H60=H60a (42/49 of losers there)
- **Sharp: n=59  W=17/L=42  WR=28.8%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; session=asia  •  ONLY when HTF60 aligned WITH trade

### L25.  `BBP=BBP0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is H60=H60a (42/49 of losers there)
- **Sharp: n=59  W=17/L=42  WR=28.8%**
- **Dir: SHORT**  •  deep below lower band; session=asia  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(54/46) | H20a(44/53) |
| H60 | — | — |
| T1 | T1c(54/47) | T1a(46/53) |
| T4 | T4c(54/47) | T4a(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/47) | short(46/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
