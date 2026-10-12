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
- Windows scored: 1053; excluded: 0
- Fill rate: 16.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 77 of 171 = 45.0% (95% range 37.8% to 52.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-14.50 (balance $5.50 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/171 = 45.0%; touch 85/185 = 45.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-11T21:15Z (market 5522576, result down)
Scored: p1 up filled at 8s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.45, 4s@0.469999906, 4s@0.47, 4s@0.469999906, 4s@0.469999906, 8s@0.22, 8s@0.2199999844, 8s@0.22, 8s@0.2199999976, 8s@0.22, 8s@0.2199999974 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4913232007, 2s@0.549999945, 2s@0.49, 2s@0.4899999944, 4s@0.62, 4s@0.64, 4s@0.63, 4s@0.6299999496, 4s@0.6299999592, 4s@0.64, 5s@0.7, 5s@0.71 ...

### 2026-10-11T21:45Z (market 5522846, result down)
Scored: p1 up filled at 53s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 53s@0.2399999923, 55s@0.25, 71s@0.2299999782, 76s@0.2, 77s@0.18, 77s@0.2, 79s@0.2199999895, 79s@0.23, 79s@0.22, 79s@0.2075, 80s@0.21, 80s@0.2099999962 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4899999944, 2s@0.47, 5s@0.51, 5s@0.51, 5s@0.52, 5s@0.4920661157, 7s@0.5699999886, 7s@0.5668306011, 7s@0.5599999851, 8s@0.6, 13s@0.59999988, 16s@0.58 ...

### 2026-10-11T23:00Z (market 5528560, result up)
Scored: p1 down filled at 93s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.51, 6s@0.535, 6s@0.57, 29s@0.509999833, 36s@0.51, 38s@0.5299998463, 39s@0.56, 39s@0.56, 39s@0.5599999851, 39s@0.559999962, 39s@0.5495833333, 42s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5099997829, 9s@0.4699999888, 9s@0.4699999796, 27s@0.48375, 30s@0.4899999969, 93s@0.2099999758, 93s@0.2, 95s@0.2, 95s@0.2, 95s@0.2, 96s@0.2, 98s@0.19 ...

### 2026-10-12T01:00Z (market 5532337, result up)
Scored: p1 down filled at 93s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.55, 6s@0.62, 6s@0.6199999651, 6s@0.62, 6s@0.6199999859, 6s@0.6199999449, 8s@0.59, 20s@0.5, 21s@0.52, 21s@0.51, 23s@0.52, 23s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 5s@0.455702459, 5s@0.45, 5s@0.46, 5s@0.45, 5s@0.4599997976, 6s@0.45, 6s@0.461686747, 17s@0.4599999687, 17s@0.4599999687, 17s@0.45, 18s@0.5 ...

### 2026-10-12T02:00Z (market 5533089, result up)
Scored: p1 down filled at 23s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6299998362, 5s@0.7, 5s@0.7, 5s@0.68, 18s@0.71, 20s@0.725, 20s@0.71, 21s@0.7699999645, 21s@0.77, 21s@0.7699999606, 21s@0.77, 21s@0.759 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 23s@0.24, 24s@0.2399999992, 24s@0.24, 27s@0.2351282051, 32s@0.25, 32s@0.2402913042, 42s@0.24, 48s@0.2099999983, 50s@0.21, 53s@0.2099999895, 54s@0.2, 63s@0.1799999856 ...


_Updated 2026-10-12 02:26Z_
