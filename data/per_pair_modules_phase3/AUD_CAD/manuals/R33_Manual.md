# AUD_CAD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,459**  (W=1,488 / L=971)  -  WR: **60.5%**

## Session distribution

- ny_mid: n=820  W=483/L=337  WR=58.9%
- asia: n=453  W=277/L=176  WR=61.1%
- ny_open: n=414  W=228/L=186  WR=55.1%
- london_open: n=314  W=200/L=114  WR=63.7%
- ny_close: n=272  W=178/L=94  WR=65.4%
- off_hours: n=88  W=55/L=33  WR=62.5%
- london: n=76  W=51/L=25  WR=67.1%
- asia_late: n=22  W=16/L=6  WR=72.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI2 drops 11/15 losers (73%)
- **Final: n=47  W=43/L=4  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when RSI 30-40 weak

### W02.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI2 drops 11/15 losers (73%)
- **Final: n=47  W=43/L=4  WR=91.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when RSI 30-40 weak

### W03.  `T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude BBP=BBP0 drops 3/9 losers (33%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when deep below lower band

### W04.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W05.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  upper third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W07.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude BBP=BBP0 drops 3/9 losers (33%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when deep below lower band

### W08.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude BBP=BBP0 drops 3/9 losers (33%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when deep below lower band

### W09.  `H20=H20a AND T4=T4a AND BBP=BBP4`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude T1=T1c drops 10/10 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when 1h trend AGAINST trade

### W10.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W11.  `T1=T1a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W12.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 strongly against

### W13.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=66  W=60/L=6  WR=90.9%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W14.  `H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W15.  `T1=T1a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W16.  `T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W17.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W18.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W19.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 strongly against

### W20.  `H60=H60e AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when 4h trend WITH trade

### W21.  `T1=T1a AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when 4h trend WITH trade

### W22.  `ZS=ZS1 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when 4h trend WITH trade

### W23.  `H60=H60e AND T1=T1a AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when 4h trend WITH trade

### W24.  `H60=H60e AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when 4h trend WITH trade

### W25.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=145  W=52/L=93  WR=35.9%
- Sharpen: sharpest is T4=T4a (55/93 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L02.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=145  W=52/L=93  WR=35.9%
- Sharpen: sharpest is T4=T4a (55/93 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: SHORT**  •  lower third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L03.  `H60=H60e AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=145  W=52/L=93  WR=35.9%
- Sharpen: sharpest is T4=T4a (55/93 of losers there)
- **Sharp: n=74  W=19/L=55  WR=25.7%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L04.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (22/88 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L05.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=140  W=52/L=88  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (22/88 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L06.  `H60=H60e AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is T4=T4a (50/80 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L07.  `ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is T4=T4a (50/80 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L08.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is T4=T4a (50/80 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L09.  `H60=H60e AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is T4=T4a (50/80 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L10.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is T4=T4a (50/80 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L11.  `H60=H60e AND T1=T1a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is RSI=RSI1 (20/75 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L12.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is RSI=RSI1 (20/75 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L13.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L14.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L15.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L16.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L17.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L18.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=111  W=44/L=67  WR=39.6%
- Sharpen: sharpest is BBP=BBP1 (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L19.  `H20=H20e AND H60=H60e AND RSI=RSI1`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is session_bucket=off_hours (26/67 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  ONLY when session=off_hours

### L20.  `H20=H20e AND T1=T1a AND RSI=RSI1`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is session_bucket=off_hours (26/67 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  ONLY when session=off_hours

### L21.  `H20=H20e AND RSI=RSI1 AND direction_exec=short`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is session_bucket=off_hours (26/67 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 20-30 oversold  •  ONLY when session=off_hours

### L22.  `H60=H60e AND T1=T1a AND RSI=RSI1`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is session_bucket=off_hours (26/67 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  ONLY when session=off_hours

### L23.  `H60=H60e AND RSI=RSI1 AND direction_exec=short`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is session_bucket=off_hours (26/67 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 20-30 oversold  •  ONLY when session=off_hours

### L24.  `T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is session_bucket=off_hours (26/67 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold  •  ONLY when session=off_hours

### L25.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI1`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is session_bucket=off_hours (26/67 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold  •  ONLY when session=off_hours

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(40/31) | H20e(30/40) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
