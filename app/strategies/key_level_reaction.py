from .base_strategy import BaseStrategy


class KeyLevelReactionStrategy(BaseStrategy):
    name = "key_level_reaction"

    def __init__(self, config: dict):
        self.config = config

    def on_bar(self, bar, context):
        return None
