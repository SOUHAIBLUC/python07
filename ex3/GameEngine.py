#!/usr/bin/env python3
"""
GameEngine Module - Game Orchestration System.

Combines Abstract Factory and Strategy patterns to create
a flexible game engine that can work with different card
factories and game strategies.
"""

from typing import Dict, Any, Optional, List
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Game orchestrator that combines factories and strategies.

    This class demonstrates how Abstract Factory and Strategy
    patterns work together to create a flexible game system.
    """

    def __init__(self) -> None:
        """Initialize the game engine."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.hand: List[Any] = []
        self.battlefield: List[Any] = []
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Configure the engine with a factory and strategy.

        Args:
            factory: Card factory for creating cards
            strategy: Game strategy for decision making
        """
        self.factory = factory
        self.strategy = strategy

        # Create a sample hand of cards
        if self.factory:
            self.hand = [
                self.factory.create_creature("Fire Dragon"),
                self.factory.create_creature("Goblin Warrior"),
                self.factory.create_spell("Lightning Bolt")
            ]
            self.cards_created = len(self.hand)

    def simulate_turn(self) -> Dict[str, Any]:
        """
        Simulate a game turn using the configured strategy.

        Returns:
            Dictionary with turn execution results
        """
        if not self.strategy:
            return {
                "error": "No strategy configured",
                "success": False
            }

        # Execute the turn using the strategy
        turn_result = self.strategy.execute_turn(
            self.hand,
            self.battlefield
        )

        # Update engine state
        self.turns_simulated += 1

        # Extract damage from turn result if available
        if "damage_dealt" in turn_result:
            self.total_damage += turn_result["damage_dealt"]

        return turn_result

    def get_engine_status(self) -> Dict[str, Any]:
        """
        Get current engine status and statistics.

        Returns:
            Dictionary with engine status information
        """
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (self.strategy.get_strategy_name()
                             if self.strategy else "None"),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
            "factory_type": (type(self.factory).__name__
                            if self.factory else "None"),
            "hand_size": len(self.hand),
            "battlefield_size": len(self.battlefield)
        }
