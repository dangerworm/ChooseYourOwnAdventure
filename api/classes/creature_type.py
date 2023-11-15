from random import random
from classes.creature_type_characteristics import CreatureTypeCharacteristics
class CreatureType:
    def __init__(self, *args):
        if len(args) == 4:
            self.id = args[0]
            self.name = args[1]
            self.description = args[2]
            self.observations = args[3]
            return

        if len(args) == 8:
            self.id = args[0]
            self.name = args[1]
            self.description = args[2]
            self.characteristics = args[3]
            self.observations = args[4]
            self.weaknesses = args[5]
            self.resistances = args[6]
            self.immunities = args[7]

        if len(args) == 13:
            self.id = args[0]
            self.name = args[1]
            self.description = args[2]
            self.observations = args[3]
            self.time_probabilities = args[4]
            self.characteristics = CreatureTypeCharacteristics(args[0],*args[5:])

    def should_spawn(self, time_of_day):
        probability = random()
        return probability < self.time_probabilities[time_of_day]

    def __repr__(self): 
        return f'Creature {self.name}'

    # def get_defensive_roll(self):
    #     return random.randint(1, 12) * self.level
