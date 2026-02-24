#!/usr/bin/env python3

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """Demonstrate the Game Engine with Factory and Strategy patterns."""
    print("=== DataDeck Game Engine ===")
    print()

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {type(strategy).__name__}")

    supported_types = factory.get_supported_types()
    print(f"Available types: {supported_types}")
    print()

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Simulating aggressive turn...")
    hand_descriptions = []
    for card in engine.hand:
        card_info = card.get_card_info()
        hand_descriptions.append(
            f"{card_info['name']} ({card_info['cost']})"
        )
    print(f"Hand: {hand_descriptions}")
    print()

    print("Turn execution:")
    turn_result = engine.simulate_turn()
    print(f"Strategy: {turn_result.get('strategy', 'Unknown')}")

    actions = {
        "cards_played": turn_result.get("cards_played", []),
        "mana_used": turn_result.get("mana_used", 0),
        "targets_attacked": turn_result.get("targets_attacked", []),
        "damage_dealt": turn_result.get("damage_dealt", 0)
    }
    print(f"Actions: {actions}")
    print()

    print("Game Report:")
    status = engine.get_engine_status()
    report = {
        "turns_simulated": status["turns_simulated"],
        "strategy_used": status["strategy_used"],
        "total_damage": status["total_damage"],
        "cards_created": status["cards_created"]
    }
    print(report)
    print()

    print("Abstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
