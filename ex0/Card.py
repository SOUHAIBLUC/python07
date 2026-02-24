from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    """Abstract base class for all DataDeck cards."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play this card, modifying game state."""
        pass

    def get_card_info(self) -> Dict:
        """Return card information as a dictionary."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.__class__.__name__.replace('Card', '')
        }

    def is_playable(self, available_mana: int) -> bool:
        """Return True if card can be played with available mana."""
        return available_mana >= self.cost
