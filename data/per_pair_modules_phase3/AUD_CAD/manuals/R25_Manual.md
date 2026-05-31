# AUD_CAD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,231**  (W=1,371 / L=860)  -  WR: **61.5%**

## Session distribution

- ny_mid: n=727  W=438/L=289  WR=60.2%
- ny_open: n=492  W=313/L=179  WR=63.6%
- asia: n=376  W=228/L=148  WR=60.6%
- ny_close: n=308  W=181/L=127  WR=58.8%
- london_open: n=220  W=144/L=76  WR=65.5%
- london: n=79  W=45/L=34  WR=57.0%
- asia_late: n=28  W=21/L=7  WR=75.0%
- off_hours: n=1  W=1/L=0  WR=100.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=159  W=137/L=22  WR=86.2%
- Refine: exclude RSI=RSI4 drops 19/22 losers (86%)
- **Final: n=113  W=110/L=3  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W02.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=159  W=137/L=22  WR=86.2%
- Refine: exclude RSI=RSI4 drops 19/22 losers (86%)
- **Final: n=113  W=110/L=3  WR=97.3%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W03.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=159  W=137/L=22  WR=86.2%
- Refine: exclude RSI=RSI4 drops 19/22 losers (86%)
- **Final: n=113  W=110/L=3  WR=97.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W04.  `H20=H20c AND T1=T1a AND T4=T4c`
- Raw: n=146  W=132/L=14  WR=90.4%
- Refine: exclude RSI=RSI3 drops 9/14 losers (64%)
- **Final: n=128  W=123/L=5  WR=96.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=140  W=126/L=14  WR=90.0%
- Refine: exclude RSI=RSI4 drops 11/14 losers (79%)
- **Final: n=113  W=110/L=3  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W06.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=140  W=126/L=14  WR=90.0%
- Refine: exclude RSI=RSI4 drops 11/14 losers (79%)
- **Final: n=113  W=110/L=3  WR=97.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W07.  `H20=H20c AND H60=H60e AND T1=T1a`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W08.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W09.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W10.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W11.  `H20=H20c AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W12.  `H20=H20c AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 40-50 lower neutral

### W13.  `H20=H20c AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W14.  `H20=H20c AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=113  W=101/L=12  WR=89.4%
- Refine: exclude RSI=RSI3 drops 9/12 losers (75%)
- **Final: n=95  W=92/L=3  WR=96.8%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W15.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=105  W=97/L=8  WR=92.4%
- Refine: exclude ZS=ZS4 drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W16.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude ZS=ZS4 drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W17.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude ZS=ZS4 drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W18.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude ZS=ZS4 drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W19.  `H20=H20c AND H60=H60e AND RSI=RSI2`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 30-40 weak  •  AVOID when just touched lower band

### W20.  `H20=H20c AND H60=H60e AND session_bucket=ny_open`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=ny_open  •  AVOID when just touched lower band

### W21.  `H20=H20c AND T1=T1a AND RSI=RSI2`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when just touched lower band

### W22.  `H20=H20c AND T1=T1a AND session_bucket=ny_open`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W23.  `H20=H20c AND T4=T4c AND RSI=RSI2`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when just touched lower band

### W24.  `H20=H20c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; session=ny_open  •  AVOID when just touched lower band

### W25.  `H20=H20c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=95  W=92/L=3  WR=96.8%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 30-40 weak  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND session_bucket=ny_open`
- Raw: n=146  W=48/L=98  WR=32.9%
- Sharpen: sharpest is H20=H20c (53/98 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_open  •  ONLY when HTF20 neutral

### L02.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=143  W=54/L=89  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_open (24/89 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third  •  ONLY when session=ny_open

### L03.  `H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=130  W=49/L=81  WR=37.7%
- Sharpen: sharpest is H20=H20c (53/81 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L04.  `T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=125  W=39/L=86  WR=31.2%
- Sharpen: sharpest is H20=H20c (53/86 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L05.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_open (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L06.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_open (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L07.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L08.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L09.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L10.  `T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L11.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L12.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L13.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L14.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=117  W=37/L=80  WR=31.6%
- Sharpen: sharpest is H20=H20c (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L15.  `H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is H20=H20c (53/70 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 neutral

### L16.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is H20=H20c (53/70 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 neutral

### L17.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is H20=H20c (53/70 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 neutral

### L18.  `H20=H20c AND T1=T1c AND T4=T4a`
- Raw: n=102  W=26/L=76  WR=25.5%
- Sharpen: sharpest is RSI=RSI2 (53/76 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 30-40 weak

### L19.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is T1=T1c (43/62 of losers there)
- **Sharp: n=55  W=12/L=43  WR=21.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L20.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is T1=T1c (43/62 of losers there)
- **Sharp: n=55  W=12/L=43  WR=21.8%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L21.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is T1=T1c (43/62 of losers there)
- **Sharp: n=55  W=12/L=43  WR=21.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L22.  `H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is ZS=ZS3 (14/65 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -1 to +1 neutral

### L23.  `T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is ZS=ZS3 (14/65 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -1 to +1 neutral

### L24.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is ZS=ZS3 (14/65 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -1 to +1 neutral

### L25.  `H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is H20=H20c (17/57 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when HTF20 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(9/15) |
| H60 | — | — |
| T1 | T1a(57/46) | T1c(43/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
