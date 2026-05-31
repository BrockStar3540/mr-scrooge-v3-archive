# NZD_USD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,411**  (W=896 / L=515)  -  WR: **63.5%**

## Session distribution

- ny_mid: n=624  W=394/L=230  WR=63.1%
- ny_close: n=275  W=174/L=101  WR=63.3%
- asia: n=168  W=101/L=67  WR=60.1%
- london_open: n=150  W=104/L=46  WR=69.3%
- ny_open: n=84  W=57/L=27  WR=67.9%
- london: n=69  W=39/L=30  WR=56.5%
- off_hours: n=41  W=27/L=14  WR=65.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=165  W=141/L=24  WR=85.5%
- Refine: exclude direction_exec=short drops 24/24 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when short

### W02.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude H20=H20a drops 12/22 losers (55%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=150  W=134/L=16  WR=89.3%
- Refine: exclude RSI=RSI4 drops 16/16 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W04.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=143  W=127/L=16  WR=88.8%
- Refine: exclude RSI=RSI4 drops 16/16 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W05.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=126  W=116/L=10  WR=92.1%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W06.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=119  W=109/L=10  WR=91.6%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=75  W=75/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W07.  `T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W08.  `T1=T1a AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=97  W=89/L=8  WR=91.8%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W09.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude RSI=RSI3 drops 12/12 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W10.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude RSI=RSI3 drops 12/12 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W11.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W12.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W14.  `T1=T1a AND T4=T4a AND BBP=BBP3`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band  •  AVOID when session=ny_close

### W15.  `T1=T1a AND T4=T4a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W16.  `H20=H20e AND T1=T1a AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W17.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude session_bucket=ny_close drops 7/7 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W19.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude session_bucket=ny_close drops 7/7 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W20.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude session_bucket=ny_close drops 7/7 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W21.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude session_bucket=ny_close drops 7/7 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W22.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude session_bucket=ny_open drops 3/7 losers (43%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_open

### W23.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude T1=T1c drops 3/6 losers (50%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend AGAINST trade

### W24.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W25.  `T1=T1a AND T4=T4a AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=68  W=65/L=3  WR=95.6%
- Refine: exclude H60=H60e drops 3/3 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=180  W=65/L=115  WR=36.1%
- Sharpen: sharpest is ZS=ZS3 (39/115 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L02.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=135  W=45/L=90  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (23/90 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L03.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=120  W=42/L=78  WR=35.0%
- Sharpen: sharpest is ZS=ZS3 (25/78 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L04.  `H20=H20a AND T1=T1c AND ZS=ZS3`
- Raw: n=115  W=44/L=71  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (39/71 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L05.  `T1=T1c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=115  W=45/L=70  WR=39.1%
- Sharpen: sharpest is ZS=ZS3 (19/70 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L06.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=112  W=36/L=76  WR=32.1%
- Sharpen: sharpest is direction_exec=short (30/76 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when short

### L07.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=104  W=30/L=74  WR=28.8%
- Sharpen: sharpest is ZS=ZS3 (25/74 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L08.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=101  W=30/L=71  WR=29.7%
- Sharpen: sharpest is ZS=ZS3 (25/71 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L09.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is BBP=BBP0 (15/57 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L10.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=88  W=32/L=56  WR=36.4%
- Sharpen: sharpest is ZS=ZS3 (17/56 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L11.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is BBP=BBP0 (15/54 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L12.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=85  W=23/L=62  WR=27.1%
- Sharpen: sharpest is ZS=ZS3 (23/62 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L13.  `H20=H20a AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=82  W=23/L=59  WR=28.0%
- Sharpen: sharpest is ZS=ZS3 (23/59 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L14.  `H60=H60a AND T1=T1c AND ZS=ZS3`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_mid (24/50 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L15.  `H60=H60a AND T1=T1c AND ZS=ZS3 AND direction_exec=long`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_mid (24/48 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L16.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=72  W=23/L=49  WR=31.9%
- Sharpen: sharpest is BBP=BBP0 (15/49 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when deep below lower band

### L17.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (17/42 of losers there)
- **Sharp: n=23  W=6/L=17  WR=26.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L18.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is ZS=ZS3 (19/42 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L19.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=65  W=21/L=44  WR=32.3%
- Sharpen: sharpest is BBP=BBP0 (15/44 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when deep below lower band

### L20.  `T4=T4c AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is T1=T1c (34/39 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L21.  `H60=H60e AND T1=T1c AND ZS=ZS3`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (25/39 of losers there)
- **Sharp: n=26  W=1/L=25  WR=3.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L22.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is ZS=ZS3 (19/39 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L23.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is BBP=BBP4 (10/38 of losers there)
- **Sharp: n=11  W=1/L=10  WR=9.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when upper third

### L24.  `H20=H20a AND H60=H60e AND T1=T1c AND ZS=ZS3`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_mid (23/37 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L25.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is ZS=ZS3 (19/36 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(54/48) | H60a(45/51) |
| T1 | T1a(61/39) | T1c(39/61) |
| T4 | T4c(53/48) | T4a(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
