from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    fire_dragon = CreatureCard(
        name='Fire Dragon',
        cost=5,
        rarity='Legendary',
        attack=7,
        health=5
    )

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    available_mana = 6
    print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
    print(f"Playable: {fire_dragon.is_playable(available_mana)}")
    print(f"Play result: {fire_dragon.play({'mana': available_mana})}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target('Goblin Warrior')}")

    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {fire_dragon.is_playable(low_mana)}")

    print("\nAbstract pattern successfully demonstrated!")
    print(
        "How do abstract base classes ensure consistency across different"
        " card types? What happens if you try to create a Card directly"
        " without implementing required methods?"
    )


if __name__ == '__main__':
    main()
