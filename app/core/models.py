from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Bar:
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    symbol: str


@dataclass
class Signal:
    symbol: str
    side: str
    timestamp: datetime
    entry_hint: float
    stop_loss: float
    take_profit: float
    strategy: str


@dataclass
class Trade:
    symbol: str
    side: str
    entry_time: datetime
    entry_price: float
    qty: float
    stop_loss: float
    take_profit: float
    exit_time: Optional[datetime] = None
    exit_price: Optional[float] = None
    realized_pnl: float = 0.0
