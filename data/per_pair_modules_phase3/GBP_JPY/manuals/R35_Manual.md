# GBP_JPY — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,886**  (W=1,123 / L=763)  -  WR: **59.5%**

## Session distribution

- london_open: n=558  W=343/L=215  WR=61.5%
- ny_mid: n=525  W=305/L=220  WR=58.1%
- asia: n=298  W=179/L=119  WR=60.1%
- ny_open: n=164  W=98/L=66  WR=59.8%
- london: n=137  W=76/L=61  WR=55.5%
- ny_close: n=103  W=51/L=52  WR=49.5%
- off_hours: n=74  W=54/L=20  WR=73.0%
- asia_late: n=27  W=17/L=10  WR=63.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=125  W=110/L=15  WR=88.0%
- Refine: exclude session_bucket=ny_open drops 6/15 losers (40%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W02.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=125  W=110/L=15  WR=88.0%
- Refine: exclude session_bucket=ny_open drops 6/15 losers (40%)
- **Final: n=101  W=92/L=9  WR=91.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W03.  `H20=H20a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude H60=H60e drops 7/13 losers (54%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=ny_mid  •  AVOID when HTF60 strongly against

### W04.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=ny_open drops 6/15 losers (40%)
- **Final: n=89  W=80/L=9  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W05.  `T4=T4a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude H20=H20a drops 15/15 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W06.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude H20=H20e drops 3/14 losers (21%)
- **Final: n=108  W=97/L=11  WR=89.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

### W07.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude session_bucket=london_open drops 4/15 losers (27%)
- **Final: n=95  W=84/L=11  WR=88.4%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W08.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/10 losers (30%)
- **Final: n=94  W=87/L=7  WR=92.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W09.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude ZS=ZS3 drops 6/13 losers (46%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when zscore -1 to +1 neutral

### W10.  `T4=T4a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/10 losers (30%)
- **Final: n=78  W=71/L=7  WR=91.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W11.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/10 losers (30%)
- **Final: n=78  W=71/L=7  WR=91.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W12.  `H20=H20a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/9 losers (33%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W13.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/9 losers (33%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W14.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=90  W=81/L=9  WR=90.0%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/9 losers (33%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W15.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W16.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W18.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 6/12 losers (50%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W19.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/10 losers (30%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W20.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=85  W=76/L=9  WR=89.4%
- Refine: exclude strategy_id=BR2_vcb_short drops 3/9 losers (33%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when strategy=BR2_vcb_short

### W21.  `H20=H20a AND H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude T4=T4c drops 8/12 losers (67%)
- **Final: n=46  W=42/L=4  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; lower third  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude T4=T4c drops 8/12 losers (67%)
- **Final: n=46  W=42/L=4  WR=91.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when 4h trend AGAINST trade

### W23.  `T4=T4a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 3/9 losers (33%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W24.  `T4=T4a AND BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude session_bucket=ny_close drops 3/9 losers (33%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W25.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude H20=H20e drops 3/10 losers (30%)
- **Final: n=77  W=70/L=7  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=ny_mid  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=196  W=72/L=124  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_mid (57/124 of losers there)
- **Sharp: n=68  W=11/L=57  WR=16.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L02.  `H20=H20e AND T4=T4c AND ZS=ZS2`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (50/105 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L03.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=167  W=62/L=105  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_mid (50/105 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L04.  `H20=H20e AND H60=H60e AND BBP=BBP2`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (43/100 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when session=ny_mid

### L05.  `H20=H20e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (43/100 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third  •  ONLY when session=ny_mid

### L06.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (43/100 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L07.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (43/100 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when session=ny_mid

### L08.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_mid (43/100 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L09.  `H20=H20e AND T1=T1c AND BBP=BBP2`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is RSI=RSI4 (43/80 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=108  W=36/L=72  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (50/72 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (33/62 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=ny_mid

### L12.  `H20=H20e AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (33/62 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L13.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (33/62 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=ny_mid

### L14.  `H20=H20e AND T1=T1c AND ZS=ZS2`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (31/60 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

### L15.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (31/60 of losers there)
- **Sharp: n=40  W=9/L=31  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is session_bucket=ny_mid (32/60 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L17.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS2`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (32/58 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L18.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (32/58 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L19.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_mid (32/58 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=95  W=33/L=62  WR=34.7%
- Sharpen: sharpest is H60=H60a (24/62 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF60 aligned WITH trade

### L21.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is BBP=BBP2 (24/56 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L22.  `T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is BBP=BBP2 (24/56 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L23.  `H60=H60a AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is BBP=BBP2 (24/56 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L24.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_mid (31/56 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L25.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=78  W=30/L=48  WR=38.5%
- Sharpen: sharpest is BBP=BBP2 (24/48 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/40) | H20e(40/51) |
| H60 | — | — |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | T4a(53/48) | T4c(47/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
