import random


class Creature:
    def __init__(self, name, level, health, strength, perception, endurance, mana, agility, strengths, weaknesses):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
        self.perception = perception
        self.endurance = endurance
        self.mana = mana
        self.agility = agility
        self.strengths = strengths
        self.weaknesses = weaknesses

    def __repr__(self):
        return f'Creature {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level
