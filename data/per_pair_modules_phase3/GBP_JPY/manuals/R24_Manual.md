# GBP_JPY — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,127**  (W=2,281 / L=1,846)  -  WR: **55.3%**

## Session distribution

- asia: n=1182  W=635/L=547  WR=53.7%
- ny_mid: n=991  W=521/L=470  WR=52.6%
- ny_close: n=646  W=397/L=249  WR=61.5%
- london_open: n=443  W=243/L=200  WR=54.9%
- london: n=409  W=244/L=165  WR=59.7%
- ny_open: n=303  W=161/L=142  WR=53.1%
- off_hours: n=104  W=51/L=53  WR=49.0%
- asia_late: n=49  W=29/L=20  WR=59.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND H60=H60e AND BBP=BBP2`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude RSI=RSI4 drops 14/14 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; lower third  •  AVOID when RSI 50-60 upper neutral

### W02.  `H20=H20d AND BBP=BBP2 AND direction_exec=short`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude RSI=RSI4 drops 14/14 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; lower third  •  AVOID when RSI 50-60 upper neutral

### W03.  `H20=H20d AND H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude RSI=RSI4 drops 14/14 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; lower third  •  AVOID when RSI 50-60 upper neutral

### W04.  `H60=H60e AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W05.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60e AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude H20=H20a drops 8/11 losers (73%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W08.  `H20=H20a AND T1=T1a AND ZS=ZS1`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude H60=H60e drops 11/12 losers (92%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W09.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20a drops 12/12 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W11.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude H20=H20a drops 7/10 losers (70%)
- **Final: n=53  W=50/L=3  WR=94.3%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W12.  `H20=H20d AND T1=T1a AND BBP=BBP2`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; lower third  •  AVOID when RSI 50-60 upper neutral

### W13.  `H20=H20d AND H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade; lower third  •  AVOID when RSI 50-60 upper neutral

### W14.  `H20=H20d AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend WITH trade; lower third  •  AVOID when RSI 50-60 upper neutral

### W15.  `H20=H20d AND T1=T1a AND ZS=ZS2`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W16.  `H20=H20d AND H60=H60e AND T1=T1a AND ZS=ZS2`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W17.  `H20=H20d AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W18.  `H20=H20d AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude RSI=RSI4 drops 8/8 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W19.  `T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude ZS=ZS5 drops 5/8 losers (62%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +2 to +3 deep overbought

### W20.  `H20=H20d AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=68  W=68/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; lower third; RSI 40-50 lower neutral

### W21.  `H20=H20d AND H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=68  W=68/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; lower third; RSI 40-50 lower neutral

### W22.  `H20=H20d AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=68  W=68/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 mildly against; lower third; RSI 40-50 lower neutral

### W23.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W24.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude H20=H20a drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W25.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude ZS=ZS5 drops 5/8 losers (62%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +2 to +3 deep overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=356  W=140/L=216  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (160/216 of losers there)
- **Sharp: n=242  W=82/L=160  WR=33.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L02.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=356  W=140/L=216  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (160/216 of losers there)
- **Sharp: n=242  W=82/L=160  WR=33.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L03.  `H20=H20e AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=356  W=140/L=216  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (160/216 of losers there)
- **Sharp: n=242  W=82/L=160  WR=33.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L04.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=271  W=107/L=164  WR=39.5%
- Sharpen: sharpest is H20=H20b (39/164 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=271  W=107/L=164  WR=39.5%
- Sharpen: sharpest is H20=H20b (39/164 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L06.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=250  W=100/L=150  WR=40.0%
- Sharpen: sharpest is H20=H20d (43/150 of losers there)
- **Sharp: n=49  W=6/L=43  WR=12.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 mildly against

### L07.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=242  W=82/L=160  WR=33.9%
- Sharpen: sharpest is session_bucket=asia (40/160 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L08.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=242  W=82/L=160  WR=33.9%
- Sharpen: sharpest is session_bucket=asia (40/160 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L09.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=205  W=82/L=123  WR=40.0%
- Sharpen: sharpest is T1=T1a (54/123 of losers there)
- **Sharp: n=70  W=16/L=54  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L10.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=205  W=82/L=123  WR=40.0%
- Sharpen: sharpest is T1=T1a (54/123 of losers there)
- **Sharp: n=70  W=16/L=54  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L11.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=199  W=73/L=126  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/126 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_mid

### L12.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=199  W=73/L=126  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/126 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when session=ny_mid

### L13.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=199  W=73/L=126  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_mid (32/126 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=ny_mid

### L14.  `H60=H60a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=196  W=78/L=118  WR=39.8%
- Sharpen: sharpest is T4=T4a (67/118 of losers there)
- **Sharp: n=88  W=21/L=67  WR=23.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=asia  •  ONLY when 4h trend WITH trade

### L15.  `BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=196  W=78/L=118  WR=39.8%
- Sharpen: sharpest is T4=T4a (67/118 of losers there)
- **Sharp: n=88  W=21/L=67  WR=23.9%**
- **Dir: LONG**  •  lower third; session=asia  •  ONLY when 4h trend WITH trade

### L16.  `H60=H60a AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=196  W=78/L=118  WR=39.8%
- Sharpen: sharpest is T4=T4a (67/118 of losers there)
- **Sharp: n=88  W=21/L=67  WR=23.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; session=asia  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=193  W=68/L=125  WR=35.2%
- Sharpen: sharpest is H20=H20b (54/125 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L18.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=193  W=68/L=125  WR=35.2%
- Sharpen: sharpest is H20=H20b (54/125 of losers there)
- **Sharp: n=57  W=3/L=54  WR=5.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF20 slightly aligned

### L19.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=186  W=71/L=115  WR=38.2%
- Sharpen: sharpest is session_bucket=london_open (34/115 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L20.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=186  W=71/L=115  WR=38.2%
- Sharpen: sharpest is session_bucket=london_open (34/115 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L21.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=186  W=71/L=115  WR=38.2%
- Sharpen: sharpest is session_bucket=london_open (34/115 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L22.  `H20=H20b AND H60=H60a AND RSI=RSI3`
- Raw: n=173  W=60/L=113  WR=34.7%
- Sharpen: sharpest is BBP=BBP2 (60/113 of losers there)
- **Sharp: n=63  W=3/L=60  WR=4.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L23.  `H20=H20b AND RSI=RSI3 AND direction_exec=long`
- Raw: n=173  W=60/L=113  WR=34.7%
- Sharpen: sharpest is BBP=BBP2 (60/113 of losers there)
- **Sharp: n=63  W=3/L=60  WR=4.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 40-50 lower neutral  •  ONLY when lower third

### L24.  `H20=H20b AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=173  W=60/L=113  WR=34.7%
- Sharpen: sharpest is BBP=BBP2 (60/113 of losers there)
- **Sharp: n=63  W=3/L=60  WR=4.8%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L25.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: sharpest is H20=H20b (52/109 of losers there)
- **Sharp: n=55  W=3/L=52  WR=5.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(42/33) | H20e(32/41) |
| H60 | — | — |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
