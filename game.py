from player import Player
from item import Item
from location import Location
from creature_time_probabilities import CreatureTimeProbabilities
from creature_type import CreatureType
from creature_type_characteristics import CreatureTypeCharacteristics
from random import randint

from constants import DIRECTIONS, N, S, E, W, MORNING, AFTERNOON, EVENING, NIGHT

class Game:
    def __init__(self):
        self.time_of_day = MORNING

        # Create the items
        self.items = [
            Item(1, "Sword", "A sharp sword", [], [], [], 10, 100, 3, -1),
            Item(2, "Shield", "A sturdy shield", [], [], [], 10, 100, 3, -1),
            Item(3, "Potion", "A healing potion", [], [], [], 10, 100, 3, -1),
            Item(4, "Key", "A key", [], [], [], 10, 100, 3, -1),
            Item(5, "Gold", "A gold coin", [], [], [], 10, 100, 3, -1),
            Item(6, "Diamond", "A diamond", [], [], [], 10, 100, 3, -1),
            Item(7, "Barrel", "A wooden barrel", ["You can see something inside the barrel"], [], [1,2], 10, 100, 3, -1),
            Item(8, "Chest", "An iron chest", ["You see a sword, a shield, and a pouch"], [], [1,2,9], 15, 200, 15, -1),
            Item(9, "Pouch", "A cloth pouch", ["You see a potion inside"], [], [3], 1, 2, 1, -1)
        ]

        # Create the creature types
        self.creature_types = [
            CreatureType(1, 'Troll', 'Fat grey troll', CreatureTypeCharacteristics(1, 1, [5, 10], [4,8], [7,10], [3,6], [5,9], [6,9], [1,3], [8,10]), 
                        [], [], [], []),
            CreatureType(2, 'Ogre', 'Fat pink ogre', CreatureTypeCharacteristics(2, 2, [6, 7], [5,7], [4,7], [7,9], [5,6], [7,9], [3,5], [9,10]), 
                        [], [], [], [])
        ]

        # Create the locations
        self.locations = [
            Location(1, ["It's a bright sunlit morning. You see a chest", "It's a calm, breezy afternoon. You see a chest", "You see a chest",
                     "You see a chest"], [], [S], [8], 4, 1, [CreatureTimeProbabilities(1, 1, [1, 0.2, 0.5, 0]), CreatureTimeProbabilities(3, 2, [0, 0, 0.1, 0.99])]),
            Location(2, ["You are in a clearing", "You are in a clearing", "You are in a clearing",
                     "You are in a clearing"], [], [N, E, S, W], [], 4, 2, [CreatureTimeProbabilities(2, 2, [0, 0.2, 0.5, 0])]),
            Location(3, ["As you continue along the path to the north, you eventually arrive at a small jungle village. The villagers look at you warily, as they have never seen someone like you before. The village is made up of a collection of small huts and buildings, with thatched roofs and walls made from woven branches and mud. As you look around, you see that the villagers are going about their daily activities. Some are tending to crops in the nearby fields, while others are preparing food over open fires. The air is thick with the sound of jungle animals and birds, and the scent of cooking fires and jungle plants. You notice that there is only one exit from the village, and that is back the way you came to the west. This realization makes you feel a little uneasy, as you realize that you are completely surrounded by the dense jungle. Despite this, you also feel a sense of wonder and curiosity about this new place, and you wonder what kind of adventures await you in this mysterious corner of the world.", "As you continue along the path to the north, you eventually arrive at a small jungle village. The villagers look at you warily, as they have never seen someone like you before. The village is made up of a collection of small huts and buildings, with thatched roofs and walls made from woven branches and mud. As you look around, you see that the villagers are going about their daily activities. Some are tending to crops in the nearby fields, while others are preparing food over open fires. The air is thick with the sound of jungle animals and birds, and the scent of cooking fires and jungle plants. You notice that there is only one exit from the village, and that is back the way you came to the west. This realization makes you feel a little uneasy, as you realize that you are completely surrounded by the dense jungle. Despite this, you also feel a sense of wonder and curiosity about this new place, and you wonder what kind of adventures await you in this mysterious corner of the world.",
                     "As you continue along the path to the north, you eventually arrive at a small jungle village. The villagers look at you warily, as they have never seen someone like you before. The village is made up of a collection of small huts and buildings, with thatched roofs and walls made from woven branches and mud. As you look around, you see that the villagers are going about their daily activities. Some are tending to crops in the nearby fields, while others are preparing food over open fires. The air is thick with the sound of jungle animals and birds, and the scent of cooking fires and jungle plants. You notice that there is only one exit from the village, and that is back the way you came to the west. This realization makes you feel a little uneasy, as you realize that you are completely surrounded by the dense jungle. Despite this, you also feel a sense of wonder and curiosity about this new place, and you wonder what kind of adventures await you in this mysterious corner of the world.", "As you continue along the path to the north, you eventually arrive at a small jungle village. The villagers look at you warily, as they have never seen someone like you before. The village is made up of a collection of small huts and buildings, with thatched roofs and walls made from woven branches and mud. As you look around, you see that the villagers are going about their daily activities. Some are tending to crops in the nearby fields, while others are preparing food over open fires. The air is thick with the sound of jungle animals and birds, and the scent of cooking fires and jungle plants. You notice that there is only one exit from the village, and that is back the way you came to the west. This realization makes you feel a little uneasy, as you realize that you are completely surrounded by the dense jungle. Despite this, you also feel a sense of wonder and curiosity about this new place, and you wonder what kind of adventures await you in this mysterious corner of the world."], [], [W], [], 11, 1, []),
            Location(4, ["You see a chest", "You see a chest", "You see a chest",
                     "You see a chest"], [], [E, S], [], 2, 2, []),
            Location(5, ["you are in a clearing. you see 4 possible routes out. North, South, East or West.", "you are in a clearing. you see 4 possible routes out. North, South, East or West.",
                     "you are in a clearing. you see 4 possible routes out. North, South, East or West.", "you are in a clearing. you see 4 possible routes out. North, South, East or West."], [], [N, E, S, W], [], 4, 2, []),
            Location(6, ["You've arrived in a village", "You've arrived in a village",
                     "You've arrived in a village", "You've arrived in a village"], [], [W, E, S], [], 6, 2, []),
            Location(7, ["As you continue along the path, you come to a fork in the road where you must choose which way to go. To the north, you can see what looks like a village nestled between the trees. The village seems to be made up of small huts and cottages, and you can see smoke rising from the chimneys. To the west, you can see a different village, also hidden amongst the trees. This one seems larger and more developed, with several buildings and a central square. The path leading north is narrow and winding, and it disappears into the dense forest beyond the village. The path leading west is wider and more defined, suggesting that it is a well-traveled route. Both paths seem to offer different adventures and possibilities, and you feel torn about which way to go. As you stand at the fork in the road, you take a moment to consider your options. The village to the north seems quaint and peaceful, while the village to the west seems larger and more bustling. Ultimately, the decision is yours, and you must choose which way to go based on your own sense of adventure and curiosity.", "As you continue along the path, you come to a fork in the road where you must choose which way to go. To the north, you can see what looks like a village nestled between the trees. The village seems to be made up of small huts and cottages, and you can see smoke rising from the chimneys. To the west, you can see a different village, also hidden amongst the trees. This one seems larger and more developed, with several buildings and a central square. The path leading north is narrow and winding, and it disappears into the dense forest beyond the village. The path leading west is wider and more defined, suggesting that it is a well-traveled route. Both paths seem to offer different adventures and possibilities, and you feel torn about which way to go. As you stand at the fork in the road, you take a moment to consider your options. The village to the north seems quaint and peaceful, while the village to the west seems larger and more bustling. Ultimately, the decision is yours, and you must choose which way to go based on your own sense of adventure and curiosity.",
                     "As you continue along the path, you come to a fork in the road where you must choose which way to go. To the north, you can see what looks like a village nestled between the trees. The village seems to be made up of small huts and cottages, and you can see smoke rising from the chimneys. To the west, you can see a different village, also hidden amongst the trees. This one seems larger and more developed, with several buildings and a central square. The path leading north is narrow and winding, and it disappears into the dense forest beyond the village. The path leading west is wider and more defined, suggesting that it is a well-traveled route. Both paths seem to offer different adventures and possibilities, and you feel torn about which way to go. As you stand at the fork in the road, you take a moment to consider your options. The village to the north seems quaint and peaceful, while the village to the west seems larger and more bustling. Ultimately, the decision is yours, and you must choose which way to go based on your own sense of adventure and curiosity.", "As you continue along the path, you come to a fork in the road where you must choose which way to go. To the north, you can see what looks like a village nestled between the trees. The village seems to be made up of small huts and cottages, and you can see smoke rising from the chimneys. To the west, you can see a different village, also hidden amongst the trees. This one seems larger and more developed, with several buildings and a central square. The path leading north is narrow and winding, and it disappears into the dense forest beyond the village. The path leading west is wider and more defined, suggesting that it is a well-traveled route. Both paths seem to offer different adventures and possibilities, and you feel torn about which way to go. As you stand at the fork in the road, you take a moment to consider your options. The village to the north seems quaint and peaceful, while the village to the west seems larger and more bustling. Ultimately, the decision is yours, and you must choose which way to go based on your own sense of adventure and curiosity."], [7], [W, N, S], [], 9, 2, []),
            Location(8, ["You see a tiny fairy", "You see a tiny fairy",
                     "You see a tiny fairy", "You see a tiny fairy"], [], [N], [], 2, 3, []),
            Location(9, ["As you step off the old steam boat, you find yourself at the edge of a dense forest. The tall trees are covered in moss and vines, and the forest floor is a carpet of fallen leaves and twigs. The sound of chirping birds and rustling leaves fill the air, and you can see small patches of wildflowers blooming in the sunlight that filters through the canopy. A small path leads deeper into the forest, lined with trees and the occasional fern. The sound of a stream can be heard in the distance, and the faint smell of wood smoke hangs in the air. Beyond the forest, you can see rolling hills and mountains in the distance, and the sky above is a deep shade of blue with the occasional cloud drifting lazily by. The forest seems peaceful and inviting yet mysterious and full of secrets. You feel a sense of adventure and excitement as you contemplate what lies ahead on your journey through this beautiful wilderness.", "As you step off the old steam boat, you find yourself at the edge of a dense forest. The tall trees are covered in moss and vines, and the forest floor is a carpet of fallen leaves and twigs. The sound of chirping birds and rustling leaves fill the air, and you can see small patches of wildflowers blooming in the sunlight that filters through the canopy. A small path leads deeper into the forest, lined with trees and the occasional fern. The sound of a stream can be heard in the distance, and the faint smell of wood smoke hangs in the air. Beyond the forest, you can see rolling hills and mountains in the distance, and the sky above is a deep shade of blue with the occasional cloud drifting lazily by. The forest seems peaceful and inviting yet mysterious and full of secrets. You feel a sense of adventure and excitement as you contemplate what lies ahead on your journey through this beautiful wilderness.",
                     "As you step off the old steam boat, you find yourself at the edge of a dense forest. The tall trees are covered in moss and vines, and the forest floor is a carpet of fallen leaves and twigs. The sound of chirping birds and rustling leaves fill the air, and you can see small patches of wildflowers blooming in the sunlight that filters through the canopy. A small path leads deeper into the forest, lined with trees and the occasional fern. The sound of a stream can be heard in the distance, and the faint smell of wood smoke hangs in the air. Beyond the forest, you can see rolling hills and mountains in the distance, and the sky above is a deep shade of blue with the occasional cloud drifting lazily by. The forest seems peaceful and inviting yet mysterious and full of secrets. You feel a sense of adventure and excitement as you contemplate what lies ahead on your journey through this beautiful wilderness.", "As you step off the old steam boat, you find yourself at the edge of a dense forest. The tall trees are covered in moss and vines, and the forest floor is a carpet of fallen leaves and twigs. The sound of chirping birds and rustling leaves fill the air, and you can see small patches of wildflowers blooming in the sunlight that filters through the canopy. A small path leads deeper into the forest, lined with trees and the occasional fern. The sound of a stream can be heard in the distance, and the faint smell of wood smoke hangs in the air. Beyond the forest, you can see rolling hills and mountains in the distance, and the sky above is a deep shade of blue with the occasional cloud drifting lazily by. The forest seems peaceful and inviting yet mysterious and full of secrets. You feel a sense of adventure and excitement as you contemplate what lies ahead on your journey through this beautiful wilderness."], [], [W], [], 11, 3, []),
            Location(10, ["You see a chest. ", "You see a chest. ", "You see a chest. ",
                     "You see a chest. "], [], [N, S], [], 4, 6, []),
            Location(11, ["You've arrived in a village", "You've arrived in a village",
                     "You've arrived in a village", "You've arrived in a village"], [], [N, S], [], 7, 6, []),
            Location(12, ["You're at the entrance to a cave", "You're at the entrance to a cave",
                     "You're at the entrance to a cave", "You're at the entrance to a cave"], [], [N, E, S, W], [], 4, 8, []),
            Location(13, ["You are in a village. ", "You are in a village. ",
                     "You are in a village. ", "You are in a village. "], [], [N], [], 0, 9, []),
            Location(14, ["You are in a field", "You are in a field", "You are in a field",
                     "You are in a field"], [], [N, E, S, W], [], 3, 13, []),
            Location(15, ["You've arrived in a village", "You've arrived in a village",
                     "You've arrived in a village", "You've arrived in a village"], [], [N], [], 1, 15, []),
            Location(16, ["You are on a bridge.", "You are on a bridge.",
                     "You are on a bridge.", "You are on a bridge."], [], [W, E], [], 9, 8, []),
            Location(17, ["You are on a bridge and there's a troll!", "You are on a bridge and there's a troll!",
                     "You are on a bridge and there's a troll!", "You are on a bridge and there's a troll!"], [], [N, S], [], 3, 17, []),
        ]
        
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
