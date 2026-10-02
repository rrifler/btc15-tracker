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
- Windows scored: 153; excluded: 0
- Fill rate: 21.6% of scored windows had a fill (0 too small)
- Fills that reached 45c: 13 of 33 = 39.4% (95% range 24.7% to 56.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.95 (balance $13.05 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 13/33 = 39.4%; touch 16/37 = 43.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-02T09:30Z (market 5172885, result up)
Scored: p1 down filled at 81s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.658, 3s@0.68, 6s@0.62, 8s@0.6199998512, 8s@0.63, 11s@0.6199998784, 11s@0.6, 14s@0.63, 14s@0.62, 14s@0.63, 14s@0.61, 14s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 81s@0.2399999808, 105s@0.1, 105s@0.1, 110s@0.1, 110s@0.11, 111s@0.1, 113s@0.1099999951, 117s@0.1, 122s@0.1, 128s@0.0899999928, 132s@0.1, 132s@0.1 ...

### 2026-10-02T12:00Z (market 5174789, result down)
Scored: p1 up filled at 92s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.49, 92s@0.2464997042, 92s@0.25, 111s@0.25, 113s@0.25, 113s@0.25, 114s@0.25, 119s@0.25, 123s@0.24, 125s@0.21, 131s@0.2, 134s@0.1951219512 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5099999966, 2s@0.5099999966, 2s@0.5099999966, 2s@0.51, 2s@0.51, 2s@0.51, 3s@0.51, 3s@0.51, 3s@0.51, 3s@0.5099999994, 3s@0.51, 3s@0.5099999994 ...

### 2026-10-02T12:15Z (market 5174941, result up)
Scored: p1 down filled at 119s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.52, 20s@0.5399999957, 20s@0.52, 20s@0.53, 20s@0.53, 20s@0.53, 20s@0.5299999251, 20s@0.5, 20s@0.5, 21s@0.54, 26s@0.549999945, 27s@0.549999945 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4899998383, 5s@0.4899998383, 15s@0.51, 15s@0.5099999966, 15s@0.5, 15s@0.5, 15s@0.5, 21s@0.46, 30s@0.4599997976, 119s@0.2291071429, 119s@0.24, 119s@0.2 ...

### 2026-10-02T12:30Z (market 5175161, result down)
Scored: p1 down filled at 8s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.4757192153, 3s@0.5347826087, 3s@0.46, 3s@0.45, 5s@0.673336502, 5s@0.61, 5s@0.5799999658, 5s@0.64, 5s@0.58, 5s@0.64, 5s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5499999994, 3s@0.5499999963, 3s@0.5499999846, 3s@0.5499999214, 3s@0.55, 3s@0.55, 3s@0.5499999968, 3s@0.5, 3s@0.5499999717, 3s@0.54, 3s@0.5399999719, 3s@0.5499999846 ...

### 2026-10-02T12:45Z (market 5175296, result up)
Scored: p1 down filled at 98s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.4799999846, 5s@0.5, 5s@0.5099998215, 5s@0.50185, 5s@0.51, 11s@0.4899999491, 14s@0.51, 14s@0.48, 15s@0.5199999971, 17s@0.54, 17s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.52, 5s@0.5, 6s@0.5599999642, 6s@0.55, 6s@0.549999945, 6s@0.5399999773, 8s@0.56, 8s@0.56, 9s@0.5599999976, 11s@0.5599998682, 15s@0.48, 18s@0.4599999687 ...


_Updated 2026-10-02 15:26Z_
