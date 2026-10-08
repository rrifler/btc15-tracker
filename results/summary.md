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
- Windows scored: 753; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 54 of 123 = 43.9% (95% range 35.4% to 52.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.85 (balance $7.15 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 54/123 = 43.9%; touch 60/133 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-08T18:15Z (market 5410449, result up)
Scored: p1 down filled at 41s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.68, 3s@0.6799998912, 3s@0.64934374, 5s@0.69, 5s@0.69, 5s@0.6899999433, 6s@0.69, 8s@0.69, 17s@0.7, 17s@0.7, 17s@0.7, 17s@0.699999993 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 35s@0.25, 41s@0.219999978, 50s@0.21, 56s@0.17, 57s@0.17, 59s@0.16, 65s@0.13, 68s@0.1399999832, 71s@0.15, 71s@0.15, 71s@0.14, 71s@0.14 ...

### 2026-10-08T21:00Z (market 5414728, result down)
Scored: p1 up filled at 83s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 83s@0.2399999992, 87s@0.24, 87s@0.24, 89s@0.24, 90s@0.25, 90s@0.25, 90s@0.25, 108s@0.24, 108s@0.24, 110s@0.24, 110s@0.24, 110s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.55, 3s@0.5899999954, 5s@0.59, 5s@0.59, 8s@0.59, 8s@0.6, 8s@0.599999994, 11s@0.6, 11s@0.599999976, 14s@0.59999994, 14s@0.6, 15s@0.629999995 ...

### 2026-10-08T21:45Z (market 5416650, result down)
Scored: p1 up filled at 65s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.48, 3s@0.48, 5s@0.5, 5s@0.49, 6s@0.51, 6s@0.51, 6s@0.51, 8s@0.53, 14s@0.478339095, 14s@0.46, 65s@0.25, 65s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 6s@0.5, 9s@0.5899999634, 9s@0.5899999762, 9s@0.5016666667, 9s@0.5839256405, 9s@0.5799999882, 9s@0.57, 11s@0.59, 11s@0.5899999712, 11s@0.59, 12s@0.59 ...


_Updated 2026-10-08 23:23Z_
