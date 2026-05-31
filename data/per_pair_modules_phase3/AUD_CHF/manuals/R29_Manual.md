# AUD_CHF — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **631**  (W=410 / L=221)  -  WR: **65.0%**

## Session distribution

- asia: n=313  W=206/L=107  WR=65.8%
- ny_mid: n=120  W=73/L=47  WR=60.8%
- ny_open: n=88  W=57/L=31  WR=64.8%
- london_open: n=41  W=27/L=14  WR=65.9%
- asia_late: n=31  W=22/L=9  WR=71.0%
- ny_close: n=26  W=19/L=7  WR=73.1%
- off_hours: n=9  W=4/L=5  WR=44.4%
- london: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=220  W=194/L=26  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/26 losers (31%)
- **Final: n=182  W=164/L=18  WR=90.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W02.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=220  W=194/L=26  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/26 losers (31%)
- **Final: n=182  W=164/L=18  WR=90.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W03.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=220  W=194/L=26  WR=88.2%
- Refine: exclude session_bucket=ny_open drops 8/26 losers (31%)
- **Final: n=182  W=164/L=18  WR=90.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W04.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=219  W=193/L=26  WR=88.1%
- Refine: exclude session_bucket=ny_open drops 8/26 losers (31%)
- **Final: n=181  W=163/L=18  WR=90.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W05.  `H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=219  W=193/L=26  WR=88.1%
- Refine: exclude session_bucket=ny_open drops 8/26 losers (31%)
- **Final: n=181  W=163/L=18  WR=90.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W06.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=219  W=193/L=26  WR=88.1%
- Refine: exclude session_bucket=ny_open drops 8/26 losers (31%)
- **Final: n=181  W=163/L=18  WR=90.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W07.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=210  W=185/L=25  WR=88.1%
- Refine: exclude session_bucket=ny_open drops 8/25 losers (32%)
- **Final: n=172  W=155/L=17  WR=90.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W08.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=210  W=185/L=25  WR=88.1%
- Refine: exclude session_bucket=ny_open drops 8/25 losers (32%)
- **Final: n=172  W=155/L=17  WR=90.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W09.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=210  W=185/L=25  WR=88.1%
- Refine: exclude session_bucket=ny_open drops 8/25 losers (32%)
- **Final: n=172  W=155/L=17  WR=90.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W10.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=151  W=135/L=16  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W11.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=151  W=135/L=16  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when session=ny_open

### W12.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=151  W=135/L=16  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W13.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=144  W=128/L=16  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=106  W=98/L=8  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W14.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=144  W=128/L=16  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=106  W=98/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  AVOID when session=ny_open

### W15.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=144  W=128/L=16  WR=88.9%
- Refine: exclude session_bucket=ny_open drops 8/16 losers (50%)
- **Final: n=106  W=98/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W16.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=141  W=126/L=15  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 8/15 losers (53%)
- **Final: n=103  W=96/L=7  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  AVOID when session=ny_open

### W17.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=141  W=126/L=15  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 8/15 losers (53%)
- **Final: n=103  W=96/L=7  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W18.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=141  W=126/L=15  WR=89.4%
- Refine: exclude session_bucket=ny_open drops 8/15 losers (53%)
- **Final: n=103  W=96/L=7  WR=93.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  AVOID when session=ny_open

### W19.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: exclude session_bucket=ny_open drops 8/12 losers (67%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W20.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: exclude session_bucket=ny_open drops 8/12 losers (67%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W21.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: exclude session_bucket=ny_open drops 8/12 losers (67%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W22.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W24.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=126  W=110/L=16  WR=87.3%
- Refine: exclude ZS=ZS3 drops 8/16 losers (50%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W25.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude session_bucket=ny_open drops 8/12 losers (67%)
- **Final: n=84  W=80/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=205  W=82/L=123  WR=40.0%
- Sharpen: sharpest is H20=H20a (102/123 of losers there)
- **Sharp: n=150  W=48/L=102  WR=32.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade  •  ONLY when HTF20 aligned WITH trade

### L02.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=150  W=48/L=102  WR=32.0%
- Sharpen: sharpest is RSI=RSI5 (66/102 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L03.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=150  W=48/L=102  WR=32.0%
- Sharpen: sharpest is RSI=RSI5 (66/102 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L04.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=150  W=48/L=102  WR=32.0%
- Sharpen: sharpest is RSI=RSI5 (66/102 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=149  W=49/L=100  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (61/100 of losers there)
- **Sharp: n=80  W=19/L=61  WR=23.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L06.  `H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=149  W=49/L=100  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (61/100 of losers there)
- **Sharp: n=80  W=19/L=61  WR=23.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L07.  `H60=H60a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=149  W=49/L=100  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (61/100 of losers there)
- **Sharp: n=80  W=19/L=61  WR=23.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L08.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20a (77/93 of losers there)
- **Sharp: n=99  W=22/L=77  WR=22.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L09.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=143  W=47/L=96  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (60/96 of losers there)
- **Sharp: n=78  W=18/L=60  WR=23.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=143  W=47/L=96  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (60/96 of losers there)
- **Sharp: n=78  W=18/L=60  WR=23.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20a AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=143  W=47/L=96  WR=32.9%
- Sharpen: sharpest is RSI=RSI5 (60/96 of losers there)
- **Sharp: n=78  W=18/L=60  WR=23.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L12.  `T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H20=H20a (66/82 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L13.  `T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H20=H20a (66/82 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L14.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H20=H20a (66/82 of losers there)
- **Sharp: n=85  W=19/L=66  WR=22.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L15.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=99  W=22/L=77  WR=22.2%
- Sharpen: sharpest is session_bucket=asia (46/77 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L16.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=99  W=22/L=77  WR=22.2%
- Sharpen: sharpest is session_bucket=asia (46/77 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L17.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=99  W=22/L=77  WR=22.2%
- Sharpen: sharpest is session_bucket=asia (46/77 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L18.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=94  W=22/L=72  WR=23.4%
- Sharpen: sharpest is session_bucket=asia (46/72 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L19.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=94  W=22/L=72  WR=23.4%
- Sharpen: sharpest is session_bucket=asia (46/72 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L20.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=94  W=22/L=72  WR=23.4%
- Sharpen: sharpest is session_bucket=asia (46/72 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L21.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=92  W=21/L=71  WR=22.8%
- Sharpen: sharpest is session_bucket=asia (46/71 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L22.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=92  W=21/L=71  WR=22.8%
- Sharpen: sharpest is session_bucket=asia (46/71 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L23.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=92  W=21/L=71  WR=22.8%
- Sharpen: sharpest is session_bucket=asia (46/71 of losers there)
- **Sharp: n=51  W=5/L=46  WR=9.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=asia

### L24.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (38/59 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (38/59 of losers there)
- **Sharp: n=42  W=4/L=38  WR=9.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(56/27), H20d(10/5) | H20a(28/54), H20b(6/14) |
| H60 | H60e(56/27), H60d(12/4) | H60a(28/53), H60b(4/16) |
| T1 | T1c(64/36) | T1a(36/64) |
| T4 | T4c(71/29) | T4a(29/71) |
| BBP | — | — |
| RSI | RSI4(46/38) | RSI5(52/58) |
| ZS | ZS2(12/7) | — |
| strategy_id | — | — |
| direction_exec | short(64/36) | long(36/64) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
