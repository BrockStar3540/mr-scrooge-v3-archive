# GBP_NZD — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,995**  (W=1,138 / L=857)  -  WR: **57.0%**

## Session distribution

- asia: n=700  W=393/L=307  WR=56.1%
- ny_mid: n=382  W=211/L=171  WR=55.2%
- ny_close: n=298  W=178/L=120  WR=59.7%
- london_open: n=259  W=151/L=108  WR=58.3%
- ny_open: n=248  W=143/L=105  WR=57.7%
- off_hours: n=46  W=24/L=22  WR=52.2%
- asia_late: n=34  W=21/L=13  WR=61.8%
- london: n=28  W=17/L=11  WR=60.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude session_bucket=asia_late drops 5/11 losers (45%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W02.  `T4=T4a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude session_bucket=asia_late drops 5/11 losers (45%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W03.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=asia_late drops 5/11 losers (45%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=asia_late

### W04.  `T4=T4a AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=asia_late drops 5/11 losers (45%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when session=asia_late

### W05.  `H20=H20a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W06.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W07.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W08.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20a AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W13.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude ZS=ZS3 drops 4/11 losers (36%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20e AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20a AND ZS=ZS3 AND session_bucket=ny_open`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -1 to +1 neutral; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3 AND session_bucket=ny_open`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude T4=T4c drops 7/8 losers (88%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W20.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI5 drops 4/4 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI5 drops 4/4 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W22.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI5 drops 4/4 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when RSI 60-70 strong

### W23.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W24.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/7 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W25.  `T4=T4a AND BBP=BBP2 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude H60=H60c drops 6/8 losers (75%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=136  W=43/L=93  WR=31.6%
- Sharpen: sharpest is RSI=RSI4 (53/93 of losers there)
- **Sharp: n=60  W=7/L=53  WR=11.7%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L02.  `H60=H60e AND T1=T1a AND ZS=ZS5`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is RSI=RSI4 (51/91 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L03.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is RSI=RSI4 (51/91 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L04.  `H60=H60e AND T1=T1a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is RSI=RSI4 (51/91 of losers there)
- **Sharp: n=58  W=7/L=51  WR=12.1%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L05.  `T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is RSI=RSI4 (53/71 of losers there)
- **Sharp: n=72  W=19/L=53  WR=26.4%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L06.  `H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is H20=H20a (41/69 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L07.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is H20=H20a (41/69 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L08.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is H20=H20a (41/69 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L09.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is H20=H20a (41/69 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L10.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is H20=H20a (41/69 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L11.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is H20=H20a (41/69 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L12.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is T4=T4c (43/61 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `T4=T4c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is H60=H60a (43/62 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L14.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is T4=T4c (43/55 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=91  W=36/L=55  WR=39.6%
- Sharpen: sharpest is T4=T4c (43/55 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L16.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is RSI=RSI4 (31/53 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L17.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=83  W=15/L=68  WR=18.1%
- Sharpen: sharpest is T4=T4a (41/68 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L18.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=83  W=15/L=68  WR=18.1%
- Sharpen: sharpest is T4=T4a (41/68 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L19.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=83  W=15/L=68  WR=18.1%
- Sharpen: sharpest is T4=T4a (41/68 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: LONG**  •  upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L20.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=83  W=15/L=68  WR=18.1%
- Sharpen: sharpest is T4=T4a (41/68 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L21.  `H60=H60e AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=83  W=15/L=68  WR=18.1%
- Sharpen: sharpest is T4=T4a (41/68 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L22.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=83  W=15/L=68  WR=18.1%
- Sharpen: sharpest is T4=T4a (41/68 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L23.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=83  W=29/L=54  WR=34.9%
- Sharpen: sharpest is T4=T4c (40/54 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L24.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=83  W=29/L=54  WR=34.9%
- Sharpen: sharpest is T4=T4c (40/54 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L25.  `T4=T4c AND RSI=RSI4 AND ZS=ZS2`
- Raw: n=80  W=26/L=54  WR=32.5%
- Sharpen: sharpest is H60=H60a (40/54 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(51/44) | H60e(45/52) |
| T1 | T1c(53/47) | T1a(47/53) |
| T4 | T4a(55/47) | T4c(45/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
