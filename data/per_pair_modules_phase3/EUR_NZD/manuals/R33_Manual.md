# EUR_NZD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,034**  (W=2,520 / L=1,514)  -  WR: **62.5%**

## Session distribution

- asia: n=1356  W=835/L=521  WR=61.6%
- ny_close: n=1233  W=776/L=457  WR=62.9%
- off_hours: n=488  W=304/L=184  WR=62.3%
- london: n=333  W=213/L=120  WR=64.0%
- ny_open: n=216  W=137/L=79  WR=63.4%
- london_open: n=196  W=115/L=81  WR=58.7%
- asia_late: n=156  W=101/L=55  WR=64.7%
- ny_mid: n=56  W=39/L=17  WR=69.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60d AND T4=T4c AND session_bucket=ny_close`
- Raw: n=173  W=152/L=21  WR=87.9%
- Refine: exclude T1=T1a drops 14/21 losers (67%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W02.  `H20=H20a AND H60=H60d AND session_bucket=ny_close`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; session=ny_close  •  AVOID when 1h trend WITH trade

### W03.  `H20=H20a AND H60=H60d AND T4=T4c AND session_bucket=ny_close`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when 1h trend WITH trade

### W04.  `H60=H60d AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude RSI=RSI1 drops 9/11 losers (82%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 mildly against; lower third; session=ny_close  •  AVOID when RSI 20-30 oversold

### W05.  `H60=H60d AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude RSI=RSI1 drops 9/11 losers (82%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; lower third; session=ny_close  •  AVOID when RSI 20-30 oversold

### W06.  `H60=H60d AND T1=T1c AND session_bucket=ny_close`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W07.  `H60=H60d AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF60 mildly against; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W08.  `H60=H60d AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W09.  `H60=H60d AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W10.  `H60=H60d AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W11.  `H60=H60d AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=94  W=87/L=7  WR=92.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 mildly against; RSI 30-40 weak; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W12.  `H60=H60d AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=93  W=86/L=7  WR=92.5%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W13.  `H60=H60d AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude RSI=RSI1 drops 9/11 losers (82%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 mildly against; zscore -2 to -1 oversold; session=ny_close  •  AVOID when RSI 20-30 oversold

### W14.  `H60=H60d AND T4=T4c AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude RSI=RSI1 drops 9/11 losers (82%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_close  •  AVOID when RSI 20-30 oversold

### W15.  `H60=H60d AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude RSI=RSI1 drops 9/11 losers (82%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 mildly against; lower third; zscore -2 to -1 oversold; session=ny_close  •  AVOID when RSI 20-30 oversold

### W16.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 slightly aligned

### W17.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 slightly aligned

### W18.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF20 slightly aligned

### W19.  `T4=T4c AND BBP=BBP0 AND session_bucket=off_hours`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude ZS=ZS1 drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; session=off_hours  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H60=H60d AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W21.  `H60=H60d AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 30-40 weak; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W22.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude T1=T1a drops 8/12 losers (67%)
- **Final: n=63  W=59/L=4  WR=93.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20a AND H60=H60d AND T4=T4c AND BBP=BBP2`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude T1=T1a drops 11/11 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend AGAINST trade; lower third  •  AVOID when 1h trend WITH trade

### W24.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T1=T1a drops 7/10 losers (70%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W25.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T1=T1a drops 7/10 losers (70%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI2 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is H20=H20b (15/53 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral; session=asia  •  ONLY when HTF20 slightly aligned

### L02.  `H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=87  W=29/L=58  WR=33.3%
- Sharpen: sharpest is T4=T4c (36/58 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when 4h trend AGAINST trade

### L03.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is T4=T4c (14/51 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20a AND H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (30/51 of losers there)
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L05.  `H20=H20a AND H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is RSI=RSI2 (30/51 of losers there)
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L06.  `H20=H20a AND H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=78  W=29/L=49  WR=37.2%
- Sharpen: sharpest is RSI=RSI2 (30/49 of losers there)
- **Sharp: n=42  W=12/L=30  WR=28.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L07.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T4=T4c (13/48 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L08.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T4=T4c (13/48 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L09.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is T4=T4c (13/48 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L10.  `H20=H20a AND T1=T1a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is H60=H60e (24/47 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L11.  `H20=H20a AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is H60=H60e (24/47 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L12.  `H20=H20a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is H60=H60e (24/47 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L13.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=74  W=28/L=46  WR=37.8%
- Sharpen: sharpest is H20=H20a (24/46 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is RSI=RSI3 (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 40-50 lower neutral

### L15.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is RSI=RSI3 (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 40-50 lower neutral

### L16.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=off_hours (21/42 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when session=off_hours

### L17.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=off_hours (21/42 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when session=off_hours

### L18.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is ZS=ZS2 (45/45 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L19.  `H20=H20a AND T1=T1a AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is RSI=RSI2 (34/41 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_close  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is RSI=RSI2 (34/41 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_close  •  ONLY when RSI 30-40 weak

### L21.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is session_bucket=off_hours (15/41 of losers there)
- **Sharp: n=20  W=5/L=15  WR=25.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=off_hours

### L22.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is T4=T4a (37/44 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L23.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is T4=T4a (37/44 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L24.  `H20=H20a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is BBP=BBP1 (21/40 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L25.  `H20=H20a AND T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is BBP=BBP1 (21/40 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(33/39) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
