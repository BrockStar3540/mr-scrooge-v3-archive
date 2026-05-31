# AUD_CHF — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,841**  (W=1,188 / L=653)  -  WR: **64.5%**

## Session distribution

- asia: n=655  W=413/L=242  WR=63.1%
- ny_mid: n=462  W=311/L=151  WR=67.3%
- london_open: n=217  W=140/L=77  WR=64.5%
- ny_close: n=185  W=114/L=71  WR=61.6%
- london: n=126  W=81/L=45  WR=64.3%
- ny_open: n=99  W=65/L=34  WR=65.7%
- asia_late: n=70  W=46/L=24  WR=65.7%
- off_hours: n=27  W=18/L=9  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=129  W=119/L=10  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 5/10 losers (50%)
- **Final: n=121  W=116/L=5  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W02.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=129  W=119/L=10  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 5/10 losers (50%)
- **Final: n=121  W=116/L=5  WR=95.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W03.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=129  W=119/L=10  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 5/10 losers (50%)
- **Final: n=121  W=116/L=5  WR=95.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W04.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=129  W=119/L=10  WR=92.2%
- Refine: exclude session_bucket=ny_open drops 5/10 losers (50%)
- **Final: n=121  W=116/L=5  WR=95.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_open

### W05.  `H20=H20a AND H60=H60a AND T4=T4c`
- Raw: n=117  W=112/L=5  WR=95.7%
- Refine: exclude ZS=ZS3 drops 4/5 losers (80%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=117  W=112/L=5  WR=95.7%
- Refine: exclude ZS=ZS3 drops 4/5 losers (80%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=117  W=112/L=5  WR=95.7%
- Refine: exclude ZS=ZS3 drops 4/5 losers (80%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=117  W=112/L=5  WR=95.7%
- Refine: exclude ZS=ZS3 drops 4/5 losers (80%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=117  W=112/L=5  WR=95.7%
- Refine: exclude ZS=ZS3 drops 4/5 losers (80%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=117  W=112/L=5  WR=95.7%
- Refine: exclude ZS=ZS3 drops 4/5 losers (80%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W11.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude session_bucket=ny_open drops 5/8 losers (62%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W12.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude session_bucket=ny_open drops 5/8 losers (62%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W13.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude session_bucket=ny_open drops 5/8 losers (62%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W14.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude session_bucket=ny_open drops 5/8 losers (62%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W15.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude session_bucket=ny_open drops 5/8 losers (62%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W16.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=105/L=8  WR=92.9%
- Refine: exclude session_bucket=ny_open drops 5/8 losers (62%)
- **Final: n=105  W=102/L=3  WR=97.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_open

### W17.  `H20=H20a AND T4=T4c AND RSI=RSI5`
- Raw: n=101  W=98/L=3  WR=97.0%
- Refine: exclude session_bucket=ny_close drops 2/3 losers (67%)
- **Final: n=92  W=91/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W18.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=101  W=98/L=3  WR=97.0%
- Refine: exclude session_bucket=ny_close drops 2/3 losers (67%)
- **Final: n=92  W=91/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W19.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=101  W=98/L=3  WR=97.0%
- Refine: exclude session_bucket=ny_close drops 2/3 losers (67%)
- **Final: n=92  W=91/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W20.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=101  W=98/L=3  WR=97.0%
- Refine: exclude session_bucket=ny_close drops 2/3 losers (67%)
- **Final: n=92  W=91/L=1  WR=98.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W21.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W22.  `T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W23.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W24.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W25.  `H60=H60a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude T4=T4a drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=london_open (20/100 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L02.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is session_bucket=london_open (20/100 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L03.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=asia_late (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia_late

### L04.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=asia_late (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=asia_late

### L05.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=asia_late (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia_late

### L06.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is session_bucket=asia_late (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia_late

### L07.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (31/63 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when session=asia

### L08.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (31/63 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when session=asia

### L09.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=104  W=41/L=63  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (31/63 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when session=asia

### L10.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (16/64 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L11.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (16/64 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L12.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (16/64 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L13.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (16/64 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L14.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (16/64 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L15.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (16/64 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when session=asia_late

### L16.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=98  W=32/L=66  WR=32.7%
- Sharpen: sharpest is session_bucket=asia_late (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=asia_late

### L17.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=98  W=32/L=66  WR=32.7%
- Sharpen: sharpest is session_bucket=asia_late (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia_late

### L18.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=98  W=32/L=66  WR=32.7%
- Sharpen: sharpest is session_bucket=asia_late (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when session=asia_late

### L19.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=98  W=32/L=66  WR=32.7%
- Sharpen: sharpest is session_bucket=asia_late (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia_late

### L20.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=98  W=32/L=66  WR=32.7%
- Sharpen: sharpest is session_bucket=asia_late (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when session=asia_late

### L21.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=98  W=32/L=66  WR=32.7%
- Sharpen: sharpest is session_bucket=asia_late (16/66 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia_late

### L22.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (31/59 of losers there)
- **Sharp: n=39  W=8/L=31  WR=20.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong  •  ONLY when session=asia

### L23.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=asia (29/58 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=asia

### L24.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=asia (29/58 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=asia

### L25.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is session_bucket=asia (29/58 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/38) | H20e(43/48) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(56/46) | T4a(44/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
