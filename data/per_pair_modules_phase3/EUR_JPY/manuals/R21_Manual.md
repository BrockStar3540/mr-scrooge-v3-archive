# EUR_JPY — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,634**  (W=2,757 / L=1,877)  -  WR: **59.5%**

## Session distribution

- asia: n=1743  W=1018/L=725  WR=58.4%
- london_open: n=856  W=504/L=352  WR=58.9%
- ny_mid: n=590  W=341/L=249  WR=57.8%
- ny_open: n=482  W=284/L=198  WR=58.9%
- ny_close: n=334  W=213/L=121  WR=63.8%
- london: n=326  W=207/L=119  WR=63.5%
- asia_late: n=230  W=144/L=86  WR=62.6%
- off_hours: n=73  W=46/L=27  WR=63.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=141  W=120/L=21  WR=85.1%
- Refine: exclude session_bucket=asia_late drops 7/21 losers (33%)
- **Final: n=132  W=118/L=14  WR=89.4%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak  •  AVOID when session=asia_late

### W02.  `H60=H60e AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W03.  `T1=T1a AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W04.  `BBP=BBP2 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: SHORT**  •  lower third; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W05.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W06.  `H60=H60e AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W07.  `T1=T1a AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=short`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W08.  `H60=H60e AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W09.  `T1=T1a AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W10.  `RSI=RSI1 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: SHORT**  •  RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W11.  `H60=H60e AND T1=T1a AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W12.  `H60=H60e AND BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W13.  `H60=H60e AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W14.  `T1=T1a AND BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W15.  `T1=T1a AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W16.  `BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=102  W=96/L=6  WR=94.1%**
- **Dir: SHORT**  •  lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W17.  `H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude BBP=BBP6 drops 5/13 losers (38%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when deep above upper band

### W18.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude BBP=BBP6 drops 5/13 losers (38%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when deep above upper band

### W19.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude BBP=BBP6 drops 5/13 losers (38%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when deep above upper band

### W20.  `H20=H20e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP0 drops 9/14 losers (64%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when deep below lower band

### W21.  `H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP0 drops 9/14 losers (64%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when deep below lower band

### W22.  `T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP0 drops 9/14 losers (64%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when deep below lower band

### W23.  `RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP0 drops 9/14 losers (64%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=asia  •  AVOID when deep below lower band

### W24.  `H20=H20e AND H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP0 drops 9/14 losers (64%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold; session=asia  •  AVOID when deep below lower band

### W25.  `H20=H20e AND T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP0 drops 9/14 losers (64%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 20-30 oversold; session=asia  •  AVOID when deep below lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=360  W=132/L=228  WR=36.7%
- Sharpen: sharpest is H20=H20a (149/228 of losers there)
- **Sharp: n=215  W=66/L=149  WR=30.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=348  W=128/L=220  WR=36.8%
- Sharpen: sharpest is H20=H20a (141/220 of losers there)
- **Sharp: n=203  W=62/L=141  WR=30.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L03.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=311  W=97/L=214  WR=31.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=311  W=97/L=214  WR=31.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia

### L04.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=296  W=96/L=200  WR=32.4%
- Sharpen: sharpest is RSI=RSI1 (47/200 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L05.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=284  W=92/L=192  WR=32.4%
- Sharpen: sharpest is RSI=RSI1 (47/192 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L06.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=246  W=90/L=156  WR=36.6%
- Sharpen: sharpest is H60=H60a (149/156 of losers there)
- **Sharp: n=215  W=66/L=149  WR=30.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L07.  `T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=226  W=84/L=142  WR=37.2%
- Sharpen: sharpest is session_bucket=london_open (34/142 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L08.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=224  W=84/L=140  WR=37.5%
- Sharpen: sharpest is BBP=BBP3 (44/140 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when middle of band

### L09.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=215  W=66/L=149  WR=30.7%
- Sharpen: sharpest is RSI=RSI1 (47/149 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L10.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=215  W=66/L=149  WR=30.7%
- Sharpen: sharpest is RSI=RSI1 (47/149 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L11.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=211  W=77/L=134  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=211  W=77/L=134  WR=36.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia

### L12.  `H60=H60a AND BBP=BBP1 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=208  W=82/L=126  WR=39.4%
- Sharpen: sharpest is T4=T4c (57/126 of losers there)
- **Sharp: n=77  W=20/L=57  WR=26.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=203  W=62/L=141  WR=30.5%
- Sharpen: sharpest is RSI=RSI1 (47/141 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L14.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=203  W=81/L=122  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (64/122 of losers there)
- **Sharp: n=79  W=15/L=64  WR=19.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L15.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=203  W=81/L=122  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (64/122 of losers there)
- **Sharp: n=79  W=15/L=64  WR=19.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when session=asia

### L16.  `T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=203  W=81/L=122  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (64/122 of losers there)
- **Sharp: n=79  W=15/L=64  WR=19.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L17.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=203  W=81/L=122  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (64/122 of losers there)
- **Sharp: n=79  W=15/L=64  WR=19.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L18.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=196  W=77/L=119  WR=39.3%
- Sharpen: sharpest is H20=H20a (76/119 of losers there)
- **Sharp: n=100  W=24/L=76  WR=24.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF20 aligned WITH trade

### L19.  `H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=192  W=69/L=123  WR=35.9%
- Sharpen: sharpest is session_bucket=london_open (34/123 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L20.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=192  W=69/L=123  WR=35.9%
- Sharpen: sharpest is session_bucket=london_open (34/123 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L21.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=190  W=69/L=121  WR=36.3%
- Sharpen: sharpest is session_bucket=london_open (34/121 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L22.  `H20=H20e AND T4=T4c AND RSI=RSI3`
- Raw: n=189  W=72/L=117  WR=38.1%
- Sharpen: sharpest is BBP=BBP3 (36/117 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when middle of band

### L23.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=188  W=69/L=119  WR=36.7%
- Sharpen: sharpest is H20=H20a (84/119 of losers there)
- **Sharp: n=112  W=28/L=84  WR=25.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF20 aligned WITH trade

### L24.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=176  W=69/L=107  WR=39.2%
- Sharpen: sharpest is H20=H20a (74/107 of losers there)
- **Sharp: n=97  W=23/L=74  WR=23.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L25.  `H20=H20a AND BBP=BBP1 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=171  W=60/L=111  WR=35.1%
- Sharpen: sharpest is T4=T4c (55/111 of losers there)
- **Sharp: n=71  W=16/L=55  WR=22.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(51/46) | long(49/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
