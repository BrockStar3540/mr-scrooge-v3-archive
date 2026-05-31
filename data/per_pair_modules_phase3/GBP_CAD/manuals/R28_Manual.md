# GBP_CAD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,966**  (W=1,861 / L=1,105)  -  WR: **62.7%**

## Session distribution

- london_open: n=1678  W=1068/L=610  WR=63.6%
- ny_open: n=663  W=413/L=250  WR=62.3%
- london: n=366  W=227/L=139  WR=62.0%
- ny_mid: n=127  W=77/L=50  WR=60.6%
- asia_late: n=85  W=46/L=39  WR=54.1%
- asia: n=47  W=30/L=17  WR=63.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=182  W=157/L=25  WR=86.3%
- Refine: exclude ZS=ZS5 drops 13/25 losers (52%)
- **Final: n=157  W=145/L=12  WR=92.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W02.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=151  W=144/L=7  WR=95.4%
- Refine: exclude H20=H20a drops 4/7 losers (57%)
- **Final: n=107  W=104/L=3  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W03.  `H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=143  W=125/L=18  WR=87.4%
- Refine: exclude H20=H20a drops 15/18 losers (83%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=143  W=125/L=18  WR=87.4%
- Refine: exclude H20=H20a drops 15/18 losers (83%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=139  W=132/L=7  WR=95.0%
- Refine: exclude direction_exec=long drops 7/7 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when long

### W06.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=139  W=132/L=7  WR=95.0%
- Refine: exclude direction_exec=long drops 7/7 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when long

### W07.  `H20=H20d AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=139  W=126/L=13  WR=90.6%
- Refine: exclude RSI=RSI4 drops 13/13 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W08.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude session_bucket=london_open drops 19/19 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W09.  `H60=H60d AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude BBP=BBP6 drops 14/20 losers (70%)
- **Final: n=115  W=109/L=6  WR=94.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when deep above upper band

### W10.  `H20=H20d AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=131  W=114/L=17  WR=87.0%
- Refine: exclude RSI=RSI4 drops 17/17 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=127  W=121/L=6  WR=95.3%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong; session=london_open  •  AVOID when 1h trend WITH trade

### W13.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought; session=london_open  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20b AND T4=T4c AND direction_exec=long`
- Raw: n=121  W=109/L=12  WR=90.1%
- Refine: exclude H60=H60a drops 6/12 losers (50%)
- **Final: n=115  W=109/L=6  WR=94.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  AVOID when HTF60 aligned WITH trade

### W15.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=111  W=104/L=7  WR=93.7%
- Refine: exclude H20=H20c drops 3/7 losers (43%)
- **Final: n=108  W=104/L=4  WR=96.3%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W16.  `H20=H20c AND T4=T4a AND RSI=RSI4`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude H60=H60b drops 5/13 losers (38%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W17.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude BBP=BBP5 drops 14/16 losers (88%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W18.  `H20=H20b AND H60=H60e AND T4=T4c`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude T1=T1c drops 10/15 losers (67%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when 1h trend AGAINST trade

### W19.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=103  W=97/L=6  WR=94.2%
- Refine: exclude H20=H20c drops 3/6 losers (50%)
- **Final: n=100  W=97/L=3  WR=97.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W20.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude H60=H60b drops 6/14 losers (43%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 slightly aligned

### W21.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude H20=H20c drops 3/7 losers (43%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 neutral

### W22.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=100  W=94/L=6  WR=94.0%
- Refine: exclude H20=H20c drops 3/6 losers (50%)
- **Final: n=97  W=94/L=3  WR=96.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 neutral

### W23.  `H20=H20b AND T1=T1a AND T4=T4c`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude H60=H60a drops 6/11 losers (55%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF60 aligned WITH trade

### W24.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude RSI=RSI3 drops 5/13 losers (38%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W25.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=93  W=91/L=2  WR=97.8%
- Refine: exclude session_bucket=london_open drops 2/2 losers (100%)
- **Final: n=84  W=84/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=161  W=57/L=104  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=161  W=57/L=104  WR=35.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade

### L02.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=152  W=51/L=101  WR=33.6%
- Sharpen: sharpest is H20=H20d (53/101 of losers there)
- **Sharp: n=53  W=0/L=53  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L03.  `H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=141  W=44/L=97  WR=31.2%
- Sharpen: sharpest is H20=H20d (30/97 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is H20=H20a (18/83 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L05.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=118  W=36/L=82  WR=30.5%
- Sharpen: sharpest is H20=H20d (45/82 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L06.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=118  W=36/L=82  WR=30.5%
- Sharpen: sharpest is H20=H20d (45/82 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L07.  `H20=H20d AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=117  W=45/L=72  WR=38.5%
- Sharpen: sharpest is RSI=RSI5 (45/72 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L08.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=111  W=38/L=73  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_open (34/73 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L09.  `H20=H20d AND T4=T4a AND direction_exec=short`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is H60=H60a (57/67 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L10.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is T4=T4a (46/67 of losers there)
- **Sharp: n=54  W=8/L=46  WR=14.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend WITH trade

### L11.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is T4=T4a (46/67 of losers there)
- **Sharp: n=54  W=8/L=46  WR=14.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend WITH trade

### L12.  `H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=101  W=31/L=70  WR=30.7%
- Sharpen: sharpest is H20=H20d (30/70 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L13.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=101  W=33/L=68  WR=32.7%
- Sharpen: sharpest is T1=T1a (23/68 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: SHORT**  •  upper third; session=ny_open  •  ONLY when 1h trend WITH trade

### L14.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is direction_exec=short (58/61 of losers there)
- **Sharp: n=85  W=27/L=58  WR=31.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when short

### L15.  `H20=H20b AND T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=98  W=35/L=63  WR=35.7%
- Sharpen: sharpest is RSI=RSI5 (23/63 of losers there)
- **Sharp: n=24  W=1/L=23  WR=4.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20d AND H60=H60a AND T4=T4a`
- Raw: n=89  W=26/L=63  WR=29.2%
- Sharpen: sharpest is RSI=RSI5 (30/63 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L17.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=89  W=28/L=61  WR=31.5%
- Sharpen: sharpest is BBP=BBP4 (39/61 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when upper third

### L18.  `H20=H20d AND H60=H60a AND BBP=BBP4`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is RSI=RSI5 (42/56 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; upper third  •  ONLY when RSI 60-70 strong

### L19.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=88  W=16/L=72  WR=18.2%
- Sharpen: sharpest is H20=H20d (42/72 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L20.  `H60=H60c AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=88  W=28/L=60  WR=31.8%
- Sharpen: sharpest is H20=H20a (21/60 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20d AND T1=T1c AND T4=T4a`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is H60=H60a (53/58 of losers there)
- **Sharp: n=63  W=10/L=53  WR=15.9%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is session_bucket=london_open (30/58 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L23.  `H20=H20c AND T4=T4c AND RSI=RSI4`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is H60=H60e (20/59 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L24.  `H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (29/52 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (40/52 of losers there)
- **Sharp: n=54  W=14/L=40  WR=25.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=london_open  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(28/20) | H20a(20/27) |
| H60 | H60d(16/11) | — |
| T1 | T1a(56/41) | T1c(44/59) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
