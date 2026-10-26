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
- Windows scored: 2479; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (300 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 245/527 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-26T17:30Z (market 6211641, result down)
Scored: p1 up filled at 47s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 47s@0.24, 53s@0.21, 54s@0.2, 57s@0.2299999693, 65s@0.23, 155s@0.45, 168s@0.5099999716, 168s@0.5044472222, 168s@0.5021885417, 168s@0.5, 168s@0.5, 170s@0.5099999758 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.55, 3s@0.57, 3s@0.55, 3s@0.55, 5s@0.64, 5s@0.63, 6s@0.64, 8s@0.64, 12s@0.6299999885, 14s@0.6299998973, 15s@0.629999995, 17s@0.64 ...

### 2026-10-26T19:00Z (market 6219249, result up)
Scored: p1 up filled at 53s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 53s@0.2099999983, 53s@0.2099999929, 54s@0.2, 54s@0.2099999969, 54s@0.2099999919, 56s@0.2, 56s@0.2, 56s@0.2, 62s@0.19, 63s@0.1899999962, 65s@0.19, 69s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5799999882, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.6199998512, 3s@0.64, 3s@0.61, 3s@0.6, 5s@0.6499999717, 5s@0.64 ...

### 2026-10-26T20:00Z (market 6222026, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.49, 5s@0.5, 5s@0.5, 8s@0.49, 57s@0.2399999808, 62s@0.2399999808, 63s@0.21, 66s@0.2, 71s@0.2, 72s@0.2, 72s@0.2, 72s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 2s@0.5199999692, 2s@0.5, 2s@0.5, 3s@0.5, 5s@0.5, 6s@0.4616666667, 8s@0.5099999144, 8s@0.5, 8s@0.49, 8s@0.48, 8s@0.4693055556 ...

### 2026-10-26T21:00Z (market 6224474, result up)
Scored: p1 down filled at 38s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 6s@0.5, 8s@0.5112027907, 8s@0.5038096618, 11s@0.5199999792, 17s@0.52, 17s@0.52, 17s@0.5199999843, 26s@0.7, 26s@0.68, 26s@0.68, 26s@0.6285225893 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.51, 9s@0.49, 11s@0.49, 12s@0.49, 24s@0.4599999311, 38s@0.2299999945, 44s@0.2099999983, 45s@0.21, 53s@0.2, 53s@0.2099999983, 57s@0.2099999895, 57s@0.2099999983 ...

### 2026-10-26T22:00Z (market 6227005, result down)
Scored: p1 up filled at 18s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.46, 8s@0.4599999787, 18s@0.2399999808, 21s@0.23, 21s@0.2299999993, 23s@0.19, 23s@0.2, 26s@0.21, 26s@0.2, 33s@0.25, 36s@0.2, 42s@0.1799999986 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.58, 12s@0.565, 12s@0.5799999768, 12s@0.55, 12s@0.5499999347, 12s@0.55, 12s@0.5399999327, 12s@0.53, 12s@0.53, 14s@0.65, 14s@0.63, 14s@0.5987030885 ...


_Updated 2026-10-26 23:33Z_
