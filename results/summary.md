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
- Windows scored: 1873; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (178 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 174/388 = 44.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-20T09:45Z (market 5918992, result up)
Scored: p1 up filled at 113s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5199999792, 3s@0.46, 113s@0.25, 113s@0.24, 113s@0.24, 113s@0.21, 114s@0.22, 119s@0.2199999998, 122s@0.2199999993, 123s@0.219999978, 128s@0.2199999995, 129s@0.2228621238 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5149625935, 3s@0.5699999886, 3s@0.5599999928, 3s@0.55, 5s@0.57, 11s@0.61, 17s@0.62, 17s@0.6599999723, 17s@0.614, 20s@0.66, 24s@0.65, 30s@0.5699999886 ...

### 2026-10-20T11:00Z (market 5919999, result up)
Scored: p1 down filled at 68s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5899999145, 5s@0.54, 8s@0.54, 11s@0.54, 12s@0.6, 15s@0.55, 17s@0.55, 18s@0.5599999934, 18s@0.6, 20s@0.6, 21s@0.659999963, 21s@0.6560636115 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.469999906, 6s@0.47, 6s@0.47, 6s@0.47, 68s@0.2299999517, 69s@0.25, 69s@0.24, 77s@0.25, 80s@0.2299999898, 101s@0.18, 104s@0.17, 107s@0.2099999895 ...

### 2026-10-20T11:45Z (market 5920396, result down)
Scored: p1 up filled at 42s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999563, 14s@0.25, 14s@0.25, 15s@0.25, 17s@0.25, 17s@0.25, 17s@0.25, 18s@0.25, 39s@0.25, 39s@0.25, 42s@0.24, 44s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.59, 5s@0.5899999145, 5s@0.5733333333, 8s@0.6, 11s@0.7199999934, 11s@0.7399999773, 11s@0.73, 11s@0.72, 11s@0.66, 11s@0.6599999448, 12s@0.75, 12s@0.75 ...

### 2026-10-20T12:45Z (market 5922439, result down)
Scored: p1 down filled at 27s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.54, 3s@0.58, 3s@0.5799999768, 5s@0.58, 5s@0.58, 5s@0.58, 5s@0.58, 5s@0.58, 5s@0.58, 5s@0.58, 14s@0.6699999163, 14s@0.6699999611 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 27s@0.24, 47s@0.45, 48s@0.5, 50s@0.51, 51s@0.54, 53s@0.55, 54s@0.5756521739, 54s@0.5699999673, 56s@0.6, 56s@0.59, 56s@0.59, 57s@0.599999976 ...

### 2026-10-20T13:00Z (market 5922597, result down)
Scored: p1 up filled at 96s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.52, 6s@0.52, 6s@0.4975, 8s@0.5, 12s@0.47, 96s@0.18, 101s@0.179999991, 105s@0.18, 111s@0.1699999983, 111s@0.17, 116s@0.1699999983, 117s@0.1699999944 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.51, 3s@0.5099999516, 5s@0.5199999914, 5s@0.52, 5s@0.52, 6s@0.5, 11s@0.51, 11s@0.51, 14s@0.54, 15s@0.55, 15s@0.54, 30s@0.6 ...


_Updated 2026-10-20 15:38Z_
