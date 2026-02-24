from ex4.TournamentCard import TournamentCard
from typing import Dict, List, Optional


class TournamentPlatform:
    """Platform for managing tournament registration and matches."""

    def __init__(self) -> None:
        self._cards: Dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its unique tournament ID."""
        card_id = card.name.lower().replace(' ', '_') + '_001'
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two registered cards."""
        card1 = self._cards.get(card1_id)
        card2 = self._cards.get(card2_id)

        if not card1 or not card2:
            return {'error': 'One or both cards not found'}

        score1 = card1.attack_power + card1.defense_power
        score2 = card2.attack_power + card2.defense_power

        if score1 >= score2:
            winner, loser = card1_id, card2_id
            self._cards[winner].update_wins(1)
            self._cards[loser].update_losses(1)
        else:
            winner, loser = card2_id, card1_id
            self._cards[winner].update_wins(1)
            self._cards[loser].update_losses(1)

        self._matches_played += 1

        return {
            'winner': winner,
            'loser': loser,
            'winner_rating': self._cards[winner].calculate_rating(),
            'loser_rating': self._cards[loser].calculate_rating()
        }

    def get_leaderboard(self) -> List[Dict]:
        """Return cards sorted by rating descending."""
        ranked = sorted(
            self._cards.items(),
            key=lambda x: x[1].calculate_rating(),
            reverse=True
        )
        leaderboard = []
        for rank, (card_id, card) in enumerate(ranked, start=1):
            info = card.get_rank_info()
            info['rank'] = rank
            info['card_id'] = card_id
            leaderboard.append(info)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Generate a summary report of the tournament."""
        total = len(self._cards)
        avg_rating = (
            sum(c.calculate_rating() for c in self._cards.values()) // total
            if total > 0 else 0
        )
        return {
            'total_cards': total,
            'matches_played': self._matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
