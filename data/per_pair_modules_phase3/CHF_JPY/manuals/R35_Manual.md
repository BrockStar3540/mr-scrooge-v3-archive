# CHF_JPY — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,477**  (W=2,788 / L=1,689)  -  WR: **62.3%**

## Session distribution

- asia: n=1783  W=1104/L=679  WR=61.9%
- ny_close: n=1372  W=838/L=534  WR=61.1%
- asia_late: n=310  W=206/L=104  WR=66.5%
- ny_open: n=273  W=165/L=108  WR=60.4%
- off_hours: n=269  W=176/L=93  WR=65.4%
- london: n=218  W=143/L=75  WR=65.6%
- london_open: n=177  W=108/L=69  WR=61.0%
- ny_mid: n=75  W=48/L=27  WR=64.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=245  W=209/L=36  WR=85.3%
- Refine: exclude session_bucket=asia drops 21/36 losers (58%)
- **Final: n=136  W=121/L=15  WR=89.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when session=asia

### W02.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=202  W=172/L=30  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 23/30 losers (77%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_close

### W03.  `H20=H20c AND H60=H60a AND T4=T4a`
- Raw: n=202  W=172/L=30  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 23/30 losers (77%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W04.  `H20=H20c AND H60=H60a AND direction_exec=long`
- Raw: n=202  W=172/L=30  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 23/30 losers (77%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade  •  AVOID when session=ny_close

### W05.  `H20=H20c AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=202  W=172/L=30  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 23/30 losers (77%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W06.  `H20=H20c AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=202  W=172/L=30  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 23/30 losers (77%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_close

### W07.  `H20=H20c AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=202  W=172/L=30  WR=85.1%
- Refine: exclude session_bucket=ny_close drops 23/30 losers (77%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W08.  `H20=H20c AND T1=T1a AND RSI=RSI5`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 18/18 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W09.  `H20=H20c AND T4=T4a AND RSI=RSI5`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 18/18 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W10.  `H20=H20c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 18/18 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; RSI 60-70 strong  •  AVOID when session=ny_close

### W11.  `H20=H20c AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 18/18 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W12.  `H20=H20c AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 18/18 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W13.  `H20=H20c AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 18/18 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W14.  `H20=H20c AND H60=H60a AND RSI=RSI5`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W15.  `H20=H20c AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W16.  `H20=H20c AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W17.  `H20=H20c AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude session_bucket=ny_close drops 9/9 losers (100%)
- **Final: n=89  W=89/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W18.  `H20=H20c AND H60=H60a AND BBP=BBP4`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; upper third  •  AVOID when session=ny_close

### W19.  `H20=H20c AND T1=T1a AND BBP=BBP4`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; upper third  •  AVOID when session=ny_close

### W20.  `H20=H20c AND T4=T4a AND BBP=BBP4`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; upper third  •  AVOID when session=ny_close

### W21.  `H20=H20c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 neutral; upper third  •  AVOID when session=ny_close

### W22.  `H20=H20c AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when session=ny_close

### W23.  `H20=H20c AND H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_close

### W24.  `H20=H20c AND H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; upper third  •  AVOID when session=ny_close

### W25.  `H20=H20c AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=99  W=89/L=10  WR=89.9%
- Refine: exclude session_bucket=ny_close drops 8/10 losers (80%)
- **Final: n=69  W=67/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=208  W=83/L=125  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (61/125 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when session=asia

### L02.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (30/109 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L03.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (30/109 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=asia

### L04.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (30/109 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when session=asia

### L05.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (30/109 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L06.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=163  W=54/L=109  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (69/109 of losers there)
- **Sharp: n=86  W=17/L=69  WR=19.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=163  W=54/L=109  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (69/109 of losers there)
- **Sharp: n=86  W=17/L=69  WR=19.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=163  W=54/L=109  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (69/109 of losers there)
- **Sharp: n=86  W=17/L=69  WR=19.8%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  ONLY when RSI 60-70 strong

### L09.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=163  W=54/L=109  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (69/109 of losers there)
- **Sharp: n=86  W=17/L=69  WR=19.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=163  W=54/L=109  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (69/109 of losers there)
- **Sharp: n=86  W=17/L=69  WR=19.8%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20c AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=163  W=54/L=109  WR=33.1%
- Sharpen: sharpest is RSI=RSI5 (69/109 of losers there)
- **Sharp: n=86  W=17/L=69  WR=19.8%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=155  W=53/L=102  WR=34.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=53/L=102  WR=34.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral

### L13.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=153  W=51/L=102  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=153  W=51/L=102  WR=33.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral

### L14.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=148  W=51/L=97  WR=34.5%
- Sharpen: sharpest is BBP=BBP4 (26/97 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when upper third

### L15.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=147  W=50/L=97  WR=34.0%
- Sharpen: sharpest is BBP=BBP4 (26/97 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when upper third

### L16.  `H20=H20d AND H60=H60e AND ZS=ZS5`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (29/88 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L17.  `H20=H20d AND T1=T1c AND ZS=ZS5`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (29/88 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L18.  `H20=H20d AND ZS=ZS5 AND direction_exec=short`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (29/88 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L19.  `H20=H20d AND H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (29/88 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L20.  `H20=H20d AND H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (29/88 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L21.  `H20=H20d AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI6 (29/88 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L22.  `H20=H20a AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=125  W=46/L=79  WR=36.8%
- Sharpen: sharpest is session_bucket=asia (41/79 of losers there)
- **Sharp: n=56  W=15/L=41  WR=26.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 60-70 strong  •  ONLY when session=asia

### L23.  `H20=H20a AND BBP=BBP3 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=125  W=46/L=79  WR=36.8%
- Sharpen: sharpest is session_bucket=asia (41/79 of losers there)
- **Sharp: n=56  W=15/L=41  WR=26.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when session=asia

### L24.  `H20=H20a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=116  W=39/L=77  WR=33.6%
- Sharpen: sharpest is RSI=RSI5 (61/77 of losers there)
- **Sharp: n=83  W=22/L=61  WR=26.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral; session=asia  •  ONLY when RSI 60-70 strong

### L25.  `H20=H20a AND BBP=BBP3 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is session_bucket=asia (38/67 of losers there)
- **Sharp: n=53  W=15/L=38  WR=28.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; middle of band; RSI 60-70 strong  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(36/30), H20b(16/10) | H20a(30/37), H20d(9/15) |
| H60 | H60a(53/44) | H60e(45/53) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
