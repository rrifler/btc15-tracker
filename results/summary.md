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
- Windows scored: 2153; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (237 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 208/453 = 45.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-23T07:15Z (market 6037415, result down)
Scored: p1 up filled at 47s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4799998464, 6s@0.4799998464, 47s@0.2299999517, 51s@0.22, 66s@0.219999978, 68s@0.219999978, 68s@0.219999978, 68s@0.219999978, 68s@0.219999978, 68s@0.219999978, 71s@0.17, 77s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5099999776, 5s@0.5199999792, 6s@0.5235283606, 14s@0.59999988, 21s@0.6, 29s@0.59, 30s@0.6499999025, 32s@0.6499999935, 33s@0.67, 36s@0.7, 36s@0.7, 36s@0.7 ...

### 2026-10-23T07:30Z (market 6037568, result down)
Scored: p1 down filled at 105s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.46, 47s@0.5799999448, 47s@0.55, 47s@0.55, 47s@0.5, 47s@0.5, 47s@0.49, 47s@0.5, 47s@0.5, 47s@0.5, 47s@0.5, 47s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5099999776, 2s@0.5099999776, 3s@0.519999984, 5s@0.52, 5s@0.54, 5s@0.52, 6s@0.57, 8s@0.5699999886, 9s@0.5699999886, 12s@0.5699999967, 23s@0.53, 24s@0.54 ...

### 2026-10-23T08:15Z (market 6038020, result up)
Scored: p1 down filled at 66s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5699999983, 6s@0.5599999789, 6s@0.56, 9s@0.619999977, 9s@0.57, 9s@0.5699999774, 17s@0.62, 18s@0.62, 27s@0.649999805, 30s@0.67, 30s@0.67, 33s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 66s@0.1699999974, 69s@0.1699999983, 71s@0.16, 74s@0.1699999983, 75s@0.14, 78s@0.15, 78s@0.15, 80s@0.1699999983, 86s@0.1699999909, 87s@0.16, 92s@0.1499999933, 96s@0.139999993 ...

### 2026-10-23T09:00Z (market 6038234, result up)
Scored: p1 up filled at 35s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 35s@0.24, 35s@0.24, 35s@0.24, 35s@0.2399999941, 36s@0.24, 36s@0.2399999979, 41s@0.23, 47s@0.2104347817, 63s@0.25, 65s@0.25, 71s@0.25, 101s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.59, 15s@0.5999999642, 15s@0.6, 15s@0.6, 15s@0.6, 15s@0.6, 15s@0.5999999607, 17s@0.6, 17s@0.6, 17s@0.59999994, 17s@0.6, 17s@0.6 ...

### 2026-10-23T09:45Z (market 6038462, result up)
Scored: p1 up filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5655884089, 5s@0.5599999496, 8s@0.5399999568, 20s@0.5099999675, 32s@0.4899999929, 72s@0.21, 74s@0.23, 74s@0.2399999693, 74s@0.21, 74s@0.22, 74s@0.21, 74s@0.2099999966 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4648605174, 8s@0.5, 8s@0.5, 8s@0.4699999876, 9s@0.49, 9s@0.5, 12s@0.5, 23s@0.4899999824, 29s@0.5, 29s@0.5, 29s@0.5, 35s@0.5916966496 ...


_Updated 2026-10-23 13:44Z_
