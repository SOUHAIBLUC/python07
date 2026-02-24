from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict, List

BASE_RATING = 1200
WIN_DELTA = 16
LOSS_DELTA = 16


class TournamentCard(Card, Combatable, Rankable):
    """Card with full combat and tournament ranking capabilities."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense_power: int,
        base_rating: int = BASE_RATING
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack_power
        self.defense_power = defense_power
        self._rating = base_rating
        self._wins = 0
        self._losses = 0

    def get_card_info(self) -> Dict:
        """Return full card information."""
        info = super().get_card_info()
        info['type'] = 'TournamentCard'
        info['attack_power'] = self.attack_power
        info['defense_power'] = self.defense_power
        return info

    def play(self, game_state: dict) -> dict:
        """Deploy the tournament card."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card deployed'
        }

    # --- Combatable interface ---

    def attack(self, target) -> dict:
        """Attack a target."""
        target_name = target if isinstance(target, str) else target.name
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'tournament'
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        blocked = min(self.defense_power, incoming_damage)
        taken = incoming_damage - blocked
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': taken < self.attack_power
        }

    def get_combat_stats(self) -> Dict:
        """Return combat statistics."""
        return {
            'name': self.name,
            'attack_power': self.attack_power,
            'defense_power': self.defense_power
        }

    # --- Rankable interface ---

    def calculate_rating(self) -> int:
        """Return current Elo-style rating."""
        return self._rating

    def update_wins(self, wins: int) -> None:
        """Add wins and increase rating."""
        self._wins += wins
        self._rating += WIN_DELTA * wins

    def update_losses(self, losses: int) -> None:
        """Add losses and decrease rating."""
        self._losses += losses
        self._rating = max(0, self._rating - LOSS_DELTA * losses)

    def get_rank_info(self) -> Dict:
        """Return ranking information."""
        return {
            'name': self.name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
            'record': f"{self._wins}-{self._losses}"
        }

    def get_tournament_stats(self) -> Dict:
        """Return combined combat and ranking stats."""
        stats = self.get_rank_info()
        stats.update(self.get_combat_stats())
        stats['interfaces'] = ['Card', 'Combatable', 'Rankable']
        return stats
