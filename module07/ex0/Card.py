from abc import ABC, abstractmethod
from enum import Enum

class RARITY(Enum):
    LEGENDARY = "Legendary"
    COMMON = "Common"
    EPIC = "Epic"
    RARE = "Rare"
    UNCOMMON = "Uncommon"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
    
    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass
    
    def get_card_info(self) -> dict:
        pass
    
    def is_playable(self, available_mana: int) -> bool:
        if isinstance(available_mana, int) and available_mana >= 0:
            return self.cost <= available_mana
        raise ValueError("Not enough mana to play the card")