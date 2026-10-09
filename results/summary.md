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
- Windows scored: 837; excluded: 0
- Fill rate: 17.0% of scored windows had a fill (0 too small)
- Fills that reached 45c: 68 of 142 = 47.9% (95% range 39.8% to 56.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.30 (balance $8.70 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 68/142 = 47.9%; touch 75/155 = 48.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T14:15Z (market 5430393, result up)
Scored: p1 down filled at 78s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.53, 4s@0.53, 10s@0.55, 12s@0.5899999634, 12s@0.5899999634, 12s@0.5899999634, 13s@0.5899999634, 13s@0.5899999634, 13s@0.5899999827, 19s@0.59, 30s@0.62, 31s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.45, 9s@0.4599999563, 78s@0.23, 78s@0.23, 79s@0.23, 81s@0.22, 94s@0.24, 94s@0.23999997, 94s@0.24, 100s@0.25, 108s@0.23, 109s@0.23 ...

### 2026-10-09T15:30Z (market 5432152, result up)
Scored: p1 down filled at 97s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 40s@0.51, 45s@0.5699999841, 46s@0.57, 46s@0.57, 52s@0.59999988, 57s@0.62, 57s@0.6199998946, 57s@0.6499999602, 58s@0.65, 60s@0.6499999932, 60s@0.6699999807, 60s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.555, 3s@0.57, 3s@0.57, 16s@0.53, 25s@0.5599999328, 28s@0.559999776, 28s@0.56, 28s@0.56, 33s@0.53, 34s@0.5299998463, 40s@0.47, 40s@0.46 ...

### 2026-10-09T16:00Z (market 5432939, result up)
Scored: p1 up filled at 63s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 63s@0.22, 63s@0.21, 65s@0.22, 65s@0.22, 66s@0.22, 66s@0.22, 66s@0.22, 68s@0.22, 69s@0.23, 69s@0.23, 69s@0.22, 71s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.51, 5s@0.65, 5s@0.65, 9s@0.6599999859, 11s@0.6599999958, 12s@0.6599999534, 17s@0.6899999606, 30s@0.72, 30s@0.69, 32s@0.7199999844, 32s@0.7199999942, 33s@0.7099999949 ...

### 2026-10-09T16:15Z (market 5432984, result down)
Scored: p1 down filled at 89s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5099999516, 4s@0.559999776, 4s@0.56, 9s@0.6, 13s@0.61, 15s@0.57, 15s@0.6099999985, 16s@0.5799999768, 16s@0.58, 24s@0.6159573782, 28s@0.64, 37s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998683, 4s@0.45, 6s@0.45, 89s@0.2399999808, 90s@0.25, 90s@0.24, 104s@0.24, 108s@0.23, 147s@0.25, 147s@0.2442996743, 228s@0.45, 239s@0.47 ...

### 2026-10-09T16:45Z (market 5433727, result up)
Scored: p1 down filled at 76s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5699999436, 4s@0.56, 4s@0.5599999851, 4s@0.5599999517, 4s@0.5699999886, 4s@0.5699999886, 7s@0.56, 8s@0.56, 11s@0.5699999886, 14s@0.5699999731, 26s@0.58, 28s@0.6199998512 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.45, 71s@0.25, 76s@0.21, 76s@0.2, 76s@0.2099999895, 77s@0.2233333333, 80s@0.25, 85s@0.2299999782, 91s@0.2099999838, 92s@0.18, 100s@0.2, 103s@0.25 ...


_Updated 2026-10-09 20:23Z_
