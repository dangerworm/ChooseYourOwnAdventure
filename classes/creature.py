from classes.creature_type import CreatureType
import random 

class Creature(CreatureType):
    def __init__(self, id, name, description, characteristics, observations, weaknesses, resistances, immunities, given_name, items, adornments, hit_points, agility, charisma, endurance, intelligence, mana, perception, strength, location):
        super().__init__(id, name, description, characteristics, observations, weaknesses, resistances, immunities)
        self.given_name = given_name
        self.items = items
        self.adornments = adornments
        self.hit_points = hit_points
        self.starting_hit_points = hit_points
        self.agility = agility
        self.charisma = charisma
        self.endurance = endurance
        self.intelligence = intelligence
        self.mana = mana
        self.perception = perception
        self.strength = strength
        self.location = location

    def __repr__(self):
        return f'Character {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return super().get_defensive_roll() * self.level

    def generate(creature_type):
        
        return Creature(1, creature_type.name, creature_type.description, creature_type.characteristics, creature_type.observations, creature_type.weaknesses, 
                        creature_type.resistances, creature_type.immunities, given_name='', items=[], adornments=[], 
                        hit_points=random.randint(*creature_type.characteristics.hit_points_range),
                        agility=random.randint(*creature_type.characteristics.agility_range),
                        charisma=random.randint(*creature_type.characteristics.charisma_range),
                        endurance=random.randint(*creature_type.characteristics.endurance_range),
                        intelligence=random.randint(*creature_type.characteristics.intelligence_range),
                        mana=random.randint(*creature_type.characteristics.mana_range),
                        perception=random.randint(*creature_type.characteristics.perception_range),
                        strength=random.randint(*creature_type.characteristics.strength_range),
                        location=None)
