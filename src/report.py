"""CSV storage for window rows and the plain-English summary."""
import csv
import datetime as dt
import os

from .stats import wilson, longest_losing_streak, verdict, combined_verdict

COLS = [
    "window_start_utc", "window_start", "market_id", "source", "result", "trade_count", "excluded_reason",
    "status",
    "p1_fill_side", "p1_fill_s", "p1_exit_hit", "p1_exit_s",
    "p2_fill_side", "p2_fill_s", "p2_exit_hit", "p2_exit_s",
    "touch_fills", "touch_hits",
    "p1_shares", "p1_pnl", "p2_shares", "p2_pnl", "balance_after",
]


def iso(ts):
    return dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def load(path):
    if not os.path.exists(path):
        return {}
    with open(path, newline="") as f:
        return {int(r["window_start"]): r for r in csv.DictReader(f)}


def save(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for k in sorted(rows):
            w.writerow(rows[k])


def make_row(window_start, market, source, trade_count, excluded, outcome, touch):
    row = {c: "" for c in COLS}
    row.update(window_start_utc=iso(window_start), window_start=window_start, source=source,
               market_id=market["market_id"] if market else "",
               result=(market or {}).get("result") or "", trade_count=trade_count,
               excluded_reason=excluded, status="excluded" if excluded else outcome.status)
    if excluded:
        return row
    for i, pos in enumerate(outcome.positions[:2], start=1):
        row[f"p{i}_fill_side"] = pos.side
        row[f"p{i}_fill_s"] = pos.fill_s
        row[f"p{i}_exit_hit"] = int(pos.exit_hit)
        row[f"p{i}_exit_s"] = "" if pos.exit_s is None else pos.exit_s
    row["touch_fills"] = len(touch.positions)
    row["touch_hits"] = sum(p.exit_hit for p in touch.positions)
    return row


def rebuild(rows, cfg):
    """Recompute shares, profit and balance for every scored row in time order. Idempotent."""
    from .sim import Outcome, Position, apply_stake
    balance = float(cfg["bankroll_start"])
    for k in sorted(rows):
        r = rows[k]
        r["p1_shares"] = r["p1_pnl"] = r["p2_shares"] = r["p2_pnl"] = ""
        if r["excluded_reason"]:
            r["balance_after"] = ""
            continue
        if not r["p1_fill_side"]:
            r["status"] = "no_fill"
            r["balance_after"] = round(balance, 4)
            continue
        out = Outcome(int(r["window_start"]), status="filled")
        for i in (1, 2):
            if r[f"p{i}_fill_side"]:
                out.positions.append(Position(
                    side=r[f"p{i}_fill_side"], fill_s=float(r[f"p{i}_fill_s"]),
                    exit_hit=str(r[f"p{i}_exit_hit"]) == "1",
                    exit_s=float(r[f"p{i}_exit_s"]) if r[f"p{i}_exit_s"] != "" else None))
        balance = apply_stake(out, r["result"], balance, cfg)
        r["status"] = out.status
        for i, p in enumerate(out.positions, start=1):
            r[f"p{i}_shares"], r[f"p{i}_pnl"] = p.shares, round(p.pnl, 4)
        r["balance_after"] = round(balance, 4)
    return rows


def metrics(rows, cfg):
    scored = sorted((r for r in rows.values() if not r["excluded_reason"]), key=lambda r: int(r["window_start"]))
    excluded = [r for r in rows.values() if r["excluded_reason"]]
    positions = []
    for r in scored:
        for i in (1, 2):
            if r[f"p{i}_fill_side"] and str(r[f"p{i}_shares"]) not in ("", "0"):
                positions.append((str(r[f"p{i}_exit_hit"]) == "1", float(r[f"p{i}_pnl"])))
    fills = len(positions)
    hits = sum(h for h, _ in positions)
    start = float(cfg["bankroll_start"])
    final = start
    for r in scored:
        if r["balance_after"] != "":
            final = float(r["balance_after"])
    reasons = {}
    for r in excluded:
        reasons[r["excluded_reason"]] = reasons.get(r["excluded_reason"], 0) + 1
    tf = sum(int(r["touch_fills"] or 0) for r in scored)
    th = sum(int(r["touch_hits"] or 0) for r in scored)
    return {
        "scored": len(scored), "excluded": len(excluded), "reasons": reasons,
        "fills": fills, "hits": hits, "hit_rate": hits / fills if fills else 0.0,
        "fill_rate": sum(1 for r in scored if r["p1_fill_side"]) / len(scored) if scored else 0.0,
        "too_small": sum(1 for r in scored if r["status"] == "too_small"),
        "profit": final - start, "final": final,
        "streak": longest_losing_streak([p for _, p in positions]),
        "touch_fills": tf, "touch_hits": th,
        "verdict": verdict(fills, hits, final - start, cfg),
    }


def _section(title, m, cfg):
    lo, hi = wilson(m["hits"], m["fills"])

    def pct(x):
        return f"{100 * x:.1f}%"

    reasons = f" ({', '.join(f'{k}: {v}' for k, v in m['reasons'].items())})" if m["reasons"] else ""
    lines = [f"## {title}", "",
             f"- Verdict: **{m['verdict']}**",
             f"- Windows scored: {m['scored']}; excluded: {m['excluded']}{reasons}",
             f"- Fill rate: {pct(m['fill_rate'])} of scored windows had a fill ({m['too_small']} too small)",
             f"- Fills that reached 45c: {m['hits']} of {m['fills']} = {pct(m['hit_rate'])} "
             f"(95% range {pct(lo)} to {pct(hi)}; pass needs the low end above {pct(cfg['hit_breakeven'])} "
             f"and at least {cfg['min_fills_for_verdict']} fills)",
             f"- Paper profit after fees: ${m['profit']:.2f} (balance ${m['final']:.2f} from ${cfg['bankroll_start']})",
             f"- Longest losing streak: {m['streak']}"]
    if m["touch_fills"]:
        lines.append(f"- Strict vs touch: strict {m['hits']}/{m['fills']} = {pct(m['hit_rate'])}; "
                     f"touch {m['touch_hits']}/{m['touch_fills']} = {pct(m['touch_hits'] / m['touch_fills'])}. "
                     f"The verdict uses strict.")
    return lines


def write_summary(path, cfg, backtest_rows, paper_rows, sources, spot_text=""):
    bm = metrics(backtest_rows, cfg) if backtest_rows else None
    pm = metrics(paper_rows, cfg) if paper_rows else None
    if bm and pm:
        overall = combined_verdict(bm["verdict"], pm["verdict"], bm["hit_rate"], pm["hit_rate"], cfg)
    else:
        overall = "NOT ENOUGH DATA"
    lines = [f"# BTC 15-min strategy tracker: {overall}", "",
             f"Data source: {', '.join(sources) or 'none yet'}. INTL_PROXY means trades from the international "
             f"exchange, used because the US gateway publishes no public trade history.",
             "Real money needs PASS in both the backtest and the live paper run, with the live hit rate within "
             "8 points of the backtest.", ""]
    if bm:
        lines += _section("Backtest", bm, cfg) + [""]
    if pm:
        lines += _section("Live paper run", pm, cfg) + [""]
    else:
        lines += ["## Live paper run", "", "- No windows scored yet.", ""]
    if spot_text:
        lines += ["## Spot-checked windows", "", spot_text]
    lines += ["", f"_Updated {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%MZ')}_"]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return overall
