from ex0.Card import Card, RARITY
from ex2.Magical import Magical
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard


def main() -> None:
    try:
        print('\n=== DataDeck Ability System ===\n')
        print('EliteCard capabilities:')
        classes = [Card, Combatable, Magical]
        game_state = {'mana': 10}
        for cls in classes:
            method_list = []
            for item in dir(cls):
                if not item.startswith('_'):
                    method_list.append(item)
            print(f"- {cls.__name__}: {method_list}")
        arcane = EliteCard("Arcane Warrior", 5, RARITY.LEGENDARY.value, 10, 5)
        enemy = EliteCard("Enemy", 5, RARITY.LEGENDARY.value, 4, 7)
        enemies = [
            EliteCard("Enemy1", 5, RARITY.COMMON.value, 4, 4),
            EliteCard("Enemy2", 5, RARITY.COMMON.value, 4, 4),
        ]
        print(f'\nPlaying {arcane.name} ({arcane.__class__.__name__}):\n')
        print('Combat phase:')
        arcane.play(game_state)
        print(f'Attack result: {arcane.attack(enemy)}')
        print(f"Defense result: {arcane.defend(enemy.attack_damage)}\n")
        print('Magic phase:')
        print(f'Spell cast: {arcane.cast_spell('Fireball', enemies)}')
        print(f'Mana channel: {arcane.channel_mana(3)}')
        print("\nMultiple interface implementation successful!")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
