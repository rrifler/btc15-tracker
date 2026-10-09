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
- Windows scored: 817; excluded: 0
- Fill rate: 16.4% of scored windows had a fill (0 too small)
- Fills that reached 45c: 61 of 134 = 45.5% (95% range 37.3% to 54.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.45 (balance $7.55 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 61/134 = 45.5%; touch 68/147 = 46.3%. The verdict uses strict.

## Spot-checked windows

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

### 2026-10-09T12:45Z (market 5429031, result down)
Scored: p1 down filled at 100s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.51, 4s@0.5, 4s@0.5109090909, 4s@0.5, 6s@0.5, 13s@0.56, 16s@0.56, 16s@0.5599999686, 16s@0.56, 16s@0.56, 18s@0.56, 18s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5099998215, 9s@0.4899999824, 9s@0.49, 12s@0.45, 12s@0.45, 34s@0.45, 100s@0.22, 100s@0.22, 100s@0.22, 114s@0.2299999971, 120s@0.23, 120s@0.22 ...


_Updated 2026-10-09 15:25Z_
