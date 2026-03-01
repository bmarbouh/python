from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard, RARITY

def main():
    print("\n=== DataDeck Deck Builder ===\n")
    creature_card = CreatureCard("Fire Dragon",5,RARITY.LEGENDARY.value,7,5)
    spell_card = SpellCard("Lightning Bolt", 3, RARITY.LEGENDARY.value, "Deal 3 damage to target")
    artifact_card = ArtifactCard("Mana Crystal", 2, RARITY.EPIC.value, 7,   "Permanent: +1 mana per turn")
    game_state = {"mana":10}
    print("Building deck with different card types...")
    deck_class = Deck()
    deck_class.add_card(spell_card)
    deck_class.add_card(artifact_card)
    deck_class.add_card(creature_card)
    print(f"Deck stats: {deck_class.get_deck_stats()}")
    print("\nDrawing and playing cards:\n")
    deck_class.shuffle()
    for _ in deck_class.cards[:]:
        draw_card = deck_class.draw_card()
        print(f"Drew: {draw_card.name} ({draw_card.type})")
        print(f"Play result: {draw_card.play(game_state)}")
        print("")
    print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()