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
- Windows scored: 2221; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.0% of scored windows had a fill (248 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 215/467 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-24T02:15Z (market 6072061, result up)
Scored: p1 up filled at 107s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 5s@0.5, 8s@0.4599999451, 107s@0.239999996, 110s@0.24, 111s@0.25, 167s@0.24, 167s@0.24, 167s@0.24, 167s@0.2216666667, 167s@0.2399999964, 167s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5112072267, 3s@0.5099997829, 5s@0.5236170213, 6s@0.54, 6s@0.5325132629, 6s@0.54, 8s@0.55, 8s@0.5499999904, 8s@0.55, 8s@0.5499999964, 9s@0.549999945, 11s@0.5499999874 ...

### 2026-10-24T03:30Z (market 6072443, result down)
Scored: p1 down filled at 107s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099998215, 5s@0.5099998215, 9s@0.5099998215, 11s@0.5099998215, 63s@0.4919499106, 63s@0.55, 63s@0.5444466442, 63s@0.5, 63s@0.5171727796, 63s@0.5, 63s@0.5099999841, 65s@0.6158611405 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4899999824, 3s@0.5, 6s@0.5, 8s@0.5, 12s@0.5, 14s@0.5, 21s@0.51, 21s@0.5099999215, 21s@0.51, 23s@0.55, 24s@0.5499999897, 35s@0.5546747176 ...


_Updated 2026-10-24 06:39Z_
