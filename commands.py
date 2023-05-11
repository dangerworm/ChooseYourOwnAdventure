from game_response import GameResponse

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

def go(game, direction):
  dx, dy = 0, 0
  if direction.lower() == 'n':
    dy = -1
  elif direction.lower() == 'ne':
    dx = 1
    dy = -1
  elif direction.lower() == 'e':
    dx = 1
  elif direction.lower() == 'se':
    dx = 1
    dy = 1
  elif direction.lower() == 's':
    dy = 1
  elif direction.lower() == 'sw':
    dx = -1
    dy = 1
  elif direction.lower() == 'w':
    dx = -1
  elif direction.lower() == 'nw':
    dy = -1
    dx = -1

  x = game.player.location.x + dx
  y = game.player.location.y + dy

  if (x < 0 or x > len(game.locations[0]) - 1 or y < 0 or y > len(game.locations) - 1):
    return GameResponse(game.player.id, 'You cannot go that way.', None)

  game.player.location = game.locations[y][x]

  return GameResponse(game.player.id, game.player.location.name, None)

def help():
    #list commands
    pass

def inventory(game):
    pass

def load(game):
    pass

def look(game):
  return GameResponse(game.player.id, game.player.location.description, None)

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
