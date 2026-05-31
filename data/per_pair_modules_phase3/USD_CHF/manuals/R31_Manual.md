# USD_CHF — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,653**  (W=1,749 / L=904)  -  WR: **65.9%**

## Session distribution

- asia: n=1459  W=975/L=484  WR=66.8%
- ny_close: n=621  W=418/L=203  WR=67.3%
- london_open: n=176  W=109/L=67  WR=61.9%
- london: n=125  W=77/L=48  WR=61.6%
- asia_late: n=97  W=56/L=41  WR=57.7%
- ny_open: n=76  W=45/L=31  WR=59.2%
- off_hours: n=70  W=46/L=24  WR=65.7%
- ny_mid: n=29  W=23/L=6  WR=79.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=226  W=196/L=30  WR=86.7%
- Refine: exclude H60=H60a drops 20/30 losers (67%)
- **Final: n=115  W=105/L=10  WR=91.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W02.  `H20=H20a AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=199  W=170/L=29  WR=85.4%
- Refine: exclude direction_exec=long drops 28/29 losers (97%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when long

### W03.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=187  W=159/L=28  WR=85.0%
- Refine: no further refinement
- **Final: n=187  W=159/L=28  WR=85.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=asia

### W04.  `T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=177  W=156/L=21  WR=88.1%
- Refine: exclude H20=H20e drops 9/21 losers (43%)
- **Final: n=139  W=127/L=12  WR=91.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W05.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=164  W=140/L=24  WR=85.4%
- Refine: exclude RSI=RSI5 drops 21/24 losers (88%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W06.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=156  W=145/L=11  WR=92.9%
- Refine: exclude direction_exec=long drops 11/11 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when long

### W07.  `T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=156  W=141/L=15  WR=90.4%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=138  W=129/L=9  WR=93.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -3 to -2 deep oversold

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=143  W=122/L=21  WR=85.3%
- Refine: exclude direction_exec=long drops 21/21 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when long

### W09.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=142  W=123/L=19  WR=86.6%
- Refine: exclude H20=H20e drops 14/19 losers (74%)
- **Final: n=98  W=93/L=5  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W10.  `H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=140  W=120/L=20  WR=85.7%
- Refine: exclude H20=H20e drops 18/20 losers (90%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  AVOID when HTF20 strongly against

### W11.  `H20=H20a AND T4=T4a AND direction_exec=short`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude H60=H60a drops 14/14 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W12.  `H20=H20a AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=136  W=129/L=7  WR=94.9%
- Refine: exclude direction_exec=long drops 7/7 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when long

### W13.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=135  W=123/L=12  WR=91.1%
- Refine: exclude ZS=ZS1 drops 6/12 losers (50%)
- **Final: n=123  W=117/L=6  WR=95.1%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude H20=H20e drops 14/18 losers (78%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W15.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude H20=H20e drops 14/18 losers (78%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 strongly against

### W16.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=132  W=117/L=15  WR=88.6%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=114  W=105/L=9  WR=92.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -3 to -2 deep oversold

### W17.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI4`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude session_bucket=asia drops 14/17 losers (82%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W18.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=121  W=108/L=13  WR=89.3%
- Refine: exclude ZS=ZS1 drops 3/13 losers (23%)
- **Final: n=113  W=103/L=10  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude T4=T4c drops 11/14 losers (79%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude H60=H60a drops 14/14 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF60 aligned WITH trade

### W21.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=114  W=103/L=11  WR=90.4%
- Refine: exclude BBP=BBP2 drops 4/11 losers (36%)
- **Final: n=104  W=97/L=7  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when lower third

### W22.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude session_bucket=asia drops 14/17 losers (82%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W23.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude ZS=ZS1 drops 6/12 losers (50%)
- **Final: n=101  W=95/L=6  WR=94.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W24.  `H20=H20a AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude T4=T4c drops 7/14 losers (50%)
- **Final: n=98  W=91/L=7  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W25.  `T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=112  W=102/L=10  WR=91.1%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=89  W=87/L=2  WR=97.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=170  W=58/L=112  WR=34.1%
- Sharpen: sharpest is H60=H60a (33/112 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L02.  `T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=126  W=40/L=86  WR=31.7%
- Sharpen: sharpest is direction_exec=long (64/86 of losers there)
- **Sharp: n=84  W=20/L=64  WR=23.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when long

### L03.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is H60=H60a (30/74 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L04.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is T1=T1a (20/68 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when 1h trend WITH trade

### L05.  `T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=106  W=28/L=78  WR=26.4%
- Sharpen: sharpest is session_bucket=ny_close (21/78 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L06.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is H60=H60a (21/64 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L07.  `H60=H60e AND T4=T4c AND direction_exec=long`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is H20=H20d (12/61 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L08.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is H20=H20d (12/60 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 mildly against

### L09.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is RSI=RSI4 (34/55 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  ONLY when RSI 50-60 upper neutral

### L10.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=87  W=26/L=61  WR=29.9%
- Sharpen: sharpest is T1=T1a (17/61 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when 1h trend WITH trade

### L11.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (31/51 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L12.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (31/51 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L13.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=84  W=20/L=64  WR=23.8%
- Sharpen: sharpest is session_bucket=ny_close (21/64 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L14.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is H20=H20d (11/51 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 mildly against

### L15.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20d (13/50 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 mildly against

### L16.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is H60=H60a (29/49 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L17.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=70  W=28/L=42  WR=40.0%
- Sharpen: sharpest is H20=H20d (10/42 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 mildly against

### L18.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is H60=H60a (20/39 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 aligned WITH trade

### L19.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is H20=H20d (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 mildly against

### L20.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H20=H20d (6/38 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 mildly against

### L21.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is H60=H60a (26/36 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L22.  `T4=T4c AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is H60=H60a (16/33 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF60 aligned WITH trade

### L23.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is H20=H20a (12/36 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L24.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=51  W=9/L=42  WR=17.6%
- Sharpen: sharpest is T1=T1a (33/42 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when 1h trend WITH trade

### L25.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is direction_exec=long (30/33 of losers there)
- **Sharp: n=41  W=11/L=30  WR=26.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when long

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/36) | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(56/40) | T4c(44/60) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
