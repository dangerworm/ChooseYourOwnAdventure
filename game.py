from beast import Beast
from character import Character
from item import Item
from location import Location

from random import randint

class Game:
  def __init__(self):
    # Create the items
    self.items = [
      Item(1, "Sword", "A sharp sword", 10, [], []),
      Item(2, "Shield", "A sturdy shield", 5, [], []),
      Item(3, "Potion", "A healing potion", 0, [], []),
      Item(4, "Key", "A key", 0, [], []),
      Item(5, "Gold", "A gold coin", 0, [], []),
      Item(6, "Diamond", "A diamond", 0, [], []),
      Item(7, "Ruby", "A ruby", 0, [], []),
      Item(8, "Emerald", "An emerald", 0, [], []),
      Item(9, "Sapphire", "A sapphire", 0, [], []),
      Item(10, "Amethyst", "An amethyst", 0, [], []),
      Item(11, "Pearl", "A pearl", 0, [], []),
      Item(12, "Topaz", "A topaz", 0, [], []),
      Item(13, "Opal", "An opal", 0, [], []),
      Item(14, "Jade", "A jade", 0, [], []),
      Item(15, "Onyx", "An onyx", 0, [], []),
      Item(16, "Turquoise", "A turquoise", 0, [], []),
      Item(17, "Quartz", "A quartz", 0, [], []),
      Item(18, "Citrine", "A citrine", 0, [], []),
      Item(19, "Agate", "An agate", 0, [], []),
      Item(20, "Garnet", "A garnet", 0, [], []),
    ]

    # Create the locations
    self.locations = [
      Location(1, "Forest", [2, 3], "You are in a forest.", [self.items[0], self.items[1]], ["You see a sword and a shield."]),
      Location(2, "Cave", [1, 4], "You are in a cave.", [self.items[2]], ["You see a potion."]),
      Location(3, "River", [1, 5], "You are by a river.", [], ["You see a river."]),
      Location(4, "Castle", [2, 6], "You are in a castle.", [self.items[3]], ["You see a key."]),
      Location(5, "Beach", [3, 6], "You are on a beach.", [], ["You see a beach."]),
      Location(6, "Town", [4, 5], "You are in a town.", [self.items[4], self.items[5], self.items[6], self.items[7], self.items[8], self.items[9], self.items[10], self.items[11], self.items[12], self.items[13], self.items[14], self.items[15], self.items[16], self.items[17], self.items[18], self.items[19]], ["You see a town."]),
    ]

    # Create the creatures
    self.beasts = [
      Beast(1, "Goblin", 1, 10, 2, 2, 2, 0, 2, [], [], self.locations[0], []),
      Beast(2, "Orc", 2, 20, 4, 4, 4, 0, 4, [], [], self.locations[1], []),
      Beast(3, "Troll", 3, 30, 6, 6, 6, 0, 6, [], [], self.locations[2], []),
      Beast(4, "Dragon", 4, 40, 8, 8, 8, 0, 8, [], [], self.locations[3], []),
      Beast(5, "Giant", 5, 50, 10, 10, 10, 0, 10, [], [], self.locations[4], []),
      Beast(6, "Golem", 6, 60, 12, 12, 12, 0, 12, [], [], self.locations[5], [])
    ]

    self.characters = [
      Character(1, "Hero", 1, 10, 2, 2, 2, 0, 2, [], [], 0, 2, 2, self.locations[4], []),
      Character(2, "Knight", 2, 20, 4, 4, 4, 0, 4, [], [], 0, 4, 4, self.locations[3], []),
      Character(3, "Warrior", 3, 30, 6, 6, 6, 0, 6, [], [], 0, 6, 6, self.locations[3], []),
      Character(4, "Paladin", 4, 40, 8, 8, 8, 0, 8, [], [], 0, 8, 8, self.locations[3], []),
      Character(5, "Ranger", 5, 50, 10, 10, 10, 0, 10, [], [], 0, 10, 10, self.locations[0], []),
      Character(6, "Bard", 6, 60, 12, 12, 12, 0, 12, [], [], 0, 12, 12, self.locations[5], []),
    ]
    
    self.player = None

  def setup_player(self, name, choose_stats):
    if name == None:
      name = input("What is your name? ")
    
    if choose_stats == None:
      choose_stats = input("Do you want to choose your character's stats? (y/n) ")

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

    self.player = Character(1, name, level, health, strength, perception, endurance, mana, agility, [], [], 0, charisma, intelligence, self.locations[0], [])
