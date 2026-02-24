from abc import ABC, abstractmethod
from typing import Dict


class Magical(ABC):
    """Abstract interface defining magical capabilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a named spell on targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel mana to build magical power."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """Return magic statistics."""
        pass
