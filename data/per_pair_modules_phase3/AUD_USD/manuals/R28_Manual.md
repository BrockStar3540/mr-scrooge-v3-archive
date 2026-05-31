# AUD_USD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,536**  (W=973 / L=563)  -  WR: **63.3%**

## Session distribution

- asia: n=360  W=231/L=129  WR=64.2%
- ny_mid: n=349  W=237/L=112  WR=67.9%
- ny_open: n=228  W=146/L=82  WR=64.0%
- ny_close: n=166  W=96/L=70  WR=57.8%
- asia_late: n=150  W=87/L=63  WR=58.0%
- london_open: n=148  W=92/L=56  WR=62.2%
- london: n=126  W=78/L=48  WR=61.9%
- off_hours: n=9  W=6/L=3  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60e AND T1=T1a`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=ny_open

### W02.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_open

### W03.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when session=ny_open

### W04.  `H20=H20a AND T1=T1a AND T4=T4a`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W05.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_open

### W06.  `H20=H20a AND T4=T4a AND direction_exec=short`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W07.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W08.  `H20=H20a AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=ny_open

### W09.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_open

### W10.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=174  W=153/L=21  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 13/21 losers (62%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W11.  `H60=H60e AND T1=T1a AND BBP=BBP0`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude H20=H20e drops 16/17 losers (94%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W12.  `H60=H60e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude H20=H20e drops 16/17 losers (94%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band  •  AVOID when HTF20 strongly against

### W13.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude H20=H20e drops 16/17 losers (94%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W14.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude H20=H20e drops 16/17 losers (94%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W15.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude H60=H60a drops 5/12 losers (42%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W16.  `H60=H60e AND T4=T4a AND BBP=BBP0`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W17.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W18.  `T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W19.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W20.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W21.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W22.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W23.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W24.  `H60=H60e AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H20=H20e drops 11/12 losers (92%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L02.  `H20=H20e AND H60=H60a AND T4=T4c`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L03.  `H20=H20e AND H60=H60a AND direction_exec=long`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade  •  ONLY when deep below lower band

### L04.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L05.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L06.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L07.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L08.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when deep below lower band

### L09.  `H20=H20e AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L10.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is BBP=BBP0 (30/90 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when deep below lower band

### L11.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (34/67 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (34/67 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (34/67 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (34/67 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (34/67 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (34/67 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H60=H60a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is T4=T4c (52/66 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is T4=T4c (52/66 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L19.  `RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is T4=T4c (52/66 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: LONG**  •  RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L20.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is T4=T4c (52/66 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is T4=T4c (52/66 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L22.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is T4=T4c (52/66 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L23.  `T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is H60=H60a (52/64 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L24.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=95  W=32/L=63  WR=33.7%
- Sharpen: sharpest is ZS=ZS1 (33/63 of losers there)
- **Sharp: n=38  W=5/L=33  WR=13.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H60=H60a AND T1=T1c AND BBP=BBP0`
- Raw: n=95  W=35/L=60  WR=36.8%
- Sharpen: sharpest is H20=H20e (30/60 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(49/35), H20b(9/1) | H20e(36/48), H20d(1/9) |
| H60 | H60e(56/43) | H60a(44/57) |
| T1 | T1a(56/42) | T1c(44/58) |
| T4 | T4a(56/46) | T4c(44/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/43) | long(44/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
