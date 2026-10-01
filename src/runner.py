"""Shared window scoring used by the backtest and paper scripts."""
import time

import yaml

from . import data, report
from .sim import classify

SOURCE = "INTL_PROXY"


def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def score_window(ws, cfg, pause=0.15):
    """Return (row, sample) for one window. Missing data excludes the window instead of raising."""
    market = data.get_market(ws)
    time.sleep(pause)
    if market is None:
        return report.make_row(ws, None, SOURCE, 0, "market_not_found", None, None), None
    if market["result"] is None:
        return report.make_row(ws, market, SOURCE, 0, "result_missing", None, None), None
    trades, truncated = data.get_trades(market["condition_id"], cfg["data_api_page"], cfg["data_api_max_offset"])
    time.sleep(pause)
    if truncated:
        return report.make_row(ws, market, SOURCE, len(trades), "trades_truncated", None, None), None
    if not trades:
        return report.make_row(ws, market, SOURCE, 0, "no_trades", None, None), None
    up, down = data.split_trades(trades, market["up_token"], market["down_token"])
    strict = classify(ws, up, down, cfg, strict=True)
    touch = classify(ws, up, down, cfg, strict=False)
    row = report.make_row(ws, market, SOURCE, len(trades), "", strict, touch)
    return row, (ws, up, down)


def spot_text(rows, samples, cfg, n=5):
    """Raw trades for up to n filled windows so a person can check the scoring by hand."""
    out, shown = [], 0
    for ws in sorted(samples):
        r = rows.get(ws)
        if not r or not r["p1_fill_side"] or shown >= n:
            continue
        shown += 1
        _, up, down = samples[ws]
        end = ws + 900
        out.append(f"### {r['window_start_utc']} (market {r['market_id']}, result {r['result']})")
        out.append(f"Scored: p1 {r['p1_fill_side']} filled at {r['p1_fill_s']}s, exit hit {r['p1_exit_hit']}; "
                   f"p2 {r['p2_fill_side'] or 'none'}. Profit p1 {r['p1_pnl']}.")
        for name, tr in (("Up", up), ("Down", down)):
            keep = [t for t in tr if ws <= t["timestamp"] < end
                    and (t["price"] <= cfg["entry_price"] or t["price"] >= cfg["exit_price"])]
            shown_t = ", ".join(f"{t['timestamp'] - ws}s@{t['price']}" for t in keep[:12])
            out.append(f"{name} trades at or below {cfg['entry_price']} or at or above {cfg['exit_price']} "
                       f"(seconds after start, price): {shown_t}" + (" ..." if len(keep) > 12 else ""))
        out.append("")
    return "\n".join(out)
