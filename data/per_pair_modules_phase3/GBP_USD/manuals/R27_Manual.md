# GBP_USD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,268**  (W=2,607 / L=1,661)  -  WR: **61.1%**

## Session distribution

- ny_mid: n=1687  W=1005/L=682  WR=59.6%
- ny_close: n=626  W=409/L=217  WR=65.3%
- ny_open: n=620  W=381/L=239  WR=61.5%
- london_open: n=611  W=371/L=240  WR=60.7%
- asia: n=367  W=218/L=149  WR=59.4%
- london: n=314  W=197/L=117  WR=62.7%
- asia_late: n=38  W=24/L=14  WR=63.2%
- off_hours: n=5  W=2/L=3  WR=40.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS3 drops 11/12 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W02.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS3 drops 11/12 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W03.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS3 drops 11/12 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W04.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS3 drops 11/12 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS3 drops 11/12 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W06.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude ZS=ZS3 drops 11/12 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND ZS=ZS3`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london drops 3/12 losers (25%)
- **Final: n=72  W=63/L=9  WR=87.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; zscore -1 to +1 neutral  •  AVOID when session=london

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND ZS=ZS3`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london drops 3/12 losers (25%)
- **Final: n=72  W=63/L=9  WR=87.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore -1 to +1 neutral  •  AVOID when session=london

### W09.  `H20=H20a AND RSI=RSI6 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london drops 3/12 losers (25%)
- **Final: n=72  W=63/L=9  WR=87.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore -1 to +1 neutral  •  AVOID when session=london

### W10.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude strategy_id=MR2_bb_reversion_short drops 3/11 losers (27%)
- **Final: n=66  W=58/L=8  WR=87.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when strategy=MR2_bb_reversion_short

### W11.  `H20=H20e AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude strategy_id=MR2_bb_reversion_short drops 3/11 losers (27%)
- **Final: n=66  W=58/L=8  WR=87.9%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 70-80 overbought  •  AVOID when strategy=MR2_bb_reversion_short

### W12.  `H20=H20a AND H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W13.  `H20=H20a AND H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W14.  `H20=H20a AND H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W15.  `H20=H20a AND BBP=BBP4 AND session_bucket=london`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london  •  AVOID when RSI 70-80 overbought

### W16.  `H20=H20a AND H60=H60e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=67  W=61/L=6  WR=91.0%
- Refine: exclude session_bucket=ny_close drops 6/6 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W17.  `H20=H20a AND ZS=ZS4 AND session_bucket=london`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=london  •  AVOID when RSI 70-80 overbought

### W18.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=67  W=58/L=9  WR=86.6%
- Refine: exclude RSI=RSI6 drops 4/9 losers (44%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=london  •  AVOID when RSI 70-80 overbought

### W19.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W20.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W21.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W22.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W23.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W24.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_open

### W25.  `H20=H20a AND BBP=BBP3 AND RSI=RSI6`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude session_bucket=london drops 3/9 losers (33%)
- **Final: n=55  W=49/L=6  WR=89.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 70-80 overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=251  W=96/L=155  WR=38.2%
- Sharpen: sharpest is T1=T1c (142/155 of losers there)
- **Sharp: n=214  W=72/L=142  WR=33.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=214  W=72/L=142  WR=33.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=214  W=72/L=142  WR=33.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L03.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=214  W=72/L=142  WR=33.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=214  W=72/L=142  WR=33.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=169  W=58/L=111  WR=34.3%
- Sharpen: sharpest is ZS=ZS5 (36/111 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H20=H20e AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: sharpest is RSI=RSI6 (68/88 of losers there)
- **Sharp: n=91  W=23/L=68  WR=25.3%**
- **Dir: ?**  •  HTF20 strongly against; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L06.  `H20=H20a AND H60=H60d AND T1=T1a`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is BBP=BBP5 (29/89 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  ONLY when just touched upper band

### L07.  `H20=H20a AND H60=H60d AND T4=T4a`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is BBP=BBP5 (29/89 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  ONLY when just touched upper band

### L08.  `H20=H20a AND H60=H60d AND direction_exec=long`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is BBP=BBP5 (29/89 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  ONLY when just touched upper band

### L09.  `H20=H20a AND H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is BBP=BBP5 (29/89 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched upper band

### L10.  `H20=H20a AND H60=H60d AND T1=T1a AND direction_exec=long`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is BBP=BBP5 (29/89 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  ONLY when just touched upper band

### L11.  `H20=H20a AND H60=H60d AND T4=T4a AND direction_exec=long`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is BBP=BBP5 (29/89 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  ONLY when just touched upper band

### L12.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=127  W=40/L=87  WR=31.5%
- Sharpen: sharpest is H20=H20d (33/87 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L13.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=127  W=40/L=87  WR=31.5%
- Sharpen: sharpest is H20=H20d (33/87 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L14.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=127  W=40/L=87  WR=31.5%
- Sharpen: sharpest is H20=H20d (33/87 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L15.  `T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is BBP=BBP6 (21/73 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when deep above upper band

### L16.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=114  W=42/L=72  WR=36.8%
- Sharpen: sharpest is RSI=RSI6 (52/72 of losers there)
- **Sharp: n=61  W=9/L=52  WR=14.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L17.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is H20=H20d (17/71 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L18.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is H20=H20d (17/71 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L19.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when deep above upper band

### L20.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (21/66 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when deep above upper band

### L21.  `H20=H20d AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is ZS=ZS5 (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H60=H60d AND T1=T1a AND RSI=RSI5`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is BBP=BBP2 (18/71 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when lower third

### L23.  `H60=H60d AND RSI=RSI5 AND direction_exec=long`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is BBP=BBP2 (18/71 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 60-70 strong  •  ONLY when lower third

### L24.  `H60=H60d AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=99  W=28/L=71  WR=28.3%
- Sharpen: sharpest is BBP=BBP2 (18/71 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when lower third

### L25.  `H60=H60d AND T4=T4a AND RSI=RSI5`
- Raw: n=98  W=28/L=70  WR=28.6%
- Sharpen: sharpest is BBP=BBP2 (18/70 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
