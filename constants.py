N = 0
E = 1
S = 2
W = 3

MORNING = 0
AFTERNOON = 1
EVENING = 2
NIGHT = 3

DIRECTIONS = {
    0: 'north',
    1: 'east',
    2: 'south',
    3: 'west'
}

DIRECTION_NAMES = {
    'north': 0,
    'east': 1,
    'south': 2,
    'west': 3
}

#Number below represents the number of arguments
POSSIBLE_COMMANDS = {
   'attack': 2,
   'cast': 2,
   'drop': 1,
   'equip': 1,
   'go': 1,
   'walk': 1,
   'move': 1,
   'visit': 1,
   'help': 0,
   'inventory': 0,
   'investigate': 1,
   'load': 0,
   'look': 0,
   'quit': 0,
   'save': 0,
   'take': 1,
   'pick up': 1,
   'unequip': 1,
   'use': 1,
}