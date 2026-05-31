# EUR_GBP — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **535**  (W=345 / L=190)  -  WR: **64.5%**

## Session distribution

- ny_open: n=118  W=70/L=48  WR=59.3%
- london_open: n=107  W=71/L=36  WR=66.4%
- ny_mid: n=107  W=73/L=34  WR=68.2%
- london: n=79  W=55/L=24  WR=69.6%
- off_hours: n=62  W=39/L=23  WR=62.9%
- asia_late: n=36  W=22/L=14  WR=61.1%
- asia: n=21  W=13/L=8  WR=61.9%
- ny_close: n=5  W=2/L=3  WR=40.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W02.  `H60=H60b AND T1=T1c AND RSI=RSI5`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W03.  `H60=H60b AND T4=T4c AND RSI=RSI5`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W04.  `H60=H60b AND RSI=RSI5 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 slightly aligned; RSI 60-70 strong  •  AVOID when lower third

### W05.  `H60=H60b AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W06.  `H60=H60b AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W07.  `H60=H60b AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude BBP=BBP2 drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W08.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 8/10 losers (80%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W09.  `H20=H20b AND T4=T4a AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 8/10 losers (80%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_mid

### W10.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 8/10 losers (80%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W11.  `H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude H20=H20d drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF20 mildly against

### W12.  `H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude H20=H20d drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade  •  AVOID when HTF20 mildly against

### W13.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude H20=H20d drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF20 mildly against

### W14.  `H20=H20a AND H60=H60b AND T1=T1c`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude BBP=BBP4 drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend AGAINST trade  •  AVOID when upper third

### W15.  `H20=H20a AND H60=H60b AND T4=T4c`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude BBP=BBP4 drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when upper third

### W16.  `H20=H20a AND H60=H60b AND direction_exec=short`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude BBP=BBP4 drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 slightly aligned  •  AVOID when upper third

### W17.  `H20=H20a AND H60=H60b AND T1=T1c AND T4=T4c`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude BBP=BBP4 drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when upper third

### W18.  `H20=H20a AND H60=H60b AND T1=T1c AND direction_exec=short`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude BBP=BBP4 drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 1h trend AGAINST trade  •  AVOID when upper third

### W19.  `H20=H20a AND H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude BBP=BBP4 drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend AGAINST trade  •  AVOID when upper third

### W20.  `H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude H20=H20d drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W21.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude H20=H20d drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W22.  `H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude H20=H20d drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W23.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude H20=H20d drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W24.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude H20=H20d drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

### W25.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude H20=H20d drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is RSI=RSI5 (39/49 of losers there)
- **Sharp: n=53  W=14/L=39  WR=26.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L02.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=63  W=20/L=43  WR=31.7%
- Sharpen: sharpest is session_bucket=asia_late (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L03.  `H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=63  W=20/L=43  WR=31.7%
- Sharpen: sharpest is session_bucket=asia_late (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L04.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=63  W=20/L=43  WR=31.7%
- Sharpen: sharpest is session_bucket=asia_late (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia_late

### L05.  `H20=H20e AND T1=T1a AND direction_exec=long`
- Raw: n=56  W=17/L=39  WR=30.4%
- Sharpen: sharpest is H60=H60d (37/39 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when HTF60 mildly against

### L06.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=54  W=17/L=37  WR=31.5%
- Sharpen: sharpest is H60=H60d (37/37 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 mildly against

### L07.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=54  W=17/L=37  WR=31.5%
- Sharpen: sharpest is H60=H60d (37/37 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when HTF60 mildly against

### L08.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=54  W=17/L=37  WR=31.5%
- Sharpen: sharpest is H60=H60d (37/37 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF60 mildly against

### L09.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=53  W=14/L=39  WR=26.4%
- Sharpen: sharpest is H20=H20d (18/39 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L10.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=53  W=14/L=39  WR=26.4%
- Sharpen: sharpest is H20=H20d (18/39 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L11.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=53  W=14/L=39  WR=26.4%
- Sharpen: sharpest is H20=H20d (18/39 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L12.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=51  W=13/L=38  WR=25.5%
- Sharpen: sharpest is H20=H20d (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L13.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=51  W=13/L=38  WR=25.5%
- Sharpen: sharpest is H20=H20d (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L14.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=51  W=13/L=38  WR=25.5%
- Sharpen: sharpest is H20=H20d (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 mildly against

### L15.  `H20=H20e AND H60=H60d AND T1=T1a`
- Raw: n=48  W=11/L=37  WR=22.9%
- Sharpen: sharpest is RSI=RSI5 (9/37 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend WITH trade  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20e AND H60=H60d AND T4=T4a`
- Raw: n=48  W=11/L=37  WR=22.9%
- Sharpen: sharpest is RSI=RSI5 (9/37 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L17.  `H20=H20e AND H60=H60d AND direction_exec=long`
- Raw: n=48  W=11/L=37  WR=22.9%
- Sharpen: sharpest is RSI=RSI5 (9/37 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20e AND H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=48  W=11/L=37  WR=22.9%
- Sharpen: sharpest is RSI=RSI5 (9/37 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20e AND H60=H60d AND T1=T1a AND direction_exec=long`
- Raw: n=48  W=11/L=37  WR=22.9%
- Sharpen: sharpest is RSI=RSI5 (9/37 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; 1h trend WITH trade  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=48  W=11/L=37  WR=22.9%
- Sharpen: sharpest is RSI=RSI5 (9/37 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=43  W=14/L=29  WR=32.6%
- Sharpen: sharpest is session_bucket=asia_late (14/29 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when session=asia_late

### L22.  `H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=43  W=14/L=29  WR=32.6%
- Sharpen: sharpest is session_bucket=asia_late (14/29 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third  •  ONLY when session=asia_late

### L23.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=43  W=14/L=29  WR=32.6%
- Sharpen: sharpest is session_bucket=asia_late (14/29 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when session=asia_late

### L24.  `H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia_late (14/28 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia_late

### L25.  `H60=H60a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is session_bucket=asia_late (14/28 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when session=asia_late

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(29/21) | H20e(14/21) |
| H60 | H60e(23/9), H60b(33/23) | H60a(12/28), H60d(26/34) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
