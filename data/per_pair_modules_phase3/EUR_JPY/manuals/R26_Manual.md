# EUR_JPY — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,808**  (W=2,404 / L=1,404)  -  WR: **63.1%**

## Session distribution

- asia: n=1361  W=862/L=499  WR=63.3%
- ny_close: n=810  W=531/L=279  WR=65.6%
- london: n=440  W=286/L=154  WR=65.0%
- ny_open: n=378  W=241/L=137  WR=63.8%
- ny_mid: n=277  W=160/L=117  WR=57.8%
- london_open: n=257  W=165/L=92  WR=64.2%
- asia_late: n=167  W=88/L=79  WR=52.7%
- off_hours: n=118  W=71/L=47  WR=60.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=126  W=112/L=14  WR=88.9%
- Refine: exclude H20=H20d drops 6/14 losers (43%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london  •  AVOID when HTF20 mildly against

### W02.  `BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude H20=H20d drops 9/17 losers (53%)
- **Final: n=103  W=95/L=8  WR=92.2%**
- **Dir: SHORT**  •  upper third; session=london  •  AVOID when HTF20 mildly against

### W03.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude H20=H20d drops 6/14 losers (43%)
- **Final: n=103  W=95/L=8  WR=92.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=london  •  AVOID when HTF20 mildly against

### W04.  `H60=H60e AND BBP=BBP4 AND session_bucket=london`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude H20=H20b drops 11/16 losers (69%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W05.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20d drops 6/10 losers (60%)
- **Final: n=101  W=97/L=4  WR=96.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 mildly against

### W06.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W07.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W08.  `H20=H20b AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W09.  `T1=T1c AND ZS=ZS4 AND session_bucket=london`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude H20=H20d drops 4/10 losers (40%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W10.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude H20=H20d drops 4/10 losers (40%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W11.  `H20=H20a AND H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude RSI=RSI5 drops 14/14 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W12.  `ZS=ZS4 AND direction_exec=short AND session_bucket=london`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H20=H20d drops 7/13 losers (54%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W13.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=london`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H20=H20d drops 7/13 losers (54%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 mildly against

### W14.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude H20=H20b drops 4/9 losers (44%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W15.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=94  W=82/L=12  WR=87.2%
- Refine: exclude H20=H20d drops 9/12 losers (75%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=london  •  AVOID when HTF20 mildly against

### W16.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=london`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20b drops 4/10 losers (40%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 slightly aligned

### W17.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=91  W=85/L=6  WR=93.4%
- Refine: exclude H20=H20b drops 4/6 losers (67%)
- **Final: n=87  W=85/L=2  WR=97.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=london  •  AVOID when HTF20 slightly aligned

### W18.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W19.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude H20=H20d drops 6/9 losers (67%)
- **Final: n=74  W=71/L=3  WR=95.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=london  •  AVOID when HTF20 mildly against

### W20.  `H20=H20e AND direction_exec=short AND session_bucket=london`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude ZS=ZS3 drops 9/11 losers (82%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude ZS=ZS3 drops 9/11 losers (82%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60e AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=91  W=79/L=12  WR=86.8%
- Refine: exclude H20=H20d drops 12/12 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 mildly against

### W23.  `H20=H20e AND H60=H60e AND session_bucket=london`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/9 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=london`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/9 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude ZS=ZS3 drops 9/9 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=238  W=94/L=144  WR=39.5%
- Sharpen: sharpest is session_bucket=london (32/144 of losers there)
- **Sharp: n=34  W=2/L=32  WR=5.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=london

### L02.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=191  W=74/L=117  WR=38.7%
- Sharpen: sharpest is session_bucket=london (23/117 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=london

### L03.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=191  W=74/L=117  WR=38.7%
- Sharpen: sharpest is session_bucket=london (23/117 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=london

### L04.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=186  W=73/L=113  WR=39.2%
- Sharpen: sharpest is H20=H20e (27/113 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L05.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=163  W=62/L=101  WR=38.0%
- Sharpen: sharpest is session_bucket=london (20/101 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=london

### L06.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=148  W=59/L=89  WR=39.9%
- Sharpen: sharpest is T1=T1c (18/89 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L07.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=129  W=48/L=81  WR=37.2%
- Sharpen: sharpest is T1=T1c (18/81 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L08.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is T4=T4c (46/66 of losers there)
- **Sharp: n=65  W=19/L=46  WR=29.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L09.  `H20=H20d AND H60=H60e AND direction_exec=short`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is T1=T1c (52/62 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against  •  ONLY when 1h trend AGAINST trade

### L10.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=96  W=37/L=59  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_open (22/59 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L11.  `H60=H60e AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is T4=T4c (42/58 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is T4=T4c (42/58 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is BBP=BBP5 (17/61 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when just touched upper band

### L14.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=89  W=16/L=73  WR=18.0%
- Sharpen: sharpest is H60=H60e (29/73 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L15.  `T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=89  W=32/L=57  WR=36.0%
- Sharpen: sharpest is RSI=RSI5 (44/57 of losers there)
- **Sharp: n=60  W=16/L=44  WR=26.7%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20e AND H60=H60a AND ZS=ZS5`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is direction_exec=short (16/57 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when short

### L17.  `T1=T1a AND BBP=BBP4 AND session_bucket=london`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is H60=H60a (34/53 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=london  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20d AND T1=T1c AND session_bucket=asia`
- Raw: n=85  W=33/L=52  WR=38.8%
- Sharpen: sharpest is H60=H60e (52/52 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 strongly against

### L19.  `H20=H20d AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=85  W=33/L=52  WR=38.8%
- Sharpen: sharpest is H60=H60e (52/52 of losers there)
- **Sharp: n=65  W=13/L=52  WR=20.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 strongly against

### L20.  `H20=H20d AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=84  W=27/L=57  WR=32.1%
- Sharpen: sharpest is T4=T4a (36/57 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; session=asia  •  ONLY when 4h trend WITH trade

### L21.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is H60=H60a (34/50 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=london  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=77  W=25/L=52  WR=32.5%
- Sharpen: sharpest is BBP=BBP5 (14/52 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when just touched upper band

### L23.  `H20=H20e AND H60=H60a AND BBP=BBP5`
- Raw: n=75  W=27/L=48  WR=36.0%
- Sharpen: sharpest is direction_exec=short (16/48 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; just touched upper band  •  ONLY when short

### L24.  `H20=H20e AND H60=H60a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=75  W=27/L=48  WR=36.0%
- Sharpen: sharpest is direction_exec=short (16/48 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when short

### L25.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (44/45 of losers there)
- **Sharp: n=60  W=16/L=44  WR=26.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

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
