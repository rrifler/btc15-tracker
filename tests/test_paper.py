import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src import markets, report, runner  # noqa: E402
from src.sim import classify  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import paper_update  # noqa: E402

CFG = runner.load_config(os.path.join(ROOT, "config.yaml"))


def fake_score(ws, cfg, pause=0.0):
    up = [{"timestamp": ws + 10, "price": 0.2, "size": 1, "side": "BUY"},
          {"timestamp": ws + 60, "price": 0.5, "size": 1, "side": "BUY"}] if ws % 1800 == 0 else []
    out = classify(ws, up, [], cfg)
    return report.make_row(ws, {"market_id": str(ws), "result": "up"}, "INTL_PROXY", len(up), "", out, out), None


def test_rerun_leaves_windows_csv_unchanged(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "config.yaml").write_text(open(os.path.join(ROOT, "config.yaml")).read())
    monkeypatch.setattr(runner, "score_window", fake_score)
    now = 1_800_000_000
    monkeypatch.setattr(paper_update.time, "time", lambda: now - 20 * 3600)     # paper started 20h ago
    monkeypatch.setattr(markets.time, "time", lambda: now)
    paper_update.main()
    first = open("results/windows.csv").read()
    summary1 = open("results/summary.md").read()
    paper_update.main()
    paper_update.main()
    assert open("results/windows.csv").read() == first
    rows = first.strip().splitlines()
    assert len(rows) - 1 == len({r.split(",")[1] for r in rows[1:]})            # no duplicate windows
    assert summary1.startswith("# BTC 15-min strategy tracker")
