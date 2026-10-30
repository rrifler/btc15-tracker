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
- Windows scored: 2828; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.2% of scored windows had a fill (370 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 279/606 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-30T16:00Z (market 6390099, result down)
Scored: p1 up filled at 36s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 36s@0.23595, 36s@0.2299999879, 36s@0.2299999517, 36s@0.22, 39s@0.2099999983, 40s@0.2099999895, 42s@0.21, 48s@0.2099999895, 48s@0.21, 48s@0.21, 54s@0.2099999895, 58s@0.2099999983 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 0s@0.5799998343, 6s@0.61, 7s@0.6099999116, 9s@0.6299999068, 10s@0.629999995, 10s@0.6299998362, 13s@0.63, 18s@0.6599998944, 24s@0.7, 24s@0.6899999345, 28s@0.72 ...

### 2026-10-30T16:30Z (market 6391042, result down)
Scored: p1 up filled at 115s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4599999697, 6s@0.48, 6s@0.48, 6s@0.47, 115s@0.21, 115s@0.21, 115s@0.21, 115s@0.2099999962, 115s@0.2, 120s@0.2199999998, 120s@0.219999978, 130s@0.2099999969 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.539999986, 4s@0.5399999568, 7s@0.6, 15s@0.6, 15s@0.59999988, 18s@0.6, 18s@0.6, 18s@0.6, 18s@0.6, 19s@0.6299999213, 27s@0.6899999586, 27s@0.69 ...

### 2026-10-30T16:45Z (market 6392221, result down)
Scored: p1 up filled at 94s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.4899998383, 6s@0.4899998383, 9s@0.51, 10s@0.5499999601, 10s@0.52, 12s@0.56, 13s@0.5099998215, 15s@0.5, 15s@0.509999987, 18s@0.5299998864, 19s@0.54, 24s@0.5299999399 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.45, 15s@0.5, 18s@0.46, 27s@0.4599999681, 28s@0.469999906, 39s@0.45, 55s@0.5, 66s@0.52, 72s@0.6299999408, 72s@0.6299999937, 72s@0.6, 73s@0.65 ...

### 2026-10-30T18:15Z (market 6395590, result down)
Scored: p1 up filled at 115s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5499999954, 4s@0.5199999792, 9s@0.5199999954, 21s@0.4599999951, 24s@0.4599999669, 45s@0.46, 54s@0.47, 54s@0.4645833333, 115s@0.2399999808, 121s@0.2399999808, 129s@0.219999978, 133s@0.2199999994 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4899999654, 7s@0.49, 9s@0.54, 9s@0.53, 9s@0.5199999843, 9s@0.5229784884, 9s@0.5199999843, 9s@0.5072132724, 9s@0.5, 9s@0.5, 9s@0.4948770833, 10s@0.55 ...


_Updated 2026-10-30 19:18Z_
