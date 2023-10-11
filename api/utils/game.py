
from classes.player import Player
from repositories.locations_repository import LocationsRepository
from random import randint

from utils.constants import DIRECTIONS, N, S, E, W, MORNING, AFTERNOON, EVENING, NIGHT

class Game:
    def __init__(self):
        self.location_repository = LocationsRepository()
        self.time_of_day = MORNING
        #self.items = Factory.generate_items()
        #self.creature_types = Factory.generate_creature_types()
        #self.locations = Factory.generate_locations(self.items)
        records = self.location_repository.get_all()

            #location.spawn_creatures(self)
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

        self.player = Player(1, name, 'Human', None, [], [], [], [], 'Matt', [], [],
                             health, agility, charisma, endurance, intelligence, 
                             mana, perception, strength, self.locations[0], 0, 
                             [self.locations[0]], [])
