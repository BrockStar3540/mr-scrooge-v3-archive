# GBP_NZD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,846**  (W=4,058 / L=2,788)  -  WR: **59.3%**

## Session distribution

- asia: n=2261  W=1361/L=900  WR=60.2%
- london_open: n=1157  W=659/L=498  WR=57.0%
- london: n=862  W=510/L=352  WR=59.2%
- ny_open: n=821  W=495/L=326  WR=60.3%
- ny_close: n=625  W=357/L=268  WR=57.1%
- asia_late: n=563  W=352/L=211  WR=62.5%
- ny_mid: n=452  W=263/L=189  WR=58.2%
- off_hours: n=105  W=61/L=44  WR=58.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=167  W=145/L=22  WR=86.8%
- Refine: exclude BBP=BBP2 drops 9/22 losers (41%)
- **Final: n=148  W=135/L=13  WR=91.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W02.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=156  W=137/L=19  WR=87.8%
- Refine: exclude BBP=BBP2 drops 9/19 losers (47%)
- **Final: n=141  W=131/L=10  WR=92.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W03.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=145  W=124/L=21  WR=85.5%
- Refine: exclude BBP=BBP2 drops 9/21 losers (43%)
- **Final: n=130  W=118/L=12  WR=90.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when lower third

### W04.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude BBP=BBP2 drops 9/18 losers (50%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  AVOID when lower third

### W05.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude BBP=BBP2 drops 9/18 losers (50%)
- **Final: n=109  W=100/L=9  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when lower third

### W06.  `H60=H60e AND ZS=ZS5 AND session_bucket=london`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude T1=T1c drops 15/17 losers (88%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=london  •  AVOID when 1h trend AGAINST trade

### W07.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=london`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude BBP=BBP2 drops 9/17 losers (53%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=london  •  AVOID when lower third

### W08.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude session_bucket=london_open drops 10/16 losers (62%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=london_open

### W09.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=london`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude BBP=BBP2 drops 9/14 losers (64%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london  •  AVOID when lower third

### W10.  `H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP4 drops 11/15 losers (73%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_close  •  AVOID when upper third

### W11.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP4 drops 11/15 losers (73%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when upper third

### W12.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude BBP=BBP4 drops 9/13 losers (69%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when upper third

### W13.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude T1=T1c drops 12/15 losers (80%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W14.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude direction_exec=long drops 13/13 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when long

### W15.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=london_open drops 10/15 losers (67%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W16.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude T4=T4c drops 10/10 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when 4h trend AGAINST trade

### W17.  `T1=T1c AND BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude ZS=ZS6 drops 11/12 losers (92%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when zscore >+3 extreme

### W18.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude H20=H20a drops 11/12 losers (92%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W19.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=london`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude H60=H60a drops 10/12 losers (83%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=london  •  AVOID when HTF60 aligned WITH trade

### W20.  `H20=H20a AND T4=T4c AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude RSI=RSI4 drops 10/13 losers (77%)
- **Final: n=34  W=31/L=3  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral; session=asia  •  AVOID when RSI 50-60 upper neutral

### W21.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/11 losers (73%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W22.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/11 losers (73%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  AVOID when session=ny_open

### W23.  `H60=H60b AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude ZS=ZS3 drops 7/13 losers (54%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W24.  `H60=H60c AND T1=T1c AND T4=T4c AND ZS=ZS3`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude BBP=BBP2 drops 3/9 losers (33%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when lower third

### W25.  `T1=T1a AND BBP=BBP6 AND session_bucket=london`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; session=london  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=273  W=104/L=169  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=273  W=104/L=169  WR=38.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open

### L02.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=240  W=93/L=147  WR=38.8%
- Sharpen: sharpest is ZS=ZS5 (69/147 of losers there)
- **Sharp: n=79  W=10/L=69  WR=12.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=239  W=86/L=153  WR=36.0%
- Sharpen: sharpest is ZS=ZS4 (146/153 of losers there)
- **Sharp: n=198  W=52/L=146  WR=26.3%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L04.  `H60=H60a AND T4=T4c AND session_bucket=london`
- Raw: n=214  W=83/L=131  WR=38.8%
- Sharpen: sharpest is T1=T1c (69/131 of losers there)
- **Sharp: n=91  W=22/L=69  WR=24.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  ONLY when 1h trend AGAINST trade

### L05.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=206  W=82/L=124  WR=39.8%
- Sharpen: sharpest is ZS=ZS4 (49/124 of losers there)
- **Sharp: n=68  W=19/L=49  WR=27.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when zscore +1 to +2 overbought

### L06.  `H20=H20e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=198  W=52/L=146  WR=26.3%
- Sharpen: sharpest is T4=T4a (72/146 of losers there)
- **Sharp: n=80  W=8/L=72  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=198  W=52/L=146  WR=26.3%
- Sharpen: sharpest is T4=T4a (72/146 of losers there)
- **Sharp: n=80  W=8/L=72  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L08.  `H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=198  W=66/L=132  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (66/132 of losers there)
- **Sharp: n=74  W=8/L=66  WR=10.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=197  W=63/L=134  WR=32.0%
- Sharpen: sharpest is ZS=ZS5 (67/134 of losers there)
- **Sharp: n=75  W=8/L=67  WR=10.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is ZS=ZS5 (31/105 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=168  W=60/L=108  WR=35.7%
- Sharpen: sharpest is ZS=ZS4 (104/108 of losers there)
- **Sharp: n=140  W=36/L=104  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L12.  `H20=H20e AND H60=H60a AND session_bucket=london`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is direction_exec=short (67/105 of losers there)
- **Sharp: n=85  W=18/L=67  WR=21.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=london  •  ONLY when short

### L13.  `T1=T1c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (57/105 of losers there)
- **Sharp: n=74  W=17/L=57  WR=23.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L14.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is BBP=BBP6 (57/105 of losers there)
- **Sharp: n=74  W=17/L=57  WR=23.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L15.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=166  W=63/L=103  WR=38.0%
- Sharpen: sharpest is ZS=ZS5 (42/103 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is H20=H20a (37/99 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L17.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=156  W=41/L=115  WR=26.3%
- Sharpen: sharpest is ZS=ZS5 (64/115 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS4`
- Raw: n=156  W=59/L=97  WR=37.8%
- Sharpen: sharpest is RSI=RSI5 (42/97 of losers there)
- **Sharp: n=44  W=2/L=42  WR=4.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=154  W=60/L=94  WR=39.0%
- Sharpen: sharpest is ZS=ZS4 (90/94 of losers there)
- **Sharp: n=126  W=36/L=90  WR=28.6%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 60-70 strong  •  ONLY when zscore +1 to +2 overbought

### L20.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=152  W=55/L=97  WR=36.2%
- Sharpen: sharpest is session_bucket=london (24/97 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L21.  `H20=H20e AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=151  W=58/L=93  WR=38.4%
- Sharpen: sharpest is T4=T4a (39/93 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when 4h trend WITH trade

### L22.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=148  W=54/L=94  WR=36.5%
- Sharpen: sharpest is ZS=ZS5 (39/94 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: sharpest is H60=H60a (41/90 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L24.  `H20=H20e AND T1=T1c AND BBP=BBP5`
- Raw: n=142  W=49/L=93  WR=34.5%
- Sharpen: sharpest is session_bucket=london (29/93 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band  •  ONLY when session=london

### L25.  `H20=H20e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=142  W=49/L=93  WR=34.5%
- Sharpen: sharpest is session_bucket=london (29/93 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=london

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/35) | H20e(35/41) |
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
