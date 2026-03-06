from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex0.Card import RARITY
from ex1.Deck import Deck


def main() -> None:
    print('\n=== DataDeck Deck Builder ===\n')
    try:
        creature = CreatureCard("Fire Dragon", 5, RARITY.LEGENDARY.value, 7, 5)
        spell = SpellCard(
            "Lightning Bolt", 3, RARITY.COMMON.value, 'Deal 3 damage to target'
        )
        artifact = ArtifactCard(
            "Mana Crystal",
            2, RARITY.EPIC.value, 7, "Permanent +1 mana per turn"
        )
        game_state = {'mana': 10}
        deck = Deck()
        deck.add_card(creature)
        deck.add_card(spell)
        deck.add_card(artifact)
        print('Building deck with different card types...')
        print(f'Deck stats: {deck.get_deck_stats()}')
        print('\nDrawing and playing cards:\n')
        for _ in deck.card_list[:]:
            draw_card = deck.draw_card()
            print(f'Draw: {draw_card.name} ({draw_card.__class__.__name__})')
            print(f'Play result: {draw_card.play(game_state)}\n')
    except Exception as v:
        print(f"Error detcted : {v}")
    print(
        '\nPolymorphism in action: Same interface, different card behaviors!'
    )


if __name__ == "__main__":
    main()
