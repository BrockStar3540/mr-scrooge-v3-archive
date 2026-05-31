# GBP_USD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,633**  (W=949 / L=684)  -  WR: **58.1%**

## Session distribution

- ny_close: n=708  W=424/L=284  WR=59.9%
- ny_mid: n=265  W=153/L=112  WR=57.7%
- asia: n=181  W=109/L=72  WR=60.2%
- london_open: n=142  W=87/L=55  WR=61.3%
- london: n=139  W=66/L=73  WR=47.5%
- ny_open: n=89  W=49/L=40  WR=55.1%
- off_hours: n=69  W=37/L=32  WR=53.6%
- asia_late: n=40  W=24/L=16  WR=60.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude T1=T1a drops 10/14 losers (71%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 1h trend WITH trade

### W02.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude T1=T1a drops 10/14 losers (71%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 1h trend WITH trade

### W03.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude RSI=RSI5 drops 6/9 losers (67%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when RSI 60-70 strong

### W04.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude BBP=BBP2 drops 5/11 losers (45%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when lower third

### W05.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude H60=H60d drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_close  •  AVOID when HTF60 mildly against

### W06.  `H20=H20a AND T4=T4c AND ZS=ZS4`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W07.  `H60=H60d AND T4=T4c AND ZS=ZS4`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20a AND H60=H60d AND T4=T4c AND ZS=ZS4`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W10.  `H20=H20a AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60d AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W12.  `H60=H60d AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude RSI=RSI4 drops 4/9 losers (44%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W13.  `H20=H20a AND T1=T1c AND ZS=ZS4`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude RSI=RSI5 drops 5/5 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W14.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude RSI=RSI5 drops 5/5 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W15.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI5 drops 4/4 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 2/7 losers (29%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; session=ny_close  •  AVOID when strategy=alpha_extended_fade_v2

### W17.  `H60=H60d AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 2/7 losers (29%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; upper third; session=ny_close  •  AVOID when strategy=alpha_extended_fade_v2

### W18.  `H60=H60d AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 2/7 losers (29%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; upper third; session=ny_close  •  AVOID when strategy=alpha_extended_fade_v2

### W19.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

### W20.  `H60=H60d AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; upper third; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

### W21.  `T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20a AND H60=H60d AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; upper third; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

### W23.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

### W24.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

### W25.  `H60=H60d AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude T1=T1c drops 6/6 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=96  W=35/L=61  WR=36.5%
- Sharpen: sharpest is T4=T4c (46/61 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L02.  `T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=94  W=26/L=68  WR=27.7%
- Sharpen: sharpest is ZS=ZS3 (25/68 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L03.  `H20=H20b AND H60=H60a AND RSI=RSI6`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L04.  `H20=H20b AND T1=T1c AND RSI=RSI6`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L05.  `H20=H20b AND T4=T4c AND RSI=RSI6`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L06.  `H20=H20b AND RSI=RSI6 AND direction_exec=short`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L07.  `H20=H20b AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L08.  `H20=H20b AND H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L09.  `H20=H20b AND H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L10.  `H20=H20b AND H60=H60a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L11.  `H20=H20b AND H60=H60a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L12.  `H20=H20b AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L13.  `H20=H20b AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L14.  `H20=H20b AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L15.  `H20=H20b AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when zscore >+3 extreme

### L16.  `H20=H20b AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L17.  `H20=H20b AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L18.  `H60=H60a AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L19.  `H60=H60a AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L20.  `H60=H60a AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is ZS=ZS6 (19/54 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore >+3 extreme

### L21.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=84  W=24/L=60  WR=28.6%
- Sharpen: sharpest is ZS=ZS6 (43/60 of losers there)
- **Sharp: n=43  W=0/L=43  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=78  W=24/L=54  WR=30.8%
- Sharpen: sharpest is ZS=ZS6 (37/54 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L23.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=78  W=24/L=54  WR=30.8%
- Sharpen: sharpest is ZS=ZS6 (37/54 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L24.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=78  W=24/L=54  WR=30.8%
- Sharpen: sharpest is ZS=ZS6 (37/54 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L25.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=77  W=30/L=47  WR=39.0%
- Sharpen: sharpest is H20=H20e (16/47 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(30/23) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
