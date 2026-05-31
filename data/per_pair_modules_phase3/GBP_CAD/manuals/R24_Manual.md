# GBP_CAD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,580**  (W=2,286 / L=1,294)  -  WR: **63.9%**

## Session distribution

- asia: n=1401  W=904/L=497  WR=64.5%
- ny_close: n=929  W=589/L=340  WR=63.4%
- london_open: n=359  W=223/L=136  WR=62.1%
- off_hours: n=301  W=187/L=114  WR=62.1%
- asia_late: n=271  W=186/L=85  WR=68.6%
- london: n=180  W=117/L=63  WR=65.0%
- ny_open: n=71  W=45/L=26  WR=63.4%
- ny_mid: n=68  W=35/L=33  WR=51.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=143  W=126/L=17  WR=88.1%
- Refine: exclude H60=H60e drops 12/17 losers (71%)
- **Final: n=114  W=109/L=5  WR=95.6%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W02.  `H20=H20a AND H60=H60c AND direction_exec=long`
- Raw: n=135  W=124/L=11  WR=91.9%
- Refine: exclude BBP=BBP5 drops 4/11 losers (36%)
- **Final: n=121  W=114/L=7  WR=94.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 neutral  •  AVOID when just touched upper band

### W03.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia_late`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude H60=H60a drops 19/19 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia_late  •  AVOID when HTF60 aligned WITH trade

### W04.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude H60=H60a drops 19/19 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia_late  •  AVOID when HTF60 aligned WITH trade

### W05.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude H60=H60a drops 19/19 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia_late  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude T1=T1a drops 18/18 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_close  •  AVOID when 1h trend WITH trade

### W07.  `H60=H60d AND T1=T1c AND session_bucket=ny_close`
- Raw: n=131  W=120/L=11  WR=91.6%
- Refine: exclude BBP=BBP6 drops 5/11 losers (45%)
- **Final: n=126  W=120/L=6  WR=95.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when deep above upper band

### W08.  `H20=H20a AND H60=H60c AND RSI=RSI5`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude session_bucket=ny_mid drops 9/18 losers (50%)
- **Final: n=122  W=113/L=9  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; RSI 60-70 strong  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude H60=H60b drops 13/18 losers (72%)
- **Final: n=108  W=103/L=5  WR=95.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when HTF60 slightly aligned

### W10.  `H20=H20a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude T1=T1a drops 18/18 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; session=ny_close  •  AVOID when 1h trend WITH trade

### W11.  `H20=H20a AND H60=H60c AND T1=T1a`
- Raw: n=121  W=111/L=10  WR=91.7%
- Refine: exclude BBP=BBP5 drops 4/10 losers (40%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when just touched upper band

### W12.  `H20=H20a AND H60=H60c AND T1=T1a AND direction_exec=long`
- Raw: n=121  W=111/L=10  WR=91.7%
- Refine: exclude BBP=BBP5 drops 4/10 losers (40%)
- **Final: n=107  W=101/L=6  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when just touched upper band

### W13.  `H20=H20a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 1h trend WITH trade

### W15.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude RSI=RSI5 drops 15/15 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when RSI 60-70 strong

### W16.  `H20=H20a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 1h trend WITH trade

### W17.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude H60=H60e drops 12/16 losers (75%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W18.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude H60=H60e drops 12/16 losers (75%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF60 strongly against

### W19.  `H20=H20a AND H60=H60c AND T1=T1a AND RSI=RSI5`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude BBP=BBP5 drops 4/8 losers (50%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W20.  `H20=H20a AND H60=H60c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude BBP=BBP5 drops 4/8 losers (50%)
- **Final: n=99  W=95/L=4  WR=96.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 neutral; RSI 60-70 strong  •  AVOID when just touched upper band

### W21.  `H20=H20a AND T1=T1c AND ZS=ZS4`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude T4=T4c drops 10/14 losers (71%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude T4=T4c drops 10/14 losers (71%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W23.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W24.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W25.  `T4=T4a AND RSI=RSI5 AND ZS=ZS2`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 5/12 losers (42%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore -2 to -1 oversold  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60b AND T4=T4c`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (23/90 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when deep above upper band

### L02.  `H20=H20e AND H60=H60b AND direction_exec=short`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (23/90 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned  •  ONLY when deep above upper band

### L03.  `H20=H20e AND H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (23/90 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when deep above upper band

### L04.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is H60=H60e (29/84 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_close  •  ONLY when HTF60 strongly against

### L05.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is H60=H60e (29/84 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_close  •  ONLY when HTF60 strongly against

### L06.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=121  W=42/L=79  WR=34.7%
- Sharpen: sharpest is H60=H60e (25/79 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF60 strongly against

### L07.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=121  W=42/L=79  WR=34.7%
- Sharpen: sharpest is H60=H60e (25/79 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF60 strongly against

### L08.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=115  W=38/L=77  WR=33.0%
- Sharpen: sharpest is H60=H60c (34/77 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  ONLY when HTF60 neutral

### L09.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is BBP=BBP4 (29/69 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  ONLY when upper third

### L10.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is BBP=BBP4 (29/69 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  ONLY when upper third

### L11.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is BBP=BBP4 (29/69 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when upper third

### L12.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=104  W=35/L=69  WR=33.7%
- Sharpen: sharpest is H20=H20c (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF20 neutral

### L13.  `H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=102  W=33/L=69  WR=32.4%
- Sharpen: sharpest is RSI=RSI5 (40/69 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L14.  `T4=T4c AND RSI=RSI5 AND session_bucket=off_hours`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is H20=H20e (39/59 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=off_hours  •  ONLY when HTF20 strongly against

### L15.  `H60=H60b AND T1=T1a AND BBP=BBP4`
- Raw: n=96  W=30/L=66  WR=31.2%
- Sharpen: sharpest is session_bucket=ny_close (35/66 of losers there)
- **Sharp: n=41  W=6/L=35  WR=14.6%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; upper third  •  ONLY when session=ny_close

### L16.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=95  W=30/L=65  WR=31.6%
- Sharpen: sharpest is H20=H20e (19/65 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L17.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H60=H60c (34/58 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 neutral

### L18.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=94  W=36/L=58  WR=38.3%
- Sharpen: sharpest is H60=H60c (34/58 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 neutral

### L19.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is RSI=RSI5 (36/57 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is H60=H60c (33/59 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_close  •  ONLY when HTF60 neutral

### L21.  `H60=H60b AND T1=T1a AND ZS=ZS4`
- Raw: n=87  W=26/L=61  WR=29.9%
- Sharpen: sharpest is session_bucket=ny_close (32/61 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L22.  `H60=H60b AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=87  W=26/L=61  WR=29.9%
- Sharpen: sharpest is session_bucket=ny_close (32/61 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_close

### L23.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=27/L=55  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (40/55 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  ONLY when RSI 60-70 strong

### L24.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=27/L=55  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (40/55 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60b AND T1=T1a AND session_bucket=ny_close`
- Raw: n=81  W=22/L=59  WR=27.2%
- Sharpen: sharpest is RSI=RSI4 (24/59 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; session=ny_close  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(25/20) | H20e(20/25) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/45) | T4c(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
