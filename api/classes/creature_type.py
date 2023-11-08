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

    def __repr__(self): 
        return f'Creature {self.name}'

    # def get_defensive_roll(self):
    #     return random.randint(1, 12) * self.level
