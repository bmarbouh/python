from abc import ABC, abstractmethod
from ex0.Card import Card


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Card) -> dict:
        pass
    
    @abstractmethod
    def defend(self, incoming_damage: int):
        pass
    
    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass