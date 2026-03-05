from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        game_state = {'mana': 10}
        for card in hand:
            card.play(game_state)
            if hasattr(card, 'name') and hasattr(card, 'cost'):
                cards_played.append(card.name)
                mana_used += card.cost
                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif hasattr(
                    card, 'effect_type'
                ) and card.effect_type == 'damage':
                    damage_dealt += 3
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        prioritized = []
        for target in available_targets:
            if 'Player' in str(target):
                prioritized.insert(0, target)
            else:
                prioritized.append(target)
        return prioritized
