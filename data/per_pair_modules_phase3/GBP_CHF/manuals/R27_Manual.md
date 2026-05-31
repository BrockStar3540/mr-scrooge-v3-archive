# GBP_CHF — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,047**  (W=1,309 / L=738)  -  WR: **63.9%**

## Session distribution

- ny_mid: n=664  W=429/L=235  WR=64.6%
- london_open: n=620  W=368/L=252  WR=59.4%
- london: n=328  W=222/L=106  WR=67.7%
- ny_open: n=310  W=204/L=106  WR=65.8%
- ny_close: n=113  W=77/L=36  WR=68.1%
- asia: n=12  W=9/L=3  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=198  W=177/L=21  WR=89.4%
- Refine: exclude ZS=ZS3 drops 14/21 losers (67%)
- **Final: n=163  W=156/L=7  WR=95.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W02.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=165  W=143/L=22  WR=86.7%
- Refine: exclude T4=T4a drops 20/22 losers (91%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W03.  `T1=T1c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=163  W=142/L=21  WR=87.1%
- Refine: exclude ZS=ZS3 drops 14/21 losers (67%)
- **Final: n=139  W=132/L=7  WR=95.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london  •  AVOID when zscore -1 to +1 neutral

### W04.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=163  W=142/L=21  WR=87.1%
- Refine: exclude ZS=ZS3 drops 14/21 losers (67%)
- **Final: n=139  W=132/L=7  WR=95.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=163  W=142/L=21  WR=87.1%
- Refine: exclude ZS=ZS3 drops 14/21 losers (67%)
- **Final: n=139  W=132/L=7  WR=95.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london  •  AVOID when zscore -1 to +1 neutral

### W06.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=126  W=118/L=8  WR=93.7%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=75  W=74/L=1  WR=98.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 strongly against

### W07.  `H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude ZS=ZS3 drops 12/18 losers (67%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60a AND direction_exec=short AND session_bucket=london`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude ZS=ZS3 drops 12/18 losers (67%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W09.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=london`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude ZS=ZS3 drops 12/18 losers (67%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=london  •  AVOID when zscore -1 to +1 neutral

### W10.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude ZS=ZS3 drops 12/18 losers (67%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W11.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=london`
- Raw: n=126  W=108/L=18  WR=85.7%
- Refine: exclude ZS=ZS3 drops 12/18 losers (67%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  AVOID when zscore -1 to +1 neutral

### W12.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when 4h trend WITH trade

### W13.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when 4h trend WITH trade

### W14.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when 4h trend WITH trade

### W15.  `T1=T1c AND BBP=BBP4 AND session_bucket=london`
- Raw: n=119  W=112/L=7  WR=94.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=109  W=106/L=3  WR=97.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london  •  AVOID when zscore -1 to +1 neutral

### W16.  `BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=119  W=112/L=7  WR=94.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=109  W=106/L=3  WR=97.2%**
- **Dir: SHORT**  •  upper third; session=london  •  AVOID when zscore -1 to +1 neutral

### W17.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london`
- Raw: n=119  W=112/L=7  WR=94.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=109  W=106/L=3  WR=97.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=london  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude BBP=BBP4 drops 16/16 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when upper third

### W19.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=116  W=103/L=13  WR=88.8%
- Refine: exclude BBP=BBP4 drops 13/13 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when upper third

### W20.  `H20=H20c AND T4=T4c AND RSI=RSI5`
- Raw: n=114  W=105/L=9  WR=92.1%
- Refine: exclude session_bucket=london drops 7/9 losers (78%)
- **Final: n=98  W=96/L=2  WR=98.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W21.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude T4=T4a drops 14/15 losers (93%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend WITH trade

### W22.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude T4=T4a drops 14/15 losers (93%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: LONG**  •  upper third; session=ny_open  •  AVOID when 4h trend WITH trade

### W23.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude T4=T4a drops 14/15 losers (93%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend WITH trade

### W24.  `T1=T1c AND ZS=ZS4 AND session_bucket=london`
- Raw: n=109  W=106/L=3  WR=97.2%
- Refine: exclude H20=H20a drops 2/3 losers (67%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 aligned WITH trade

### W25.  `ZS=ZS4 AND direction_exec=short AND session_bucket=london`
- Raw: n=109  W=106/L=3  WR=97.2%
- Refine: exclude H20=H20a drops 2/3 losers (67%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=london  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND session_bucket=london_open`
- Raw: n=148  W=49/L=99  WR=33.1%
- Sharpen: sharpest is T1=T1c (77/99 of losers there)
- **Sharp: n=93  W=16/L=77  WR=17.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=london_open  •  ONLY when 1h trend AGAINST trade

### L02.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=136  W=34/L=102  WR=25.0%
- Sharpen: sharpest is T4=T4a (49/102 of losers there)
- **Sharp: n=55  W=6/L=49  WR=10.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend WITH trade

### L03.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=130  W=45/L=85  WR=34.6%
- Sharpen: sharpest is ZS=ZS4 (49/85 of losers there)
- **Sharp: n=59  W=10/L=49  WR=16.9%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  ONLY when zscore +1 to +2 overbought

### L04.  `H20=H20c AND T1=T1c AND RSI=RSI6`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is session_bucket=london_open (44/79 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L05.  `H20=H20c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is session_bucket=london_open (44/79 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 70-80 overbought  •  ONLY when session=london_open

### L06.  `H20=H20c AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is session_bucket=london_open (44/79 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L07.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=122  W=44/L=78  WR=36.1%
- Sharpen: sharpest is H60=H60e (77/78 of losers there)
- **Sharp: n=93  W=16/L=77  WR=17.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF60 strongly against

### L08.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=34/L=79  WR=30.1%
- Sharpen: sharpest is ZS=ZS5 (32/79 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=34/L=79  WR=30.1%
- Sharpen: sharpest is ZS=ZS5 (32/79 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H60=H60e AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=107  W=38/L=69  WR=35.5%
- Sharpen: sharpest is T4=T4a (26/69 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L11.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H20=H20a (58/66 of losers there)
- **Sharp: n=81  W=23/L=58  WR=28.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L12.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (23/64 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 30-40 weak

### L13.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=104  W=26/L=78  WR=25.0%
- Sharpen: sharpest is H60=H60e (49/78 of losers there)
- **Sharp: n=55  W=6/L=49  WR=10.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF60 strongly against

### L14.  `H20=H20a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=101  W=35/L=66  WR=34.7%
- Sharpen: sharpest is BBP=BBP4 (35/66 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  ONLY when upper third

### L15.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=99  W=22/L=77  WR=22.2%
- Sharpen: sharpest is RSI=RSI2 (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L16.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is T4=T4a (22/57 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L17.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is T4=T4a (22/57 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L18.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=95  W=38/L=57  WR=40.0%
- Sharpen: sharpest is T4=T4a (22/57 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when 4h trend WITH trade

### L19.  `H20=H20a AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=93  W=16/L=77  WR=17.2%
- Sharpen: sharpest is RSI=RSI2 (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20a AND H60=H60e AND T4=T4c`
- Raw: n=91  W=31/L=60  WR=34.1%
- Sharpen: sharpest is BBP=BBP4 (40/60 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when upper third

### L21.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is T1=T1c (23/55 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when 1h trend AGAINST trade

### L22.  `T1=T1c AND RSI=RSI6 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is H20=H20c (27/53 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when HTF20 neutral

### L23.  `RSI=RSI6 AND ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is H20=H20c (27/53 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when HTF20 neutral

### L24.  `H20=H20c AND T4=T4a AND RSI=RSI5`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_mid (27/55 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is H20=H20a (22/54 of losers there)
- **Sharp: n=29  W=7/L=22  WR=24.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(42/36) | H60e(35/43) |
| T1 | T1a(52/42) | T1c(48/58) |
| T4 | T4c(57/47) | T4a(43/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | london_open(28/34) |

*Read: `bucket(winner%/loser%)`.*
