# AUD_CAD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,482**  (W=2,222 / L=1,260)  -  WR: **63.8%**

## Session distribution

- asia: n=1263  W=821/L=442  WR=65.0%
- ny_close: n=1071  W=668/L=403  WR=62.4%
- ny_mid: n=315  W=192/L=123  WR=61.0%
- london: n=238  W=151/L=87  WR=63.4%
- london_open: n=226  W=154/L=72  WR=68.1%
- ny_open: n=204  W=135/L=69  WR=66.2%
- off_hours: n=158  W=97/L=61  WR=61.4%
- asia_late: n=7  W=4/L=3  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND T1=T1a AND T4=T4c`
- Raw: n=171  W=148/L=23  WR=86.5%
- Refine: exclude ZS=ZS2 drops 10/23 losers (43%)
- **Final: n=130  W=117/L=13  WR=90.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W02.  `H20=H20a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=143  W=123/L=20  WR=86.0%
- Refine: exclude T4=T4a drops 20/20 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W03.  `H20=H20c AND H60=H60e AND T1=T1a`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude ZS=ZS2 drops 10/19 losers (53%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W04.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude ZS=ZS2 drops 10/19 losers (53%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W05.  `H20=H20c AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude ZS=ZS2 drops 10/19 losers (53%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W06.  `H20=H20c AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude ZS=ZS2 drops 10/19 losers (53%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W07.  `H20=H20c AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude ZS=ZS2 drops 10/19 losers (53%)
- **Final: n=92  W=83/L=9  WR=90.2%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

### W08.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude T4=T4c drops 15/18 losers (83%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W09.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude H20=H20d drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W10.  `H20=H20a AND H60=H60a AND ZS=ZS1`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP0 drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W11.  `H20=H20a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP0 drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W12.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP0 drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W13.  `H20=H20a AND T1=T1a AND ZS=ZS1`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude BBP=BBP0 drops 11/15 losers (73%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W14.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS1`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude BBP=BBP0 drops 11/15 losers (73%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W15.  `H20=H20a AND T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude BBP=BBP0 drops 11/15 losers (73%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W16.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude BBP=BBP0 drops 12/13 losers (92%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W17.  `T1=T1a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude BBP=BBP0 drops 12/13 losers (92%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W18.  `RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude BBP=BBP0 drops 12/13 losers (92%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W19.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude BBP=BBP0 drops 12/13 losers (92%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W20.  `H60=H60a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude BBP=BBP0 drops 12/13 losers (92%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W21.  `T1=T1a AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: exclude BBP=BBP0 drops 12/13 losers (92%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W22.  `T1=T1a AND T4=T4c AND BBP=BBP6`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude session_bucket=ny_open drops 8/12 losers (67%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=ny_open

### W23.  `T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude BBP=BBP0 drops 7/10 losers (70%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W24.  `H60=H60a AND T1=T1a AND BBP=BBP1`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude H20=H20d drops 10/14 losers (71%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; just touched lower band  •  AVOID when HTF20 mildly against

### W25.  `T1=T1a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude H20=H20d drops 10/14 losers (71%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: LONG**  •  1h trend WITH trade; just touched lower band  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=102  W=39/L=63  WR=38.2%
- Sharpen: sharpest is H20=H20e (40/63 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND T1=T1c AND session_bucket=london`
- Raw: n=90  W=31/L=59  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (32/59 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when RSI 60-70 strong

### L03.  `T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=90  W=31/L=59  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (32/59 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london  •  ONLY when RSI 60-70 strong

### L04.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=90  W=31/L=59  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (32/59 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london  •  ONLY when RSI 60-70 strong

### L05.  `T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (45/53 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20e AND H60=H60e AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=83  W=31/L=52  WR=37.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; middle of band; RSI 50-60 upper neutral

### L07.  `H20=H20e AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=83  W=31/L=52  WR=37.3%**
- **Dir: SHORT**  •  HTF20 strongly against; middle of band; RSI 50-60 upper neutral

### L08.  `H20=H20e AND H60=H60e AND ZS=ZS1`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/53 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L09.  `H20=H20e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/53 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L10.  `H20=H20e AND H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (29/53 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L11.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=77  W=25/L=52  WR=32.5%
- Sharpen: sharpest is T4=T4c (40/52 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=77  W=25/L=52  WR=32.5%
- Sharpen: sharpest is T4=T4c (40/52 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=77  W=25/L=52  WR=32.5%
- Sharpen: sharpest is T4=T4c (40/52 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=77  W=25/L=52  WR=32.5%
- Sharpen: sharpest is T4=T4c (40/52 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L15.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=77  W=27/L=50  WR=35.1%
- Sharpen: sharpest is RSI=RSI4 (42/50 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=77  W=27/L=50  WR=35.1%
- Sharpen: sharpest is RSI=RSI4 (42/50 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L17.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=77  W=27/L=50  WR=35.1%
- Sharpen: sharpest is RSI=RSI4 (42/50 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 50-60 upper neutral

### L18.  `H60=H60e AND T4=T4a AND BBP=BBP6`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (45/45 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L19.  `T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (45/45 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L20.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (45/45 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60e AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (45/45 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L22.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (45/45 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L23.  `H60=H60e AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=74  W=20/L=54  WR=27.0%
- Sharpen: sharpest is ZS=ZS6 (20/54 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; session=ny_close  •  ONLY when zscore >+3 extreme

### L24.  `T1=T1c AND BBP=BBP6 AND session_bucket=ny_close`
- Raw: n=74  W=20/L=54  WR=27.0%
- Sharpen: sharpest is ZS=ZS6 (20/54 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; session=ny_close  •  ONLY when zscore >+3 extreme

### L25.  `BBP=BBP6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=74  W=20/L=54  WR=27.0%
- Sharpen: sharpest is ZS=ZS6 (20/54 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  deep above upper band; session=ny_close  •  ONLY when zscore >+3 extreme

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/25) | H20e(27/40) |
| H60 | H60a(53/45) | H60e(47/55) |
| T1 | T1a(55/43) | T1c(45/57) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/45) | short(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
