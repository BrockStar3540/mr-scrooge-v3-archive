# AUD_NZD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,399**  (W=887 / L=512)  -  WR: **63.4%**

## Session distribution

- asia: n=573  W=358/L=215  WR=62.5%
- ny_close: n=197  W=139/L=58  WR=70.6%
- ny_mid: n=181  W=116/L=65  WR=64.1%
- london_open: n=159  W=105/L=54  WR=66.0%
- off_hours: n=81  W=46/L=35  WR=56.8%
- london: n=75  W=41/L=34  WR=54.7%
- ny_open: n=75  W=46/L=29  WR=61.3%
- asia_late: n=58  W=36/L=22  WR=62.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W02.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W03.  `H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_close  •  AVOID when deep above upper band

### W04.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W05.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W06.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W07.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W08.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W09.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W10.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W11.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude BBP=BBP6 drops 7/16 losers (44%)
- **Final: n=95  W=86/L=9  WR=90.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W12.  `H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W13.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W14.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W15.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W16.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W17.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W18.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W19.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W20.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude BBP=BBP6 drops 7/13 losers (54%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W21.  `H20=H20a AND H60=H60a AND session_bucket=ny_close`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  AVOID when deep above upper band

### W22.  `H20=H20a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W23.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when deep above upper band

### W24.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude BBP=BBP6 drops 7/14 losers (50%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  AVOID when deep above upper band

### W25.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H20=H20e drops 14/14 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is BBP=BBP2 (16/40 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when lower third

### L02.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is BBP=BBP2 (16/40 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  ONLY when lower third

### L03.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is BBP=BBP2 (16/40 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  ONLY when lower third

### L04.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is BBP=BBP2 (16/40 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when lower third

### L05.  `H60=H60a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L06.  `T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L07.  `BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  lower third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L08.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60a AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L10.  `T4=T4a AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is RSI=RSI3 (21/41 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L11.  `H20=H20a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=55  W=8/L=47  WR=14.5%
- Sharpen: sharpest is T1=T1a (13/47 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 1h trend WITH trade

### L12.  `H60=H60a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L13.  `T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L14.  `ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L15.  `H60=H60a AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L16.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L17.  `H60=H60a AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L18.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L19.  `T4=T4a AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L20.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=48  W=16/L=32  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (16/32 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is session_bucket=off_hours (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when session=off_hours

### L22.  `H60=H60a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is T1=T1a (23/29 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend WITH trade

### L23.  `T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is T1=T1a (23/29 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend WITH trade

### L24.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is T1=T1a (23/29 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend WITH trade

### L25.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is T1=T1a (23/29 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/39) | H20e(37/45) |
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
