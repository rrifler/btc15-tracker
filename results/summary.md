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
- Windows scored: 3044; excluded: 14 (trades_truncated: 3, no_trades: 2, market_not_found: 9)
- Fill rate: 19.1% of scored windows had a fill (408 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 295/651 = 45.3%. The verdict uses strict.

## Spot-checked windows

### 2026-11-02T00:30Z (market 6502435, result down)
Scored: p1 up filled at 93s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.5, 4s@0.57, 6s@0.5199999406, 10s@0.5099999939, 10s@0.5099999984, 12s@0.5099999776, 12s@0.5099999776, 93s@0.2299999517, 96s@0.2364415546, 105s@0.24, 184s@0.219999978 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4661904762, 6s@0.45, 13s@0.5, 13s@0.5, 15s@0.52, 15s@0.5, 18s@0.52, 21s@0.53, 21s@0.53, 24s@0.55, 25s@0.6199999792, 34s@0.6499999986 ...

### 2026-11-02T01:15Z (market 6503155, result up)
Scored: p1 up filled at 94s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 94s@0.22, 99s@0.21, 99s@0.2099999895, 105s@0.2, 111s@0.1899999998, 115s@0.1799999981, 117s@0.1799999856, 123s@0.18, 123s@0.18, 123s@0.18, 123s@0.18, 127s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5099999773, 3s@0.450504581, 4s@0.4571022727, 4s@0.45, 6s@0.6590909091, 6s@0.63, 6s@0.6, 6s@0.5872727273, 6s@0.5529707039, 7s@0.67, 7s@0.65, 7s@0.67 ...

### 2026-11-02T03:30Z (market 6504994, result down)
Scored: p1 up filled at 69s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 6s@0.4799999846, 9s@0.47, 10s@0.4699998298, 10s@0.4699998298, 12s@0.469999906, 12s@0.4699999761, 12s@0.469999906, 13s@0.4699999944, 13s@0.4699999944, 13s@0.4699999944, 15s@0.4699999878 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999883, 3s@0.5359801462, 6s@0.53, 6s@0.5299999868, 7s@0.53, 7s@0.5299999251, 9s@0.55, 9s@0.5299999512, 9s@0.5362893082, 9s@0.5299999057, 9s@0.5299999057, 9s@0.53 ...


_Updated 2026-11-02 05:54Z_
