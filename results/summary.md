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
- Windows scored: 2372; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (278 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 228/500 = 45.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-25T14:00Z (market 6132607, result up)
Scored: p1 up filled at 96s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.49, 3s@0.49, 96s@0.23, 99s@0.22, 104s@0.22, 105s@0.22, 105s@0.22, 111s@0.2325251925, 111s@0.24, 111s@0.2299999517, 113s@0.24, 116s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5828571429, 26s@0.6299999829, 26s@0.6101586728, 33s@0.67, 35s@0.6699999964, 42s@0.66, 45s@0.6599999991, 45s@0.6599998944, 63s@0.6199999053, 74s@0.6199999864, 80s@0.67, 80s@0.68 ...

### 2026-10-25T15:00Z (market 6134164, result up)
Scored: p1 down filled at 47s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4563909293, 3s@0.45, 6s@0.5299999826, 6s@0.52, 6s@0.5, 6s@0.48, 6s@0.4799999687, 17s@0.56, 17s@0.56, 17s@0.55, 18s@0.5599999955, 23s@0.5599999851 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.56, 3s@0.5299998463, 5s@0.53, 5s@0.53, 5s@0.53, 5s@0.5299999839, 6s@0.48, 6s@0.4799999904, 6s@0.48, 6s@0.49, 8s@0.4799999705, 8s@0.48 ...

### 2026-10-25T15:30Z (market 6136105, result up)
Scored: p1 down filled at 72s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.54, 3s@0.57, 3s@0.54, 3s@0.54, 8s@0.5976267536, 8s@0.61, 9s@0.61, 12s@0.63, 12s@0.6227757982, 14s@0.6299999896, 14s@0.63, 15s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 68s@0.25, 72s@0.24, 78s@0.25, 84s@0.229999994, 92s@0.25, 92s@0.23, 92s@0.23, 101s@0.19, 101s@0.18, 102s@0.19, 110s@0.2, 116s@0.2 ...

### 2026-10-25T16:30Z (market 6139708, result up)
Scored: p1 down filled at 32s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6, 3s@0.6, 3s@0.6299999181, 3s@0.62, 6s@0.7, 6s@0.7, 6s@0.7, 6s@0.7, 8s@0.69, 8s@0.69, 24s@0.7, 24s@0.6999999856 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 32s@0.2399999952, 32s@0.229999994, 33s@0.2399999981, 42s@0.2299999517, 50s@0.1699999983, 57s@0.16, 57s@0.16, 74s@0.14, 75s@0.1399999943, 84s@0.19, 87s@0.19, 96s@0.22 ...

### 2026-10-25T18:00Z (market 6145046, result down)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 8s@0.4599999833, 12s@0.47, 14s@0.49, 14s@0.4899999531, 14s@0.4899999531, 21s@0.47, 69s@0.5332309322, 71s@0.8799999909, 71s@0.61, 71s@0.8015607007, 71s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5199999659, 6s@0.53, 8s@0.55, 8s@0.54, 8s@0.55, 9s@0.55, 20s@0.53, 21s@0.5599999382, 21s@0.5499999241, 21s@0.55, 21s@0.55, 21s@0.54 ...


_Updated 2026-10-25 20:31Z_
