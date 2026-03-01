from ex0.Card import Card
from enum import Enum


class RARITY(Enum):
    LEGENDARY = "Legendary"
    COMMON = "Common"
    EPIC = "Epic"
    RARE = "Rare"
    UNCOMMON = "Uncommon"


class CreatureCard(Card):


    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.type = "creature"
        if attack > 0 and health > 0:
            self.attack = attack
            self.health = health
        else:
            raise ValueError("value of attack / health must positve & valid number")

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("mana")):
            return {"playable": False, "error": "Insufficient mana"}
        game_state['mana'] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        if not target:
            raise ValueError("target cannot be empty")
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self):
        return {
            "name": self.name,
            "cost":self.cost,
            "rarity":self.rarity,
            "type": self.type,
            "attack":self.attack,
            "health":self.health
            }
