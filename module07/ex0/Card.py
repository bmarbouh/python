from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type = "card"
    @abstractmethod 
    def play(self, game_state: dict) -> dict:
        pass
    
    def  get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }
    
    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int) and available_mana >= 0:
            return self.cost <= available_mana
        raise ValueError("Not enough mana")
