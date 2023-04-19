from creature import Creature


class Beast(Creature):
    def __init__(self, id, name, level, health, strength, perception, endurance, mana, agility, strengths, weaknesses, location, items):
        super().__init__(name, level, health, strength, perception,
                         endurance, mana, agility, strengths, weaknesses)
        self.id = id
        self.location = location
        self.items = items

    def __repr__(self):
        return f'Beast {self.name} of level {self.level}'

    def get_defensive_roll(self):
        return super().get_defensive_roll() * self.level
