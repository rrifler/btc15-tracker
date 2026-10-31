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
- Windows scored: 2894; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.3% of scored windows had a fill (384 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 286/622 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-31T06:00Z (market 6409019, result up)
Scored: p1 down filled at 118s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.5899999933, 7s@0.5899999878, 9s@0.6699999939, 9s@0.64, 9s@0.63, 10s@0.6699999729, 10s@0.6699999988, 12s@0.6199999681, 15s@0.5799998119, 30s@0.5099999913, 39s@0.54, 43s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 4s@0.4799998464, 21s@0.5, 25s@0.5, 25s@0.49, 37s@0.4699999944, 118s@0.2, 118s@0.2, 120s@0.2, 123s@0.2, 127s@0.15, 132s@0.14 ...

### 2026-10-31T08:00Z (market 6411839, result up)
Scored: p1 down filled at 109s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6, 3s@0.5699999214, 3s@0.5699999214, 3s@0.5699999214, 3s@0.5699999214, 3s@0.5699999801, 3s@0.5699999214, 3s@0.5699999067, 3s@0.5699999525, 3s@0.5699999947, 6s@0.5601723365, 9s@0.5699999886 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 85s@0.25, 109s@0.24, 109s@0.24, 123s@0.45, 124s@0.49, 124s@0.544549045, 126s@0.54, 132s@0.57, 133s@0.55, 135s@0.56, 142s@0.56 ...

### 2026-10-31T09:00Z (market 6413381, result up)
Scored: p1 down filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5133333333, 7s@0.6, 7s@0.5999999877, 12s@0.6, 12s@0.59999988, 13s@0.6099998597, 16s@0.6199998422, 18s@0.63, 18s@0.64, 18s@0.64, 18s@0.64, 24s@0.6505667803 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 54s@0.25, 63s@0.2299999967, 63s@0.2299999517, 69s@0.2299999966, 70s@0.2399999761, 90s@0.2, 90s@0.2, 91s@0.2, 94s@0.2099999895, 114s@0.24, 114s@0.24, 114s@0.2 ...

### 2026-10-31T11:15Z (market 6416854, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5172463768, 4s@0.53, 6s@0.53, 13s@0.5335135135, 13s@0.5199999843, 13s@0.5299999998, 13s@0.52, 13s@0.5199999843, 15s@0.53, 39s@0.5299999868, 55s@0.5299999868, 58s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4799999939, 10s@0.4899999781, 10s@0.4899999183, 27s@0.48, 28s@0.48, 37s@0.47, 45s@0.49, 49s@0.4799999687, 49s@0.4799999875, 112s@0.25, 114s@0.2199999909, 117s@0.2199999921 ...


_Updated 2026-10-31 12:16Z_
