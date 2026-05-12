from datetime import datetime
from .base_provider import BaseDataProvider


class OandaProvider(BaseDataProvider):
    """Primary provider adapter (implementation in Phase 2)."""

    def __init__(self, config: dict):
        self.config = config

    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime):
        raise NotImplementedError("OANDA fetch implementation will be added in Phase 2")
