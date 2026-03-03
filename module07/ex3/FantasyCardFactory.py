from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.Card import Card, RARITY
from ex3.CardFactory import CardFactory
import random

class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power) -> Card:
        data = {
            'dragon': {'name':"Fire Dragon",'cost': 5,'rarity' :RARITY.LEGENDARY.value,'attack': 7,'health': 5},
            'goblin': {'name':'Goblin Warrior','cost': 2,'rarity' : RARITY.COMMON.value,'attack': 3,'health': 2}
        }
        if name_or_power in data:
            c = data[name_or_power]
            player = CreatureCard(c['name'], c['cost'], c['rarity'], c['attack'], c['health'])
            return player
        raise ValueError("ERROR: creat creature card faild !!")

    def create_spell(self, name_or_power) -> Card:
        data = {
            'fireball': {'name':'Lightning Bolt','cost': 3, 'rarity':RARITY.COMMON.value,'effect_type': 'damage'},
        }
        
        if name_or_power in data:
            c = data[name_or_power]
            player = SpellCard(c['name'], c['cost'], c['rarity'], c['effect_type'])
            return player
        raise ValueError("ERROR: creat spell card faild !!")
    
    def create_artifact(self, name_or_power) -> Card:
        data = {
            'mana_ring': {'name': 'Mana Crystal','cost': 2,'rarity': RARITY.RARE.value,'durability': 5,'effect': '+1 mana per turn'},
        }
        if name_or_power in data:
            c = data[name_or_power]
            player = ArtifactCard(c['name'], c['cost'], c['rarity'], c['durability'], c['effect'])
            return player
        raise ValueError("ERROR: creat artifact card faild !!")
    
    def create_themed_deck(self, size: int) -> dict:
        deck = {"creature": [], "spell": [], "artifact": []}
        types = ["creature", "spell", "artifact"]
        
        creature_names = ["dragon", "goblin"]
        spell_names = ["fireball"]
        artifact_names = ["mana_ring"]

        for _ in range(size):
            e = random.choice(types)
            if e == 'creature':
                deck['creature'].append(self.create_creature(random.choice(creature_names)))
            elif e == 'spell':
                deck['spell'].append(self.create_spell(random.choice(spell_names)))
            elif e == 'artifact':
                deck['artifact'].append(self.create_artifact(random.choice(artifact_names)))
        
        return deck
    
    def get_supported_types(self) -> dict:
        return {
            'creature': ["dragon", "goblin"],
            'spell': ["fireball"],
            'artifact': ["mana_ring"]
        }
