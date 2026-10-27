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
- Windows scored: 2504; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.0% of scored windows had a fill (301 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 246/530 = 46.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-27T03:45Z (market 6236052, result down)
Scored: p1 up filled at 86s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.472605042, 27s@0.4699999796, 27s@0.469999906, 42s@0.4799998464, 86s@0.22, 86s@0.22, 86s@0.21, 86s@0.21, 89s@0.24, 98s@0.2399999923, 102s@0.17, 102s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.48, 11s@0.5399999129, 26s@0.5399999568, 48s@0.54, 48s@0.55, 59s@0.66, 59s@0.6422924397, 59s@0.63, 60s@0.69, 60s@0.67, 62s@0.6999999296 ...


_Updated 2026-10-27 05:37Z_
