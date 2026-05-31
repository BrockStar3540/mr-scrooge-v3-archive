# AUD_CHF — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,209**  (W=802 / L=407)  -  WR: **66.3%**

## Session distribution

- ny_mid: n=386  W=265/L=121  WR=68.7%
- london_open: n=258  W=179/L=79  WR=69.4%
- ny_close: n=156  W=99/L=57  WR=63.5%
- ny_open: n=131  W=87/L=44  WR=66.4%
- asia: n=117  W=72/L=45  WR=61.5%
- london: n=85  W=60/L=25  WR=70.6%
- asia_late: n=38  W=23/L=15  WR=60.5%
- off_hours: n=38  W=17/L=21  WR=44.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=164  W=141/L=23  WR=86.0%
- Refine: exclude session_bucket=ny_mid drops 11/23 losers (48%)
- **Final: n=127  W=115/L=12  WR=90.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W02.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude session_bucket=asia_late drops 5/13 losers (38%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W03.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude session_bucket=asia_late drops 5/13 losers (38%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W04.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude session_bucket=asia_late drops 5/13 losers (38%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W05.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W06.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/13 losers (38%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W07.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/13 losers (38%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W08.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 5/13 losers (38%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W09.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W10.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W11.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=asia_late drops 5/10 losers (50%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W12.  `T1=T1a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude session_bucket=asia_late drops 5/10 losers (50%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W13.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude H20=H20b drops 3/7 losers (43%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  AVOID when HTF20 slightly aligned

### W14.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W15.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=ny_mid drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W16.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=66  W=64/L=2  WR=97.0%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W17.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W18.  `H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W19.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W20.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W21.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=62  W=60/L=2  WR=96.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W23.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=62  W=60/L=2  WR=96.8%
- Refine: exclude BBP=BBP4 drops 2/2 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when upper third

### W24.  `T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude H20=H20b drops 3/5 losers (60%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W25.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude H20=H20b drops 3/5 losers (60%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_open (18/75 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L02.  `T4=T4a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=77  W=29/L=48  WR=37.7%
- Sharpen: sharpest is H60=H60a (42/48 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L03.  `H60=H60a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=67  W=21/L=46  WR=31.3%
- Sharpen: sharpest is T4=T4a (42/46 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L04.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=67  W=21/L=46  WR=31.3%
- Sharpen: sharpest is T4=T4a (42/46 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L05.  `H60=H60a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=67  W=21/L=46  WR=31.3%
- Sharpen: sharpest is T4=T4a (42/46 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is T4=T4a (32/36 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is T4=T4a (32/36 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is T4=T4a (32/36 of losers there)
- **Sharp: n=44  W=12/L=32  WR=27.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L09.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=54  W=12/L=42  WR=22.2%
- Sharpen: sharpest is session_bucket=asia (12/42 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L10.  `T4=T4a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=54  W=12/L=42  WR=22.2%
- Sharpen: sharpest is session_bucket=asia (12/42 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L11.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (16/34 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L12.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is T4=T4a (32/32 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is T4=T4a (32/32 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L14.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is T4=T4a (32/32 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is BBP=BBP1 (27/34 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L16.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is BBP=BBP1 (27/34 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L17.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is T4=T4a (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L18.  `T1=T1c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is T4=T4a (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L19.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is strategy_id=TF2_pullback_EMA20_short (12/31 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  middle of band; zscore -1 to +1 neutral  •  ONLY when strategy=TF2_pullback_EMA20_short

### L20.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is H20=H20a (27/29 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS1`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_open (13/28 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L22.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_open (13/28 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L23.  `H60=H60a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is T4=T4a (25/28 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L24.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is T4=T4a (25/28 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L25.  `H60=H60a AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is T4=T4a (25/28 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(50/39) | H20a(32/45) |
| H60 | H60e(57/41) | H60a(34/53) |
| T1 | — | — |
| T4 | T4c(62/39) | T4a(38/61) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(60/47) | long(40/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
