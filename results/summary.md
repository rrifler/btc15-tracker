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
- Windows scored: 2512; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.0% of scored windows had a fill (304 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 248/533 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-27T03:45Z (market 6236052, result down)
Scored: p1 up filled at 86s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.472605042, 27s@0.4699999796, 27s@0.469999906, 42s@0.4799998464, 86s@0.22, 86s@0.22, 86s@0.21, 86s@0.21, 89s@0.24, 98s@0.2399999923, 102s@0.17, 102s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.48, 11s@0.5399999129, 26s@0.5399999568, 48s@0.54, 48s@0.55, 59s@0.66, 59s@0.6422924397, 59s@0.63, 60s@0.69, 60s@0.67, 62s@0.6999999296 ...

### 2026-10-27T06:00Z (market 6242191, result down)
Scored: p1 up filled at 104s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 71s@0.25, 72s@0.25, 72s@0.25, 83s@0.25, 93s@0.25, 96s@0.25, 98s@0.25, 104s@0.1699999972, 104s@0.1699999933, 104s@0.15, 104s@0.16, 104s@0.14 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6, 3s@0.59999988, 8s@0.61, 17s@0.6299999898, 23s@0.61, 38s@0.59, 56s@0.6299999181, 60s@0.64, 60s@0.66, 60s@0.65, 60s@0.64, 60s@0.65 ...

### 2026-10-27T06:15Z (market 6242272, result down)
Scored: p1 up filled at 90s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.52, 11s@0.5099999776, 17s@0.5, 23s@0.51, 33s@0.5099999958, 35s@0.5, 39s@0.48, 45s@0.48, 50s@0.5, 56s@0.48, 60s@0.4799999616, 63s@0.4799998464 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 11s@0.49, 15s@0.49, 23s@0.5099999215, 24s@0.5, 27s@0.5499999518, 36s@0.516, 57s@0.53, 66s@0.6599998939, 66s@0.65, 66s@0.645194715, 66s@0.64, 66s@0.57 ...

### 2026-10-27T06:30Z (market 6242327, result down)
Scored: p1 down filled at 113s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5299999883, 3s@0.55, 3s@0.55, 3s@0.54, 3s@0.54, 6s@0.57, 6s@0.5699999886, 8s@0.61, 9s@0.61, 12s@0.6387225549, 14s@0.6499999825, 14s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 21s@0.4538888889, 21s@0.48, 21s@0.47, 113s@0.18, 113s@0.1799999811, 113s@0.18, 114s@0.18, 114s@0.18, 116s@0.19, 131s@0.1799999856, 132s@0.1799999856, 135s@0.2 ...


_Updated 2026-10-27 07:49Z_
