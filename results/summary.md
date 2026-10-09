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
- Windows scored: 805; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 60 of 131 = 45.8% (95% range 37.5% to 54.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.15 (balance $7.85 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 60/131 = 45.8%; touch 67/144 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T06:45Z (market 5424777, result down)
Scored: p1 down filled at 67s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.55, 7s@0.5599999686, 7s@0.56, 9s@0.5599999686, 10s@0.549999945, 12s@0.5699999873, 12s@0.5605202572, 12s@0.57, 13s@0.57, 13s@0.5699999886, 16s@0.5899999797, 16s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599997976, 3s@0.4689993314, 3s@0.4710332871, 4s@0.4599997976, 4s@0.46, 4s@0.4602154071, 4s@0.4526724342, 4s@0.46, 6s@0.459999972, 6s@0.46, 6s@0.4599999828, 6s@0.46 ...

### 2026-10-09T09:00Z (market 5426092, result down)
Scored: p1 up filled at 66s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.25, 58s@0.25, 66s@0.24, 73s@0.2199999974, 75s@0.2199999974, 76s@0.22, 84s@0.22, 85s@0.22, 87s@0.2017844444, 88s@0.2099999895, 93s@0.2099999895, 93s@0.2099999895 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5699999886, 1s@0.5699999886, 3s@0.5899998466, 3s@0.57, 3s@0.57, 4s@0.63, 4s@0.63, 4s@0.6, 4s@0.59, 4s@0.5899998466, 4s@0.59, 6s@0.64 ...

### 2026-10-09T10:00Z (market 5426366, result up)
Scored: p1 up filled at 99s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.4599999986, 3s@0.48, 3s@0.49, 3s@0.47, 4s@0.5865697466, 4s@0.58, 4s@0.502604845, 6s@0.5899999145, 7s@0.59, 16s@0.5699999157, 21s@0.5699999886, 24s@0.57 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 3s@0.52, 46s@0.47, 46s@0.46, 48s@0.51, 48s@0.51, 48s@0.5, 48s@0.4879166667, 52s@0.55, 52s@0.55, 52s@0.52, 54s@0.57 ...

### 2026-10-09T10:45Z (market 5427057, result up)
Scored: p1 down filled at 48s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.58, 3s@0.6099999756, 3s@0.6099998597, 3s@0.6144468136, 4s@0.6099998597, 4s@0.6099998597, 4s@0.61, 4s@0.6099999736, 7s@0.59, 9s@0.589999941, 9s@0.59, 10s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.25, 48s@0.24, 55s@0.25, 55s@0.25, 60s@0.25, 61s@0.25, 63s@0.25, 66s@0.25, 67s@0.25, 67s@0.25, 72s@0.2299999983, 72s@0.2299999984 ...

### 2026-10-09T11:45Z (market 5427947, result up)
Scored: p1 down filled at 73s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.48, 3s@0.46, 3s@0.48, 3s@0.48, 3s@0.46, 4s@0.5086584615, 4s@0.52, 4s@0.48, 4s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.52, 4s@0.4699999962, 4s@0.47, 4s@0.5299998463, 4s@0.53, 4s@0.5299998463, 4s@0.5299998463, 4s@0.53, 6s@0.45, 7s@0.45, 9s@0.45 ...


_Updated 2026-10-09 12:29Z_
