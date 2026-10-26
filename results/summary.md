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
- Windows scored: 2460; excluded: 3 (trades_truncated: 2, result_missing: 1)
- Fill rate: 19.1% of scored windows had a fill (295 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 242/522 = 46.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-26T13:00Z (market 6192268, result down)
Scored: p1 up filled at 90s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998383, 3s@0.49, 8s@0.5, 8s@0.4899998383, 11s@0.48, 12s@0.47, 14s@0.45, 17s@0.4599999472, 18s@0.4932328454, 21s@0.479999993, 87s@0.25, 89s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.48, 0s@0.48, 0s@0.48, 2s@0.48, 3s@0.5, 3s@0.49, 23s@0.6099999848, 23s@0.5799999768, 23s@0.6, 26s@0.61, 29s@0.64, 30s@0.63 ...

### 2026-10-26T17:30Z (market 6211641, result down)
Scored: p1 up filled at 47s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 47s@0.24, 53s@0.21, 54s@0.2, 57s@0.2299999693, 65s@0.23, 155s@0.45, 168s@0.5099999716, 168s@0.5044472222, 168s@0.5021885417, 168s@0.5, 168s@0.5, 170s@0.5099999758 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.55, 3s@0.57, 3s@0.55, 3s@0.55, 5s@0.64, 5s@0.63, 6s@0.64, 8s@0.64, 12s@0.6299999885, 14s@0.6299998973, 15s@0.629999995, 17s@0.64 ...


_Updated 2026-10-26 18:50Z_
