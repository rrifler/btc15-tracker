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
- Windows scored: 2488; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (300 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 246/529 = 46.5%. The verdict uses strict.

## Spot-checked windows

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

### 2026-10-26T22:30Z (market 6229448, result up)
Scored: p1 up filled at 63s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5199999792, 63s@0.21, 65s@0.21, 65s@0.21, 68s@0.2, 69s@0.2099999983, 74s@0.2099999983, 74s@0.2099999983, 77s@0.2, 78s@0.2099999895, 80s@0.18, 81s@0.15 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 5s@0.5, 5s@0.5, 6s@0.53, 6s@0.5299999607, 6s@0.5, 8s@0.5903225426, 8s@0.53, 8s@0.53, 9s@0.61, 11s@0.61, 14s@0.6099999488 ...


_Updated 2026-10-27 01:46Z_
