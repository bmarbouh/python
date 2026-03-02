from ex0.Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.attack = attack
        self.health = health
        self.type = 'Creatures'
        
    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get('mana')):
            return {
                'error': "insufficient mana!"
            }
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }
    
    def attack_target(self, target) -> dict:
        if not target:
            raise ValueError("error target cannot be empty or none")
        return {
            'attacker':self.name,
            'target': target,
            'damage_dealt': 7,
            'combat_resolved': True
        }
    
    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            'rarity': self.rarity,
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        }