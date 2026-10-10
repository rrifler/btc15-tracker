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
- Windows scored: 921; excluded: 0
- Fill rate: 16.4% of scored windows had a fill (0 too small)
- Fills that reached 45c: 70 of 151 = 46.4% (95% range 38.6% to 54.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.65 (balance $7.35 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 70/151 = 46.4%; touch 77/164 = 47.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-10T13:00Z (market 5456384, result up)
Scored: p1 down filled at 112s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5999999897, 4s@0.5899999954, 4s@0.5899999894, 4s@0.6076923077, 7s@0.629999995, 9s@0.63, 9s@0.63, 13s@0.62, 15s@0.6199999899, 19s@0.6199999471, 37s@0.6199999651, 45s@0.6541230769 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.47, 112s@0.1899999896, 112s@0.18, 112s@0.189999978, 114s@0.1951349275, 114s@0.2, 114s@0.1799999988, 114s@0.1875324666, 114s@0.19, 114s@0.18, 114s@0.1799999856, 114s@0.2 ...

### 2026-10-10T13:45Z (market 5457249, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5899998466, 3s@0.55, 4s@0.6, 6s@0.61, 7s@0.6099999756, 9s@0.6, 9s@0.61, 10s@0.599999976, 13s@0.6099998597, 15s@0.6099999766, 18s@0.6099998597, 19s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 3s@0.47, 3s@0.4606882128, 3s@0.46, 114s@0.24, 115s@0.24, 117s@0.24, 117s@0.24, 121s@0.2399999808, 127s@0.21, 145s@0.2199999961, 147s@0.219999978 ...

### 2026-10-10T14:30Z (market 5458054, result up)
Scored: p1 down filled at 6s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.629999937, 0s@0.62, 0s@0.61, 0s@0.6, 0s@0.5941747457, 0s@0.58, 0s@0.5799999673, 0s@0.57, 1s@0.63, 1s@0.6099999322, 3s@0.70246, 3s@0.649585992 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.25, 6s@0.219999978, 6s@0.2299999998, 6s@0.2299999961, 7s@0.22, 7s@0.2199999983, 19s@0.49, 19s@0.45, 19s@0.4535205184, 22s@0.469999998, 24s@0.47, 30s@0.5073003874 ...

### 2026-10-10T15:30Z (market 5458838, result up)
Scored: p1 down filled at 103s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999776, 4s@0.48, 12s@0.5, 16s@0.5199999844, 18s@0.5314646753, 21s@0.55, 28s@0.54, 28s@0.56, 30s@0.6425, 30s@0.62, 34s@0.65, 34s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 3s@0.5, 3s@0.5, 27s@0.4599999034, 28s@0.47, 103s@0.1699999983, 105s@0.17, 108s@0.1635848983, 108s@0.16, 109s@0.16, 114s@0.17, 117s@0.1699999986 ...


_Updated 2026-10-10 17:21Z_
