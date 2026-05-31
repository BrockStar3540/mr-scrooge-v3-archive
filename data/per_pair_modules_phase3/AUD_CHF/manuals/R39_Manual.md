# AUD_CHF — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **955**  (W=606 / L=349)  -  WR: **63.5%**

## Session distribution

- ny_mid: n=290  W=184/L=106  WR=63.4%
- ny_close: n=250  W=148/L=102  WR=59.2%
- asia: n=124  W=81/L=43  WR=65.3%
- ny_open: n=105  W=71/L=34  WR=67.6%
- london: n=78  W=49/L=29  WR=62.8%
- london_open: n=63  W=46/L=17  WR=73.0%
- off_hours: n=32  W=22/L=10  WR=68.8%
- asia_late: n=13  W=5/L=8  WR=38.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W02.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W03.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W05.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W06.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W07.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W09.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W10.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=248  W=219/L=29  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/29 losers (45%)
- **Final: n=231  W=215/L=16  WR=93.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W11.  `H20=H20a AND T4=T4a AND RSI=RSI5`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W12.  `H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W13.  `T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W14.  `T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W15.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W16.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W17.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W18.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W19.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W20.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude session_bucket=london_open drops 13/23 losers (57%)
- **Final: n=180  W=170/L=10  WR=94.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=london_open

### W21.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=132  W=124/L=8  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W22.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=132  W=124/L=8  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W23.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=132  W=124/L=8  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W24.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=132  W=124/L=8  WR=93.9%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong  •  AVOID when session=london_open

### W25.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude session_bucket=london_open drops 5/13 losers (38%)
- **Final: n=132  W=124/L=8  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_close

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L03.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when session=ny_close

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L05.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_close

### L06.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L07.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L08.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when session=ny_close

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=192  W=71/L=121  WR=37.0%
- Sharpen: sharpest is session_bucket=ny_close (42/121 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=ny_close

### L11.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (40/75 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L12.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (40/75 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when RSI 60-70 strong

### L13.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (40/75 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L14.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=124  W=49/L=75  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (40/75 of losers there)
- **Sharp: n=50  W=10/L=40  WR=20.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=118  W=33/L=85  WR=28.0%
- Sharpen: sharpest is RSI=RSI5 (42/85 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=118  W=33/L=85  WR=28.0%
- Sharpen: sharpest is RSI=RSI5 (42/85 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  ONLY when RSI 60-70 strong

### L17.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=118  W=33/L=85  WR=28.0%
- Sharpen: sharpest is RSI=RSI5 (42/85 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L18.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=118  W=33/L=85  WR=28.0%
- Sharpen: sharpest is RSI=RSI5 (42/85 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is RSI=RSI5 (42/84 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is RSI=RSI5 (42/84 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L21.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is RSI=RSI5 (42/84 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is RSI=RSI5 (42/84 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L23.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is RSI=RSI5 (42/84 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=117  W=33/L=84  WR=28.2%
- Sharpen: sharpest is RSI=RSI5 (42/84 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when RSI 60-70 strong

### L25.  `H20=H20e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=92  W=33/L=59  WR=35.9%
- Sharpen: sharpest is session_bucket=ny_close (18/59 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 60-70 strong  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(59/32) | H20e(37/64) |
| H60 | H60a(63/32) | H60e(37/68) |
| T1 | T1a(63/33) | T1c(37/67) |
| T4 | T4a(55/42) | T4c(45/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(63/32) | short(37/68) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
