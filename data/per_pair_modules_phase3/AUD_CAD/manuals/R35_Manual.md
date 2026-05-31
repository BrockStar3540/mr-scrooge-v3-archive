# AUD_CAD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,607**  (W=1,718 / L=889)  -  WR: **65.9%**

## Session distribution

- asia: n=1143  W=765/L=378  WR=66.9%
- ny_close: n=580  W=361/L=219  WR=62.2%
- off_hours: n=232  W=150/L=82  WR=64.7%
- london_open: n=192  W=132/L=60  WR=68.8%
- london: n=183  W=129/L=54  WR=70.5%
- asia_late: n=174  W=115/L=59  WR=66.1%
- ny_open: n=103  W=66/L=37  WR=64.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60d AND T4=T4a`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=london drops 9/17 losers (53%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=london

### W02.  `H20=H20a AND H60=H60d AND direction_exec=long`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=london drops 9/17 losers (53%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when session=london

### W03.  `H20=H20a AND H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=london drops 9/17 losers (53%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=london

### W04.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude strategy_id=BR5_opening_range_breakout_long drops 4/14 losers (29%)
- **Final: n=89  W=79/L=10  WR=88.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when strategy=BR5_opening_range_breakout_long

### W05.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude strategy_id=BR5_opening_range_breakout_long drops 4/14 losers (29%)
- **Final: n=89  W=79/L=10  WR=88.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when strategy=BR5_opening_range_breakout_long

### W06.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude strategy_id=BR5_opening_range_breakout_long drops 3/13 losers (23%)
- **Final: n=85  W=75/L=10  WR=88.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when strategy=BR5_opening_range_breakout_long

### W07.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=off_hours drops 3/12 losers (25%)
- **Final: n=76  W=67/L=9  WR=88.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=off_hours

### W08.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=off_hours drops 3/12 losers (25%)
- **Final: n=76  W=67/L=9  WR=88.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=off_hours

### W09.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=off_hours drops 3/12 losers (25%)
- **Final: n=76  W=67/L=9  WR=88.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=off_hours

### W10.  `H20=H20c AND H60=H60a AND RSI=RSI5`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS4 drops 9/11 losers (82%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W11.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H20=H20a drops 10/11 losers (91%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 aligned WITH trade

### W12.  `T1=T1a AND BBP=BBP5 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H60=H60c drops 4/11 losers (36%)
- **Final: n=64  W=57/L=7  WR=89.1%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 60-70 strong; session=asia  •  AVOID when HTF60 neutral

### W13.  `H20=H20b AND H60=H60a AND direction_exec=long`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude session_bucket=off_hours drops 4/7 losers (57%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when session=off_hours

### W14.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude session_bucket=off_hours drops 3/11 losers (27%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=off_hours

### W15.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=75  W=70/L=5  WR=93.3%
- Refine: exclude session_bucket=off_hours drops 4/5 losers (80%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=off_hours

### W16.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=75  W=70/L=5  WR=93.3%
- Refine: exclude session_bucket=off_hours drops 4/5 losers (80%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=off_hours

### W17.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude session_bucket=off_hours drops 4/4 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=off_hours

### W18.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude session_bucket=off_hours drops 4/4 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=off_hours

### W19.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=74  W=70/L=4  WR=94.6%
- Refine: exclude session_bucket=off_hours drops 4/4 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=off_hours

### W20.  `H20=H20c AND H60=H60c AND T4=T4c`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 neutral; 4h trend AGAINST trade  •  AVOID when session=asia

### W21.  `H20=H20c AND H60=H60c AND T1=T1c`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS2 drops 3/10 losers (30%)
- **Final: n=61  W=54/L=7  WR=88.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 neutral; 1h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W22.  `H20=H20c AND H60=H60c AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS2 drops 3/10 losers (30%)
- **Final: n=61  W=54/L=7  WR=88.5%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 neutral  •  AVOID when zscore -2 to -1 oversold

### W23.  `H20=H20c AND H60=H60c AND T1=T1c AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude ZS=ZS2 drops 3/10 losers (30%)
- **Final: n=61  W=54/L=7  WR=88.5%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 neutral; 1h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W24.  `H20=H20c AND H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 3/9 losers (33%)
- **Final: n=57  W=51/L=6  WR=89.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when strategy=TF2_pullback_EMA20_long

### W25.  `H20=H20c AND H60=H60c AND T4=T4c AND direction_exec=short`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 3/9 losers (33%)
- **Final: n=57  W=51/L=6  WR=89.5%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 neutral; 4h trend AGAINST trade  •  AVOID when strategy=TF2_pullback_EMA20_long

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is ZS=ZS3 (15/48 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L02.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is ZS=ZS3 (15/48 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L03.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is ZS=ZS3 (15/48 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L04.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is ZS=ZS3 (15/47 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L05.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is ZS=ZS3 (15/47 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L06.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is ZS=ZS3 (15/47 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L07.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=73  W=26/L=47  WR=35.6%
- Sharpen: sharpest is ZS=ZS3 (15/47 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L08.  `H20=H20e AND H60=H60b AND T4=T4c`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=asia_late (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L09.  `H20=H20e AND H60=H60b AND direction_exec=short`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=asia_late (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned  •  ONLY when session=asia_late

### L10.  `T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=72  W=28/L=44  WR=38.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L11.  `H20=H20e AND H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: sharpest is session_bucket=asia_late (11/44 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L12.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=72  W=28/L=44  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=72  W=28/L=44  WR=38.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L13.  `H20=H20e AND H60=H60b AND T1=T1c`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=asia_late (11/43 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade  •  ONLY when session=asia_late

### L14.  `H20=H20e AND H60=H60b AND T1=T1c AND T4=T4c`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=asia_late (11/43 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L15.  `H20=H20e AND H60=H60b AND T1=T1c AND direction_exec=short`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=asia_late (11/43 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade  •  ONLY when session=asia_late

### L16.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=70  W=26/L=44  WR=37.1%
- Sharpen: sharpest is ZS=ZS3 (12/44 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L17.  `T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=70  W=28/L=42  WR=40.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -2 to -1 oversold

### L18.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=70  W=28/L=42  WR=40.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold

### L19.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=70  W=28/L=42  WR=40.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold

### L20.  `H60=H60b AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20b (15/34 of losers there)
- **Sharp: n=18  W=3/L=15  WR=16.7%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 60-70 strong; session=asia  •  ONLY when HTF20 slightly aligned

### L21.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_close (18/32 of losers there)
- **Sharp: n=24  W=6/L=18  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L22.  `H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is session_bucket=off_hours (5/29 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=off_hours

### L23.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is session_bucket=off_hours (5/29 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=off_hours

### L24.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is session_bucket=off_hours (5/29 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=off_hours

### L25.  `H60=H60e AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is session_bucket=off_hours (5/29 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=off_hours

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(31/37) |
| H60 | H60a(39/33) | H60e(35/42) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | ZS5(29/24) | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
