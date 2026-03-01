from ex0.Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card: Card) -> None:
        self.cards.append(card)
    
    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card_name == card.name:
                self.cards.remove(card)
                return True
        return False
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def draw_card(self) -> Card:
        return self.cards.pop(0)
    
    def get_deck_stats(self) -> dict:
        artifact_count = 0
        creature_count = 0
        spell_count = 0 
        total_cost = 0
        for card in self.cards:
            if card.type.lower() == "creature":
                creature_count += 1
                total_cost += card.cost
            elif card.type.lower() == "spell":
                spell_count += 1
                total_cost += card.cost
            elif card.type.lower() == "artifact":
                artifact_count += 1
                total_cost += card.cost
                
        return {
            "total_card": len(self.cards),
            "creatures": creature_count,
            "spells": spell_count,
            "artifact": artifact_count,
            "avg_cost":round((total_cost / len(self.cards)),1)
        }
    