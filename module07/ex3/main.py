from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    try:
        fantasy_cf = FantasyCardFactory()
        ag_strategy = AggressiveStrategy()
        print(f"Factory: {fantasy_cf.__class__.__name__}")
        print(f"Strategy: {ag_strategy.__class__.__name__}")
        print(f"Available types: {fantasy_cf.get_supported_types()}")
        game_engine = GameEngine()
        game_engine.configure_engine(fantasy_cf, ag_strategy)
        print("\nSimulating aggressive turn...")
        hand = [
            f"{card.name} ({getattr(card, 'cost')})"
            for card in game_engine.hand
        ]
        print(f"hand: {hand}\n")
        print("Turn execution:")
        res = game_engine.simulate_turn()
        print(f'Strategy: {ag_strategy.get_strategy_name()}')
        print(f"Actions: {res}")
        print('\nGame Report:')
        print(game_engine.get_engine_status())
    except Exception as v:
        print(f"Error dected : {v}")
    print(
        '\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!'
        )


if __name__ == "__main__":
    main()
