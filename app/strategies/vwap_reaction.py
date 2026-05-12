from .base_strategy import BaseStrategy


class VwapReactionStrategy(BaseStrategy):
    name = "vwap_reaction"

    def __init__(self, config: dict):
        self.config = config

    def on_bar(self, bar, context):
        return None
