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
- Windows scored: 3003; excluded: 15 (trades_truncated: 3, no_trades: 2, market_not_found: 9, result_missing: 1)
- Fill rate: 19.2% of scored windows had a fill (403 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 290/644 = 45.0%. The verdict uses strict.

## Spot-checked windows

### 2026-11-01T14:00Z (market 6465338, result up)
Scored: p1 up filled at 96s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5599998611, 3s@0.5599999382, 7s@0.5799999768, 9s@0.5799999768, 12s@0.5099999716, 19s@0.469999906, 19s@0.469999906, 22s@0.4899998383, 75s@0.25, 96s@0.2, 96s@0.21, 99s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.45, 10s@0.5, 10s@0.4899999884, 12s@0.5, 12s@0.5, 12s@0.5, 12s@0.5, 18s@0.5399999568, 18s@0.54, 21s@0.536746966, 25s@0.58, 25s@0.58 ...

### 2026-11-01T15:30Z (market 6474876, result down)
Scored: p1 up filled at 81s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 48s@0.25, 81s@0.2245470744, 81s@0.24, 81s@0.24, 81s@0.2299999748, 81s@0.2339086247, 81s@0.24, 81s@0.25, 82s@0.25, 82s@0.25, 82s@0.2400727364, 82s@0.219999999 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5899999546, 3s@0.5599999067, 3s@0.57, 3s@0.57, 3s@0.57, 3s@0.57, 4s@0.5899999084, 4s@0.5899999084, 4s@0.5899998254, 4s@0.5899999084, 6s@0.5899999458, 6s@0.5899999084 ...

### 2026-11-01T16:15Z (market 6477034, result up)
Scored: p1 down filled at 66s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6694455852, 0s@0.6599999991, 1s@0.6724390927, 3s@0.64, 4s@0.63, 6s@0.64, 7s@0.6270642011, 7s@0.64, 10s@0.6699999698, 10s@0.63, 12s@0.6799996464, 12s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 66s@0.248125, 67s@0.24, 81s@0.2465886635, 93s@0.25, 108s@0.25, 148s@0.22, 148s@0.2099999895, 150s@0.18, 151s@0.18, 151s@0.17, 153s@0.17, 154s@0.1399999989 ...


_Updated 2026-11-01 19:36Z_
