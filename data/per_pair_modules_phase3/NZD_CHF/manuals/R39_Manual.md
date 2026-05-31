# NZD_CHF — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **532**  (W=343 / L=189)  -  WR: **64.5%**

## Session distribution

- asia: n=324  W=215/L=109  WR=66.4%
- ny_mid: n=82  W=51/L=31  WR=62.2%
- ny_close: n=54  W=36/L=18  WR=66.7%
- ny_open: n=37  W=21/L=16  WR=56.8%
- off_hours: n=20  W=11/L=9  WR=55.0%
- london_open: n=8  W=4/L=4  WR=50.0%
- london: n=4  W=3/L=1  WR=75.0%
- asia_late: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=195  W=174/L=21  WR=89.2%
- Refine: exclude BBP=BBP2 drops 19/21 losers (90%)
- **Final: n=102  W=100/L=2  WR=98.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W02.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W03.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W04.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=140  W=127/L=13  WR=90.7%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=73  W=73/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W05.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W06.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when lower third

### W07.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W08.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W09.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when lower third

### W10.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude BBP=BBP2 drops 12/14 losers (86%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W11.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP2 drops 14/15 losers (93%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when lower third

### W12.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP2 drops 14/15 losers (93%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia  •  AVOID when lower third

### W13.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude BBP=BBP2 drops 14/15 losers (93%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when lower third

### W14.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H60=H60a drops 11/13 losers (85%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when HTF60 aligned WITH trade

### W15.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H60=H60a drops 11/13 losers (85%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when HTF60 aligned WITH trade

### W16.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude H60=H60a drops 11/13 losers (85%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20a AND H60=H60a AND RSI=RSI1`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude session_bucket=ny_open drops 5/11 losers (45%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_open

### W18.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude T4=T4c drops 6/7 losers (86%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude T4=T4c drops 6/7 losers (86%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=85  W=78/L=7  WR=91.8%
- Refine: exclude T4=T4c drops 6/7 losers (86%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W21.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when lower third

### W22.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  AVOID when lower third

### W23.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=81  W=75/L=6  WR=92.6%
- Refine: exclude BBP=BBP2 drops 5/6 losers (83%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when lower third

### W24.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=164  W=62/L=102  WR=37.8%
- Sharpen: sharpest is session_bucket=asia (63/102 of losers there)
- **Sharp: n=87  W=24/L=63  WR=27.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L02.  `T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=129  W=41/L=88  WR=31.8%
- Sharpen: sharpest is H20=H20a (41/88 of losers there)
- **Sharp: n=51  W=10/L=41  WR=19.6%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is ZS=ZS1 (30/74 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is session_bucket=asia (41/69 of losers there)
- **Sharp: n=51  W=10/L=41  WR=19.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=asia

### L05.  `H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is RSI=RSI1 (39/66 of losers there)
- **Sharp: n=53  W=14/L=39  WR=26.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade  •  ONLY when RSI 20-30 oversold

### L06.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (41/69 of losers there)
- **Sharp: n=51  W=10/L=41  WR=19.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L07.  `H20=H20a AND T4=T4a AND direction_exec=short`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (41/69 of losers there)
- **Sharp: n=51  W=10/L=41  WR=19.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L08.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (41/69 of losers there)
- **Sharp: n=51  W=10/L=41  WR=19.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when session=asia

### L09.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=87  W=24/L=63  WR=27.6%
- Sharpen: sharpest is H60=H60c (26/63 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 neutral

### L10.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=24/L=63  WR=27.6%
- Sharpen: sharpest is H60=H60c (26/63 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  ONLY when HTF60 neutral

### L11.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=24/L=63  WR=27.6%
- Sharpen: sharpest is H60=H60c (26/63 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 neutral

### L12.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is ZS=ZS1 (9/50 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is ZS=ZS1 (9/50 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is ZS=ZS1 (9/50 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is T4=T4a (29/42 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L16.  `RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is T4=T4a (29/42 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is T4=T4a (29/42 of losers there)
- **Sharp: n=39  W=10/L=29  WR=25.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is ZS=ZS1 (9/39 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is ZS=ZS1 (9/39 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=63  W=24/L=39  WR=38.1%
- Sharpen: sharpest is ZS=ZS1 (9/39 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is H20=H20a (21/37 of losers there)
- **Sharp: n=28  W=7/L=21  WR=25.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L22.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is H20=H20a (21/37 of losers there)
- **Sharp: n=28  W=7/L=21  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is H20=H20a (21/37 of losers there)
- **Sharp: n=28  W=7/L=21  WR=25.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L24.  `H20=H20e AND H60=H60e AND RSI=RSI1`
- Raw: n=59  W=19/L=40  WR=32.2%
- Sharpen: sharpest is T4=T4c (29/40 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  ONLY when 4h trend AGAINST trade

### L25.  `T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=56  W=14/L=42  WR=25.0%
- Sharpen: sharpest is H60=H60c (19/42 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF60 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(47/38) | H20a(45/51) |
| H60 | H60a(44/26), H60d(6/0) | H60e(27/46) |
| T1 | T1c(73/30) | T1a(27/70) |
| T4 | T4c(64/37) | T4a(36/63) |
| BBP | — | BBP0(13/19) |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(73/30) | short(27/70) |
| session_bucket | asia(63/58) | — |

*Read: `bucket(winner%/loser%)`.*
