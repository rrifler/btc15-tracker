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
- Windows scored: 1761; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.0% of scored windows had a fill (143 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 157/352 = 44.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-19T05:30Z (market 5857539, result up)
Scored: p1 down filled at 14s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.57, 2s@0.5901638925, 3s@0.6257784749, 3s@0.62, 3s@0.63, 5s@0.67, 5s@0.67, 5s@0.65, 5s@0.65, 6s@0.68, 6s@0.68, 6s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 14s@0.24, 14s@0.25, 14s@0.2483333333, 77s@0.17, 78s@0.18, 80s@0.19, 86s@0.17, 92s@0.14, 96s@0.14, 96s@0.14, 101s@0.18, 102s@0.149999997 ...

### 2026-10-19T07:45Z (market 5863861, result down)
Scored: p1 up filled at 72s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.51, 15s@0.5099999949, 29s@0.5099999984, 48s@0.45, 72s@0.24, 74s@0.2399999808, 77s@0.24, 80s@0.23, 81s@0.2099999983, 81s@0.2, 81s@0.23, 83s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 3s@0.5, 3s@0.5, 3s@0.5, 6s@0.5, 9s@0.5, 17s@0.5, 17s@0.5, 18s@0.5, 18s@0.5, 18s@0.5, 18s@0.5 ...

### 2026-10-19T09:00Z (market 5866083, result down)
Scored: p1 up filled at 48s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.22, 48s@0.219999978, 48s@0.219999978, 54s@0.25, 54s@0.2279371685, 60s@0.23, 60s@0.23, 62s@0.24, 63s@0.24, 71s@0.2299999693, 77s@0.21, 77s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5603932526, 5s@0.5533333333, 8s@0.58, 12s@0.59, 17s@0.61, 20s@0.6699999839, 20s@0.66, 20s@0.65, 20s@0.6423076923, 27s@0.67, 27s@0.6699999996, 30s@0.69 ...

### 2026-10-19T10:30Z (market 5868833, result up)
Scored: p1 up filled at 75s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999886, 3s@0.5699999886, 6s@0.5699999914, 8s@0.5699999967, 8s@0.5699999886, 9s@0.549999945, 9s@0.5, 9s@0.52, 9s@0.53, 11s@0.519999844, 11s@0.51, 15s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.45, 8s@0.45, 8s@0.4595892915, 8s@0.45, 8s@0.45, 8s@0.45, 8s@0.45, 8s@0.45, 9s@0.491087515, 9s@0.509999966, 9s@0.469999998, 9s@0.4599999993 ...


_Updated 2026-10-19 11:37Z_
