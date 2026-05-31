# USD_CHF — R27 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,563**  (W=1,039 / L=524)  -  WR: **66.5%**

## Session distribution

- ny_mid: n=353  W=222/L=131  WR=62.9%
- london_open: n=340  W=237/L=103  WR=69.7%
- ny_close: n=306  W=192/L=114  WR=62.7%
- asia: n=272  W=184/L=88  WR=67.6%
- ny_open: n=126  W=97/L=29  WR=77.0%
- london: n=117  W=79/L=38  WR=67.5%
- off_hours: n=29  W=17/L=12  WR=58.6%
- asia_late: n=20  W=11/L=9  WR=55.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W02.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W03.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W04.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W05.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H20=H20e drops 10/12 losers (83%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W06.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS5`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude RSI=RSI5 drops 6/6 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W07.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=79  W=73/L=6  WR=92.4%
- Refine: exclude RSI=RSI5 drops 6/6 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W08.  `H20=H20a AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W09.  `H60=H60a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band  •  AVOID when HTF20 strongly against

### W10.  `H60=H60a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W11.  `H60=H60a AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude H20=H20e drops 5/7 losers (71%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W12.  `H20=H20a AND H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=64  W=60/L=4  WR=93.8%
- Refine: exclude RSI=RSI5 drops 4/4 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W13.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude H20=H20e drops 8/8 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W14.  `H60=H60a AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20e drops 5/7 losers (71%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W15.  `H60=H60a AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20e drops 5/7 losers (71%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W16.  `H20=H20a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 7/9 losers (78%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep above upper band  •  AVOID when session=ny_close

### W17.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude H60=H60a drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W18.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude session_bucket=london_open drops 5/8 losers (62%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W19.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude session_bucket=london_open drops 5/8 losers (62%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W20.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 strongly against

### W21.  `H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when session=asia

### W22.  `H20=H20d AND H60=H60a AND T4=T4c`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20d AND H60=H60a AND direction_exec=short`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20a AND T1=T1c AND BBP=BBP6`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude T4=T4a drops 7/9 losers (78%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep above upper band  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20d AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is RSI=RSI4 (29/50 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L02.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_mid (9/40 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  ONLY when session=ny_mid

### L03.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_mid (9/40 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L04.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60e (29/38 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L05.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=53  W=14/L=39  WR=26.4%
- Sharpen: sharpest is RSI=RSI4 (23/39 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L06.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is H60=H60e (13/35 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L07.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=51  W=14/L=37  WR=27.5%
- Sharpen: sharpest is T4=T4a (29/37 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L08.  `BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=45  W=16/L=29  WR=35.6%
- Sharpen: sharpest is H20=H20e (7/29 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: LONG**  •  upper third; session=asia  •  ONLY when HTF20 strongly against

### L09.  `T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is RSI=RSI4 (16/30 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is RSI=RSI4 (14/30 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L11.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=44  W=14/L=30  WR=31.8%
- Sharpen: sharpest is RSI=RSI4 (16/30 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L12.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is H20=H20a (25/26 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (14/28 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 50-60 upper neutral

### L14.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is H20=H20e (7/27 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 strongly against

### L15.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is H20=H20e (7/27 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=41  W=12/L=29  WR=29.3%
- Sharpen: sharpest is RSI=RSI4 (23/29 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L17.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is H60=H60e (13/27 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=40  W=14/L=26  WR=35.0%
- Sharpen: sharpest is T4=T4a (22/26 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L19.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=40  W=14/L=26  WR=35.0%
- Sharpen: sharpest is T1=T1a (20/26 of losers there)
- **Sharp: n=28  W=8/L=20  WR=28.6%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=asia  •  ONLY when 1h trend WITH trade

### L20.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=39  W=13/L=26  WR=33.3%
- Sharpen: sharpest is H60=H60e (13/26 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L21.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=38  W=13/L=25  WR=34.2%
- Sharpen: sharpest is session_bucket=ny_close (14/25 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_close

### L22.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=37  W=10/L=27  WR=27.0%
- Sharpen: sharpest is session_bucket=london_open (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L23.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=37  W=13/L=24  WR=35.1%
- Sharpen: sharpest is H60=H60e (13/24 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L24.  `T4=T4a AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=37  W=13/L=24  WR=35.1%
- Sharpen: sharpest is H20=H20e (7/24 of losers there)
- **Sharp: n=8  W=1/L=7  WR=12.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 strongly against

### L25.  `H20=H20e AND H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=37  W=14/L=23  WR=37.8%
- Sharpen: sharpest is direction_exec=short (13/23 of losers there)
- **Sharp: n=17  W=4/L=13  WR=23.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when short

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
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
