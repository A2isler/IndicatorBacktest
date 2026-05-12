# IndicatorBacktest

Local, modular backtesting project for comparing multiple TradingView/Pine strategy logics on the same datasets.

## Quick Start
1. Dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Config dry-run:
   ```bash
   python -m app.cli.run_backtest --dry-run
   ```
3. Local server (ayakta kalır):
   ```bash
   python -m app.cli.run_backtest --serve --host 127.0.0.1 --port 8000
   ```

## Localhost Endpoints
- `GET /` : endpoint list
- `GET /health` : health check
- `GET /config` : loaded config summary

Open in browser:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/config

## Notes
- Current server is intentionally minimal for Phase-1/2 visibility.
- Full backtest API routes will be added after engine/provider implementation.
