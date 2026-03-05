from ex4.TournamentCard import TournamentCard
from typing import Dict
import random


class TournamentPlatform:
    def __init__(self) -> None:
        self.registre: Dict[str, TournamentCard] = {}
        self.matches = 0

    def register_card(self, card: TournamentCard) -> str:
        cid = card.id
        if cid in self.registre:
            raise ValueError("Carde already exsite")
        self.registre[cid] = card
        return cid

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.registre[card1_id]
        c2 = self.registre[card2_id]
        score1 = c1.attack_power + random.randint(0, c1.defense)
        score2 = c2.attack_power + random.randint(0, c2.defense)
        if score1 > score2:
            winner, loser = card1_id, card2_id
        else:
            winner, loser = card2_id, card1_id
        self.registre[winner].update_wins(1)
        self.registre[loser].update_losses(1)
        self.matches += 1
        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": self.registre[winner].calculate_rating(),
            "loser_rating": self.registre[loser].calculate_rating()
        }

    def get_leaderboard(self) -> list:
        ranked = sorted(
            self.registre.items(),
            key=lambda x: x[1].calculate_rating(),
            reverse=True
        )
        lines = []
        for i, (cid, card) in enumerate(ranked, 1):
            info = card.get_rank_info()
            lines.append(
                f"{i}. {card.name} - Rating:"
                f"{info['rating']} {info['record']}"
                )
        return lines

    def generate_tournament_report(self) -> dict:
        avg = 0
        s = 0
        for c in self.registre.values():
            s += c.calculate_rating()
            avg += 1
        avg = s / avg
        return {
            'total_cards': len(self.registre),
            'matches_played': self.matches,
            'avg_rating': int(avg),
            'platform_status': 'active'
        }
