# NZD_CAD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,954**  (W=1,915 / L=1,039)  -  WR: **64.8%**

## Session distribution

- asia: n=998  W=636/L=362  WR=63.7%
- ny_close: n=528  W=346/L=182  WR=65.5%
- off_hours: n=368  W=216/L=152  WR=58.7%
- ny_open: n=262  W=189/L=73  WR=72.1%
- london_open: n=251  W=167/L=84  WR=66.5%
- london: n=212  W=143/L=69  WR=67.5%
- asia_late: n=170  W=111/L=59  WR=65.3%
- ny_mid: n=165  W=107/L=58  WR=64.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=150  W=143/L=7  WR=95.3%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=142  W=139/L=3  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london

### W02.  `H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=149  W=128/L=21  WR=85.9%
- Refine: exclude ZS=ZS3 drops 7/21 losers (33%)
- **Final: n=123  W=109/L=14  WR=88.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W03.  `H20=H20a AND T1=T1c AND RSI=RSI4`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude H60=H60c drops 17/21 losers (81%)
- **Final: n=112  W=108/L=4  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF60 neutral

### W04.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=134  W=132/L=2  WR=98.5%
- Refine: exclude strategy_id=charlie_compression_breakout drops 2/2 losers (100%)
- **Final: n=128  W=128/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when strategy=charlie_compression_breakout

### W05.  `H60=H60e AND T1=T1c AND ZS=ZS3`
- Raw: n=133  W=114/L=19  WR=85.7%
- Refine: exclude H20=H20e drops 17/19 losers (89%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when HTF20 strongly against

### W06.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=131  W=122/L=9  WR=93.1%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=118  W=116/L=2  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF20 neutral

### W07.  `T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=124  W=114/L=10  WR=91.9%
- Refine: exclude ZS=ZS4 drops 8/10 losers (80%)
- **Final: n=82  W=80/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore +1 to +2 overbought

### W08.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=123  W=108/L=15  WR=87.8%
- Refine: exclude H20=H20c drops 4/15 losers (27%)
- **Final: n=113  W=102/L=11  WR=90.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W09.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=114  W=112/L=2  WR=98.2%
- Refine: exclude strategy_id=charlie_compression_breakout drops 2/2 losers (100%)
- **Final: n=108  W=108/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when strategy=charlie_compression_breakout

### W10.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude H60=H60d drops 5/15 losers (33%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 mildly against

### W11.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude H60=H60d drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 mildly against

### W12.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude H60=H60d drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  AVOID when HTF60 mildly against

### W13.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude H60=H60d drops 5/15 losers (33%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 mildly against

### W14.  `T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude ZS=ZS4 drops 10/13 losers (77%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H60=H60d drops 5/15 losers (33%)
- **Final: n=90  W=80/L=10  WR=88.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 mildly against

### W16.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H60=H60d drops 5/15 losers (33%)
- **Final: n=90  W=80/L=10  WR=88.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  AVOID when HTF60 mildly against

### W17.  `H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude H20=H20e drops 12/12 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W18.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude H20=H20e drops 12/12 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W19.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=london_open drops 8/14 losers (57%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W20.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=london_open

### W21.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W22.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=96  W=92/L=4  WR=95.8%
- Refine: exclude session_bucket=london drops 3/4 losers (75%)
- **Final: n=89  W=88/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W23.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W24.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=91  W=85/L=6  WR=93.4%
- Refine: exclude H60=H60c drops 5/6 losers (83%)
- **Final: n=81  W=80/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W25.  `H20=H20a AND T1=T1c AND direction_exec=long`
- Raw: n=89  W=84/L=5  WR=94.4%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=81  W=80/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND T4=T4c`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is H60=H60a (55/73 of losers there)
- **Sharp: n=66  W=11/L=55  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L02.  `T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=94  W=34/L=60  WR=36.2%
- Sharpen: sharpest is direction_exec=long (33/60 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when long

### L03.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=85  W=28/L=57  WR=32.9%
- Sharpen: sharpest is ZS=ZS5 (19/57 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=85  W=30/L=55  WR=35.3%
- Sharpen: sharpest is T4=T4c (12/55 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L05.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is H60=H60b (11/51 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF60 slightly aligned

### L06.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=81  W=30/L=51  WR=37.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close

### L07.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS5 (19/48 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=79  W=17/L=62  WR=21.5%
- Sharpen: sharpest is direction_exec=long (42/62 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when long

### L09.  `H60=H60c AND T1=T1c AND session_bucket=asia`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is BBP=BBP4 (29/52 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when upper third

### L10.  `H60=H60c AND T4=T4c AND session_bucket=asia`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is BBP=BBP4 (29/52 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L11.  `H60=H60c AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is BBP=BBP4 (29/52 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF60 neutral; session=asia  •  ONLY when upper third

### L12.  `H60=H60c AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is BBP=BBP4 (29/52 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L13.  `H60=H60c AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is BBP=BBP4 (29/52 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when upper third

### L14.  `H60=H60c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=27/L=52  WR=34.2%
- Sharpen: sharpest is BBP=BBP4 (29/52 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L15.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=73  W=12/L=61  WR=16.4%
- Sharpen: sharpest is session_bucket=asia (23/61 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=asia

### L16.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is H60=H60a (36/45 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L17.  `H60=H60e AND T1=T1a AND session_bucket=off_hours`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is ZS=ZS4 (20/45 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=off_hours  •  ONLY when zscore +1 to +2 overbought

### L18.  `H60=H60c AND T1=T1c AND BBP=BBP4`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/45 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; upper third  •  ONLY when session=asia

### L19.  `H60=H60c AND T4=T4c AND BBP=BBP4`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/45 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; upper third  •  ONLY when session=asia

### L20.  `H60=H60c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/45 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF60 neutral; upper third  •  ONLY when session=asia

### L21.  `H60=H60c AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/45 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=asia

### L22.  `H60=H60c AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/45 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade; upper third  •  ONLY when session=asia

### L23.  `H60=H60c AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/45 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend AGAINST trade; upper third  •  ONLY when session=asia

### L24.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=66  W=11/L=55  WR=16.7%
- Sharpen: sharpest is direction_exec=long (35/55 of losers there)
- **Sharp: n=38  W=3/L=35  WR=7.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when long

### L25.  `H20=H20e AND H60=H60d AND RSI=RSI5`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (17/44 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 60-70 strong  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(55/46) | T1a(45/54) |
| T4 | T4a(52/46) | T4c(48/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
