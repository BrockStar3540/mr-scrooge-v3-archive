# EUR_AUD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,911**  (W=1,121 / L=790)  -  WR: **58.7%**

## Session distribution

- asia: n=829  W=500/L=329  WR=60.3%
- ny_close: n=488  W=275/L=213  WR=56.4%
- off_hours: n=178  W=94/L=84  WR=52.8%
- ny_open: n=170  W=106/L=64  WR=62.4%
- london: n=143  W=84/L=59  WR=58.7%
- asia_late: n=49  W=30/L=19  WR=61.2%
- london_open: n=35  W=20/L=15  WR=57.1%
- ny_mid: n=19  W=12/L=7  WR=63.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude RSI=RSI6 drops 4/8 losers (50%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 70-80 overbought

### W02.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude BBP=BBP5 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W03.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude BBP=BBP5 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W04.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude BBP=BBP5 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W05.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude BBP=BBP5 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W06.  `H60=H60e AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude BBP=BBP5 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W07.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude BBP=BBP5 drops 7/11 losers (64%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when just touched upper band

### W08.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude H20=H20a drops 3/4 losers (75%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS1 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W11.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS1 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W12.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude ZS=ZS1 drops 4/8 losers (50%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W13.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W14.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W15.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W16.  `H60=H60a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W17.  `T1=T1c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=off_hours drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W18.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude ZS=ZS6 drops 5/6 losers (83%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when zscore >+3 extreme

### W19.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=59  W=54/L=5  WR=91.5%
- Refine: exclude RSI=RSI6 drops 4/5 losers (80%)
- **Final: n=55  W=54/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 70-80 overbought

### W20.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude session_bucket=off_hours drops 5/7 losers (71%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W21.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude session_bucket=off_hours drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W22.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude session_bucket=off_hours drops 5/7 losers (71%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W23.  `H20=H20e AND T4=T4a AND BBP=BBP3`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=35  W=33/L=2  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; middle of band  •  AVOID when session=ny_close

### W24.  `H20=H20e AND T4=T4a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=35  W=33/L=2  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when session=ny_close

### W25.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude session_bucket=off_hours drops 5/8 losers (62%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=off_hours

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=56/L=84  WR=40.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral

### L02.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=56/L=84  WR=40.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral

### L03.  `H60=H60a AND RSI=RSI5 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=56/L=84  WR=40.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral

### L04.  `H60=H60e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L05.  `T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L06.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L07.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L08.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L09.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L11.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L12.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (32/77 of losers there)
- **Sharp: n=35  W=3/L=32  WR=8.6%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20e AND T4=T4a AND ZS=ZS5`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is H60=H60a (17/69 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L14.  `H20=H20e AND H60=H60e AND RSI=RSI4`
- Raw: n=104  W=38/L=66  WR=36.5%
- Sharpen: sharpest is ZS=ZS3 (24/66 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L15.  `H20=H20e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=104  W=38/L=66  WR=36.5%
- Sharpen: sharpest is ZS=ZS3 (24/66 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=104  W=38/L=66  WR=36.5%
- Sharpen: sharpest is ZS=ZS3 (24/66 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L17.  `H20=H20e AND T1=T1a AND RSI=RSI4`
- Raw: n=103  W=37/L=66  WR=35.9%
- Sharpen: sharpest is ZS=ZS3 (24/66 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L18.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is ZS=ZS3 (24/66 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L19.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is ZS=ZS3 (24/66 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L20.  `H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is BBP=BBP4 (37/66 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L21.  `T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is BBP=BBP4 (37/66 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L22.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is BBP=BBP4 (37/66 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L23.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is BBP=BBP4 (37/66 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L24.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is BBP=BBP4 (37/66 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

### L25.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=100  W=34/L=66  WR=34.0%
- Sharpen: sharpest is BBP=BBP4 (37/66 of losers there)
- **Sharp: n=40  W=3/L=37  WR=7.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(44/50) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
