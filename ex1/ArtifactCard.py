from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    """Concrete artifact card - permanent game modifiers."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def get_card_info(self) -> Dict:
        """Return artifact card information."""
        info = super().get_card_info()
        info['type'] = 'Artifact'
        info['durability'] = self.durability
        info['effect'] = self.effect
        return info

    def play(self, game_state: dict) -> dict:
        """Place artifact into play."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect}'
        }

    def activate_ability(self) -> dict:
        """Activate the artifact's ongoing effect."""
        if self.durability <= 0:
            return {
                'artifact': self.name,
                'activated': False,
                'reason': 'Artifact destroyed'
            }
        self.durability -= 1
        return {
            'artifact': self.name,
            'activated': True,
            'effect': self.effect,
            'durability_remaining': self.durability
        }
