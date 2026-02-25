from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    fire_dragon = TournamentCard(
        name='Fire Dragon',
        cost=5,
        rarity='Legendary',
        attack_power=7,
        defense_power=5,
        base_rating=1200
    )
    ice_wizard = TournamentCard(
        name='Ice Wizard',
        cost=4,
        rarity='Rare',
        attack_power=5,
        defense_power=4,
        base_rating=1150
    )

    platform = TournamentPlatform()
    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    def print_card_status(card: TournamentCard, card_id: str) -> None:
        info = card.get_rank_info()
        print(f"{card.name} (ID: {card_id}):")
        print(f"  - Interfaces: {card.get_tournament_stats()['interfaces']}")
        print(f"  - Rating: {info['rating']}")
        print(f"  - Record: {info['record']}")

    print_card_status(fire_dragon, dragon_id)
    print_card_status(ice_wizard, wizard_id)

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']}"
            f" - Rating: {entry['rating']}"
            f" ({entry['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == '__main__':
    main()
