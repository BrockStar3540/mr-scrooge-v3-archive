# USD_CAD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,990**  (W=1,286 / L=704)  -  WR: **64.6%**

## Session distribution

- ny_open: n=464  W=301/L=163  WR=64.9%
- london_open: n=351  W=230/L=121  WR=65.5%
- ny_close: n=331  W=211/L=120  WR=63.7%
- asia: n=304  W=190/L=114  WR=62.5%
- ny_mid: n=286  W=186/L=100  WR=65.0%
- london: n=201  W=129/L=72  WR=64.2%
- off_hours: n=39  W=31/L=8  WR=79.5%
- asia_late: n=14  W=8/L=6  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude session_bucket=london_open drops 8/14 losers (57%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W02.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude BBP=BBP5 drops 11/14 losers (79%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W03.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=london_open drops 8/10 losers (80%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W04.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=london_open drops 8/10 losers (80%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W05.  `H60=H60e AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude session_bucket=london_open drops 10/13 losers (77%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W06.  `H20=H20a AND H60=H60a AND ZS=ZS3`
- Raw: n=87  W=77/L=10  WR=88.5%
- Refine: no further refinement
- **Final: n=87  W=77/L=10  WR=88.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -1 to +1 neutral

### W07.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=london_open drops 8/12 losers (67%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W08.  `H20=H20a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude RSI=RSI4 drops 10/12 losers (83%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W09.  `H20=H20a AND T1=T1a AND ZS=ZS3`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude H60=H60d drops 5/10 losers (50%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when HTF60 mildly against

### W10.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude session_bucket=london_open drops 8/9 losers (89%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W11.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W12.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 aligned WITH trade

### W13.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  AVOID when HTF60 aligned WITH trade

### W14.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 aligned WITH trade

### W15.  `H20=H20a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=74  W=69/L=5  WR=93.2%
- Refine: exclude session_bucket=asia drops 2/5 losers (40%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W16.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=74  W=69/L=5  WR=93.2%
- Refine: exclude session_bucket=asia drops 2/5 losers (40%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W17.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude RSI=RSI5 drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W18.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=73  W=67/L=6  WR=91.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W19.  `H20=H20a AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=72  W=67/L=5  WR=93.1%
- Refine: exclude session_bucket=asia drops 2/5 losers (40%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=asia

### W20.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H60=H60b drops 8/9 losers (89%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  AVOID when HTF60 slightly aligned

### W21.  `H60=H60b AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W22.  `H60=H60b AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude H20=H20b drops 6/9 losers (67%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF60 slightly aligned; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W23.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=65  W=62/L=3  WR=95.4%
- Refine: exclude H60=H60b drops 2/3 losers (67%)
- **Final: n=63  W=62/L=1  WR=98.4%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W24.  `T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude session_bucket=london_open drops 6/7 losers (86%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W25.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude session_bucket=london_open drops 6/7 losers (86%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (22/46 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L02.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (22/46 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L03.  `H20=H20e AND H60=H60e AND ZS=ZS3`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_close (16/45 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L04.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is RSI=RSI4 (23/42 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L05.  `T1=T1a AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is RSI=RSI4 (23/42 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L06.  `T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is H20=H20e (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L07.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is H20=H20e (11/41 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L08.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_close (22/41 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L09.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is RSI=RSI4 (28/39 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 50-60 upper neutral

### L10.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is RSI=RSI4 (28/39 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  upper third; session=ny_close  •  ONLY when RSI 50-60 upper neutral

### L11.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is RSI=RSI4 (28/39 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when RSI 50-60 upper neutral

### L12.  `T1=T1c AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is H20=H20e (11/39 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L13.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_close (22/35 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L14.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is T4=T4a (20/36 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_close (13/35 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L16.  `H20=H20e AND ZS=ZS3 AND direction_exec=short`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H60=H60e (19/35 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L17.  `H20=H20d AND H60=H60a AND T4=T4c`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (7/33 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L18.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS3`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is H60=H60e (18/33 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H60=H60e (18/34 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L20.  `H20=H20e AND T4=T4c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H60=H60e (19/34 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L21.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is BBP=BBP5 (7/35 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_open  •  ONLY when just touched upper band

### L22.  `T1=T1c AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (27/33 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 50-60 upper neutral

### L23.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (27/33 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 50-60 upper neutral

### L24.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (27/33 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 50-60 upper neutral

### L25.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (27/33 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(6/11) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
