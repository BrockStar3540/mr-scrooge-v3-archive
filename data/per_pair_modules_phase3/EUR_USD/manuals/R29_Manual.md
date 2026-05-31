# EUR_USD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,017**  (W=1,841 / L=1,176)  -  WR: **61.0%**

## Session distribution

- asia: n=800  W=498/L=302  WR=62.3%
- ny_close: n=552  W=343/L=209  WR=62.1%
- ny_mid: n=544  W=332/L=212  WR=61.0%
- london_open: n=443  W=279/L=164  WR=63.0%
- ny_open: n=335  W=188/L=147  WR=56.1%
- london: n=211  W=127/L=84  WR=60.2%
- off_hours: n=89  W=51/L=38  WR=57.3%
- asia_late: n=43  W=23/L=20  WR=53.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI7 drops 4/16 losers (25%)
- **Final: n=107  W=95/L=12  WR=88.8%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W02.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI7 drops 4/16 losers (25%)
- **Final: n=107  W=95/L=12  WR=88.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when RSI>80 extreme overbought

### W03.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/14 losers (21%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W04.  `H60=H60e AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/14 losers (21%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W05.  `H60=H60e AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=96  W=85/L=11  WR=88.5%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF20 strongly against

### W06.  `H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/12 losers (17%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W08.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/12 losers (17%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W09.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/13 losers (23%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W10.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude RSI=RSI6 drops 12/12 losers (100%)
- **Final: n=17  W=17/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; session=ny_close  •  AVOID when RSI 70-80 overbought

### W11.  `H20=H20e AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude RSI=RSI6 drops 12/12 losers (100%)
- **Final: n=17  W=17/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; session=ny_close  •  AVOID when RSI 70-80 overbought

### W12.  `H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when HTF20 aligned WITH trade

### W13.  `H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude H20=H20a drops 12/13 losers (92%)
- **Final: n=23  W=22/L=1  WR=95.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60a AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W18.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/11 losers (18%)
- **Final: n=80  W=71/L=9  WR=88.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W19.  `H20=H20e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/11 losers (18%)
- **Final: n=80  W=71/L=9  WR=88.8%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W20.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/11 losers (18%)
- **Final: n=80  W=71/L=9  WR=88.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_close  •  AVOID when strategy=bravo_expansion_continuation

### W21.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude ZS=ZS3 drops 3/11 losers (27%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude ZS=ZS3 drops 3/11 losers (27%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude ZS=ZS3 drops 3/11 losers (27%)
- **Final: n=74  W=66/L=8  WR=89.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude RSI=RSI6 drops 11/11 losers (100%)
- **Final: n=17  W=17/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; session=ny_close  •  AVOID when RSI 70-80 overbought

### W25.  `H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude RSI=RSI6 drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 70-80 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60c AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; session=asia  •  ONLY when just touched upper band

### L02.  `H60=H60c AND T1=T1c AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L03.  `H60=H60c AND T4=T4c AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L04.  `H60=H60c AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; session=asia  •  ONLY when just touched upper band

### L05.  `H20=H20e AND H60=H60c AND T1=T1c AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L06.  `H20=H20e AND H60=H60c AND T4=T4c AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L07.  `H20=H20e AND H60=H60c AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 neutral; session=asia  •  ONLY when just touched upper band

### L08.  `H60=H60c AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L09.  `H60=H60c AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L10.  `H60=H60c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is BBP=BBP5 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend AGAINST trade; session=asia  •  ONLY when just touched upper band

### L11.  `H20=H20e AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L12.  `T1=T1c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L13.  `T4=T4c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L14.  `RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L17.  `H20=H20e AND RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI7 AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L19.  `T1=T1c AND RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L20.  `T4=T4c AND RSI=RSI7 AND direction_exec=short AND session_bucket=asia`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is BBP=BBP5 (20/69 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI>80 extreme overbought; session=asia  •  ONLY when just touched upper band

### L21.  `H60=H60a AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is ZS=ZS4 (41/61 of losers there)
- **Sharp: n=57  W=16/L=41  WR=28.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when zscore +1 to +2 overbought

### L22.  `H60=H60a AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is RSI=RSI6 (53/59 of losers there)
- **Sharp: n=77  W=24/L=53  WR=31.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 70-80 overbought

### L23.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is RSI=RSI6 (53/59 of losers there)
- **Sharp: n=77  W=24/L=53  WR=31.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_close  •  ONLY when RSI 70-80 overbought

### L24.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=32/L=59  WR=35.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; session=ny_close

### L25.  `H60=H60a AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=32/L=59  WR=35.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(36/41) |
| H60 | H60a(45/38) | — |
| T1 | — | — |
| T4 | T4a(51/45) | T4c(49/55) |
| BBP | — | — |
| RSI | — | RSI7(17/22) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
