from creature import Creature

class Player(Creature):
    def __init__(self, id, name, description, characteristics, observations, weaknesses, resistances, immunities, given_name, items, adornments, hit_points, agility, charisma, endurance, intelligence, mana, perception, strength, location, xp, location_history, conversation_history):
        super().__init__(id, name, description, characteristics, observations, weaknesses, resistances, immunities, given_name, items, adornments, hit_points, agility, charisma, endurance, intelligence, mana, perception, strength, location)
        
        self.xp = xp
        self.location_history = location_history
        self.conversation_history = conversation_history
