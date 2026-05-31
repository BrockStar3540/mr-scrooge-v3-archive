# AUD_USD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,662**  (W=1,742 / L=920)  -  WR: **65.4%**

## Session distribution

- asia: n=1240  W=806/L=434  WR=65.0%
- ny_close: n=422  W=265/L=157  WR=62.8%
- london: n=239  W=157/L=82  WR=65.7%
- asia_late: n=205  W=148/L=57  WR=72.2%
- london_open: n=203  W=133/L=70  WR=65.5%
- ny_open: n=176  W=117/L=59  WR=66.5%
- off_hours: n=148  W=100/L=48  WR=67.6%
- ny_mid: n=29  W=16/L=13  WR=55.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND RSI=RSI4`
- Raw: n=212  W=181/L=31  WR=85.4%
- Refine: exclude ZS=ZS3 drops 8/31 losers (26%)
- **Final: n=187  W=164/L=23  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W02.  `H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=200  W=170/L=30  WR=85.0%
- Refine: exclude ZS=ZS3 drops 9/30 losers (30%)
- **Final: n=171  W=150/L=21  WR=87.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W03.  `T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=188  W=164/L=24  WR=87.2%
- Refine: exclude ZS=ZS3 drops 6/24 losers (25%)
- **Final: n=167  W=149/L=18  WR=89.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W04.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=178  W=156/L=22  WR=87.6%
- Refine: exclude ZS=ZS3 drops 6/22 losers (27%)
- **Final: n=157  W=141/L=16  WR=89.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W05.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=177  W=155/L=22  WR=87.6%
- Refine: exclude ZS=ZS3 drops 6/22 losers (27%)
- **Final: n=156  W=140/L=16  WR=89.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=167  W=147/L=20  WR=88.0%
- Refine: exclude ZS=ZS3 drops 6/20 losers (30%)
- **Final: n=146  W=132/L=14  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=152  W=130/L=22  WR=85.5%
- Refine: exclude T4=T4c drops 11/22 losers (50%)
- **Final: n=105  W=94/L=11  WR=89.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=139  W=119/L=20  WR=85.6%
- Refine: exclude ZS=ZS5 drops 9/20 losers (45%)
- **Final: n=99  W=88/L=11  WR=88.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W09.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude ZS=ZS5 drops 9/18 losers (50%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W10.  `T1=T1c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=127  W=113/L=14  WR=89.0%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 3/14 losers (21%)
- **Final: n=120  W=109/L=11  WR=90.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when strategy=charlie_pullback_continuation_v2

### W11.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=122  W=106/L=16  WR=86.9%
- Refine: exclude ZS=ZS5 drops 9/16 losers (56%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +2 to +3 deep overbought

### W12.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude BBP=BBP2 drops 4/15 losers (27%)
- **Final: n=108  W=97/L=11  WR=89.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when lower third

### W13.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=109  W=97/L=12  WR=89.0%
- Refine: exclude ZS=ZS3 drops 4/12 losers (33%)
- **Final: n=99  W=91/L=8  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude RSI=RSI2 drops 8/16 losers (50%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W15.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude strategy_id=echo_box_fade_v2 drops 3/8 losers (38%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when strategy=echo_box_fade_v2

### W16.  `T1=T1c AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude direction_exec=short drops 9/12 losers (75%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when short

### W17.  `T1=T1c AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude direction_exec=short drops 9/12 losers (75%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when short

### W18.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude ZS=ZS3 drops 3/10 losers (30%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W19.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude RSI=RSI2 drops 5/11 losers (45%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 30-40 weak

### W20.  `T1=T1c AND T4=T4c AND session_bucket=asia_late`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude RSI=RSI4 drops 6/9 losers (67%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W21.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude ZS=ZS3 drops 3/8 losers (38%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W22.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=82  W=75/L=7  WR=91.5%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W23.  `H20=H20e AND T4=T4c AND session_bucket=asia_late`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude RSI=RSI4 drops 7/9 losers (78%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia_late  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI3 drops 7/11 losers (64%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W25.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=164  W=63/L=101  WR=38.4%
- Sharpen: sharpest is H20=H20e (80/101 of losers there)
- **Sharp: n=113  W=33/L=80  WR=29.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L02.  `H20=H20e AND T1=T1a AND RSI=RSI4`
- Raw: n=158  W=63/L=95  WR=39.9%
- Sharpen: sharpest is H60=H60e (80/95 of losers there)
- **Sharp: n=113  W=33/L=80  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L03.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=152  W=53/L=99  WR=34.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=152  W=53/L=99  WR=34.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral

### L04.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=138  W=45/L=93  WR=32.6%
- Sharpen: sharpest is T4=T4c (61/93 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=127  W=41/L=86  WR=32.3%
- Sharpen: sharpest is ZS=ZS5 (32/86 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=113  W=33/L=80  WR=29.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=113  W=33/L=80  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral

### L07.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=104  W=33/L=71  WR=31.7%
- Sharpen: sharpest is H60=H60e (61/71 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L08.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=101  W=33/L=68  WR=32.7%
- Sharpen: sharpest is T4=T4c (53/68 of losers there)
- **Sharp: n=71  W=18/L=53  WR=25.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L09.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=97  W=30/L=67  WR=30.9%
- Sharpen: sharpest is session_bucket=asia (53/67 of losers there)
- **Sharp: n=71  W=18/L=53  WR=25.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L10.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is T4=T4c (49/64 of losers there)
- **Sharp: n=63  W=14/L=49  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L11.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=83  W=22/L=61  WR=26.5%
- Sharpen: sharpest is session_bucket=asia (49/61 of losers there)
- **Sharp: n=63  W=14/L=49  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L12.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (12/41 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L13.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is H20=H20a (26/41 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is session_bucket=london_open (9/41 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L15.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is session_bucket=london_open (9/41 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when session=london_open

### L16.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is session_bucket=london_open (9/41 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=london_open

### L17.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=59  W=19/L=40  WR=32.2%
- Sharpen: sharpest is BBP=BBP5 (20/40 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L18.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=59  W=19/L=40  WR=32.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=59  W=19/L=40  WR=32.2%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral

### L19.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is H20=H20e (26/35 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L20.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=56  W=18/L=38  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=56  W=18/L=38  WR=32.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L21.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is BBP=BBP5 (19/39 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L22.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=52  W=15/L=37  WR=28.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=52  W=15/L=37  WR=28.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral

### L23.  `H20=H20e AND H60=H60b AND T4=T4c`
- Raw: n=51  W=17/L=34  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L24.  `H20=H20e AND H60=H60b AND direction_exec=short`
- Raw: n=51  W=17/L=34  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned  •  ONLY when RSI 40-50 lower neutral

### L25.  `H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=51  W=17/L=34  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(57/43) | T1a(43/57) |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(51/46) | short(49/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
