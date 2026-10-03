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

- Verdict: **NOT ENOUGH DATA**
- Windows scored: 263; excluded: 0
- Fill rate: 19.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 23 of 50 = 46.0% (95% range 33.0% to 59.6%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.45 (balance $13.55 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 23/50 = 46.0%; touch 26/54 = 48.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-03T14:45Z (market 5205415, result up)
Scored: p1 down filled at 86s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.559999776, 8s@0.55, 9s@0.5499999934, 9s@0.5499999854, 9s@0.55, 9s@0.5499998396, 11s@0.5499998382, 15s@0.549999945, 15s@0.5499999954, 15s@0.5499999995, 20s@0.55, 20s@0.5499999222 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 11s@0.46, 15s@0.46, 86s@0.2, 90s@0.18, 99s@0.1899999998, 102s@0.19, 102s@0.19, 102s@0.19, 104s@0.16, 104s@0.18, 114s@0.169999993 ...

### 2026-10-03T15:00Z (market 5205709, result up)
Scored: p1 up filled at 69s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.56, 5s@0.5799999991, 6s@0.58, 11s@0.49, 12s@0.4899998383, 12s@0.48999997, 12s@0.4899999824, 14s@0.49, 69s@0.21, 77s@0.21, 80s@0.2, 83s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.45, 9s@0.5125806452, 9s@0.45, 9s@0.46, 9s@0.45, 12s@0.5499999948, 12s@0.5499999325, 12s@0.52, 12s@0.52, 14s@0.6999999706, 14s@0.682128, 14s@0.69 ...

### 2026-10-03T15:30Z (market 5206803, result down)
Scored: p1 up filled at 95s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 93s@0.25, 93s@0.25, 95s@0.25, 95s@0.25, 95s@0.25, 95s@0.25, 95s@0.24, 95s@0.24, 95s@0.24, 95s@0.24, 95s@0.25, 95s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.59, 3s@0.6240852575, 3s@0.6336633663, 5s@0.609999986, 5s@0.59, 8s@0.61, 14s@0.6299999943, 14s@0.61, 15s@0.6299998362, 18s@0.63, 23s@0.62, 24s@0.64 ...

### 2026-10-03T17:30Z (market 5208745, result up)
Scored: p1 up filled at 54s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 54s@0.24, 56s@0.23, 56s@0.23, 57s@0.2299999996, 57s@0.2299999517, 60s@0.2, 62s@0.15, 69s@0.16, 90s@0.14, 95s@0.1066666667, 96s@0.1099999925, 99s@0.1099999998 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.62, 3s@0.6199998946, 5s@0.65, 5s@0.65, 5s@0.65, 5s@0.64, 5s@0.64, 5s@0.64, 6s@0.6417721482, 6s@0.649999805, 9s@0.65, 17s@0.7 ...


_Updated 2026-10-03 19:02Z_
