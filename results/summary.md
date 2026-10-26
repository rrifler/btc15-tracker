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
- Windows scored: 2464; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (296 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 243/523 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-26T17:30Z (market 6211641, result down)
Scored: p1 up filled at 47s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 47s@0.24, 53s@0.21, 54s@0.2, 57s@0.2299999693, 65s@0.23, 155s@0.45, 168s@0.5099999716, 168s@0.5044472222, 168s@0.5021885417, 168s@0.5, 168s@0.5, 170s@0.5099999758 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.55, 3s@0.57, 3s@0.55, 3s@0.55, 5s@0.64, 5s@0.63, 6s@0.64, 8s@0.64, 12s@0.6299999885, 14s@0.6299998973, 15s@0.629999995, 17s@0.64 ...

### 2026-10-26T19:00Z (market 6219249, result up)
Scored: p1 up filled at 53s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 53s@0.2099999983, 53s@0.2099999929, 54s@0.2, 54s@0.2099999969, 54s@0.2099999919, 56s@0.2, 56s@0.2, 56s@0.2, 62s@0.19, 63s@0.1899999962, 65s@0.19, 69s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5799999882, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.6199998512, 3s@0.64, 3s@0.61, 3s@0.6, 5s@0.6499999717, 5s@0.64 ...


_Updated 2026-10-26 19:44Z_
