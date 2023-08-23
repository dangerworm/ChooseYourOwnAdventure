import random

class CreatureType:
    def __init__(self, id, name, description, characteristics, observations, weaknesses, resistances, immunities):
        self.id = id
        self.name = name
        self.description = description
        self.characteristics = characteristics
        self.observations = observations
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities

    def __repr__(self):
        return f'Creature {self.name}'

    # def get_defensive_roll(self):
    #     return random.randint(1, 12) * self.level
