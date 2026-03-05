from ex4.Rankable import Rankable
from ex0.Card import Card
from ex2.Combatable import Combatable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        id: str,
        name: str,
        cost: int,
        rarity: int,
        attack_power: int,
        defense: int,
        rating: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.id = id
        self.wins = 0
        self.lose = 0
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get('mana')):
            return {
                'error': "insufficient mana!"
            }
        game_state['mana'] -= self.cost
        return {
            'name': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card entered battlefield'
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': str(target),
            'damage': self.attack_power
        }

    def defend(self, incoming_damage: int):
        blocked = min(self.defense, incoming_damage)
        taken = max(0, incoming_damage - blocked)
        return {
            "defender": self.name,
            "damage_blocked": blocked,
            "damage_taken": taken
        }

    def get_combat_stats(self) -> dict:
        return {"attacker": self.attack_power, "defense": self.defense}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.lose += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "record": f"({self.wins}-{self.lose})"
        }

    def get_tournament_stats(self) -> dict:
        return {
            self.get_card_info(),
            self.get_combat_stats(),
            self.get_rank_info()
        }
