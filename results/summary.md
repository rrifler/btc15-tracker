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
- Windows scored: 2113; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (223 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 201/439 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-22T21:15Z (market 6027000, result up)
Scored: p1 down filled at 93s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6099999756, 5s@0.6, 23s@0.58, 23s@0.5599999686, 23s@0.57, 23s@0.56, 23s@0.5599999923, 23s@0.56, 26s@0.58, 26s@0.5799999882, 26s@0.5799999973, 26s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.45, 47s@0.46, 93s@0.21, 95s@0.2099999972, 98s@0.2, 98s@0.189999976, 99s@0.2, 99s@0.2, 104s@0.21, 107s@0.21, 113s@0.22, 134s@0.2 ...

### 2026-10-23T00:00Z (market 6031438, result down)
Scored: p1 up filled at 30s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 30s@0.219999978, 41s@0.1799999976, 47s@0.16, 48s@0.16, 48s@0.16, 48s@0.16, 48s@0.16, 48s@0.16, 51s@0.16, 54s@0.1499999993, 57s@0.1499999925, 60s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5415833333, 3s@0.56, 3s@0.559999776, 3s@0.56, 5s@0.6, 5s@0.58, 6s@0.6499999678, 6s@0.593877551, 8s@0.65, 11s@0.66, 11s@0.65, 12s@0.6899999933 ...

### 2026-10-23T01:00Z (market 6032896, result up)
Scored: p1 down filled at 95s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 5s@0.54, 6s@0.53, 6s@0.5299998463, 12s@0.5499998087, 12s@0.549999945, 18s@0.5399999325, 29s@0.549999979, 29s@0.55, 30s@0.55, 32s@0.5499997885, 35s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.469999998, 6s@0.47, 11s@0.4599999879, 12s@0.4599999928, 15s@0.4599999725, 17s@0.4599999828, 17s@0.46, 21s@0.45, 35s@0.4699999773, 39s@0.48, 44s@0.5, 44s@0.5 ...

### 2026-10-23T01:15Z (market 6032958, result up)
Scored: p1 up filled at 27s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 27s@0.2299999945, 33s@0.2, 35s@0.1899999998, 57s@0.1699999947, 60s@0.16, 68s@0.1965297297, 68s@0.1899999939, 68s@0.1899999962, 68s@0.19, 69s@0.2, 69s@0.19, 69s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.57, 6s@0.59999994, 6s@0.602143838, 12s@0.61, 17s@0.67, 17s@0.67, 17s@0.6699999823, 18s@0.7, 20s@0.71, 21s@0.72, 23s@0.73, 24s@0.74 ...

### 2026-10-23T01:45Z (market 6033102, result down)
Scored: p1 down filled at 74s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6, 6s@0.63, 6s@0.6, 6s@0.63, 8s@0.63, 8s@0.63, 8s@0.629999937, 15s@0.62, 15s@0.62, 15s@0.62, 17s@0.6299999578, 17s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 53s@0.25, 53s@0.25, 60s@0.25, 62s@0.25, 62s@0.25, 74s@0.2, 108s@0.12, 111s@0.12, 113s@0.11, 117s@0.1199999976, 117s@0.1199999904, 129s@0.1099999999 ...


_Updated 2026-10-23 03:37Z_
