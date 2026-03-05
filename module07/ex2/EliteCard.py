from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Magical, Combatable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        health: int,
        attack_damage: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.attack_damage = attack_damage if attack_damage >= 0 else 0
        self.type = "elite"
        self.shield = 5
        self.game_state = {}
        self.combat_type = "melee"

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get("mana")):
            return {"error": "insufficient mana!"}
        game_state["mana"] -= self.cost
        self.game_state = game_state
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": (
                f"Elite {self.name} summoned with {self.attack_damage} "
                f"attack and {self.health} health"
            ),
        }

    def attack(self, target: Card) -> dict:
        if not self.is_playable(self.game_state.get("mana")):
            return {"error": "insufficient mana!"}
        target.health -= self.attack_damage
        if target.health < 0:
            target.health = 0
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_damage,
            'combat_type': self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not self.is_playable(self.game_state.get('mana')):
            return {
                'error': "insufficient mana!"
            }
        for target in targets:
            target.health -= self.attack_damage
            if target.health < 0:
                target.health = 0
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [card.name for card in targets],
            'mana_used': self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        return {
            'channeled': amount,
            'total_mana': self.game_state['mana'] + amount
        }

    def get_magic_stats(self) -> dict:
        return {
            'name': self.name,
            'mana': self.game_state.get("mana"),
        }

    def defend(self, incoming_damage: int) -> dict:
        dmg = incoming_damage - self.shield
        damage_taken = max(dmg, 0)
        self.health -= dmg
        damage_blocked = (
            self.shield if self.shield < incoming_damage
            else incoming_damage
        )
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'attack': self.attack_damage,
            'health': self.health,
            'shield': self.shield,
            'combat_type': self.combat_type
        }
