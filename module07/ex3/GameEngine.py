from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.card_created = 0
        self.size = 3

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        deck = factory.create_themed_deck(self.size)
        self.hand.extend(deck['creature'])
        self.hand.extend(deck['spell'])
        self.hand.extend(deck['artifact'])
        self.card_created = len(self.hand)

    def simulate_turn(self) -> dict:
        res = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += res.get('damage_dealt', 0)
        return res

    def get_engine_status(self) -> dict:
        if self.strategy is None:
            raise RuntimeError("Engine Strategy not configured")
        return {
            'turn_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'card_created': self.card_created
        }
