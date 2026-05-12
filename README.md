# IndicatorBacktest

Local, modular backtesting project for comparing multiple TradingView/Pine strategy logics on the same datasets.

## MVP Scope (Phase 1)
- Python project skeleton.
- Config-driven runtime defaults.
- Provider abstraction with OANDA as primary provider target.
- Backtest engine interfaces (commission, slippage, risk controls).
- Strategy interfaces for VWAP Reaction and Key Level Reaction.
- Reporting folders for CSV/HTML output.

## Confirmed Defaults
- Initial capital: 1000 USD
- Commission: 0.0005 (per side)
- Risk per trade: 2%
- Fill model: signal bar close -> next bar open
- Slippage default: 0.01% (configurable)
- Session timezone base: UTC (with London/NY filters configurable)
- Primary data provider target: OANDA

## Quick Start (How to run)
1. Python 3.11+ kur.
2. Dependency yükle:
   ```bash
   pip install -r requirements.txt
   ```
3. CLI dry-run çalıştır:
   ```bash
   python -m app.cli.run_backtest --dry-run
   ```

Beklenen örnek çıktı:
- primary provider
- sembol sayısı
- risk yüzdesi

## Current Status
- Bu sürümde gerçek veri çekme ve backtest event loop henüz uygulanmadı.
- CLI şu an config doğrulama + başlangıç kontrolü yapar.
