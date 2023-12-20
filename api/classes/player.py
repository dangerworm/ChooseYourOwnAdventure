from classes.creature import Creature
from utils.phrasing import Phrasing

class Player(Creature):
    def __init__(self, id, name, description, characteristics, observations, weaknesses, resistances, immunities, given_name, items, adornments, hit_points, agility, charisma, endurance, intelligence, mana, perception, strength, location, xp, location_history, conversation_history):
        super().__init__(id, name, description, characteristics, observations, weaknesses, resistances, immunities, given_name, items, adornments, hit_points, agility, charisma, endurance, intelligence, mana, perception, strength, location)
        
        self.xp = xp
        self.location_history = location_history
        self.conversation_history = conversation_history

    def set_location(self, location, time_of_day):
        location.spawn_creatures(time_of_day)

        self.location_history.append(location.id)
    
    def check_player_inventory(self):
        text_items = Phrasing.count_items(self.items)
        return text_items   