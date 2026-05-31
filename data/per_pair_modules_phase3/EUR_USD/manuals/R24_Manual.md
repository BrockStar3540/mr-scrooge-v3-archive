# EUR_USD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,103**  (W=1,946 / L=1,157)  -  WR: **62.7%**

## Session distribution

- asia: n=1065  W=671/L=394  WR=63.0%
- london_open: n=433  W=284/L=149  WR=65.6%
- ny_close: n=424  W=261/L=163  WR=61.6%
- ny_open: n=384  W=236/L=148  WR=61.5%
- london: n=255  W=168/L=87  WR=65.9%
- ny_mid: n=240  W=141/L=99  WR=58.8%
- asia_late: n=219  W=127/L=92  WR=58.0%
- off_hours: n=83  W=58/L=25  WR=69.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60d AND T1=T1a AND RSI=RSI5`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/16 losers (38%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W02.  `H20=H20a AND H60=H60d AND RSI=RSI5 AND direction_exec=long`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude session_bucket=london_open drops 6/16 losers (38%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=london_open

### W03.  `H20=H20d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude T1=T1a drops 5/18 losers (28%)
- **Final: n=115  W=102/L=13  WR=88.7%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 60-70 strong  •  AVOID when 1h trend WITH trade

### W04.  `H20=H20d AND T4=T4c AND RSI=RSI5`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude BBP=BBP6 drops 6/16 losers (38%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W05.  `H20=H20d AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude BBP=BBP6 drops 6/16 losers (38%)
- **Final: n=104  W=94/L=10  WR=90.4%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W06.  `H20=H20d AND T1=T1c AND RSI=RSI5`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude ZS=ZS4 drops 8/13 losers (62%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W07.  `H20=H20d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude ZS=ZS4 drops 8/13 losers (62%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20d AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=111  W=100/L=11  WR=90.1%
- Refine: exclude ZS=ZS4 drops 8/11 losers (73%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore +1 to +2 overbought

### W09.  `T4=T4c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI6 drops 9/14 losers (64%)
- **Final: n=79  W=74/L=5  WR=93.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when RSI 70-80 overbought

### W10.  `H20=H20a AND H60=H60e AND RSI=RSI6`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude session_bucket=ny_close drops 6/7 losers (86%)
- **Final: n=78  W=77/L=1  WR=98.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when session=ny_close

### W11.  `H60=H60e AND T1=T1a AND RSI=RSI6`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_close drops 6/6 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_close

### W12.  `H60=H60e AND RSI=RSI6 AND direction_exec=long`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_close drops 6/6 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 70-80 overbought  •  AVOID when session=ny_close

### W13.  `H60=H60e AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=ny_close drops 6/6 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_close

### W14.  `H20=H20d AND T1=T1c AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude T4=T4a drops 2/11 losers (18%)
- **Final: n=75  W=66/L=9  WR=88.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W15.  `H20=H20d AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude T4=T4a drops 2/11 losers (18%)
- **Final: n=75  W=66/L=9  WR=88.0%**
- **Dir: SHORT**  •  HTF20 mildly against; session=asia  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20d AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude T4=T4a drops 2/11 losers (18%)
- **Final: n=75  W=66/L=9  WR=88.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20a AND H60=H60d AND session_bucket=asia`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude BBP=BBP2 drops 5/9 losers (56%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; session=asia  •  AVOID when lower third

### W18.  `H20=H20d AND T4=T4c AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W19.  `H20=H20d AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W20.  `H20=H20d AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W21.  `H20=H20d AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W22.  `H20=H20d AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W23.  `H20=H20d AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude BBP=BBP4 drops 6/9 losers (67%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W24.  `H60=H60e AND T4=T4a AND RSI=RSI6`
- Raw: n=73  W=67/L=6  WR=91.8%
- Refine: exclude session_bucket=ny_close drops 6/6 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_close

### W25.  `H20=H20a AND H60=H60e AND T1=T1a AND RSI=RSI6`
- Raw: n=73  W=67/L=6  WR=91.8%
- Refine: exclude session_bucket=ny_close drops 6/6 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=145  W=55/L=90  WR=37.9%
- Sharpen: sharpest is ZS=ZS5 (27/90 of losers there)
- **Sharp: n=35  W=8/L=27  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H20=H20b AND T1=T1a AND direction_exec=long`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: sharpest is RSI=RSI5 (66/86 of losers there)
- **Sharp: n=92  W=26/L=66  WR=28.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade  •  ONLY when RSI 60-70 strong

### L03.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (27/85 of losers there)
- **Sharp: n=35  W=8/L=27  WR=22.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H20=H20e AND H60=H60b AND RSI=RSI5`
- Raw: n=126  W=50/L=76  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (27/76 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; RSI 60-70 strong  •  ONLY when session=asia

### L05.  `H20=H20e AND H60=H60b AND T4=T4c AND RSI=RSI5`
- Raw: n=126  W=50/L=76  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (27/76 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L06.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=125  W=46/L=79  WR=36.8%
- Sharpen: sharpest is T4=T4a (41/79 of losers there)
- **Sharp: n=55  W=14/L=41  WR=25.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20e AND T1=T1c AND RSI=RSI6`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is H60=H60a (43/76 of losers there)
- **Sharp: n=43  W=0/L=43  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 aligned WITH trade

### L08.  `H20=H20e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is H60=H60a (43/76 of losers there)
- **Sharp: n=43  W=0/L=43  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought  •  ONLY when HTF60 aligned WITH trade

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is H60=H60a (43/76 of losers there)
- **Sharp: n=43  W=0/L=43  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is H60=H60a (43/76 of losers there)
- **Sharp: n=43  W=0/L=43  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 aligned WITH trade

### L11.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is H60=H60a (43/76 of losers there)
- **Sharp: n=43  W=0/L=43  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 aligned WITH trade

### L12.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is RSI=RSI5 (63/78 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is RSI=RSI5 (63/78 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=113  W=42/L=71  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (24/71 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20b AND RSI=RSI5 AND direction_exec=long`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is T1=T1a (66/66 of losers there)
- **Sharp: n=92  W=26/L=66  WR=28.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L16.  `H20=H20b AND T4=T4a AND RSI=RSI5`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is T1=T1a (63/63 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L17.  `H20=H20b AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is T1=T1a (63/63 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L18.  `H20=H20b AND T1=T1a AND RSI=RSI5`
- Raw: n=92  W=26/L=66  WR=28.3%
- Sharpen: sharpest is H60=H60e (26/66 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L19.  `H20=H20b AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=92  W=26/L=66  WR=28.3%
- Sharpen: sharpest is H60=H60e (26/66 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L20.  `H20=H20e AND H60=H60b AND T1=T1c AND RSI=RSI5`
- Raw: n=92  W=34/L=58  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (34/58 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when upper third

### L21.  `H20=H20e AND H60=H60b AND RSI=RSI5 AND direction_exec=short`
- Raw: n=92  W=34/L=58  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (34/58 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned; RSI 60-70 strong  •  ONLY when upper third

### L22.  `T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is H20=H20a (15/54 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is H60=H60b (17/53 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  ONLY when HTF60 slightly aligned

### L24.  `H20=H20b AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=86  W=23/L=63  WR=26.7%
- Sharpen: sharpest is H60=H60e (26/63 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L25.  `BBP=BBP6 AND ZS=ZS6 AND direction_exec=short`
- Raw: n=82  W=31/L=51  WR=37.8%
- Sharpen: sharpest is H20=H20c (13/51 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  deep above upper band; zscore >+3 extreme  •  ONLY when HTF20 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/36) | H20e(37/46) |
| H60 | — | — |
| T1 | T1a(54/47) | T1c(46/52) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/45) | short(44/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
