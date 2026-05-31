# GBP_CAD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,155**  (W=2,509 / L=1,646)  -  WR: **60.4%**

## Session distribution

- ny_mid: n=1096  W=649/L=447  WR=59.2%
- london_open: n=796  W=483/L=313  WR=60.7%
- ny_close: n=743  W=481/L=262  WR=64.7%
- ny_open: n=538  W=302/L=236  WR=56.1%
- london: n=437  W=259/L=178  WR=59.3%
- asia: n=345  W=220/L=125  WR=63.8%
- off_hours: n=103  W=57/L=46  WR=55.3%
- asia_late: n=97  W=58/L=39  WR=59.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=273  W=233/L=40  WR=85.3%
- Refine: exclude H20=H20a drops 25/40 losers (62%)
- **Final: n=191  W=176/L=15  WR=92.1%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=271  W=233/L=38  WR=86.0%
- Refine: exclude H20=H20a drops 25/38 losers (66%)
- **Final: n=189  W=176/L=13  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=258  W=227/L=31  WR=88.0%
- Refine: exclude H20=H20a drops 25/31 losers (81%)
- **Final: n=176  W=170/L=6  WR=96.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=252  W=221/L=31  WR=87.7%
- Refine: exclude direction_exec=short drops 21/31 losers (68%)
- **Final: n=171  W=161/L=10  WR=94.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=london_open  •  AVOID when short

### W05.  `T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=226  W=202/L=24  WR=89.4%
- Refine: exclude T1=T1c drops 16/24 losers (67%)
- **Final: n=157  W=149/L=8  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when 1h trend AGAINST trade

### W06.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=226  W=202/L=24  WR=89.4%
- Refine: exclude T1=T1c drops 16/24 losers (67%)
- **Final: n=157  W=149/L=8  WR=94.9%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when 1h trend AGAINST trade

### W07.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=195  W=175/L=20  WR=89.7%
- Refine: exclude H20=H20a drops 16/20 losers (80%)
- **Final: n=125  W=121/L=4  WR=96.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W08.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=195  W=175/L=20  WR=89.7%
- Refine: exclude H20=H20a drops 16/20 losers (80%)
- **Final: n=125  W=121/L=4  WR=96.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=178  W=155/L=23  WR=87.1%
- Refine: exclude H20=H20a drops 16/23 losers (70%)
- **Final: n=108  W=101/L=7  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=177  W=156/L=21  WR=88.1%
- Refine: exclude H20=H20d drops 12/21 losers (57%)
- **Final: n=153  W=144/L=9  WR=94.1%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 mildly against

### W11.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=175  W=164/L=11  WR=93.7%
- Refine: exclude RSI=RSI4 drops 4/11 losers (36%)
- **Final: n=147  W=140/L=7  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W12.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=171  W=161/L=10  WR=94.2%
- Refine: exclude RSI=RSI4 drops 4/10 losers (40%)
- **Final: n=143  W=137/L=6  WR=95.8%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W13.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=165  W=149/L=16  WR=90.3%
- Refine: exclude H20=H20a drops 16/16 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W14.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=163  W=147/L=16  WR=90.2%
- Refine: exclude H20=H20d drops 11/16 losers (69%)
- **Final: n=140  W=135/L=5  WR=96.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 mildly against

### W15.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=157  W=149/L=8  WR=94.9%
- Refine: exclude RSI=RSI4 drops 4/8 losers (50%)
- **Final: n=137  W=133/L=4  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W16.  `T4=T4a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=157  W=149/L=8  WR=94.9%
- Refine: exclude RSI=RSI4 drops 4/8 losers (50%)
- **Final: n=137  W=133/L=4  WR=97.1%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W17.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=153  W=133/L=20  WR=86.9%
- Refine: exclude H20=H20d drops 12/20 losers (60%)
- **Final: n=129  W=121/L=8  WR=93.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=london_open  •  AVOID when HTF20 mildly against

### W18.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=142  W=123/L=19  WR=86.6%
- Refine: exclude H20=H20d drops 11/19 losers (58%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 mildly against

### W19.  `T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=132  W=119/L=13  WR=90.2%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=91  W=91/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF20 aligned WITH trade

