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
- Windows scored: 1073; excluded: 0
- Fill rate: 16.4% of scored windows had a fill (2 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 86/192 = 44.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-12T01:00Z (market 5532337, result up)
Scored: p1 down filled at 93s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.55, 6s@0.62, 6s@0.6199999651, 6s@0.62, 6s@0.6199999859, 6s@0.6199999449, 8s@0.59, 20s@0.5, 21s@0.52, 21s@0.51, 23s@0.52, 23s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 5s@0.455702459, 5s@0.45, 5s@0.46, 5s@0.45, 5s@0.4599997976, 6s@0.45, 6s@0.461686747, 17s@0.4599999687, 17s@0.4599999687, 17s@0.45, 18s@0.5 ...

### 2026-10-12T02:00Z (market 5533089, result up)
Scored: p1 down filled at 23s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6299998362, 5s@0.7, 5s@0.7, 5s@0.68, 18s@0.71, 20s@0.725, 20s@0.71, 21s@0.7699999645, 21s@0.77, 21s@0.7699999606, 21s@0.77, 21s@0.759 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 23s@0.24, 24s@0.2399999992, 24s@0.24, 27s@0.2351282051, 32s@0.25, 32s@0.2402913042, 42s@0.24, 48s@0.2099999983, 50s@0.21, 53s@0.2099999895, 54s@0.2, 63s@0.1799999856 ...

### 2026-10-12T03:00Z (market 5533506, result down)
Scored: p1 up filled at 51s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 51s@0.2399999852, 53s@0.24, 54s@0.22, 56s@0.22, 59s@0.219999978, 71s@0.1799999856, 75s@0.16, 77s@0.1679012342, 78s@0.1720706406, 80s@0.18, 80s@0.2, 81s@0.1899999962 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 6s@0.5099999442, 6s@0.5, 6s@0.5, 8s@0.5, 9s@0.5199999692, 9s@0.5199999692, 9s@0.5099999841, 9s@0.51, 11s@0.53, 11s@0.56, 11s@0.5495833333 ...

### 2026-10-12T04:30Z (market 5535830, result up)
Scored: p1 down filled at 92s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.52, 8s@0.5, 17s@0.6, 17s@0.6, 17s@0.5216666667, 17s@0.57, 17s@0.53, 18s@0.5999999607, 18s@0.6, 21s@0.5899999145, 24s@0.59, 24s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.4980258256, 6s@0.5, 92s@0.2, 95s@0.21, 176s@0.23, 230s@0.21, 230s@0.2099999895, 231s@0.21, 233s@0.21, 242s@0.2199999941, 245s@0.21 ...

### 2026-10-12T05:30Z (market 5538218, result down)
Scored: p1 up filled at 32s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 32s@0.2, 35s@0.16, 35s@0.179, 39s@0.1699999983, 39s@0.1699999983, 45s@0.2, 47s@0.21, 47s@0.2099999895, 47s@0.21, 48s@0.24, 48s@0.24, 48s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.64, 5s@0.64, 5s@0.5599999851, 6s@0.64, 6s@0.64, 6s@0.64, 8s@0.64, 8s@0.64, 8s@0.64, 9s@0.6899999561, 9s@0.69, 9s@0.6899999801 ...


_Updated 2026-10-12 07:30Z_
