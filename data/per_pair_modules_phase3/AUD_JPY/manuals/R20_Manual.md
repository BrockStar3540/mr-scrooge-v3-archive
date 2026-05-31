# AUD_JPY — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,843**  (W=1,779 / L=1,064)  -  WR: **62.6%**

## Session distribution

- asia: n=996  W=616/L=380  WR=61.8%
- london_open: n=474  W=292/L=182  WR=61.6%
- ny_open: n=387  W=254/L=133  WR=65.6%
- ny_mid: n=294  W=173/L=121  WR=58.8%
- london: n=274  W=178/L=96  WR=65.0%
- ny_close: n=270  W=170/L=100  WR=63.0%
- asia_late: n=123  W=82/L=41  WR=66.7%
- off_hours: n=25  W=14/L=11  WR=56.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND BBP=BBP6`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude T4=T4a drops 9/10 losers (90%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when 4h trend WITH trade

### W02.  `H20=H20e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude T4=T4a drops 9/10 losers (90%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band  •  AVOID when 4h trend WITH trade

### W03.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude T4=T4a drops 9/10 losers (90%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when 4h trend WITH trade

### W04.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude T4=T4a drops 7/8 losers (88%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W05.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude T4=T4a drops 7/8 losers (88%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude T4=T4a drops 7/8 losers (88%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W07.  `H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when 4h trend WITH trade

### W08.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london  •  AVOID when 4h trend WITH trade

### W09.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=74  W=69/L=5  WR=93.2%
- Refine: exclude session_bucket=london_open drops 4/5 losers (80%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W11.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=74  W=69/L=5  WR=93.2%
- Refine: exclude session_bucket=london_open drops 4/5 losers (80%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W12.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=74  W=69/L=5  WR=93.2%
- Refine: exclude session_bucket=london_open drops 4/5 losers (80%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W13.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/8 losers (38%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when strategy=bravo_expansion_continuation

### W14.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when strategy=bravo_expansion_continuation

### W15.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when strategy=bravo_expansion_continuation

### W16.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W17.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W18.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W19.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W20.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20b drops 3/10 losers (30%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W21.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude H20=H20a drops 9/10 losers (90%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W22.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/8 losers (38%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when strategy=bravo_expansion_continuation

### W23.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/8 losers (38%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when strategy=bravo_expansion_continuation

### W24.  `H20=H20e AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend WITH trade

### W25.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is BBP=BBP2 (34/80 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L02.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is BBP=BBP2 (34/74 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L03.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is BBP=BBP2 (34/74 of losers there)
- **Sharp: n=46  W=12/L=34  WR=26.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L04.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (29/72 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L05.  `H20=H20a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (29/72 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L06.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (29/72 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L07.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=106  W=40/L=66  WR=37.7%
- Sharpen: sharpest is RSI=RSI2 (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L08.  `T1=T1c AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=106  W=40/L=66  WR=37.7%
- Sharpen: sharpest is RSI=RSI2 (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L09.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is H20=H20a (33/62 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF20 aligned WITH trade

### L10.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is H20=H20a (33/62 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF20 aligned WITH trade

### L11.  `T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is ZS=ZS1 (21/66 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=94  W=28/L=66  WR=29.8%
- Sharpen: sharpest is RSI=RSI2 (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L13.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is H20=H20a (33/60 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is session_bucket=asia (12/59 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L15.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is session_bucket=asia (12/59 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L16.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is session_bucket=asia (12/59 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L17.  `H20=H20a AND T4=T4a AND BBP=BBP0`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is RSI=RSI3 (30/58 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 40-50 lower neutral

### L18.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=90  W=30/L=60  WR=33.3%
- Sharpen: sharpest is ZS=ZS1 (21/60 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(53/47) | H60a(47/53) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/47) | long(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
