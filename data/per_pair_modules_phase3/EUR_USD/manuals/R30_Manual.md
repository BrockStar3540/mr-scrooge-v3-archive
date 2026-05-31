# EUR_USD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,135**  (W=1,383 / L=752)  -  WR: **64.8%**

## Session distribution

- asia: n=851  W=540/L=311  WR=63.5%
- ny_close: n=800  W=539/L=261  WR=67.4%
- ny_open: n=159  W=97/L=62  WR=61.0%
- off_hours: n=98  W=65/L=33  WR=66.3%
- london: n=97  W=56/L=41  WR=57.7%
- asia_late: n=76  W=50/L=26  WR=65.8%
- ny_mid: n=32  W=21/L=11  WR=65.6%
- london_open: n=22  W=15/L=7  WR=68.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=129  W=113/L=16  WR=87.6%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 5/16 losers (31%)
- **Final: n=117  W=106/L=11  WR=90.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when strategy=charlie_pullback_continuation_v2

### W02.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=119  W=110/L=9  WR=92.4%
- Refine: exclude BBP=BBP1 drops 6/9 losers (67%)
- **Final: n=102  W=99/L=3  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when just touched lower band

### W03.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=117  W=106/L=11  WR=90.6%
- Refine: exclude BBP=BBP1 drops 6/11 losers (55%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when just touched lower band

### W04.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude T4=T4a drops 7/12 losers (58%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; session=asia  •  AVOID when 4h trend WITH trade

### W05.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W06.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W07.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H20=H20e drops 12/13 losers (92%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; session=ny_close  •  AVOID when HTF20 strongly against

### W08.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude T4=T4a drops 7/10 losers (70%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 4h trend WITH trade

### W09.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=83  W=72/L=11  WR=86.7%
- Refine: exclude T1=T1a drops 9/11 losers (82%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W10.  `H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 8/12 losers (67%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W11.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 8/12 losers (67%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W12.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_close

### W13.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 8/12 losers (67%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W14.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when just touched lower band

### W15.  `H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude H20=H20c drops 5/9 losers (56%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W16.  `T4=T4a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude ZS=ZS2 drops 5/11 losers (45%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -2 to -1 oversold

### W17.  `H20=H20a AND H60=H60d AND direction_exec=short`
- Raw: n=80  W=77/L=3  WR=96.2%
- Refine: exclude BBP=BBP2 drops 3/3 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when lower third

### W18.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude direction_exec=short drops 5/7 losers (71%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when short

### W19.  `T1=T1a AND T4=T4c AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude H20=H20e drops 8/9 losers (89%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W20.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W21.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T4=T4c drops 5/9 losers (56%)
- **Final: n=58  W=54/L=4  WR=93.1%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend AGAINST trade

### W22.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude T4=T4a drops 9/10 losers (90%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when 4h trend WITH trade

### W23.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude T4=T4a drops 6/7 losers (86%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_close  •  AVOID when 4h trend WITH trade

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude H60=H60a drops 5/8 losers (62%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W25.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude direction_exec=short drops 9/11 losers (82%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when short

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=133  W=43/L=90  WR=32.3%
- Sharpen: sharpest is ZS=ZS1 (36/90 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=133  W=43/L=90  WR=32.3%
- Sharpen: sharpest is ZS=ZS1 (36/90 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=133  W=43/L=90  WR=32.3%
- Sharpen: sharpest is ZS=ZS1 (36/90 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20e AND T4=T4c AND RSI=RSI2`
- Raw: n=106  W=38/L=68  WR=35.8%
- Sharpen: sharpest is session_bucket=asia (35/68 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L05.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is session_bucket=asia (35/64 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L06.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is session_bucket=asia (35/64 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L07.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is H20=H20e (35/64 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF20 strongly against

### L08.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=93  W=29/L=64  WR=31.2%
- Sharpen: sharpest is H20=H20e (35/64 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF20 strongly against

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=83  W=22/L=61  WR=26.5%
- Sharpen: sharpest is T4=T4c (35/61 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=83  W=22/L=61  WR=26.5%
- Sharpen: sharpest is T4=T4c (35/61 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20e AND T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (18/51 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L12.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (18/51 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L13.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is H20=H20b (9/42 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when HTF20 slightly aligned

### L14.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is RSI=RSI5 (19/45 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is T4=T4a (18/42 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend WITH trade

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is T4=T4a (18/42 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is T4=T4a (18/42 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND T4=T4c AND BBP=BBP1`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is T1=T1c (21/41 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20a AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is T1=T1c (21/41 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L20.  `H20=H20e AND T1=T1c AND BBP=BBP0`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is ZS=ZS0 (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L21.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=62  W=18/L=44  WR=29.0%
- Sharpen: sharpest is H20=H20a (22/44 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L22.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=62  W=18/L=44  WR=29.0%
- Sharpen: sharpest is H20=H20a (22/44 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H20=H20a (21/40 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when HTF20 aligned WITH trade

### L24.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H20=H20a (21/40 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L25.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_open (19/39 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(54/43) | H20e(42/53) |
| H60 | H60a(43/36) | H60e(36/42) |
| T1 | T1a(55/43) | T1c(45/57) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/47) | long(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
