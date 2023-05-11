from game_response import GameResponse
from game import DIRECTIONS, N, S, E, W

def run_command(game, command, arguments):
  if command == 'attack':
    return attack(game, arguments)
  elif command == 'cast':
    return cast(game, arguments)
  elif command == 'drop':
    return drop(game, arguments)
  elif command == 'equip':
    return equip(game, arguments)
  elif command == 'go':
    return go(game, arguments)
  elif command == 'help':
     return help()
  elif command == 'inventory':
     return inventory(game)
  elif command == 'load':
     return load(game)
  elif command == 'look':
     return look(game)
  elif command == 'quit':
     return quit(game)
  elif command == 'save':
     return save(game)
  elif command == 'take':
     return take(game, arguments)
  elif command == 'unequip':
     return unequip(game, arguments)
  elif command == 'use':
     return use(game, arguments)

def attack(game, target):
    pass

def cast(game, spell):
    pass

def drop(game, item):
    pass

def equip(game, item):
    pass

def go(game, arguments):
  direction = arguments[0]
  
  if direction not in game.player.location.exits:
    return GameResponse(game.player.id, 'You cannot go that way.', None)
  
  x_values = [location.x for location in game.locations]
  y_values = [location.y for location in game.locations]

  x_values = x_values.sort()
  y_values = y_values.sort()

  x_index = x_values.index(game.player.location.x)
  y_index = y_values.index(game.player.location.y)

  if direction == N:
    y_index -= 1
  elif direction == E:
    x_index += 1
  elif direction == S:
    y_index += 1
  elif direction == W:
    x_index -= 1

  game.player.location = [location for location in game.locations if location.x == x_values[x_index] and location.y == y_values[y_index]][0]

  return GameResponse(game.player.id, game.player.location.location_summary(game.time_of_day), None)

def help():
    #list commands
    pass

def inventory(game):
    pass

def load(game):
    pass

def look(game):
  return GameResponse(game.player.id, game.player.location, None)

def quit(game):
    pass

def save(game):
    pass

def take(game, item):
    pass

def unequip(game, item):
    pass

def use(game, item):
    pass
