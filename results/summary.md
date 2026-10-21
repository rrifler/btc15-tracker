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
- Windows scored: 1957; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (193 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 187/405 = 46.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-21T06:15Z (market 5962605, result up)
Scored: p1 down filled at 95s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5799999768, 2s@0.54, 2s@0.54, 2s@0.54, 3s@0.5899999145, 3s@0.5852980733, 6s@0.59, 6s@0.59, 8s@0.5899998466, 11s@0.65, 11s@0.65, 12s@0.649999805 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 95s@0.2099999895, 99s@0.2, 104s@0.1899999951, 108s@0.1899999962, 111s@0.1899999962, 134s@0.22, 134s@0.2, 134s@0.22, 134s@0.19, 134s@0.2, 134s@0.19, 134s@0.19 ...

### 2026-10-21T06:30Z (market 5962688, result up)
Scored: p1 down filled at 60s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999886, 6s@0.5654166667, 6s@0.56, 6s@0.56, 8s@0.5799999768, 8s@0.5799999768, 12s@0.58, 14s@0.6199998512, 14s@0.6199999666, 20s@0.6899999821, 20s@0.6899999831, 20s@0.6899999643 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.25, 50s@0.25, 50s@0.25, 56s@0.25, 60s@0.2299999782, 63s@0.2309090909, 65s@0.2399999918, 66s@0.2399999992, 66s@0.2399999808, 71s@0.2399999981, 75s@0.2299999983, 81s@0.219999997 ...

### 2026-10-21T07:30Z (market 5965035, result up)
Scored: p1 down filled at 9s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.71, 2s@0.69, 3s@0.75, 3s@0.73, 3s@0.75, 3s@0.72, 3s@0.7399999855, 3s@0.7199999424, 3s@0.6900413793, 3s@0.7, 5s@0.75, 5s@0.75 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.25, 6s@0.25, 6s@0.25, 8s@0.25, 8s@0.25, 8s@0.25, 8s@0.25, 8s@0.25, 9s@0.2199999974, 9s@0.2199999827, 9s@0.2199999941, 9s@0.25 ...

### 2026-10-21T08:15Z (market 5965694, result up)
Scored: p1 up filled at 119s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 3s@0.4899999584, 95s@0.25, 119s@0.24, 120s@0.25, 122s@0.25, 123s@0.25, 123s@0.25, 134s@0.24, 137s@0.21, 164s@0.2199999962, 165s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.52, 3s@0.5176835437, 3s@0.52, 5s@0.54, 5s@0.54, 5s@0.5199999792, 6s@0.5399999881, 6s@0.5399999881, 6s@0.56, 6s@0.55, 6s@0.5399999881, 6s@0.5399999881 ...

### 2026-10-21T10:15Z (market 5966938, result down)
Scored: p1 up filled at 93s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 83s@0.25, 93s@0.2399999923, 93s@0.2399999923, 95s@0.24, 98s@0.23, 98s@0.24, 98s@0.23, 99s@0.25, 101s@0.25, 105s@0.25, 122s@0.25, 294s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5699999886, 14s@0.5699999886, 23s@0.6199999449, 24s@0.61, 24s@0.61, 24s@0.61, 24s@0.6021593377, 26s@0.61, 26s@0.61, 27s@0.6199999549, 33s@0.6199999529, 35s@0.62 ...


_Updated 2026-10-21 12:45Z_
