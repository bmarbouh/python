from ex0.CreatureCard import CreatureCard
from ex0.Card import RARITY


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print('Testing Abstract Base Class Design:\n')
    creature = CreatureCard('Fire Dragon', 5, RARITY.LEGENDARY.value, 7, 5)
    print("CreatureCard Info:")
    print(creature.get_card_info())
    print('Playing Fire Dragon with 6 mana available:')
    state = {"mana": 6}
    try:
        print(f'Playable: {creature.is_playable(state.get('mana'))}')
        print('\nPlaying Fire Dragon with 6 mana available:')
        print(f'Play result: {creature.play(state)}')
        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {creature.attack_target('Goblin Warrior')}")
        print(f'\nTesting insufficient mana ({state.get('mana')} available):')
        print(f"Playble: {creature.is_playable(state.get('mana'))}")
        print('\nAbstract pattern successfully demonstrated!')
    except Exception as v:
        print(f"Error Detected {v}")


if __name__ == "__main__":
    main()
