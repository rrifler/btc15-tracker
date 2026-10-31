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
- Windows scored: 2931; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.2% of scored windows had a fill (389 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 287/628 = 45.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-31T17:45Z (market 6428225, result up)
Scored: p1 down filled at 72s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.47, 4s@0.4699999612, 33s@0.5, 37s@0.49, 60s@0.51, 60s@0.6199998512, 60s@0.5, 60s@0.53, 60s@0.52, 60s@0.51, 60s@0.5, 60s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5399999568, 6s@0.53, 7s@0.53, 7s@0.5299999868, 9s@0.53, 10s@0.5299998193, 28s@0.52, 30s@0.5099999853, 34s@0.51, 36s@0.51, 40s@0.5099999853, 49s@0.51 ...

### 2026-10-31T19:45Z (market 6433519, result down)
Scored: p1 up filled at 46s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.5199998823, 33s@0.48, 46s@0.2, 51s@0.1899999929, 54s@0.1699999983, 55s@0.1699999995, 55s@0.1699999983, 57s@0.17, 57s@0.1799999794, 61s@0.1705380052, 85s@0.177570838, 85s@0.1799999856 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4699999612, 6s@0.47, 7s@0.469999998, 9s@0.4772234233, 10s@0.4899998505, 12s@0.4699999944, 18s@0.48, 18s@0.469999998, 19s@0.4899999743, 25s@0.4899999944, 25s@0.4899999984, 25s@0.4899999584 ...

### 2026-10-31T20:00Z (market 6434132, result up)
Scored: p1 down filled at 61s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6199999971, 3s@0.57, 3s@0.57, 3s@0.5669029187, 3s@0.5599999067, 4s@0.659999909, 4s@0.64, 4s@0.6012048193, 4s@0.5799998711, 4s@0.6199999145, 4s@0.5799999156, 4s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.45, 60s@0.25, 61s@0.24, 61s@0.24, 61s@0.24, 61s@0.24, 63s@0.24, 63s@0.24, 64s@0.23, 66s@0.2399999971, 70s@0.24, 72s@0.2099999764 ...

### 2026-10-31T21:00Z (market 6435719, result down)
Scored: p1 up filled at 100s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999949, 3s@0.5099999516, 7s@0.55, 7s@0.55, 7s@0.55, 9s@0.57, 9s@0.56, 9s@0.5586821705, 10s@0.5699999886, 21s@0.56, 22s@0.57, 24s@0.57 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.51, 3s@0.51, 28s@0.46, 36s@0.47, 58s@0.46, 60s@0.4899999412, 64s@0.5225351885, 66s@0.5299998172, 69s@0.5, 72s@0.5, 73s@0.5199999792 ...


_Updated 2026-10-31 21:27Z_
