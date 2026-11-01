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
- Windows scored: 3019; excluded: 14 (trades_truncated: 3, no_trades: 2, market_not_found: 9)
- Fill rate: 19.2% of scored windows had a fill (405 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 292/647 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-11-01T20:00Z (market 6492464, result down)
Scored: p1 down filled at 109s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.54, 4s@0.55, 4s@0.5499999918, 4s@0.549999945, 4s@0.54, 4s@0.52, 4s@0.52, 4s@0.52, 4s@0.52, 6s@0.6699999911, 6s@0.64, 7s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.45, 109s@0.23, 114s@0.25, 195s@0.45, 199s@0.5, 207s@0.55, 207s@0.6045535628, 208s@0.6199998512, 208s@0.6181062875, 210s@0.6099999956, 214s@0.61, 214s@0.6 ...

### 2026-11-01T23:00Z (market 6499528, result up)
Scored: p1 down filled at 40s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 3s@0.45, 3s@0.5, 3s@0.48, 4s@0.56, 4s@0.5599999956, 4s@0.5599999956, 4s@0.5599999869, 4s@0.56, 4s@0.56, 4s@0.56, 4s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399998231, 3s@0.539999991, 4s@0.45, 4s@0.45, 13s@0.4675, 13s@0.45, 15s@0.47, 40s@0.24, 42s@0.25, 42s@0.24, 42s@0.2484375, 48s@0.22 ...


_Updated 2026-11-01 23:32Z_
