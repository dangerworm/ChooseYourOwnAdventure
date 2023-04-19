from creature import Creature


class Character(Creature):
    def __init__(self, id, name, level, health, strength, perception, endurance, mana, agility, strengths, weaknesses, xp, charisma, intelligence, location, items):
        super().__init__(name, level, health, strength, perception,
                         endurance, mana, agility, strengths, weaknesses)
        self.id = id
        self.xp = xp
        self.charisma = charisma
        self.intelligence = intelligence
        self.location = location
        self.items = items

    def __repr__(self):
        return f'Character {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return super().get_defensive_roll() * self.level
