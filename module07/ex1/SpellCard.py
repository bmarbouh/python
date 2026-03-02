from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = 'Spells'
    def play(self, game_state):
        if not self.is_playable(game_state.get('mana')):
            return {
                'error': "insufficient mana!"
            }
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }
    
    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'effect': self.effect_type,
            'targets': targets
        }