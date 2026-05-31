# EUR_AUD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,627**  (W=2,585 / L=2,042)  -  WR: **55.9%**

## Session distribution

- asia: n=1183  W=692/L=491  WR=58.5%
- ny_open: n=781  W=431/L=350  WR=55.2%
- ny_mid: n=770  W=371/L=399  WR=48.2%
- london_open: n=706  W=414/L=292  WR=58.6%
- ny_close: n=560  W=316/L=244  WR=56.4%
- london: n=539  W=308/L=231  WR=57.1%
- off_hours: n=71  W=42/L=29  WR=59.2%
- asia_late: n=17  W=11/L=6  WR=64.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude H60=H60a drops 10/11 losers (91%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF60 aligned WITH trade

### W02.  `H60=H60a AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W03.  `BBP=BBP3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: SHORT**  •  middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W04.  `H60=H60a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; zscore -1 to +1 neutral; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60a AND BBP=BBP3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W06.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude RSI=RSI3 drops 5/7 losers (71%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: SHORT**  •  middle of band; zscore -1 to +1 neutral; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W07.  `H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP0 drops 8/10 losers (80%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W08.  `T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP0 drops 8/10 losers (80%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W09.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP0 drops 8/10 losers (80%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W10.  `H20=H20e AND T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP0 drops 8/10 losers (80%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W11.  `H60=H60e AND T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP0 drops 8/10 losers (80%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W12.  `T1=T1c AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H60=H60e drops 4/10 losers (40%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; session=ny_close  •  AVOID when HTF60 strongly against

### W13.  `T1=T1c AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H60=H60e drops 4/10 losers (40%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; zscore -1 to +1 neutral; session=ny_close  •  AVOID when HTF60 strongly against

### W14.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=69  W=65/L=4  WR=94.2%
- Refine: exclude H60=H60a drops 3/4 losers (75%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF60 aligned WITH trade

### W15.  `H20=H20a AND H60=H60a AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude strategy_id=TF2_pullback_EMA20_short drops 2/7 losers (29%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; middle of band; session=ny_close  •  AVOID when strategy=TF2_pullback_EMA20_short

### W16.  `H20=H20a AND BBP=BBP3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude strategy_id=TF2_pullback_EMA20_short drops 2/7 losers (29%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; middle of band; session=ny_close  •  AVOID when strategy=TF2_pullback_EMA20_short

### W17.  `H60=H60a AND T1=T1c AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1c AND BBP=BBP3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=40  W=39/L=1  WR=97.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60a AND T4=T4a AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W20.  `T4=T4a AND BBP=BBP3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: SHORT**  •  4h trend WITH trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W21.  `H20=H20a AND H60=H60e AND session_bucket=ny_open`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude RSI=RSI4 drops 5/8 losers (62%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W22.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude RSI=RSI4 drops 5/8 losers (62%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude RSI=RSI4 drops 5/8 losers (62%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20a AND T1=T1c AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude RSI=RSI3 drops 5/6 losers (83%)
- **Final: n=32  W=31/L=1  WR=96.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; middle of band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W25.  `H20=H20b AND H60=H60e AND T4=T4a`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude BBP=BBP6 drops 4/9 losers (44%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade  •  AVOID when deep above upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=356  W=142/L=214  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (68/214 of losers there)
- **Sharp: n=76  W=8/L=68  WR=10.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=325  W=125/L=200  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (64/200 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=325  W=125/L=200  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (64/200 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=325  W=125/L=200  WR=38.5%
- Sharpen: sharpest is ZS=ZS5 (64/200 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=319  W=123/L=196  WR=38.6%
- Sharpen: sharpest is ZS=ZS5 (64/196 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=319  W=123/L=196  WR=38.6%
- Sharpen: sharpest is ZS=ZS5 (64/196 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=259  W=101/L=158  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_mid (68/158 of losers there)
- **Sharp: n=76  W=8/L=68  WR=10.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L08.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=237  W=93/L=144  WR=39.2%
- Sharpen: sharpest is ZS=ZS5 (68/144 of losers there)
- **Sharp: n=76  W=8/L=68  WR=10.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=227  W=89/L=138  WR=39.2%
- Sharpen: sharpest is ZS=ZS5 (68/138 of losers there)
- **Sharp: n=76  W=8/L=68  WR=10.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=226  W=90/L=136  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (64/136 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L11.  `T1=T1c AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=226  W=90/L=136  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (64/136 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L12.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=216  W=81/L=135  WR=37.5%
- Sharpen: sharpest is ZS=ZS5 (68/135 of losers there)
- **Sharp: n=76  W=8/L=68  WR=10.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (55/117 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L14.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (55/117 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L15.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (55/117 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L16.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (55/117 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L17.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (55/117 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep above upper band

### L18.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (55/117 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L19.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=179  W=62/L=117  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (55/117 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep above upper band

### L20.  `T1=T1a AND T4=T4c AND BBP=BBP3`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_close (33/101 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band  •  ONLY when session=ny_close

### L21.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_close (33/101 of losers there)
- **Sharp: n=42  W=9/L=33  WR=21.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when session=ny_close

### L22.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is BBP=BBP4 (28/102 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when upper third

### L23.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is BBP=BBP4 (28/102 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_open  •  ONLY when upper third

### L24.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=159  W=57/L=102  WR=35.8%
- Sharpen: sharpest is BBP=BBP4 (28/102 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when upper third

### L25.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=159  W=63/L=96  WR=39.6%
- Sharpen: sharpest is H60=H60a (85/96 of losers there)
- **Sharp: n=131  W=46/L=85  WR=35.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | ny_mid(14/20) |

*Read: `bucket(winner%/loser%)`.*
