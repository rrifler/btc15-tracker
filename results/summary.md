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
- Windows scored: 2541; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (311 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 252/541 = 46.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-27T10:45Z (market 6247251, result up)
Scored: p1 down filled at 29s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6, 2s@0.599999976, 2s@0.6, 2s@0.6, 6s@0.6199999449, 8s@0.6366839378, 9s@0.64, 11s@0.63, 12s@0.71, 15s@0.72, 18s@0.71, 18s@0.7 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.2099999895, 32s@0.25, 32s@0.25, 32s@0.25, 32s@0.21, 32s@0.23, 35s@0.25, 36s@0.2199999974, 38s@0.2199999974, 39s@0.25, 39s@0.25, 39s@0.25 ...

### 2026-10-27T11:00Z (market 6247369, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5299998463, 3s@0.53, 6s@0.58, 6s@0.58, 9s@0.5799999936, 9s@0.58, 12s@0.58, 12s@0.58, 15s@0.58, 18s@0.59, 18s@0.5899999725, 20s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799999616, 114s@0.2099999983, 120s@0.2199999974, 120s@0.2, 120s@0.2, 122s@0.2199999974, 123s@0.2199999933, 146s@0.16, 146s@0.16, 158s@0.1335365854, 158s@0.14, 158s@0.15 ...

### 2026-10-27T11:15Z (market 6247548, result down)
Scored: p1 up filled at 63s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 63s@0.24, 63s@0.23, 66s@0.2399999808, 71s@0.19, 77s@0.2, 78s@0.2, 98s@0.2, 98s@0.2, 108s@0.2, 122s@0.19, 122s@0.19, 123s@0.1957065111 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.57, 5s@0.62, 5s@0.62, 5s@0.6099999451, 5s@0.57, 6s@0.64, 6s@0.6199999778, 9s@0.64, 12s@0.64, 15s@0.64, 17s@0.64, 18s@0.6599997888 ...

### 2026-10-27T12:15Z (market 6248576, result up)
Scored: p1 down filled at 30s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5672849795, 2s@0.56, 3s@0.6099999662, 3s@0.57, 5s@0.61, 5s@0.6099999831, 8s@0.65, 8s@0.66, 14s@0.71, 14s@0.7, 17s@0.72, 20s@0.73 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 30s@0.22, 35s@0.2, 41s@0.1899999918, 41s@0.1899999947, 41s@0.19, 42s@0.19, 42s@0.19, 44s@0.2, 47s@0.2, 47s@0.2, 47s@0.2, 48s@0.2 ...

### 2026-10-27T14:00Z (market 6252426, result up)
Scored: p1 up filled at 84s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.533130122, 3s@0.5299998463, 6s@0.5027368421, 27s@0.4599999387, 84s@0.24, 84s@0.2399999868, 86s@0.25, 89s@0.239999999, 93s@0.25, 96s@0.22, 99s@0.2199999941, 99s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.505, 5s@0.48, 6s@0.56, 8s@0.59, 17s@0.5299999607, 17s@0.53, 18s@0.5799999574, 20s@0.59, 21s@0.5599999328, 27s@0.5299999763, 27s@0.5399999568, 30s@0.55 ...


_Updated 2026-10-27 14:51Z_
