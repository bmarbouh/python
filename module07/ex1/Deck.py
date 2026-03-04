from ex0.Card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.card_list = []
    
    def add_card(self, card: Card) -> None:
        self.card_list.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        for item in self.card_list:
            if item.name == card_name:
                self.card_list.remove(item)
                return True
        return False
    
    def shuffle(self) -> None:
        random.shuffle(self.card_list)
    
    def draw_card(self) -> Card:
        return self.card_list.pop(0)
    
    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0
        
        for item in self.card_list:
            if item.type.lower() == 'creatures':
                creatures += 1
                total_cost += item.cost
            elif item.type.lower() == 'spells':
                spells += 1
                total_cost += item.cost
            elif item.type.lower() == 'artifacts':
                artifacts += 1
                total_cost += item.cost
            avg_cost = total_cost / len(self.card_list)
        return {
            'total_cards': len(self.card_list),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg_cost, 1)
        }