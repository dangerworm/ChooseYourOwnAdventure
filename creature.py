from creature_type import CreatureType

class Creature(CreatureType):
    def __init__(self, id, name, description, observations, weaknesses, resistances, immunities, given_name, items, adornments, hit_points, agility, charisma, endurance, intelligence, mana, perception, strength, location):
        super().__init__(id, name, description, observations, weaknesses, resistances, immunities)
        self.given_name = given_name
        self.items = items
        self.adornments = adornments
        self.hit_points = hit_points
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
