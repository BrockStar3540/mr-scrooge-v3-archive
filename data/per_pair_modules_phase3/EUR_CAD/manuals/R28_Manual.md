# EUR_CAD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,305**  (W=1,459 / L=846)  -  WR: **63.3%**

## Session distribution

- asia: n=850  W=546/L=304  WR=64.2%
- ny_close: n=513  W=327/L=186  WR=63.7%
- london_open: n=227  W=136/L=91  WR=59.9%
- london: n=204  W=128/L=76  WR=62.7%
- ny_open: n=195  W=117/L=78  WR=60.0%
- asia_late: n=139  W=99/L=40  WR=71.2%
- ny_mid: n=119  W=68/L=51  WR=57.1%
- off_hours: n=58  W=38/L=20  WR=65.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=214  W=193/L=21  WR=90.2%
- Refine: exclude session_bucket=ny_mid drops 12/21 losers (57%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W02.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=214  W=193/L=21  WR=90.2%
- Refine: exclude session_bucket=ny_mid drops 12/21 losers (57%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W03.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=214  W=193/L=21  WR=90.2%
- Refine: exclude session_bucket=ny_mid drops 12/21 losers (57%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W04.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=214  W=193/L=21  WR=90.2%
- Refine: exclude session_bucket=ny_mid drops 12/21 losers (57%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W05.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=214  W=193/L=21  WR=90.2%
- Refine: exclude session_bucket=ny_mid drops 12/21 losers (57%)
- **Final: n=182  W=173/L=9  WR=95.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 9/14 losers (64%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W07.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 9/14 losers (64%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W08.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 9/14 losers (64%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W09.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 9/14 losers (64%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=151  W=137/L=14  WR=90.7%
- Refine: exclude session_bucket=ny_mid drops 9/14 losers (64%)
- **Final: n=124  W=119/L=5  WR=96.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W11.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=135  W=125/L=10  WR=92.6%
- Refine: exclude session_bucket=ny_mid drops 9/10 losers (90%)
- **Final: n=108  W=107/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W12.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=135  W=125/L=10  WR=92.6%
- Refine: exclude session_bucket=ny_mid drops 9/10 losers (90%)
- **Final: n=108  W=107/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W13.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W14.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W15.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W17.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W18.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude ZS=ZS3 drops 7/14 losers (50%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W19.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=120  W=112/L=8  WR=93.3%
- Refine: exclude H60=H60c drops 6/8 losers (75%)
- **Final: n=85  W=83/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 neutral

### W20.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=112  W=104/L=8  WR=92.9%
- Refine: exclude H60=H60c drops 6/8 losers (75%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 neutral

### W21.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=112  W=104/L=8  WR=92.9%
- Refine: exclude H60=H60c drops 6/8 losers (75%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 neutral

### W22.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

### W23.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude session_bucket=ny_mid drops 9/12 losers (75%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=ny_mid

### W24.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=103  W=91/L=12  WR=88.3%
- Refine: exclude session_bucket=ny_mid drops 9/12 losers (75%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=ny_mid

### W25.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude H60=H60e drops 13/13 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=asia  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=201  W=70/L=131  WR=34.8%
- Sharpen: sharpest is direction_exec=short (128/131 of losers there)
- **Sharp: n=170  W=42/L=128  WR=24.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when short

### L02.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=170  W=42/L=128  WR=24.7%
- Sharpen: sharpest is H60=H60e (88/128 of losers there)
- **Sharp: n=110  W=22/L=88  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L03.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=170  W=42/L=128  WR=24.7%
- Sharpen: sharpest is H60=H60e (88/128 of losers there)
- **Sharp: n=110  W=22/L=88  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L04.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=169  W=42/L=127  WR=24.9%
- Sharpen: sharpest is H60=H60e (87/127 of losers there)
- **Sharp: n=109  W=22/L=87  WR=20.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L05.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=169  W=42/L=127  WR=24.9%
- Sharpen: sharpest is H60=H60e (87/127 of losers there)
- **Sharp: n=109  W=22/L=87  WR=20.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=169  W=42/L=127  WR=24.9%
- Sharpen: sharpest is H60=H60e (87/127 of losers there)
- **Sharp: n=109  W=22/L=87  WR=20.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L07.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=152  W=54/L=98  WR=35.5%
- Sharpen: sharpest is direction_exec=short (95/98 of losers there)
- **Sharp: n=121  W=26/L=95  WR=21.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when short

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=141  W=50/L=91  WR=35.5%
- Sharpen: sharpest is direction_exec=short (88/91 of losers there)
- **Sharp: n=110  W=22/L=88  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when short

### L09.  `H20=H20e AND T4=T4a AND ZS=ZS5`
- Raw: n=131  W=47/L=84  WR=35.9%
- Sharpen: sharpest is RSI=RSI6 (44/84 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L10.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=131  W=47/L=84  WR=35.9%
- Sharpen: sharpest is RSI=RSI6 (44/84 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L11.  `H20=H20e AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=131  W=47/L=84  WR=35.9%
- Sharpen: sharpest is RSI=RSI6 (44/84 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L12.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=129  W=46/L=83  WR=35.7%
- Sharpen: sharpest is RSI=RSI6 (44/83 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L13.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=121  W=26/L=95  WR=21.5%
- Sharpen: sharpest is BBP=BBP5 (23/95 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when just touched upper band

### L14.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=121  W=26/L=95  WR=21.5%
- Sharpen: sharpest is BBP=BBP5 (23/95 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L15.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=120  W=26/L=94  WR=21.7%
- Sharpen: sharpest is BBP=BBP5 (23/94 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L16.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=120  W=26/L=94  WR=21.7%
- Sharpen: sharpest is BBP=BBP5 (23/94 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L17.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=120  W=26/L=94  WR=21.7%
- Sharpen: sharpest is BBP=BBP5 (23/94 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

### L18.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (39/73 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  ONLY when upper third

### L19.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (39/73 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  ONLY when upper third

### L20.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (39/73 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_close  •  ONLY when upper third

### L21.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (39/73 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  ONLY when upper third

### L22.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (39/73 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  ONLY when upper third

### L23.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is BBP=BBP4 (39/73 of losers there)
- **Sharp: n=46  W=7/L=39  WR=15.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  ONLY when upper third

### L24.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=110  W=22/L=88  WR=20.0%
- Sharpen: sharpest is BBP=BBP5 (23/88 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when just touched upper band

### L25.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=109  W=22/L=87  WR=20.2%
- Sharpen: sharpest is BBP=BBP5 (23/87 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when just touched upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(53/41) | H20e(41/53) |
| H60 | H60a(45/39) | H60e(39/45) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
