# AUD_CAD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,344**  (W=1,477 / L=867)  -  WR: **63.0%**

## Session distribution

- asia: n=697  W=439/L=258  WR=63.0%
- ny_mid: n=480  W=300/L=180  WR=62.5%
- london_open: n=410  W=261/L=149  WR=63.7%
- ny_open: n=335  W=215/L=120  WR=64.2%
- ny_close: n=150  W=87/L=63  WR=58.0%
- london: n=122  W=83/L=39  WR=68.0%
- asia_late: n=119  W=76/L=43  WR=63.9%
- off_hours: n=31  W=16/L=15  WR=51.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=159  W=140/L=19  WR=88.1%
- Refine: exclude BBP=BBP4 drops 13/19 losers (68%)
- **Final: n=100  W=94/L=6  WR=94.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when upper third

### W02.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude BBP=BBP4 drops 13/23 losers (57%)
- **Final: n=100  W=90/L=10  WR=90.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  AVOID when upper third

### W03.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=158  W=139/L=19  WR=88.0%
- Refine: exclude ZS=ZS4 drops 11/19 losers (58%)
- **Final: n=103  W=95/L=8  WR=92.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W04.  `H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude BBP=BBP4 drops 13/18 losers (72%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when upper third

### W05.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude BBP=BBP4 drops 13/18 losers (72%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when upper third

### W06.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=150  W=136/L=14  WR=90.7%
- Refine: exclude ZS=ZS4 drops 11/14 losers (79%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=150  W=136/L=14  WR=90.7%
- Refine: exclude ZS=ZS4 drops 11/14 losers (79%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W08.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=150  W=132/L=18  WR=88.0%
- Refine: exclude ZS=ZS4 drops 11/18 losers (61%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W09.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=150  W=132/L=18  WR=88.0%
- Refine: exclude ZS=ZS4 drops 11/18 losers (61%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W10.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=142  W=129/L=13  WR=90.8%
- Refine: exclude ZS=ZS4 drops 11/13 losers (85%)
- **Final: n=87  W=85/L=2  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W11.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 7/17 losers (41%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=126  W=112/L=14  WR=88.9%
- Refine: exclude RSI=RSI4 drops 7/14 losers (50%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=126  W=112/L=14  WR=88.9%
- Refine: exclude RSI=RSI4 drops 7/14 losers (50%)
- **Final: n=93  W=86/L=7  WR=92.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W14.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude ZS=ZS3 drops 7/16 losers (44%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude ZS=ZS3 drops 7/16 losers (44%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=123  W=111/L=12  WR=90.2%
- Refine: exclude H60=H60d drops 3/12 losers (25%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF60 mildly against

### W17.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=123  W=111/L=12  WR=90.2%
- Refine: exclude H60=H60d drops 3/12 losers (25%)
- **Final: n=117  W=108/L=9  WR=92.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF60 mildly against

### W18.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude RSI=RSI4 drops 7/13 losers (54%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W19.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=117  W=108/L=9  WR=92.3%
- Refine: exclude ZS=ZS4 drops 6/9 losers (67%)
- **Final: n=75  W=72/L=3  WR=96.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W20.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude H60=H60d drops 3/11 losers (27%)
- **Final: n=109  W=101/L=8  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 mildly against

### W21.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude BBP=BBP5 drops 3/10 losers (30%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W22.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude BBP=BBP5 drops 3/10 losers (30%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W23.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude BBP=BBP5 drops 3/10 losers (30%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W24.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude H60=H60d drops 3/9 losers (33%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when HTF60 mildly against

### W25.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude H60=H60d drops 3/9 losers (33%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when HTF60 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=156  W=60/L=96  WR=38.5%
- Sharpen: sharpest is RSI=RSI5 (72/96 of losers there)
- **Sharp: n=94  W=22/L=72  WR=23.4%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L02.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=142  W=54/L=88  WR=38.0%
- Sharpen: sharpest is T1=T1c (80/88 of losers there)
- **Sharp: n=113  W=33/L=80  WR=29.2%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L03.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=139  W=51/L=88  WR=36.7%
- Sharpen: sharpest is RSI=RSI5 (72/88 of losers there)
- **Sharp: n=99  W=27/L=72  WR=27.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L04.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=134  W=46/L=88  WR=34.3%
- Sharpen: sharpest is RSI=RSI5 (72/88 of losers there)
- **Sharp: n=94  W=22/L=72  WR=23.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L05.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=134  W=46/L=88  WR=34.3%
- Sharpen: sharpest is RSI=RSI5 (72/88 of losers there)
- **Sharp: n=94  W=22/L=72  WR=23.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=130  W=42/L=88  WR=32.3%
- Sharpen: sharpest is BBP=BBP6 (24/88 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when deep above upper band

### L07.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=130  W=42/L=88  WR=32.3%
- Sharpen: sharpest is BBP=BBP6 (24/88 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when deep above upper band

### L08.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is RSI=RSI5 (61/77 of losers there)
- **Sharp: n=86  W=25/L=61  WR=29.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L09.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is RSI=RSI5 (61/77 of losers there)
- **Sharp: n=86  W=25/L=61  WR=29.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L10.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is RSI=RSI5 (61/77 of losers there)
- **Sharp: n=81  W=20/L=61  WR=24.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L11.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=117  W=40/L=77  WR=34.2%
- Sharpen: sharpest is T1=T1c (69/77 of losers there)
- **Sharp: n=95  W=26/L=69  WR=27.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L12.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=113  W=33/L=80  WR=29.2%
- Sharpen: sharpest is BBP=BBP6 (24/80 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L13.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=113  W=33/L=80  WR=29.2%
- Sharpen: sharpest is BBP=BBP6 (24/80 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L14.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=108  W=28/L=80  WR=25.9%
- Sharpen: sharpest is BBP=BBP6 (24/80 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L15.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=100  W=31/L=69  WR=31.0%
- Sharpen: sharpest is BBP=BBP6 (14/69 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when deep above upper band

### L16.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=99  W=27/L=72  WR=27.3%
- Sharpen: sharpest is BBP=BBP6 (23/72 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L17.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=27/L=72  WR=27.3%
- Sharpen: sharpest is BBP=BBP6 (23/72 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L18.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=27/L=72  WR=27.3%
- Sharpen: sharpest is BBP=BBP6 (23/72 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L19.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=94  W=22/L=72  WR=23.4%
- Sharpen: sharpest is BBP=BBP6 (23/72 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=94  W=22/L=72  WR=23.4%
- Sharpen: sharpest is BBP=BBP6 (23/72 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L21.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=94  W=22/L=72  WR=23.4%
- Sharpen: sharpest is BBP=BBP6 (23/72 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L22.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=94  W=32/L=62  WR=34.0%
- Sharpen: sharpest is H60=H60e (61/62 of losers there)
- **Sharp: n=81  W=20/L=61  WR=24.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=89  W=25/L=64  WR=28.1%
- Sharpen: sharpest is BBP=BBP6 (23/64 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L24.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=89  W=25/L=64  WR=28.1%
- Sharpen: sharpest is BBP=BBP6 (23/64 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

### L25.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=89  W=25/L=64  WR=28.1%
- Sharpen: sharpest is BBP=BBP6 (23/64 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/35) | H20e(37/49) |
| H60 | H60a(50/42) | H60e(41/52) |
| T1 | T1a(53/45) | T1c(46/55) |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/45) | short(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
