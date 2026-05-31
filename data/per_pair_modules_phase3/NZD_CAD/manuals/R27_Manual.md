# NZD_CAD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,272**  (W=1,415 / L=857)  -  WR: **62.3%**

## Session distribution

- asia: n=628  W=394/L=234  WR=62.7%
- ny_close: n=551  W=328/L=223  WR=59.5%
- ny_mid: n=406  W=264/L=142  WR=65.0%
- ny_open: n=263  W=158/L=105  WR=60.1%
- london_open: n=215  W=131/L=84  WR=60.9%
- off_hours: n=99  W=61/L=38  WR=61.6%
- asia_late: n=71  W=50/L=21  WR=70.4%
- london: n=39  W=29/L=10  WR=74.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=171  W=151/L=20  WR=88.3%
- Refine: exclude H60=H60e drops 6/20 losers (30%)
- **Final: n=163  W=149/L=14  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 strongly against

### W02.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude H60=H60d drops 11/18 losers (61%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 mildly against

### W03.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=163  W=145/L=18  WR=89.0%
- Refine: exclude H60=H60d drops 11/18 losers (61%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 mildly against

### W04.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude H60=H60d drops 11/18 losers (61%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 mildly against

### W05.  `H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; lower third  •  AVOID when session=asia

### W06.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  AVOID when session=asia

### W07.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third  •  AVOID when session=asia

### W08.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude session_bucket=asia drops 9/14 losers (64%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=asia

### W09.  `H20=H20a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude H60=H60e drops 4/12 losers (33%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 strongly against

### W10.  `H60=H60e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=asia drops 7/12 losers (58%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -2 to -1 oversold  •  AVOID when session=asia

### W11.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS2`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=asia drops 7/12 losers (58%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W12.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=asia drops 7/12 losers (58%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W13.  `H60=H60e AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=asia drops 7/12 losers (58%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=asia

### W14.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=asia drops 7/12 losers (58%)
- **Final: n=61  W=56/L=5  WR=91.8%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  AVOID when session=asia

### W15.  `T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=91  W=85/L=6  WR=93.4%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W16.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W17.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W18.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W19.  `T1=T1a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W20.  `BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: SHORT**  •  deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W21.  `H20=H20a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude H60=H60e drops 4/12 losers (33%)
- **Final: n=85  W=77/L=8  WR=90.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=ny_close  •  AVOID when HTF60 strongly against

### W22.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude ZS=ZS4 drops 10/13 losers (77%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W23.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude ZS=ZS4 drops 10/13 losers (77%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W24.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=83  W=77/L=6  WR=92.8%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W25.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=83  W=77/L=6  WR=92.8%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=208  W=81/L=127  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (93/127 of losers there)
- **Sharp: n=132  W=39/L=93  WR=29.5%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_close  •  ONLY when RSI 30-40 weak

### L02.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=205  W=80/L=125  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (93/125 of losers there)
- **Sharp: n=132  W=39/L=93  WR=29.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L03.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=205  W=80/L=125  WR=39.0%
- Sharpen: sharpest is RSI=RSI2 (93/125 of losers there)
- **Sharp: n=132  W=39/L=93  WR=29.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L04.  `H20=H20e AND H60=H60d AND T1=T1c`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L05.  `H20=H20e AND H60=H60d AND T4=T4c`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L06.  `H20=H20e AND H60=H60d AND direction_exec=long`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against  •  ONLY when session=ny_close

### L07.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L08.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L09.  `H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L10.  `H20=H20e AND H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L11.  `H20=H20e AND H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L12.  `H20=H20e AND H60=H60d AND T4=T4c AND direction_exec=long`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L13.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=186  W=74/L=112  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_close (49/112 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L14.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is T4=T4a (43/102 of losers there)
- **Sharp: n=55  W=12/L=43  WR=21.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L15.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is T4=T4a (43/102 of losers there)
- **Sharp: n=55  W=12/L=43  WR=21.8%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is T4=T4a (43/102 of losers there)
- **Sharp: n=55  W=12/L=43  WR=21.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=156  W=57/L=99  WR=36.5%
- Sharpen: sharpest is H60=H60c (31/99 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L18.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=156  W=57/L=99  WR=36.5%
- Sharpen: sharpest is H60=H60c (31/99 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L19.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=156  W=57/L=99  WR=36.5%
- Sharpen: sharpest is H60=H60c (31/99 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L20.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=138  W=43/L=95  WR=31.2%
- Sharpen: sharpest is H60=H60c (31/95 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L21.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is H60=H60d (33/80 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 mildly against

### L22.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is H60=H60d (33/80 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 mildly against

### L23.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=132  W=39/L=93  WR=29.5%
- Sharpen: sharpest is H60=H60c (31/93 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L24.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=132  W=39/L=93  WR=29.5%
- Sharpen: sharpest is H60=H60c (31/93 of losers there)
- **Sharp: n=31  W=0/L=31  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L25.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=115  W=39/L=76  WR=33.9%
- Sharpen: sharpest is H60=H60c (12/76 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(48/39) | H20e(39/49) |
| H60 | — | — |
| T1 | T1a(53/47) | T1c(47/52) |
| T4 | T4c(53/47) | T4a(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
