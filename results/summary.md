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
- Windows scored: 1286; excluded: 0
- Fill rate: 17.4% of scored windows had a fill (50 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 114/249 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-14T07:00Z (market 5644366, result up)
Scored: p1 up filled at 73s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 2s@0.46, 4s@0.45, 4s@0.45, 4s@0.46, 28s@0.45, 73s@0.2399999808, 73s@0.2399999808, 83s@0.2, 85s@0.2, 86s@0.18, 86s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5799999976, 4s@0.58, 4s@0.5599999642, 4s@0.5599999851, 4s@0.5599999951, 4s@0.5599999309, 4s@0.5599998756, 5s@0.56, 5s@0.56, 7s@0.61, 31s@0.569999772, 32s@0.64 ...

### 2026-10-14T10:30Z (market 5646315, result up)
Scored: p1 down filled at 104s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.4899998383, 5s@0.48, 8s@0.47, 8s@0.47, 16s@0.6099999615, 16s@0.5830747483, 16s@0.6025351536, 16s@0.5999999813, 16s@0.59, 16s@0.51, 16s@0.57, 16s@0.498364701 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5199999894, 4s@0.52, 4s@0.5199999792, 5s@0.52, 11s@0.5299998463, 16s@0.53, 104s@0.23, 106s@0.23, 106s@0.23, 125s@0.22, 128s@0.2199999993, 136s@0.2099999958 ...

### 2026-10-14T11:00Z (market 5646852, result down)
Scored: p1 up filled at 67s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.5299999868, 1s@0.5299999868, 1s@0.53, 2s@0.5299999868, 4s@0.53, 67s@0.2399999808, 70s@0.24, 73s@0.2399999849, 73s@0.2399999808, 77s@0.24, 77s@0.2399999808, 79s@0.2399999959 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4799999983, 4s@0.48, 4s@0.48, 4s@0.4799999616, 5s@0.48, 5s@0.48, 5s@0.48, 7s@0.48, 7s@0.4799999846, 7s@0.48, 7s@0.4799999962, 8s@0.48 ...

### 2026-10-14T11:45Z (market 5647360, result up)
Scored: p1 down filled at 50s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.52, 2s@0.55, 4s@0.5572677596, 5s@0.5899999458, 5s@0.6, 5s@0.5999998929, 11s@0.64, 14s@0.63, 14s@0.62, 23s@0.65, 23s@0.63, 23s@0.63 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 50s@0.2199999974, 52s@0.2099999983, 53s@0.2099999895, 53s@0.22, 53s@0.2099999983, 56s@0.229999994, 59s@0.2, 59s@0.2299999812, 59s@0.2299999517, 61s@0.2, 61s@0.21, 61s@0.22 ...


_Updated 2026-10-14 12:44Z_
