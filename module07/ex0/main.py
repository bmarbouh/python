from ex0.CreatureCard import CreatureCard, RARITY


def main():
    print("\n=== DataDeck Card Foundation ===\n")
    print("\nTesting Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    try:
        creature_card = CreatureCard("Fire Dragon",5,RARITY.LEGENDARY.value,7,5)
        print(creature_card.get_card_info())
        state = {"mana": 6}
        print(f"\nPlaying Fire Dragon with {state.get("mana")} mana available:\n")
        print(f"Playable: {creature_card.is_playable(state["mana"])}")
        print(f"Play result: {creature_card.play(state)}")
        print("\nFire Dragon attacks Goblin Warrior:\n")
        print(f"Attack result: {creature_card.attack_target('Goblin Warrior')}")
        print(f"\nTesting insufficient mana ({state.get('mana')} available):")
        print(f"Playable: {creature_card.is_playable(state["mana"])}")
        print("\nAbstract pattern successfully demonstrated!")
    except Exception as v:
        print(v)

if __name__ == "__main__":
    main()