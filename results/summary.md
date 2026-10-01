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
- Windows scored: 13; excluded: 0
- Fill rate: 30.8% of scored windows had a fill (0 too small)
- Fills that reached 45c: 3 of 4 = 75.0% (95% range 30.1% to 95.4%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $1.20 (balance $21.20 from $20)
- Longest losing streak: 1
- Strict vs touch: strict 3/4 = 75.0%; touch 3/4 = 75.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-01T01:15Z (market 5144896, result up)
Scored: p1 up filled at 36s, exit hit 1; p2 none. Profit p1 0.8.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 32s@0.25, 32s@0.25, 35s@0.25, 36s@0.2399999808, 42s@0.25, 42s@0.2299999517, 44s@0.235, 63s@0.48, 65s@0.49, 65s@0.49, 65s@0.48, 65s@0.4799998551 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6299999892, 2s@0.57, 5s@0.63, 6s@0.73, 6s@0.7, 6s@0.6702354145, 6s@0.7, 6s@0.7, 6s@0.6504347487, 8s@0.7399999803, 8s@0.73, 8s@0.72 ...

### 2026-10-01T01:30Z (market 5144966, result down)
Scored: p1 up filled at 53s, exit hit 0; p2 none. Profit p1 -1.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.47, 2s@0.47, 53s@0.23, 56s@0.2399999808, 56s@0.24, 56s@0.23, 62s@0.2, 62s@0.2099999995, 69s@0.14, 69s@0.13, 72s@0.14, 72s@0.1399999832 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 5s@0.5899999841, 9s@0.59, 11s@0.64, 11s@0.64, 11s@0.62, 11s@0.59, 12s@0.65, 12s@0.66, 27s@0.659999934, 27s@0.65, 29s@0.7056661135 ...

### 2026-10-01T02:30Z (market 5145460, result down)
Scored: p1 down filled at 42s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5699999479, 3s@0.57, 5s@0.599999988, 6s@0.6, 9s@0.65, 9s@0.65, 9s@0.6499999888, 11s@0.66, 12s@0.69, 12s@0.68, 12s@0.68, 15s@0.7 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 42s@0.22, 48s@0.23, 156s@0.2399999808, 159s@0.2423220153, 162s@0.24, 170s@0.22, 174s@0.2199999941, 200s@0.25, 201s@0.25, 201s@0.25, 201s@0.25, 201s@0.25 ...

### 2026-10-01T03:30Z (market 5146492, result up)
Scored: p1 up filled at 111s, exit hit 1; p2 none. Profit p1 0.8.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4899999873, 111s@0.23, 114s@0.2299999517, 117s@0.23, 120s@0.23, 128s@0.23, 128s@0.25, 189s@0.45, 191s@0.45, 195s@0.45, 228s@0.5, 228s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4957142857, 3s@0.54, 3s@0.52, 5s@0.5899999966, 5s@0.5899999841, 5s@0.5899999288, 6s@0.58, 9s@0.59, 11s@0.6, 29s@0.5799999768, 36s@0.58, 42s@0.5799999768 ...


_Updated 2026-10-01 04:25Z_
