# GBP_CHF — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,479**  (W=1,566 / L=913)  -  WR: **63.2%**

## Session distribution

- london_open: n=859  W=541/L=318  WR=63.0%
- ny_mid: n=716  W=453/L=263  WR=63.3%
- london: n=426  W=267/L=159  WR=62.7%
- ny_open: n=257  W=164/L=93  WR=63.8%
- ny_close: n=160  W=102/L=58  WR=63.7%
- asia: n=26  W=16/L=10  WR=61.5%
- asia_late: n=23  W=17/L=6  WR=73.9%
- off_hours: n=12  W=6/L=6  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI5 AND session_bucket=london`
- Raw: n=162  W=138/L=24  WR=85.2%
- Refine: exclude H20=H20a drops 13/24 losers (54%)
- **Final: n=105  W=94/L=11  WR=89.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london  •  AVOID when HTF20 aligned WITH trade

### W02.  `H20=H20e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=142  W=130/L=12  WR=91.5%
- Refine: exclude BBP=BBP3 drops 6/12 losers (50%)
- **Final: n=126  W=120/L=6  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  AVOID when middle of band

### W03.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=134  W=114/L=20  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 7/20 losers (35%)
- **Final: n=111  W=98/L=13  WR=88.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W04.  `H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H20=H20a drops 9/18 losers (50%)
- **Final: n=124  W=115/L=9  WR=92.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H20=H20c drops 11/18 losers (61%)
- **Final: n=97  W=90/L=7  WR=92.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W06.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H20=H20c drops 11/18 losers (61%)
- **Final: n=97  W=90/L=7  WR=92.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W07.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 7/18 losers (39%)
- **Final: n=100  W=89/L=11  WR=89.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W08.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H20=H20c drops 10/18 losers (56%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when HTF20 neutral

### W09.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=120  W=108/L=12  WR=90.0%
- Refine: exclude BBP=BBP3 drops 5/12 losers (42%)
- **Final: n=109  W=102/L=7  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when middle of band

### W10.  `H60=H60a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=119  W=104/L=15  WR=87.4%
- Refine: exclude H20=H20c drops 7/15 losers (47%)
- **Final: n=108  W=100/L=8  WR=92.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 neutral

### W11.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude T4=T4a drops 9/17 losers (53%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend WITH trade

### W12.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude T4=T4a drops 14/16 losers (88%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=london  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20b AND T4=T4c AND BBP=BBP4`
- Raw: n=114  W=104/L=10  WR=91.2%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_close

### W14.  `H20=H20b AND T4=T4c AND ZS=ZS4`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude T1=T1c drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20b AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=110  W=100/L=10  WR=90.9%
- Refine: exclude T1=T1c drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H60=H60d drops 6/16 losers (38%)
- **Final: n=92  W=82/L=10  WR=89.1%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  AVOID when HTF60 mildly against

### W17.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20c drops 9/13 losers (69%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W18.  `H60=H60a AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude H20=H20c drops 6/10 losers (60%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W19.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 7/15 losers (47%)
- **Final: n=92  W=84/L=8  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W20.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when deep above upper band

### W21.  `H20=H20e AND direction_exec=long AND session_bucket=london`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude BBP=BBP3 drops 4/15 losers (27%)
- **Final: n=92  W=81/L=11  WR=88.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=london  •  AVOID when middle of band

### W22.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 6/15 losers (40%)
- **Final: n=88  W=79/L=9  WR=89.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W23.  `H20=H20b AND H60=H60a AND BBP=BBP4`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third  •  AVOID when session=ny_open

### W24.  `H20=H20b AND H60=H60a AND ZS=ZS4`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W25.  `H20=H20b AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=ny_open drops 6/13 losers (46%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=170  W=63/L=107  WR=37.1%
- Sharpen: sharpest is direction_exec=short (34/107 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when short

### L02.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is H60=H60a (28/102 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L03.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: sharpest is T4=T4a (68/95 of losers there)
- **Sharp: n=91  W=23/L=68  WR=25.3%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20a AND H60=H60e AND session_bucket=london_open`
- Raw: n=149  W=53/L=96  WR=35.6%
- Sharpen: sharpest is RSI=RSI4 (50/96 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (37/83 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L06.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is T4=T4a (61/81 of losers there)
- **Sharp: n=84  W=23/L=61  WR=27.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L07.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is H20=H20d (19/76 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L08.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=122  W=43/L=79  WR=35.2%
- Sharpen: sharpest is RSI=RSI4 (33/79 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L09.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=119  W=41/L=78  WR=34.5%
- Sharpen: sharpest is T1=T1a (68/78 of losers there)
- **Sharp: n=91  W=23/L=68  WR=25.3%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L10.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=118  W=43/L=75  WR=36.4%
- Sharpen: sharpest is H20=H20d (19/75 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L11.  `H60=H60a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=117  W=41/L=76  WR=35.0%
- Sharpen: sharpest is H20=H20a (36/76 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L12.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=115  W=45/L=70  WR=39.1%
- Sharpen: sharpest is H20=H20a (37/70 of losers there)
- **Sharp: n=47  W=10/L=37  WR=21.3%**
- **Dir: LONG**  •  upper third; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L13.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is T4=T4a (41/69 of losers there)
- **Sharp: n=45  W=4/L=41  WR=8.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L14.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is T4=T4a (41/69 of losers there)
- **Sharp: n=45  W=4/L=41  WR=8.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is RSI=RSI4 (36/71 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L16.  `T4=T4a AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is H60=H60e (24/68 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; session=london_open  •  ONLY when HTF60 strongly against

### L17.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=111  W=38/L=73  WR=34.2%
- Sharpen: sharpest is H20=H20a (36/73 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L18.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=111  W=38/L=73  WR=34.2%
- Sharpen: sharpest is H20=H20a (36/73 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  ONLY when HTF20 aligned WITH trade

### L19.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=111  W=41/L=70  WR=36.9%
- Sharpen: sharpest is T1=T1a (61/70 of losers there)
- **Sharp: n=84  W=23/L=61  WR=27.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L20.  `H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=109  W=38/L=71  WR=34.9%
- Sharpen: sharpest is H20=H20a (50/71 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H20=H20d (18/66 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L22.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=101  W=28/L=73  WR=27.7%
- Sharpen: sharpest is H20=H20d (19/73 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L23.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is H20=H20a (31/63 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L24.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is H20=H20a (31/63 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L25.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is H20=H20a (31/60 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(42/30) | H20a(29/40) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(56/45) | T4a(44/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/48) | long(47/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
