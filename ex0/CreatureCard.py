from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    """Concrete creature card implementation."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer.")
        self.attack = attack
        self.health = health

    def get_card_info(self) -> Dict:
        """Return creature card information."""
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info
