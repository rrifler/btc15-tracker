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
- Windows scored: 825; excluded: 0
- Fill rate: 16.7% of scored windows had a fill (0 too small)
- Fills that reached 45c: 64 of 138 = 46.4% (95% range 38.3% to 54.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.10 (balance $7.90 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 64/138 = 46.4%; touch 71/151 = 47.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T11:45Z (market 5427947, result up)
Scored: p1 down filled at 73s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.46, 3s@0.48, 3s@0.48, 3s@0.46, 4s@0.5086584615, 4s@0.52, 4s@0.48, 4s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.52, 4s@0.4699999962, 4s@0.47, 4s@0.5299998463, 4s@0.53, 4s@0.5299998463, 4s@0.5299998463, 4s@0.53, 6s@0.45, 7s@0.45, 9s@0.45 ...

### 2026-10-09T12:45Z (market 5429031, result down)
Scored: p1 down filled at 100s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.51, 4s@0.5, 4s@0.5109090909, 4s@0.5, 6s@0.5, 13s@0.56, 16s@0.56, 16s@0.5599999686, 16s@0.56, 16s@0.56, 18s@0.56, 18s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5099998215, 9s@0.4899999824, 9s@0.49, 12s@0.45, 12s@0.45, 34s@0.45, 100s@0.22, 100s@0.22, 100s@0.22, 114s@0.2299999971, 120s@0.23, 120s@0.22 ...

### 2026-10-09T13:00Z (market 5429421, result up)
Scored: p1 down filled at 48s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.559999776, 6s@0.5799999383, 7s@0.58, 13s@0.57, 15s@0.59, 19s@0.6, 24s@0.61, 25s@0.61, 28s@0.63, 31s@0.64, 33s@0.6599999534, 33s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.24, 48s@0.2399999923, 49s@0.25, 49s@0.25, 54s@0.25, 54s@0.25, 54s@0.25, 360s@0.219999978, 363s@0.2248367329, 364s@0.2446761727, 369s@0.25, 375s@0.23 ...

### 2026-10-09T14:15Z (market 5430393, result up)
Scored: p1 down filled at 78s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.53, 4s@0.53, 10s@0.55, 12s@0.5899999634, 12s@0.5899999634, 12s@0.5899999634, 13s@0.5899999634, 13s@0.5899999634, 13s@0.5899999827, 19s@0.59, 30s@0.62, 31s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.45, 9s@0.4599999563, 78s@0.23, 78s@0.23, 79s@0.23, 81s@0.22, 94s@0.24, 94s@0.23999997, 94s@0.24, 100s@0.25, 108s@0.23, 109s@0.23 ...

### 2026-10-09T15:30Z (market 5432152, result up)
Scored: p1 down filled at 97s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 40s@0.51, 45s@0.5699999841, 46s@0.57, 46s@0.57, 52s@0.59999988, 57s@0.62, 57s@0.6199998946, 57s@0.6499999602, 58s@0.65, 60s@0.6499999932, 60s@0.6699999807, 60s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.555, 3s@0.57, 3s@0.57, 16s@0.53, 25s@0.5599999328, 28s@0.559999776, 28s@0.56, 28s@0.56, 33s@0.53, 34s@0.5299998463, 40s@0.47, 40s@0.46 ...


_Updated 2026-10-09 17:23Z_
