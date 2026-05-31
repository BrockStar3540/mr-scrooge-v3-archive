# EUR_AUD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,928**  (W=3,334 / L=2,594)  -  WR: **56.2%**

## Session distribution

- ny_mid: n=1787  W=955/L=832  WR=53.4%
- asia: n=1701  W=992/L=709  WR=58.3%
- ny_close: n=809  W=478/L=331  WR=59.1%
- ny_open: n=636  W=356/L=280  WR=56.0%
- london_open: n=515  W=290/L=225  WR=56.3%
- off_hours: n=173  W=98/L=75  WR=56.6%
- london: n=156  W=79/L=77  WR=50.6%
- asia_late: n=151  W=86/L=65  WR=57.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude T4=T4a drops 11/14 losers (79%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend WITH trade

### W02.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude T4=T4a drops 11/14 losers (79%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend WITH trade

### W03.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude T4=T4a drops 11/14 losers (79%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=ny_close  •  AVOID when 4h trend WITH trade

### W04.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude T4=T4a drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend WITH trade

### W05.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude T4=T4a drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend WITH trade

### W06.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude T4=T4a drops 7/8 losers (88%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when 4h trend WITH trade

### W07.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=ny_close`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H60=H60e drops 11/12 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W08.  `H20=H20a AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W09.  `H60=H60a AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W10.  `T1=T1c AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W11.  `ZS=ZS6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W12.  `H20=H20a AND H60=H60a AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W13.  `H20=H20a AND T1=T1c AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W14.  `H20=H20a AND BBP=BBP6 AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W15.  `H20=H20a AND ZS=ZS6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W16.  `H60=H60a AND T1=T1c AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W17.  `H60=H60a AND BBP=BBP6 AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W18.  `H60=H60a AND ZS=ZS6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W19.  `T1=T1c AND BBP=BBP6 AND ZS=ZS6 AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W20.  `T1=T1c AND ZS=ZS6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W21.  `BBP=BBP6 AND ZS=ZS6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude RSI=RSI5 drops 7/7 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore >+3 extreme; session=asia  •  AVOID when RSI 60-70 strong

### W22.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia_late  •  AVOID when just touched lower band

### W23.  `H60=H60a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia_late  •  AVOID when just touched lower band

### W24.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia_late  •  AVOID when just touched lower band

### W25.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=asia_late`
- Raw: n=41  W=38/L=3  WR=92.7%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia_late  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=319  W=91/L=228  WR=28.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=319  W=91/L=228  WR=28.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought

### L02.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=259  W=85/L=174  WR=32.8%
- Sharpen: sharpest is RSI=RSI5 (118/174 of losers there)
- **Sharp: n=157  W=39/L=118  WR=24.8%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=250  W=86/L=164  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=250  W=86/L=164  WR=34.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid

### L04.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=250  W=86/L=164  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=250  W=86/L=164  WR=34.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid

### L05.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=245  W=81/L=164  WR=33.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=81/L=164  WR=33.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid

### L06.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=220  W=73/L=147  WR=33.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=220  W=73/L=147  WR=33.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L07.  `H20=H20a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=215  W=86/L=129  WR=40.0%
- Sharpen: sharpest is T4=T4c (82/129 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L08.  `T1=T1c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=213  W=71/L=142  WR=33.3%
- Sharpen: sharpest is T4=T4c (110/142 of losers there)
- **Sharp: n=148  W=38/L=110  WR=25.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L09.  `ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=213  W=71/L=142  WR=33.3%
- Sharpen: sharpest is T4=T4c (108/142 of losers there)
- **Sharp: n=146  W=38/L=108  WR=26.0%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L10.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=211  W=71/L=140  WR=33.6%
- Sharpen: sharpest is T4=T4c (108/140 of losers there)
- **Sharp: n=146  W=38/L=108  WR=26.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L11.  `T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=210  W=60/L=150  WR=28.6%
- Sharpen: sharpest is BBP=BBP6 (57/150 of losers there)
- **Sharp: n=70  W=13/L=57  WR=18.6%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when deep above upper band

### L12.  `T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=199  W=77/L=122  WR=38.7%
- Sharpen: sharpest is RSI=RSI5 (80/122 of losers there)
- **Sharp: n=108  W=28/L=80  WR=25.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L13.  `T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=199  W=77/L=122  WR=38.7%
- Sharpen: sharpest is RSI=RSI5 (80/122 of losers there)
- **Sharp: n=108  W=28/L=80  WR=25.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L14.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=199  W=77/L=122  WR=38.7%
- Sharpen: sharpest is RSI=RSI5 (80/122 of losers there)
- **Sharp: n=108  W=28/L=80  WR=25.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=197  W=56/L=141  WR=28.4%
- Sharpen: sharpest is BBP=BBP6 (80/141 of losers there)
- **Sharp: n=101  W=21/L=80  WR=20.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L16.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=197  W=56/L=141  WR=28.4%
- Sharpen: sharpest is BBP=BBP6 (80/141 of losers there)
- **Sharp: n=101  W=21/L=80  WR=20.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L17.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=197  W=56/L=141  WR=28.4%
- Sharpen: sharpest is BBP=BBP6 (80/141 of losers there)
- **Sharp: n=101  W=21/L=80  WR=20.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L18.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=193  W=65/L=128  WR=33.7%
- Sharpen: sharpest is T4=T4c (94/128 of losers there)
- **Sharp: n=126  W=32/L=94  WR=25.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60a AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=193  W=65/L=128  WR=33.7%
- Sharpen: sharpest is T4=T4c (94/128 of losers there)
- **Sharp: n=126  W=32/L=94  WR=25.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=191  W=65/L=126  WR=34.0%
- Sharpen: sharpest is T4=T4c (94/126 of losers there)
- **Sharp: n=126  W=32/L=94  WR=25.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=187  W=60/L=127  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=187  W=60/L=127  WR=32.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L22.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=187  W=60/L=127  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=187  W=60/L=127  WR=32.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L23.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=187  W=60/L=127  WR=32.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=187  W=60/L=127  WR=32.1%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L24.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=186  W=62/L=124  WR=33.3%
- Sharpen: sharpest is BBP=BBP6 (22/124 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when deep above upper band

### L25.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=185  W=60/L=125  WR=32.4%
- Sharpen: sharpest is ZS=ZS5 (118/125 of losers there)
- **Sharp: n=157  W=39/L=118  WR=24.8%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | T4a(54/48) | T4c(46/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
