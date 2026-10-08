# BTC 15-min strategy tracker: FAIL

Data source: INTL_PROXY. INTL_PROXY means trades from the international exchange, used because the US gateway publishes no public trade history.
Real money needs PASS in both the backtest and the live paper run, with the live hit rate within 8 points of the backtest.

## Backtest

- Verdict: **FAIL**
- Windows scored: 700; excluded: 0
- Fill rate: 16.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 52 of 118 = 44.1% (95% range 35.4% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.35 (balance $7.65 from $20)
- Longest losing streak: 9
- Strict vs touch: strict 52/118 = 44.1%; touch 67/136 = 49.3%. The verdict uses strict.

## Live paper run

- Verdict: **FAIL**
- Windows scored: 741; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 53 of 121 = 43.8% (95% range 35.3% to 52.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.80 (balance $7.20 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 53/121 = 43.8%; touch 59/131 = 45.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-08T15:15Z (market 5406435, result down)
Scored: p1 up filled at 117s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 5s@0.45, 5s@0.45, 6s@0.46, 6s@0.45, 11s@0.45, 69s@0.48, 69s@0.4599999269, 72s@0.5, 75s@0.4699999944, 80s@0.4799999846, 83s@0.4799999899 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 3s@0.565, 5s@0.56, 6s@0.5599999328, 8s@0.56, 8s@0.5599999686, 9s@0.5699999735, 9s@0.5699999731, 11s@0.559999776, 14s@0.57, 14s@0.5699999214, 17s@0.61 ...

### 2026-10-08T16:30Z (market 5407708, result down)
Scored: p1 up filled at 99s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.48, 6s@0.45, 6s@0.45, 8s@0.45, 8s@0.45, 9s@0.48, 29s@0.4599999269, 29s@0.4599999269, 30s@0.46, 32s@0.5, 32s@0.4699999422, 33s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.549999945, 6s@0.55, 6s@0.53, 11s@0.5299999512, 11s@0.5299999959, 12s@0.53, 14s@0.56, 14s@0.5699999443, 14s@0.56, 14s@0.54, 15s@0.58, 15s@0.5799999383 ...

### 2026-10-08T18:15Z (market 5410449, result up)
Scored: p1 down filled at 41s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.68, 3s@0.6799998912, 3s@0.64934374, 5s@0.69, 5s@0.69, 5s@0.6899999433, 6s@0.69, 8s@0.69, 17s@0.7, 17s@0.7, 17s@0.7, 17s@0.699999993 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 35s@0.25, 41s@0.219999978, 50s@0.21, 56s@0.17, 57s@0.17, 59s@0.16, 65s@0.13, 68s@0.1399999832, 71s@0.15, 71s@0.15, 71s@0.14, 71s@0.14 ...


_Updated 2026-10-08 20:27Z_
