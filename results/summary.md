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
- Windows scored: 1789; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.2% of scored windows had a fill (151 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 161/361 = 44.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-19T12:15Z (market 5875035, result up)
Scored: p1 down filled at 33s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.59, 5s@0.6199999864, 5s@0.62, 5s@0.618, 8s@0.61, 9s@0.61, 12s@0.6599999448, 12s@0.64, 12s@0.64, 12s@0.6070146775, 14s@0.6799999478, 14s@0.69 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 33s@0.2399999923, 35s@0.219999999, 39s@0.219999978, 41s@0.2399999808, 41s@0.2299999962, 42s@0.2399999981, 57s@0.2199999974, 60s@0.204403243, 60s@0.2, 65s@0.2, 69s@0.21, 75s@0.2 ...

### 2026-10-19T14:30Z (market 5883816, result down)
Scored: p1 up filled at 119s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.61, 0s@0.6, 0s@0.5993575889, 2s@0.6199999434, 3s@0.6499999458, 3s@0.6499999458, 5s@0.62, 11s@0.5699999256, 11s@0.57, 11s@0.5699999841, 11s@0.54, 12s@0.5799999518 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.48, 27s@0.48, 27s@0.48, 27s@0.5, 27s@0.5, 32s@0.48, 35s@0.45, 38s@0.47, 48s@0.47, 50s@0.49, 51s@0.5, 53s@0.52 ...

### 2026-10-19T14:45Z (market 5885213, result up)
Scored: p1 down filled at 51s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.559999776, 6s@0.559999776, 8s@0.5999999016, 8s@0.6, 8s@0.5999999516, 9s@0.6228023599, 11s@0.6199999529, 11s@0.62, 12s@0.6199999957, 14s@0.6077239724, 15s@0.62, 18s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 51s@0.1399999989, 51s@0.13, 53s@0.13, 53s@0.13, 54s@0.13, 54s@0.1299999982, 54s@0.1299999948, 57s@0.109999989, 59s@0.1, 59s@0.1, 60s@0.1099999948, 60s@0.1 ...

### 2026-10-19T15:30Z (market 5887802, result down)
Scored: p1 up filled at 53s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 53s@0.22, 60s@0.24, 60s@0.24, 62s@0.24, 81s@0.19, 84s@0.19, 84s@0.19, 86s@0.1899999962, 87s@0.1931330472, 92s@0.1899999962, 96s@0.1740718834 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.54, 0s@0.54, 3s@0.5499998382, 3s@0.549999945, 5s@0.55, 9s@0.5699999886, 14s@0.5799999448, 14s@0.5799999992, 20s@0.59, 26s@0.6, 30s@0.64, 30s@0.66 ...

### 2026-10-19T17:30Z (market 5895415, result down)
Scored: p1 up filled at 114s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 114s@0.23, 116s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 117s@0.23, 120s@0.1943823501 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6199998512, 5s@0.62, 5s@0.619999916, 11s@0.66, 15s@0.69, 15s@0.68, 15s@0.67, 17s@0.7199999424, 17s@0.7, 20s@0.7299998102, 24s@0.72, 36s@0.729999975 ...


_Updated 2026-10-19 18:42Z_
