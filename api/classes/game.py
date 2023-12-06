
from classes.player import Player
from classes.creature import Creature
from repositories.locations_repository import LocationsRepository
from repositories.items_repository import ItemsRepository
from repositories.creature_types_repository import CreatureTypesRepository
from random import randint

from utils.constants import DIRECTIONS, N, S, E, W, MORNING, AFTERNOON, EVENING, NIGHT


class Game:
    def __init__(self, items, creature_types, locations, time_of_day = MORNING):
        #call game_setup_workflow - to be added
        self.items = items
        self.creature_types = creature_types
        self.locations = locations
        self.time_of_day = time_of_day

        for location in locations.values():
            location.creature_types = [creature_type 
                                       for creature_type in self.creature_types.values()
                                        if creature_type.id in location.creature_type_ids.keys()]
            location.creatures = [Creature.generate(creature_type)
                                  for creature_type in location.creature_types]

            location.items = [item for item in self.items.values() 
                                   if item.id in location.item_ids.keys()]
            

        self.player = None

    def setup_player(self, name, choose_stats):
        if name == None:
            name = input("What is your name? ")

        if choose_stats == None:
            choose_stats = input(
                "Do you want to choose your character's stats? (y/n) ")

        if (choose_stats == "y"):
            print("Choose your character's stats:")
            level = int(input("Level: "))
            health = int(input("Health: "))
            strength = int(input("Strength: "))
            perception = int(input("Perception: "))
            endurance = int(input("Endurance: "))
            mana = int(input("Mana: "))
            agility = int(input("Agility: "))
            charisma = int(input("Charisma: "))
            intelligence = int(input("Intelligence: "))
        else:
            minStat = 6
            maxStat = 14

            level = 1
            health = 10
            strength = randint(minStat, maxStat)
            perception = randint(minStat, maxStat)
            endurance = randint(minStat, maxStat)
            mana = randint(minStat, maxStat)
            agility = randint(minStat, maxStat)
            charisma = randint(minStat, maxStat)
            intelligence = randint(minStat, maxStat)

        self.player = Player(1, name, 'Human', None, [], [], [], [], name, [], [],
                             health, agility, charisma, endurance, intelligence, 
                             mana, perception, strength, self.locations[1], 0, 
                             [self.locations[1]], [])
