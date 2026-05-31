# NZD_CHF — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,617**  (W=1,071 / L=546)  -  WR: **66.2%**

## Session distribution

- asia: n=442  W=290/L=152  WR=65.6%
- ny_close: n=261  W=180/L=81  WR=69.0%
- ny_open: n=214  W=132/L=82  WR=61.7%
- ny_mid: n=204  W=125/L=79  WR=61.3%
- london_open: n=203  W=142/L=61  WR=70.0%
- off_hours: n=131  W=96/L=35  WR=73.3%
- london: n=120  W=77/L=43  WR=64.2%
- asia_late: n=42  W=29/L=13  WR=69.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=211  W=180/L=31  WR=85.3%
- Refine: exclude RSI=RSI5 drops 23/31 losers (74%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when RSI 60-70 strong

### W02.  `H20=H20a AND H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=97  W=89/L=8  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; upper third  •  AVOID when session=ny_open

### W03.  `H60=H60e AND T4=T4a AND RSI=RSI6`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 7/18 losers (39%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND H60=H60e AND T4=T4a AND ZS=ZS4`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W05.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude session_bucket=asia drops 9/17 losers (53%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W06.  `H20=H20a AND H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when session=ny_open

### W07.  `H20=H20a AND H60=H60e AND BBP=BBP4 AND direction_exec=long`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; upper third  •  AVOID when session=ny_open

### W08.  `H20=H20a AND H60=H60e AND RSI=RSI6`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude BBP=BBP6 drops 4/12 losers (33%)
- **Final: n=92  W=84/L=8  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when deep above upper band

### W09.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude session_bucket=asia drops 10/13 losers (77%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W10.  `H60=H60b AND T1=T1a AND direction_exec=long`
- Raw: n=88  W=81/L=7  WR=92.0%
- Refine: exclude session_bucket=ny_close drops 3/7 losers (43%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_close

### W11.  `H60=H60b AND T1=T1a AND T4=T4a`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W12.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_close

### W13.  `H60=H60b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=86  W=81/L=5  WR=94.2%
- Refine: exclude session_bucket=ny_close drops 3/5 losers (60%)
- **Final: n=81  W=79/L=2  WR=97.5%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W14.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI6`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude BBP=BBP6 drops 4/8 losers (50%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when deep above upper band

### W15.  `H60=H60b AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=83  W=80/L=3  WR=96.4%
- Refine: exclude session_bucket=ny_mid drops 3/3 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W16.  `H60=H60b AND T4=T4a AND RSI=RSI5`
- Raw: n=81  W=77/L=4  WR=95.1%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W17.  `H60=H60b AND T1=T1c AND direction_exec=short`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude RSI=RSI6 drops 11/11 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend AGAINST trade  •  AVOID when RSI 70-80 overbought

### W18.  `H60=H60b AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=80  W=78/L=2  WR=97.5%
- Refine: exclude H20=H20a drops 2/2 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 slightly aligned; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W19.  `H20=H20a AND T1=T1c AND ZS=ZS5`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W20.  `H20=H20a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W21.  `H20=H20a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W22.  `H20=H20a AND T4=T4c AND ZS=ZS5`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W23.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP6 drops 4/8 losers (50%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when deep above upper band

### W24.  `H20=H20a AND H60=H60e AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP6 drops 4/8 losers (50%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when deep above upper band

### W25.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude session_bucket=asia drops 7/8 losers (88%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI6 (29/67 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when RSI 70-80 overbought

### L02.  `H20=H20e AND H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is RSI=RSI6 (26/62 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 70-80 overbought

### L03.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=98  W=35/L=63  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_open (14/63 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L04.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (21/59 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (21/59 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (21/59 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (21/59 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H20=H20e AND H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (21/54 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (21/54 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third  •  ONLY when RSI 70-80 overbought

### L10.  `H20=H20e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is H60=H60e (19/56 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L11.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is ZS=ZS5 (21/42 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is ZS=ZS5 (21/42 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is ZS=ZS5 (21/42 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is ZS=ZS5 (21/42 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is ZS=ZS5 (21/42 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is ZS=ZS5 (21/42 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H20=H20e AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=66  W=21/L=45  WR=31.8%
- Sharpen: sharpest is session_bucket=ny_open (11/45 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 60-70 strong  •  ONLY when session=ny_open

### L18.  `H20=H20e AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=66  W=21/L=45  WR=31.8%
- Sharpen: sharpest is session_bucket=ny_open (11/45 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L19.  `H60=H60a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is H20=H20c (18/41 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF20 neutral

### L20.  `H20=H20e AND T4=T4c AND BBP=BBP5`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is session_bucket=ny_open (14/41 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_open

### L21.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is session_bucket=ny_open (14/41 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L22.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=london (9/39 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L23.  `H20=H20e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=london (9/39 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L24.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=london (9/39 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L25.  `H20=H20e AND T1=T1c AND BBP=BBP5`
- Raw: n=60  W=20/L=40  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_open (14/40 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/29), H20d(6/1) | H20e(32/51) |
| H60 | H60b(14/3), H60e(36/29) | H60d(4/14), H60a(34/41) |
| T1 | T1a(54/43) | T1c(46/57) |
| T4 | T4a(57/39) | T4c(43/61) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/43) | short(45/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
