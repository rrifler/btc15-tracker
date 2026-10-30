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
- Windows scored: 2807; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.2% of scored windows had a fill (366 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 279/601 = 46.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-30T07:30Z (market 6381495, result down)
Scored: p1 down filled at 42s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6099997897, 3s@0.6099997897, 3s@0.6099999775, 3s@0.58, 3s@0.6099999053, 3s@0.58, 7s@0.6699999964, 15s@0.7199999844, 15s@0.69, 30s@0.75, 30s@0.7408536541, 30s@0.72 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 31s@0.25, 39s@0.25, 42s@0.2399999981, 43s@0.2399999726, 45s@0.2399999981, 60s@0.22, 69s@0.229999994, 72s@0.2299999975, 100s@0.2199999974, 102s@0.2, 102s@0.2, 102s@0.2 ...

### 2026-10-30T07:45Z (market 6381636, result up)
Scored: p1 down filled at 67s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.45, 6s@0.4899998102, 6s@0.4799999846, 6s@0.48, 6s@0.48, 6s@0.48, 7s@0.48, 7s@0.4893692157, 9s@0.4599999951, 15s@0.45, 18s@0.4899999824, 21s@0.51 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.57, 4s@0.56, 6s@0.5099998215, 7s@0.5299999507, 7s@0.52, 7s@0.5199999792, 7s@0.4899999584, 7s@0.4899998383, 9s@0.529999982, 9s@0.535, 10s@0.5799999448, 10s@0.57 ...

### 2026-10-30T08:15Z (market 6382019, result down)
Scored: p1 down filled at 39s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.53, 6s@0.5313833333, 22s@0.6, 27s@0.67, 27s@0.7, 31s@0.74, 31s@0.74, 31s@0.7283333333, 34s@0.7399999688, 34s@0.74, 36s@0.74, 37s@0.7799999769 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.48, 7s@0.4599999885, 39s@0.219999978, 40s@0.22, 42s@0.2, 43s@0.2, 46s@0.25, 46s@0.25, 148s@0.45, 151s@0.4799999616, 153s@0.48, 157s@0.4799998464 ...

### 2026-10-30T10:30Z (market 6383165, result up)
Scored: p1 down filled at 105s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.52, 3s@0.53, 3s@0.5118023124, 3s@0.51, 4s@0.53, 4s@0.5299999868, 4s@0.53, 7s@0.480392146, 7s@0.47, 7s@0.4699999796, 7s@0.4699999944, 7s@0.4899999944 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 4s@0.4799999737, 6s@0.48, 6s@0.48, 7s@0.52, 7s@0.5199999843, 7s@0.52, 7s@0.52, 7s@0.5, 7s@0.5099999966, 7s@0.5, 9s@0.54 ...

### 2026-10-30T10:45Z (market 6383369, result up)
Scored: p1 up filled at 105s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.515, 7s@0.5372136057, 21s@0.4899998383, 28s@0.46, 28s@0.4599999387, 36s@0.5, 37s@0.5, 105s@0.23, 108s@0.2399999852, 109s@0.2299999891, 117s@0.23, 121s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.47, 16s@0.49, 16s@0.4899998383, 22s@0.53, 39s@0.524752469, 42s@0.57, 49s@0.599999988, 60s@0.63, 63s@0.64, 63s@0.64, 84s@0.6699999839, 84s@0.65 ...


_Updated 2026-10-30 14:04Z_
