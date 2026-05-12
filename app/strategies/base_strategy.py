from abc import ABC, abstractmethod


class BaseStrategy(ABC):
    name = "base"

    @abstractmethod
    def on_bar(self, bar, context):
        """Return signal(s) or None."""
        raise NotImplementedError
