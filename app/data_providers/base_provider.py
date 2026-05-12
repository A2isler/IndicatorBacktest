from abc import ABC, abstractmethod
from datetime import datetime


class BaseDataProvider(ABC):
    @abstractmethod
    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime):
        """Return normalized OHLCV rows in UTC."""
        raise NotImplementedError
