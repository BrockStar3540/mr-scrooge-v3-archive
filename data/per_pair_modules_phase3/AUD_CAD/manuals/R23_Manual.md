# AUD_CAD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,976**  (W=1,242 / L=734)  -  WR: **62.9%**

## Session distribution

- asia: n=816  W=522/L=294  WR=64.0%
- ny_close: n=401  W=245/L=156  WR=61.1%
- ny_open: n=252  W=163/L=89  WR=64.7%
- london: n=148  W=89/L=59  WR=60.1%
- asia_late: n=129  W=81/L=48  WR=62.8%
- off_hours: n=129  W=73/L=56  WR=56.6%
- london_open: n=70  W=51/L=19  WR=72.9%
- ny_mid: n=31  W=18/L=13  WR=58.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=139  W=120/L=19  WR=86.3%
- Refine: exclude BBP=BBP6 drops 4/19 losers (21%)
- **Final: n=131  W=116/L=15  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when deep above upper band

### W02.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=112  W=99/L=13  WR=88.4%
- Refine: exclude H20=H20e drops 8/13 losers (62%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W03.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude H20=H20e drops 8/13 losers (62%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W04.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20e drops 3/14 losers (21%)
- **Final: n=91  W=80/L=11  WR=87.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 strongly against

### W05.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  AVOID when session=asia

### W06.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_open

### W07.  `H20=H20c AND T1=T1c AND RSI=RSI4`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W08.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI3 drops 5/9 losers (56%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude T4=T4c drops 6/9 losers (67%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W10.  `H60=H60d AND RSI=RSI3 AND direction_exec=long`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude session_bucket=ny_open drops 5/7 losers (71%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W11.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude strategy_id=BR5_opening_range_breakout_short drops 3/7 losers (43%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when strategy=BR5_opening_range_breakout_short

### W12.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude H20=H20e drops 3/8 losers (38%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W13.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude ZS=ZS1 drops 5/9 losers (56%)
- **Final: n=42  W=38/L=4  WR=90.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W15.  `H20=H20a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude RSI=RSI3 drops 5/9 losers (56%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band  •  AVOID when RSI 40-50 lower neutral

### W16.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude RSI=RSI3 drops 5/9 losers (56%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W17.  `H20=H20c AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=58  W=54/L=4  WR=93.1%
- Refine: exclude BBP=BBP0 drops 3/4 losers (75%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when deep below lower band

### W18.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W19.  `H60=H60d AND T1=T1c AND RSI=RSI3`
- Raw: n=53  W=50/L=3  WR=94.3%
- Refine: exclude session_bucket=ny_open drops 2/3 losers (67%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W20.  `H60=H60d AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=53  W=50/L=3  WR=94.3%
- Refine: exclude session_bucket=ny_open drops 2/3 losers (67%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W21.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=53  W=49/L=4  WR=92.5%
- Refine: exclude T4=T4c drops 3/4 losers (75%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=53  W=49/L=4  WR=92.5%
- Refine: exclude T4=T4c drops 3/4 losers (75%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W23.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude strategy_id=BR5_opening_range_breakout_short drops 3/7 losers (43%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when strategy=BR5_opening_range_breakout_short

### W24.  `T1=T1c AND T4=T4a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=52  W=45/L=7  WR=86.5%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=ny_close

### W25.  `H60=H60b AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=50  W=46/L=4  WR=92.0%
- Refine: exclude T1=T1a drops 4/4 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; session=ny_open  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is H20=H20c (20/59 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 neutral

### L02.  `H60=H60c AND T4=T4a AND direction_exec=short`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (13/58 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L03.  `H20=H20d AND T1=T1c AND T4=T4a`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is RSI=RSI5 (21/53 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L04.  `H20=H20d AND H60=H60c AND T4=T4a`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is RSI=RSI5 (13/50 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20d AND H60=H60c AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is RSI=RSI5 (13/50 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 neutral  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20d AND H60=H60c AND T4=T4a AND direction_exec=short`
- Raw: n=76  W=26/L=50  WR=34.2%
- Sharpen: sharpest is RSI=RSI5 (13/50 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 neutral; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L07.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is H20=H20e (25/49 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L08.  `H20=H20d AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is RSI=RSI5 (21/43 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L09.  `H20=H20c AND T1=T1a AND T4=T4c`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is H60=H60a (20/42 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L10.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is direction_exec=long (38/38 of losers there)
- **Sharp: n=54  W=16/L=38  WR=29.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when long

### L11.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is H60=H60a (35/36 of losers there)
- **Sharp: n=51  W=16/L=35  WR=31.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L12.  `H60=H60c AND T1=T1c AND direction_exec=short`
- Raw: n=58  W=20/L=38  WR=34.5%
- Sharpen: sharpest is RSI=RSI5 (13/38 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L13.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is H20=H20e (17/36 of losers there)
- **Sharp: n=23  W=6/L=17  WR=26.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L14.  `H60=H60c AND T1=T1c AND T4=T4a`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is RSI=RSI5 (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60c AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=56  W=19/L=37  WR=33.9%
- Sharpen: sharpest is RSI=RSI5 (13/37 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=54  W=16/L=38  WR=29.6%
- Sharpen: sharpest is H20=H20d (8/38 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 mildly against

### L17.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is direction_exec=long (33/33 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when long

### L18.  `T4=T4c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is ZS=ZS1 (32/33 of losers there)
- **Sharp: n=42  W=10/L=32  WR=23.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is H20=H20c (13/33 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 neutral

### L20.  `T1=T1a AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is H20=H20e (22/32 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L21.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=48  W=13/L=35  WR=27.1%
- Sharpen: sharpest is H20=H20c (9/35 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 neutral

### L22.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is RSI=RSI5 (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L23.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is RSI=RSI5 (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is RSI=RSI5 (6/31 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60d AND RSI=RSI4 AND direction_exec=long`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is session_bucket=ny_open (17/31 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 50-60 upper neutral  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(34/27) | H20d(9/16) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
