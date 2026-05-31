# AUD_JPY — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,723**  (W=2,990 / L=1,733)  -  WR: **63.3%**

## Session distribution

- asia: n=1869  W=1173/L=696  WR=62.8%
- ny_close: n=775  W=497/L=278  WR=64.1%
- ny_open: n=584  W=376/L=208  WR=64.4%
- ny_mid: n=505  W=343/L=162  WR=67.9%
- london: n=427  W=265/L=162  WR=62.1%
- london_open: n=353  W=216/L=137  WR=61.2%
- asia_late: n=135  W=73/L=62  WR=54.1%
- off_hours: n=75  W=47/L=28  WR=62.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=170  W=147/L=23  WR=86.5%
- Refine: exclude RSI=RSI5 drops 14/23 losers (61%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when RSI 60-70 strong

### W02.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=160  W=138/L=22  WR=86.2%
- Refine: exclude T4=T4c drops 19/22 losers (86%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W03.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=160  W=138/L=22  WR=86.2%
- Refine: exclude T4=T4c drops 19/22 losers (86%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W04.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=160  W=138/L=22  WR=86.2%
- Refine: exclude T4=T4c drops 19/22 losers (86%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W05.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=160  W=138/L=22  WR=86.2%
- Refine: exclude T4=T4c drops 19/22 losers (86%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W06.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=160  W=138/L=22  WR=86.2%
- Refine: exclude T4=T4c drops 19/22 losers (86%)
- **Final: n=84  W=81/L=3  WR=96.4%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W07.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude H20=H20e drops 13/20 losers (65%)
- **Final: n=110  W=103/L=7  WR=93.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 strongly against

### W08.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude T4=T4c drops 14/17 losers (82%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W09.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude T4=T4c drops 14/17 losers (82%)
- **Final: n=82  W=79/L=3  WR=96.3%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W10.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude H20=H20e drops 13/18 losers (72%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W11.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude H20=H20e drops 13/18 losers (72%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W12.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude T4=T4a drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W13.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude T4=T4a drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: LONG**  •  upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W14.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude T4=T4a drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W15.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude H20=H20e drops 9/14 losers (64%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 strongly against

### W16.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude BBP=BBP5 drops 8/14 losers (57%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when just touched upper band

### W17.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude H20=H20e drops 9/14 losers (64%)
- **Final: n=94  W=89/L=5  WR=94.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W18.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=110  W=103/L=7  WR=93.6%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/7 losers (29%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when strategy=charlie_pullback_continuation_v2

### W19.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=110  W=103/L=7  WR=93.6%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 2/7 losers (29%)
- **Final: n=104  W=99/L=5  WR=95.2%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when strategy=charlie_pullback_continuation_v2

### W20.  `H60=H60a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=109  W=102/L=7  WR=93.6%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W21.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=109  W=102/L=7  WR=93.6%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W22.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=109  W=102/L=7  WR=93.6%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W23.  `H60=H60a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=109  W=102/L=7  WR=93.6%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W24.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=109  W=102/L=7  WR=93.6%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=45  W=45/L=0  WR=100.0%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20e AND T4=T4c AND session_bucket=london`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude T1=T1c drops 8/13 losers (62%)
- **Final: n=70  W=65/L=5  WR=92.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (63/96 of losers there)
- **Sharp: n=89  W=26/L=63  WR=29.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (63/96 of losers there)
- **Sharp: n=89  W=26/L=63  WR=29.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L03.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (63/96 of losers there)
- **Sharp: n=89  W=26/L=63  WR=29.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 40-50 lower neutral

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L05.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong

### L06.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong

### L07.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L08.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong

### L09.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong

### L10.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L11.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L12.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong

### L13.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=147  W=57/L=90  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=57/L=90  WR=38.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L14.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=146  W=58/L=88  WR=39.7%
- Sharpen: sharpest is H20=H20a (20/88 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L15.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=146  W=58/L=88  WR=39.7%
- Sharpen: sharpest is H20=H20a (20/88 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND T4=T4a AND session_bucket=london`
- Raw: n=142  W=39/L=103  WR=27.5%
- Sharpen: sharpest is BBP=BBP5 (27/103 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london  •  ONLY when just touched upper band

### L17.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong

### L18.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L19.  `H20=H20e AND T4=T4a AND RSI=RSI5`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong

### L20.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong

### L21.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L22.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong

### L23.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong

### L24.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L25.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=49/L=88  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=49/L=88  WR=35.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(49/36) | H20e(37/51) |
| H60 | H60a(54/45) | H60e(46/55) |
| T1 | T1a(57/43) | T1c(43/57) |
| T4 | T4c(53/47) | T4a(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/45) | short(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