### W20.  `H20=H20e AND T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=121  W=108/L=13  WR=89.3%
- Refine: exclude direction_exec=short drops 9/13 losers (69%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third; session=london_open  •  AVOID when short

### W21.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H60=H60c drops 11/17 losers (65%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W22.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude H60=H60c drops 11/17 losers (65%)
- **Final: n=95  W=89/L=6  WR=93.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W23.  `T1=T1a AND BBP=BBP6 AND session_bucket=ny_mid`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H60=H60d drops 15/17 losers (88%)
- **Final: n=98  W=96/L=2  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; session=ny_mid  •  AVOID when HTF60 mildly against

### W24.  `BBP=BBP6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H60=H60d drops 15/17 losers (88%)
- **Final: n=98  W=96/L=2  WR=98.0%**
- **Dir: LONG**  •  deep above upper band; session=ny_mid  •  AVOID when HTF60 mildly against

### W25.  `T1=T1a AND BBP=BBP6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude H60=H60d drops 15/17 losers (88%)
- **Final: n=98  W=96/L=2  WR=98.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; session=ny_mid  •  AVOID when HTF60 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=339  W=134/L=205  WR=39.5%
- Sharpen: sharpest is H60=H60d (46/205 of losers there)
- **Sharp: n=50  W=4/L=46  WR=8.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 mildly against

### L02.  `H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=245  W=98/L=147  WR=40.0%
- Sharpen: sharpest is T4=T4c (111/147 of losers there)
- **Sharp: n=148  W=37/L=111  WR=25.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=238  W=82/L=156  WR=34.5%
- Sharpen: sharpest is H60=H60d (46/156 of losers there)
- **Sharp: n=50  W=4/L=46  WR=8.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 mildly against

### L04.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=238  W=82/L=156  WR=34.5%
- Sharpen: sharpest is H60=H60d (46/156 of losers there)
- **Sharp: n=50  W=4/L=46  WR=8.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 mildly against

### L05.  `H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=232  W=92/L=140  WR=39.7%
- Sharpen: sharpest is T4=T4c (111/140 of losers there)
- **Sharp: n=148  W=37/L=111  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L06.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=232  W=92/L=140  WR=39.7%
- Sharpen: sharpest is T4=T4c (111/140 of losers there)
- **Sharp: n=148  W=37/L=111  WR=25.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L07.  `T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=230  W=89/L=141  WR=38.7%
- Sharpen: sharpest is direction_exec=short (97/141 of losers there)
- **Sharp: n=127  W=30/L=97  WR=23.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when short

### L08.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=224  W=72/L=152  WR=32.1%
- Sharpen: sharpest is BBP=BBP4 (98/152 of losers there)
- **Sharp: n=111  W=13/L=98  WR=11.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  ONLY when upper third

### L09.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=216  W=64/L=152  WR=29.6%
- Sharpen: sharpest is BBP=BBP4 (101/152 of losers there)
- **Sharp: n=112  W=11/L=101  WR=9.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when upper third

### L10.  `H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=202  W=72/L=130  WR=35.6%
- Sharpen: sharpest is T1=T1c (111/130 of losers there)
- **Sharp: n=148  W=37/L=111  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when 1h trend AGAINST trade

### L11.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=201  W=52/L=149  WR=25.9%
- Sharpen: sharpest is ZS=ZS4 (93/149 of losers there)
- **Sharp: n=102  W=9/L=93  WR=8.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L12.  `BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=192  W=73/L=119  WR=38.0%
- Sharpen: sharpest is T4=T4c (98/119 of losers there)
- **Sharp: n=111  W=13/L=98  WR=11.7%**
- **Dir: SHORT**  •  upper third; session=london_open  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=189  W=68/L=121  WR=36.0%
- Sharpen: sharpest is T4=T4c (101/121 of losers there)
- **Sharp: n=112  W=11/L=101  WR=9.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london_open  •  ONLY when 4h trend AGAINST trade

### L14.  `T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=186  W=50/L=136  WR=26.9%
- Sharpen: sharpest is T1=T1c (101/136 of losers there)
- **Sharp: n=112  W=11/L=101  WR=9.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=london_open  •  ONLY when 1h trend AGAINST trade

### L15.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=186  W=68/L=118  WR=36.6%
- Sharpen: sharpest is T4=T4c (98/118 of losers there)
- **Sharp: n=109  W=11/L=98  WR=10.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=london_open  •  ONLY when 4h trend AGAINST trade

### L16.  `ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: sharpest is T4=T4c (93/109 of losers there)
- **Sharp: n=104  W=11/L=93  WR=10.6%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend AGAINST trade

### L17.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: sharpest is T4=T4c (93/109 of losers there)
- **Sharp: n=104  W=11/L=93  WR=10.6%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=171  W=62/L=109  WR=36.3%
- Sharpen: sharpest is T4=T4c (93/109 of losers there)
- **Sharp: n=102  W=9/L=93  WR=8.8%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend AGAINST trade

### L19.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=171  W=62/L=109  WR=36.3%
- Sharpen: sharpest is T4=T4c (93/109 of losers there)
- **Sharp: n=102  W=9/L=93  WR=8.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend AGAINST trade

### L20.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=171  W=62/L=109  WR=36.3%
- Sharpen: sharpest is T4=T4c (93/109 of losers there)
- **Sharp: n=102  W=9/L=93  WR=8.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend AGAINST trade

### L21.  `T4=T4c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=166  W=41/L=125  WR=24.7%
- Sharpen: sharpest is T1=T1c (93/125 of losers there)
- **Sharp: n=102  W=9/L=93  WR=8.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L22.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=166  W=41/L=125  WR=24.7%
- Sharpen: sharpest is T1=T1c (93/125 of losers there)
- **Sharp: n=102  W=9/L=93  WR=8.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is T1=T1c (63/99 of losers there)
- **Sharp: n=80  W=17/L=63  WR=21.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L24.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=156  W=53/L=103  WR=34.0%
- Sharpen: sharpest is H60=H60e (30/103 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF60 strongly against

### L25.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=156  W=59/L=97  WR=37.8%
- Sharpen: sharpest is H20=H20b (18/97 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(15/20) |
| H60 | H60e(38/29) | H60d(8/13) |
| T1 | T1a(54/42) | T1c(46/58) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/44) | short(48/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
