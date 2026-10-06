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

- Verdict: **NOT ENOUGH DATA**
- Windows scored: 501; excluded: 0
- Fill rate: 17.6% of scored windows had a fill (0 too small)
- Fills that reached 45c: 37 of 88 = 42.0% (95% range 32.3% to 52.5%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-11.75 (balance $8.25 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 37/88 = 42.0%; touch 42/95 = 44.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-06T02:45Z (market 5311273, result down)
Scored: p1 up filled at 58s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 58s@0.24, 58s@0.25, 60s@0.24, 61s@0.24, 66s@0.17, 66s@0.19, 67s@0.1899999962, 69s@0.18, 76s@0.2299999517, 78s@0.219999978, 79s@0.219999978, 82s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.58, 0s@0.57, 3s@0.6, 4s@0.6169154008, 6s@0.64, 6s@0.6365387569, 6s@0.6299999181, 6s@0.629999937, 7s@0.64, 7s@0.65, 9s@0.6499999515, 9s@0.6499999861 ...

### 2026-10-06T03:30Z (market 5311723, result down)
Scored: p1 up filled at 42s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.4882, 3s@0.4765325936, 3s@0.4731267433, 4s@0.4699999962, 4s@0.4566210046, 4s@0.4677713394, 4s@0.47, 6s@0.48, 6s@0.48, 6s@0.4799998464, 6s@0.48, 6s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 3s@0.53, 4s@0.5568199811, 4s@0.5399999966, 7s@0.5322644928, 7s@0.5599999728, 7s@0.5299999025, 7s@0.5299999868, 9s@0.5599999772, 9s@0.5599999825, 9s@0.5599999843, 13s@0.5602327757 ...

### 2026-10-06T05:45Z (market 5315521, result down)
Scored: p1 up filled at 82s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.49, 6s@0.469999906, 6s@0.469999906, 9s@0.49, 82s@0.22, 82s@0.22, 82s@0.22, 82s@0.2025687392, 82s@0.22, 84s@0.25, 88s@0.25, 94s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 4s@0.51, 4s@0.5099998215, 6s@0.5399999568, 16s@0.55, 16s@0.51, 18s@0.57, 21s@0.5899998466, 24s@0.56, 24s@0.559999776, 25s@0.61, 25s@0.6 ...

### 2026-10-06T06:00Z (market 5316494, result down)
Scored: p1 up filled at 58s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5099998215, 6s@0.4599997976, 6s@0.4899998383, 7s@0.46, 58s@0.24, 61s@0.24, 63s@0.2099999983, 64s@0.19, 64s@0.2, 66s@0.18, 66s@0.18, 66s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 4s@0.5, 4s@0.5, 6s@0.5, 6s@0.51, 6s@0.5, 6s@0.5, 6s@0.5, 10s@0.559999776, 16s@0.56, 22s@0.6, 22s@0.61 ...

### 2026-10-06T06:45Z (market 5316771, result down)
Scored: p1 down filled at 106s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.59, 1s@0.580625, 3s@0.606573031, 4s@0.6199998512, 4s@0.617529819, 9s@0.64, 9s@0.6361538462, 9s@0.6199999958, 18s@0.5799999768, 24s@0.6099998597, 40s@0.6099998597, 57s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 103s@0.25, 106s@0.2399999923, 109s@0.2399999912, 115s@0.239999962, 120s@0.2312781641, 121s@0.2399999808, 138s@0.2399999923, 157s@0.2399999959, 159s@0.2399999808, 160s@0.24, 166s@0.24, 175s@0.24 ...


_Updated 2026-10-06 08:26Z_
