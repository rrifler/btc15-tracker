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
- Windows scored: 2321; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.9% of scored windows had a fill (265 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 223/487 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-25T02:30Z (market 6103529, result up)
Scored: p1 down filled at 39s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.549999945, 5s@0.549999945, 5s@0.5498904734, 11s@0.549999945, 23s@0.55, 23s@0.5499999876, 36s@0.7035360679, 36s@0.6999999829, 36s@0.63, 38s@0.77, 38s@0.7699999885, 38s@0.7699999891 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.47, 5s@0.4599997976, 8s@0.45, 15s@0.4599997976, 39s@0.2399999808, 41s@0.219999978, 44s@0.219999978, 44s@0.2199999873, 45s@0.2199999941, 47s@0.2199999939, 47s@0.22, 47s@0.22 ...

### 2026-10-25T05:45Z (market 6109271, result up)
Scored: p1 up filled at 80s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.54, 3s@0.5299999868, 3s@0.5105882353, 3s@0.51, 5s@0.53, 5s@0.53, 5s@0.53, 5s@0.53, 5s@0.53, 5s@0.53, 5s@0.53, 5s@0.5299999946 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 3s@0.48, 3s@0.4818970552, 6s@0.4599999962, 9s@0.4599999993, 9s@0.4638843932, 9s@0.47, 9s@0.47, 9s@0.46, 32s@0.4699999926, 32s@0.4699999926, 32s@0.4799999781 ...

### 2026-10-25T07:00Z (market 6111796, result up)
Scored: p1 down filled at 60s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.54, 5s@0.5699999556, 6s@0.6, 8s@0.59, 9s@0.5899998399, 9s@0.5899999145, 12s@0.58, 12s@0.59, 14s@0.58, 14s@0.5799999189, 17s@0.58, 18s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 60s@0.2399999808, 78s@0.24, 81s@0.24, 83s@0.24, 95s@0.24, 96s@0.24, 96s@0.24, 102s@0.25, 129s@0.25, 234s@0.1872972973, 236s@0.1899999824, 243s@0.1499999993 ...


_Updated 2026-10-25 07:40Z_
