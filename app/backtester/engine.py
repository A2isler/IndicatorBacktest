from dataclasses import dataclass


@dataclass
class EngineConfig:
    initial_capital: float = 1000.0
    commission_rate: float = 0.0005
    risk_per_trade: float = 0.02
    slippage_bps: float = 1.0


class BacktestEngine:
    """Execution simulator shell. Detailed event loop in Phase 3."""

    def __init__(self, config: EngineConfig):
        self.config = config

    def run(self, bars, strategy):
        raise NotImplementedError("Backtest event loop will be added in Phase 3")
