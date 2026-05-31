# NZD_CHF — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **914**  (W=582 / L=332)  -  WR: **63.7%**

## Session distribution

- ny_mid: n=355  W=233/L=122  WR=65.6%
- asia: n=289  W=173/L=116  WR=59.9%
- ny_close: n=122  W=86/L=36  WR=70.5%
- ny_open: n=79  W=50/L=29  WR=63.3%
- london_open: n=42  W=26/L=16  WR=61.9%
- london: n=24  W=12/L=12  WR=50.0%
- off_hours: n=3  W=2/L=1  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=86  W=84/L=2  WR=97.7%
- Refine: exclude H20=H20e drops 2/2 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when HTF20 strongly against

### W02.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H20=H20e drops 6/10 losers (60%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W03.  `H20=H20a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=76  W=71/L=5  WR=93.4%
- Refine: exclude T1=T1a drops 5/5 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W04.  `T1=T1c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20e drops 9/11 losers (82%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W05.  `ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20e drops 9/11 losers (82%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W06.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude H20=H20e drops 9/11 losers (82%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W07.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=73  W=67/L=6  WR=91.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=asia

### W08.  `H20=H20a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=71  W=66/L=5  WR=93.0%
- Refine: exclude session_bucket=ny_mid drops 3/5 losers (60%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=70  W=65/L=5  WR=92.9%
- Refine: exclude session_bucket=ny_mid drops 3/5 losers (60%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=ny_mid

### W10.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W11.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W12.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W13.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=66  W=65/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### W14.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=66  W=65/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong

### W15.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=66  W=65/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### W16.  `H20=H20a AND T1=T1a AND BBP=BBP6`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=asia

### W17.  `H20=H20a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band  •  AVOID when session=asia

### W18.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=asia

### W19.  `H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=asia

### W20.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=asia

### W21.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when session=asia

### W22.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=asia

### W23.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude session_bucket=asia drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when session=asia

### W24.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=64  W=59/L=5  WR=92.2%
- Refine: exclude session_bucket=ny_mid drops 3/5 losers (60%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=ny_mid

### W25.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=64  W=59/L=5  WR=92.2%
- Refine: exclude session_bucket=ny_mid drops 3/5 losers (60%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND direction_exec=long`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is ZS=ZS5 (19/45 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (28/35 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L03.  `H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (28/35 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L04.  `H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (28/35 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is RSI=RSI5 (28/35 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=54  W=19/L=35  WR=35.2%
- Sharpen: sharpest is session_bucket=asia (19/35 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L07.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=54  W=20/L=34  WR=37.0%
- Sharpen: sharpest is H20=H20a (23/34 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L08.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is RSI=RSI6 (15/29 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L09.  `H60=H60d AND T4=T4c AND RSI=RSI5`
- Raw: n=45  W=9/L=36  WR=20.0%
- Sharpen: sharpest is H20=H20e (12/36 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L10.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L11.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L12.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L13.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is RSI=RSI6 (10/28 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L14.  `H20=H20b AND H60=H60d AND T1=T1c`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L15.  `H20=H20b AND H60=H60d AND T4=T4c`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L16.  `H20=H20b AND H60=H60d AND direction_exec=short`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 mildly against  •  ONLY when zscore -1 to +1 neutral

### L17.  `H20=H20b AND H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L18.  `H20=H20b AND H60=H60d AND T1=T1c AND direction_exec=short`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L19.  `H20=H20b AND H60=H60d AND T4=T4c AND direction_exec=short`
- Raw: n=39  W=11/L=28  WR=28.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 mildly against; 4h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L20.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=38  W=5/L=33  WR=13.2%
- Sharpen: sharpest is ZS=ZS4 (15/33 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L21.  `H60=H60d AND T1=T1c AND RSI=RSI5`
- Raw: n=36  W=8/L=28  WR=22.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore -1 to +1 neutral

### L22.  `H60=H60d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=36  W=8/L=28  WR=22.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 60-70 strong  •  ONLY when zscore -1 to +1 neutral

### L23.  `H60=H60d AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=36  W=8/L=28  WR=22.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore -1 to +1 neutral

### L24.  `H60=H60d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=36  W=8/L=28  WR=22.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore -1 to +1 neutral

### L25.  `H60=H60d AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=36  W=8/L=28  WR=22.2%
- Sharpen: sharpest is ZS=ZS3 (6/28 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore -1 to +1 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(46/33) | H20e(32/45) |
| H60 | H60b(16/3), H60a(42/32) | H60e(29/42), H60d(4/16) |
| T1 | — | — |
| T4 | T4a(62/37) | T4c(38/63) |
| BBP | BBP6(22/16) | — |
| RSI | RSI5(72/66) | RSI6(12/17) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | asia(30/35) |

*Read: `bucket(winner%/loser%)`.*
