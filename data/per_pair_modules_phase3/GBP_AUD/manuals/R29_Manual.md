# GBP_AUD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,165**  (W=1,711 / L=1,454)  -  WR: **54.1%**

## Session distribution

- asia: n=750  W=398/L=352  WR=53.1%
- london_open: n=663  W=376/L=287  WR=56.7%
- ny_open: n=507  W=273/L=234  WR=53.8%
- ny_mid: n=493  W=237/L=256  WR=48.1%
- london: n=371  W=223/L=148  WR=60.1%
- ny_close: n=227  W=118/L=109  WR=52.0%
- off_hours: n=85  W=48/L=37  WR=56.5%
- asia_late: n=69  W=38/L=31  WR=55.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W02.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W03.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W04.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W07.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude T4=T4c drops 10/11 losers (91%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W08.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london_open drops 9/12 losers (75%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W09.  `T4=T4a AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude session_bucket=london_open drops 9/12 losers (75%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W10.  `H20=H20e AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W11.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W12.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W13.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W15.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W18.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W19.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W20.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W21.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W22.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W23.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W24.  `H20=H20a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T4=T4c drops 8/8 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T4=T4c drops 8/8 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=265  W=91/L=174  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_mid (92/174 of losers there)
- **Sharp: n=124  W=32/L=92  WR=25.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L02.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=265  W=91/L=174  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_mid (92/174 of losers there)
- **Sharp: n=124  W=32/L=92  WR=25.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L03.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=265  W=91/L=174  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_mid (92/174 of losers there)
- **Sharp: n=124  W=32/L=92  WR=25.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=265  W=91/L=174  WR=34.3%
- Sharpen: sharpest is session_bucket=ny_mid (92/174 of losers there)
- **Sharp: n=124  W=32/L=92  WR=25.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L05.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=262  W=104/L=158  WR=39.7%
- Sharpen: sharpest is H60=H60a (103/158 of losers there)
- **Sharp: n=135  W=32/L=103  WR=23.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L06.  `H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=238  W=92/L=146  WR=38.7%
- Sharpen: sharpest is RSI=RSI5 (92/146 of losers there)
- **Sharp: n=124  W=32/L=92  WR=25.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L07.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=236  W=94/L=142  WR=39.8%
- Sharpen: sharpest is T1=T1c (103/142 of losers there)
- **Sharp: n=135  W=32/L=103  WR=23.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L08.  `H60=H60a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=236  W=94/L=142  WR=39.8%
- Sharpen: sharpest is T1=T1c (103/142 of losers there)
- **Sharp: n=135  W=32/L=103  WR=23.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L09.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=236  W=94/L=142  WR=39.8%
- Sharpen: sharpest is T1=T1c (103/142 of losers there)
- **Sharp: n=135  W=32/L=103  WR=23.7%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=236  W=94/L=142  WR=39.8%
- Sharpen: sharpest is T1=T1c (103/142 of losers there)
- **Sharp: n=135  W=32/L=103  WR=23.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L11.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=217  W=78/L=139  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/139 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L12.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=217  W=78/L=139  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/139 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L13.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=217  W=78/L=139  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/139 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L14.  `H20=H20a AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=217  W=78/L=139  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/139 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L15.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=217  W=78/L=139  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/139 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L16.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=217  W=78/L=139  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_mid (57/139 of losers there)
- **Sharp: n=76  W=19/L=57  WR=25.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_mid

### L17.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=217  W=79/L=138  WR=36.4%
- Sharpen: sharpest is RSI=RSI4 (96/138 of losers there)
- **Sharp: n=128  W=32/L=96  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=217  W=79/L=138  WR=36.4%
- Sharpen: sharpest is RSI=RSI4 (96/138 of losers there)
- **Sharp: n=128  W=32/L=96  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L19.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=217  W=79/L=138  WR=36.4%
- Sharpen: sharpest is RSI=RSI4 (96/138 of losers there)
- **Sharp: n=128  W=32/L=96  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L20.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=213  W=80/L=133  WR=37.6%
- Sharpen: sharpest is ZS=ZS5 (61/133 of losers there)
- **Sharp: n=74  W=13/L=61  WR=17.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=213  W=80/L=133  WR=37.6%
- Sharpen: sharpest is ZS=ZS5 (61/133 of losers there)
- **Sharp: n=74  W=13/L=61  WR=17.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=213  W=80/L=133  WR=37.6%
- Sharpen: sharpest is ZS=ZS5 (61/133 of losers there)
- **Sharp: n=74  W=13/L=61  WR=17.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=207  W=78/L=129  WR=37.7%
- Sharpen: sharpest is T1=T1c (95/129 of losers there)
- **Sharp: n=123  W=28/L=95  WR=22.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L24.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=199  W=67/L=132  WR=33.7%
- Sharpen: sharpest is ZS=ZS2 (103/132 of losers there)
- **Sharp: n=142  W=39/L=103  WR=27.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  ONLY when zscore -2 to -1 oversold

### L25.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=199  W=67/L=132  WR=33.7%
- Sharpen: sharpest is ZS=ZS2 (103/132 of losers there)
- **Sharp: n=142  W=39/L=103  WR=27.5%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when zscore -2 to -1 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(55/44) | T1c(45/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
