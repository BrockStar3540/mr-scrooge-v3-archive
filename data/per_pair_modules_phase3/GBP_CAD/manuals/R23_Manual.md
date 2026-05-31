# GBP_CAD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,541**  (W=2,763 / L=1,778)  -  WR: **60.8%**

## Session distribution

- ny_mid: n=1072  W=658/L=414  WR=61.4%
- london_open: n=897  W=539/L=358  WR=60.1%
- ny_open: n=660  W=403/L=257  WR=61.1%
- ny_close: n=659  W=389/L=270  WR=59.0%
- london: n=639  W=403/L=236  WR=63.1%
- asia: n=371  W=232/L=139  WR=62.5%
- off_hours: n=177  W=99/L=78  WR=55.9%
- asia_late: n=66  W=40/L=26  WR=60.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60c AND T1=T1a AND RSI=RSI5`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude H20=H20b drops 9/21 losers (43%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W02.  `H60=H60c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude H20=H20b drops 9/21 losers (43%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: LONG**  •  HTF60 neutral; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W03.  `H60=H60c AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude H20=H20b drops 9/21 losers (43%)
- **Final: n=113  W=101/L=12  WR=89.4%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W04.  `H20=H20b AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude BBP=BBP5 drops 7/17 losers (41%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 70-80 overbought; session=ny_mid  •  AVOID when just touched upper band

### W05.  `H20=H20b AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W06.  `H20=H20b AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W07.  `H20=H20b AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; session=ny_mid  •  AVOID when just touched upper band

### W08.  `H20=H20b AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W09.  `H20=H20b AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when just touched upper band

### W10.  `H20=H20b AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W11.  `H20=H20b AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when just touched upper band

### W12.  `H20=H20b AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W13.  `H20=H20b AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 70-80 overbought; session=ny_mid  •  AVOID when just touched upper band

### W14.  `H60=H60c AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude H20=H20b drops 9/14 losers (64%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W15.  `H60=H60c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude H20=H20b drops 9/14 losers (64%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: LONG**  •  HTF60 neutral; upper third; RSI 60-70 strong  •  AVOID when HTF20 slightly aligned

### W16.  `T1=T1a AND T4=T4a AND RSI=RSI7`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought

### W17.  `T1=T1a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI>80 extreme overbought

### W18.  `T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: LONG**  •  4h trend WITH trade; RSI>80 extreme overbought

### W19.  `T1=T1a AND T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=95  W=94/L=1  WR=98.9%
- Refine: no further refinement
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought

### W20.  `H20=H20b AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude strategy_id=RG1_range_bound_scalp_short drops 2/9 losers (22%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; session=ny_mid  •  AVOID when strategy=RG1_range_bound_scalp_short

### W21.  `H20=H20a AND T1=T1a AND session_bucket=london`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when RSI 70-80 overbought

### W22.  `H20=H20a AND T4=T4a AND session_bucket=london`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when RSI 70-80 overbought

### W23.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  AVOID when RSI 70-80 overbought

### W24.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when RSI 70-80 overbought

### W25.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when RSI 70-80 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=139  W=45/L=94  WR=32.4%
- Sharpen: sharpest is H20=H20e (35/94 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=54/L=81  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L03.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=54/L=81  WR=40.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L04.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=54/L=81  WR=40.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L05.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=131  W=45/L=86  WR=34.4%
- Sharpen: sharpest is H20=H20e (35/86 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L06.  `T4=T4c AND BBP=BBP6 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=131  W=45/L=86  WR=34.4%
- Sharpen: sharpest is H20=H20e (35/86 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L07.  `H60=H60e AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=49/L=74  WR=39.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 70-80 overbought; session=ny_mid

### L08.  `H20=H20d AND H60=H60c AND T1=T1c`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is RSI=RSI6 (59/74 of losers there)
- **Sharp: n=77  W=18/L=59  WR=23.4%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20d AND H60=H60c AND T4=T4c`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is RSI=RSI6 (59/74 of losers there)
- **Sharp: n=77  W=18/L=59  WR=23.4%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L10.  `H20=H20d AND H60=H60c AND direction_exec=short`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is RSI=RSI6 (59/74 of losers there)
- **Sharp: n=77  W=18/L=59  WR=23.4%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 neutral  •  ONLY when RSI 70-80 overbought

### L11.  `H20=H20d AND H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is RSI=RSI6 (59/74 of losers there)
- **Sharp: n=77  W=18/L=59  WR=23.4%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L12.  `H20=H20d AND H60=H60c AND T1=T1c AND direction_exec=short`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is RSI=RSI6 (59/74 of losers there)
- **Sharp: n=77  W=18/L=59  WR=23.4%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L13.  `H20=H20d AND H60=H60c AND T4=T4c AND direction_exec=short`
- Raw: n=110  W=36/L=74  WR=32.7%
- Sharpen: sharpest is RSI=RSI6 (59/74 of losers there)
- **Sharp: n=77  W=18/L=59  WR=23.4%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L14.  `T4=T4c AND BBP=BBP6 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=106  W=38/L=68  WR=35.8%
- Sharpen: sharpest is H20=H20e (29/68 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L15.  `H60=H60e AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is ZS=ZS5 (58/66 of losers there)
- **Sharp: n=72  W=14/L=58  WR=19.4%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60a AND T1=T1c AND BBP=BBP5`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is H20=H20e (37/61 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  ONLY when HTF20 strongly against

### L17.  `H60=H60a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is H20=H20e (37/61 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; just touched upper band  •  ONLY when HTF20 strongly against

### L18.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is H20=H20e (37/61 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L19.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is H20=H20e (37/61 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  ONLY when HTF20 strongly against

### L20.  `H60=H60a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is H20=H20e (37/61 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L21.  `H20=H20d AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=100  W=38/L=62  WR=38.0%
- Sharpen: sharpest is session_bucket=london (27/62 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  HTF20 mildly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L22.  `H60=H60a AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is H20=H20e (22/71 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L23.  `H60=H60a AND BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is H20=H20e (22/71 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L24.  `H20=H20e AND T4=T4c AND BBP=BBP6`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is RSI=RSI6 (35/65 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when RSI 70-80 overbought

### L25.  `H20=H20c AND H60=H60d AND ZS=ZS4`
- Raw: n=95  W=35/L=60  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (37/60 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 mildly against; zscore +1 to +2 overbought  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(18/12) | H20d(13/19), H20e(26/31) |
| H60 | — | — |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/45) | short(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
