# EUR_NZD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,586**  (W=2,688 / L=1,898)  -  WR: **58.6%**

## Session distribution

- ny_mid: n=1515  W=900/L=615  WR=59.4%
- asia: n=1076  W=618/L=458  WR=57.4%
- london_open: n=1064  W=633/L=431  WR=59.5%
- ny_open: n=335  W=197/L=138  WR=58.8%
- ny_close: n=295  W=170/L=125  WR=57.6%
- off_hours: n=211  W=119/L=92  WR=56.4%
- london: n=61  W=33/L=28  WR=54.1%
- asia_late: n=29  W=18/L=11  WR=62.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 16/25 losers (64%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W02.  `H20=H20c AND H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 16/25 losers (64%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 strongly against; RSI 60-70 strong  •  AVOID when session=ny_mid

### W03.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=145  W=133/L=12  WR=91.7%
- Refine: exclude H20=H20c drops 6/12 losers (50%)
- **Final: n=139  W=133/L=6  WR=95.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W04.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude H20=H20d drops 7/19 losers (37%)
- **Final: n=120  W=108/L=12  WR=90.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W05.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude H20=H20d drops 7/19 losers (37%)
- **Final: n=120  W=108/L=12  WR=90.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W06.  `H20=H20b AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=122  W=105/L=17  WR=86.1%
- Refine: exclude BBP=BBP5 drops 17/17 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W07.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude H60=H60e drops 11/11 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W08.  `H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W09.  `H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_close  •  AVOID when HTF20 strongly against

### W10.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W11.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 strongly against

### W12.  `H60=H60e AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 strongly against

### W13.  `H20=H20b AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude BBP=BBP5 drops 10/10 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W14.  `H20=H20b AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude BBP=BBP5 drops 10/10 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W15.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/9 losers (33%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W16.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude H60=H60a drops 5/5 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20b AND H60=H60e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude session_bucket=ny_close drops 7/7 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W18.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20c drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 neutral

### W19.  `H20=H20b AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when upper third

### W20.  `H20=H20b AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when upper third

### W21.  `H20=H20b AND H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude BBP=BBP4 drops 7/10 losers (70%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; session=london_open  •  AVOID when upper third

### W22.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude H20=H20e drops 7/8 losers (88%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_close  •  AVOID when HTF20 strongly against

### W23.  `H20=H20a AND H60=H60d AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 60-70 strong; session=ny_mid  •  AVOID when 4h trend WITH trade

### W24.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude H20=H20e drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=285  W=106/L=179  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (72/179 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=285  W=106/L=179  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (72/179 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=285  W=106/L=179  WR=37.2%
- Sharpen: sharpest is ZS=ZS5 (72/179 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=173  W=67/L=106  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_close (33/106 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L05.  `H20=H20c AND H60=H60a AND T1=T1c`
- Raw: n=168  W=63/L=105  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_close (33/105 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L06.  `H20=H20c AND H60=H60a AND direction_exec=short`
- Raw: n=168  W=63/L=105  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_close (33/105 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade  •  ONLY when session=ny_close

### L07.  `H20=H20c AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=168  W=63/L=105  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_close (33/105 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L08.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is H20=H20e (38/102 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L09.  `T4=T4a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is H20=H20e (38/102 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L10.  `H20=H20c AND H60=H60a AND RSI=RSI5`
- Raw: n=147  W=47/L=100  WR=32.0%
- Sharpen: sharpest is session_bucket=ny_close (32/100 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L11.  `H20=H20c AND T1=T1c AND RSI=RSI5`
- Raw: n=147  W=50/L=97  WR=34.0%
- Sharpen: sharpest is session_bucket=ny_close (32/97 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L12.  `H20=H20c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=50/L=97  WR=34.0%
- Sharpen: sharpest is session_bucket=ny_close (32/97 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 60-70 strong  •  ONLY when session=ny_close

### L13.  `H20=H20c AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=50/L=97  WR=34.0%
- Sharpen: sharpest is session_bucket=ny_close (32/97 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L14.  `H20=H20e AND T1=T1c AND ZS=ZS3`
- Raw: n=146  W=58/L=88  WR=39.7%
- Sharpen: sharpest is RSI=RSI5 (73/88 of losers there)
- **Sharp: n=110  W=37/L=73  WR=33.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 60-70 strong

### L15.  `H20=H20e AND T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is RSI=RSI5 (73/87 of losers there)
- **Sharp: n=110  W=37/L=73  WR=33.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20c AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=142  W=46/L=96  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (32/96 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L17.  `H20=H20c AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=142  W=46/L=96  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (32/96 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L18.  `H60=H60a AND T1=T1c AND BBP=BBP5`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is H20=H20c (30/84 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  ONLY when HTF20 neutral

### L19.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is H20=H20c (30/84 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 neutral

### L20.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is H20=H20c (30/84 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  ONLY when HTF20 neutral

### L21.  `H20=H20d AND T1=T1c AND RSI=RSI5`
- Raw: n=138  W=55/L=83  WR=39.9%
- Sharpen: sharpest is H60=H60a (57/83 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=138  W=55/L=83  WR=39.9%
- Sharpen: sharpest is H60=H60a (57/83 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=138  W=55/L=83  WR=39.9%
- Sharpen: sharpest is H60=H60a (57/83 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 aligned WITH trade

### L24.  `H20=H20d AND H60=H60a AND T1=T1c`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (57/81 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L25.  `H20=H20d AND H60=H60a AND direction_exec=short`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is RSI=RSI5 (57/81 of losers there)
- **Sharp: n=71  W=14/L=57  WR=19.7%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 aligned WITH trade  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(44/38) | H60a(38/44) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
