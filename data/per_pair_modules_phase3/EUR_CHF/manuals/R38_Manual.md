# EUR_CHF — R38 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,592**  (W=1,024 / L=568)  -  WR: **64.3%**

## Session distribution

- asia: n=458  W=293/L=165  WR=64.0%
- ny_close: n=280  W=175/L=105  WR=62.5%
- london_open: n=224  W=151/L=73  WR=67.4%
- ny_mid: n=178  W=117/L=61  WR=65.7%
- london: n=172  W=102/L=70  WR=59.3%
- ny_open: n=143  W=88/L=55  WR=61.5%
- asia_late: n=99  W=73/L=26  WR=73.7%
- off_hours: n=38  W=25/L=13  WR=65.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 7/16 losers (44%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W02.  `H20=H20a AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 7/16 losers (44%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W03.  `H20=H20a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude RSI=RSI3 drops 7/15 losers (47%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W04.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=100  W=92/L=8  WR=92.0%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=88  W=80/L=8  WR=90.9%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H20=H20e drops 5/13 losers (38%)
- **Final: n=78  W=70/L=8  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W07.  `H20=H20a AND T1=T1c AND ZS=ZS5`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude RSI=RSI3 drops 4/11 losers (36%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W08.  `H60=H60b AND T1=T1a AND direction_exec=long`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20e drops 10/11 losers (91%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when HTF20 strongly against

### W09.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude session_bucket=london drops 3/7 losers (43%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W10.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=london drops 3/7 losers (43%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W11.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=london drops 3/7 losers (43%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W12.  `H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W13.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W14.  `H20=H20a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched upper band  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20a AND H60=H60d AND direction_exec=short`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI3 drops 8/9 losers (89%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when RSI 40-50 lower neutral

### W17.  `H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W18.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=asia

### W19.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia

### W20.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=london drops 3/6 losers (50%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W21.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude H60=H60e drops 2/5 losers (40%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W22.  `H20=H20a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=63  W=58/L=5  WR=92.1%
- Refine: exclude H60=H60e drops 2/5 losers (40%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W23.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude RSI=RSI3 drops 6/7 losers (86%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W24.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W25.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=57  W=52/L=5  WR=91.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is session_bucket=ny_close (15/59 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L02.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is session_bucket=ny_close (15/59 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L03.  `H20=H20d AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (12/45 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L04.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is T1=T1a (19/41 of losers there)
- **Sharp: n=26  W=7/L=19  WR=26.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend WITH trade

### L05.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is T1=T1c (29/42 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  ONLY when 1h trend AGAINST trade

### L06.  `H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is T1=T1c (22/44 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L07.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_close (8/35 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L08.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=57  W=22/L=35  WR=38.6%
- Sharpen: sharpest is T1=T1a (23/35 of losers there)
- **Sharp: n=33  W=10/L=23  WR=30.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend WITH trade

### L09.  `H20=H20d AND H60=H60e AND BBP=BBP4`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_close (13/34 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; upper third  •  ONLY when session=ny_close

### L10.  `H20=H20d AND H60=H60e AND ZS=ZS4`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_close (13/34 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L11.  `H20=H20d AND H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_close (13/34 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L12.  `H20=H20d AND H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_close (13/34 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; upper third  •  ONLY when session=ny_close

### L13.  `H20=H20d AND H60=H60e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=53  W=19/L=34  WR=35.8%
- Sharpen: sharpest is session_bucket=ny_close (13/34 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L14.  `H60=H60c AND T4=T4a AND direction_exec=long`
- Raw: n=53  W=20/L=33  WR=37.7%
- Sharpen: sharpest is session_bucket=london (11/33 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when session=london

### L15.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: sharpest is session_bucket=london_open (10/35 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L16.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is T1=T1a (22/32 of losers there)
- **Sharp: n=32  W=10/L=22  WR=31.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L17.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=51  W=20/L=31  WR=39.2%
- Sharpen: sharpest is H20=H20e (19/31 of losers there)
- **Sharp: n=26  W=7/L=19  WR=26.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF20 strongly against

### L18.  `T4=T4a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=50  W=16/L=34  WR=32.0%
- Sharpen: sharpest is BBP=BBP0 (14/34 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when deep below lower band

### L19.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is H60=H60e (18/30 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 strongly against

### L20.  `H20=H20d AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is session_bucket=ny_close (12/31 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L21.  `H20=H20d AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is session_bucket=ny_close (12/31 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L22.  `H20=H20d AND H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=45  W=17/L=28  WR=37.8%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade; upper third

### L23.  `H20=H20d AND H60=H60e AND T1=T1a AND ZS=ZS4`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=45  W=17/L=28  WR=37.8%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought

### L24.  `H20=H20d AND T4=T4a AND RSI=RSI4`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L25.  `H20=H20d AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(37/26) | H20e(29/39) |
| H60 | H60a(35/22) | H60e(22/37) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(52/42) | long(48/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
