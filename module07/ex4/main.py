from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    print('\n=== DataDeck Tournament Platform ===\n')
    print('\nRegistering Tournament Cards...\n')
    try:
        platform = TournamentPlatform()
        dragon = TournamentCard(
            "dragon_001", "Fire Dragon", 5, "Legendary", 7, 3, rating=1200
        )
        wizard = TournamentCard(
            "wizard_001", "Ice Wizard", 4, "Epic", 5, 4, rating=1150
        )
        id1 = platform.register_card(dragon)
        id2 = platform.register_card(wizard)
        for cid, card in [(id1, dragon), (id2, wizard)]:
            info = card.get_rank_info()
            print(f"{card.name} (ID: {cid}):")
            print("- Interfaces: [Card, Combatable, Rankable]")
            print(f"- Rating: {info['rating']}")
            print(f"- Record: {info['record']}\n")
        match_result = platform.create_match(id1, id2)
        print("Creating tournament match...")
        print(f"Match result: {match_result}\n")
        print("Tournament Leaderboard:")
        for line in platform.get_leaderboard():
            print(line)
        print("\nPlatform Report:")
        print(f"{platform.generate_tournament_report()}")
    except Exception as v:
        print(f"Error dected : {v}")
    print('\n=== Tournament Platform Successfully Deployed! ===')
    print('All abstract patterns working together harmoniously!')


if __name__ == "__main__":
    main()
