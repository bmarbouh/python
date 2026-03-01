from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name, cost, rarity, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.effect = effect
        self.durability = durability
        self.type = "artifact"
        
    def play(self, game_state):
        if not self.is_playable(game_state.get("mana")):
            return {"playable": False, "error": "Insufficient mana"}
        game_state['mana'] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }
    
    def activate_ability(self) -> dict:
        return {"effect":self.effect,"active": True}
    