# CHF_JPY — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,419**  (W=1,381 / L=1,038)  -  WR: **57.1%**

## Session distribution

- asia: n=516  W=321/L=195  WR=62.2%
- ny_mid: n=507  W=289/L=218  WR=57.0%
- london_open: n=368  W=212/L=156  WR=57.6%
- london: n=357  W=202/L=155  WR=56.6%
- ny_open: n=341  W=175/L=166  WR=51.3%
- ny_close: n=200  W=129/L=71  WR=64.5%
- off_hours: n=71  W=31/L=40  WR=43.7%
- asia_late: n=59  W=22/L=37  WR=37.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND direction_exec=long`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude BBP=BBP4 drops 8/16 losers (50%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade  •  AVOID when upper third

### W02.  `H20=H20e AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude BBP=BBP4 drops 8/16 losers (50%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when upper third

### W03.  `H20=H20e AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude BBP=BBP4 drops 8/16 losers (50%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when upper third

### W04.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude BBP=BBP4 drops 8/16 losers (50%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when upper third

### W05.  `H20=H20e AND H60=H60a AND ZS=ZS4`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T1=T1c drops 9/15 losers (60%)
- **Final: n=55  W=49/L=6  WR=89.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W06.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude T1=T1c drops 9/15 losers (60%)
- **Final: n=55  W=49/L=6  WR=89.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W07.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4c drops 13/14 losers (93%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20e AND H60=H60a AND RSI=RSI5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W09.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W10.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W11.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when just touched upper band

### W12.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W13.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W14.  `H20=H20e AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W15.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W16.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W17.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 6/12 losers (50%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W18.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude H20=H20a drops 6/11 losers (55%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  upper third; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W19.  `T1=T1a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H20=H20a drops 6/9 losers (67%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=ny_open

### W21.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W22.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=ny_open

### W23.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W24.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when session=ny_open

### W25.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_open drops 4/11 losers (36%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=227  W=82/L=145  WR=36.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=227  W=82/L=145  WR=36.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third

### L02.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=213  W=72/L=141  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=213  W=72/L=141  WR=33.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold

### L03.  `H20=H20a AND H60=H60a AND BBP=BBP2`
- Raw: n=198  W=71/L=127  WR=35.9%
- Sharpen: sharpest is RSI=RSI2 (42/127 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L04.  `H20=H20a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=198  W=71/L=127  WR=35.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=198  W=71/L=127  WR=35.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold

### L05.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=198  W=71/L=127  WR=35.9%
- Sharpen: sharpest is RSI=RSI2 (42/127 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L06.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=198  W=71/L=127  WR=35.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=198  W=71/L=127  WR=35.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold

### L07.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=184  W=72/L=112  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (62/112 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=184  W=72/L=112  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (62/112 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when RSI 60-70 strong

### L09.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=184  W=72/L=112  WR=39.1%
- Sharpen: sharpest is RSI=RSI5 (62/112 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L10.  `H20=H20a AND H60=H60a AND ZS=ZS2`
- Raw: n=172  W=60/L=112  WR=34.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=172  W=60/L=112  WR=34.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold

### L11.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=172  W=60/L=112  WR=34.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=172  W=60/L=112  WR=34.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold

### L12.  `H20=H20a AND H60=H60a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=172  W=60/L=112  WR=34.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=172  W=60/L=112  WR=34.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold

### L13.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L15.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L17.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L18.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L19.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L22.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=163  W=44/L=119  WR=27.0%
- Sharpen: sharpest is H20=H20a (62/119 of losers there)
- **Sharp: n=75  W=13/L=62  WR=17.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L23.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=162  W=64/L=98  WR=39.5%
- Sharpen: sharpest is H60=H60e (51/98 of losers there)
- **Sharp: n=64  W=13/L=51  WR=20.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when HTF60 strongly against

### L24.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: sharpest is T1=T1a (50/91 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20a AND T1=T1c AND BBP=BBP2`
- Raw: n=144  W=51/L=93  WR=35.4%
- Sharpen: sharpest is RSI=RSI2 (42/93 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(53/47) | H20a(47/53) |
| H60 | H60a(53/45) | H60e(46/55) |
| T1 | T1a(54/44) | T1c(46/56) |
| T4 | T4c(56/44) | T4a(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/47) | short(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
