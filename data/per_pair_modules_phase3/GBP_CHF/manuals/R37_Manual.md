# GBP_CHF — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,790**  (W=1,172 / L=618)  -  WR: **65.5%**

## Session distribution

- asia: n=1049  W=699/L=350  WR=66.6%
- ny_close: n=363  W=231/L=132  WR=63.6%
- asia_late: n=136  W=87/L=49  WR=64.0%
- off_hours: n=102  W=56/L=46  WR=54.9%
- london_open: n=68  W=49/L=19  WR=72.1%
- london: n=34  W=23/L=11  WR=67.6%
- ny_mid: n=30  W=21/L=9  WR=70.0%
- ny_open: n=8  W=6/L=2  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=146  W=125/L=21  WR=85.6%
- Refine: exclude H60=H60e drops 13/21 losers (62%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W02.  `H20=H20b AND H60=H60a AND T1=T1c`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude RSI=RSI5 drops 15/16 losers (94%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when RSI 60-70 strong

### W03.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude RSI=RSI5 drops 15/16 losers (94%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when RSI 60-70 strong

### W04.  `H20=H20b AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude RSI=RSI5 drops 15/16 losers (94%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when RSI 60-70 strong

### W05.  `H20=H20b AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude RSI=RSI5 drops 15/16 losers (94%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when RSI 60-70 strong

### W06.  `H20=H20b AND H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude RSI=RSI5 drops 15/16 losers (94%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 60-70 strong

### W07.  `H20=H20b AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude RSI=RSI5 drops 11/12 losers (92%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 60-70 strong

### W08.  `H20=H20b AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude RSI=RSI5 drops 11/12 losers (92%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W09.  `H20=H20a AND H60=H60a AND BBP=BBP4`
- Raw: n=68  W=59/L=9  WR=86.8%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  AVOID when 1h trend WITH trade

### W10.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude RSI=RSI4 drops 9/9 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W11.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude RSI=RSI4 drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when 1h trend WITH trade

### W13.  `H20=H20a AND H60=H60a AND ZS=ZS4`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W15.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude T4=T4c drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude T4=T4c drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when 4h trend AGAINST trade

### W17.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=62  W=55/L=7  WR=88.7%
- Refine: exclude H20=H20e drops 4/7 losers (57%)
- **Final: n=42  W=39/L=3  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong; session=asia  •  AVOID when HTF20 strongly against

### W18.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude T1=T1a drops 5/5 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when 1h trend WITH trade

### W19.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=59  W=54/L=5  WR=91.5%
- Refine: exclude RSI=RSI4 drops 5/5 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W20.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude T1=T1a drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  AVOID when 1h trend WITH trade

### W21.  `H20=H20c AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude T1=T1a drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade  •  AVOID when 1h trend WITH trade

### W22.  `H20=H20d AND T1=T1c AND session_bucket=asia`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W23.  `H20=H20d AND direction_exec=short AND session_bucket=asia`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; session=asia  •  AVOID when zscore +1 to +2 overbought

### W24.  `H20=H20d AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=57  W=52/L=5  WR=91.2%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W25.  `H20=H20a AND H60=H60b AND T4=T4a`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude session_bucket=ny_close drops 7/8 losers (88%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is T1=T1a (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 1h trend WITH trade

### L02.  `H20=H20d AND H60=H60e AND T1=T1a`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when RSI 70-80 overbought

### L03.  `H20=H20d AND H60=H60e AND direction_exec=long`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against  •  ONLY when RSI 70-80 overbought

### L04.  `H20=H20d AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 70-80 overbought

### L05.  `H20=H20d AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when RSI 70-80 overbought

### L06.  `H20=H20d AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is RSI=RSI6 (7/40 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 70-80 overbought

### L07.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is H20=H20e (12/39 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L08.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is H20=H20e (12/39 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L09.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is RSI=RSI5 (16/36 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_close (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=ny_close

### L11.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=51  W=18/L=33  WR=35.3%
- Sharpen: sharpest is RSI=RSI5 (16/33 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20c AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=50  W=18/L=32  WR=36.0%
- Sharpen: sharpest is session_bucket=ny_close (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=ny_close

### L13.  `T1=T1a AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is H20=H20e (18/31 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=off_hours  •  ONLY when HTF20 strongly against

### L14.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is H60=H60a (7/30 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L15.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is H60=H60a (7/30 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L16.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is H60=H60a (7/29 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L17.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is H60=H60a (7/29 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L18.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=46  W=15/L=31  WR=32.6%
- Sharpen: sharpest is H20=H20e (11/31 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong; session=asia  •  ONLY when HTF20 strongly against

### L19.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=45  W=12/L=33  WR=26.7%
- Sharpen: sharpest is RSI=RSI5 (16/33 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=45  W=15/L=30  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (17/30 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore -1 to +1 neutral; session=asia  •  ONLY when RSI 60-70 strong

### L21.  `H20=H20c AND T1=T1a AND RSI=RSI4`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_close (8/28 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_close

### L22.  `H20=H20c AND T4=T4c AND direction_exec=long`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is RSI=RSI5 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L23.  `H20=H20c AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=43  W=16/L=27  WR=37.2%
- Sharpen: sharpest is RSI=RSI5 (12/27 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20b AND H60=H60e AND session_bucket=asia`
- Raw: n=42  W=12/L=30  WR=28.6%
- Sharpen: sharpest is RSI=RSI4 (5/30 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  ONLY when RSI 50-60 upper neutral

### L25.  `H60=H60d AND T1=T1c AND session_bucket=asia`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is H20=H20e (24/28 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(36/26) | H20e(27/37) |
| H60 | H60a(43/36) | H60e(34/40) |
| T1 | T1c(55/45) | T1a(45/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/46) | long(44/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
